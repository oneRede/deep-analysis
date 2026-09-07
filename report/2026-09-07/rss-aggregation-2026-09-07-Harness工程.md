# RSS 聚合报告 - Harness工程

**生成时间**: 2026-09-08 07:11:32
**文章数量**: 50 篇

---

### 1. Measuring LLM performance drift: observations and methodology from 31,352 repeated benchmark measurements [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-09-07T07:44:34+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/
- **AI 摘要**: 该研究对LLM性能漂移进行了系统测量，基于31,352次重复基准测试，提出了观测结果和方法论。研究发现LLM在多次运行中性能存在波动，且不同模型和任务的表现漂移程度不同。作者提出了一套评估性能漂移的标准化方法，强调在基准测试中需考虑随机性和时间因素，为LLM的可靠评估和部署提供了重要参考。
- **原始摘要**: One thing that has bothered me about LLM benchmarks for a while is that most of them are essentially snapshots. A model is evaluated, a score is published, and we tend to talk about that score as if i...

### 2. How the AI ROI Gap Comes Down to Trust
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Mon, 07 Sep 2026 15:38:00 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.bloomberg.com/news/videos/2026-09-07/how-the-ai-roi-gap-comes-down-to-trust-video
- **AI 摘要**: SAS的新研究显示，投资于可信AI实践的企业更有可能获得可观的投资回报。然而，信任仍是主要障碍：97%的用户至少有时会覆盖AI建议，员工对日益自主的AI代理信任度较低。SAS首席信息官Jay Upchurch在彭博电视上讨论了这一AI投资回报率与信任之间的关键联系。
- **原始摘要**: Companies investing in trustworthy AI practices are far more likely to see strong returns from the technology, according to new research from SAS. But trust remains a hurdle: 97% of users override AI...

### 3. A Systematic Evaluation of Cross-Lingual Consistency Enhancement Methods in Multilingual Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04409
- **AI 摘要**: 本文对多语言模型跨语言一致性增强方法进行了统一评估，涵盖推理时干预和训练后方法。结果表明训练后方法更可靠，直接分布对齐始终提升一致性，而跨领域迁移有限。
- **原始摘要**: arXiv:2609.04409v1 Announce Type: new Abstract: Multilingual language models often produce inconsistent answers to semantically equivalent questions across languages, motivating methods to improve cro...

