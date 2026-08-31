# RSS 聚合报告 - Harness工程

**生成时间**: 2026-09-01 07:13:39
**文章数量**: 52 篇

---

### 1. Your GNN is probably just an overcomplicated MLP (Tabular Leakage). We built SynthFin-AML to enforce strict causal boundaries. [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-31T16:21:10+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w3imxy/your_gnn_is_probably_just_an_overcomplicated_mlp/
- **AI 摘要**: 文章指出图神经网络（GNN）在表格数据上可能退化为过复杂的MLP，存在表格泄漏问题。作者构建了SynthFin-AML数据集，通过严格因果边界来避免泄漏，确保模型学习真正的图结构信息而非表格特征。该工作旨在为金融反洗钱（AML）领域提供更可靠的GNN评估基准，推动模型在真实场景中的有效性。
- **原始摘要**: We noticed our anti-money laundering models were performing suspiciously well. After digging into standard baselines on dynamic graphs, we found widespread temporal leakage in message-passing. If you...

### 2. How to assess if there is a strong signal in your dirty data [Project]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-31T12:02:54+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w3br9c/how_to_assess_if_there_is_a_strong_signal_in_your/
- **AI 摘要**: 文章讨论了如何评估脏数据中是否存在强信号。作者提出了一套方法论，包括数据清洗、特征分析、统计检验和可视化等手段，帮助研究者判断数据中是否包含有意义的模式或趋势，避免被噪声误导。内容强调在数据质量不佳时仍能提取可靠信号的重要性，适合数据科学实践者参考。
- **原始摘要**: I'm sharing this new tabular data diagnostic tool (Entropic Scree). It can be used to estimate these properties of your high-d, real-world, dirty dataset: The informational volume of the signal (i.e.,...

### 3. Cycle-Level Simulator for Distributed GPUs For AI Workloads (Purdue)
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Sun, 30 Aug 2026 07:02:05 +0000 (2 天前)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/cycle-level-simulator-for-distributed-gpus-for-ai-workloads-purdue/
- **AI 摘要**: 普渡大学的研究人员提出了一种用于AI工作负载的分布式GPU周期级仿真框架，支持Ampere、Hopper和Blackwell等现代GPU架构。该框架在H100 GPU上验证了99%的皮尔逊相关系数，展示了高精度。研究旨在架构下一代异步分布式GPU，通过仿真探索多芯片模块、NVLink互连和L2缓存等设计空间，为AI时代的GPU架构优化提供工具支持。
- **原始摘要**: Researchers from Purdue University published a technical paper titled “Architecting the Next Generation of Asynchronous, Distributed GPUs for the AI Era.” Abstract Excerpt: The paper presents a “cycle...

### 4. Predicting Post-Route PPA from Macro and Standard-Cell Placements (U. of Alberta)
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Sat, 29 Aug 2026 17:00:22 +0000 (2 天前)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/predicting-post-route-ppa-from-macro-and-standard-cell-placements-u-of-alberta/
- **AI 摘要**: 阿尔伯塔大学的研究人员提出了PPAPlace，一种可微分的跨阶段目标优化方法，用于芯片布局优化。研究发现传统布局方法优化的半周长线长（HPWL）与布线后时序指标（如WNS和TNS）相关性接近零，导致AI布局器性能退化。PPAPlace通过双流预测器结合图注意力和空间卷积，从宏单元和标准单元布局预测布线后PPA，并使用布线后标签训练。预测的时序梯度端到端传播到单元坐标，作为协同目标或后布局优化步骤，显著改善布局质量。
- **原始摘要**: Researchers from University of Alberta published a technical paper titled “PPAPlace: Differentiable Cross-Stage Objectives for Chip Placement Optimization.” Abstract: “Macro placement significantly af...

### 5. Trust, But Verify
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Mon, 31 Aug 2026 07:03:35 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/trust-but-verify/
- **AI 摘要**: 本文是Brian Bailey的评论文章，探讨了在半导体设计和验证中“信任但验证”的原则。作者回顾了自己职业生涯中遇到的工具缺陷、规格边界错误、规格遗漏等问题，强调即使设计师尽力而为，工具和规格也不可能完美。随着AI在设计和验证中的介入，AI的不可预测性使得验证变得更加重要。文章呼吁在AI辅助设计中保持警惕，不能盲目信任AI的输出，必须通过严格的验证流程确保正确性，尤其是在安全关键应用中。
- **原始摘要**: We trust designers to do the best they can, but know they cannot be perfect. That's why we verify. When AI gets involved, it cannot be trusted. The post Trust, But Verify appeared first on Semiconduct...

