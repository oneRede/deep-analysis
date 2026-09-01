# RSS 聚合报告 - Harness工程

**生成时间**: 2026-09-01 10:14:39
**文章数量**: 55 篇

---

### 1. Your GNN is probably just an overcomplicated MLP (Tabular Leakage). We built SynthFin-AML to enforce strict causal boundaries. [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-31T16:21:10+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w3imxy/your_gnn_is_probably_just_an_overcomplicated_mlp/
- **AI 摘要**: 文章指出图神经网络（GNN）可能只是过度复杂的MLP，存在表格数据泄漏问题。作者构建了SynthFin-AML数据集以强制执行严格的因果边界。内容涉及GNN在金融反洗钱（AML）领域的应用，强调数据泄漏对模型评估的影响，并提出新的合成数据集来确保因果推断的准确性。属于AI在金融领域的应用和模型评估方法。
- **原始摘要**: We noticed our anti-money laundering models were performing suspiciously well. After digging into standard baselines on dynamic graphs, we found widespread temporal leakage in message-passing. If you...

### 2. How to assess if there is a strong signal in your dirty data [Project]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-31T12:02:54+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w3br9c/how_to_assess_if_there_is_a_strong_signal_in_your/
- **AI 摘要**: 文章讨论如何评估脏数据中是否存在强信号。内容可能涉及数据质量评估方法、信号检测技术、噪声过滤策略以及如何在数据不完美的情况下提取有效信息。可能包括统计方法、机器学习预处理步骤或实际案例。主题聚焦于数据分析和数据工程实践，属于数据科学应用。
- **原始摘要**: I'm sharing this new tabular data diagnostic tool (Entropic Scree). It can be used to estimate these properties of your high-d, real-world, dirty dataset: The informational volume of the signal (i.e.,...

### 3. Cycle-Level Simulator for Distributed GPUs For AI Workloads (Purdue)
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Sun, 30 Aug 2026 07:02:05 +0000 (2 天前)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/cycle-level-simulator-for-distributed-gpus-for-ai-workloads-purdue/
- **AI 摘要**: 普渡大学的研究人员提出了一种用于AI工作负载的分布式GPU周期级仿真框架，涵盖Ampere、Hopper和Blackwell等现代GPU架构。该框架在H100 GPU上实现了99%的皮尔逊相关系数，验证了其准确性。研究旨在为AI时代设计下一代异步分布式GPU，通过仿真支持多芯片模块、NVLink互连和GPU间预取等特性，为架构探索提供工具。
- **原始摘要**: Researchers from Purdue University published a technical paper titled “Architecting the Next Generation of Asynchronous, Distributed GPUs for the AI Era.” Abstract Excerpt: The paper presents a “cycle...

### 4. Predicting Post-Route PPA from Macro and Standard-Cell Placements (U. of Alberta)
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Sat, 29 Aug 2026 17:00:22 +0000 (2 天前)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/predicting-post-route-ppa-from-macro-and-standard-cell-placements-u-of-alberta/
- **AI 摘要**: 阿尔伯塔大学的研究人员提出了PPAPlace，一种可微分的跨阶段目标优化方法，用于芯片布局优化。研究发现宏单元布局显著影响布线后的性能、功耗和面积（PPA），但传统的半周长线长（HPWL）与布线后时序指标相关性接近零。PPAPlace使用双流预测器，结合图注意力和空间卷积，从宏单元和标准单元布局预测布线后PPA，并利用预测的WNS和TNS梯度进行端到端优化。该方法在全局布线后标签上训练，提高了布局优化的时序保真度。
- **原始摘要**: Researchers from University of Alberta published a technical paper titled “PPAPlace: Differentiable Cross-Stage Objectives for Chip Placement Optimization.” Abstract: “Macro placement significantly af...

