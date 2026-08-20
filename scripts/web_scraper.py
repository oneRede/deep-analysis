#!/usr/bin/env python3
"""
Web Scraper Module - 为没有 RSS 的网站提供爬取功能
用于 DeepSeek 和 Qwen 等官方博客
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import time
import re
import json

try:
    import cloudscraper
    CLOUDSCRAPER_AVAILABLE = True
except ImportError:
    CLOUDSCRAPER_AVAILABLE = False


class WebScraper:
    def __init__(self, user_agent: str = None):
        """初始化爬虫"""
        self.user_agent = user_agent or "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        self.session = requests.Session()

        # 设置更完整的请求头，模拟真实浏览器
        self.session.headers.update({
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        })

    def scrape_deepseek_blog(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取 DeepSeek 官方博客
        URL: https://deepseek.ai/blog
        注意：这是一个动态加载的网站，使用备用方案
        """
        articles = []

        # DeepSeek 博客是 SPA，内容在 JSON 中
        # 尝试从页面源码中提取 JSON 数据
        url = "https://deepseek.ai/blog"

        try:
            print(f"🕷️  爬取: DeepSeek Blog ({url})")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            # 尝试从页面中提取 JSON-LD 或内联数据
            soup = BeautifulSoup(response.content, 'html.parser')

            # 查找 JSON-LD 结构化数据
            json_ld_scripts = soup.find_all('script', type='application/ld+json')

            for script in json_ld_scripts:
                try:
                    data = json.loads(script.string)

                    # 检查是否包含博客文章
                    if isinstance(data, dict) and 'blogPost' in data:
                        cutoff_date = datetime.now() - timedelta(days=days_lookback)

                        for post in data['blogPost']:
                            if isinstance(post, dict):
                                title = post.get('headline', '')
                                url_path = post.get('url', '')
                                date_str = post.get('datePublished', '')
                                description = post.get('description', '')

                                if not title or not url_path:
                                    continue

                                # 解析日期
                                article_date = self._parse_date(date_str)
                                if article_date and article_date < cutoff_date:
                                    continue

                                articles.append({
                                    'title': title,
                                    'url': url_path if url_path.startswith('http') else f"https://deepseek.ai{url_path}",
                                    'summary': description,
                                    'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                                    'published_raw': None,
                                    'source': 'DeepSeek Blog',
                                    'type': 'blog',
                                    'priority': 'high',
                                })

                except json.JSONDecodeError:
                    continue

            print(f"✅ DeepSeek Blog: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ 爬取 DeepSeek Blog 失败: {str(e)}")

        return articles

        return articles

    def scrape_qwen_blog(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取 Qwen 官方博客
        URL: https://qwenlm.github.io/blog/
        """
        articles = []
        url = "https://qwenlm.github.io/blog/"

        try:
            print(f"🕷️  爬取: Qwen Blog ({url})")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            cutoff_date = datetime.now() - timedelta(days=days_lookback)

            # 查找文章列表
            article_items = soup.find_all('article') or soup.find_all('div', class_=re.compile(r'post|article|blog', re.I))

            for item in article_items:
                try:
                    # 提取标题
                    title_tag = item.find(['h1', 'h2', 'h3', 'h4'])
                    if not title_tag:
                        continue

                    title = title_tag.get_text(strip=True)

                    # 提取链接
                    link_tag = title_tag.find('a') or item.find('a')
                    if not link_tag:
                        continue

                    link = link_tag.get('href', '')
                    if link.startswith('/'):
                        link = f"https://qwenlm.github.io{link}"

                    # 提取日期
                    date_tag = item.find(['time', 'span'], class_=re.compile(r'date|time|published', re.I))
                    date_str = date_tag.get_text(strip=True) if date_tag else ""

                    # 提取摘要
                    summary_tag = item.find(['p', 'div'], class_=re.compile(r'summary|excerpt|description|content', re.I))
                    summary = summary_tag.get_text(strip=True) if summary_tag else ""

                    # 解析日期
                    article_date = self._parse_date(date_str)

                    # 时间过滤
                    if article_date and article_date < cutoff_date:
                        continue

                    articles.append({
                        'title': title,
                        'url': link,
                        'summary': summary,
                        'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                        'published_raw': None,
                        'source': 'Qwen Blog',
                        'type': 'blog',
                        'priority': 'high',
                    })

                except Exception as e:
                    print(f"  ⚠️  解析文章失败: {str(e)}")
                    continue

            print(f"✅ Qwen Blog: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ 爬取 Qwen Blog 失败: {str(e)}")

        return articles

    def _parse_date(self, date_str: str) -> Optional[datetime]:
        """解析日期字符串"""
        if not date_str:
            return None

        # 常见日期格式
        formats = [
            '%Y-%m-%d',
            '%Y/%m/%d',
            '%B %d, %Y',  # August 16, 2026
            '%b %d, %Y',   # Aug 16, 2026
            '%d %B %Y',
            '%d %b %Y',
        ]

        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except:
                continue

        # 尝试提取年月日数字
        match = re.search(r'(\d{4})[/-](\d{1,2})[/-](\d{1,2})', date_str)
        if match:
            try:
                return datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            except:
                pass

        return None


    def scrape_zhipu_research(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取智谱 AI 研究页面
        URL: https://www.zhipuai.cn/en/research/
        """
        articles = []
        url = "https://www.zhipuai.cn/en/research/"

        try:
            print(f"🕷️  爬取: Zhipu AI Research ({url})")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            cutoff_date = datetime.now() - timedelta(days=days_lookback)

            # 查找所有包含标题和链接的元素
            # 尝试多种选择器策略
            all_links = soup.find_all('a', href=True)

            for link_tag in all_links:
                try:
                    # 检查链接是否指向研究内容
                    href = link_tag.get('href', '')
                    if not href or href == '#':
                        continue

                    # 提取标题（从链接文本或子元素）
                    title = link_tag.get_text(strip=True)
                    if not title or len(title) < 10:
                        continue

                    # 构建完整URL
                    if href.startswith('/'):
                        full_url = f"https://www.zhipuai.cn{href}"
                    elif href.startswith('http'):
                        full_url = href
                    else:
                        continue

                    # 查找相关的日期（在父元素或兄弟元素中）
                    parent = link_tag.parent
                    date_str = ""
                    if parent:
                        # 在父元素中查找日期
                        date_elem = parent.find(['time', 'span'], class_=re.compile(r'date|time', re.I))
                        if date_elem:
                            date_str = date_elem.get_text(strip=True)
                        else:
                            # 尝试从文本中提取日期
                            text = parent.get_text()
                            date_match = re.search(r'(\w+\s+\d{1,2},\s+\d{4})', text)
                            if date_match:
                                date_str = date_match.group(1)

                    # 解析日期
                    article_date = self._parse_date(date_str)
                    if article_date and article_date < cutoff_date:
                        continue

                    # 避免重复
                    if any(a['url'] == full_url for a in articles):
                        continue

                    articles.append({
                        'title': title,
                        'url': full_url,
                        'summary': '',
                        'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                        'published_raw': None,
                        'source': 'Zhipu AI Research',
                        'type': 'research',
                        'priority': 'high',
                    })

                except Exception as e:
                    continue

            print(f"✅ Zhipu AI Research: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ 爬取 Zhipu AI Research 失败: {str(e)}")

        return articles

    def scrape_kimi_blog(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取 Kimi (Moonshot AI) 官方博客
        URL: https://platform.kimi.ai/blog
        """
        articles = []
        url = "https://platform.kimi.ai/blog"

        try:
            print(f"🕷️  爬取: Kimi Blog ({url})")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            cutoff_date = datetime.now() - timedelta(days=days_lookback)

            # 查找文章列表
            article_items = soup.find_all(['article', 'div'], class_=re.compile(r'post|blog|article', re.I))

            for item in article_items:
                try:
                    # 提取标题
                    title_tag = item.find(['h1', 'h2', 'h3', 'h4'])
                    if not title_tag:
                        continue

                    title = title_tag.get_text(strip=True)

                    # 提取链接
                    link_tag = title_tag.find('a') or item.find('a')
                    if not link_tag:
                        continue

                    link = link_tag.get('href', '')
                    if link.startswith('/'):
                        link = f"https://platform.kimi.ai{link}"

                    # 提取日期
                    date_tag = item.find(['time', 'span'], class_=re.compile(r'date|time', re.I))
                    date_str = date_tag.get_text(strip=True) if date_tag else ""

                    # 提取摘要
                    summary_tag = item.find(['p'], class_=re.compile(r'summary|excerpt|description', re.I))
                    summary = summary_tag.get_text(strip=True) if summary_tag else ""

                    # 解析日期
                    article_date = self._parse_date(date_str)
                    if article_date and article_date < cutoff_date:
                        continue

                    articles.append({
                        'title': title,
                        'url': link,
                        'summary': summary,
                        'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                        'published_raw': None,
                        'source': 'Kimi Blog',
                        'type': 'blog',
                        'priority': 'high',
                    })

                except Exception as e:
                    continue

            print(f"✅ Kimi Blog: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ 爬取 Kimi Blog 失败: {str(e)}")

        return articles

    def scrape_anthropic_research(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取 Anthropic 研究页面
        URL: https://www.anthropic.com/research
        """
        articles = []
        url = "https://www.anthropic.com/research"

        try:
            print(f"🕷️  爬取: Anthropic Research ({url})")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            cutoff_date = datetime.now() - timedelta(days=days_lookback)

            # 查找所有包含研究内容的链接
            all_links = soup.find_all('a', href=True)

            for link_tag in all_links:
                try:
                    href = link_tag.get('href', '')

                    # 过滤掉非研究内容的链接
                    if not href or href == '#' or not ('/research/' in href or '/news/' in href):
                        continue

                    # 提取标题
                    title = link_tag.get_text(strip=True)
                    if not title or len(title) < 10:
                        # 尝试从子元素获取
                        title_elem = link_tag.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                        if title_elem:
                            title = title_elem.get_text(strip=True)
                        else:
                            continue

                    # 构建完整URL
                    if href.startswith('/'):
                        full_url = f"https://www.anthropic.com{href}"
                    elif href.startswith('http'):
                        full_url = href
                    else:
                        continue

                    # 查找日期
                    parent = link_tag.parent
                    date_str = ""
                    if parent:
                        date_elem = parent.find(['time', 'span'], class_=re.compile(r'date|time', re.I))
                        if date_elem:
                            date_str = date_elem.get_text(strip=True)
                        else:
                            # 尝试从周围文本提取日期
                            text = parent.get_text()
                            # 匹配 "Aug 18, 2026" 格式
                            date_match = re.search(r'(\w{3}\s+\d{1,2},\s+\d{4})', text)
                            if date_match:
                                date_str = date_match.group(1)

                    # 解析日期
                    article_date = self._parse_date(date_str)
                    if article_date and article_date < cutoff_date:
                        continue

                    # 避免重复
                    if any(a['url'] == full_url for a in articles):
                        continue

                    articles.append({
                        'title': title,
                        'url': full_url,
                        'summary': '',
                        'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                        'published_raw': None,
                        'source': 'Anthropic Research',
                        'type': 'research',
                        'priority': 'high',
                    })

                except Exception as e:
                    continue

            print(f"✅ Anthropic Research: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ 爬取 Anthropic Research 失败: {str(e)}")

        return articles

    def scrape_openai_blog(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取 OpenAI 新闻和研究页面
        URL: https://openai.com/news 和 https://openai.com/research
        使用 cloudscraper 绕过 Cloudflare，智能重试多种配置
        """
        articles = []
        urls = [
            ('https://openai.com/news', 'OpenAI News'),
            ('https://openai.com/research', 'OpenAI Research')
        ]

        # 多种浏览器配置，按成功率排序
        browser_configs = [
            {'browser': 'chrome', 'platform': 'darwin', 'desktop': True},
            {'browser': 'firefox', 'platform': 'windows', 'desktop': True},
            {'browser': 'chrome', 'platform': 'windows', 'desktop': True},
        ]

        for url, source_name in urls:
            success = False

            for attempt, config in enumerate(browser_configs):
                try:
                    if attempt > 0:
                        print(f"  🔄 重试 {attempt+1}/{len(browser_configs)} ({config['browser']}/{config['platform']})...")
                        time.sleep(3)
                    else:
                        print(f"🕷️  爬取: {source_name} ({url})")

                    # 使用 cloudscraper 绕过 Cloudflare
                    if CLOUDSCRAPER_AVAILABLE:
                        scraper = cloudscraper.create_scraper(browser=config)

                        # 添加完整的请求头
                        scraper.headers.update({
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webif,*/*;q=0.8',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'DNT': '1',
                            'Connection': 'keep-alive',
                            'Upgrade-Insecure-Requests': '1',
                        })

                        response = scraper.get(url, timeout=30)
                    else:
                        print(f"⚠️  cloudscraper 未安装，使用标准请求...")
                        response = self.session.get(url, timeout=30)

                    if response.status_code == 403:
                        if attempt < len(browser_configs) - 1:
                            continue  # 尝试下一个配置
                        else:
                            raise Exception(f"403 Forbidden (尝试了 {len(browser_configs)} 种配置)")

                    response.raise_for_status()
                    success = True
                    break  # 成功，跳出重试循环

                except Exception as e:
                    if attempt == len(browser_configs) - 1:  # 最后一次尝试
                        print(f"❌ 爬取 {source_name} 失败: {str(e)}")
                        break
                    # 否则继续下一个配置

            if not success:
                continue  # 跳过这个URL，继续下一个

            # 成功获取，开始解析
            soup = BeautifulSoup(response.content, 'html.parser')
            cutoff_date = datetime.now() - timedelta(days=days_lookback)

            # 查找所有新闻/研究文章链接
            all_links = soup.find_all('a', href=True)

            for link_tag in all_links:
                try:
                    href = link_tag.get('href', '')

                    # 过滤文章链接
                    if not href or href == '#':
                        continue

                    # 只保留 news 或 research 路径的链接
                    if '/news/' not in href and '/research/' not in href:
                        continue

                    # 提取标题
                    title = link_tag.get_text(strip=True)
                    if not title or len(title) < 10:
                        title_elem = link_tag.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                        if title_elem:
                            title = title_elem.get_text(strip=True)
                        else:
                            continue

                    # 构建完整URL
                    if href.startswith('/'):
                        full_url = f"https://openai.com{href}"
                    elif href.startswith('http'):
                        full_url = href
                    else:
                        continue

                    # 查找日期
                    parent = link_tag.parent
                    date_str = ""
                    if parent:
                        date_elem = parent.find(['time', 'span'], class_=re.compile(r'date|time', re.I))
                        if date_elem:
                            date_str = date_elem.get_text(strip=True)
                        else:
                            text = parent.get_text()
                            date_match = re.search(r'(\w{3}\s+\d{1,2},\s+\d{4})', text)
                            if date_match:
                                date_str = date_match.group(1)

                    # 解析日期
                    article_date = self._parse_date(date_str)
                    if article_date and article_date < cutoff_date:
                        continue

                    # 避免重复
                    if any(a['url'] == full_url for a in articles):
                        continue

                    articles.append({
                        'title': title,
                        'url': full_url,
                        'summary': '',
                        'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                        'published_raw': None,
                        'source': source_name,
                        'type': 'news' if 'news' in url else 'research',
                        'priority': 'high',
                    })

                except Exception as e:
                    continue

            print(f"✅ {source_name}: {len([a for a in articles if a['source'] == source_name])} 篇文章")

        return articles

    def scrape_xai_blog(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取 xAI (Grok) 博客
        URL: https://x.ai/blog
        使用 cloudscraper 绕过 Cloudflare
        """
        articles = []
        url = "https://x.ai/blog"

        try:
            print(f"🕷️  爬取: xAI Blog ({url})")

            # 使用 cloudscraper 绕过 Cloudflare
            if CLOUDSCRAPER_AVAILABLE:
                scraper = cloudscraper.create_scraper(
                    browser={
                        'browser': 'chrome',
                        'platform': 'darwin',
                        'desktop': True
                    }
                )
                response = scraper.get(url, timeout=30)
            else:
                print(f"⚠️  cloudscraper 未安装，使用标准请求...")
                response = self.session.get(url, timeout=30)

            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            cutoff_date = datetime.now() - timedelta(days=days_lookback)

            # 查找所有新闻/博客链接
            all_links = soup.find_all('a', href=True)

            for link_tag in all_links:
                try:
                    href = link_tag.get('href', '')

                    # 过滤新闻/博客链接
                    if not href or href == '#' or not ('/news/' in href or '/blog/' in href):
                        continue

                    # 提取标题
                    title = link_tag.get_text(strip=True)
                    if not title or len(title) < 10:
                        title_elem = link_tag.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                        if title_elem:
                            title = title_elem.get_text(strip=True)
                        else:
                            continue

                    # 构建完整URL
                    if href.startswith('/'):
                        full_url = f"https://x.ai{href}"
                    elif href.startswith('http'):
                        full_url = href
                    else:
                        continue

                    # 查找日期
                    parent = link_tag.parent
                    date_str = ""
                    if parent:
                        date_elem = parent.find(['time', 'span'], class_=re.compile(r'date|time', re.I))
                        if date_elem:
                            date_str = date_elem.get_text(strip=True)
                        else:
                            text = parent.get_text()
                            date_match = re.search(r'(\w{3}\s+\d{1,2},\s+\d{4})', text)
                            if date_match:
                                date_str = date_match.group(1)

                    # 解析日期
                    article_date = self._parse_date(date_str)
                    if article_date and article_date < cutoff_date:
                        continue

                    # 避免重复
                    if any(a['url'] == full_url for a in articles):
                        continue

                    articles.append({
                        'title': title,
                        'url': full_url,
                        'summary': '',
                        'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                        'published_raw': None,
                        'source': 'xAI Blog',
                        'type': 'blog',
                        'priority': 'high',
                    })

                except Exception as e:
                    continue

            print(f"✅ xAI Blog: {len(articles)} 篇文章")

        except Exception as e:
            print(f"❌ 爬取 xAI Blog 失败: {str(e)}")

        return articles


    def scrape_embodied_ai_companies(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取具身智能公司的博客/新闻
        包括：Figure AI, Physical Intelligence, Skild AI, 1X Technologies, Covariant
        以及中国公司：UBTECH, Unitree, Agibot
        """
        all_articles = []

        companies = [
            {
                'name': 'Physical Intelligence',
                'url': 'https://www.physicalintelligence.company/blog',
                'path_filter': '/blog/'
            },
            {
                'name': 'Skild AI',
                'url': 'https://www.skild.ai/blogs',
                'path_filter': '/blogs/'
            },
            {
                'name': 'Figure AI',
                'url': 'https://www.figure.ai/news',
                'path_filter': '/news/'
            },
            {
                'name': '1X Technologies',
                'url': 'https://www.1x.tech/discover',
                'path_filter': '/discover/'
            },
            # 中国具身智能公司
            {
                'name': 'UBTECH (优必选)',
                'url': 'https://www.ubtrobot.com/en/news-list',
                'path_filter': '/news'
            },
            {
                'name': 'Unitree (宇树科技)',
                'url': 'https://www.unitree.com/',
                'path_filter': ['/news', '/article']
            },
            {
                'name': 'Agibot (智元机器人)',
                'url': 'https://agibot.com/news',
                'path_filter': ['/news', '/article']
            }
        ]

        for company in companies:
            try:
                print(f"🕷️  爬取: {company['name']} ({company['url']})")

                if CLOUDSCRAPER_AVAILABLE:
                    scraper = cloudscraper.create_scraper(
                        browser={'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
                    )
                    response = scraper.get(company['url'], timeout=30)
                else:
                    response = self.session.get(company['url'], timeout=30)

                response.raise_for_status()

                soup = BeautifulSoup(response.content, 'html.parser')
                cutoff_date = datetime.now() - timedelta(days=days_lookback)

                all_links = soup.find_all('a', href=True)

                for link_tag in all_links:
                    try:
                        href = link_tag.get('href', '')

                        if not href or href == '#':
                            continue

                        # 过滤相关路径（支持单个或多个过滤器）
                        path_filter = company['path_filter']
                        if isinstance(path_filter, list):
                            # 多个路径过滤器
                            if not any(pf in href for pf in path_filter):
                                continue
                        else:
                            # 单个路径过滤器
                            if path_filter not in href:
                                continue

                        title = link_tag.get_text(strip=True)
                        if not title or len(title) < 10:
                            title_elem = link_tag.find(['h1', 'h2', 'h3', 'h4'])
                            if title_elem:
                                title = title_elem.get_text(strip=True)
                            else:
                                continue

                        # 构建完整URL
                        if href.startswith('/'):
                            base_url = company['url'].split('/blog')[0].split('/blogs')[0]
                            full_url = f"{base_url}{href}"
                        elif href.startswith('http'):
                            full_url = href
                        else:
                            continue

                        # 查找日期
                        parent = link_tag.parent
                        date_str = ""
                        if parent:
                            date_elem = parent.find(['time', 'span'], class_=re.compile(r'date|time', re.I))
                            if date_elem:
                                date_str = date_elem.get_text(strip=True)
                            else:
                                text = parent.get_text()
                                date_match = re.search(r'(\w{3}\s+\d{1,2},\s+\d{4})', text)
                                if date_match:
                                    date_str = date_match.group(1)

                        article_date = self._parse_date(date_str)
                        if article_date and article_date < cutoff_date:
                            continue

                        if any(a['url'] == full_url for a in all_articles):
                            continue

                        all_articles.append({
                            'title': title,
                            'url': full_url,
                            'summary': '',
                            'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                            'published_raw': None,
                            'source': company['name'],
                            'type': 'blog',
                            'priority': 'high',
                        })

                    except Exception as e:
                        continue

                company_articles = [a for a in all_articles if a['source'] == company['name']]
                print(f"✅ {company['name']}: {len(company_articles)} 篇文章")

            except Exception as e:
                print(f"❌ 爬取 {company['name']} 失败: {str(e)}")

        return all_articles


    def scrape_ai_chip_companies(self, days_lookback: int = 7) -> List[Dict]:
        """
        爬取AI芯片公司的博客/新闻
        包括：Cerebras, SambaNova, Tenstorrent, D-Matrix, Etched
        """
        all_articles = []

        companies = [
            {
                'name': 'Cerebras',
                'url': 'https://www.cerebras.ai/blog',
                'path_filter': '/blog/',
                'browser_config': {'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
            },
            {
                'name': 'SambaNova',
                'url': 'https://sambanova.ai/blog',
                'path_filter': '/blog/',
                'browser_config': {'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
            },
            {
                'name': 'Tenstorrent',
                'url': 'https://tenstorrent.com/newsroom',
                'path_filter': '/newsroom/',
                'browser_config': {'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
            },
            {
                'name': 'D-Matrix',
                'url': 'https://www.d-matrix.ai/blog/',  # 注意 www 前缀和结尾 /
                'path_filter': ['/blog/', '/announcements/'],
                'browser_config': {'browser': 'firefox', 'platform': 'windows', 'desktop': True}  # Firefox/Windows 成功
            },
            {
                'name': 'Etched',
                'url': 'https://etched.com/progress',
                'path_filter': '/progress/',
                'browser_config': {'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
            },
            # 中国AI芯片公司
            {
                'name': 'Cambricon (寒武纪)',
                'url': 'https://www.cambricon.com/',
                'path_filter': ['/news', '新闻'],
                'browser_config': {'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
            },
            {
                'name': 'Iluvatar (天数智芯)',
                'url': 'https://www.iluvatar.com/news',
                'path_filter': ['/news', '/newsdetails'],
                'browser_config': {'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
            },
            {
                'name': 'Enflame (燧原科技)',
                'url': 'https://www.enflame-tech.com/news',
                'path_filter': '/news',
                'browser_config': {'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
            },
            {
                'name': 'MetaX (沐曦)',
                'url': 'https://www.metax-tech.com/news.html',
                'path_filter': ['/news', 'news.html'],
                'browser_config': {'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
            },
            {
                'name': 'Biren (壁仞科技)',
                'url': 'https://www.birentech.com/news/',
                'path_filter': '/news',
                'browser_config': {'browser': 'chrome', 'platform': 'darwin', 'desktop': True}
            }
        ]

        for company in companies:
            try:
                print(f"🕷️  爬取: {company['name']} ({company['url']})")

                if CLOUDSCRAPER_AVAILABLE:
                    scraper = cloudscraper.create_scraper(browser=company.get('browser_config', {
                        'browser': 'chrome', 'platform': 'darwin', 'desktop': True
                    }))

                    # D-Matrix 需要特殊处理：先访问主页建立会话，多次重试
                    if company['name'] == 'D-Matrix':
                        success = False
                        for attempt in range(3):  # 最多尝试3次
                            try:
                                if attempt > 0:
                                    print(f"  🔄 重试 {attempt}/3...")
                                    time.sleep(5 * attempt)  # 递增延迟

                                # 先访问主页
                                homepage_resp = scraper.get('https://www.d-matrix.ai/', timeout=30)
                                if homepage_resp.status_code == 200:
                                    time.sleep(2)  # 模拟人类浏览
                                    response = scraper.get(company['url'], timeout=30)
                                    if response.status_code == 200:
                                        success = True
                                        break
                            except Exception as e:
                                if attempt == 2:  # 最后一次尝试
                                    print(f"  ⚠️  多次尝试后仍失败，跳过 D-Matrix")
                                continue

                        if not success:
                            print(f"❌ D-Matrix: Cloudflare 保护（403），暂时跳过")
                            continue
                    else:
                        response = scraper.get(company['url'], timeout=30)
                else:
                    response = self.session.get(company['url'], timeout=30)

                response.raise_for_status()

                soup = BeautifulSoup(response.content, 'html.parser')
                cutoff_date = datetime.now() - timedelta(days=days_lookback)

                all_links = soup.find_all('a', href=True)

                for link_tag in all_links:
                    try:
                        href = link_tag.get('href', '')

                        if not href or href == '#':
                            continue

                        # 过滤博客路径（支持单个或多个过滤器）
                        path_filter = company['path_filter']
                        if isinstance(path_filter, list):
                            # 多个路径过滤器
                            if not any(pf in href for pf in path_filter):
                                continue
                        else:
                            # 单个路径过滤器
                            if path_filter not in href:
                                continue

                        title = link_tag.get_text(strip=True)
                        if not title or len(title) < 10:
                            title_elem = link_tag.find(['h1', 'h2', 'h3', 'h4'])
                            if title_elem:
                                title = title_elem.get_text(strip=True)
                            else:
                                continue

                        # 构建完整URL
                        if href.startswith('/'):
                            base_url = company['url'].split('/blog')[0]
                            full_url = f"{base_url}{href}"
                        elif href.startswith('http'):
                            full_url = href
                        else:
                            continue

                        # 查找日期
                        parent = link_tag.parent
                        date_str = ""
                        if parent:
                            date_elem = parent.find(['time', 'span'], class_=re.compile(r'date|time', re.I))
                            if date_elem:
                                date_str = date_elem.get_text(strip=True)
                            else:
                                text = parent.get_text()
                                date_match = re.search(r'(\w{3}\s+\d{1,2},\s+\d{4})', text)
                                if date_match:
                                    date_str = date_match.group(1)

                        article_date = self._parse_date(date_str)
                        if article_date and article_date < cutoff_date:
                            continue

                        if any(a['url'] == full_url for a in all_articles):
                            continue

                        all_articles.append({
                            'title': title,
                            'url': full_url,
                            'summary': '',
                            'published': date_str or datetime.now().strftime('%Y-%m-%d'),
                            'published_raw': None,
                            'source': company['name'],
                            'type': 'blog',
                            'priority': 'high',
                        })

                    except Exception as e:
                        continue

                company_articles = [a for a in all_articles if a['source'] == company['name']]
                print(f"✅ {company['name']}: {len(company_articles)} 篇文章")

            except Exception as e:
                print(f"❌ 爬取 {company['name']} 失败: {str(e)}")

        return all_articles


def scrape_all_custom_sources(days_lookback: int = 1) -> List[Dict]:
    """爬取所有自定义网站源 - 默认获取昨天(1天)的文章"""
    scraper = WebScraper()
    all_articles = []

    # ============================================================
    # 主流大模型公司
    # ============================================================

    # 爬取 DeepSeek
    all_articles.extend(scraper.scrape_deepseek_blog(days_lookback))
    time.sleep(1)

    # 爬取 Qwen
    all_articles.extend(scraper.scrape_qwen_blog(days_lookback))
    time.sleep(1)

    # 爬取智谱 AI
    all_articles.extend(scraper.scrape_zhipu_research(days_lookback))
    time.sleep(1)

    # 爬取 Kimi (Moonshot AI)
    all_articles.extend(scraper.scrape_kimi_blog(days_lookback))
    time.sleep(1)

    # 爬取 Anthropic
    all_articles.extend(scraper.scrape_anthropic_research(days_lookback))
    time.sleep(1)

    # 爬取 OpenAI
    all_articles.extend(scraper.scrape_openai_blog(days_lookback))
    time.sleep(1)

    # 爬取 xAI/Grok
    all_articles.extend(scraper.scrape_xai_blog(days_lookback))
    time.sleep(1)

    # ============================================================
    # 具身智能公司
    # ============================================================

    all_articles.extend(scraper.scrape_embodied_ai_companies(days_lookback))
    time.sleep(1)

    # ============================================================
    # AI 芯片公司
    # ============================================================

    all_articles.extend(scraper.scrape_ai_chip_companies(days_lookback))
    time.sleep(1)

    return all_articles


if __name__ == "__main__":
    # 测试爬虫
    articles = scrape_all_custom_sources(days_lookback=30)
    print(f"\n总计爬取: {len(articles)} 篇文章")

    for article in articles[:5]:  # 显示前5篇
        print(f"\n标题: {article['title']}")
        print(f"来源: {article['source']}")
        print(f"链接: {article['url']}")
        print(f"日期: {article['published']}")
