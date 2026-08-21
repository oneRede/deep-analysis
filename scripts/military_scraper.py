#!/usr/bin/env python3
"""
军事新闻网站爬虫 - 处理没有RSS的军事媒体
支持的网站：
- Jane's Defence (janes.com)
- Army Technology (army-technology.com)
- 环球网军事 (mil.huanqiu.com)
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import List, Dict
import time
import re

class MilitaryScraper:
    def __init__(self, days_lookback: int = 7):
        self.days_lookback = days_lookback
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        self.cutoff_date = datetime.now() - timedelta(days=days_lookback)

    def scrape_janes(self) -> List[Dict]:
        """爬取 Jane's Defence 文章"""
        print("📡 爬取: Jane's Defence")
        articles = []

        try:
            url = "https://www.janes.com"
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # 查找文章链接
            article_links = soup.find_all('a', href=re.compile(r'/defence-|/article/'))

            seen_urls = set()
            for link in article_links[:10]:  # 限制前10篇
                href = link.get('href', '')
                if not href.startswith('http'):
                    href = f"https://www.janes.com{href}"

                if href in seen_urls:
                    continue
                seen_urls.add(href)

                title = link.get_text(strip=True)
                if len(title) < 15:  # 过滤太短的标题
                    continue

                article = {
                    'title': title,
                    'url': href,
                    'summary': '',
                    'published': datetime.now().strftime('%Y-%m-%d'),
                    'published_raw': None,
                    'source': "Jane's Defence",
                    'type': 'news',
                    'priority': 'high'
                }
                articles.append(article)

            print(f"✅ Jane's Defence: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ Jane's Defence 爬取失败: {str(e)}")

        return articles

    def scrape_army_technology(self) -> List[Dict]:
        """爬取 Army Technology 文章"""
        print("📡 爬取: Army Technology")
        articles = []

        try:
            # 尝试主页
            url = "https://www.army-technology.com/"

            # 使用更完整的headers来避免403
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }

            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # 查找文章链接 - 更宽泛的搜索
            article_links = soup.find_all('a', href=re.compile(r'/news/|/features/|/analysis/'))

            seen_urls = set()
            for link in article_links[:20]:
                href = link.get('href', '')
                if not href.startswith('http'):
                    href = f"https://www.army-technology.com{href}"

                if href in seen_urls:
                    continue
                seen_urls.add(href)

                title = link.get_text(strip=True)
                if len(title) < 15:
                    continue

                article = {
                    'title': title,
                    'url': href,
                    'summary': '',
                    'published': datetime.now().strftime('%Y-%m-%d'),
                    'published_raw': None,
                    'source': 'Army Technology',
                    'type': 'news',
                    'priority': 'medium'
                }
                articles.append(article)

            print(f"✅ Army Technology: {len(articles)} 篇文章")

        except Exception as e:
            print(f"⚠️  Army Technology 爬取失败: {str(e)}")

        return articles

    def scrape_huanqiu_military(self) -> List[Dict]:
        """爬取环球网军事频道"""
        print("📡 爬取: 环球网军事")
        articles = []

        try:
            url = "https://mil.huanqiu.com"
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()

            # 设置正确的编码
            response.encoding = response.apparent_encoding

            soup = BeautifulSoup(response.content, 'html.parser')

            # 查找文章链接 - 多种模式
            article_links = []

            # 模式1: /article/ 路径
            article_links.extend(soup.find_all('a', href=re.compile(r'/article/\w+')))

            # 模式2: 查找所有包含标题的a标签
            for link in soup.find_all('a'):
                text = link.get_text(strip=True)
                href = link.get('href', '')
                if len(text) >= 10 and 'huanqiu.com' in href:
                    article_links.append(link)

            seen_urls = set()
            seen_titles = set()

            for link in article_links[:30]:  # 扩大搜索范围
                href = link.get('href', '')

                # 确保是完整URL
                if href and not href.startswith('http'):
                    if href.startswith('/'):
                        href = f"https://mil.huanqiu.com{href}"
                    else:
                        continue

                if href in seen_urls:
                    continue

                title = link.get_text(strip=True)

                # 过滤条件
                if len(title) < 10 or len(title) > 100:
                    continue

                # 排除导航链接
                if any(nav in title for nav in ['环球网', '登录', '注册', '首页', '频道']):
                    continue

                if title in seen_titles:
                    continue

                seen_urls.add(href)
                seen_titles.add(title)

                article = {
                    'title': title,
                    'url': href,
                    'summary': '',
                    'published': datetime.now().strftime('%Y-%m-%d'),
                    'published_raw': None,
                    'source': '环球网军事',
                    'type': 'news',
                    'priority': 'medium'
                }
                articles.append(article)

            print(f"✅ 环球网军事: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ 环球网军事爬取失败: {str(e)}")

        return articles

    def scrape_all(self) -> List[Dict]:
        """爬取所有军事新闻网站"""
        all_articles = []

        print(f"\n{'='*60}")
        print("🕷️  军事新闻网站爬取")
        print(f"{'='*60}\n")

        # Jane's Defence
        articles = self.scrape_janes()
        all_articles.extend(articles)
        time.sleep(2)

        # Army Technology
        articles = self.scrape_army_technology()
        all_articles.extend(articles)
        time.sleep(2)

        # 环球网军事
        articles = self.scrape_huanqiu_military()
        all_articles.extend(articles)

        print(f"\n✅ 军事新闻爬取总计: {len(all_articles)} 篇文章\n")

        return all_articles


def scrape_military_sources(days_lookback: int = 7) -> List[Dict]:
    """供外部调用的入口函数"""
    scraper = MilitaryScraper(days_lookback=days_lookback)
    return scraper.scrape_all()


if __name__ == "__main__":
    # 测试运行
    articles = scrape_military_sources(days_lookback=7)

    print("\n示例文章：")
    for i, article in enumerate(articles[:3], 1):
        print(f"\n{i}. {article['title']}")
        print(f"   来源: {article['source']}")
        print(f"   链接: {article['url']}")
