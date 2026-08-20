# 自动化脚本

自动化追踪 AI 技术进展的工具集合。

## 📂 脚本列表

### 1. RSS 聚合器 (`rss-aggregator.py`)

自动抓取配置的 RSS/Atom feeds，生成候选文章清单。

**功能**：
- 抓取 Tier 1/2/3 信源的最新内容
- 基于关键词过滤
- 自动去重（URL + 标题相似度）
- 时间窗口过滤（默认7天）
- 生成结构化 Markdown 报告

**使用方法**：

```bash
# 安装依赖
pip3 install -r requirements.txt

# 运行脚本
python3 scripts/rss-aggregator.py
```

**输出**：
- 报告文件：`report/rss-aggregation-YYYY-MM-DD.md`
- 缓存文件：`scripts/.rss-cache.json`（自动维护）

**配置**：
- 配置文件：`config/feeds.yml`
- 可自定义信源、关键词、过滤规则

**定时运行**：

```bash
# 方法1: macOS launchd（推荐）
# 见下方 setup-cron.sh

# 方法2: 手动 cron
crontab -e
# 添加：0 9 * * 1 cd /Users/rede/git/deep_analysis && /usr/bin/python3 scripts/rss-aggregator.py

# 方法3: GitHub Actions
# 见 .github/workflows/weekly-research.yml
```

---

## 🚀 快速开始

### 首次运行

```bash
# 1. 安装依赖
cd ~/git/deep_analysis
pip3 install -r scripts/requirements.txt

# 2. 测试运行
python3 scripts/rss-aggregator.py

# 3. 查看报告
ls -lh report/rss-aggregation-*.md
```

### 定时自动化

```bash
# 使用提供的安装脚本
bash scripts/setup-cron.sh
```

---

## 📊 工作流程

```
RSS Feeds → 抓取 → 过滤 → 去重 → 生成报告 → 人工审查 → Claude 深度分析 → curate-research
```

**与现有流水线集成**：

1. **RSS 聚合器**（本脚本）→ 生成候选清单
2. **人工审查** → 快速浏览报告，标记感兴趣的
3. **Claude 深度分析** → 使用 `prompts/deep-research-tracker.md` Prompt B
4. **启动流水线** → `/curate-research` skill 处理最终候选

---

## 🔧 故障排查

### 问题1: `feedparser` 安装失败

```bash
pip3 install --upgrade pip
pip3 install feedparser
```

### 问题2: SSL 证书错误

某些 RSS feed 可能有 SSL 问题，脚本会自动跳过并报告。

### 问题3: 无新文章

检查：
- 时间窗口设置（`config/feeds.yml` 中的 `days_lookback`）
- 缓存文件（`.rss-cache.json`）是否过大，可删除重新开始
- RSS 源是否正常（手动访问 URL 测试）

---

## 📝 未来扩展

- [ ] arXiv 专用追踪器（`arxiv-tracker.py`）
- [ ] 语义相似度去重（使用 sentence-transformers）
- [ ] 自动评分系统（ML 模型预测文章价值）
- [ ] Slack/Email 通知集成
- [ ] Web Dashboard

---

## 📄 License

与主仓库相同，MIT License