### 5. Trust, But Verify
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Mon, 31 Aug 2026 07:03:35 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/trust-but-verify/
- **AI 摘要**: 本文是Brian Bailey的评论文章，探讨了在半导体设计和验证中“信任但验证”的原则。作者回顾了自己职业生涯中遇到的工具缺陷、规格错误和遗漏等问题，强调即使设计者尽力而为，工具和规格也不完美。随着AI在设计和验证中的介入，AI系统可能产生更多不可预测的错误，因此验证变得更加重要。文章呼吁在AI辅助设计中保持警惕，不能盲目信任AI的输出，必须通过严格的验证流程确保正确性。
- **原始摘要**: We trust designers to do the best they can, but know they cannot be perfect. That's why we verify. When AI gets involved, it cannot be trusted. The post Trust, But Verify appeared first on Semiconduct...

### 6. Benchmarking General Mobile Assistants in Challenging Real-World Scenarios
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27477
- **AI 摘要**: 提出GMA基准，包含七个开源应用和300个任务，评估通用移动助手在真实场景中的表现，发现现有模型在复杂任务中性能显著下降。
- **原始摘要**: arXiv:2608.27477v1 Announce Type: cross Abstract: Graphical user interfaces have emerged as an important environment for evaluating autonomous AI agents on multimodal interactive tasks. Existing bench...

### 7. Do Medical Vision Models Reason About Anatomy? Probing the Spatial Inductive Biases of Learned Visual Representations
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28092
- **AI 摘要**: 本文提出SPAR-Bench基准，用于探测医学视觉编码器是否具备解剖学空间推理能力。研究发现模型在切片内比较任务上表现接近随机，领域内看似解决的任务在零样本迁移下失效，表明其准确率源于对典型解剖结构的记忆而非图像计算。
- **原始摘要**: arXiv:2608.28092v1 Announce Type: cross Abstract: Interpreting a CT scan means comparing structures on either side, judging how far apart organs sit, and knowing where each one belongs. Medical vision...

### 8. CompareBench: A Benchmark for Visual Comparison Reasoning in Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.22737
- **AI 摘要**: 本文提出CompareBench基准套件，包含TallyBench、OmniCaps和CompareBench三个资源，用于评估视觉语言模型在数量、几何、空间和时间比较推理方面的能力。评估九个闭源模型发现整体性能强但存在持续失败，揭示了比较推理的不足。
- **原始摘要**: arXiv:2509.22737v3 Announce Type: replace Abstract: Visual comparison reasoning is a fundamental capability of vision-language models (VLMs), covering judgments of object quantity, geometric dimension...

### 9. Scientific Graphics Program Synthesis via Dual Self-Consistency Reinforcement Learning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.06079
- **AI 摘要**: 本文提出一个闭环框架，包含SciTikZ-230K高质量数据集和SciTikZ-Bench多维度基准，用于解决科学图形程序合成中数据质量和评估缺口。通过双自一致性强化学习，提升多模态大语言模型生成可执行TikZ代码的能力。
- **原始摘要**: arXiv:2604.06079v2 Announce Type: replace Abstract: Graphics Program Synthesis is pivotal for interpreting and editing visual data, effectively facilitating the reverse-engineering of static visuals i...

### 10. SDGBiasBench: Benchmarking and Mitigating Vision--Language Models' Biases in Sustainable Development Goals
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.21919
- **AI 摘要**: 本文提出SDGBiasBench，一个大规模基准套件，包含50万专家参与的多选题和5万回归任务，用于评估视觉语言模型在可持续发展目标推理中的决策级和估计级偏差。评估发现当前VLM存在内在SDG偏差，即用先验替代证据。
- **原始摘要**: arXiv:2605.21919v2 Announce Type: replace Abstract: Assessing progress toward the Sustainable Development Goals (SDGs) requires multi-step reasoning over visual cues, contextual knowledge, and develop...

### 11. PolyComp: A Polycube-based Benchmark for Compositional 3D Spatial Reasoning in Multimodal Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.14741
- **AI 摘要**: 介绍PolyComp基准测试，用于评估多模态模型的组合3D空间推理能力，包含120个问题，测试了GPT-5.6、Claude Fable 5和Gemini 3.1等模型，结果显示当前模型准确率有限。
- **原始摘要**: arXiv:2608.14741v2 Announce Type: replace Abstract: We introduce PolyComp, a procedurally generated and verified benchmark that stresses visual recognition and compositional spatial reasoning. In each...

