# RSS 聚合报告 - 具身智能

**生成时间**: 2026-09-05 10:09:40
**文章数量**: 4 篇

---

### 1. 机器人不能停下来等模型：星尘发布 SmoothRL，让在线强化学习跟上大模型的异步推理
- **来源**: 量子位 (TIER3)
- **发布日期**: Fri, 04 Sep 2026 09:19:29 +0000 (昨天)
- **类型**: news
- **优先级**: low
- **分类**: 具身智能
- **链接**: https://www.qbitai.com/2026/09/484437.html
- **AI 摘要**: 星尘智能发布SmoothRL框架，解决真实机器人异步推理场景下在线强化学习的问题。传统在线RL假设模型生成动作与机器人执行动作一致，但异步执行中action chunk被划分为已提交、执行和丢弃三个区域，若全部用于训练会导致错误归因。SmoothRL只让梯度通过实际执行的执行区域，并让训练和部署遵循相同异步节奏。在真实机器人上验证了动态投掷、给笔戴帽、快递开箱三项任务，成功率分别从39%提升至94%、8%提升至83%、30%提升至90%，证明了在线学习能适配高动态操作。
- **原始摘要**: 星尘智能（Astribot） 基座模型团队发布能异步执行的在线强化学习框架 SmoothRL

### 2. XDOF, just three months out of stealth, is in talks for a Series B at a $1.2B valuation
- **来源**: TechCrunch (TIER3)
- **发布日期**: Fri, 04 Sep 2026 23:36:14 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/
- **AI 摘要**: XDOF是一家由UC Berkeley研究人员创立的机器人数据初创公司，专注于为通用机器人训练收集真实世界遥操作数据。公司刚从隐身模式走出三个月，年化收入接近5000万美元，正与8VC领投方洽谈B轮融资，估值约12亿美元。XDOF旨在构建数据管道、收集工具和标注系统，充当机器人行业的外包数据供应链，其低成本遥操作系统GELLO为机器人研究提供了大规模训练数据。
- **原始摘要**: The round is being raised just months after the robot data startup exited from stealth.

### 3. Tesla’s Cybercab Is Being Investigated by Federal Regulators
- **来源**: The New York Times Technology (TIER3)
- **发布日期**: Fri, 04 Sep 2026 18:07:14 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://www.nytimes.com/2026/09/04/business/tesla-cybercab-nhtsa-investigation.html
- **AI 摘要**: 文章报道了美国国家公路交通安全管理局（NHTSA）正在对特斯拉的Cybercab自动驾驶出租车展开调查。该车型没有方向盘，NHTSA将审查其是否符合联邦汽车安全法规。此次调查聚焦于无方向盘设计在紧急情况下的操控能力、安全标准合规性以及乘客安全保护措施。调查结果可能影响特斯拉自动驾驶出租车商业化进程，并引发对新型自动驾驶车辆监管框架的讨论。
- **原始摘要**: The National Highway Traffic Safety Administration said it would examine whether the company’s new self-driving taxi, which has no steering wheel, meets federal auto regulations.

### 4. AGIBOT Showcases Embodied AI Robots in A...2026-09-04
- **来源**: Agibot (智元机器人) (TIER1)
- **发布日期**: 2026-09-05
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://agibot.com/article/231/detail/96.html
- **AI 摘要**: 文章报道AGIBOT在2026年展示具身智能机器人，强调其在物理世界交互中的先进能力与应用前景。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
