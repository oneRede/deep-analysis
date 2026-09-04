#!/usr/bin/env python3
"""
OpenAI 爬虫 - 使用Playwright处理JavaScript动态渲染
"""

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import List, Dict
import time

class OpenAIPlaywrightScraper:
    def __init__(self, headless: bool = True):
        """初始化Playwright爬虫"""
        self.headless = headless

    def scrape_openai_news(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取OpenAI News页面（使用Playwright渲染JavaScript）
        """
        articles = []
        url = "https://openai.com/news"

        try:
            print(f"🕷️  爬取: OpenAI News ({url})")
            print(f"  使用Playwright渲染JavaScript...")

            with sync_playwright() as p:
                # 启动浏览器
                browser = p.chromium.launch(headless=self.headless)
                context = browser.new_context(
                    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                )
                page = context.new_page()

                # 访问页面（使用更宽松的等待条件）
                try:
                    print(f"  正在访问页面...")
                    page.goto(url, wait_until='domcontentloaded', timeout=60000)

                    # 等待Cloudflare验证完成（检查特定元素或等待足够长的时间）
                    print(f"  等待Cloudflare验证...")
                    time.sleep(10)  # 给Cloudflare足够时间完成验证

                    # 检查是否还在Cloudflare页面
                    if "Just a moment" in page.content():
                        print(f"  ⚠️  仍在Cloudflare验证页面，再等待...")
                        time.sleep(10)

                except Exception as e:
                    print(f"  ⚠️  页面加载警告: {str(e)}")
                    # 继续执行，可能部分内容已加载

                # 等待内容加载
                print(f"  等待页面渲染...")
                time.sleep(5)  # 额外等待，确保动态内容加载完成

                # 获取渲染后的HTML
                content = page.content()
                browser.close()

            # 解析HTML
            soup = BeautifulSoup(content, 'html.parser')
            cutoff_date = datetime.now() - timedelta(days=days_lookback)

            # 查找所有包含 /news/ 的链接
            all_links = soup.find_all('a', href=True)
            seen_urls = set()

            for link_tag in all_links:
                try:
                    href = link_tag.get('href', '')

                    # 只保留 /news/ 路径且不是主页
                    if '/news/' not in href or href in ['/news', '/news/']:
                        continue

                    # 构建完整URL
                    if href.startswith('/'):
                        full_url = f"https://openai.com{href}"
                    elif href.startswith('http'):
                        full_url = href
                    else:
                        continue

                    # 去重
                    if full_url in seen_urls:
                        continue
                    seen_urls.add(full_url)

                    # 提取标题
                    title = link_tag.get_text(strip=True)
                    if not title or len(title) < 10:
                        # 尝试从父元素获取
                        parent = link_tag.parent
                        if parent:
                            title_elem = parent.find(['h1', 'h2', 'h3', 'h4'])
                            if title_elem:
                                title = title_elem.get_text(strip=True)

                    if not title or len(title) < 10:
                        continue

                    # 尝试提取日期
                    date_str = ""
                    parent = link_tag.parent
                    if parent:
                        # 查找time标签
                        time_elem = parent.find('time')
                        if time_elem:
                            date_str = time_elem.get_text(strip=True) or time_elem.get('datetime', '')

                    articles.append({
                        'title': title,
                        'url': full_url,
                        'summary': '',
                        'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                        'published_raw': None,
                        'source': 'OpenAI News',
                        'type': 'news',
                        'priority': 'high',
                    })

                except Exception as e:
                    continue

            print(f"✅ OpenAI News: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ 爬取 OpenAI News 失败: {str(e)}")

        return articles

    def scrape_openai_research(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取OpenAI Research页面
        """
        articles = []
        url = "https://openai.com/research"

        try:
            print(f"🕷️  爬取: OpenAI Research ({url})")
            print(f"  使用Playwright渲染JavaScript...")

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=self.headless)
                context = browser.new_context(
                    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                )
                page = context.new_page()

                print(f"  正在访问页面...")
                page.goto(url, wait_until='domcontentloaded', timeout=60000)

                # 等待Cloudflare验证完成
                print(f"  等待Cloudflare验证...")
                time.sleep(10)

                # 检查是否还在Cloudflare页面
                if "Just a moment" in page.content():
                    print(f"  ⚠️  仍在Cloudflare验证页面，再等待...")
                    time.sleep(10)

                print(f"  等待页面渲染...")
                time.sleep(3)

                content = page.content()
                browser.close()

            soup = BeautifulSoup(content, 'html.parser')
            cutoff_date = datetime.now() - timedelta(days=days_lookback)

            all_links = soup.find_all('a', href=True)
            seen_urls = set()

            for link_tag in all_links:
                try:
                    href = link_tag.get('href', '')

                    if '/research/' not in href or href in ['/research', '/research/']:
                        continue

                    if href.startswith('/'):
                        full_url = f"https://openai.com{href}"
                    elif href.startswith('http'):
                        full_url = href
                    else:
                        continue

                    if full_url in seen_urls:
                        continue
                    seen_urls.add(full_url)

                    title = link_tag.get_text(strip=True)
                    if not title or len(title) < 10:
                        parent = link_tag.parent
                        if parent:
                            title_elem = parent.find(['h1', 'h2', 'h3', 'h4'])
                            if title_elem:
                                title = title_elem.get_text(strip=True)

                    if not title or len(title) < 10:
                        continue

                    date_str = ""
                    parent = link_tag.parent
                    if parent:
                        time_elem = parent.find('time')
                        if time_elem:
                            date_str = time_elem.get_text(strip=True) or time_elem.get('datetime', '')

                    articles.append({
                        'title': title,
                        'url': full_url,
                        'summary': '',
                        'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                        'published_raw': None,
                        'source': 'OpenAI Research',
                        'type': 'research',
                        'priority': 'high',
                    })

                except Exception as e:
                    continue

            print(f"✅ OpenAI Research: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ 爬取 OpenAI Research 失败: {str(e)}")

        return articles

    def scrape_all(self, days_lookback: int = 7) -> List[Dict]:
        """爬取所有OpenAI页面"""
        articles = []
        articles.extend(self.scrape_openai_news(days_lookback))
        articles.extend(self.scrape_openai_research(days_lookback))
        return articles


if __name__ == "__main__":
    """测试脚本"""
    print("\n🧪 测试OpenAI Playwright爬虫\n")

    scraper = OpenAIPlaywrightScraper(headless=True)
    articles = scraper.scrape_all(days_lookback=30)

    print(f"\n📊 总结:")
    print(f"  总计: {len(articles)} 篇文章")

    if articles:
        print(f"\n前5篇文章:")
        for i, article in enumerate(articles[:5], 1):
            print(f"\n{i}. {article['title']}")
            print(f"   来源: {article['source']}")
            print(f"   URL: {article['url']}")
            if article['published']:
                print(f"   日期: {article['published']}")

    print("\n✅ 测试完成!")
