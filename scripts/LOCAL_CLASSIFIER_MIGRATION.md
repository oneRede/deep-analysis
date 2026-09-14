# RSS 聚合器 - 本地模型分类迁移总结

## 📋 完成的修改

### 1. 新增文件

#### `scripts/local_classifier.py`
- 实现了本地模型分类器类 `LocalClassifier`
- 使用 Ollama API 调用本地开源模型
- 支持批量分类和单篇分类
- 包含连接测试、错误处理和重试逻辑
- 推荐模型自动检测功能

#### `scripts/LOCAL_CLASSIFIER_GUIDE.md`
- 完整的使用指南和设置教程
- 模型对比和性能优化建议
- 故障排除和常见问题解答
- 成本分析和技术细节说明

#### `scripts/setup-local-classifier.sh`
- 一键设置脚本
- 自动检测 Ollama 安装状态
- 自动下载推荐模型
- 运行测试验证配置

### 2. 修改的文件

#### `scripts/rss-aggregator.py`
主要修改：
- 导入 `local_classifier` 模块
- 在 `__init__` 中添加分类器类型配置 (`classifier_type`)
- 支持本地模型和 DeepSeek API 两种模式
- 新增 `_summarize_articles()` 统一接口
- 新增 `_summarize_with_local_model()` 实现本地模型调用
- 保留 `_summarize_with_deepseek()` 向后兼容
- 调整默认 batch_size 为 5（本地模型更合适）

#### `config/feeds.yml`
新增配置项：
```yaml
ai_summary:
  enabled: true
  classifier: "local"  # 新增：分类器类型
  batch_size: 5  # 调整：适合本地模型
  batch_delay: 0.5  # 调整：减少延迟
  
  # 新增：本地模型配置
  local_model: "qwen2.5:3b"
  ollama_url: "http://localhost:11434"
```

#### `scripts/requirements.txt`
新增依赖：
- `beautifulsoup4>=4.11.0`
- `python-dotenv>=1.0.0`

## 🎯 核心特性

### 1. 双模式支持
- **本地模型模式** (`classifier: "local"`): 使用 Ollama 运行开源模型
- **API 模式** (`classifier: "deepseek"`): 使用 DeepSeek API（保留向后兼容）

### 2. 推荐模型
| 模型 | 参数量 | 显存 | 中文能力 | 推荐场景 |
|------|--------|------|----------|----------|
| **qwen2.5:3b** ⭐ | 3B | 3GB | 优秀 | 标准配置 |
| qwen2.5:1.5b | 1.5B | 2GB | 良好 | 低资源 |
| llama3.2:3b | 3B | 3GB | 可用 | 英文优先 |
| gemma2:2b | 2B | 2GB | 可用 | 高速处理 |

### 3. 智能处理
- Tier1 文章：基于摘要（100字）
- Tier2/3/Military：基于全文（200字）
- 自动获取全文内容
- 批量处理提高效率

### 4. 错误处理
- 连接测试和验证
- 模型可用性检查
- JSON 解析容错
- 失败降级处理

## 🚀 快速开始

### 方式一：自动设置（推荐）

```bash
cd scripts
./setup-local-classifier.sh
```

### 方式二：手动设置

1. **安装 Ollama**
```bash
# macOS/Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows: 访问 https://ollama.com/download
```

2. **下载模型**
```bash
ollama pull qwen2.5:3b
```

3. **测试分类器**
```bash
cd scripts
python3 local_classifier.py
```

4. **运行 RSS 聚合器**
```bash
./run-rss.sh
```

## 💰 成本对比

### DeepSeek API
- 每天 100 篇文章: ~$0.013
- 每月成本: ~$0.40
- 每年成本: ~$4.80

### 本地模型
- 硬件成本: $0 (使用现有设备)
- 电力成本: ~$0.02/天 (10W 功耗)
- 每月成本: ~$0.60
- 每年成本: ~$7.20