### 6. Benchmarking General Mobile Assistants in Challenging Real-World Scenarios
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27477
- **AI 摘要**: 提出GMA基准，基于开源应用构建7个应用和300个任务，评估通用移动助手在真实场景中的表现，发现当前模型随任务复杂度增加性能显著下降。
- **原始摘要**: arXiv:2608.27477v1 Announce Type: cross Abstract: Graphical user interfaces have emerged as an important environment for evaluating autonomous AI agents on multimodal interactive tasks. Existing bench...

### 7. CompareBench: A Benchmark for Visual Comparison Reasoning in Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.22737
- **AI 摘要**: 本文介绍CompareBench基准套件，包含TallyBench、OmniCaps和CompareBench三个资源，用于评估视觉语言模型在数量、几何、空间和时间比较推理上的能力。评估九个闭源模型发现整体性能强但存在持续失败，特别是在计数和复杂比较场景中。
- **原始摘要**: arXiv:2509.22737v3 Announce Type: replace Abstract: Visual comparison reasoning is a fundamental capability of vision-language models (VLMs), covering judgments of object quantity, geometric dimension...

### 8. Scientific Graphics Program Synthesis via Dual Self-Consistency Reinforcement Learning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.06079
- **AI 摘要**: 本文提出一个闭环框架，包含SciTikZ-230K高质量数据集和SciTikZ-Bench多维度基准，用于科学图形程序合成。通过执行中心数据引擎和双自一致性强化学习，解决现有图像-TikZ语料库可执行性和视觉对齐不足的问题，提升多模态大语言模型生成TikZ代码的准确性和保真度。
- **原始摘要**: arXiv:2604.06079v2 Announce Type: replace Abstract: Graphics Program Synthesis is pivotal for interpreting and editing visual data, effectively facilitating the reverse-engineering of static visuals i...

### 9. SDGBiasBench: Benchmarking and Mitigating Vision--Language Models' Biases in Sustainable Development Goals
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.21919
- **AI 摘要**: 本文提出SDGBiasBench，一个大规模基准套件，用于评估视觉语言模型在可持续发展目标推理中的偏差。包含50万道专家参与的多选题和5万回归任务，评估决策级和估计级偏差，揭示当前VLM存在内在SDG偏差，即用先验替代证据。
- **原始摘要**: arXiv:2605.21919v2 Announce Type: replace Abstract: Assessing progress toward the Sustainable Development Goals (SDGs) requires multi-step reasoning over visual cues, contextual knowledge, and develop...

### 10. PolyComp: A Polycube-based Benchmark for Compositional 3D Spatial Reasoning in Multimodal Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.14741
- **AI 摘要**: 介绍PolyComp基准，用于评估多模态模型的组合3D空间推理能力。包含120个问题，测试GPT-5.6、Claude Fable 5和Gemini 3.1等模型，结果显示准确率差异大，最高仅50%，表明该任务对现有模型极具挑战性。
- **原始摘要**: arXiv:2608.14741v2 Announce Type: replace Abstract: We introduce PolyComp, a procedurally generated and verified benchmark that stresses visual recognition and compositional spatial reasoning. In each...

### 11. SciReC: Diagnostic Evaluation of Multimodal, Multi-Turn Relational Reasoning with Adaptive Interaction
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27461
- **AI 摘要**: 本文介绍了SciReC，一个用于评估多模态大语言模型在关系推理能力上的自适应学术对话基准，并提出了基于缺陷的诊断框架DMRA来量化各组件贡献，识别失败原因。Claude 4.6表现最佳，得分73%。
- **原始摘要**: arXiv:2608.27461v1 Announce Type: new Abstract: Relational reasoning requires the process of perceptual understanding, comparing, and integrating the underlying relationships between concepts. This ab...

### 12. Select, Don't Train: The Benefits of Modular Entity Disambiguation with LLM-Based Selection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27470
- **AI 摘要**: 本文系统比较了在共享LLM选择阶段下，不同候选实体检索策略（稀疏检索、Web搜索、密集检索）对实体消歧性能的影响，发现模块化方法优于联合训练，且无需昂贵训练的检索器维护。
- **原始摘要**: arXiv:2608.27470v1 Announce Type: new Abstract: Entity Disambiguation (ED) is a key task for constructing and using knowledge graphs. State-of-the-art neural approaches commonly model ED as a single t...

