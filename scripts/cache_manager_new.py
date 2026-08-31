#!/usr/bin/env python3
"""
缓存管理器 - 每天一个缓存文件
用途：管理RSS聚合器的URL缓存，避免单文件过大
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Set, List
import os


class CacheManager:
    """分布式缓存管理器 - 每天一个文件"""

    def __init__(self, cache_dir: Path):
        """
        初始化缓存管理器

        Args:
            cache_dir: 缓存目录路径
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # 元数据文件
        self.meta_file = self.cache_dir / "cache_meta.json"
        self.meta = self._load_meta()

    def _load_meta(self) -> dict:
        """加载元数据"""
        if self.meta_file.exists():
            with open(self.meta_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "version": "3.0",
            "created": datetime.now().isoformat(),
            "last_cleanup": None
        }

    def _save_meta(self):
        """保存元数据"""
        self.meta["last_updated"] = datetime.now().isoformat()
        with open(self.meta_file, 'w', encoding='utf-8') as f:
            json.dump(self.meta, f, indent=2, ensure_ascii=False)

    def _get_cache_file(self, date_str: str) -> Path:
        """获取指定日期的缓存文件路径"""
        return self.cache_dir / f"cache_{date_str}.json"

    def add_urls(self, date_str: str, urls: List[str]):
        """
        添加URL到指定日期的缓存

        Args:
            date_str: 日期字符串 (YYYY-MM-DD)
            urls: URL列表
        """
        cache_file = self._get_cache_file(date_str)

        # 读取现有缓存
        existing_urls = set()
        if cache_file.exists():
            with open(cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                existing_urls = set(data.get('urls', []))

        # 合并新URL
        existing_urls.update(urls)

        # 保存
        data = {
            "date": date_str,
            "urls": sorted(list(existing_urls)),
            "count": len(existing_urls),
            "updated": datetime.now().isoformat()
        }

        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_urls(self, date_str: str) -> Set[str]:
        """
        获取指定日期的缓存URL

        Args:
            date_str: 日期字符串 (YYYY-MM-DD)

        Returns:
            URL集合
        """
        cache_file = self._get_cache_file(date_str)

        if not cache_file.exists():
            return set()

        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return set(data.get('urls', []))
        except Exception as e:
            print(f"⚠️  读取缓存文件失败 {date_str}: {e}")
            return set()

    def get_urls_in_range(self, days_back: int = 7, exclude_date: str = None) -> Set[str]:
        """
        获取最近N天的所有缓存URL

        Args:
            days_back: 往前追溯的天数
            exclude_date: 要排除的日期字符串(YYYY-MM-DD)，防止同一天多次运行时的重复去重

        Returns:
            URL集合
        """
        all_urls = set()

        today = datetime.now()

        for i in range(days_back + 1):
            date = today - timedelta(days=i)
            date_str = date.strftime('%Y-%m-%d')

            # 跳过要排除的日期
            if exclude_date and date_str == exclude_date:
                continue

            all_urls.update(self.get_urls(date_str))

        return all_urls

    def cleanup_old_caches(self, keep_days: int = 30) -> int:
        """
        清理超过指定天数的缓存文件

        Args:
            keep_days: 保留最近多少天的缓存

        Returns:
            删除的文件数
        """
        cutoff_date = datetime.now() - timedelta(days=keep_days)
        cutoff_str = cutoff_date.strftime('%Y-%m-%d')

        deleted = 0
        total_urls = 0

        # 遍历缓存目录
        for cache_file in self.cache_dir.glob('cache_*.json'):
            # 从文件名提取日期
            filename = cache_file.stem  # cache_2026-08-31
            date_str = filename.replace('cache_', '')

            if date_str < cutoff_str:
                # 读取URL数量（用于统计）
                try:
                    with open(cache_file, 'r') as f:
                        data = json.load(f)
                        total_urls += data.get('count', 0)
                except:
                    pass

                # 删除文件
                cache_file.unlink()
                deleted += 1

        if deleted > 0:
            print(f"  🧹 清理了 {deleted} 个旧缓存文件（{total_urls} 个 URL）")
            print(f"     保留范围: {cutoff_str} 至今")

            self.meta["last_cleanup"] = datetime.now().isoformat()
            self._save_meta()

        return deleted

    def get_statistics(self) -> dict:
        """
        获取缓存统计信息

        Returns:
            统计信息字典
        """
        cache_files = list(self.cache_dir.glob('cache_*.json'))

        total_files = len(cache_files)
        total_urls = 0
        dates = []

        for cache_file in cache_files:
            try:
                with open(cache_file, 'r') as f:
                    data = json.load(f)
                    total_urls += data.get('count', 0)
                    date = data.get('date')
                    if date:  # 只添加非空日期
                        dates.append(date)
            except:
                pass

        return {
            "total_files": total_files,
            "total_urls": total_urls,
            "date_range": f"{min(dates)} 至 {max(dates)}" if dates else "无数据",
            "cache_dir": str(self.cache_dir)
        }

    def migrate_from_old_cache(self, old_cache_file: Path):
        """
        从旧的单文件缓存迁移到新的分布式缓存

        Args:
            old_cache_file: 旧缓存文件路径
        """
        if not old_cache_file.exists():
            print("  ℹ️  旧缓存文件不存在，无需迁移")
            return

        print("  🔄 开始迁移旧缓存...")

        with open(old_cache_file, 'r', encoding='utf-8') as f:
            old_cache = json.load(f)

        # 处理 version 2.0 格式
        if "by_date" in old_cache:
            migrated_dates = 0
            migrated_urls = 0

            for date_str, urls in old_cache["by_date"].items():
                self.add_urls(date_str, urls)
                migrated_dates += 1
                migrated_urls += len(urls)

            print(f"  ✅ 迁移完成: {migrated_dates} 天, {migrated_urls} 个URL")

            # 备份旧文件
            backup_file = old_cache_file.with_suffix('.json.backup')
            old_cache_file.rename(backup_file)
            print(f"  💾 旧缓存已备份至: {backup_file}")

        # 处理旧格式 (processed_urls列表)
        elif "processed_urls" in old_cache:
            yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
            urls = old_cache["processed_urls"]
            self.add_urls(yesterday, urls)
            print(f"  ✅ 迁移完成: {len(urls)} 个URL → {yesterday}")

            backup_file = old_cache_file.with_suffix('.json.backup')
            old_cache_file.rename(backup_file)
            print(f"  💾 旧缓存已备份至: {backup_file}")

        self._save_meta()


def main():
    """命令行工具 - 用于维护缓存"""
    import argparse

    parser = argparse.ArgumentParser(description='RSS缓存管理工具')
    parser.add_argument('--cache-dir', default='scripts/.cache',
                       help='缓存目录路径')
    parser.add_argument('--cleanup', type=int, metavar='DAYS',
                       help='清理N天前的缓存')
    parser.add_argument('--stats', action='store_true',
                       help='显示缓存统计信息')
    parser.add_argument('--migrate', metavar='OLD_FILE',
                       help='从旧缓存文件迁移')

    args = parser.parse_args()

    manager = CacheManager(Path(args.cache_dir))

    if args.migrate:
        manager.migrate_from_old_cache(Path(args.migrate))

    if args.cleanup:
        manager.cleanup_old_caches(args.cleanup)

    if args.stats:
        stats = manager.get_statistics()
        print("\n📊 缓存统计:")
        print(f"  文件数: {stats['total_files']}")
        print(f"  URL总数: {stats['total_urls']}")
        print(f"  日期范围: {stats['date_range']}")
        print(f"  缓存目录: {stats['cache_dir']}")


if __name__ == '__main__':
    main()
