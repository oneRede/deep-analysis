# 🚀 本地模型安装 - macOS 快速指南

## 当前状态
✅ 代码已完成  
✅ 配置已更新（使用本地模型）  
❌ Ollama 未安装  

## 安装步骤（5分钟）

### 方式 1: 自动安装（推荐）

```bash
./install-local-model.sh
```

这个脚本会：
1. 引导您安装 Ollama
2. 下载推荐模型 (qwen2.5:3b)
3. 自动验证配置
4. 运行测试

### 方式 2: 手动安装

#### 1. 安装 Ollama

```bash
# 使用安装脚本
curl -fsSL https://ollama.com/install.sh | sh

# 或访问下载页面
open https://ollama.com/download
```

#### 2. 启动 Ollama 服务

```bash
# 前台运行（用于调试）
ollama serve

# 或后台运行
nohup ollama serve > /dev/null 2>&1 &
```

#### 3. 下载推荐模型

```bash
# 推荐：Qwen2.5-3B (中文最佳，1.9GB)
ollama pull qwen2.5:3b

# 备选：更小的模型
ollama pull qwen2.5:1.5b  # 更快，1GB
ollama pull gemma2:2b     # 最快，1.4GB
```

#### 4. 验证安装

```bash
# 检查 Ollama 状态
./scripts/verify-ollama.sh

# 或手动检查
ollama list
curl http://localhost:11434/api/tags
```

#### 5. 测试分类器

```bash
cd scripts
python3 test-local-classifier.py
```

#### 6. 运行 RSS 聚合器

```bash
./run-rss.sh
```

## 模型选择

| 模型 | 大小 | 速度 | 中文能力 | 推荐场景 |
|------|------|------|----------|----------|
| **qwen2.5:3b** ⭐ | 1.9GB | 快 | 优秀 | 推荐首选 |
| qwen2.5:1.5b | 1GB | 很快 | 良好 | 低配机器 |
| llama3.2:3b | 1.9GB | 快 | 可用 | 英文优先 |
| gemma2:2b | 1.4GB | 很快 | 可用 | 追求速度 |

## 验证清单

- [ ] Ollama 已安装: `which ollama`
- [ ] Ollama 服务运行: `curl http://localhost:11434/api/tags`
- [ ] 模型已下载: `ollama list`
- [ ] 分类器测试通过: `python3 scripts/test-local-classifier.py`
- [ ] RSS 聚合器运行成功: `./scripts/run-rss.sh`

## 常见问题

### Q: 下载速度慢？
A: Ollama 从官方服务器下载，可能较慢。可以尝试：
- 使用代理
- 等待完整下载（通常 2-5 分钟）

### Q: 提示端口 11434 被占用？
A: 说明 Ollama 已经在运行，无需重新启动

### Q: 模型运行慢？
A: 
- 使用更小的模型（qwen2.5:1.5b 或 gemma2:2b）
- 减少 batch_size（在 config/feeds.yml 中设置为 3）

### Q: 显存/内存不足？
A: 
- 使用 qwen2.5:1.5b (需要 2GB RAM)
- 使用 gemma2:2b (需要 2GB RAM)

## 下一步

安装完成后：

1. **测试运行**
   ```bash
   cd scripts
   ./run-rss.sh
   ```

2. **查看文档**
   - 快速参考: `scripts/QUICK_REFERENCE.md`
   - 完整指南: `scripts/LOCAL_CLASSIFIER_GUIDE.md`

3. **调整配置**
   根据需要在 `config/feeds.yml` 中调整：
   - `batch_size`: 批处理大小
   - `local_model`: 模型名称

## 技术支持

遇到问题？运行诊断：

```bash
# 完整诊断
python3 scripts/test-local-classifier.py

# 检查 Ollama 状态
./scripts/verify-ollama.sh

# 查看 Ollama 日志
ollama logs
```

## 切换回 API 模式（可选）

如果需要临时使用 DeepSeek API：

```yaml
# config/feeds.yml
ai_summary:
  classifier: "deepseek"  # 改为 deepseek
```

并确保设置了 API key：
```bash
export DEEPSEEK_API_KEY="your-key"
```

---

**创建时间**: 2026-09-14  
**适用系统**: macOS  
**预计时间**: 5-10 分钟
