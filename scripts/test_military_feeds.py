#!/usr/bin/env python3
"""
测试军事新闻源的RSS和爬虫功能
"""

import feedparser
from military_scraper import scrape_military_sources

def test_rss_feeds():
    """测试RSS源"""
    print("\n" + "="*60)
    print("📡 测试军事RSS源")
    print("="*60 + "\n")

    feeds = [
        ('Defense News', 'https://www.defensenews.com/m/rss/'),
        ('Military Times', 'https://www.militarytimes.com/m/rss/'),
        ('Breaking Defense', 'https://breakingdefense.com/full-rss-feed/?v=2'),
        ('Stars and Stripes', 'https://subscribe.stripes.com/rss'),
        ('TASS', 'http://tass.com/rss/v2.xml'),
        ('Military.com', 'https://www.military.com/feed/'),
        ('The War Zone', 'https://www.twz.com/feed'),
    ]

    total = 0
    working = []

    for name, url in feeds:
        try:
            feed = feedparser.parse(url)
            count = len(feed.entries)

            if count > 0:
                print(f'✅ {name}: {count} 篇文章')
                if feed.entries:
                    print(f'   最新: {feed.entries[0].title[:70]}')
                working.append(name)
                total += count
            else:
                print(f'⚠️  {name}: 0 篇文章 (可能需要检查URL)')

        except Exception as e:
            print(f'❌ {name}: {str(e)[:50]}')

        print()

    print(f"\n总计: {len(working)}/{len(feeds)} 个源正常工作，共 {total} 篇文章\n")
    return working

def test_scrapers():
    """测试爬虫"""
    print("\n" + "="*60)
    print("🕷️  测试网页爬虫")
    print("="*60 + "\n")

    articles = scrape_military_sources(days_lookback=7)

    print(f"\n爬虫获取: {len(articles)} 篇文章")

    if articles:
        print("\n示例文章（前3篇）:")
        for i, article in enumerate(articles[:3], 1):
            print(f"\n{i}. {article['title'][:80]}")
            print(f"   来源: {article['source']}")
            print(f"   URL: {article['url'][:80]}")

    return articles

def main():
    print("\n" + "="*60)
    print("🎯 军事新闻源测试")
    print("="*60)

    # 测试RSS
    rss_sources = test_rss_feeds()

    # 测试爬虫
    scraped_articles = test_scrapers()

    # 总结
    print("\n" + "="*60)
    print("📊 测试总结")
    print("="*60)
    print(f"\n✅ RSS源工作正常: {len(rss_sources)} 个")
    print(f"✅ 爬虫获取文章: {len(scraped_articles)} 篇")
    print(f"\n推荐使用RSS的源: {', '.join(rss_sources)}")
    print("\n💡 提示: RSS源可以获取更多元数据（日期、摘要等），优先使用RSS")

if __name__ == "__main__":
    main()
