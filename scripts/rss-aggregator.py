#!/usr/bin/env python3
"""
RSS/Atom Feed 聚合器 - AI 技术进展自动追踪
用途：定期抓取配置的信源，生成候选清单，自动去重
"""

import feedparser
import yaml
import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Set
from urllib.parse import urlparse
import re
import os
import requests
import time
from bs4 import BeautifulSoup
from web_scraper import scrape_all_custom_sources
from military_scraper import scrape_military_sources
from dotenv import load_dotenv

# 配置路径
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
CONFIG_FILE = ROOT_DIR / "config" / "feeds.yml"
CATEGORIES_FILE = ROOT_DIR / "config" / "categories.yml"
REPORT_DIR = ROOT_DIR / "report"
CACHE_FILE = SCRIPT_DIR / ".rss-cache.json"

# 加载 .env 文件
ENV_FILE = ROOT_DIR / ".env"
if ENV_FILE.exists():
    load_dotenv(ENV_FILE)
    print(f"✅ 已从 {ENV_FILE} 加载环境变量")

class RSSAggregator:
    def __init__(self, config_path: Path, categories_path: Path = CATEGORIES_FILE):
        """初始化聚合器"""
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        # 加载分类配置
        with open(categories_path, 'r', encoding='utf-8') as f:
            categories_config = yaml.safe_load(f)
            self.categories = categories_config['categories']
            self.default_category = categories_config.get('default_category', 'ai_application')
            self.enable_uncategorized = categories_config.get('enable_uncategorized', True)

        # 构建分类映射
        self.category_name_to_key = {cat['name']: cat['key'] for cat in self.categories}
        self.category_key_to_name = {cat['key']: cat['name'] for cat in self.categories}

        self.cache = self._load_cache()
        self.articles = []
        self.seen_urls: Set[str] = set()

        # DeepSeek API 配置
        self.deepseek_api_key = os.getenv('DEEPSEEK_API_KEY', '').strip()
        self.deepseek_api_url = "https://api.deepseek.com/chat/completions"
        self.enable_ai_summary = self.config.get('ai_summary', {}).get('enabled', True)
        self.batch_size = self.config.get('ai_summary', {}).get('batch_size', 10)
        self.batch_delay = self.config.get('ai_summary', {}).get('batch_delay', 1.0)

        # 调试信息：检查API密钥
        if self.enable_ai_summary:
            if not self.deepseek_api_key:
                print("⚠️  警告: DEEPSEEK_API_KEY 未设置，AI摘要功能将被禁用")
                self.enable_ai_summary = False
            else:
                print(f"✅ DeepSeek API 已配置 (密钥长度: {len(self.deepseek_api_key)})")
                # 测试API连接
                self._test_api_connection()

    def _test_api_connection(self):
        """测试API连接是否正常"""
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.deepseek_api_key}"
            }

            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": "test"}],
                "max_tokens": 5,
                "temperature": 0.3
            }

            response = requests.post(
                self.deepseek_api_url,
                headers=headers,
                json=payload,
                timeout=10
            )

            if response.status_code == 200:
                print("✅ DeepSeek API 连接测试成功")
            else:
                print(f"⚠️  DeepSeek API 连接测试失败 ({response.status_code}): {response.text[:200]}")
                self.enable_ai_summary = False
        except Exception as e:
            print(f"⚠️  DeepSeek API 连接测试异常: {str(e)}")
            self.enable_ai_summary = False

    def _load_cache(self) -> Dict:
        """加载缓存（已处理的文章）- 新格式按日期组织"""
        if CACHE_FILE.exists():
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                cache = json.load(f)

                # 兼容旧格式：如果是旧的列表格式，转换为新格式
                if isinstance(cache.get('processed_urls'), list):
                    print("  🔄 检测到旧缓存格式，正在迁移...")
                    old_urls = cache['processed_urls']
                    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

                    # 将旧 URL 列表迁移到昨天的日期
                    cache = {
                        "by_date": {
                            yesterday: old_urls
                        },
                        "last_run": cache.get("last_run"),
                        "version": "2.0"
                    }
                    print(f"  ✅ 已迁移 {len(old_urls)} 个 URL 到 {yesterday}")

                return cache

        # 默认新格式
        return {
            "by_date": {},
            "last_run": None,
            "version": "2.0"
        }

    def _save_cache(self):
        """保存缓存"""
        self.cache["last_run"] = datetime.now().isoformat()
        self.cache["version"] = "2.0"

        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, indent=2, ensure_ascii=False)

    def _cleanup_old_cache(self, keep_days: int = 30):
        """清理超过指定天数的缓存

        Args:
            keep_days: 保留最近多少天的缓存（默认30天）
        """
        if "by_date" not in self.cache:
            return

        cutoff_date = datetime.now() - timedelta(days=keep_days)
        cutoff_str = cutoff_date.strftime('%Y-%m-%d')

        dates_to_remove = []
        for date_str in self.cache["by_date"].keys():
            if date_str < cutoff_str:
                dates_to_remove.append(date_str)

        if dates_to_remove:
            total_urls_removed = 0
            for date_str in dates_to_remove:
                urls_count = len(self.cache["by_date"][date_str])
                total_urls_removed += urls_count
                del self.cache["by_date"][date_str]

            print(f"  🧹 清理了 {len(dates_to_remove)} 天的旧缓存（{total_urls_removed} 个 URL）")
            print(f"     保留范围: {cutoff_str} 至今")

    def _get_all_cached_urls(self) -> Set[str]:
        """获取所有已缓存的 URL（跨所有日期）"""
        all_urls = set()
        if "by_date" in self.cache:
            for date_urls in self.cache["by_date"].values():
                all_urls.update(date_urls)
        return all_urls

    def _is_recent(self, published_parsed) -> bool:
        """检查文章是否在时间窗口内 - 使用配置的 days_lookback 参数"""
        if not published_parsed:
            return True  # 无日期信息，保守处理

        # 使用配置的时间窗口，去重由缓存机制处理
        days_lookback = self.config.get('filters', {}).get('days_lookback', 7)
        cutoff_date = datetime.now() - timedelta(days=days_lookback)

        article_date = datetime(*published_parsed[:6])

        # 检查文章是否在时间窗口内
        return article_date >= cutoff_date

    def _normalize_url(self, url: str) -> str:
        """标准化 URL（去除查询参数和 fragment）"""
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    def _calculate_similarity(self, title1: str, title2: str) -> float:
        """计算标题相似度（简单的 Jaccard 相似度）"""
        words1 = set(re.findall(r'\w+', title1.lower()))
        words2 = set(re.findall(r'\w+', title2.lower()))

        if not words1 or not words2:
            return 0.0

        intersection = words1 & words2
        union = words1 | words2
        return len(intersection) / len(union)

    def _calculate_days_ago(self, published_parsed) -> int:
        """计算文章发布距今的天数"""
        if not published_parsed:
            return None

        try:
            article_date = datetime(*published_parsed[:6])
            days = (datetime.now() - article_date).days
            return days
        except:
            return None

    def _clean_html(self, text: str) -> str:
        """清理文本中的 HTML 标签和特殊字符"""
        if not text:
            return ""

        # 移除 HTML 注释
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

        # 移除 HTML 标签
        text = re.sub(r'<[^>]+>', '', text)

        # 解码 HTML 实体
        import html
        text = html.unescape(text)

        # 合并多个空格
        text = re.sub(r'\s+', ' ', text)

        # 移除首尾空格
        text = text.strip()

        return text

    def _extract_arxiv_date(self, article: Dict) -> tuple:
        """从 arXiv 文章中提取实际提交日期"""
        # 仅对 arXiv 类型文章处理
        if article.get('type') != 'arxiv':
            return None, None

        # 从 summary 中提取 arXiv ID
        import re
        summary = article.get('summary', '')
        match = re.search(r'arXiv:(\d{4})\.(\d+)v\d+', summary)

        if match:
            arxiv_date = match.group(1)  # 例如 "2608"
            year = "20" + arxiv_date[:2]  # "2026"
            month = arxiv_date[2:4]       # "08"

            # 构造日期字符串
            date_str = f"{year}年{month}月"

            # 计算大致的天数（使用月份中间作为估算）
            try:
                arxiv_dt = datetime(int(year), int(month), 15)
                days_ago = (datetime.now() - arxiv_dt).days
                return date_str, days_ago
            except:
                return date_str, None

        return None, None

    def _is_duplicate(self, article: Dict) -> bool:
        """检查是否重复（URL 或高相似度标题）"""
        url = self._normalize_url(article['url'])

        # URL 去重 - 检查所有日期的缓存
        cached_urls = self._get_all_cached_urls()
        if url in self.seen_urls or url in cached_urls:
            return True

        # 标题相似度去重
        threshold = self.config.get('output', {}).get('similarity_threshold', 0.85)
        for existing in self.articles:
            similarity = self._calculate_similarity(article['title'], existing['title'])
            if similarity >= threshold:
                return True

        return False

    def _should_exclude(self, article: Dict) -> bool:
        """检查是否应该排除"""
        filters = self.config.get('filters', {})

        # 排除关键词检查
        exclude_keywords = filters.get('exclude_keywords', [])
        title_lower = article['title'].lower()
        summary_lower = article.get('summary', '').lower()

        for keyword in exclude_keywords:
            if keyword.lower() in title_lower or keyword.lower() in summary_lower:
                return True

        # 最小标题长度检查
        min_length = filters.get('min_title_length', 10)
        if len(article['title']) < min_length:
            return True

        return False

    def _match_keywords(self, article: Dict, keywords: List[str]) -> bool:
        """检查文章是否匹配关键词"""
        if not keywords:
            return True  # 无关键词限制，全部通过

        text = f"{article['title']} {article.get('summary', '')}".lower()
        return any(keyword.lower() in text for keyword in keywords)

    def _generate_ai_summary_and_category(self, article: Dict) -> tuple:
        """使用 DeepSeek API 生成文章摘要并分类（单篇，保留用于兼容性）"""
        if not self.enable_ai_summary:
            return None, None

        batch_result = self._generate_ai_summaries_batch([article])
        if batch_result and len(batch_result) > 0:
            return batch_result[0]
        return None, None

    def _generate_ai_summaries_batch(self, articles: List[Dict]) -> List[tuple]:
        """批量使用 DeepSeek API 生成文章摘要并分类

        根据文章的 tier 决定处理方式：
        - tier1: 只使用摘要总结（100字）
        - tier2/tier3/military: 获取全文后总结（200字）
        """
        if not self.enable_ai_summary or not articles:
            return [(None, None)] * len(articles)

        try:
            # 按 tier 分组文章
            tier1_articles = []
            other_articles = []

            for idx, article in enumerate(articles):
                tier = article.get('tier', 'tier2')
                if tier == 'tier1':
                    tier1_articles.append((idx, article))
                else:
                    other_articles.append((idx, article))

            results = [None] * len(articles)

            # 处理 tier1 文章（基于摘要，100字）
            if tier1_articles:
                print(f"     处理 tier1 文章: {len(tier1_articles)} 篇（基于摘要）")
                tier1_results = self._summarize_from_abstract(
                    [art for _, art in tier1_articles],
                    max_length=100
                )
                for (idx, _), result in zip(tier1_articles, tier1_results):
                    results[idx] = result

            # 处理其他 tier 文章（获取全文，200字）
            if other_articles:
                print(f"     处理 tier2/3/military 文章: {len(other_articles)} 篇（基于全文）")
                other_results = self._summarize_from_fulltext(
                    [art for _, art in other_articles],
                    max_length=200
                )
                for (idx, _), result in zip(other_articles, other_results):
                    results[idx] = result

            return results

        except Exception as e:
            print(f"⚠️  批量生成 AI 摘要和分类失败: {str(e)}")
            return [(None, None)] * len(articles)

    def _summarize_from_abstract(self, articles: List[Dict], max_length: int = 100) -> List[tuple]:
        """基于摘要生成总结（用于 tier1）"""
        try:
            # 构建批量 prompt
            articles_text = []
            for idx, article in enumerate(articles, 1):
                title = article.get('title', '')
                summary = article.get('summary', '')[:1000]  # 限制输入长度
                articles_text.append(f"文章 {idx}:\n标题：{title}\n摘要：{summary}\n")

            # 动态构建分类描述
            category_descriptions = []
            category_names = []
            for cat in self.categories:
                category_descriptions.append(f"   - {cat['name']}：{cat['description']}")
                category_names.append(cat['name'])

            category_list = '/'.join(category_names)
            category_count = len(category_names)

            prompt = f"""请分析以下 {len(articles)} 篇文章，为每篇文章完成两个任务：
1. 基于标题和摘要，生成一个简洁的中文总结（不超过{max_length}字）
2. 将文章分类到以下类别之一：
{chr(10).join(category_descriptions)}

文章列表：
{''.join(articles_text)}

请严格按照以下JSON数组格式返回（数组包含 {len(articles)} 个对象）：
[
  {{
    "article_id": 1,
    "summary": "{max_length}字以内的中文总结",
    "category": "{category_list}（{category_count}选一）"
  }},
  ...
]

只返回JSON数组，不要有其他内容。"""

            return self._call_deepseek_api(prompt, articles, max_length)

        except Exception as e:
            print(f"⚠️  基于摘要总结失败: {str(e)}")
            return [(None, None)] * len(articles)

    def _summarize_from_fulltext(self, articles: List[Dict], max_length: int = 200) -> List[tuple]:
        """基于全文生成总结（用于 tier2/tier3/military）"""
        try:
            # 获取全文
            articles_with_content = []
            for article in articles:
                url = article.get('url', '')
                title = article.get('title', '')

                # 尝试获取全文
                full_content = self._fetch_full_content(url)

                if full_content:
                    articles_with_content.append({
                        **article,
                        'full_content': full_content[:3000]  # 限制长度
                    })
                else:
                    # 全文获取失败，回退到摘要
                    articles_with_content.append(article)

            # 构建批量 prompt
            articles_text = []
            for idx, article in enumerate(articles_with_content, 1):
                title = article.get('title', '')

                if 'full_content' in article:
                    content = article['full_content']
                    articles_text.append(f"文章 {idx}:\n标题：{title}\n全文：{content}\n")
                else:
                    summary = article.get('summary', '')[:1000]
                    articles_text.append(f"文章 {idx}:\n标题：{title}\n摘要：{summary}\n")

            # 动态构建分类描述
            category_descriptions = []
            category_names = []
            for cat in self.categories:
                category_descriptions.append(f"   - {cat['name']}：{cat['description']}")
                category_names.append(cat['name'])

            category_list = '/'.join(category_names)
            category_count = len(category_names)

            prompt = f"""请分析以下 {len(articles_with_content)} 篇文章，为每篇文章完成两个任务：
1. 基于全文内容，生成一个详细的中文总结（不超过{max_length}字）
2. 将文章分类到以下类别之一：
{chr(10).join(category_descriptions)}

文章列表：
{''.join(articles_text)}

请严格按照以下JSON数组格式返回（数组包含 {len(articles_with_content)} 个对象）：
[
  {{
    "article_id": 1,
    "summary": "{max_length}字以内的中文总结",
    "category": "{category_list}（{category_count}选一）"
  }},
  ...
]

只返回JSON数组，不要有其他内容。"""

            return self._call_deepseek_api(prompt, articles_with_content, max_length)

        except Exception as e:
            print(f"⚠️  基于全文总结失败: {str(e)}")
            return [(None, None)] * len(articles)

    def _fetch_full_content(self, url: str) -> str:
        """获取文章全文（简化版）"""
        try:
            import requests
            from bs4 import BeautifulSoup

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # 移除脚本和样式
            for script in soup(["script", "style"]):
                script.decompose()

            # 提取文本
            text = soup.get_text(separator='\n', strip=True)

            # 清理空行
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            content = '\n'.join(lines)

            return content[:5000]  # 限制长度

        except Exception as e:
            # 全文获取失败，静默返回空
            return ""

    def _call_deepseek_api(self, prompt: str, articles: List[Dict], max_length: int) -> List[tuple]:
        """调用 DeepSeek API"""
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.deepseek_api_key}"
            }

            payload = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "你是一个专业的AI技术文章分析助手。请严格按照JSON格式返回结果。"},
                    {"role": "user", "content": prompt}
                ],
                "stream": False,
                "max_tokens": (max_length + 50) * len(articles),  # 每篇文章的 token 估算
                "temperature": 0.3
            }

            response = requests.post(
                self.deepseek_api_url,
                headers=headers,
                json=payload,
                timeout=60
            )

            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content'].strip()

                # 尝试解析 JSON
                # 移除可能的 markdown 代码块标记
                content = content.replace('```json', '').replace('```', '').strip()

                try:
                    parsed = json.loads(content)

                    # 确保返回的是数组
                    if not isinstance(parsed, list):
                        print(f"⚠️  返回的不是数组格式，使用默认值")
                        return [(None, None)] * len(articles)

                    # 构建结果
                    results = []
                    for i, article in enumerate(articles):
                        # 查找对应的结果
                        article_result = None
                        for item in parsed:
                            if item.get('article_id') == i + 1:
                                article_result = item
                                break

                        if article_result:
                            ai_summary = article_result.get('summary', '').strip()
                            category = article_result.get('category', self.category_key_to_name[self.default_category]).strip()
                            category_key = self.category_name_to_key.get(category, self.default_category)
                            results.append((ai_summary, category_key))
                        else:
                            results.append((None, None))

                    return results

                except json.JSONDecodeError as e:
                    print(f"⚠️  JSON 解析失败: {str(e)}")
                    print(f"    响应内容: {content[:200]}...")
                    return [(None, None)] * len(articles)
            else:
                print(f"⚠️  DeepSeek API 错误 ({response.status_code}): {response.text}")
                return [(None, None)] * len(articles)

        except Exception as e:
            print(f"⚠️  API 调用失败: {str(e)}")
            return [(None, None)] * len(articles)

    def fetch_feed(self, feed_config: Dict, tier: str):
        """抓取单个 feed"""
        try:
            print(f"📡 抓取: {feed_config['name']} ({feed_config['url']})")
            feed = feedparser.parse(feed_config['url'])

            if feed.bozo and feed.bozo_exception:
                print(f"⚠️  警告: {feed_config['name']} - {feed.bozo_exception}")
                return

            # 先收集所有符合条件的文章
            pending_articles = []

            for entry in feed.entries:
                # 基本信息提取
                article = {
                    'title': entry.get('title', 'Untitled'),
                    'url': entry.get('link', ''),
                    'summary': entry.get('summary', entry.get('description', '')),
                    'published': entry.get('published', entry.get('updated', '')),
                    'published_raw': entry.get('published_parsed'),
                    'source': feed_config['name'],
                    'tier': tier,
                    'type': feed_config.get('type', 'blog'),
                    'priority': feed_config.get('priority', 'medium'),
                }

                # 时间过滤
                if not self._is_recent(entry.get('published_parsed')):
                    continue

                # 排除规则检查
                if self._should_exclude(article):
                    continue

                # 关键词匹配检查
                if not self._match_keywords(article, feed_config.get('keywords', [])):
                    continue

                # 去重检查
                if self._is_duplicate(article):
                    continue

                pending_articles.append(article)

            # 批量处理 AI 摘要和分类
            if self.enable_ai_summary and pending_articles:
                print(f"  🤖 批量分析 {len(pending_articles)} 篇文章...")

                # 分批处理
                for i in range(0, len(pending_articles), self.batch_size):
                    batch = pending_articles[i:i + self.batch_size]
                    batch_num = i // self.batch_size + 1
                    total_batches = (len(pending_articles) + self.batch_size - 1) // self.batch_size

                    print(f"     批次 {batch_num}/{total_batches}: {len(batch)} 篇")

                    results = self._generate_ai_summaries_batch(batch)

                    # 将结果应用到文章
                    for article, (ai_summary, category) in zip(batch, results):
                        if ai_summary:
                            article['ai_summary'] = ai_summary
                        if category:
                            article['category'] = category

                    # 批次间延迟
                    if i + self.batch_size < len(pending_articles):
                        time.sleep(self.batch_delay)

            # 添加所有文章到结果
            for article in pending_articles:
                self.articles.append(article)
                self.seen_urls.add(self._normalize_url(article['url']))

            print(f"✅ {feed_config['name']}: {len(pending_articles)} 篇新文章")

        except Exception as e:
            print(f"❌ 错误: {feed_config['name']} - {str(e)}")

    def fetch_all(self):
        """抓取所有 feeds"""
        print(f"\n🚀 开始抓取 RSS feeds - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        # 首先抓取自定义网页源（DeepSeek, Qwen 博客）
        print(f"\n{'='*60}")
        print(f"🕷️  自定义网页爬取")
        print(f"{'='*60}\n")

        try:
            days = self.config.get('filters', {}).get('days_lookback', 7)
            custom_articles = scrape_all_custom_sources(days_lookback=days)

            # 收集需要 AI 分析的文章
            pending_articles = []

            for article in custom_articles:
                # 设置 tier（自定义源归为 tier1）
                article['tier'] = 'tier1'

                # 排除规则检查
                if self._should_exclude(article):
                    continue

                # 去重检查
                if self._is_duplicate(article):
                    continue

                pending_articles.append(article)

            # 批量生成 AI 摘要和分类
            if self.enable_ai_summary and pending_articles:
                print(f"  🤖 批量分析 {len(pending_articles)} 篇文章...")

                for i in range(0, len(pending_articles), self.batch_size):
                    batch = pending_articles[i:i + self.batch_size]
                    batch_num = i // self.batch_size + 1
                    total_batches = (len(pending_articles) + self.batch_size - 1) // self.batch_size

                    print(f"     批次 {batch_num}/{total_batches}: {len(batch)} 篇")

                    results = self._generate_ai_summaries_batch(batch)

                    for article, (ai_summary, category) in zip(batch, results):
                        if ai_summary:
                            article['ai_summary'] = ai_summary
                        if category:
                            article['category'] = category

                    if i + self.batch_size < len(pending_articles):
                        time.sleep(self.batch_delay)

            # 添加到结果
            for article in pending_articles:
                self.articles.append(article)
                self.seen_urls.add(self._normalize_url(article['url']))

            print(f"✅ 自定义网页爬取: {len(pending_articles)} 篇文章")

        except Exception as e:
            print(f"❌ 自定义网页爬取失败: {str(e)}")

        # 爬取军事新闻网站（无RSS）
        try:
            days = self.config.get('filters', {}).get('days_lookback', 7)
            military_articles = scrape_military_sources(days_lookback=days)

            # 收集需要 AI 分析的文章
            pending_articles = []

            for article in military_articles:
                # 设置 tier（军事源归为 military）
                article['tier'] = 'military'

                # 排除规则检查
                if self._should_exclude(article):
                    continue

                # 去重检查
                if self._is_duplicate(article):
                    continue

                pending_articles.append(article)

            # 批量生成 AI 摘要和分类
            if self.enable_ai_summary and pending_articles:
                print(f"  🤖 批量分析 {len(pending_articles)} 篇文章...")

                for i in range(0, len(pending_articles), self.batch_size):
                    batch = pending_articles[i:i + self.batch_size]
                    batch_num = i // self.batch_size + 1
                    total_batches = (len(pending_articles) + self.batch_size - 1) // self.batch_size

                    print(f"     批次 {batch_num}/{total_batches}: {len(batch)} 篇")

                    results = self._generate_ai_summaries_batch(batch)

                    for article, (ai_summary, category) in zip(batch, results):
                        if ai_summary:
                            article['ai_summary'] = ai_summary
                        if category:
                            article['category'] = category

                    if i + self.batch_size < len(pending_articles):
                        time.sleep(self.batch_delay)

            # 添加到结果
            for article in pending_articles:
                self.articles.append(article)
                self.seen_urls.add(self._normalize_url(article['url']))

        except Exception as e:
            print(f"❌ 军事新闻爬取失败: {str(e)}")

        # 然后抓取 RSS feeds
        for tier in ['tier1', 'tier2', 'tier3', 'military']:
            feeds = self.config.get(tier, [])
            if feeds:
                print(f"\n{'='*60}")
                print(f"📂 {tier.upper()} ({len(feeds)} 个信源)")
                print(f"{'='*60}\n")

                for feed in feeds:
                    self.fetch_feed(feed, tier)

        print(f"\n{'='*60}")
        print(f"📊 总计: {len(self.articles)} 篇新文章")
        print(f"{'='*60}\n")

    def generate_report(self) -> Dict[str, str]:
        """生成 Markdown 报告，按分类分组"""
        if not self.articles:
            return {"all": "# RSS 聚合报告\n\n本次运行未发现新文章。\n"}

        # 从配置构建分类字典
        categories = {}
        for cat in self.categories:
            categories[cat['key']] = {
                'name': cat['name'],
                'articles': []
            }

        # 添加未分类类别（如果启用）
        if self.enable_uncategorized:
            categories['uncategorized'] = {'name': '未分类', 'articles': []}

        # 按分类分组文章
        for article in self.articles:
            category = article.get('category', 'uncategorized')
            if category not in categories:
                category = 'uncategorized'
            categories[category]['articles'].append(article)

        # 生成报告字典
        reports = {}

        # 生成总报告
        all_report = self._generate_full_report(categories)
        reports['all'] = all_report

        # 为每个分类生成独立报告
        for cat_key, cat_data in categories.items():
            if cat_data['articles']:
                cat_report = self._generate_category_report(cat_key, cat_data)
                reports[cat_key] = cat_report

        return reports

    def _generate_full_report(self, categories: Dict) -> str:
        """生成完整报告"""
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

        report = []
        report.append(f"# RSS 聚合报告 - {yesterday}")
        report.append(f"\n**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**报告日期**: {yesterday} (昨天)")
        report.append(f"**新发现文章**: {len(self.articles)} 篇\n")

        # 统计各分类数量
        report.append("## 📊 分类统计\n")
        for cat_key, cat_data in categories.items():
            count = len(cat_data['articles'])
            if count > 0:
                report.append(f"- **{cat_data['name']}**: {count} 篇")

        report.append("\n---\n")

        # 按分类显示文章
        for cat_key, cat_data in categories.items():
            if not cat_data['articles']:
                continue

            report.append(f"## 🏷️  {cat_data['name']}")
            report.append(f"\n**{len(cat_data['articles'])} 篇文章**\n")

            self._append_articles(report, cat_data['articles'])

        # 添加下一步建议
        self._append_next_steps(report)

        return '\n'.join(report)

    def _generate_category_report(self, cat_key: str, cat_data: Dict) -> str:
        """生成单个分类的报告"""
        report = []
        report.append(f"# RSS 聚合报告 - {cat_data['name']}")
        report.append(f"\n**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**文章数量**: {len(cat_data['articles'])} 篇\n")
        report.append("---\n")

        self._append_articles(report, cat_data['articles'])
        self._append_next_steps(report)

        return '\n'.join(report)

    def _append_articles(self, report: List[str], articles: List[Dict]):
        """将文章列表添加到报告中"""
        # 按 tier 和优先级排序
        articles_sorted = sorted(articles, key=lambda x: (
            {'tier1': 0, 'tier2': 1, 'tier3': 2}.get(x.get('tier', 'tier2'), 1),
            {'high': 0, 'medium': 1, 'low': 2}.get(x.get('priority', 'medium'), 1),
            x['published']
        ), reverse=True)

        for i, article in enumerate(articles_sorted, 1):
            report.append(f"### {i}. {article['title']}")
            report.append(f"- **来源**: {article['source']} ({article['tier'].upper()})")

            # 格式化日期显示
            published_date = article['published']

            # 对于 arXiv 文章，尝试提取实际提交日期
            arxiv_date, arxiv_days = self._extract_arxiv_date(article)

            if arxiv_date:
                # arXiv 文章：显示实际提交月份
                if arxiv_days is not None and arxiv_days <= 30:
                    date_display = f"{arxiv_date} (约 {arxiv_days} 天前)"
                else:
                    date_display = arxiv_date
                report.append(f"- **提交时间**: {date_display}")
            else:
                # 其他文章：显示 RSS 发布日期
                days_ago = self._calculate_days_ago(article.get('published_raw'))
                if days_ago is not None:
                    if days_ago == 0:
                        date_display = f"{published_date} (今天)"
                    elif days_ago == 1:
                        date_display = f"{published_date} (昨天)"
                    elif days_ago <= 7:
                        date_display = f"{published_date} ({days_ago} 天前)"
                    else:
                        date_display = published_date
                else:
                    date_display = published_date

                report.append(f"- **发布日期**: {date_display}")

            report.append(f"- **类型**: {article['type']}")
            report.append(f"- **优先级**: {article.get('priority', 'medium')}")

            # 显示分类
            if article.get('category'):
                category_display = self.category_key_to_name.get(article['category'], article['category'])
                report.append(f"- **分类**: {category_display}")

            report.append(f"- **链接**: {article['url']}")

            # AI 生成的摘要（优先显示）
            if article.get('ai_summary'):
                report.append(f"- **AI 摘要**: {article['ai_summary']}")

            # 原始摘要（作为补充）
            if article.get('summary'):
                # 清理 HTML 标签
                summary = self._clean_html(article['summary'])
                # 截取摘要前200字符
                summary = summary[:200].strip()
                if len(article['summary']) > 200:
                    summary += "..."
                # 只有清理后还有内容才显示
                if summary and summary != "...":
                    report.append(f"- **原始摘要**: {summary}")

            report.append("")  # 空行

    def _append_next_steps(self, report: List[str]):
        """添加下一步行动建议"""
        report.append("---\n")
        report.append("## 📋 下一步行动")
        report.append("\n1. **人工审查**: 阅读上述文章，标记高价值候选")
        report.append("2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B")
        report.append("3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill")
        report.append("\n**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。\n")

    def save_report(self, reports: Dict[str, str]):
        """保存报告到文件，按日期目录分别保存"""
        REPORT_DIR.mkdir(exist_ok=True)

        # 使用昨天的日期作为目录名
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        date_dir = REPORT_DIR / yesterday
        date_dir.mkdir(exist_ok=True)

        saved_files = []

        # 保存总报告
        filename = f"rss-aggregation-{yesterday}.md"
        filepath = date_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(reports['all'])
        saved_files.append(('全部文章', filepath))

        # 保存分类报告
        for cat in self.categories:
            cat_key = cat['key']
            cat_name = cat['name']
            if cat_key in reports:
                filename = f"rss-aggregation-{yesterday}-{cat_name}.md"
                filepath = date_dir / filename
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(reports[cat_key])
                saved_files.append((cat_name, filepath))

        # 保存未分类报告（如果启用且存在）
        if self.enable_uncategorized and 'uncategorized' in reports:
            filename = f"rss-aggregation-{yesterday}-未分类.md"
            filepath = date_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(reports['uncategorized'])
            saved_files.append(('未分类', filepath))

        print(f"\n{'='*60}")
        print(f"✅ 报告已保存到: {date_dir}")
        print(f"{'='*60}")
        for name, path in saved_files:
            print(f"   📄 {name}: {path.name}")
        print(f"{'='*60}")

        # 更新缓存 - 按日期保存
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

        if yesterday not in self.cache['by_date']:
            self.cache['by_date'][yesterday] = []

        for article in self.articles:
            url = self._normalize_url(article['url'])
            if url not in self.cache['by_date'][yesterday]:
                self.cache['by_date'][yesterday].append(url)

        # 清理超过30天的旧缓存
        self._cleanup_old_cache(keep_days=30)

        self._save_cache()

        # 统计缓存信息
        total_urls = sum(len(urls) for urls in self.cache['by_date'].values())
        date_count = len(self.cache['by_date'])

        print(f"✅ 缓存已更新:")
        print(f"   • 今日新增: {len(self.articles)} 个 URL")
        print(f"   • 总计: {total_urls} 个 URL，跨 {date_count} 天")
        print(f"   • 缓存日期范围: {min(self.cache['by_date'].keys())} 至 {max(self.cache['by_date'].keys())}")

def main():
    """主函数 - 每日运行，获取昨天的文章"""
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    print("="*60)
    print(f"📰 AI技术追踪 - 每日报告")
    print(f"📅 报告日期: {yesterday} (昨天)")
    print(f"🕐 运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60 + "\n")

    if not CONFIG_FILE.exists():
        print(f"❌ 配置文件不存在: {CONFIG_FILE}")
        return

    aggregator = RSSAggregator(CONFIG_FILE)
    aggregator.fetch_all()

    reports = aggregator.generate_report()
    print("\n" + "="*60)
    print(f"📄 报告预览 - {yesterday}")
    print("="*60 + "\n")
    print(reports['all'][:500] + "...\n")

    aggregator.save_report(reports)

    print(f"\n🎉 完成! 昨天({yesterday})的文章已整理完毕")

if __name__ == "__main__":
    main()
