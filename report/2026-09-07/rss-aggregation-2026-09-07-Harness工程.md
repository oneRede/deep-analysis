# RSS 聚合报告 - Harness工程

**生成时间**: 2026-09-08 10:13:28
**文章数量**: 57 篇

---

### 1. Measuring LLM performance drift: observations and methodology from 31,352 repeated benchmark measurements [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-09-07T07:44:34+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/
- **AI 摘要**: 该文章报告了基于31,352次重复基准测量对LLM性能漂移的观察和方法论。研究可能发现模型在多次运行中输出不一致，导致性能波动，并提出了测量和量化漂移的框架。文章旨在提高LLM评估的可靠性，讨论漂移来源（如采样、硬件、版本）及缓解策略，对模型部署和监控有重要参考价值。
- **原始摘要**: One thing that has bothered me about LLM benchmarks for a while is that most of them are essentially snapshots. A model is evaluated, a score is published, and we tend to talk about that score as if i...

### 2. How the AI ROI Gap Comes Down to Trust
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Mon, 07 Sep 2026 15:38:00 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.bloomberg.com/news/videos/2026-09-07/how-the-ai-roi-gap-comes-down-to-trust-video
- **AI 摘要**: SAS的新研究显示，投资于可信AI实践的公司更有可能从技术中获得高回报。然而信任仍是障碍：97%的用户至少有时会覆盖AI建议，员工对日益自主的AI代理信任度较低。SAS执行副总裁兼首席信息官Jay Upchurch在彭博电视上讨论了这一发现，强调了建立AI信任的重要性。
- **原始摘要**: Companies investing in trustworthy AI practices are far more likely to see strong returns from the technology, according to new research from SAS. But trust remains a hurdle: 97% of users override AI...

### 3. Post Fusion Bird's Eye View Feature Stabilization for Robust Multimodal 3D Detection
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.05623
- **AI 摘要**: 提出后融合稳定器(PFS)，一种轻量模块，作用于现有检测器的中间鸟瞰图表示，在域偏移和传感器故障下稳定特征统计、抑制退化区域并自适应恢复弱化线索，无需修改融合架构或重新训练。
- **原始摘要**: arXiv:2603.05623v2 Announce Type: replace Abstract: Camera-LiDAR fusion is widely used in autonomous driving to enable accurate 3D object detection. However, bird's-eye view (BEV) fusion detectors can...

### 4. A Systematic Evaluation of Cross-Lingual Consistency Enhancement Methods in Multilingual Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04409
- **AI 摘要**: 本文对多语言模型的跨语言一致性增强方法进行了统一评估，涵盖推理时干预和训练后方法。结果显示训练后方法更可靠，直接分布对齐持续提升一致性，跨领域迁移有限，除非源和目标任务输出格式相似。
- **原始摘要**: arXiv:2609.04409v1 Announce Type: new Abstract: Multilingual language models often produce inconsistent answers to semantically equivalent questions across languages, motivating methods to improve cro...

