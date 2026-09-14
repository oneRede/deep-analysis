# 本地模型分类器使用指南

## 概述

RSS 聚合器现在支持使用本地开源模型进行文章分类和摘要生成，替代了原有的 DeepSeek API 调用。这种方式：

- ✅ **完全免费**：无需 API 密钥，无使用费用
- ✅ **隐私保护**：数据不离开本地机器
- ✅ **无网络依赖**：可离线运行
- ✅ **速度快**：3B 参数模型在本地运行速度很快
- ✅ **高质量**：Qwen2.5-3B 等模型在中文理解和分类任务上表现优秀

## 快速开始

### 1. 安装 Ollama

Ollama 是一个轻量级的本地 LLM 运行工具。

**macOS / Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
访问 https://ollama.com/download 下载安装包

**验证安装:**
```bash
ollama --version
```

### 2. 下载推荐模型

我们推荐使用 **Qwen2.5-3B-Instruct**，它在中文理解和分类任务上表现最好：

```bash
# 推荐：Qwen2.5-3B (中文最佳，3GB 显存)
ollama pull qwen2.5:3b

# 备选：Llama 3.2-3B (英文强，中文可用，3GB 显存)
ollama pull llama3.2:3b

# 备选：Gemma2-2B (最轻量，速度最快，2GB 显存)
ollama pull gemma2:2b
```

### 3. 测试分类器

```bash
cd scripts
python3 local_classifier.py
```

如果看到以下输出，说明配置成功：
```
✅ Ollama 连接成功，模型 qwen2.5:3b 可用
✅ 分类结果:
   摘要: OpenAI发布了最新的GPT-5大语言模型...
   分类: ai_model
```

### 4. 配置 RSS 聚合器

编辑 `config/feeds.yml`，确保使用本地分类器：

```yaml
ai_summary:
  enabled: true
  classifier: "local"  # 使用本地模型
  batch_size: 5  # 本地模型建议 3-5 篇
  batch_delay: 0.5  # 批次延迟
  
  # 本地模型配置
  local_model: "qwen2.5:3b"  # 模型名称
  ollama_url: "http://localhost:11434"  # Ollama 地址
```

### 5. 运行 RSS 聚合器

```bash
cd scripts
./run-rss.sh
```

## 模型对比

| 模型 | 参数量 | 显存需求 | 速度 | 中文能力 | 推荐度 |
|------|--------|----------|------|----------|--------|
| **qwen2.5:3b** | 3B | ~3GB | 快 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| qwen2.5:1.5b | 1.5B | ~2GB | 很快 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| llama3.2:3b | 3B | ~3GB | 快 | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| llama3.2:1b | 1B | ~1.5GB | 很快 | ⭐⭐ | ⭐⭐⭐ |
| gemma2:2b | 2B | ~2GB | 很快 | ⭐⭐⭐ | ⭐⭐⭐ |

**推荐配置:**
- **标准配置**: qwen2.5:3b - 最佳的中文分类效果
- **低资源配置**: qwen2.5:1.5b 或 gemma2:2b - 更少的显存占用
- **高吞吐配置**: gemma2:2b - 最快的处理速度

## 性能优化

### 调整批处理大小

根据机器性能调整 `batch_size`:

```yaml
ai_summary:
  batch_size: 3   # 低配机器 (4GB RAM)
  batch_size: 5   # 标准配置 (8GB RAM)
  batch_size: 10  # 高配机器 (16GB+ RAM)
```

### GPU 加速

Ollama 会自动使用 GPU（如果可用）。检查 GPU 使用情况：

```bash
# NVIDIA GPU
nvidia-smi

# Apple Silicon
# Ollama 会自动使用 Metal
```

### 并发处理

本地模型目前使用逐篇处理，确保稳定性。如果需要更快的速度，可以：

1. 使用更小的模型（gemma2:2b）
2. 增加 CPU/GPU 资源
3. 减少 `batch_delay` 到 0.1 秒

## 切换回 DeepSeek API

如果需要切换回 DeepSeek API：

```yaml
ai_summary:
  enabled: true
  classifier: "deepseek"  # 使用 DeepSeek API
  batch_size: 10
  batch_delay: 1.0
```

并确保设置了环境变量：
```bash
export DEEPSEEK_API_KEY="your-api-key"
```

