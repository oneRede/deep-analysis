#!/usr/bin/env python3
"""
快速测试RSS聚合器 - 只抓取少量文章
"""

import os
os.environ['DEEPSEEK_API_KEY'] = 'sk-47f4bcaec20a436399ac7674e7f15c0b'

import sys
from pathlib import Path

# 添加脚本目录到路径
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

# 导入所需模块
import feedparser
import yaml
from datetime import datetime

print("=" * 60)
print("快速测试RSS聚合器")
print("=" * 60)
print()

# 测试单个feed
feed_url = "https://export.arxiv.org/rss/cs.AI"
print(f"测试抓取: {feed_url}")

feed = feedparser.parse(feed_url)
print(f"   找到 {len(feed.entries)} 篇文章")

# 只取前3篇
test_articles = []
for entry in feed.entries[:3]:
    article = {
        'title': entry.get('title', 'Untitled'),
        'url': entry.get('link', ''),
        'summary': entry.get('summary', entry.get('description', ''))[:500],
        'source': 'arXiv cs.AI',
        'tier': 'tier1'
    }
    test_articles.append(article)
    print(f"   • {article['title'][:60]}...")

print()
print(f"准备测试 {len(test_articles)} 篇文章的AI分析...")
print()

# 导入并测试RSSAggregator
from rss_aggregator import RSSAggregator

ROOT_DIR = SCRIPT_DIR.parent
CONFIG_FILE = ROOT_DIR / "config" / "feeds.yml"

agg = RSSAggregator(CONFIG_FILE)

print()
print("批量生成AI摘要和分类...")
results = agg._generate_ai_summaries_batch(test_articles)

print()
print("结果:")
print("-" * 60)
for i, (article, (ai_summary, category)) in enumerate(zip(test_articles, results), 1):
    print(f"\n{i}. {article['title'][:60]}...")
    if ai_summary:
        print(f"   摘要: {ai_summary}")
    else:
        print(f"   摘要: (未生成)")

    if category:
        category_name = agg.category_key_to_name.get(category, category)
        print(f"   分类: {category_name} ({category})")
    else:
        print(f"   分类: (未分类)")

print()
print("=" * 60)
print("测试完成")
print("=" * 60)
