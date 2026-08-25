#!/usr/bin/env python3
"""
简化版RSS聚合器测试 - 只处理少量文章
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# 设置环境变量
os.environ['DEEPSEEK_API_KEY'] = 'sk-47f4bcaec20a436399ac7674e7f15c0b'

# 切换到项目根目录
ROOT_DIR = Path(__file__).parent
os.chdir(ROOT_DIR)
sys.path.insert(0, str(ROOT_DIR / 'scripts'))

print("=" * 60)
print("简化版RSS聚合器测试")
print("=" * 60)
print()

# 动态加载模块
import importlib.util
spec = importlib.util.spec_from_file_location("rss_aggregator", ROOT_DIR / "scripts/rss-aggregator.py")
rss_module = importlib.util.module_from_spec(spec)
sys.modules["rss_aggregator"] = rss_module
spec.loader.exec_module(rss_module)

RSSAggregator = rss_module.RSSAggregator

# 初始化
config_path = ROOT_DIR / "config" / "feeds.yml"
print("初始化聚合器...")
agg = RSSAggregator(config_path)
print()

# 手动创建几篇测试文章
test_articles = [
    {
        'title': 'GPT-5: Next Generation Language Model with Enhanced Reasoning',
        'url': 'https://example.com/gpt5',
        'summary': 'This paper introduces GPT-5, a next-generation language model with significantly improved reasoning capabilities, larger context window, and better multilingual support.',
        'source': 'Test Source',
        'tier': 'tier1',
        'published': datetime.now().strftime('%Y-%m-%d'),
        'type': 'paper'
    },
    {
        'title': '基于Transformer的机器人控制系统研究',
        'url': 'https://example.com/robot',
        'summary': '本文提出了一种基于Transformer架构的机器人控制系统，能够实现复杂任务的自主学习和执行。',
        'source': 'Test Source',
        'tier': 'tier2',
        'published': datetime.now().strftime('%Y-%m-%d'),
        'type': 'paper'
    },
    {
        'title': 'New AI Chip Achieves 10x Performance Improvement',
        'url': 'https://example.com/chip',
        'summary': 'A breakthrough in AI chip design delivers 10x performance improvement over previous generation, enabling faster model training and inference.',
        'source': 'Test Source',
        'tier': 'tier1',
        'published': datetime.now().strftime('%Y-%m-%d'),
        'type': 'news'
    }
]

print(f"测试文章数量: {len(test_articles)}")
for i, article in enumerate(test_articles, 1):
    print(f"  {i}. {article['title']}")
print()

# 批量生成摘要和分类
print("生成AI摘要和分类...")
results = agg._generate_ai_summaries_batch(test_articles)

# 应用结果
for article, (ai_summary, category) in zip(test_articles, results):
    if ai_summary:
        article['ai_summary'] = ai_summary
    if category:
        article['category'] = category

print()
print("=" * 60)
print("测试结果")
print("=" * 60)
print()

for i, article in enumerate(test_articles, 1):
    print(f"{i}. {article['title']}")
    print(f"   来源: {article['source']}")

    if article.get('ai_summary'):
        print(f"   ✅ AI摘要: {article['ai_summary']}")
    else:
        print(f"   ❌ AI摘要: 未生成")

    if article.get('category'):
        cat_name = agg.category_key_to_name.get(article['category'], article['category'])
        print(f"   ✅ 分类: {cat_name} ({article['category']})")
    else:
        print(f"   ❌ 分类: 未分类")

    print()

# 统计
success_summary = sum(1 for a in test_articles if a.get('ai_summary'))
success_category = sum(1 for a in test_articles if a.get('category'))

print("=" * 60)
print(f"✅ AI摘要成功率: {success_summary}/{len(test_articles)}")
print(f"✅ 分类成功率: {success_category}/{len(test_articles)}")
print("=" * 60)

if success_summary == len(test_articles) and success_category == len(test_articles):
    print("\n🎉 所有测试通过！RSS聚合器工作正常")
    sys.exit(0)
else:
    print("\n⚠️  部分测试失败")
    sys.exit(1)
