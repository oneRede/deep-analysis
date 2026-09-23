#!/usr/bin/env python3
"""
本地模型分类器 - 使用 Ollama 运行开源模型进行文章分类和摘要生成
支持的模型: qwen2.5:3b, llama3.2:3b, gemma2:2b
"""

import requests
import json
import re
from typing import List, Dict, Tuple, Optional
import time


class LocalClassifier:
    """本地模型分类器，使用 Ollama API"""

    # 高置信度来源 → 分类名提示，避免小模型把所有内容都归入 AI应用
    SOURCE_HINTS = [
        ("cs.RO", "具身智能"),
        ("机器人", "具身智能"),
        ("cs.AR", "AI芯片"),
        ("硬件架构", "AI芯片"),
        ("cs.PL", "编译器"),
        ("编程语言", "编译器"),
        ("physics.optics", "光计算"),
        ("光学", "光计算"),
        ("Defense News", "军事技术"),
        ("Military Times", "军事技术"),
        ("Breaking Defense", "军事技术"),
        ("Stars and Stripes", "军事技术"),
        ("Military.com", "军事技术"),
        ("The War Zone", "军事技术"),
        ("Army Technology", "军事技术"),
        ("Jane", "军事技术"),
        ("环球网", "军事技术"),
        ("Bloomberg Markets", "经济"),
        ("Bloomberg Economics", "经济"),
        ("Financial Times", "经济"),
        ("Wall Street Journal Markets", "经济"),
        ("Wall Street Journal US Business", "经济"),
        ("Economist Business", "经济"),
        ("Economist Finance", "经济"),
        ("CNBC Top News", "经济"),
        ("New York Times Business", "经济"),
        ("Bloomberg Politics", "时政"),
        ("CNBC World News", "时政"),
        ("New York Times World", "时政"),
        ("New York Times HomePage", "时政"),
        ("Economist International", "时政"),
        ("Economist - The World", "时政"),
        ("Wall Street Journal World", "时政"),
    ]

    # 无 routing_rules 配置时的内置兜底规则
    DEFAULT_ROUTING_RULES = [
        "与机器人/机械臂/人形机器人/运动控制/操作/导航/自动驾驶相关 → 具身智能",
        "发布新模型、模型架构、训练方法、参数规模、MoE/RLHF/蒸馏/量化相关 → AI模型",
        "基准测试(benchmark)/评估/部署/推理服务/工具链/Agent框架/RAG系统相关 → Harness工程",
        "芯片/加速器/GPU/HBM/ASIC/NPU/存算一体/半导体制造相关 → AI芯片",
        "编译器/IR/JIT/静态分析/代码生成相关 → 编译器",
        "光子/光芯片/硅光/光神经网络/光互连相关 → 光计算",
        "军事装备/武器系统/国防/军队/军事行动相关 → 军事技术",
        "金融/股市/债券/IPO/通胀/央行/商业/企业财报相关 → 经济",
        "国际政治/外交/政府决策/选举/制裁/国家安全相关 → 时政",
        "仅当文章是 AI 在具体行业落地的产品/解决方案时才 → AI应用",
    ]

    def __init__(
        self,
        model: str = "qwen2.5:3b",
        base_url: str = "http://localhost:11434",
        temperature: float = 0.3,
        timeout: int = 60
    ):
        """
        初始化本地分类器

        Args:
            model: Ollama 模型名称，推荐 qwen2.5:3b 或 llama3.2:3b
            base_url: Ollama API 地址
            temperature: 生成温度 (0-1)
            timeout: 请求超时时间（秒）
        """
        self.model = model
        self.base_url = base_url
        self.api_url = f"{base_url}/api/generate"
        self.temperature = temperature
        self.timeout = timeout

    def test_connection(self) -> bool:
        """测试 Ollama 连接是否正常"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get('models', [])
                model_names = [m['name'] for m in models]

                if self.model in model_names:
                    print(f"✅ Ollama 连接成功，模型 {self.model} 可用")
                    return True
                else:
                    print(f"⚠️  模型 {self.model} 未安装")
                    print(f"   可用模型: {', '.join(model_names)}")
                    print(f"   安装命令: ollama pull {self.model}")
                    return False
            return False
        except Exception as e:
            print(f"⚠️  Ollama 连接失败: {str(e)}")
            print(f"   请确保 Ollama 已启动: https://ollama.com")
            return False

    def _call_ollama(self, prompt: str, system_prompt: str = None) -> Optional[str]:
        """调用 Ollama API"""
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": self.temperature,
                    "num_predict": 512,  # 最大生成长度
                }
            }

            if system_prompt:
                payload["system"] = system_prompt

            response = requests.post(
                self.api_url,
                json=payload,
                timeout=self.timeout
            )

            if response.status_code == 200:
                result = response.json()
                return result.get('response', '').strip()
            else:
                print(f"⚠️  Ollama API 错误 ({response.status_code}): {response.text[:200]}")
                return None

        except Exception as e:
            print(f"⚠️  Ollama API 调用失败: {str(e)}")
            return None

    def _build_routing_block(self, routing_rules: Optional[List[str]]) -> str:
        """构建分类路由规则文本"""
        rules = routing_rules or self.DEFAULT_ROUTING_RULES
        return "\n".join(f"{i}. {rule}" for i, rule in enumerate(rules, 1))

    def _build_source_hint(self, article: Dict) -> str:
        """根据来源给出分类提示，帮助小模型避免一律归入 AI应用"""
        source = article.get('source', '') or ''
        for needle, category_name in self.SOURCE_HINTS:
            if needle in source:
                return (
                    f"\n来源提示：该文章来自「{source}」，通常属于「{category_name}」，"
                    f"若无明显理由请优先归入该类别。\n"
                )
        return ""

    def _resolve_category_key(
        self, category_name: str, name_to_key: Dict[str, str], default_category: str
    ) -> str:
        """把模型返回的分类名解析为分类 key，容忍空白/引号/轻微偏差"""
        normalized = (category_name or '').strip().strip('"').strip("'").strip()
        if normalized in name_to_key:
            return name_to_key[normalized]
        for name, key in name_to_key.items():
            if name in normalized or normalized in name:
                return key
        return default_category

    def _parse_json_response(self, response: str) -> Optional[Dict]:
        """从模型响应中稳健地提取 JSON 对象"""
        if not response:
            return None

        cleaned = response.replace('```json', '').replace('```', '').strip()

        start = cleaned.find('{')
        end = cleaned.rfind('}')
        candidate = cleaned[start:end + 1] if start != -1 and end > start else cleaned

        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            # 修复非法的反斜杠转义（小模型常见问题）
            fixed = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', candidate)
            try:
                return json.loads(fixed)
            except json.JSONDecodeError:
                return None

    def classify_and_summarize_batch(
        self,
        articles: List[Dict],
        categories: List[Dict],
        default_category: str,
        max_length: int = 200,
        routing_rules: Optional[List[str]] = None
    ) -> List[Tuple[Optional[str], Optional[str]]]:
        """
        批量分类和生成摘要

        Args:
            articles: 文章列表
            categories: 分类配置列表
            default_category: 默认分类 key
            max_length: 摘要最大长度
            routing_rules: 分类路由规则（来自 categories.yml）

        Returns:
            List of (summary, category_key) tuples
        """
        results = []

        # 构建分类描述
        category_descriptions = []
        for cat in categories:
            category_descriptions.append(f"   - {cat['name']}：{cat['description']}")

        category_name_to_key = {cat['name']: cat['key'] for cat in categories}
        routing_block = self._build_routing_block(routing_rules)

        system_prompt = "你是一个专业的AI技术文章分析助手。请严格按照JSON格式返回结果。"

        # 逐篇处理（本地模型通常不适合大批量）
        for idx, article in enumerate(articles, 1):
            print(f"       处理 {idx}/{len(articles)}: {article.get('title', '')[:50]}...")

            title = article.get('title', '')

            # 根据是否有全文内容选择不同的 prompt
            if 'full_content' in article:
                content = article['full_content'][:2000]  # 限制长度
                content_type = "全文"
            else:
                content = article.get('summary', '')[:1000]
                content_type = "摘要"

            source_hint = self._build_source_hint(article)

            prompt = f"""你是专业的AI技术文章分类助手。请先判断文章主题，再选择最贴切的类别。

