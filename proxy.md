export ANTHROPIC_BASE_URL="https://www.autodl.art/api/v1/anthropic"
export ANTHROPIC_AUTH_TOKEN="YmPyQUbvXR3t7FNb486tiRrQF2uBxw9hDjLKE2z3Ewr1VO3s"

export ANTHROPIC_BASE_URL="https://cc-vibe.com"
export ANTHROPIC_AUTH_TOKEN="sk-626c99e0e161eb8145cd8fc82a21d7fa08689ae399ea87b4cb0a5406fbd2f794"

curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-47f4bcaec20a436399ac7674e7f15c0b" \
  -d '{
        "model": "deepseek-v4-pro",
        "messages": [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Hello!"}
        ],
        "thinking": {"type": "enabled"},
        "reasoning_effort": "high",
        "stream": false
      }'

  curl -X POST https://api.anysearch.com/v1/search \
  -H "Authorization: Bearer as_sk_3c38026829b6b3bf9d1702d008f5fc1a" \
  -H "Content-Type: application/json" \
  -d '{
        "query": "AI 应用案例 医疗",
        "max_results": 5
      }'