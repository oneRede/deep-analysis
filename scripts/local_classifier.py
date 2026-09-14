#!/usr/bin/env python3
"""
本地模型分类器 - 使用 Ollama 运行开源模型进行文章分类和摘要生成
支持的模型: qwen2.5:3b, llama3.2:3b, gemma2:2b
"""

import requests
import json
from typing import List, Dict, Tuple, Optional
import time


class LocalClassifier:
    """本地模型分类器，使用 Ollama API"""

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

    def classify_and_summarize_batch(
        self,
        articles: List[Dict],
        categories: List[Dict],
        default_category: str,
        max_length: int = 200
    ) -> List[Tuple[Optional[str], Optional[str]]]:
        """
        批量分类和生成摘要

        Args:
            articles: 文章列表
            categories: 分类配置列表
            default_category: 默认分类 key
            max_length: 摘要最大长度

        Returns:
            List of (summary, category_key) tuples
        """
        results = []

        # 构建分类描述
        category_descriptions = []
        category_names = []
        for cat in categories:
            category_descriptions.append(f"   - {cat['name']}：{cat['description']}")
            category_names.append(cat['name'])

        category_name_to_key = {cat['name']: cat['key'] for cat in categories}
        category_key_to_name = {cat['key']: cat['name'] for cat in categories}

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

            prompt = f"""请分析以下文章，完成两个任务：
1. 生成一个简洁的中文总结（{max_length}字以内）
2. 将文章分类到以下类别之一：
{chr(10).join(category_descriptions)}

文章信息：
标题：{title}
{content_type}：{content}

请严格按照以下JSON格式返回（不要有markdown代码块标记）：
{{
  "summary": "简洁的中文总结",
  "category": "类别名称"
}}

只返回JSON对象，不要有其他内容。"""

            response = self._call_ollama(prompt, system_prompt)

            if response:
                try:
                    # 清理可能的 markdown 代码块标记
                    response = response.replace('```json', '').replace('```', '').strip()

                    # 尝试解析 JSON
                    parsed = json.loads(response)

                    summary = parsed.get('summary', '').strip()
                    category_name = parsed.get('category', '').strip()

                    # 转换分类名称为 key
                    category_key = category_name_to_key.get(
                        category_name,
                        default_category
                    )

                    # 截断过长的摘要
                    if len(summary) > max_length + 50:
                        summary = summary[:max_length] + "..."

                    results.append((summary, category_key))

                except json.JSONDecodeError as e:
                    print(f"⚠️  JSON 解析失败: {str(e)}")
                    print(f"    响应内容: {response[:200]}...")
                    results.append((None, None))
            else:
                results.append((None, None))

            # 短暂延迟，避免过载
            time.sleep(0.1)

        return results

    def classify_and_summarize_single(
        self,
        article: Dict,
        categories: List[Dict],
        default_category: str,
        max_length: int = 200
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        单篇文章分类和生成摘要

        Args:
            article: 文章字典
            categories: 分类配置列表
            default_category: 默认分类 key
            max_length: 摘要最大长度

        Returns:
            (summary, category_key) tuple
        """
        results = self.classify_and_summarize_batch(
            [article],
            categories,
            default_category,
            max_length
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