分类路由规则（按优先级判断）：
{routing_block}
注意：AI应用不是兜底类别。无法归入上述具体类别时优先考虑 AI模型 或 Harness工程，只有确实是 AI 在具体行业落地的产品/解决方案时才选 AI应用。
{source_hint}
可选类别：
{chr(10).join(category_descriptions)}

文章信息：
标题：{title}
{content_type}：{content}

请只返回JSON对象（不要有markdown代码块标记）：
{{
  "summary": "{max_length}字以内的中文总结",
  "category": "类别名称"
}}

只返回JSON对象，不要有其他内容。"""

            response = self._call_ollama(prompt, system_prompt)

            parsed = self._parse_json_response(response) if response else None

            if parsed:
                summary = (parsed.get('summary') or '').strip()
                category_name = parsed.get('category') or ''
                category_key = self._resolve_category_key(
                    category_name, category_name_to_key, default_category
                )

                # 截断过长的摘要
                if len(summary) > max_length + 50:
                    summary = summary[:max_length] + "..."

                results.append((summary, category_key))
            else:
                if response:
                    print(f"⚠️  JSON 解析失败: {response[:200]}...")
                results.append((None, None))

            # 短暂延迟，避免过载
            time.sleep(0.1)

        return results

    def classify_and_summarize_single(
        self,
        article: Dict,
        categories: List[Dict],
        default_category: str,
        max_length: int = 200,
        routing_rules: Optional[List[str]] = None
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        单篇文章分类和生成摘要

        Args:
            article: 文章字典
            categories: 分类配置列表
            default_category: 默认分类 key
            max_length: 摘要最大长度
            routing_rules: 分类路由规则（来自 categories.yml）

        Returns:
            (summary, category_key) tuple
        """
        results = self.classify_and_summarize_batch(
            [article],
            categories,
            default_category,
            max_length,
            routing_rules
        )
        return results[0] if results else (None, None)