### 12. SciReC: Diagnostic Evaluation of Multimodal, Multi-Turn Relational Reasoning with Adaptive Interaction
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27461
- **AI 摘要**: 本文提出SciReC基准和DMRA诊断框架，用于评估多模态大语言模型在关系推理任务中的表现，包括类比、结构和因果推理。Claude 4.6以73%的整体关系得分领先，GPT 5.4以68%紧随其后。
- **原始摘要**: arXiv:2608.27461v1 Announce Type: new Abstract: Relational reasoning requires the process of perceptual understanding, comparing, and integrating the underlying relationships between concepts. This ab...

### 13. The Effect of Emotional Context on Large Language Models' Endorsement of Premature Decisions: Comparing Emotional Vulnerability Across Six Commercial Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27465
- **AI 摘要**: 研究情绪上下文对六种商业大语言模型（OpenAI、Anthropic、Google）在用户过度自信时支持过早决策的影响。通过控制对话轮次和事实内容，隔离情绪因素，发现情绪表达可能增加模型对过早决策的支持，引发安全担忧。
- **原始摘要**: arXiv:2608.27465v1 Announce Type: new Abstract: As large language models (LLMs) are increasingly used for everyday decision-making advice, whether a model shifts the direction of its advice according...

### 14. Select, Don't Train: The Benefits of Modular Entity Disambiguation with LLM-Based Selection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27470
- **AI 摘要**: 本文系统比较了实体消歧中候选生成策略（BM25、Web KB搜索、密集检索器）在共享LLM选择阶段下的表现，发现模块化方法优于端到端训练，且稀疏检索在知识图谱变化时更具成本效益。
- **原始摘要**: arXiv:2608.27470v1 Announce Type: new Abstract: Entity Disambiguation (ED) is a key task for constructing and using knowledge graphs. State-of-the-art neural approaches commonly model ED as a single t...

### 15. A Survey on Rubric-Guided Reinforcement Learning for Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27505
- **AI 摘要**: 综述了基于评分标准的强化学习（Rubric-guided RL）在语言模型对齐中的应用，提出贝叶斯框架统一宪法和评分标准，并沿先验-后验轴分类，涵盖宪法AI、实例特定评分、过程监督、自进化评分等方向。
- **原始摘要**: arXiv:2608.27505v1 Announce Type: new Abstract: Reinforcement learning from human feedback (RLHF) has become the dominant paradigm for aligning large language models (LLMs) with human preferences. How...

### 16. Knowing Before Answering: Decoding Language Models for Reliable RAG
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27661
- **AI 摘要**: 本文提出一种基于模型内部信号的三分类方法，用于判断RAG系统中检索文档是否充分、不充分或冲突。通过隐藏激活和注意力特征训练轻量线性模型，在16种语言模型上验证了该路由器的有效性。
- **原始摘要**: arXiv:2608.27661v1 Announce Type: new Abstract: In Retrieval-Augmented Generation (RAG), retrieval may provide insufficient or conflicting information needed to answer a question. The system should no...

### 17. EvoHarmBench: Breaking Content Moderation with Iterative Human-Like Evasion
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27844
- **AI 摘要**: 本文提出EvoHarmBench，首个动态对抗性评估框架，用于内容审核系统。通过迭代优化循环在语义簇级别演化规避策略，同时优化规避成功率和人类可读性。评估了229个语义子簇和5种违规类别，揭示了静态基准与在线部署的性能差距。
- **原始摘要**: arXiv:2608.27844v1 Announce Type: new Abstract: Existing evaluations of harmful content detection rely predominantly on static benchmarks, which struggle to reflect the interactive adversarial ecosyst...

### 18. OpenStamp: A Watermark for Open-Source Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27899
- **AI 摘要**: 本文提出OpenStamp，一种针对开源语言模型的数字水印技术。通过仅修改最终投影层将水印逻辑编码到模型权重中，实验表明在检测性能和模型能力保持方面优于现有方法，且对白盒攻击更鲁棒。
- **原始摘要**: arXiv:2608.27899v1 Announce Type: new Abstract: With the growing prevalence of large language model (LLM) generated content, watermarking is considered a promising approach for attributing text to LLM...