### 13. A Survey on Rubric-Guided Reinforcement Learning for Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27505
- **AI 摘要**: 本文综述了基于评分标准的强化学习（Rubric-guided RL）在语言模型对齐中的应用，提出贝叶斯框架统一理解宪法和评分标准，并沿先验-后验轴分类了宪法AI、实例特定评分标准、过程级监督等变体。
- **原始摘要**: arXiv:2608.27505v1 Announce Type: new Abstract: Reinforcement learning from human feedback (RLHF) has become the dominant paradigm for aligning large language models (LLMs) with human preferences. How...

### 14. Knowing Before Answering: Decoding Language Models for Reliable RAG
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27661
- **AI 摘要**: 本文提出一种基于模型内部信号的三分类方法，用于判断RAG系统中检索文档信息是否充分、不足或冲突。通过隐藏激活和注意力特征训练轻量线性模型，在16种语言模型上验证了该路由器的有效性，提升RAG可靠性。
- **原始摘要**: arXiv:2608.27661v1 Announce Type: new Abstract: In Retrieval-Augmented Generation (RAG), retrieval may provide insufficient or conflicting information needed to answer a question. The system should no...

### 15. EvoHarmBench: Breaking Content Moderation with Iterative Human-Like Evasion
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27844
- **AI 摘要**: 本文提出EvoHarmBench，首个动态对抗性内容审核评估框架，通过迭代优化在语义簇级别演化规避策略，同时优化规避成功率和人类可读性。覆盖5类违规、229个子簇，系统评估了LLM防御模型，弥补静态基准的不足。
- **原始摘要**: arXiv:2608.27844v1 Announce Type: new Abstract: Existing evaluations of harmful content detection rely predominantly on static benchmarks, which struggle to reflect the interactive adversarial ecosyst...

### 16. OpenStamp: A Watermark for Open-Source Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27899
- **AI 摘要**: 本文提出OpenStamp，一种针对开源语言模型的权重水印技术，通过修改最终投影层将水印逻辑编码进模型权重。实验表明该方法检测性能优越，能力退化最小，且对白盒攻击更鲁棒。
- **原始摘要**: arXiv:2608.27899v1 Announce Type: new Abstract: With the growing prevalence of large language model (LLM) generated content, watermarking is considered a promising approach for attributing text to LLM...

### 17. What Makes Agent Memory Useful for Reliable Unanswerable Question Handling?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27924
- **AI 摘要**: 本文系统研究了智能体记忆中不可回答问题处理的作用，在统一框架下评估四种记忆方法。发现记忆提升效果具有选择性且脆弱，跨模型记忆复用比跨数据集更可行，决策指导比轨迹塑造更能保留提升效果。
- **原始摘要**: arXiv:2608.27924v1 Announce Type: new Abstract: Reliable handling of unanswerable questions (UAQs) is critical for trustworthy LLM-based agents. Although memory is widely used in agent systems, its ro...

### 18. Entity-Memory Graph Retrieval Improves Evidence Coverage in Long-Conversation Question Answering
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27925
- **AI 摘要**: 提出实体记忆图检索方法，通过实体链接和时序边增强长对话问答中的证据覆盖。在LoCoMo数据集上，图检索将top-k=25的证据召回率从79.75%提升至84.48%，且优势在多个k值下稳健。
- **原始摘要**: arXiv:2608.27925v1 Announce Type: new Abstract: Entity-Memory graph retrieval keeps dialogue turns as verbatim Memory nodes, links repeated mentions through shared Entities, and connects adjacent Memo...

### 19. CNeo-Bench: Diagnosing Large Language Models on Chinese Neologisms
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28053
- **AI 摘要**: 介绍CNeo-Bench基准，包含4759个中文新词，评估18个LLM。发现中文新词仍是挑战，多数模型定义生成低于40%，且存在识别-操作差距，模型能描述但无法正确还原源形式。
- **原始摘要**: arXiv:2608.28053v1 Announce Type: new Abstract: Chinese neologisms exploit diverse and unique linguistic mechanisms, such as phonetic substitution (e.g., 886 for ``bye-bye'') and visual character deco...

