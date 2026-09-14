# 本地模型分类 - 快速参考

## 🎯 一句话总结

使用 **Ollama + Qwen2.5-3B** 替代 DeepSeek API，实现完全本地的文章分类和摘要生成。

## ⚡ 快速开始 (3分钟)

```bash
# 1. 安装 Ollama (仅首次)
curl -fsSL https://ollama.com/install.sh | sh

# 2. 一键设置
cd scripts
./setup-local-classifier.sh

# 3. 运行
./run-rss.sh
```

## 📋 命令速查

```bash
# 安装模型
ollama pull qwen2.5:3b

# 查看已安装模型
ollama list

# 启动 Ollama 服务
ollama serve

# 测试分类器
python3 scripts/local_classifier.py

# 完整诊断
python3 scripts/test-local-classifier.py

# 运行 RSS 聚合器
cd scripts && ./run-rss.sh
```

## 🔧 配置速查

### 使用本地模型 (推荐)
```yaml
# config/feeds.yml
ai_summary:
  classifier: "local"
  local_model: "qwen2.5:3b"
```

### 切换回 API
```yaml
# config/feeds.yml
ai_summary:
  classifier: "deepseek"
```

## 🤖 推荐模型

| 选择 | 命令 | 特点 |
|------|------|------|
| **标准** ⭐ | `ollama pull qwen2.5:3b` | 中文最佳 |
| 轻量 | `ollama pull qwen2.5:1.5b` | 省资源 |
| 快速 | `ollama pull gemma2:2b` | 最快速度 |

## 🐛 问题速查

| 问题 | 解决方案 |
|------|----------|
| Ollama 连接失败 | `ollama serve` |
| 模型未安装 | `ollama pull qwen2.5:3b` |
| 显存不足 | 使用 `qwen2.5:1.5b` |
| 分类不准确 | 检查 `config/categories.yml` |

## 📖 完整文档

- **使用指南**: `scripts/LOCAL_CLASSIFIER_GUIDE.md` (380+ 行)
- **实施总结**: `scripts/IMPLEMENTATION_SUMMARY.md`
- **迁移文档**: `scripts/LOCAL_CLASSIFIER_MIGRATION.md`

## 💡 优势

✅ 完全免费 | ✅ 数据隐私 | ✅ 离线可用 | ✅ 无限制

## 🆚 对比

|  | 本地模型 | API |
|--|---------|-----|
| **成本** | 电费 (~$0.02/天) | API费 (~$0.013/天) |
| **隐私** | ✅ 完全本地 | ❌ 数据上传 |
| **网络** | ✅ 离线可用 | ❌ 需要连接 |
| **限额** | ✅ 无限制 | ⚠️ API 限制 |
| **速度** | ⚡ 0.5-3秒/篇 | 🐌 1-5秒/篇 |

## 📞 获取帮助

```bash
# 运行诊断
python3 scripts/test-local-classifier.py

# 查看 Ollama 状态
curl http://localhost:11434/api/tags

# 查看日志
ollama logs
```

## 🔗 相关链接

- [Ollama 官网](https://ollama.com)
- [Qwen2.5 介绍](https://github.com/QwenLM/Qwen2.5)
- [支持的模型列表](https://ollama.com/library)

---

**最后更新**: 2026-09-14 | **版本**: 1.0.0