### 5. GRACE: Graph-Grounded Reflective Agent Copilot Engine for Expert-in-the-Loop Knowledge Expansion
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04442
- **AI 摘要**: GRACE是一个图基反思智能体框架，将LLM响应分解为原子声明，并在加权二分图中与可信先验知识进行比对，通过中心性分析分类为有据、反驳或边界。引入注意力回报目标，优化人类或智能体资源分配，用于专家在环的知识扩展。
- **原始摘要**: arXiv:2609.04442v1 Announce Type: new Abstract: Large language models deployed in high-stakes settings frequently generate plausible but ungrounded claims. Standard retrieval-augmented generation (RAG...

### 6. Scale-QLoRA: Code-Invariant Adapter Merging for Native 4-bit Microscaling LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04526
- **AI 摘要**: Scale-QLoRA提出了一种针对原生4位微缩放模型的适配器合并方法，仅调整每块缩放因子并冻结代码，避免了传统合并导致的适配性能大幅下降，实现了高效部署。
- **原始摘要**: arXiv:2609.04526v1 Announce Type: new Abstract: Merging a LoRA adapter into its base model is standard deployment practice: it removes the runtime adapter's per-forward overhead and leaves a single st...

### 7. ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04648
- **AI 摘要**: 本文提出ConsensusBench数据集，通过聚类正确轨迹的中间结论提供基于规则的流程级奖励信号，以解决GRPO等强化学习方法在长推理任务中稀疏奖励不足的问题。
- **原始摘要**: arXiv:2609.04648v1 Announce Type: new Abstract: Reinforcement learning (RL) has become one of the primary paradigms for reasoning enhancement of large language models (LLMs). In particular, Group Rela...

### 8. Knowing What Not to Answer: Selective Non-Compliance in Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04720
- **AI 摘要**: 本文提出KoNA基准，用于评估视觉语言模型的选择性不服从能力，涵盖错误前提、视觉不可达、普遍未知、任务可行性和安全五类，并区分查询级和组件级不服从。评估发现模型常无法拒绝、纠正或回答。
- **原始摘要**: arXiv:2609.04720v1 Announce Type: new Abstract: Vision-language models (VLMs) are expected to respond helpfully to appropriate requests while withholding compliance with requests that are incorrect, u...

### 9. A Systematic Comparison of Multilingual Interpretability Methods Reveals Anisotropy-Driven Failures
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04819
- **AI 摘要**: 本文系统比较四种多语言可解释性方法，发现指标间分歧源于表示的各向异性。仅ILO与跨语言迁移的相关性（ρ=0.90）在控制模型大小、家族和任务后依然稳健，推荐使用ILO。
- **原始摘要**: arXiv:2609.04819v1 Announce Type: new Abstract: Multilingual language models develop shared cross-lingual representations, and various interpretability methods claim to quantify this sharing. These me...

### 10. On Epistemic Diversity in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04835
- **AI 摘要**: 本文从哲学角度提出LLM的认知多样性概念，指模型向用户展示的有效答案、解释和推理路径范围。提出初步测量框架，发现前沿LLM常表现出认知狭窄，重复相同内容。
- **原始摘要**: arXiv:2609.04835v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used not only to retrieve information, but to answer questions, explain, teach, and support inquiry. In su...

### 11. MMTClinic: Multimodal, Multilingual Time Series Question Answering and Reasoning Benchmark for Clinical Domain
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04842
- **AI 摘要**: 本文提出MMTClinic基准，用于评估LLM在临床时间序列上的多模态、多语言问答和推理能力。包含3万对问答，覆盖五种语言和三种问题类型，填补了临床AI评估空白。
- **原始摘要**: arXiv:2609.04842v1 Announce Type: new Abstract: Time-series data in clinical settings is crucial for capturing dynamic changes in a patient's health over time, enabling timely diagnosis, personalized...

### 12. Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04895
- **AI 摘要**: 本文针对MoE模型推理时专家权重重复传输问题，提出缓存感知的联合路由器适配框架，包括时间路由器和时空路由器，在Qwen3和GPT-OSS上提升缓存命中率并减少专家权重流量。
- **原始摘要**: arXiv:2609.04895v1 Announce Type: new Abstract: Mixture-of-Experts (MoE) models activate only a small subset of experts per token, but the full expert set often exceeds GPU memory, causing repeated we...

### 13. Compression Beyond the Uncompressed: A Two-Stage Training Recipe for Soft Context Compression in RAG
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05152
- **AI 摘要**: 提出DEX-Comp两阶段训练方法用于RAG中的软上下文压缩。先通过纯蒸馏预热，再用强化学习处理原始模型失败的查询，使压缩模型超越未压缩RAG的性能，在五个问答基准上将检索上下文压缩16倍并提升准确率。
- **原始摘要**: arXiv:2609.05152v1 Announce Type: new Abstract: Retrieval-Augmented Generation (RAG) enhances language models with external knowledge, but the lengthy retrieved context inflates the input and degrades...

### 14. A Verifier-Guided Explainable Reasoning Framework with Gold-Anchored QLoRA, Task-Aware Mixture-of-Experts, and Group-Relative RLVR
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05221
- **AI 摘要**: 提出一种验证器引导的可解释推理框架，结合金标准锚定QLoRA、任务感知混合专家和组相对RLVR，用于教育问答。通过逻辑和物理验证器反馈支持候选评估和自修正，从正确性、证据一致性和推理深度三个维度评估。
- **原始摘要**: arXiv:2609.05221v1 Announce Type: new Abstract: Large language models (LLMs) show strong reasoning ability, but their explanations can remain inconsistent, weakly grounded, or difficult to verify. We...

### 15. LexFlip: A Dissociation Diagnostic for Legal Meaning Preservation Metrics
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05296
- **AI 摘要**: 发布LexFlip诊断数据集，包含373个最小扰动样本，用于评估法律文本简化后语义保持度。现有指标在表面形式不变而法律效力改变时表现不佳，双向NLI表现最好，但长度特征仍优于所有语义指标，凸显了评估指标的缺陷。
- **原始摘要**: arXiv:2609.05296v1 Announce Type: new Abstract: Does a simplified legal clause still say what the original said? The checks in current use cannot establish that it does: requiring an identical pair to...

### 16. WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05405
- **AI 摘要**: 提出WearableQA基准，包含4084个基于200名真实用户可穿戴数据（时间序列、血液生物标志物等）的多选题，用于评估AI系统对纵向健康数据的推理能力。基准涵盖数据推理与健康推理、单信号与跨信号推理等16种问题类型。
- **原始摘要**: arXiv:2609.05405v1 Announce Type: new Abstract: Recent advances in wearable sensing enable continuous monitoring of physiological and behavioral signals, yet existing benchmarks rarely evaluate whethe...

### 17. Auditing Bias and Safety in Voice AI Customer Care
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04206
- **AI 摘要**: 本文针对语音AI客服系统提出了一种验证门控审计框架，用于检测偏见和安全问题。框架区分不同架构，控制呼叫者呈现条件，验证事实不变性和路径负担，并记录实质性结果和服务路径，以识别在最终拒绝前可能出现的额外负担。
- **原始摘要**: arXiv:2609.04206v1 Announce Type: cross Abstract: Voice AI systems increasingly mediate customer care interactions where caller presentation cues such as accent, affect, fluency, and urgency are avail...

### 18. EVOHARNESSBENCH: Can Your Agents Keep Pace with an Evolving Harness?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04280
- **AI 摘要**: 本文介绍EVOHARNESSBENCH基准，用于评估LLM智能体在工具、技能和智能体三个维度上的持续演化能力。该基准包含17个多阶段流程、802个任务，并评估部署和持续学习两种设置，以应对智能体工具链动态变化的挑战。
- **原始摘要**: arXiv:2609.04280v1 Announce Type: cross Abstract: Modern LLM-based agents operate through a harness of tools, reusable skills, and specialist agents that shapes what they observe and what they can do....

### 19. Harbor Adapters and Harbor-Index: Infrastructure and a Curated Meta-Dataset for Large-Scale Agentic Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04298
- **AI 摘要**: 本文提出Harbor Adapters统一评估基础设施，将80多个智能体基准适配到任意智能体，并大规模评估8个模型在54个基准上的表现。同时引入Harbor-Index精选数据集，包含82个高质量任务，用于深入分析智能体能力与失败模式。
- **原始摘要**: arXiv:2609.04298v1 Announce Type: cross Abstract: Evaluating agents on the growing number of agentic benchmarks is challenging because they often require complex environments and agent integrations. W...

### 20. A Removal Based Approach to Improve LLM Faithfulness at Test-Time
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04343
- **AI 摘要**: 本文提出一种测试时方法，通过移除输入因素来直接改善LLM解释的不完整性，即遗漏影响答案的因素。该方法无需访问模型权重或大量计算资源，补充了现有主要针对不健全性的测试时方法。
- **原始摘要**: arXiv:2609.04343v1 Announce Type: cross Abstract: Large language models (LLMs) are increasingly used for consequential decisions, making their explanations an important tool for auditing model behavio...

### 21. Conformity Breaks Conformal Prediction
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04445
- **AI 摘要**: 本文揭示多智能体LLM系统中，同伴一致错误答案会改变模型对正确答案的评分，导致符合性预测失效。校准覆盖率从90%降至74%，攻击者可针对低置信度子组将覆盖率从87%降至47%，影响系统决策。
- **原始摘要**: arXiv:2609.04445v1 Announce Type: cross Abstract: A conformal certificate can be valid when an LLM answers alone and invalid when the same LLM sees peers that unanimously assert a wrong answer. The qu...

### 22. Persistent Teacher Anchoring for Tool-Using Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04773
- **AI 摘要**: 本文提出持久教师锚定（PTA）方法，用于工具使用智能体的知识蒸馏。PTA保留块级验证并增加回合级承诺，使教师决定学生提出的工具调用是否执行，减少师生分布差距累积，提升下游强化学习效果。
- **原始摘要**: arXiv:2609.04773v1 Announce Type: cross Abstract: Distillation is common in LLM post-training, where on-policy knowledge distillation (OPKD) uses student-generated trajectories to prepare the student...

### 23. BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04971
- **AI 摘要**: 大型推理模型在长链推理中KV缓存内存瓶颈严重，现有压缩方法基于近期查询估计未来重要性，但在长时推理中失效。本文发现思考回溯令牌的查询在嵌入空间聚类，提出免训练的BeaconKV压缩方法。
- **原始摘要**: arXiv:2609.04971v1 Announce Type: cross Abstract: Large Reasoning Models (LRMs) achieve superior problem-solving through extended Chain-of-Thought (CoT) generation, but the resulting key-value (KV) ca...

### 24. TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05079
- **AI 摘要**: 现有AI科学家基准偏向复现而非发现。TruthInsightBench提供40个盲任务，仅暴露中性目标和冻结数据，用固定LLM法官按六维度评估代理自身主张的证据成熟度，实现自动化确定性聚合。
- **原始摘要**: arXiv:2609.05079v1 Announce Type: cross Abstract: Autonomous coding agents are increasingly proposed as AI-scientist systems that conduct analyses and write research reports, but executing a prescribe...

### 25. Measuring AI Accountability Through Argumentation Analysis: Can Model Reasoning Withstand Scrutiny?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05088
- **AI 摘要**: AI监督依赖真实标签，但适当行为存在争议。本文提出基于论证结构质量的替代标准，通过四阶段辩证协议测量模型辩护质量。在九个前沿模型和200个高模糊道德选择上验证，模型防御能力有限。
- **原始摘要**: arXiv:2609.05088v1 Announce Type: cross Abstract: AI oversight methods rely on ground truth for validation, but what constitutes appropriate AI behavior is contested. This leaves evaluation of moral r...

### 26. Technical Manual for a Toolkit for Measuring Contextual Individuation in Transformer Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05333
- **AI 摘要**: 本文档介绍测量Transformer语言模型上下文个体化的工具包，围绕桥接形式构建，涵盖规范说明、语料获取、表征提取、轮廓测量和可视化协议，并论证每个设计选择。
- **原始摘要**: arXiv:2609.05333v1 Announce Type: cross Abstract: A transformer language model assigns a single, context-independent vector to a word type at its embedding layer, yet is widely believed to individuate...

### 27. Harnessing the Reasoning Economy: A Survey of Efficient Reasoning for Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2503.24377
- **AI 摘要**: 本文综述了大型语言模型在推理经济性方面的研究，探讨了System 1与System 2推理的权衡，分析了推理低效的原因、不同推理模式的行为，并提出了在训练后和推理阶段优化性能与计算成本平衡的潜在解决方案。
- **原始摘要**: arXiv:2503.24377v2 Announce Type: replace Abstract: Recent advancements in Large Language Models (LLMs) have significantly enhanced their ability to perform complex reasoning tasks, transitioning from...

### 28. QoNext: Towards Next-generation QoE for Foundation Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.21889
- **AI 摘要**: 本文提出QoNext框架，将网络和多媒体中的体验质量原则应用于基础模型的整体评估，考虑生成速度和延迟等动态服务属性，通过受控实验和人类评分构建数据库，并训练神经网络预测器来估计用户体验。
- **原始摘要**: arXiv:2509.21889v3 Announce Type: replace Abstract: Existing evaluations of foundation models predominantly focus on output correctness, treating interaction as a static exchange of information. Howev...

### 29. Exploring Solution Divergence and Its Effect on Large Language Model Problem Solving
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.22480
- **AI 摘要**: 本文研究了大型语言模型针对同一问题生成解决方案的多样性，发现更高的解发散度与更好的问题解决能力正相关，并提出将解发散度作为新指标，支持监督微调和强化学习策略，在多个领域提升成功率。
- **原始摘要**: arXiv:2509.22480v2 Announce Type: replace Abstract: Large language models (LLMs) have been widely used for problem-solving tasks. Most recent work improves their performance through supervised fine-tu...

### 30. TeleTables: A Benchmark for Large Language Models in Telecom Table Interpretation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2601.04202
- **AI 摘要**: 本文介绍了TeleTables基准，包含来自3GPP规范的2220个表格和500个多选题，用于评估大型语言模型在电信表格理解上的表现，发现领域知识是闭卷设置的主要瓶颈，而提供表格后性能提升但受推理深度和结构复杂度影响。
- **原始摘要**: arXiv:2601.04202v2 Announce Type: replace Abstract: Large Language Models (LLMs) are increasingly applied to telecom engineering tasks, yet perform poorly on 3GPP specifications. These standards encod...

### 31. PROMPT2BOX:Improving LLM Weakness Discovery and Specificity Estimation by Uncovering Entailment Structure among Prompts
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.21438
- **AI 摘要**: 本文提出Prompt2Box方法，将提示嵌入到盒嵌入空间，以捕捉语义相似性和特异性关系，从而改进大型语言模型弱点的发现和特异性估计，并开发了盒嵌入的降维技术以支持数据集可视化。
- **原始摘要**: arXiv:2603.21438v3 Announce Type: replace Abstract: To discover the weaknesses of LLMs, researchers often embed prompts into a vector space and cluster them to extract insightful patterns. However, ve...

### 32. Unified Deployment-Aware Evaluation of Open Reasoning Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.07035
- **AI 摘要**: 本文对七个开放推理语言模型配置在四个基准上进行了统一部署感知评估，涵盖零样本、思维链和少样本提示，报告了准确率、延迟、显存、帕累托最优操作点等指标，发现Gemma-4-26B-A4B零样本提示得分最高。
- **原始摘要**: arXiv:2604.07035v3 Announce Type: replace Abstract: Open reasoning language models are often compared under mixed sample sizes, partially standardized prompts, and accuracy-centered summaries, which m...

### 33. KCSAT-ML: Probing Reasoning Models with Nationwide-Cohort Human Difficulty
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.10403
- **AI 摘要**: 本文提出KCSAT-ML数学推理基准，包含韩国高考十年试题及官方错误率，并引入难度对齐推理增益指标，揭示模型在人类难题上的表现模式及测试时扩展的影响。
- **原始摘要**: arXiv:2606.10403v3 Announce Type: replace Abstract: Math reasoning benchmarks have proliferated, yet most lack a per-item difficulty signal grounded in actual human performance. We introduce KCSAT-ML,...

### 34. CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.19667
- **AI 摘要**: 本文提出CacheWeaver，一种缓存感知的证据排序方法，通过前缀树和贪心遍历优化RAG推理中的前缀缓存复用，降低TTFT约20-33%，且不影响答案质量。
- **原始摘要**: arXiv:2606.19667v2 Announce Type: replace Abstract: Retrieval-Augmented Generation (RAG) improves factual grounding, but it also lengthens prompts and raises prefill cost. Prefix caching in serving en...

### 35. Estimating Uncertainty from Reasoning: A Large-Scale Study of Multi- and Crosslingual MCQA Performance in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.06327
- **AI 摘要**: 本文首次大规模评估22种语言下LLM的不确定性估计方法，发现用英语推理可显著提升低资源语言的表现，表明理解能力完好而生成环节是瓶颈。
- **原始摘要**: arXiv:2607.06327v3 Announce Type: replace Abstract: Uncertainty estimation (UE) enables LLM-powered systems to recognize when to abstain, yet existing research has predominantly focused on English. We...

### 36. Revisiting Lossy Verification in Speculative Decoding: Mechanisms, Trade-offs, and Failure Modes
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.26627
- **AI 摘要**: 本文对推测解码中的有损验证机制进行了原理性分析，将其统一为截断验证和协作验证两类，并构建诊断评估框架，揭示其可能导致的分布改变和生成质量下降问题。
- **原始摘要**: arXiv:2607.26627v2 Announce Type: replace Abstract: Speculative Decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose tokens that are subsequently v...

### 37. Search-G1: Grounded Search Agents via Representation-Based Intrinsic Rewards
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 24 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.07531
- **AI 摘要**: 提出Search-G1框架，通过基于表征的内在奖励衡量搜索代理的答案接地性，区分必要检索与冗余搜索，无需昂贵标注，提升检索增强语言代理的效率和准确性。
- **原始摘要**: arXiv:2608.07531v3 Announce Type: replace Abstract: Search-augmented language agents should retrieve external information only when necessary and ground their answers in retrieved evidence. Existing e...

### 38. When Linguistic and Internal Confidence Diverge in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 24 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28382
- **AI 摘要**: 研究大语言模型中语言表达的信心与内部信心的分歧，通过分类和生成任务分析关联性、幅度一致性和校准，发现两者经常不一致，指令调优和提示设计影响信心报告。
- **原始摘要**: arXiv:2608.28382v2 Announce Type: replace Abstract: Users often ask large language models (LLMs) to report how confident they are, but it is unclear whether such linguistic confidence tracks the model...

### 39. From Tokens to Semantics: Leveraging Complementary Signals for Hallucination Detection in Black-Box LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02679
- **AI 摘要**: 针对黑盒LLM的幻觉检测，结合语义熵和令牌不确定性等互补信号，提出TopK聚合方法和监督方法，提升检测准确性，减少漏报和误报。
- **原始摘要**: arXiv:2609.02679v2 Announce Type: replace Abstract: When LLMs support public-facing or high-stakes workflows, missed fabrications can harm users and institutions, while false alarms consume limited hu...

### 40. Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 24 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.23873
- **AI 摘要**: 本文提出语义覆盖（Semantic Overlays）技术，通过在冻结模型的残差流中应用小型学习适配器，为输入跨度提供非文本的带外注释通道，以缓解提示注入攻击。该方法不同于转向向量，可训练、可适应且选择性应用，能有效防止模型被恶意文本混淆。
- **原始摘要**: arXiv:2608.23873v3 Announce Type: replace-cross Abstract: Everything a language model sees is tokens. The serving stack knows what each span is -- user input, tool output, instructions -- but the mode...

### 41. What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04518
- **AI 摘要**: 本文研究多工具强化学习在编码智能体中的信用分配和可移植性。通过对比组内相对策略优化中同组和跨组两种规则，发现评估工具是影响求解率的主要变量，其影响远大于训练策略，揭示了评估工具在编码智能体RL中的关键作用。
- **原始摘要**: arXiv:2609.04518v1 Announce Type: new Abstract: Agent reinforcement learning (RL) increasingly runs through full execution harnesses, and a multi-harness recipe mixes two choices: exposing the policy...

### 42. GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05284
- **AI 摘要**: 提出基于图复杂度的GUT方法，量化并优化大语言模型推理不确定性，通过有向无环图覆盖推理分支，包含量化模块和优化模块，以减少LLM推理中的不确定性和错误分支。
- **原始摘要**: arXiv:2609.05284v1 Announce Type: new Abstract: Recent years have witnessed great advances in the reasoning ability of Large Language Models (LLMs). However, the reasoning processes of LLMs often exhi...

### 43. TreeFI: Value-Aware Statistical Fault Injection for Deep Neural Networks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04912
- **AI 摘要**: 本文提出TreeFI，一种价值感知的统计故障注入方法，用于评估深度神经网络在FP32单比特翻转下的可靠性。TreeFI利用回归树划分值分布区间，按区间相关性分配注入，在保持置信度的同时减少不必要的注入。
- **原始摘要**: arXiv:2609.04912v1 Announce Type: cross Abstract: Reliability evaluation of deep neural networks under hardware faults commonly relies on fault injection, but exhaustive campaigns are intractable for...

### 44. Amortizing Scaling Law Construction Costs
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05016
- **AI 摘要**: 本文提出高效构建缩放定律的框架，将数据收集形式化为贝叶斯优化问题，并引入比较指标。研究发现渐进扩展计算预算和代理幻想评估能显著提高恢复效率，减少训练成本。
- **原始摘要**: arXiv:2609.05016v1 Announce Type: cross Abstract: Scaling laws guide the design choices for training large foundation models, but deriving them involves training an exhaustive grid over hyperparameter...

### 45. Gradient-based Model Shortcut Detection for Time Series Classification
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2025年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2510.10075
- **AI 摘要**: 本文首次研究时间序列分类中深度神经网络的捷径学习行为，提出基于梯度的方法检测模型中的点级捷径。该方法不依赖外部属性，而是关注模型内部偏差，有助于理解泛化问题。
- **原始摘要**: arXiv:2510.10075v2 Announce Type: replace-cross Abstract: Deep learning models have attracted lots of research attention in time series classification (TSC) task in the past two decades. Recently, dee...

### 46. HLS-Seek: QoR-Aware Code Generation for High-Level Synthesis via Proxy Comparative Reward Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.13536
- **AI 摘要**: 本文提出HLS-Seek框架，用于高质量综合的QoR感知代码生成。该框架通过比较代理奖励模型避免全综合强化学习，实现99.53%的帕累托优势准确率，并采用不确定性感知的MC dropout切换防止奖励黑客，形成自改进奖励系统。
- **原始摘要**: arXiv:2605.13536v2 Announce Type: replace-cross Abstract: High-Level Synthesis (HLS) compiles algorithmic C/C++ descriptions into hardware, with Quality of Results (QoR)---latency and resource utiliza...

### 47. MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 24 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.23473
- **AI 摘要**: 提出MetaCaster元优化多智能体框架，通过智能体数据生成自动训练轻量级时间序列预测器，解决少样本学习问题。智能体作为中间工程师而非预测器，在18个数据集上验证有效性。
- **原始摘要**: arXiv:2608.23473v2 Announce Type: replace-cross Abstract: Time series forecasting (TSF) is evolving toward multimodal and agentic settings, yet using foundation models remains uneconomical in resource...

### 48. Learning-Augmented Algorithms: Guarantees, Construction Mechanisms, and System-Level Implications
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04787
- **AI 摘要**: 综述学习增强算法，综合预测接口、误差度量、一致性-鲁棒性权衡及五种构造机制，区分形式保证与系统实证，提出端到端推理的充分条件并列出开放问题。
- **原始摘要**: arXiv:2609.04787v1 Announce Type: new Abstract: Learning-augmented algorithms use fallible predictions while retaining formal performance guarantees. This survey synthesizes prediction interfaces, err...

### 49. Sustainable Edge Vision via Empirically Calibrated DVFS: Eliminating Thermal Throttling on Passively Cooled Hardware
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04705
- **AI 摘要**: 提出经验校准的状态感知DVFS调度器，消除无风扇边缘设备上DNN推理的热节流，在树莓派5上验证，帧率提升6.8%且能耗降低，优于温度反应式基线。
- **原始摘要**: arXiv:2609.04705v1 Announce Type: cross Abstract: Passive cooling eliminates the energy overhead and mechanical failure modes of fans, making it attractive for edge deployment, yet sustained Deep Neur...

### 50. Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04748
- **AI 摘要**: 研究发现前缀缓存会放大LLM服务中量化导致的输出分歧，在16位精度下36.2%轨迹改变，4位下达75%，禁用缓存则完全确定，揭示了缓存对可复现性的影响。
- **原始摘要**: arXiv:2609.04748v1 Announce Type: cross Abstract: Prefix caching, in which a serving engine reuses the key and value tensors of a shared prompt prefix across requests, is enabled by default in the maj...

### 51. Evaluating Uncertainty and Quality of Vision-Language-Action-enabled Robots
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2025年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2507.17049
- **AI 摘要**: 本文针对视觉-语言-动作机器人，提出八种不确定性和五种质量度量指标，并通过大规模实证研究评估其有效性，以弥补仅用任务成功率的评估不足。
- **原始摘要**: arXiv:2507.17049v4 Announce Type: replace-cross Abstract: Vision-Language-Action (VLA)-enabled robots integrate visual perception, natural language understanding, and action planning to interpret thei...

### 52. Budgeting Bytes: A Windowed Storage Roofline and Dual-Budget Architecture Ablations for Storage-Bound LLM Decoding
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04238
- **AI 摘要**: 本文提出窗口化存储屋顶线模型和双预算架构消融方法，用于分析存储受限的LLM自回归解码性能。通过地址确定性分类法优化预取调度，并在真实MoE部署中验证了模型预测的RAM溢出和带宽瓶颈问题。
- **原始摘要**: arXiv:2609.04238v1 Announce Type: new Abstract: Autoregressive decoding on cheap hardware is bound not by FLOPs but by the bytes each generated token must move across the slowest populated tier of a m...

### 53. MonoMoE: An Efficient Fused Mega-kernel for Quantized MoE Decoding
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04244
- **AI 摘要**: 本文提出MonoMoE，一种面向量化MoE解码的高效融合巨型内核。采用权重主序的持久化网格设计，消除专家局部token物化，减少填充计算，融合路由、top-k选择和量化等阶段，提升解码效率。
- **原始摘要**: arXiv:2609.04244v1 Announce Type: new Abstract: Mixture-of-Experts (MoE) layers increase model capacity without proportionally increasing arithmetic, but their sparse expert computation is difficult t...

### 54. Golden Ruler: A Numeric Format Catalog with Bit-Exact Conformance Vectors for FP8, BF16, MXFP4, and Microscaling Formats
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.09686
- **AI 摘要**: 本文提出数值格式目录，涵盖109种格式及位精确一致性测试包，支持FP8、BF16、MXFP4等，提供SHA-256指纹和标准映射，帮助工程师跨硬件诊断数值差异。
- **原始摘要**: arXiv:2606.09686v3 Announce Type: replace Abstract: Numeric format proliferation in machine learning hardware -- FP8 (E4M3 and E5M2), BF16, MXFP4, microscaling block formats, and dozens of research va...

### 55. Augur: Predicting View Serializability Violations in Relational Data Store Applications
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05288
- **AI 摘要**: 本文介绍Augur，首个支持复杂关系查询并仅报告违反视图可串行化执行的动态预测分析工具。它针对数据存储应用中的弱隔离导致的不可串行化执行，在OLTP-Bench和Spree等应用中成功发现可行的不可串行化执行。
- **原始摘要**: arXiv:2609.05288v1 Announce Type: new Abstract: Data stores are widely used because they provide persistence, scalability, and fault tolerance with a simple interface. However, most data store applica...

### 56. An Empirical Analysis of CodeQL False Positives and Query Refinements for Java Vulnerabilities
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04535
- **AI 摘要**: 本文对CodeQL在Java安全分析中的误报进行实证研究，分析了167个CVE实例，手动审查500个误报路径，构建了五类误报分类法。基于发现实现查询级优化，可移除81.8%的误报。
- **原始摘要**: arXiv:2609.04535v1 Announce Type: cross Abstract: Static application security testing (SAST) tools help developers find vulnerabilities before deployment, but false positives create substantial triage...

### 57. 2026-09-07共探训推融通新路径！壁仞科技 x 龙蜥社区 x PyTorch生态共建MeetUp圆满收官
- **来源**: Biren (壁仞科技) (TIER1)
- **发布日期**: 2026-09-08
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.birentech.com/news//news/z7mnt0q87wmvhpfshy0fumoi/
- **AI 摘要**: 壁仞科技与龙蜥社区、PyTorch生态联合举办MeetUp，探讨训练与推理融合的新路径，推动AI基础设施发展。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
