#!/usr/bin/env python3
"""测试RSS聚合器初始化"""

import os
import sys
from pathlib import Path

# 设置环境变量
os.environ['DEEPSEEK_API_KEY'] = 'sk-47f4bcaec20a436399ac7674e7f15c0b'

print("=" * 60)
print("测试RSS聚合器初始化和API连接")
print("=" * 60)
print()

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent))

# 导入模块
print("导入模块...")
import yaml
import feedparser
import json
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Any, Set
from urllib.parse import urlparse
import re
import requests
import time
from bs4 import BeautifulSoup

print("✅ 基础模块导入成功")
print()

# 测试配置文件
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
CONFIG_FILE = ROOT_DIR / "config" / "feeds.yml"
CATEGORIES_FILE = ROOT_DIR / "config" / "categories.yml"

print(f"配置文件: {CONFIG_FILE}")
print(f"分类文件: {CATEGORIES_FILE}")
print()

# 加载配置
print("加载配置...")
with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

with open(CATEGORIES_FILE, 'r', encoding='utf-8') as f:
    categories_config = yaml.safe_load(f)

print(f"✅ 配置加载成功")
print(f"   分类数量: {len(categories_config['categories'])}")
print(f"   默认分类: {categories_config.get('default_category', 'ai_application')}")
print()

# 测试API
api_key = os.getenv('DEEPSEEK_API_KEY', '').strip()
print(f"API密钥: {api_key[:10]}...{api_key[-10:]} (长度: {len(api_key)})")
print()

print("测试API连接...")
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "test"}],
    "max_tokens": 5,
    "temperature": 0.3
}

try:
    response = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers=headers,
        json=payload,
        timeout=10
    )

    if response.status_code == 200:
        print("✅ DeepSeek API 连接测试成功")
    else:
        print(f"❌ DeepSeek API 连接测试失败 ({response.status_code})")
        print(f"   响应: {response.text[:200]}")
except Exception as e:
    print(f"❌ DeepSeek API 连接测试异常: {str(e)}")

print()
print("=" * 60)
print("测试完成")
print("=" * 60)