### 20. PersonaForge: Realistic Multi-Turn User Simulation for Agentic Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28378
- **AI 摘要**: 提出PersonaForge框架，用于合成真实多轮用户-智能体交互。基于16K真实会话分析，构建6.3K训练数据和138任务基准，实验表明能提升智能体系统的多轮交互能力。
- **原始摘要**: arXiv:2608.28378v1 Announce Type: new Abstract: Large language models are increasingly used as agentic workflow executors, yet existing training data and benchmarks largely assume informationally comp...

### 21. CultureConverse: A Multilingual Multi-turn Simulation Harness for Culturally Grounded Assistance in East and Southeast Asia
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28405
- **AI 摘要**: 提出CultureConverse，一个多语言多轮文化场景模拟与评估框架，覆盖东亚和东南亚10个地区，包含基准数据集和评估协议，用于测试LLM在文化场景中的辅助能力。
- **原始摘要**: arXiv:2608.28405v1 Announce Type: new Abstract: Current cultural evaluations for large language models (LLMs) often reduce culture to single-turn factual recall via MCQs, failing to capture a common u...

### 22. ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28476
- **AI 摘要**: 提出ContextPilot，一种用于长时程智能体任务的主动上下文管理框架，通过细粒度强化学习支持全局规划、长期记忆和自适应压缩，解决现有方法工具集有限和信用分配粗糙的问题。
- **原始摘要**: arXiv:2608.28476v1 Announce Type: new Abstract: Long-horizon agentic tasks require large language models (LLMs) to iteratively retrieve, integrate, and maintain dispersed information across multi-turn...

### 23. Blind Men and the Elephant: Probing the Epistemic Myopia of LLMs under Long-Tail Divergent Knowledge
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28478
- **AI 摘要**: 引入ElephantBench基准，测试LLM对长尾事实的多种分歧性知识记忆能力，发现即使最强模型也只能恢复52.4%的双重答案，模型规模增大和推理增强不能完全解决知识不完整问题。
- **原始摘要**: arXiv:2608.28478v1 Announce Type: new Abstract: Factual question answering (QA) typically assumes a single canonical answer, obscuring whether large language models (LLMs) retain divergent accounts of...

### 24. NL2AGBench: Benchmarking LLM Auto-Formalization for AlphaGeometry
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28481
- **AI 摘要**: 提出NL2AGBench基准，评估LLM将英文几何问题自动形式化为AlphaGeometry专用DSL的能力，采用执行验证方式衡量翻译质量，旨在解决手动转换的瓶颈。
- **原始摘要**: arXiv:2608.28481v1 Announce Type: new Abstract: Recent advances in large language models (LLMs) have demonstrated strong capabilities in natural language understanding and mathematical reasoning. Howe...

### 25. Quantization-Triggered Backdoors in Language Models: Cross-Quantizer Transferability and the Validation--Deployment Gap
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27512
- **AI 摘要**: 本文提出量化触发后门攻击，利用量化导致的验证-部署差距，在满足源精度检查的模型中嵌入恶意负载，激活时产生对抗行为。
- **原始摘要**: arXiv:2608.27512v1 Announce Type: cross Abstract: Post-training quantization is often treated as a semantically neutral optimization for edge deployment of Large Language Models. When a full-precision...

### 26. The Calls are Coming from Inside the Model: Investigating Probe-based Detection of Tool-Calling Errors in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27750
- **AI 摘要**: 研究使用线性探针检测LLM工具调用错误，在18个模型上评估，发现探针能有效捕获多种错误，包括类型正确但值错误的参数，模型大小和层数影响效果。
- **原始摘要**: arXiv:2608.27750v1 Announce Type: cross Abstract: The hidden states of large language models (LLMs) are known to capture rich information relating to model knowledge and behavior that can be hard to e...

### 27. Why Didn't It Check? Unsupported Final Claims and Their Repair in Two Tool-Equipped Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27768
- **AI 摘要**: 分析语言模型在工具辅助下做出无证据支持的最终声明，定义发生率和条件修复两个量，通过重放实验研究修复机制。
- **原始摘要**: arXiv:2608.27768v1 Announce Type: cross Abstract: A language model with access to tools can commit to a final claim unsupported by the evidence it has seen, even when a single available tool call woul...

### 28. Memorization Is Not Extraction: Tight Differential-Privacy Bounds and Audit Blind Spots
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27782
- **AI 摘要**: 严格界定反事实记忆和自适应提取的差分隐私常数，证明二者互不控制，并揭示审计盲点，提出基于最小熵的分布无关界。
- **原始摘要**: arXiv:2608.27782v1 Announce Type: cross Abstract: Memorization in large language models is measured through a zoo of definitions whose formal relations are unknown, and differential privacy (DP) is tr...

