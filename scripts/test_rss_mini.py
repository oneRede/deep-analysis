#!/usr/bin/env python3
"""最小化RSS聚合测试 - 只测试1个feed"""

import os
import sys
from pathlib import Path

# 设置环境变量
os.environ['DEEPSEEK_API_KEY'] = 'sk-47f4bcaec20a436399ac7674e7f15c0b'

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent))

print("=" * 60)
print("最小化RSS聚合测试")
print("=" * 60)
print()

# 导入RSSAggregator类
import yaml
import feedparser
import json
from datetime import datetime, timedelta
from typing import List, Dict
import requests

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
CONFIG_FILE = ROOT_DIR / "config" / "feeds.yml"
CATEGORIES_FILE = ROOT_DIR / "config" / "categories.yml"

class MiniRSSTest:
    def __init__(self):
        # 加载配置
        with open(CATEGORIES_FILE, 'r', encoding='utf-8') as f:
            categories_config = yaml.safe_load(f)
            self.categories = categories_config['categories']
            self.default_category = categories_config.get('default_category', 'ai_application')

        self.category_name_to_key = {cat['name']: cat['key'] for cat in self.categories}
        self.category_key_to_name = {cat['key']: cat['name'] for cat in self.categories}

        self.deepseek_api_key = os.getenv('DEEPSEEK_API_KEY', '').strip()
        self.deepseek_api_url = "https://api.deepseek.com/chat/completions"

        print(f"✅ 初始化完成")
        print(f"   分类数量: {len(self.categories)}")
        print(f"   API密钥长度: {len(self.deepseek_api_key)}")
        print()

    def test_api_call(self):
        """测试单篇文章的API调用"""
        print("测试API调用...")

        article = {
            'title': '大型语言模型的最新进展',
            'summary': '本文介绍了大型语言模型在自然语言处理领域的最新研究成果，包括模型架构、训练方法和应用场景。'
        }

        # 构建分类描述
        category_descriptions = []
        category_names = []
        for cat in self.categories:
            category_descriptions.append(f"   - {cat['name']}：{cat['description']}")
            category_names.append(cat['name'])

        category_list = '/'.join(category_names)

        prompt = f"""请分析以下文章，完成两个任务：
1. 生成一个简洁的中文总结（不超过100字）
2. 将文章分类到以下类别之一：
{chr(10).join(category_descriptions)}

文章：
标题：{article['title']}
摘要：{article['summary']}

请严格按照以下JSON格式返回：
{{
  "summary": "100字以内的中文总结",
  "category": "{category_list}（选一）"
}}

只返回JSON，不要有其他内容。"""

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
            "max_tokens": 200,
            "temperature": 0.3
        }

        try:
            response = requests.post(
                self.deepseek_api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            print(f"   状态码: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content'].strip()

                # 移除可能的markdown标记
                content = content.replace('```json', '').replace('```', '').strip()

                print(f"   原始响应: {content}")
                print()

                # 解析JSON
                parsed = json.loads(content)
                summary = parsed.get('summary', '')
                category = parsed.get('category', '')
                category_key = self.category_name_to_key.get(category, self.default_category)

                print(f"✅ API调用成功")
                print(f"   AI摘要: {summary}")
                print(f"   分类: {category} ({category_key})")

                return True
            else:
                print(f"❌ API调用失败: {response.text}")
                return False

        except Exception as e:
            print(f"❌ 异常: {str(e)}")
            return False

# 运行测试
test = MiniRSSTest()
success = test.test_api_call()

print()
print("=" * 60)
if success:
    print("✅ 测试通过")
else:
    print("❌ 测试失败")
print("=" * 60)