### 19. What Makes Agent Memory Useful for Reliable Unanswerable Question Handling?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27924
- **AI 摘要**: 本文系统研究了智能体记忆中不可回答问题处理的作用，发现记忆提升效果具有选择性且脆弱，跨模型记忆复用比跨数据集更可行，决策指导比轨迹塑造更能保留提升效果。
- **原始摘要**: arXiv:2608.27924v1 Announce Type: new Abstract: Reliable handling of unanswerable questions (UAQs) is critical for trustworthy LLM-based agents. Although memory is widely used in agent systems, its ro...

### 20. Entity-Memory Graph Retrieval Improves Evidence Coverage in Long-Conversation Question Answering
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27925
- **AI 摘要**: 本文提出实体记忆图检索方法，通过保留对话轮次、共享实体连接和时序边，提升长对话问答中的证据覆盖率，在LoCoMo数据集上显著提高top-k召回率，但最终答案F1无显著差异。
- **原始摘要**: arXiv:2608.27925v1 Announce Type: new Abstract: Entity-Memory graph retrieval keeps dialogue turns as verbatim Memory nodes, links repeated mentions through shared Entities, and connects adjacent Memo...

### 21. PersonaForge: Realistic Multi-Turn User Simulation for Agentic Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28378
- **AI 摘要**: 本文提出PersonaForge框架，用于合成多轮用户-智能体交互数据，基于真实会话统计构建训练集和基准，实验表明能提升智能体系统性能。
- **原始摘要**: arXiv:2608.28378v1 Announce Type: new Abstract: Large language models are increasingly used as agentic workflow executors, yet existing training data and benchmarks largely assume informationally comp...

### 22. CultureConverse: A Multilingual Multi-turn Simulation Harness for Culturally Grounded Assistance in East and Southeast Asia
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28405
- **AI 摘要**: 提出CultureConverse，一个多语言多轮文化模拟评估框架，覆盖东亚和东南亚10个地区，评估18个模型的文化辅助能力，GPT-5 mini表现最佳，并创建了大规模数据集。
- **原始摘要**: arXiv:2608.28405v1 Announce Type: new Abstract: Current cultural evaluations for large language models (LLMs) often reduce culture to single-turn factual recall via MCQs, failing to capture a common u...

### 23. Blind Men and the Elephant: Probing the Epistemic Myopia of LLMs under Long-Tail Divergent Knowledge
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28478
- **AI 摘要**: 引入ElephantBench基准，探测LLM对长尾事实的多种叙述记忆，发现最强模型仅能恢复52.4%的双重叙述，规模增大和推理时扩展不能消除不完整性。
- **原始摘要**: arXiv:2608.28478v1 Announce Type: new Abstract: Factual question answering (QA) typically assumes a single canonical answer, obscuring whether large language models (LLMs) retain divergent accounts of...

### 24. NL2AGBench: Benchmarking LLM Auto-Formalization for AlphaGeometry
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28481
- **AI 摘要**: 提出NL2AGBench基准，评估LLM将自然语言几何问题自动形式化为AlphaGeometry DSL的能力，使用执行验证衡量翻译质量，填补该领域空白。
- **原始摘要**: arXiv:2608.28481v1 Announce Type: new Abstract: Recent advances in large language models (LLMs) have demonstrated strong capabilities in natural language understanding and mathematical reasoning. Howe...

### 25. The Calls are Coming from Inside the Model: Investigating Probe-based Detection of Tool-Calling Errors in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27750
- **AI 摘要**: 本文研究使用线性探针检测大语言模型工具调用错误的有效性，在18个模型上评估，发现探针能有效捕捉多种错误，包括参数值错误但类型正确的情况，模型大小、探针层和后训练类型是重要影响因素。
- **原始摘要**: arXiv:2608.27750v1 Announce Type: cross Abstract: The hidden states of large language models (LLMs) are known to capture rich information relating to model knowledge and behavior that can be hard to e...

