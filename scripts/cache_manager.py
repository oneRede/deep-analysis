#!/usr/bin/env python3
"""
缓存管理工具
用途：查看、统计、清理按日期组织的 RSS 缓存
"""

import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta

CACHE_FILE = Path(__file__).parent / ".rss-cache.json"

def load_cache():
    """加载缓存"""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_cache(cache):
    """保存缓存"""
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def show_stats(cache):
    """显示缓存统计"""
    if not cache or 'by_date' not in cache:
        print("❌ 缓存文件不存在或格式错误")
        return

    print("\n" + "="*60)
    print("📊 RSS 缓存统计")
    print("="*60)

    by_date = cache['by_date']

    if not by_date:
        print("\n缓存为空")
        return

    # 按日期排序
    sorted_dates = sorted(by_date.keys())

    print(f"\n版本: {cache.get('version', '未知')}")
    print(f"最后运行: {cache.get('last_run', '未知')}")
    print(f"\n日期范围: {sorted_dates[0]} 至 {sorted_dates[-1]}")
    print(f"总天数: {len(sorted_dates)} 天")

    # 统计总 URL 数
    total_urls = sum(len(urls) for urls in by_date.values())
    print(f"总 URL 数: {total_urls} 个")

    # 按日期显示
    print("\n" + "-"*60)
    print("按日期统计:")
    print("-"*60)

    for date_str in sorted_dates:
        count = len(by_date[date_str])
        # 计算天数
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        days_ago = (datetime.now() - date_obj).days

        if days_ago == 0:
            days_str = "(今天)"
        elif days_ago == 1:
            days_str = "(昨天)"
        else:
            days_str = f"({days_ago}天前)"

        print(f"  {date_str} {days_str:12s}: {count:4d} 个 URL")

    print("-"*60)

def show_details(cache, date_str):
    """显示指定日期的详细信息"""
    if not cache or 'by_date' not in cache:
        print("❌ 缓存文件不存在或格式错误")
        return

    if date_str not in cache['by_date']:
        print(f"❌ 未找到 {date_str} 的缓存")
        print(f"\n可用日期: {', '.join(sorted(cache['by_date'].keys()))}")
        return

    urls = cache['by_date'][date_str]

    print("\n" + "="*60)
    print(f"📄 {date_str} 的缓存详情")
    print("="*60)
    print(f"\n共 {len(urls)} 个 URL:\n")

    for i, url in enumerate(urls[:50], 1):  # 只显示前50个
        print(f"  {i:3d}. {url}")

    if len(urls) > 50:
        print(f"\n  ... 还有 {len(urls) - 50} 个 URL 未显示")

def cleanup(cache, keep_days):
    """清理超过指定天数的缓存"""
    if not cache or 'by_date' not in cache:
        print("❌ 缓存文件不存在或格式错误")
        return

    cutoff_date = datetime.now() - timedelta(days=keep_days)
    cutoff_str = cutoff_date.strftime('%Y-%m-%d')

    dates_to_remove = []
    for date_str in cache['by_date'].keys():
        if date_str < cutoff_str:
            dates_to_remove.append(date_str)

    if not dates_to_remove:
        print(f"\n✅ 无需清理（所有缓存都在 {keep_days} 天内）")
        return

    print("\n" + "="*60)
    print(f"🧹 清理超过 {keep_days} 天的缓存")
    print("="*60)

    total_urls_removed = 0
    for date_str in dates_to_remove:
        urls_count = len(cache['by_date'][date_str])
        total_urls_removed += urls_count
        print(f"  删除: {date_str} ({urls_count} 个 URL)")
        del cache['by_date'][date_str]

    print("\n" + "-"*60)
    print(f"总计删除: {len(dates_to_remove)} 天，{total_urls_removed} 个 URL")
    print(f"保留范围: {cutoff_str} 至今")
    print("-"*60)

    # 保存更新后的缓存
    save_cache(cache)
    print("\n✅ 缓存已更新")

def remove_date(cache, date_str):
    """删除指定日期的缓存"""
    if not cache or 'by_date' not in cache:
        print("❌ 缓存文件不存在或格式错误")
        return

    if date_str not in cache['by_date']:
        print(f"❌ 未找到 {date_str} 的缓存")
        return

    urls_count = len(cache['by_date'][date_str])
    del cache['by_date'][date_str]

    save_cache(cache)

    print(f"\n✅ 已删除 {date_str} 的缓存（{urls_count} 个 URL）")

def main():
    parser = argparse.ArgumentParser(
        description='RSS 缓存管理工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 查看统计
  python3 cache_manager.py stats

  # 查看指定日期的详情
  python3 cache_manager.py details 2026-08-23

  # 清理超过30天的缓存
  python3 cache_manager.py cleanup --days 30

  # 删除指定日期的缓存
  python3 cache_manager.py remove 2026-08-20
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='命令')

    # stats 命令
    subparsers.add_parser('stats', help='显示缓存统计')

    # details 命令
    details_parser = subparsers.add_parser('details', help='显示指定日期的详细信息')
    details_parser.add_argument('date', help='日期 (格式: YYYY-MM-DD)')

    # cleanup 命令
    cleanup_parser = subparsers.add_parser('cleanup', help='清理旧缓存')
    cleanup_parser.add_argument('--days', type=int, default=30,
                                help='保留最近多少天的缓存（默认30天）')
    cleanup_parser.add_argument('--yes', '-y', action='store_true',
                                help='跳过确认直接删除')

    # remove 命令
    remove_parser = subparsers.add_parser('remove', help='删除指定日期的缓存')
    remove_parser.add_argument('date', help='日期 (格式: YYYY-MM-DD)')
    remove_parser.add_argument('--yes', '-y', action='store_true',
                                help='跳过确认直接删除')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # 加载缓存
    cache = load_cache()

    if args.command == 'stats':
        show_stats(cache)

    elif args.command == 'details':
        show_details(cache, args.date)

    elif args.command == 'cleanup':
        if not args.yes:
            show_stats(cache)
            print(f"\n⚠️  将删除超过 {args.days} 天的缓存")
            confirm = input("\n确认删除? (yes/no): ")
            if confirm.lower() != 'yes':
                print("❌ 已取消")
                return

        cleanup(cache, args.days)

    elif args.command == 'remove':
        if not args.yes:
            show_details(cache, args.date)
            print(f"\n⚠️  将删除 {args.date} 的缓存")
            confirm = input("\n确认删除? (yes/no): ")
            if confirm.lower() != 'yes':
                print("❌ 已取消")
                return

        remove_date(cache, args.date)

if __name__ == "__main__":
    main()
