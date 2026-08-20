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
import requests
import time
from web_scraper import scrape_all_custom_sources

# 配置路径
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
CONFIG_FILE = ROOT_DIR / "config" / "feeds.yml"
CATEGORIES_FILE = ROOT_DIR / "config" / "categories.yml"
REPORT_DIR = ROOT_DIR / "report"
CACHE_FILE = SCRIPT_DIR / ".rss-cache.json"

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
        self.deepseek_api_key = os.getenv('DEEPSEEK_API_KEY', '')
        self.deepseek_api_url = "https://api.deepseek.com/chat/completions"
        self.enable_ai_summary = self.config.get('ai_summary', {}).get('enabled', True)

    def _load_cache(self) -> Dict:
        """加载缓存（已处理的文章）"""
        if CACHE_FILE.exists():
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"processed_urls": [], "last_run": None}

    def _save_cache(self):
        """保存缓存"""
        self.cache["last_run"] = datetime.now().isoformat()
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, indent=2, ensure_ascii=False)

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

        # URL 去重
        if url in self.seen_urls or url in self.cache['processed_urls']:
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
        """使用 DeepSeek API 生成文章摘要并分类"""
        if not self.enable_ai_summary:
            return None, None

        try:
            # 构建 prompt
            title = article.get('title', '')
            summary = article.get('summary', '')[:500]  # 限制输入长度

            # 动态构建分类描述
            category_descriptions = []
            category_names = []
            for cat in self.categories:
                category_descriptions.append(f"   - {cat['name']}：{cat['description']}")
                category_names.append(cat['name'])

            category_list = '/'.join(category_names)
            category_count = len(category_names)

            prompt = f"""请分析以下文章并完成两个任务：

文章标题：{title}

文章摘要：{summary}

任务：
1. 生成一个简洁的中文摘要（不超过100字）
2. 将文章分类到以下类别之一：
{chr(10).join(category_descriptions)}

请严格按照以下JSON格式返回：
{{
  "summary": "100字以内的中文摘要",
  "category": "{category_list}（{category_count}选一）"
}}

只返回JSON，不要有其他内容。"""

            # 调用 DeepSeek API
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
                "max_tokens": 300,
                "temperature": 0.3
            }

            response = requests.post(
                self.deepseek_api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content'].strip()

                # 尝试解析 JSON
                # 移除可能的 markdown 代码块标记
                content = content.replace('```json', '').replace('```', '').strip()

                try:
                    parsed = json.loads(content)
                    ai_summary = parsed.get('summary', '').strip()
                    category = parsed.get('category', self.category_key_to_name[self.default_category]).strip()

                    # 使用配置的分类映射
                    category_key = self.category_name_to_key.get(category, self.default_category)

                    return ai_summary, category_key
                except json.JSONDecodeError:
                    print(f"⚠️  JSON 解析失败: {content}")
                    return None, None
            else:
                print(f"⚠️  DeepSeek API 错误 ({response.status_code}): {response.text}")
                return None, None

        except Exception as e:
            print(f"⚠️  生成 AI 摘要和分类失败: {str(e)}")
            return None, None


    def fetch_feed(self, feed_config: Dict, tier: str):
        """抓取单个 feed"""
        try:
            print(f"📡 抓取: {feed_config['name']} ({feed_config['url']})")
            feed = feedparser.parse(feed_config['url'])

            if feed.bozo and feed.bozo_exception:
                print(f"⚠️  警告: {feed_config['name']} - {feed.bozo_exception}")
                return

            count = 0
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

                # 生成 AI 摘要和分类
                if self.enable_ai_summary:
                    print(f"  🤖 分析文章: {article['title'][:50]}...")
                    ai_summary, category = self._generate_ai_summary_and_category(article)
                    if ai_summary:
                        article['ai_summary'] = ai_summary
                    if category:
                        article['category'] = category
                    time.sleep(0.5)  # 避免 API 调用过快

                # 添加到结果
                self.articles.append(article)
                self.seen_urls.add(self._normalize_url(article['url']))
                count += 1

            print(f"✅ {feed_config['name']}: {count} 篇新文章")

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

            for article in custom_articles:
                # 设置 tier（自定义源归为 tier1）
                article['tier'] = 'tier1'

                # 排除规则检查
                if self._should_exclude(article):
                    continue

                # 去重检查
                if self._is_duplicate(article):
                    continue

                # 生成 AI 摘要和分类
                if self.enable_ai_summary:
                    print(f"  🤖 分析文章: {article['title'][:50]}...")
                    ai_summary, category = self._generate_ai_summary_and_category(article)
                    if ai_summary:
                        article['ai_summary'] = ai_summary
                    if category:
                        article['category'] = category
                    time.sleep(0.5)

                # 添加到结果
                self.articles.append(article)
                self.seen_urls.add(self._normalize_url(article['url']))

            print(f"✅ 自定义网页爬取: {len(custom_articles)} 篇文章")

        except Exception as e:
            print(f"❌ 自定义网页爬取失败: {str(e)}")

        # 然后抓取 RSS feeds
        for tier in ['tier1', 'tier2', 'tier3']:
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

        # 更新缓存
        for article in self.articles:
            url = self._normalize_url(article['url'])
            if url not in self.cache['processed_urls']:
                self.cache['processed_urls'].append(url)

        self._save_cache()
        print(f"✅ 缓存已更新: {len(self.cache['processed_urls'])} 个已处理 URL")

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