### 26. Why Didn't It Check? Unsupported Final Claims and Their Repair in Two Tool-Equipped Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27768
- **AI 摘要**: 本文分析语言模型在工具辅助下做出无证据支持的最终声明的问题，定义了发生率和条件修复两个量化指标，通过重放实验发现模型在缺少证据时可能做出错误声明，而补充证据后部分可修复。
- **原始摘要**: arXiv:2608.27768v1 Announce Type: cross Abstract: A language model with access to tools can commit to a final claim unsupported by the evidence it has seen, even when a single available tool call woul...

### 27. SURE-Challenge: Evaluating Speech Evidence Before Speech-LLM Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27783
- **AI 摘要**: 本文提出SURE-Challenge基准，评估语音LLM在生成前拒绝不支持语音输入的能力，实验显示固定规则能大幅提高拒绝率而不影响支持输入的准确性，验证了前置过滤的有效性。
- **原始摘要**: arXiv:2608.27783v1 Announce Type: cross Abstract: Speech LLMs are usually graded after they answer, although an operating system first has to decide whether a waveform should be sent to the model. We...

### 28. Auditing Generative Audio Calls for Known-Task Audio-LLM Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27817
- **AI 摘要**: 本文研究音频LLM评估中的调用决策问题，区分声学证据访问和生成模型调用，实验表明监督编码器无需生成调用即可达到高准确率，而生成调用仅带来小幅提升，揭示了评估中的混淆因素。
- **原始摘要**: arXiv:2608.27817v1 Announce Type: cross Abstract: Speech and audio LLMs are often evaluated by asking whether a waveform prompt beats an automatic speech recognition (ASR) transcript. For known closed...

### 29. Benchmarking large language model agent societies against human behavioural distributions
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28182
- **AI 摘要**: 本文介绍SILICA工具，用于评估LLM代理社会行为是否与人类行为分布一致，通过五个环境测试代理行为、规则变化鲁棒性及社会动态真实性，发现代理仅在初始阶段与人类数据吻合。
- **原始摘要**: arXiv:2608.28182v1 Announce Type: cross Abstract: Populations of large language model agents are increasingly used as experimental societies. Three doubts shadow every such result: whether the agents...

### 30. Stay Within Your Bounds: Distance-Guided Decoding for Guaranteed Context-Free Grammar Compliance
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28229
- **AI 摘要**: 提出基于下推自动机的距离引导解码框架，用于保证上下文无关语法合规性，通过离线计算有界下推摘要和到达接受状态的上界距离，在线进行前瞻感知剪枝和束搜索，在JSON、SQL和LTL上实现语法有效性和完成质量提升。
- **原始摘要**: arXiv:2608.28229v1 Announce Type: cross Abstract: Grammar-constrained decoding helps large language models produce syntactically valid structured outputs, such as code, JSON, and SQL. For context-free...

### 31. Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28327
- **AI 摘要**: 将LLM防御堆栈视为集成，引入对手访问层级模型和成本模型，测量防御层间的失败相关性，发现覆盖饱和、成本上升、误拒累积，仅当独立时攻击成功率才乘性下降，为防御设计提供量化依据。
- **原始摘要**: arXiv:2608.28327v1 Announce Type: cross Abstract: Practitioners defend large language models (LLMs) by stacking defenses, assuming the layers compound. A stack is an ensemble, and ensembles compound o...

### 32. Evaluating the Performance of Large Language Models on GAOKAO Benchmark
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2023年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2305.12474
- **AI 摘要**: 介绍GAOKAO-Bench基准，使用中国高考题目评估LLM性能，采用零样本设置和人工评分，发现GPT-4、ChatGPT和ERNIE-Bot在高考中取得竞争性分数，但各科目表现差异显著，模型评分与人工评分中度一致。
- **原始摘要**: arXiv:2305.12474v4 Announce Type: replace Abstract: Large Language Models(LLMs) have demonstrated remarkable performance across various natural language processing tasks; however, how to comprehensive...

