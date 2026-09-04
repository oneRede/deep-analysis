#!/usr/bin/env python3
"""
测试爬虫修复 - 验证DeepSeek和Army Technology的爬取
"""

import sys
sys.path.insert(0, '/Users/rede/Git/deep_analysis/scripts')

from web_scraper import WebScraper
from military_scraper import MilitaryScraper

def test_deepseek():
    """测试DeepSeek Blog爬取（使用curl解决SSL问题）"""
    print("=" * 60)
    print("测试 1: DeepSeek Blog")
    print("=" * 60)

    scraper = WebScraper()
    articles = scraper.scrape_deepseek_blog(days_lookback=30)

    print(f"\n结果: 找到 {len(articles)} 篇文章")
    if articles:
        print("\n前3篇文章:")
        for i, article in enumerate(articles[:3], 1):
            print(f"{i}. {article['title']}")
            print(f"   URL: {article['url']}")
            print(f"   日期: {article['published']}")
    print()

def test_army_technology():
    """测试Army Technology爬取（使用cloudscraper绕过DataDome）"""
    print("=" * 60)
    print("测试 2: Army Technology")
    print("=" * 60)

    scraper = MilitaryScraper(days_lookback=7)
    articles = scraper.scrape_army_technology()

    print(f"\n结果: 找到 {len(articles)} 篇文章")
    if articles:
        print("\n前3篇文章:")
        for i, article in enumerate(articles[:3], 1):
            print(f"{i}. {article['title']}")
            print(f"   URL: {article['url']}")
    print()

if __name__ == "__main__":
    print("\n🧪 开始测试爬虫修复...\n")

    try:
        test_deepseek()
    except Exception as e:
        print(f"❌ DeepSeek测试失败: {str(e)}\n")

    try:
        test_army_technology()
    except Exception as e:
        print(f"❌ Army Technology测试失败: {str(e)}\n")

    print("🎉 测试完成！")