### 29. SURE-Challenge: Evaluating Speech Evidence Before Speech-LLM Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27783
- **AI 摘要**: 提出SURE-Challenge基准，评估语音LLM在生成前拒绝不支持输入的能力，实验显示简单规则可大幅提升拒绝率而不影响支持输入准确率。
- **原始摘要**: arXiv:2608.27783v1 Announce Type: cross Abstract: Speech LLMs are usually graded after they answer, although an operating system first has to decide whether a waveform should be sent to the model. We...

### 30. Auditing Generative Audio Calls for Known-Task Audio-LLM Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27817
- **AI 摘要**: 审计生成式音频调用，区分声学证据访问与生成模型调用，实验表明监督编码器可达到高准确率而无需生成调用，提出调用决策问题。
- **原始摘要**: arXiv:2608.27817v1 Announce Type: cross Abstract: Speech and audio LLMs are often evaluated by asking whether a waveform prompt beats an automatic speech recognition (ASR) transcript. For known closed...

### 31. Benchmarking large language model agent societies against human behavioural distributions
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28182
- **AI 摘要**: 本文介绍SILICA工具，用于测试大语言模型代理社会是否像人类行为分布、结果是否受装置变化影响以及社会动态是否真实。在五个环境、十二个开源模型上测试，发现模型仅在初始阶段与人类数据一致。
- **原始摘要**: arXiv:2608.28182v1 Announce Type: cross Abstract: Populations of large language model agents are increasingly used as experimental societies. Three doubts shadow every such result: whether the agents...

### 32. Stay Within Your Bounds: Distance-Guided Decoding for Guaranteed Context-Free Grammar Compliance
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28229
- **AI 摘要**: 提出基于下推自动机的lookahead引导解码框架，通过离线计算有界下推摘要和距离估计，实现在线剪枝和束搜索，保证语法合规性。在JSON、SQL和LTL上验证了语法有效性和完成质量提升。
- **原始摘要**: arXiv:2608.28229v1 Announce Type: cross Abstract: Grammar-constrained decoding helps large language models produce syntactically valid structured outputs, such as code, JSON, and SQL. For context-free...

### 33. Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28327
- **AI 摘要**: 研究大语言模型多层防御的叠加效果，提出对手访问层级模型和成本模型，测量防御层之间的失败相关性。发现防御堆叠的覆盖饱和、成本上升、误拒累积，仅在独立失败时攻击成功率才乘法下降。
- **原始摘要**: arXiv:2608.28327v1 Announce Type: cross Abstract: Practitioners defend large language models (LLMs) by stacking defenses, assuming the layers compound. A stack is an ensemble, and ensembles compound o...

### 34. Evaluating the Performance of Large Language Models on GAOKAO Benchmark
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2023年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2305.12474
- **AI 摘要**: 介绍GAOKAO-Bench基准，使用中国高考题目评估大语言模型性能，包括主观和客观题。发现GPT-4、ChatGPT和ERNIE-Bot在高考中取得有竞争力分数，但各科目表现差异显著。
- **原始摘要**: arXiv:2305.12474v4 Announce Type: replace Abstract: Large Language Models(LLMs) have demonstrated remarkable performance across various natural language processing tasks; however, how to comprehensive...

### 35. Auditing LLM Benchmarks with Item Response Theory
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.30504
- **AI 摘要**: 本文提出基于项目反应理论的指标，用于审计LLM基准测试中的错误标签，在七个基准测试中达到95%精度，并发现奖励模型偏向风格而非事实知识。
- **原始摘要**: arXiv:2605.30504v2 Announce Type: replace Abstract: LLM benchmark labels are frozen at release and silently propagated into downstream benchmarks, errors and all. We introduce an Item Response Theory-...

### 36. Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.01629
- **AI 摘要**: 本文介绍LongJudgeBench基准，用于评估LLM作为裁判在长文本输出评估中的可靠性，涵盖多种场景和评估协议，系统评估多个基础模型和设置。
- **原始摘要**: arXiv:2606.01629v4 Announce Type: replace Abstract: As large language models (LLMs) are increasingly used for long-form generation, reliably evaluating long-form outputs has become a critical challeng...