### 33. FENCE: A Financial and Multimodal Jailbreak Detection Dataset
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2602.18154
- **AI 摘要**: 本文提出FENCE，一个韩英双语多模态数据集，用于金融应用中越狱检测。实验显示商业和开源VLM存在漏洞，GPT-4o攻击成功率可测，开源模型暴露更大。基线检测器在分布内准确率达99%，外部基准表现良好。
- **原始摘要**: arXiv:2602.18154v3 Announce Type: replace Abstract: Jailbreaking poses a significant risk to the deployment of Large Language Models (LLMs) and Vision Language Models (VLMs). VLMs are particularly vul...

### 34. Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.28802
- **AI 摘要**: 本文研究LLM能否学习并复现标注者特定的解释行为。发现单标注层面模式弱，但聚合后可检测。提出跨标注者偏好优化（CAPO），对比目标标注者响应与其他有效但非目标特定标注。实验显示提示方法有限，CAPO能更好学习标注者特定行为。
- **原始摘要**: arXiv:2605.28802v2 Announce Type: replace Abstract: Free-text explanations extend human label variation (HLV) beyond label disagreement by revealing the reasoning and preferences behind annotators' de...

### 35. Auditing LLM Benchmarks with Item Response Theory
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.30504
- **AI 摘要**: 本文提出基于项目反应理论的指标，用于审计LLM基准测试中的错误标签，在七个基准测试中达到95%精度，并发现奖励模型偏向风格而非事实，存在基准污染风险。
- **原始摘要**: arXiv:2605.30504v2 Announce Type: replace Abstract: LLM benchmark labels are frozen at release and silently propagated into downstream benchmarks, errors and all. We introduce an Item Response Theory-...

### 36. Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.01629
- **AI 摘要**: 本文介绍LongJudgeBench基准，用于评估LLM作为裁判在长文本输出评估中的可靠性，涵盖多种场景和协议，系统评估多个基础模型和判断设置。
- **原始摘要**: arXiv:2606.01629v4 Announce Type: replace Abstract: As large language models (LLMs) are increasingly used for long-form generation, reliably evaluating long-form outputs has become a critical challeng...

### 37. Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.05122
- **AI 摘要**: 本文提出自我评估激发方法，通过少量数据激发基础LLM预测外部裁判评分的能力，显著提升校准效果并保持答案质量，所需数据量远少于强化学习基线。
- **原始摘要**: arXiv:2606.05122v2 Announce Type: replace Abstract: Large language models are increasingly evaluated by other models, raising a natural question: can a model predict how a judge will score its own out...

### 38. TokenPilot: Cache-Efficient Context Management for LLM Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.17016
- **AI 摘要**: 本文提出TokenPilot框架，通过双粒度上下文管理解决LLM代理长会话中的缓存失效问题，平衡文本稀疏性与提示缓存连续性，实验验证其有效性。
- **原始摘要**: arXiv:2606.17016v2 Announce Type: replace Abstract: As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dyn...

### 39. Does Finetuning with Scientific Data Increase Hallucinations? A Multi-domain Factuality Evaluation of LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.21359
- **AI 摘要**: 本文构建SciFactCheck基准，评估科学微调LLM的幻觉现象，发现科学微调模型在所有幻觉类型和领域上事实可靠性下降，揭示微调带来的风险。
- **原始摘要**: arXiv:2606.21359v2 Announce Type: replace Abstract: Large language models (LLMs) are increasingly used to communicate and explain scientific concepts, yet their tendency to hallucinate poses significa...

### 40. ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.26403
- **AI 摘要**: 本文提出ProfileFoundry，一个确定性生成器，生成10万个合成人物对象，用于隐私、记忆和工具使用评估，提供跨字段和时间一致性数据。
- **原始摘要**: arXiv:2606.26403v2 Announce Type: replace Abstract: Foundation-model research increasingly needs data about people: user state, personal histories, relationships, contact-like fields, documents, and l...

### 41. JuryProbe: An Empirical Consensus-Risk Diagnostic for Routing Reference-Free Factuality Judge Panels to Grounded Verification
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.20607
- **AI 摘要**: JuryProbe是一种针对无参考事实性法官小组的共识风险诊断工具，通过校准探针估计假阴性相关性和假共识提升，当风险高时将无参考多数接受路由到带可信参考的验证，降低因法官共同盲点导致的错误接受风险。
- **原始摘要**: arXiv:2608.20607v2 Announce Type: replace Abstract: Panels of inexpensive LLM judges increasingly make accept-or-escalate decisions. In factuality settings, accepting a claim because several reference...