## 故障排除

### 问题 1: Ollama 连接失败

```
⚠️  Ollama 连接失败: Connection refused
```

**解决方案:**
```bash
# 启动 Ollama 服务
ollama serve

# 或在后台运行（macOS/Linux）
nohup ollama serve > /dev/null 2>&1 &
```

### 问题 2: 模型未安装

```
⚠️  模型 qwen2.5:3b 未安装
```

**解决方案:**
```bash
ollama pull qwen2.5:3b
```

### 问题 3: 显存不足

```
Error: out of memory
```

**解决方案:**
1. 使用更小的模型：
   ```bash
   ollama pull qwen2.5:1.5b
   ```

2. 更新配置：
   ```yaml
   local_model: "qwen2.5:1.5b"
   ```

### 问题 4: 分类结果不准确

**解决方案:**
1. 使用更大的模型（qwen2.5:3b 而不是 1.5b）
2. 检查 `config/categories.yml` 中的分类描述是否清晰
3. 增加 `temperature` 参数（在 `local_classifier.py` 中）

## 高级配置

### 自定义 Ollama 地址

如果 Ollama 运行在其他机器或端口：

```yaml
ai_summary:
  ollama_url: "http://192.168.1.100:11434"  # 远程服务器
```

### 使用自定义模型

Ollama 支持加载任何 GGUF 格式的模型：

```bash
# 创建 Modelfile
cat > Modelfile << EOF
FROM ./my-model.gguf
PARAMETER temperature 0.3
PARAMETER top_p 0.9
EOF

# 创建模型
ollama create my-custom-model -f Modelfile

# 使用自定义模型
# 在 feeds.yml 中设置：
# local_model: "my-custom-model"
```

### 调整生成参数

编辑 `scripts/local_classifier.py` 中的参数：

```python
classifier = LocalClassifier(
    model="qwen2.5:3b",
    temperature=0.3,  # 降低随机性 (0-1)
    timeout=60        # 请求超时时间
)
```

## 成本对比

### DeepSeek API 成本估算

假设每天处理 100 篇文章：
- 每篇文章约 500 tokens 输入 + 200 tokens 输出
- DeepSeek 价格：约 $0.14 / 1M tokens (输入) + $0.28 / 1M tokens (输出)
- **每天成本**: ~$0.013
- **每月成本**: ~$0.40
- **每年成本**: ~$4.80

### 本地模型成本

- **设备成本**: 已有电脑/服务器（$0）
- **电力成本**: 约 10W 功耗，24小时运行约 $0.02/天
- **每月成本**: ~$0.60（纯电费）
- **每年成本**: ~$7.20（纯电费）

**结论**: 对于中小规模使用，本地模型和 API 成本相近。但本地模型提供了更好的隐私保护和无网络依赖。

## 技术细节

### 分类流程

1. **文章预处理**: 提取标题、摘要或全文（根据 tier）
2. **批量处理**: 将文章分批送入模型
3. **Prompt 构建**: 动态生成包含所有分类的 prompt
4. **结果解析**: 从 JSON 响应中提取摘要和分类
5. **错误处理**: 失败的文章返回 (None, None)

### API 接口

本地分类器实现了与 DeepSeek API 相同的接口：

```python
from local_classifier import LocalClassifier

classifier = LocalClassifier(model="qwen2.5:3b")

# 单篇分类
summary, category = classifier.classify_and_summarize_single(
    article={"title": "...", "summary": "..."},
    categories=[...],
    default_category="ai_application",
    max_length=200
)

# 批量分类
results = classifier.classify_and_summarize_batch(
    articles=[...],
    categories=[...],
    default_category="ai_application",
    max_length=200
)
```

## 参考资源

- [Ollama 官网](https://ollama.com)
- [Qwen2.5 模型介绍](https://github.com/QwenLM/Qwen2.5)
- [Llama 3.2 模型介绍](https://ai.meta.com/blog/llama-3-2/)
- [Gemma 2 模型介绍](https://ai.google.dev/gemma)

## 反馈与支持

如果遇到问题或有改进建议，请：

1. 检查本文档的故障排除部分
2. 查看 Ollama 日志：`ollama logs`
3. 测试分类器：`python3 scripts/local_classifier.py`
4. 提交 issue 或 PR

---

**最后更新**: 2026-09-14