### 4. GRACE: Graph-Grounded Reflective Agent Copilot Engine for Expert-in-the-Loop Knowledge Expansion
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04442
- **AI 摘要**: GRACE是一个图接地反思智能体框架，将LLM响应分解为原子声明，并在加权二分图中与可信知识先验进行接地验证，分类为有根据、反驳或边界，并优化专家审查资源分配。
- **原始摘要**: arXiv:2609.04442v1 Announce Type: new Abstract: Large language models deployed in high-stakes settings frequently generate plausible but ungrounded claims. Standard retrieval-augmented generation (RAG...

### 5. Scale-QLoRA: Code-Invariant Adapter Merging for Native 4-bit Microscaling LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04526
- **AI 摘要**: 本文提出Scale-QLoRA方法，针对原生4位微缩格式的模型，仅适配每块缩放因子并在部署网格上训练，冻结E2M1代码，避免了传统LoRA合并时因量化导致的适配损失。
- **原始摘要**: arXiv:2609.04526v1 Announce Type: new Abstract: Merging a LoRA adapter into its base model is standard deployment practice: it removes the runtime adapter's per-forward overhead and leaves a single st...

### 6. ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04648
- **AI 摘要**: 本文提出ConsensusBench数据集，为强化学习提供基于规则的中间过程级奖励信号，通过聚类正确轨迹中的中间结论作为可验证子结果，以解决稀疏最终奖励在长推理任务中的不足。
- **原始摘要**: arXiv:2609.04648v1 Announce Type: new Abstract: Reinforcement learning (RL) has become one of the primary paradigms for reasoning enhancement of large language models (LLMs). In particular, Group Rela...

### 7. A Systematic Comparison of Multilingual Interpretability Methods Reveals Anisotropy-Driven Failures
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04819
- **AI 摘要**: 本文系统比较四种多语言可解释性指标，发现它们对跨语言共享的量化不一致，源于各向异性。仅ILO与跨语言迁移强相关（ρ=0.90），推荐使用ILO。
- **原始摘要**: arXiv:2609.04819v1 Announce Type: new Abstract: Multilingual language models develop shared cross-lingual representations, and various interpretability methods claim to quantify this sharing. These me...

### 8. Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04895
- **AI 摘要**: 本文提出缓存感知的联合路由器适配框架，用于内存高效的MoE推理，通过时间与空间路由器预测专家重用，减少权重传输，提升缓存命中率。
- **原始摘要**: arXiv:2609.04895v1 Announce Type: new Abstract: Mixture-of-Experts (MoE) models activate only a small subset of experts per token, but the full expert set often exceeds GPU memory, causing repeated we...

### 9. A Verifier-Guided Explainable Reasoning Framework with Gold-Anchored QLoRA, Task-Aware Mixture-of-Experts, and Group-Relative RLVR
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05221
- **AI 摘要**: 本文提出一个验证器引导的可解释推理框架，结合金锚定QLoRA、任务感知混合专家和组相对RLVR，用于教育问答，通过符号验证器提升推理的准确性和可解释性。
- **原始摘要**: arXiv:2609.05221v1 Announce Type: new Abstract: Large language models (LLMs) show strong reasoning ability, but their explanations can remain inconsistent, weakly grounded, or difficult to verify. We...

### 10. LexFlip: A Dissociation Diagnostic for Legal Meaning Preservation Metrics
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05296
- **AI 摘要**: 本文提出LexFlip诊断工具，用于评估法律文本简化后语义保持的度量标准，通过最小扰动改变法律效力，发现现有语义度量表现不佳，而简单长度特征反而更好。
- **原始摘要**: arXiv:2609.05296v1 Announce Type: new Abstract: Does a simplified legal clause still say what the original said? The checks in current use cannot establish that it does: requiring an identical pair to...

### 11. WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05405
- **AI 摘要**: 本文介绍WearableQA基准，包含4084个基于真实用户可穿戴数据的问题，用于评估AI系统对纵向健康数据的推理能力，涵盖数据推理和健康推理等多种问题类型。
- **原始摘要**: arXiv:2609.05405v1 Announce Type: new Abstract: Recent advances in wearable sensing enable continuous monitoring of physiological and behavioral signals, yet existing benchmarks rarely evaluate whethe...

### 12. Auditing Bias and Safety in Voice AI Customer Care
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04206
- **AI 摘要**: 本文提出一个验证门控审计框架，用于评估语音AI客服系统中的偏见和安全问题，考虑口音、情感等展示线索，并区分不同架构，记录服务负担路径。
- **原始摘要**: arXiv:2609.04206v1 Announce Type: cross Abstract: Voice AI systems increasingly mediate customer care interactions where caller presentation cues such as accent, affect, fluency, and urgency are avail...

### 13. EVOHARNESSBENCH: Can Your Agents Keep Pace with an Evolving Harness?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04280
- **AI 摘要**: 本文介绍EVOHARNESSBENCH基准，用于评估LLM代理在工具、技能和代理三个维度上不断演化的外部harness环境下的性能，包含17个多阶段流、802个任务等，并评估了部署和持续学习两种设置。
- **原始摘要**: arXiv:2609.04280v1 Announce Type: cross Abstract: Modern LLM-based agents operate through a harness of tools, reusable skills, and specialist agents that shapes what they observe and what they can do....

### 14. Harbor Adapters and Harbor-Index: Infrastructure and a Curated Meta-Dataset for Large-Scale Agentic Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04298
- **AI 摘要**: 本文提出Harbor Adapters统一评估基础设施，将80多个代理基准适配为可评估任意代理，并对8个模型在54个基准上进行大规模评估，同时引入Harbor-Index精选82个高质量任务，以支持大规模代理评估。
- **原始摘要**: arXiv:2609.04298v1 Announce Type: cross Abstract: Evaluating agents on the growing number of agentic benchmarks is challenging because they often require complex environments and agent integrations. W...

### 15. A Removal Based Approach to Improve LLM Faithfulness at Test-Time
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04343
- **AI 摘要**: 本文提出一种测试时方法，通过移除输入因素来直接针对LLM解释的不完整性，提高解释的忠实度，无需访问模型权重或大量计算资源，补充了现有主要解决不健全性的测试时方法。
- **原始摘要**: arXiv:2609.04343v1 Announce Type: cross Abstract: Large language models (LLMs) are increasingly used for consequential decisions, making their explanations an important tool for auditing model behavio...

### 16. Conformity Breaks Conformal Prediction
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04445
- **AI 摘要**: 本文揭示多代理LLM系统中，同伴一致错误答案会改变模型评分机制，导致共形预测失效，覆盖率从90%降至74%，攻击者可通过针对低置信度项使覆盖率降至47%，影响决策层。
- **原始摘要**: arXiv:2609.04445v1 Announce Type: cross Abstract: A conformal certificate can be valid when an LLM answers alone and invalid when the same LLM sees peers that unanimously assert a wrong answer. The qu...

### 17. Persistent Teacher Anchoring for Tool-Using Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04773
- **AI 摘要**: 本文提出持久教师锚定（PTA）方法，用于工具使用代理的蒸馏，通过块级验证和回合级承诺，让教师决定学生生成的文本和工具调用是否保留，减少师生分布差距，提升下游RL性能。
- **原始摘要**: arXiv:2609.04773v1 Announce Type: cross Abstract: Distillation is common in LLM post-training, where on-policy knowledge distillation (OPKD) uses student-generated trajectories to prepare the student...

### 18. BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04971
- **AI 摘要**: 大型推理模型在长链推理中KV缓存内存瓶颈严重，现有压缩方法假设近期查询可预测未来注意力，但研究发现存在重新关注早期上下文的思维回溯令牌。据此提出BeaconKV，一种免训练的KV缓存压缩方法，利用查询聚类特性实现高效压缩。
- **原始摘要**: arXiv:2609.04971v1 Announce Type: cross Abstract: Large Reasoning Models (LRMs) achieve superior problem-solving through extended Chain-of-Thought (CoT) generation, but the resulting key-value (KV) ca...

### 19. TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05079
- **AI 摘要**: 现有AI科学家基准聚焦复现，TruthInsightBench则面向发现，包含40个盲任务，仅暴露中性目标和冻结数据。固定LLM裁判从六个维度评估代理自身主张的证据成熟度，实现自动化确定性聚合，无需人工逐例评分。
- **原始摘要**: arXiv:2609.05079v1 Announce Type: cross Abstract: Autonomous coding agents are increasingly proposed as AI-scientist systems that conduct analyses and write research reports, but executing a prescribe...

### 20. Technical Manual for a Toolkit for Measuring Contextual Individuation in Transformer Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05333
- **AI 摘要**: 技术手册介绍测量Transformer语言模型上下文个体化的工具包，围绕桥形式概念：同一词在不同领域有不同含义。详细说明从规范声明、语料获取、表征提取到轮廓测量的完整流程，并论证每个设计选择。
- **原始摘要**: arXiv:2609.05333v1 Announce Type: cross Abstract: A transformer language model assigns a single, context-independent vector to a word type at its embedding layer, yet is widely believed to individuate...

### 21. Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05395
- **AI 摘要**: 开源模型在多步工具调用上表现不佳，文章提出KOPA-Bench基准和EDGE数据合成方法，通过执行验证构建工具调用图并合成可执行轨迹。微调后的9B模型接近未调优的27B模型，在KOPA-Bench和BFCL上均有显著提升。
- **原始摘要**: arXiv:2609.05395v1 Announce Type: cross Abstract: Data-sovereignty regulations increasingly require public institutions to deploy open-source, on-premise LLM agents that chain multiple tool-calls acro...

### 22. Harnessing the Reasoning Economy: A Survey of Efficient Reasoning for Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2503.24377
- **AI 摘要**: 本文综述了大语言模型在推理经济性方面的研究，探讨了System 1快速直觉与System 2深度推理之间的权衡，分析了推理效率低下的原因、不同推理模式的行为，并提出了在训练后和推理阶段优化推理成本与性能平衡的潜在解决方案。
- **原始摘要**: arXiv:2503.24377v2 Announce Type: replace Abstract: Recent advancements in Large Language Models (LLMs) have significantly enhanced their ability to perform complex reasoning tasks, transitioning from...

### 23. QoNext: Towards Next-generation QoE for Foundation Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.21889
- **AI 摘要**: 本文提出QoNext框架，将网络和多媒体中的体验质量原则应用于基础模型的整体评估，关注生成速度和延迟等动态服务属性，通过受控实验收集人类评分，构建数据库并训练神经预测器，以更全面地评估人机交互体验。
- **原始摘要**: arXiv:2509.21889v3 Announce Type: replace Abstract: Existing evaluations of foundation models predominantly focus on output correctness, treating interaction as a static exchange of information. Howev...

### 24. Exploring Solution Divergence and Its Effect on Large Language Model Problem Solving
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.22480
- **AI 摘要**: 本文研究了大语言模型在解决单一问题时生成解决方案的多样性，发现更高的解发散度与更好的问题解决能力正相关，并提出将解发散度作为新指标，可同时支持监督微调和强化学习策略，在多个问题领域显著提升成功率。
- **原始摘要**: arXiv:2509.22480v2 Announce Type: replace Abstract: Large language models (LLMs) have been widely used for problem-solving tasks. Most recent work improves their performance through supervised fine-tu...

### 25. TeleTables: A Benchmark for Large Language Models in Telecom Table Interpretation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2601.04202
- **AI 摘要**: 本文介绍TeleTables基准，包含来自13个3GPP规范的2220个表格和500个专家验证的多项选择题，用于评估大语言模型在电信表格理解上的能力。结果显示模型在闭卷场景下准确率低，但在提供表格时表现提升，且性能随推理深度和结构复杂度下降。
- **原始摘要**: arXiv:2601.04202v2 Announce Type: replace Abstract: Large Language Models (LLMs) are increasingly applied to telecom engineering tasks, yet perform poorly on 3GPP specifications. These standards encod...

### 26. PROMPT2BOX:Improving LLM Weakness Discovery and Specificity Estimation by Uncovering Entailment Structure among Prompts
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.21438
- **AI 摘要**: 本文提出Prompt2Box方法，将提示词嵌入到盒嵌入空间，以捕捉语义相似性和特异性关系，从而更精细地发现大语言模型的弱点。实验表明盒嵌入能有效区分不同难度的提示，并支持数据集可视化和比较。
- **原始摘要**: arXiv:2603.21438v3 Announce Type: replace Abstract: To discover the weaknesses of LLMs, researchers often embed prompts into a vector space and cluster them to extract insightful patterns. However, ve...

### 27. Unified Deployment-Aware Evaluation of Open Reasoning Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.07035
- **AI 摘要**: 本文对七个开放推理语言模型在四个基准上进行了统一部署感知评估，涵盖零样本、思维链和少样本思维链提示，报告准确率、置信区间、延迟、显存等指标，并识别帕累托最优操作点，为实际模型选择提供参考。
- **原始摘要**: arXiv:2604.07035v3 Announce Type: replace Abstract: Open reasoning language models are often compared under mixed sample sizes, partially standardized prompts, and accuracy-centered summaries, which m...

### 28. KCSAT-ML: Probing Reasoning Models with Nationwide-Cohort Human Difficulty
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.10403
- **AI 摘要**: 本文提出KCSAT-ML数学推理基准，包含韩国高考十年试题及官方错误率，并引入难度对齐推理增益指标，揭示模型错误分布与人类难度不一致的现象，以及测试时扩展对推理性能的非单调影响。
- **原始摘要**: arXiv:2606.10403v3 Announce Type: replace Abstract: Math reasoning benchmarks have proliferated, yet most lack a per-item difficulty signal grounded in actual human performance. We introduce KCSAT-ML,...

### 29. CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.19667
- **AI 摘要**: 本文提出CacheWeaver，一种缓存感知的证据排序方法，通过前缀树和贪心遍历优化RAG推理中的证据顺序，提高前缀缓存复用率，降低中位首令牌延迟约20-33%，且不损害答案质量。
- **原始摘要**: arXiv:2606.19667v2 Announce Type: replace Abstract: Retrieval-Augmented Generation (RAG) improves factual grounding, but it also lengthens prompts and raises prefill cost. Prefix caching in serving en...

### 30. Estimating Uncertainty from Reasoning: A Large-Scale Study of Multi- and Crosslingual MCQA Performance in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.06327
- **AI 摘要**: 本文首次大规模评估22种语言下LLM的不确定性估计方法，发现低资源语言中提示模型用英语推理可显著提升不确定性估计性能，表明理解能力完好而生成环节是可靠性瓶颈。
- **原始摘要**: arXiv:2607.06327v3 Announce Type: replace Abstract: Uncertainty estimation (UE) enables LLM-powered systems to recognize when to abstain, yet existing research has predominantly focused on English. We...

### 31. Revisiting Lossy Verification in Speculative Decoding: Mechanisms, Trade-offs, and Failure Modes
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.26627
- **AI 摘要**: 本文对推测解码中的有损验证机制进行了原理性分析，将多种方法统一为截断验证和协作验证两类，并构建诊断评估框架，揭示了截断方法在生成质量上的根本缺陷。
- **原始摘要**: arXiv:2607.26627v2 Announce Type: replace Abstract: Speculative Decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose tokens that are subsequently v...

### 32. Search-G1: Grounded Search Agents via Representation-Based Intrinsic Rewards
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 24 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.07531
- **AI 摘要**: 提出Search-G1框架，利用基于表征的内在奖励来训练搜索增强语言代理，通过干预校准的读出信号衡量证据接地性，区分必要检索与冗余搜索，提升检索效率和答案可靠性。
- **原始摘要**: arXiv:2608.07531v3 Announce Type: replace Abstract: Search-augmented language agents should retrieve external information only when necessary and ground their answers in retrieved evidence. Existing e...

### 33. When Linguistic and Internal Confidence Diverge in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 24 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.28382
- **AI 摘要**: 研究了LLM语言表达的信心与其内部置信度的一致性，发现两者在多个任务和模型上经常背离，指令微调虽提高报告信心但增大差距，提示设计会影响报告分布。
- **原始摘要**: arXiv:2608.28382v2 Announce Type: replace Abstract: Users often ask large language models (LLMs) to report how confident they are, but it is unclear whether such linguistic confidence tracks the model...

### 34. From Tokens to Semantics: Leveraging Complementary Signals for Hallucination Detection in Black-Box LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02679
- **AI 摘要**: 针对黑盒LLM的幻觉检测，结合语义熵和令牌不确定性两种互补信号，提出TopK聚合方法和监督门控方法，以平衡漏检与误报，提升检测可靠性。
- **原始摘要**: arXiv:2609.02679v2 Announce Type: replace Abstract: When LLMs support public-facing or high-stakes workflows, missed fabrications can harm users and institutions, while false alarms consume limited hu...

### 35. Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 24 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.23873
- **AI 摘要**: 本文提出语义覆盖（Semantic Overlays）技术，通过在冻结模型的残差流上应用小型学习适配器，为输入跨度提供非文本的带外注释通道，以缓解提示注入攻击。该方法比转向向量更灵活，可训练且选择性应用，增强了模型对跨度身份的识别能力。
- **原始摘要**: arXiv:2608.23873v3 Announce Type: replace-cross Abstract: Everything a language model sees is tokens. The serving stack knows what each span is -- user input, tool output, instructions -- but the mode...

### 36. What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04518
- **AI 摘要**: 本文研究多执行环境强化学习中的信用分配与可移植性，对比组内与跨组相对优势优化策略，发现评估环境对求解率影响远大于训练方法，跨组策略可提升泛化能力。
- **原始摘要**: arXiv:2609.04518v1 Announce Type: new Abstract: Agent reinforcement learning (RL) increasingly runs through full execution harnesses, and a multi-harness recipe mixes two choices: exposing the policy...

### 37. GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05284
- **AI 摘要**: 提出基于图复杂度的不确定性方法（GUT），用于量化和优化大语言模型推理中的不确定性。通过有向无环图覆盖推理链分支，构建量化模块和优化模块，以减少推理不确定性。
- **原始摘要**: arXiv:2609.05284v1 Announce Type: new Abstract: Recent years have witnessed great advances in the reasoning ability of Large Language Models (LLMs). However, the reasoning processes of LLMs often exhi...

### 38. TreeFI: Value-Aware Statistical Fault Injection for Deep Neural Networks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04912
- **AI 摘要**: 本文提出TreeFI，一种价值感知的统计故障注入方法，用于评估深度神经网络在FP32单比特翻转下的可靠性。通过回归树划分值分布区间并分层分配注入，在保持置信度和误差的同时减少不必要的注入，提高评估效率。
- **原始摘要**: arXiv:2609.04912v1 Announce Type: cross Abstract: Reliability evaluation of deep neural networks under hardware faults commonly relies on fault injection, but exhaustive campaigns are intractable for...

### 39. Amortizing Scaling Law Construction Costs
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05016
- **AI 摘要**: 本文提出一种高效构建缩放定律的框架，将数据收集视为贝叶斯优化问题，并引入比较指标。通过渐进扩展计算预算和代理幻想评估，显著提高恢复效率，减少训练大规模模型时的计算成本。
- **原始摘要**: arXiv:2609.05016v1 Announce Type: cross Abstract: Scaling laws guide the design choices for training large foundation models, but deriving them involves training an exhaustive grid over hyperparameter...

### 40. Gradient-based Model Shortcut Detection for Time Series Classification
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2025年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2510.10075
- **AI 摘要**: 本文首次研究了时间序列分类中深度神经网络的捷径学习行为，提出了基于梯度的模型捷径检测方法，以识别模型依赖的虚假相关性，提升泛化能力。
- **原始摘要**: arXiv:2510.10075v2 Announce Type: replace-cross Abstract: Deep learning models have attracted lots of research attention in time series classification (TSC) task in the past two decades. Recently, dee...

### 41. GLOW: Graph-Language Co-Encoding for Agentic Workflow Performance Prediction
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2512.15751
- **AI 摘要**: 本文提出GLOW框架，结合图神经网络和大型语言模型，用于智能体工作流性能预测，通过图结构建模和拓扑感知语义编码，避免昂贵的执行评估。
- **原始摘要**: arXiv:2512.15751v2 Announce Type: replace-cross Abstract: Agentic Workflows (AWs) have emerged as a promising paradigm for solving complex tasks. However, automatically generating high-quality AWs rem...

### 42. MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 24 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.23473
- **AI 摘要**: 本文提出MetaCaster，一种元优化多智能体框架，通过智能体数据生成实现轻量级时间序列预测器的少样本学习，在18个数据集上验证了其有效性。
- **原始摘要**: arXiv:2608.23473v2 Announce Type: replace-cross Abstract: Time series forecasting (TSF) is evolving toward multimodal and agentic settings, yet using foundation models remains uneconomical in resource...

### 43. Sustainable Edge Vision via Empirically Calibrated DVFS: Eliminating Thermal Throttling on Passively Cooled Hardware
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04705
- **AI 摘要**: 本文提出经验校准的状态感知DVFS调度器，用于被动散热边缘SoC上的DNN推理，通过时间域保护和绝对温度界限消除热节流，在树莓派5上实现更高帧率和更低能耗。
- **原始摘要**: arXiv:2609.04705v1 Announce Type: cross Abstract: Passive cooling eliminates the energy overhead and mechanical failure modes of fans, making it attractive for edge deployment, yet sustained Deep Neur...

### 44. Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04748
- **AI 摘要**: 本文研究LLM服务中前缀缓存对可复现性的影响，发现启用缓存会改变代理轨迹，且量化精度越低差异越大，16位时36.2%情节受影响，4位时达75%，禁用缓存则完全一致。
- **原始摘要**: arXiv:2609.04748v1 Announce Type: cross Abstract: Prefix caching, in which a serving engine reuses the key and value tensors of a shared prompt prefix across requests, is enabled by default in the maj...

### 45. Evaluating Uncertainty and Quality of Vision-Language-Action-enabled Robots
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2025年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2507.17049
- **AI 摘要**: 本文针对视觉-语言-动作机器人，提出八种不确定性度量和五种质量度量，通过大规模实证研究（908次成功执行）评估其有效性，以补充传统成功率评估的不足。
- **原始摘要**: arXiv:2507.17049v4 Announce Type: replace-cross Abstract: Vision-Language-Action (VLA)-enabled robots integrate visual perception, natural language understanding, and action planning to interpret thei...

### 46. Golden Ruler: A Numeric Format Catalog with Bit-Exact Conformance Vectors for FP8, BF16, MXFP4, and Microscaling Formats
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.09686
- **AI 摘要**: 本文介绍Golden Ruler数值格式目录，涵盖109种格式和6个位精确一致性测试包，提供FP8、BF16、MXFP4等格式的参考向量，用于跨硬件数值一致性验证。
- **原始摘要**: arXiv:2606.09686v3 Announce Type: replace Abstract: Numeric format proliferation in machine learning hardware -- FP8 (E4M3 and E5M2), BF16, MXFP4, microscaling block formats, and dozens of research va...

### 47. Corten - Foundational Verification of Rust Programs
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04372
- **AI 摘要**: Corten是一个在Rocq定理证明器中基于Iris分离逻辑构建的Rust程序基础验证框架。它首次在证明助手中为表面级Rust提供语义，将THIR嵌入Rocq并形式化动态语义，使验证目标接近源代码，便于维护。
- **原始摘要**: arXiv:2609.04372v1 Announce Type: new Abstract: We present Corten, a foundational verification framework for Rust programs in the Rocq theorem prover, built on the Iris separation logic framework. Cor...

### 48. Augur: Predicting View Serializability Violations in Relational Data Store Applications
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.05288
- **AI 摘要**: Augur是首个支持复杂关系查询并仅报告违反视图可串行化执行的动态预测分析工具。它处理SQL查询，在OLTP-Bench和电商应用Spree中发现可行的不可串行化执行，帮助数据存储应用避免弱隔离导致的错误。
- **原始摘要**: arXiv:2609.05288v1 Announce Type: new Abstract: Data stores are widely used because they provide persistence, scalability, and fault tolerance with a simple interface. However, most data store applica...

### 49. An Empirical Analysis of CodeQL False Positives and Query Refinements for Java Vulnerabilities
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04535
- **AI 摘要**: 本文分析CodeQL在Java安全分析中的误报，基于167个CVE实例和500个样本，建立源级分类法，识别五类误报模式。通过查询级优化过滤重复模式，移除81.8%的误报。
- **原始摘要**: arXiv:2609.04535v1 Announce Type: cross Abstract: Static application security testing (SAST) tools help developers find vulnerabilities before deployment, but false positives create substantial triage...

### 50. 2026-09-07共探训推融通新路径！壁仞科技 x 龙蜥社区 x PyTorch生态共建MeetUp圆满收官
- **来源**: Biren (壁仞科技) (TIER1)
- **发布日期**: 2026-09-08
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.birentech.com/news//news/z7mnt0q87wmvhpfshy0fumoi/
- **AI 摘要**: 壁仞科技联合龙蜥社区和PyTorch生态举办MeetUp，探讨训练与推理融合的新路径，推动AI软件生态与硬件协同发展。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