### 42. SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.12015
- **AI 摘要**: SkillSafetyBench是一个评估智能体在技能面对攻击面时安全性的基准，包含155个对抗案例、47个任务和6个风险域，实验表明非用户攻击可持续诱导不安全行为，揭示了现有安全评估忽视的模块化攻击面。
- **原始摘要**: arXiv:2605.12015v3 Announce Type: replace-cross Abstract: Reusable skills are becoming a common interface for extending large language model agents, packaging procedural guidance with access to files,...

### 43. LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.30434
- **AI 摘要**: LongDS-Bench是长时程多轮数据分析基准，包含68个真实世界任务和2225轮交互，评估智能体维护和演化分析状态的能力。最佳模型准确率仅48.45%，长时程错误占失败52%-69%，揭示现有智能体在长时程分析中的严重不足。
- **原始摘要**: arXiv:2605.30434v2 Announce Type: replace-cross Abstract: Real-world data analysis is inherently iterative, yet existing benchmarks mostly evaluate isolated or short interactive tasks, leaving agents'...

### 44. Securing Multi-Agent GIS Systems: Risk Evaluation and Prompt Hardening Optimization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.17092
- **AI 摘要**: 本文提出面向多智能体GIS系统的安全框架，涵盖风险识别、评估和缓解，采用模块化状态机编排、红队攻击和提示优化，通过对抗演示注入增强系统鲁棒性，并验证了框架的通用性。
- **原始摘要**: arXiv:2606.17092v2 Announce Type: replace-cross Abstract: Agentic systems are increasingly integrated with geographic information systems (GIS), where multi-agent coordination enables complex conversa...

### 45. Closing the Operational Gap in Semantic Caching
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.19719
- **AI 摘要**: 本文指出语义缓存系统常用PR-AUC指标忽略固定阈值可用性，导致部署选择不佳。提出P-CHR AUC和操作保留率指标，分解离线与部署质量差距，发现训练目标决定阈值效用差距，为语义缓存评估提供新方法。
- **原始摘要**: arXiv:2606.19719v3 Announce Type: replace-cross Abstract: Semantic caching cuts LLM inference costs by serving a cached response to semantically similar queries. Standard practice evaluates these syst...

### 46. Set-shifting Behavioral Test for Harnessed Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.13396
- **AI 摘要**: 本文借用认知心理学中的集合转换概念，设计测试评估LLM智能体在工具可靠性变化时的适应能力。实验显示不同模型对相同转换表现出不同行为，前沿模型持续调用可靠工具组，而较弱模型常遗漏，揭示了智能体适应性的差异。
- **原始摘要**: arXiv:2607.13396v2 Announce Type: replace-cross Abstract: What happens to an LLM agent's tool choice when the reliable tool silently changes within an ongoing session? We borrow the notion of set-shif...

### 47. When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.25553
- **AI 摘要**: 本文研究智能体在验证预算有限时，对继承记忆中过时约束的验证失败问题。实验显示，多数语言模型很少重新验证看似已定的约束，导致在约束被撤销后仍做出过时决策。通过重新分配验证槽位可显著改善该问题。
- **原始摘要**: arXiv:2608.25553v3 Announce Type: replace-cross Abstract: Provenance links keep the evidence behind an inherited belief reachable; an agent with a verification budget must still choose which links to...

### 48. SegBench-GC: Testing Segmentation Invariance in Multi-Step Offline Goal-Conditioned Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27678
- **AI 摘要**: 本文介绍SegBench-GC，一个用于测试离线目标条件强化学习分割不变性的压力测试框架，通过控制变量研究人工分割边界对算法性能的影响。
- **原始摘要**: arXiv:2608.27678v1 Announce Type: new Abstract: Offline goal-conditioned reinforcement learning (GCRL) often uses trajectory structure for future-goal sampling and multi-step targets, yet logged traje...