### 37. Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.05122
- **AI 摘要**: 本文提出自我评估激发方法，通过少量数据激发基础LLM预测外部裁判评分的能力，在三个基准上提升校准性能，同时保持答案质量。
- **原始摘要**: arXiv:2606.05122v2 Announce Type: replace Abstract: Large language models are increasingly evaluated by other models, raising a natural question: can a model predict how a judge will score its own out...

### 38. TokenPilot: Cache-Efficient Context Management for LLM Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.17016
- **AI 摘要**: 本文提出TokenPilot，一种双粒度上下文管理框架，通过稳定前缀和生命周期感知驱逐，平衡文本稀疏性与提示缓存连续性，降低LLM代理推理成本。
- **原始摘要**: arXiv:2606.17016v2 Announce Type: replace Abstract: As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dyn...

### 39. Does Finetuning with Scientific Data Increase Hallucinations? A Multi-domain Factuality Evaluation of LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.21359
- **AI 摘要**: 本文创建SciFactCheck基准，评估科学微调LLM的幻觉现象，发现科学微调模型在所有幻觉类型和领域上事实可靠性下降。
- **原始摘要**: arXiv:2606.21359v2 Announce Type: replace Abstract: Large language models (LLMs) are increasingly used to communicate and explain scientific concepts, yet their tendency to hallucinate poses significa...

### 40. ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.26403
- **AI 摘要**: 本文提出ProfileFoundry，一个确定性生成器，发布10万个合成人物对象，用于隐私、记忆和工具使用评估，确保跨字段和时间一致性。
- **原始摘要**: arXiv:2606.26403v2 Announce Type: replace Abstract: Foundation-model research increasingly needs data about people: user state, personal histories, relationships, contact-like fields, documents, and l...

### 41. JuryProbe: An Empirical Consensus-Risk Diagnostic for Routing Reference-Free Factuality Judge Panels to Grounded Verification
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.20607
- **AI 摘要**: JuryProbe是一种用于参考无关事实性法官面板的共识风险诊断方法，结合基于校准的路由策略。它通过仅假阴性相关性和假共识提升来估计共识风险，高风险时路由到带可信参考的法官，以降低因共享盲点导致的错误接受风险。
- **原始摘要**: arXiv:2608.20607v2 Announce Type: replace Abstract: Panels of inexpensive LLM judges increasingly make accept-or-escalate decisions. In factuality settings, accepting a claim because several reference...

### 42. PRISM: Self-Pruning Intrinsic Selection Method for Training-Free Multimodal Data Selection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2502.12119
- **AI 摘要**: PRISM是一种无需训练的多模态数据选择方法，通过自剪枝内在选择机制解决视觉指令调优中数据冗余和计算成本高的问题。它识别视觉特征分布的各向异性导致的全局语义漂移，并据此进行高效数据选择。
- **原始摘要**: arXiv:2502.12119v5 Announce Type: replace-cross Abstract: Visual instruction tuning adapts pre-trained Multimodal Large Language Models (MLLMs) to follow human instructions for real-world applications...

### 43. SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.12015
- **AI 摘要**: SkillSafetyBench是一个评估智能体在技能面对攻击面时安全性的基准，包含155个对抗案例，覆盖47个任务、6个风险域和30个安全类别。实验表明非用户攻击可一致诱导不安全行为，揭示了现有安全评估的盲区。
- **原始摘要**: arXiv:2605.12015v3 Announce Type: replace-cross Abstract: Reusable skills are becoming a common interface for extending large language model agents, packaging procedural guidance with access to files,...

### 44. LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.30434
- **AI 摘要**: LongDS-Bench是一个长时程多轮数据分析基准，包含68个任务、2225轮对话，评估智能体在长时间跨度内维持、更新和组合分析状态的能力。最佳模型平均准确率仅48.45%，且性能随轮次显著下降，长时程错误占失败原因的52%-69%。
- **原始摘要**: arXiv:2605.30434v2 Announce Type: replace-cross Abstract: Real-world data analysis is inherently iterative, yet existing benchmarks mostly evaluate isolated or short interactive tasks, leaving agents'...

