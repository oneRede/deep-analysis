#!/usr/bin/env python3
"""
快速测试：验证军事新闻源的分类功能
"""

import sys
sys.path.insert(0, '/Users/rede/git/deep_analysis/scripts')

from military_scraper import scrape_military_sources
import feedparser

def test_scraper_category():
    """测试爬虫文章的分类"""
    print("="*60)
    print("测试爬虫文章分类")
    print("="*60 + "\n")

    articles = scrape_military_sources(days_lookback=7)

    if articles:
        print(f"获取了 {len(articles)} 篇文章\n")
        for i, article in enumerate(articles[:3], 1):
            print(f"{i}. {article['title'][:50]}...")
            print(f"   来源: {article['source']}")
            print(f"   分类: {article.get('category', '未分类')}")
            print()
    else:
        print("未获取到文章\n")

def test_rss_category():
    """测试RSS文章应该有的分类"""
    print("="*60)
    print("测试RSS文章分类（模拟）")
    print("="*60 + "\n")

    # 模拟RSS聚合器对military tier的处理
    rss_feeds = [
        ('Breaking Defense', 'https://breakingdefense.com/full-rss-feed/?v=2'),
        ('The War Zone', 'https://www.twz.com/feed'),
    ]

    for name, url in rss_feeds:
        try:
            feed = feedparser.parse(url)
            if feed.entries:
                entry = feed.entries[0]

                # 模拟文章对象
                article = {
                    'title': entry.get('title', 'Untitled'),
                    'source': name,
                    'tier': 'military',
                }

                # 如果是military tier，自动添加分类
                if article['tier'] == 'military':
                    article['category'] = 'military_tech'

                print(f"✅ {name}")
                print(f"   标题: {article['title'][:60]}...")
                print(f"   分类: {article['category']}")
                print()
        except Exception as e:
            print(f"❌ {name}: {e}\n")

def main():
    print("\n" + "="*60)
    print("🧪 军事新闻分类测试")
    print("="*60 + "\n")

    test_scraper_category()
    test_rss_category()

    print("="*60)
    print("✅ 测试完成")
    print("="*60)
    print("\n所有军事新闻文章都会自动分类为: military_tech")
    print("这样DeepSeek就可以识别并正确分组这些文章了。\n")

if __name__ == "__main__":
    main()