### 49. HARTS: Efficient Agentic Reinforcement Learning for Hybrid-Attention Models over Arbitrary Rollout Trees
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28158
- **AI 摘要**: 本文提出HARTS系统，用于混合注意力模型的高效智能体强化学习，通过规划微批次和调度，减少重复计算，提升训练效率。
- **原始摘要**: arXiv:2608.28158v1 Announce Type: new Abstract: Agentic reinforcement learning (RL) often produces irregular rollout trees with shared histories. Training root-to-leaf trajectories independently recom...

### 50. Deriving Scaling Laws for OpenEuroLLM Models: Learning Rate, Batch Size and Loss
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28308
- **AI 摘要**: 本文研究OpenEuroLLM模型预训练中学习率、批量大小与损失之间的缩放规律。探讨了最优超参数随模型规模和数据量的边际演化，以及学习率退火带来的收益，并评估了新的缩放形式对欠训练和过训练状态的捕捉能力。
- **原始摘要**: arXiv:2608.28308v1 Announce Type: new Abstract: We study the scaling behavior of learning rate and batch size in pretraining dense large language models on English-prevalent corpora. Beyond scaling \t...

### 51. Blog: Survey of Optimizers
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28557
- **AI 摘要**: 本文综述了2025-2026年神经网络优化器的最新进展，从坐标级扩展到矩阵级、层级，从固定训练周期到时间策略，从数学更新规则到状态表示。按时间估计、更新几何、周期管理、表示与系统四个独立轴组织，并指出矩阵感知方法是真正进步，但无通用替代方案。
- **原始摘要**: arXiv:2608.28557v1 Announce Type: new Abstract: Neural-network optimization in 2025-2026 is no longer well described as a succession of new Adam variants. The design space has expanded from coordinate...

### 52. On the Computational and Statistical Efficiency of the Empirical Maximum Entropy on the Mean Method
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27705
- **AI 摘要**: 本文研究经验最大熵均值（MEM）方法的计算与统计效率，建立了期望收敛率O(n^{-1/2})，优于此前O(n^{-1/4})的保证。通过原始和对偶问题的稳定性分析，并将MEM对偶问题重构为期望风险最小化，使其适用于随机优化。
- **原始摘要**: arXiv:2608.27705v1 Announce Type: cross Abstract: The Maximum Entropy on the Mean (MEM) method provides a flexible computational framework for solving inverse problems by combining data fidelity with...

### 53. Localizing Global Discrepancies: Marginal Contributions and Contextual Anomaly Detection
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28375
- **AI 摘要**: 本文开发了一个框架，通过为每个观测分配随机统计上下文中的条件或边际贡献，定位全局差异的来源。将重采样诊断和数据估值与投影理论及事件级异常检测联系起来，并推导出更高效的估计器。
- **原始摘要**: arXiv:2608.28375v1 Announce Type: cross Abstract: Global goodness-of-fit and discrepancy statistics can establish that a sample departs from a reference distribution without identifying which observat...

### 54. ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.12451
- **AI 摘要**: ToolSense是一个开源诊断框架，用于审计LLM中的参数化工具知识。它自动生成三个基准测试，包括真实检索基准，以评估模型对工具语义的真正理解，弥补现有基准仅依赖受限解码和冗长查询的不足。
- **原始摘要**: arXiv:2606.12451v2 Announce Type: replace-cross Abstract: Large language models deployed as agents over large tool catalogs face a critical tool-retrieval bottleneck. As embedding-based retrieval appr...

### 55. Gen-TAS: A Generative AI-Aided Hardware-Software Task Allocation Framework for FPGA-GPP Heterogeneous Systems
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28160
- **AI 摘要**: 提出Gen-TAS框架，利用知识增强的LLM为FPGA-GPP异构系统生成硬件软件任务分配策略。结合任务图分析和RAG，支持多目标优化，并通过人在回路和确定性后端实现可复现的FPGA SoC实现，在CNN和SDR负载上验证了有效性。
- **原始摘要**: arXiv:2608.28160v1 Announce Type: new Abstract: FPGA-GPP heterogeneous systems combine software flexibility with the performance and energy efficiency of reconfigurable hardware. However, determining...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
