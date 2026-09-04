#!/usr/bin/env python3
"""
OpenAI爬虫 - 生产版本
使用Playwright处理JavaScript动态渲染，针对生产环境优化
"""

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import time
import re

class OpenAIScraper:
    def __init__(self, headless: bool = True, timeout: int = 90):
        """
        初始化OpenAI爬虫

        Args:
            headless: 是否使用无头模式（生产环境建议True，但可能被Cloudflare阻止）
            timeout: 页面加载超时时间（秒）
        """
        self.headless = headless
        self.timeout = timeout * 1000  # 转换为毫秒

    def _wait_for_cloudflare(self, page, max_wait: int = 45) -> bool:
        """
        等待Cloudflare验证完成

        Returns:
            True if successful, False if still blocked
        """
        print(f"  ⏳ 等待Cloudflare验证（最多{max_wait}秒）...")

        start_time = time.time()
        check_interval = 3

        while time.time() - start_time < max_wait:
            content = page.content()

            # 检查是否还在Cloudflare页面
            if "Just a moment" not in content and "Checking your browser" not in content:
                print(f"  ✅ Cloudflare验证通过（耗时{int(time.time() - start_time)}秒）")
                return True

            time.sleep(check_interval)

        print(f"  ⚠️  Cloudflare验证超时")
        return False

    def _extract_articles(self, soup: BeautifulSoup, base_url: str,
                         path_filter: str, source_name: str,
                         article_type: str, days_lookback: int) -> List[Dict]:
        """
        从HTML中提取文章信息
        不进行日期过滤，由RSS聚合器的缓存机制处理重复
        """
        articles = []
        # 移除日期过滤 - 由缓存处理

        # 查找所有链接
        all_links = soup.find_all('a', href=True)
        seen_urls = set()

        # OpenAI的文章分类（用于排除分类页）
        category_keywords = [
            'company-announcements', 'research', 'product-releases',
            'safety-alignment', 'engineering', 'applied-ai',
            'global-affairs', 'security', 'ai-adoption'
        ]

        for link_tag in all_links:
            try:
                href = link_tag.get('href', '').strip()

                # 过滤条件：
                # 1. 包含 /news/ 或 /index/ 路径
                # 2. 不是分类页
                # 3. 不是特殊文件

                # OpenAI文章可能在 /news/ 或 /index/ 路径
                is_news_article = path_filter in href
                is_index_article = '/index/' in href and article_type == 'news'

                if not (is_news_article or is_index_article):
                    continue

                # 排除特殊文件
                if href.endswith('.xml') or href.endswith('.rss'):
                    continue

                # 排除根路径
                if href in [path_filter, path_filter.rstrip('/'), '/index/', '/index']:
                    continue

                # 排除语言版本
                if re.search(r'/[a-z]{2}-[A-Z]{2}/', href):
                    continue

                # 排除分类页（通过关键词识别）
                is_category = any(cat in href for cat in category_keywords)
                if is_category:
                    continue

                # 构建完整URL
                if href.startswith('/'):
                    full_url = f"{base_url}{href}"
                elif href.startswith('http'):
                    if base_url.split('//')[1].split('/')[0] not in href:
                        continue  # 跳过外部链接
                    full_url = href
                else:
                    continue

                # 去重
                if full_url in seen_urls:
                    continue
                seen_urls.add(full_url)

                # 提取标题 - 多种策略
                title = None

                # 策略1: 链接文本
                link_text = link_tag.get_text(strip=True)
                if link_text and len(link_text) >= 10 and len(link_text) <= 200:
                    title = link_text

                # 策略2: 从父元素查找标题标签
                if not title or len(title) < 10:
                    for parent in [link_tag.parent, link_tag.parent.parent if link_tag.parent else None]:
                        if parent:
                            for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                                h_tag = parent.find(tag_name)
                                if h_tag:
                                    title = h_tag.get_text(strip=True)
                                    if len(title) >= 10:
                                        break
                            if title and len(title) >= 10:
                                break

                # 策略3: aria-label属性
                if not title or len(title) < 10:
                    title = link_tag.get('aria-label', '').strip()

                # 策略4: 从URL生成标题（最后备选）
                if not title or len(title) < 10:
                    # 从URL路径生成可读标题
                    url_parts = href.rstrip('/').split('/')
                    if url_parts:
                        title = url_parts[-1].replace('-', ' ').title()

                if not title or len(title) < 10:
                    continue

                # 清理标题（去掉多余空白）
                title = ' '.join(title.split())

                # 尝试提取日期
                date_str = ""
                parent = link_tag.parent

                for _ in range(3):  # 向上查找3层
                    if parent:
                        # 查找time标签
                        time_elem = parent.find('time')
                        if time_elem:
                            date_str = time_elem.get('datetime', '') or time_elem.get_text(strip=True)
                            break

                        # 查找日期格式文本
                        parent_text = parent.get_text()
                        date_match = re.search(r'(\d{4}-\d{2}-\d{2}|\w+ \d{1,2}, \d{4})', parent_text)
                        if date_match:
                            date_str = date_match.group(1)
                            break

                        parent = parent.parent

                articles.append({
                    'title': title[:200],  # 限制长度
                    'url': full_url,
                    'summary': '',
                    'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                    'published_raw': None,
                    'source': source_name,
                    'type': article_type,
                    'priority': 'high',
                })

            except Exception as e:
                continue

        return articles

    def scrape_openai_page(self, url: str, source_name: str,
                          path_filter: str, article_type: str,
                          days_lookback: int = 7) -> List[Dict]:
        """
        爬取OpenAI页面的通用方法
        """
        articles = []

        try:
            print(f"🕷️  爬取: {source_name} ({url})")

            with sync_playwright() as p:
                # 启动浏览器
                browser = p.chromium.launch(
                    headless=self.headless,
                    args=[
                        '--disable-blink-features=AutomationControlled',
                        '--disable-dev-shm-usage',
                        '--no-sandbox'
                    ]
                )

                # 创建上下文，模拟真实浏览器
                context = browser.new_context(
                    viewport={'width': 1920, 'height': 1080},
                    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    locale='en-US',
                    timezone_id='America/New_York'
                )

                page = context.new_page()

                # 设置额外的headers
                page.set_extra_http_headers({
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                })

                try:
                    # 访问页面
                    print(f"  📡 正在访问页面...")
                    page.goto(url, wait_until='domcontentloaded', timeout=self.timeout)

                    # 等待Cloudflare验证
                    if not self._wait_for_cloudflare(page, max_wait=45):
                        print(f"  ❌ Cloudflare验证失败，尝试继续...")

                    # 额外等待确保内容加载
                    print(f"  ⏳ 等待内容加载...")
                    time.sleep(5)

                    # 获取渲染后的HTML
                    content = page.content()

                    # 检查内容大小
                    if len(content) < 50000:
                        print(f"  ⚠️  页面内容较小（{len(content)}字节），可能未完全加载")

                    browser.close()

                    # 解析HTML
                    soup = BeautifulSoup(content, 'html.parser')

                    # 提取文章
                    articles = self._extract_articles(
                        soup, 'https://openai.com',
                        path_filter, source_name,
                        article_type, days_lookback
                    )

                    print(f"✅ {source_name}: {len(articles)} 篇文章")

                except PlaywrightTimeout:
                    print(f"  ⚠️  页面加载超时")
                    browser.close()
                except Exception as e:
                    print(f"  ⚠️  爬取过程出错: {str(e)}")
                    browser.close()

        except Exception as e:
            print(f"❌ 爬取 {source_name} 失败: {str(e)}")

        return articles

    def scrape_openai_news(self, days_lookback: int = 7) -> List[Dict]:
        """爬取OpenAI News"""
        return self.scrape_openai_page(
            url='https://openai.com/news',
            source_name='OpenAI News',
            path_filter='/news/',
            article_type='news',
            days_lookback=days_lookback
        )

    def scrape_openai_research(self, days_lookback: int = 7) -> List[Dict]:
        """爬取OpenAI Research"""
        return self.scrape_openai_page(
            url='https://openai.com/research',
            source_name='OpenAI Research',
            path_filter='/research/',
            article_type='research',
            days_lookback=days_lookback
        )

    def scrape_all(self, days_lookback: int = 7) -> List[Dict]:
        """爬取所有OpenAI页面"""
        articles = []

        # 爬取News
        news_articles = self.scrape_openai_news(days_lookback)
        articles.extend(news_articles)

        # 爬取Research
        research_articles = self.scrape_openai_research(days_lookback)
        articles.extend(research_articles)

        return articles


