#!/usr/bin/env python3
"""测试新的缓存系统"""

import json
from pathlib import Path
from datetime import datetime, timedelta

CACHE_FILE = Path("/Users/rede/Git/deep_analysis/scripts/.rss-cache.json")

print("="*60)
print("测试缓存系统")
print("="*60)

# 1. 读取当前缓存
if CACHE_FILE.exists():
    with open(CACHE_FILE, 'r') as f:
        cache = json.load(f)

    print(f"\n当前缓存格式:")
    print(f"  版本: {cache.get('version', '未知')}")

    # 检查是否是旧格式
    if isinstance(cache.get('processed_urls'), list):
        print(f"  ⚠️  检测到旧格式")
        print(f"  URL 总数: {len(cache['processed_urls'])}")
        print(f"\n  前5个 URL:")
        for url in cache['processed_urls'][:5]:
            print(f"    - {url}")

    # 检查是否是新格式
    elif 'by_date' in cache:
        print(f"  ✅ 新格式（按日期组织）")
        print(f"\n  缓存统计:")

        total_urls = 0
        for date_str, urls in sorted(cache['by_date'].items()):
            count = len(urls)
            total_urls += count
            print(f"    {date_str}: {count} 个 URL")

        print(f"\n  总计: {total_urls} 个 URL，跨 {len(cache['by_date'])} 天")

        if cache['by_date']:
            print(f"  日期范围: {min(cache['by_date'].keys())} 至 {max(cache['by_date'].keys())}")

    print(f"\n  最后运行: {cache.get('last_run', '未知')}")

else:
    print("\n⚠️  缓存文件不存在")

print("\n" + "="*60)