### 45. Securing Multi-Agent GIS Systems: Risk Evaluation and Prompt Hardening Optimization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.17092
- **AI 摘要**: 本文提出了一个面向多智能体GIS系统的安全框架，用于风险识别、评估和缓解。通过红队框架和自适应攻击者LLM评估鲁棒性，并利用提示优化框架将提示视为结构化签名并注入对抗示例，以增强系统韧性。
- **原始摘要**: arXiv:2606.17092v2 Announce Type: replace-cross Abstract: Agentic systems are increasingly integrated with geographic information systems (GIS), where multi-agent coordination enables complex conversa...

### 46. Closing the Operational Gap in Semantic Caching
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.19719
- **AI 摘要**: 本文指出语义缓存系统常用的PR-AUC指标忽略了固定阈值下的可用性，导致部署选择不佳。提出了缓存感知的P-CHR AUC指标和操作保留率，用于衡量离线排序质量在部署中的保留程度，并分解操作差距为可恢复和不可恢复部分。
- **原始摘要**: arXiv:2606.19719v3 Announce Type: replace-cross Abstract: Semantic caching cuts LLM inference costs by serving a cached response to semantically similar queries. Standard practice evaluates these syst...

### 47. Set-shifting Behavioral Test for Harnessed Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.13396
- **AI 摘要**: 本文借用认知心理学的集合转换概念，研究LLM智能体在工具可靠性隐藏变化时的适应能力。通过分支调度改变可靠工具组，比较不同模型的行为差异，发现不同模型对相同变化的反应不同，有的固守固定程序，有的持续变化。
- **原始摘要**: arXiv:2607.13396v2 Announce Type: replace-cross Abstract: What happens to an LLM agent's tool choice when the reliable tool silently changes within an ongoing session? We borrow the notion of set-shif...

### 48. When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.25553
- **AI 摘要**: 本文研究智能体在验证预算有限时，对继承记忆中过时约束的验证失败问题。实验发现，16个语言模型很少重新验证看似已定的约束，导致在约束被取代后产生过时一致决策的比例高达77.3%。重新分配验证槽位可显著减少此类失败。
- **原始摘要**: arXiv:2608.25553v3 Announce Type: replace-cross Abstract: Provenance links keep the evidence behind an inherited belief reachable; an agent with a verification budget must still choose which links to...

### 49. SegBench-GC: Testing Segmentation Invariance in Multi-Step Offline Goal-Conditioned Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.27678
- **AI 摘要**: 本文介绍SegBench-GC，一个用于测试离线目标条件强化学习中分割不变性的受控压力测试，通过保持其他因素固定，仅改变人工备份边界，研究分割对算法性能的影响，实验表明分割会显著降低成功率。
- **原始摘要**: arXiv:2608.27678v1 Announce Type: new Abstract: Offline goal-conditioned reinforcement learning (GCRL) often uses trajectory structure for future-goal sampling and multi-step targets, yet logged traje...

### 50. HARTS: Efficient Agentic Reinforcement Learning for Hybrid-Attention Models over Arbitrary Rollout Trees
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28158
- **AI 摘要**: 本文提出HARTS系统，用于混合注意力模型的高效智能体强化学习，通过联合规划微批次、数据并行副本分配和调度，利用前缀压缩和线性时间算法，减少计算重复，提升训练效率。
- **原始摘要**: arXiv:2608.28158v1 Announce Type: new Abstract: Agentic reinforcement learning (RL) often produces irregular rollout trees with shared histories. Training root-to-leaf trajectories independently recom...

### 51. ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.12451
- **AI 摘要**: ToolSense是一个开源诊断框架，用于审计LLM的参数化工具知识，自动生成三个基准测试，包括真实检索基准等，以评估模型对工具语义的真正理解，弥补现有基准仅依赖受限解码和冗长查询的不足。
- **原始摘要**: arXiv:2606.12451v2 Announce Type: replace-cross Abstract: Large language models deployed as agents over large tool catalogs face a critical tool-retrieval bottleneck. As embedding-based retrieval appr...

### 52. Gen-TAS: A Generative AI-Aided Hardware-Software Task Allocation Framework for FPGA-GPP Heterogeneous Systems
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28160
- **AI 摘要**: 本文提出Gen-TAS，一种基于LLM和RAG的FPGA-GPP异构系统任务分配框架，结合任务图分析和历史知识，生成可解释的分配策略，并通过人机协同和确定性后端实现可复现的FPGA SoC实现。
- **原始摘要**: arXiv:2608.28160v1 Announce Type: new Abstract: FPGA-GPP heterogeneous systems combine software flexibility with the performance and energy efficiency of reconfigurable hardware. However, determining...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