if __name__ == "__main__":
    """测试脚本"""
    import sys

    print("\n" + "="*70)
    print("🧪 测试 OpenAI 爬虫（生产版本）")
    print("="*70 + "\n")

    # 检查是否在支持图形界面的环境
    headless = '--headless' in sys.argv or True  # 默认headless

    if not headless:
        print("⚠️  使用非headless模式（需要图形界面）\n")

    scraper = OpenAIScraper(headless=headless, timeout=90)
    articles = scraper.scrape_all(days_lookback=30)

    print(f"\n" + "="*70)
    print(f"📊 爬取结果统计")
    print("="*70)
    print(f"总计: {len(articles)} 篇文章")

    # 按来源统计
    news_count = len([a for a in articles if a['source'] == 'OpenAI News'])
    research_count = len([a for a in articles if a['source'] == 'OpenAI Research'])

    print(f"  - OpenAI News: {news_count} 篇")
    print(f"  - OpenAI Research: {research_count} 篇")

    if articles:
        print(f"\n前5篇文章:")
        for i, article in enumerate(articles[:5], 1):
            print(f"\n{i}. {article['title']}")
            print(f"   来源: {article['source']}")
            print(f"   URL: {article['url']}")
            if article['published']:
                print(f"   日期: {article['published']}")
    else:
        print("\n⚠️  未能获取到文章")
        print("可能原因:")
        print("  1. Cloudflare验证未通过")
        print("  2. 页面结构已变化")
        print("  3. 网络连接问题")

    print("\n" + "="*70)
    print("✅ 测试完成!")
    print("="*70 + "\n")
