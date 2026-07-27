# Deep Analysis - AI 技术进展追踪体系

> 一个基于智能体的 AI 技术进展自动化追踪与整理系统，包含三个互补的专题仓库。

## 📂 仓库结构

```
deep_analysis/
├── ai_model_research/          # AI 大模型技术进展
├── ai_physical_research/       # 具身智能与物理世界 AI
├── ai_application_research/    # AI 应用案例（原始版本，已停止更新）
└── harness-engineering/        # Harness Engineering 实践
```

## 🎯 三大专题仓库

### 1. AI 大模型技术进展 ([ai_model_research/](ai_model_research/))

追踪大模型本身的技术进展：

- **新模型发布**：GPT、Claude、Gemini、LLaMA 等
- **架构创新**：Transformer 变体、MoE、新注意力机制
- **训练技术**：预训练、长上下文、多模态融合
- **对齐与安全**：RLHF、Constitutional AI、Red Teaming
- **评测基准**：新评测方法、基准数据集
- **模型能力研究**：推理、规划、工具使用
- **推理优化**：量化、剪枝、KV-cache 优化
- **硬件基础设施**：训练集群、GPU/TPU 优化
- **数据工程**：合成数据、数据清洗

**信源覆盖**：OpenAI、Anthropic、Google DeepMind、Meta AI、DeepSeek、Kimi、智谱、Qwen 等主流大模型官方博客 + arXiv + 顶会论文

### 2. 具身智能与物理世界 AI ([ai_physical_research/](ai_physical_research/))

追踪 AI 在物理世界的感知、决策与行动：

- **机器人技术**：人形机器人、灵巧操作、工业/服务机器人
- **自动驾驶**：感知、规划、端到端驾驶、车路协同
- **具身智能基础**：世界模型、物理推理、空间理解
- **感知与导航**：视觉 SLAM、语义地图、路径规划
- **操作与交互**：物体抓取、HRI、任务规划
- **仿真与数据**：sim-to-real、物理仿真器、数字孪生
- **多模态融合**：VLA 模型、embodied vision-language
- **物理 AI 应用**：AI for Physics、材料科学、量子计算
- **硬件与平台**：传感器、边缘计算、实时系统

**信源覆盖**：Boston Dynamics、Tesla AI、Waymo、Figure AI、Unitree、小鹏/理想/蔚来、MIT CSAIL、Stanford、Berkeley、CMU 等

### 3. AI 应用案例 ([ai_application_research/](ai_application_research/))

原始的 AI 应用案例收录仓库（已停止更新，保留历史内容）。已有 14 篇翻译作品，涵盖医疗、金融、工业、企业等领域。

## 🛠️ 技术架构

所有专题仓库共享同一套技术架构：

### 6 阶段策展流水线

```
①抓取 → ②翻译 → ③评审[全自动] → 🚧人类闸门🚧 → ④收录 → ⑤校验 → ⑥清理
```

- **抓取**：使用 `baoyu-url-to-markdown` skill
- **翻译**：使用 `baoyu-translate` skill（高质量完整翻译）
- **评审**：并行 agent 自动评审，生成建议
- **人类闸门**：决策权始终在人类手中
- **收录**：分流到 `works/` 或 `references/articles.md` 观察项
- **校验**：C1-C12 一致性检查
- **清理**：删除过程稿，保留最终版

### C1-C12 一致性守卫

通过 `scripts/check-consistency.sh` 守护：

- **C1-C5**：编号连续性、计数同步、索引一致性
- **C6-C8**：翻译流水线完整性、历史提法限定、pipeline 血统
- **C10-C12**：图片保真、表格格式、元数据完整性

每个子仓库都启用 pre-commit hook + GitHub Actions CI 双重保障。

### 目录结构

```
<subrepo>/
├── README.md              # 面向人类的入口
├── AGENTS.md              # 面向智能体的导航
├── works/                 # 翻译作品（正式收录）
├── references/            # 文章索引与外部资源
├── thinking/              # 独立思考与质疑
├── feedback/              # 踩坑与迭代心得
├── prompts/               # 验证有效的提示词
├── scripts/               # 一致性检查脚本
└── .claude/skills/        # 子 skill（抓取、翻译、策展）
```

## 🤖 自动化能力

- **情报追踪**：`prompts/deep-research-tracker.md` 提供双阶段 prompt（ChatGPT Deep Research + Claude 深度分析）
- **批量收录**：`/curate-research` skill 自动走完整个流水线
- **质量保证**：C1-C12 机械化检查，杜绝数量类漂移
- **渐进式披露**：每个目录都有 `AGENTS.md` 导航

## 📊 当前状态

| 仓库 | 状态 | 收录数 | 最后更新 |
|------|------|--------|----------|
| ai_model_research | ✅ 活跃 | 0 篇 | 2026-07-27 |
| ai_physical_research | ✅ 活跃 | 0 篇 | 2026-07-27 |
| ai_application_research | 🔒 归档 | 14 篇 | 2026-07-24 |
| harness-engineering | ✅ 活跃 | - | - |

## 🚀 快速开始

### 1. 启用 Git Hooks

每个子仓库都需要单独启用：

```bash
cd ai_model_research && git config core.hooksPath .githooks
cd ai_physical_research && git config core.hooksPath .githooks
cd ai_application_research && git config core.hooksPath .githooks
```

### 2. 开始追踪

使用各仓库的 `prompts/deep-research-tracker.md` 进行每周追踪。

### 3. 收录内容

使用 Claude Code 调用 `/curate-research` skill，或手动执行流水线。

## 📝 变更历史

- **2026-07-27**：创建统一的 `deep_analysis` 仓库
- **2026-07-27**：将 `ai_model_research` 重新聚焦为大模型技术进展
- **2026-07-27**：将 `ai_physical_research` 重新聚焦为具身智能与物理世界 AI
- **2026-07-24**：`ai_application_research` 完成 14 篇应用案例翻译

## 🔗 相关链接

- [Claude Code](https://claude.ai/code)
- [Harness Engineering 理念](harness-engineering/)

## 📄 License

MIT License

---

Built with ❤️ using Claude Code and Harness Engineering principles.
