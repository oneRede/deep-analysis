#!/usr/bin/env python3
"""
测试 OpenAI 和 Anthropic 爬虫修复
"""

import sys
sys.path.insert(0, '/Users/rede/Git/deep_analysis/scripts')

from web_scraper import WebScraper

def test_anthropic():
    """测试Anthropic Research爬取"""
    print("=" * 60)
    print("测试: Anthropic Research")
    print("=" * 60)

    scraper = WebScraper()
    articles = scraper.scrape_anthropic_research(days_lookback=30)

    print(f"\n结果: 找到 {len(articles)} 篇文章")
    if articles:
        print("\n前5篇文章:")
        for i, article in enumerate(articles[:5], 1):
            print(f"{i}. {article['title']}")
            print(f"   URL: {article['url']}")
            print(f"   日期: {article['published']}")
            print()
    else:
        print("⚠️  没有找到文章，可能需要进一步调试")
    print()

def test_openai():
    """测试OpenAI爬取"""
    print("=" * 60)
    print("测试: OpenAI News & Research")
    print("=" * 60)

    scraper = WebScraper()
    articles = scraper.scrape_openai_blog(days_lookback=30)

    print(f"\n结果: 找到 {len(articles)} 篇文章")
    if articles:
        print("\n前5篇文章:")
        for i, article in enumerate(articles[:5], 1):
            print(f"{i}. {article['title']}")
            print(f"   URL: {article['url']}")
            print(f"   日期: {article['published']}")
            print()
    else:
        print("⚠️  没有找到文章")
        print("原因: OpenAI页面使用JavaScript动态渲染")
        print("建议: 考虑使用Selenium或Playwright获取渲染后的内容")
    print()

if __name__ == "__main__":
    print("\n🧪 开始测试 OpenAI 和 Anthropic 爬虫...\n")

    try:
        test_anthropic()
    except Exception as e:
        print(f"❌ Anthropic测试失败: {str(e)}\n")

    try:
        test_openai()
    except Exception as e:
        print(f"❌ OpenAI测试失败: {str(e)}\n")

    print("🎉 测试完成！")