def get_recommended_model() -> str:
    """
    获取推荐的模型

    优先级：
    1. qwen2.5:3b - 中文表现最好，速度快
    2. llama3.2:3b - 英文强，中文可用
    3. gemma2:2b - 最轻量，速度最快
    """
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [m['name'] for m in models]

            # 按优先级检查
            preferences = [
                'qwen2.5:3b',
                'qwen2.5:1.5b',
                'llama3.2:3b',
                'llama3.2:1b',
                'gemma2:2b'
            ]

            for model in preferences:
                if model in model_names:
                    return model

            # 如果没有推荐的，返回第一个可用的
            if model_names:
                return model_names[0]
    except:
        pass

    return "qwen2.5:3b"  # 默认返回


if __name__ == "__main__":
    """测试本地分类器"""
    print("="*60)
    print("🧪 本地分类器测试")
    print("="*60 + "\n")

    # 测试文章
    test_article = {
        'title': 'OpenAI 发布 GPT-5 大模型',
        'summary': 'OpenAI 今天发布了最新的 GPT-5 大语言模型，该模型在推理、编程和多模态理解方面有显著提升。',
        'url': 'https://example.com/gpt5'
    }

    # 测试分类
    test_categories = [
        {'key': 'ai_model', 'name': 'AI模型', 'description': '关于新模型、模型架构、训练方法、模型优化'},
        {'key': 'ai_application', 'name': 'AI应用', 'description': '关于AI在实际场景中的应用、产品、解决方案'},
    ]

    model = get_recommended_model()
    print(f"📦 使用模型: {model}\n")

    classifier = LocalClassifier(model=model)

    if classifier.test_connection():
        print("\n开始分类测试...\n")
        summary, category = classifier.classify_and_summarize_single(
            test_article,
            test_categories,
            'ai_application'
        )

        print(f"✅ 分类结果:")
        print(f"   摘要: {summary}")
        print(f"   分类: {category}")
    else:
        print("\n❌ 测试失败: 无法连接到 Ollama")
        print("\n安装步骤:")
        print("1. 访问 https://ollama.com 下载安装 Ollama")
        print(f"2. 运行: ollama pull {model}")
        print("3. 确保 Ollama 服务已启动")