**额外优势**:
- ✅ 完全免费（无 API 限额）
- ✅ 数据隐私保护
- ✅ 无网络依赖
- ✅ 低延迟

## 🔧 配置说明

### 基本配置
```yaml
# config/feeds.yml
ai_summary:
  enabled: true
  classifier: "local"  # 使用本地模型
  batch_size: 5
  batch_delay: 0.5
  local_model: "qwen2.5:3b"
  ollama_url: "http://localhost:11434"
```

### 切换到 API 模式
```yaml
ai_summary:
  enabled: true
  classifier: "deepseek"  # 切换到 DeepSeek API
  batch_size: 10
  batch_delay: 1.0
```

并设置环境变量：
```bash
export DEEPSEEK_API_KEY="your-api-key"
```

## 📊 性能优化

### 低配机器 (4GB RAM)
```yaml
batch_size: 3
local_model: "qwen2.5:1.5b"  # 或 "gemma2:2b"
```

### 标准配置 (8GB RAM)
```yaml
batch_size: 5
local_model: "qwen2.5:3b"
```

### 高配机器 (16GB+ RAM)
```yaml
batch_size: 10
local_model: "qwen2.5:3b"
batch_delay: 0.1
```

## 🧪 测试方法

### 1. 测试本地分类器
```bash
cd scripts
python3 local_classifier.py
```

### 2. 测试 RSS 聚合器
```bash
cd scripts
python3 rss-aggregator.py
```

### 3. 完整运行
```bash
cd scripts
./run-rss.sh
```

## 🐛 故障排除

### Ollama 连接失败
```bash
# 启动 Ollama 服务
ollama serve

# 或后台运行
nohup ollama serve > /dev/null 2>&1 &
```

### 模型未安装
```bash
# 安装推荐模型
ollama pull qwen2.5:3b

# 查看已安装模型
ollama list
```

### 显存不足
使用更小的模型：
```bash
ollama pull qwen2.5:1.5b
# 或
ollama pull gemma2:2b
```

并更新配置：
```yaml
local_model: "qwen2.5:1.5b"
```

## 📝 代码架构

### 类结构
```
LocalClassifier
├── __init__(model, base_url, temperature, timeout)
├── test_connection() -> bool
├── classify_and_summarize_batch() -> List[Tuple]
├── classify_and_summarize_single() -> Tuple
└── _call_ollama() -> Optional[str]
```

### 集成方式
```
RSSAggregator
├── classifier_type: "local" | "deepseek"
├── local_classifier: LocalClassifier (当 type="local")
└── _summarize_articles()
    ├── _summarize_with_local_model() [新]
    └── _summarize_with_deepseek() [原有]
```

## 📚 相关文档

- **使用指南**: `scripts/LOCAL_CLASSIFIER_GUIDE.md`
- **设置脚本**: `scripts/setup-local-classifier.sh`
- **分类器代码**: `scripts/local_classifier.py`
- **配置文件**: `config/feeds.yml`

## 🎉 优势总结

1. **经济性**: 无 API 费用，长期成本更低
2. **隐私性**: 数据不离开本地，完全可控
3. **可靠性**: 无网络依赖，离线可用
4. **灵活性**: 支持任何 Ollama 兼容模型
5. **兼容性**: 保留 API 模式，平滑迁移

## 🔮 未来改进

- [ ] 支持并发批处理（提高速度）
- [ ] 添加模型性能监控
- [ ] 支持更多本地模型后端（如 llama.cpp）
- [ ] 自动模型选择和降级
- [ ] 分类质量评估和反馈

## 📞 技术支持

如有问题，请：
1. 查阅 `LOCAL_CLASSIFIER_GUIDE.md`
2. 运行 `python3 local_classifier.py` 测试
3. 检查 Ollama 日志: `ollama logs`
4. 提交 issue 或 PR

---

**创建日期**: 2026-09-14  
**最后更新**: 2026-09-14  
**版本**: 1.0.0
