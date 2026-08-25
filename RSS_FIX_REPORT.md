# RSS聚合器问题修复报告

**日期**: 2026-08-25  
**问题**: 分类不起作用 + 许多文章没有中文总结

---

## 问题诊断

### 1. 分类问题
- **现象**: 348篇文章全部被分类为"未分类"
- **根本原因**: DeepSeek API认证失败（401错误）

### 2. AI摘要问题
- **现象**: 所有文章都没有生成中文总结
- **根本原因**: 同样是API认证失败

### 3. API认证失败原因
- **错误信息**: `Authentication Fails (auth header format should be Bearer sk-...)`
- **真实原因**: 环境变量加载方式不可靠
  - 原方法: `export $(grep -v '^#' "$ROOT_DIR/.env" | xargs)`
  - 问题: 这种方式在某些情况下可能无法正确导出环境变量

---

## 修复方案

### 1. 修复环境变量加载（scripts/run-rss.sh）

**修改前**:
```bash
if [ -f "$ROOT_DIR/.env" ]; then
    export $(grep -v '^#' "$ROOT_DIR/.env" | xargs)
    echo "✅ 已加载环境变量"
fi
```

**修改后**:
```bash
if [ -f "$ROOT_DIR/.env" ]; then
    # 使用 set -a 来自动导出所有变量
    set -a
    source "$ROOT_DIR/.env"
    set +a
    echo "✅ 已加载环境变量"

    # 验证关键环境变量
    if [ -z "$DEEPSEEK_API_KEY" ]; then
        echo "⚠️  警告: DEEPSEEK_API_KEY 未设置"
    else
        echo "✅ DEEPSEEK_API_KEY 已设置 (长度: ${#DEEPSEEK_API_KEY})"
    fi
fi
```

**改进点**:
- 使用 `set -a` + `source` 组合，更可靠
- 添加环境变量验证，立即发现问题
- 显示API密钥长度，便于调试

### 2. 增强Python脚本（scripts/rss-aggregator.py）

#### 2.1 添加API密钥验证和测试

在 `__init__` 方法中添加：
```python
# DeepSeek API 配置
self.deepseek_api_key = os.getenv('DEEPSEEK_API_KEY', '').strip()  # 添加 .strip()
self.deepseek_api_url = "https://api.deepseek.com/chat/completions"
self.enable_ai_summary = self.config.get('ai_summary', {}).get('enabled', True)
self.batch_size = self.config.get('ai_summary', {}).get('batch_size', 10)
self.batch_delay = self.config.get('ai_summary', {}).get('batch_delay', 1.0)

# 调试信息：检查API密钥
if self.enable_ai_summary:
    if not self.deepseek_api_key:
        print("⚠️  警告: DEEPSEEK_API_KEY 未设置，AI摘要功能将被禁用")
        self.enable_ai_summary = False
    else:
        print(f"✅ DeepSeek API 已配置 (密钥长度: {len(self.deepseek_api_key)})")
        # 测试API连接
        self._test_api_connection()
```

#### 2.2 添加API连接测试方法

```python
def _test_api_connection(self):
    """测试API连接是否正常"""
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.deepseek_api_key}"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": "test"}],
            "max_tokens": 5,
            "temperature": 0.3
        }

        response = requests.post(
            self.deepseek_api_url,
            headers=headers,
            json=payload,
            timeout=10
        )

        if response.status_code == 200:
            print("✅ DeepSeek API 连接测试成功")
        else:
            print(f"⚠️  DeepSeek API 连接测试失败 ({response.status_code}): {response.text[:200]}")
            self.enable_ai_summary = False
    except Exception as e:
        print(f"⚠️  DeepSeek API 连接测试异常: {str(e)}")
        self.enable_ai_summary = False
```

**改进点**:
- 初始化时立即测试API连接
- 如果连接失败，自动禁用AI摘要功能
- 提供清晰的错误信息

---

## 验证结果

### 测试1: API密钥验证
```
✅ API密钥存在且有效
✅ 长度: 35字符
✅ 格式: sk-... 正确
```

### 测试2: API连接测试
```
✅ DeepSeek API 连接测试成功
✅ 返回状态码: 200
```

### 测试3: 单篇文章摘要和分类
```
✅ AI摘要生成成功
✅ 分类功能正常
✅ 分类结果: AI模型 (ai_model)
```

### 测试4: 批量处理（3篇文章）
```
✅ AI摘要成功率: 3/3 (100%)
✅ 分类成功率: 3/3 (100%)

文章1: GPT-5模型 → 分类为"AI模型"
文章2: 机器人控制系统 → 分类为"具身智能"
文章3: AI芯片 → 分类为"AI芯片"
```

---

## 修复后的工作流程

1. **环境变量加载**
   ```
   run-rss.sh → 使用 set -a + source 加载 .env
   ↓
   验证 DEEPSEEK_API_KEY 是否存在
   ↓
   显示密钥长度确认
   ```

2. **脚本初始化**
   ```
   rss-aggregator.py 初始化
   ↓
   读取 DEEPSEEK_API_KEY（带 strip()）
   ↓
   测试API连接
   ↓
   连接成功 → 启用AI功能
   连接失败 → 禁用AI功能并告警
   ```

3. **文章处理**
   ```
   抓取文章
   ↓
   批量调用API生成摘要和分类
   ↓
   应用到文章
   ↓
   生成分类报告
   ```

---

## 下一步建议

### 1. 立即执行
重新运行完整的RSS聚合：
```bash
bash scripts/run-rss.sh
```

预期结果：
- 所有文章都应该有AI摘要
- 所有文章都应该被正确分类
- 报告目录中应该生成多个分类文件

### 2. 检查输出
```bash
# 查看今天的报告
ls -la report/$(date +%Y-%m-%d)/

# 应该看到类似：
# rss-aggregation-2026-08-25.md          # 总报告
# rss-aggregation-2026-08-25-AI应用.md
# rss-aggregation-2026-08-25-AI模型.md
# rss-aggregation-2026-08-25-具身智能.md
# ... 等等
```

### 3. 验证质量
随机抽查几篇文章，确认：
- AI摘要准确且简洁（100-200字）
- 分类合理且符合定义
- 没有"未分类"文章（除非真的无法分类）

---

## 技术细节

### 为什么 `set -a` + `source` 更好？

**原方法的问题**:
```bash
export $(grep -v '^#' .env | xargs)
```
- 如果值中有空格或特殊字符会出错
- 不能正确处理多行值
- 不能处理引号

**新方法的优势**:
```bash
set -a          # 自动导出所有变量
source .env     # 执行文件，就像在当前shell中运行
set +a          # 关闭自动导出
```
- 正确处理所有shell变量赋值语法
- 支持引号、空格、特殊字符
- 更符合shell脚本最佳实践

### API密钥为什么要 .strip()？

环境变量可能包含：
- 末尾的换行符 `\n`
- 首尾的空格
- 不可见的控制字符

这些都会导致API认证失败，但很难发现。`.strip()` 清除所有这些问题。

---

## 总结

✅ **根本原因**: 环境变量加载不可靠  
✅ **修复方案**: 改用 `set -a` + `source` + 添加验证  
✅ **测试结果**: 所有测试通过，功能正常  
✅ **预期效果**: 所有文章都会有AI摘要和正确分类

修复已完成，可以放心使用了！
