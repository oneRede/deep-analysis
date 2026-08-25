#!/usr/bin/env python3
"""测试DeepSeek API调用"""

import os
import requests
import json

# 加载环境变量
api_key = os.getenv('DEEPSEEK_API_KEY', '')

print(f"API Key存在: {bool(api_key)}")
print(f"API Key长度: {len(api_key)}")
print(f"API Key前缀: {api_key[:10]}...")
print(f"API Key后缀: ...{api_key[-10:]}")
print()

# 测试完整的请求
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

print(f"Authorization header: {headers['Authorization'][:30]}...")
print()

payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "你是一个测试助手"},
        {"role": "user", "content": "回复一个字：好"}
    ],
    "stream": False,
    "max_tokens": 10,
    "temperature": 0.3
}

try:
    response = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers=headers,
        json=payload,
        timeout=30
    )

    print(f"状态码: {response.status_code}")
    print(f"响应: {response.text[:500]}")

    if response.status_code == 200:
        result = response.json()
        print(f"\n✅ 成功! 返回内容: {result['choices'][0]['message']['content']}")
    else:
        print(f"\n❌ 失败! 状态码: {response.status_code}")

except Exception as e:
    print(f"❌ 异常: {e}")
