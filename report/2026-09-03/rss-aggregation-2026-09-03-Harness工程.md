# RSS 聚合报告 - Harness工程

**生成时间**: 2026-09-04 15:59:22
**文章数量**: 73 篇

---

### 1. How many repeated LLM queries are enough? Testing a pilot-based reliability protocol [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-09-04T06:53:00+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w6wtw7/how_many_repeated_llm_queries_are_enough_testing/
- **AI 摘要**: 该文章讨论了在重复LLM查询中需要多少次才能获得可靠结果的问题，并提出了一种基于试点（pilot）的可靠性协议进行测试。研究关注LLM输出的稳定性和评估方法，属于AI工程实践中的评估和测试范畴。内容涉及如何设计实验来验证LLM可靠性，对实际应用有指导意义。
- **原始摘要**: I’m the author of a new preprint on repeated-query auditing of LLM brand recommendations, and the founder of Rankfor.AI. The practical question: how many times should we repeat a prompt before compari...

### 2. Nvidia PAIR utility joins every GPU in your home into a cluster for agentic AI tasks — tool uses spare cycles to keep agent swarms from hammering one GPU
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 03 Sep 2026 16:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pair-utility-joins-every-gpu-in-your-home-into-a-cluster-for-agentic-ai-tasks-tool-uses-spare-cycles-to-keep-agent-swarms-from-hammering-one-gpu
- **AI 摘要**: 英伟达推出PAIR工具，可将家庭中的多块GPU组成一个集群，用于处理代理型AI任务。该工具利用各GPU的空闲计算周期，避免单个GPU过载，从而提升整体效率。文章解释了PAIR的工作原理、其在分布式AI计算中的应用场景，以及如何通过资源调度优化多GPU环境下的任务执行。
- **原始摘要**: Nvidia's Personal AI Router (PAIR) clustering utility lets agentic AI workloads take advantage of every spare GPU cycle on a home network, potentially making for faster execution and more private infe...

### 3. Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Thu, 03 Sep 2026 00:00:00 GMT (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://huggingface.co/blog/grpo-with-trl-ifstruct
- **AI 摘要**: 本文介绍了一个完全公开且成本低廉的微调方法，通过GRPO算法和TRL库对LFM2.5-350M小模型进行微调，以提升其结构化输出能力。整个训练仅需约500个样本和100步，可在免费GPU上运行。在IFStruct基准上，模型性能从22.6%提升至29.7%。文章详细说明了训练数据、LoRA配置、奖励函数设计、模型合并保存等步骤，并对比了微调前后的评估结果，展示了任务特定微调能让小模型接近大模型的表现。

### 4. Intelligent Engineering: From Optimization To AI
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Thu, 03 Sep 2026 07:08:39 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/intelligent-engineering-from-optimization-to-ai/
- **AI 摘要**: 本文探讨了智能工程方法论，从传统优化向AI驱动转型。现代电子系统复杂性增长超过传统工程流程管理能力，高速接口、密集PCB布局、先进封装等技术迫使组织重新思考设计决策。文章提出基于优化、自动化和AI三大能力的智能工程方法：优化通过系统探索提升决策质量，自动化实现规模化执行，AI辅助解读结果和识别模式，将工程决策从经验猜测转变为数据驱动选择。
- **原始摘要**: A methodology for transforming engineering decisions from educated guesses into data-driven choices. The post Intelligent Engineering: From Optimization To AI appeared first on Semiconductor Engineeri...

### 5. AI Is Forcing Data Centers To Rethink Trust
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Thu, 03 Sep 2026 07:02:45 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/ai-is-forcing-data-centers-to-rethink-trust/
- **AI 摘要**: 本文探讨AI推动数据中心重新思考信任问题。AI驱动的容量需求使数据中心安全至关重要，物理与网络安全融合不能再是事后考虑。信任边界需扩展至整个供应链，需要新的防御协作体系。数据中心组件的新安全标准正在推动设计，但也可能造成瓶颈。开发者正设计零信任系统，持续验证芯片身份、固件完整性和后量子就绪性等。
- **原始摘要**: Exploding compute demand is exposing new gaps across the hardware supply chain, from chip identity and firmware integrity to post-quantum readiness. The post AI Is Forcing Data Centers To Rethink Trus...

### 6. How Many Design Experiments Does A Machine Learning Predictor Actually Need?
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Thu, 03 Sep 2026 07:02:30 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/how-many-design-experiments-does-a-machine-learning-predictor-actually-need/
- **AI 摘要**: 本文研究机器学习预测器在CAE中所需的设计实验数量。通过四个碰撞研究案例，发现所需数据集大小和预测精度与响应平滑度相关，而非模型规模或设计变量数量。例如，简单的两板厚参数化需要比25次乘员安全研究多四倍的实验。不连续响应（如电池损坏计数）比连续响应（如质量）更难预测，为ML工作流中的实验规划提供指导。
- **原始摘要**: Required dataset size and achievable accuracy track how smooth the response is, not model size or number of design variables. The post How Many Design Experiments Does A Machine Learning Predictor Act...

### 7. VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03153
- **AI 摘要**: 提出VeriPhy，一个可审计的物理验证系统，通过文本规划器将提示编译为类型化物理义务和静态验证执行计划，利用冻结专家模型进行证据收集，对世界模型生成的视频进行物理可靠性评估与改进。
- **原始摘要**: arXiv:2609.03153v1 Announce Type: new Abstract: Visual fluency in generated video does not imply physical reliability, and a scalar quality score alone is incapable of indicating the obligation a clip...

### 8. MedQA-MM: Shortcuts Behind Medical Visual Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03261
- **AI 摘要**: 研究医学多模态选择题中模型可能利用捷径而非真实视觉推理的问题，提出推理膨胀概念，通过多数据集审计和消融实验揭示模型依赖文本、选项等非视觉线索，呼吁关注推理路径而非仅最终分数。
- **原始摘要**: arXiv:2609.03261v1 Announce Type: new Abstract: A benchmark score credits final answers, but not the route by which an item can be answered. In medical multimodal multiple-choice questions (MCQs), thi...

### 9. When Do Frozen VLMs Respond to Image-Free Object-Token Edits? An Answer-Key-Free Protocol and What It Reveals
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03429
- **AI 摘要**: 研究冻结视觉语言模型对图像级对象令牌编辑的响应机制，提出无答案键的评估协议，揭示响应受显式编辑教学、令牌清洁度和密度影响，为表示级场景编辑提供新见解。
- **原始摘要**: arXiv:2609.03429v1 Announce Type: new Abstract: Answering what-if queries about a scene with a VLM usually means injecting the assumption as text or repainting the scene with a generative model. We in...

### 10. VKnowU: Evaluating Visual Knowledge Understanding in Multimodal LLMs
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2511.20272
- **AI 摘要**: 本文介绍VKnowU基准，用于评估多模态大语言模型的视觉知识理解能力，涵盖8类世界中心与人类中心知识。评估28个模型发现其与人类表现有差距，并引入VKnowQA数据集和VideoKnow+基线模型以弥补这一差距。
- **原始摘要**: arXiv:2511.20272v3 Announce Type: replace Abstract: While Multimodal Large Language Models (MLLMs) have become adept at recognizing objects, they often lack the intuitive, human-like understanding of...

### 11. Invoice Haystack: Benchmarking Document Retrieval and Visual Question Answering Under Strong Visual Homogeneity
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.25343
- **AI 摘要**: 本文提出Invoice Haystack基准，用于测试视觉语言模型在视觉高度同质文档集合中的检索能力。该基准包含1500张发票图像和200个问答对，平均余弦相似度0.73，比现有基准更具挑战性，旨在解决嵌入崩溃问题。
- **原始摘要**: arXiv:2606.25343v3 Announce Type: replace Abstract: Vision Language Models have achieved near-human performance on single-document Visual Question Answering, yet their effectiveness degrades significa...

### 12. Where Does Harness-Optimization Value Live? Localized Gains and the Budget-Splitting Trap in Self-Evolving LLM Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02889
- **AI 摘要**: 本文提出HARNESSEVO框架，将LLM代理的提示词脚手架分解为角色、策略、格式规则和反思控制四个可进化槽位，并研究优化价值分布。在ALFWorld基准上，分解优化未显著提升整体成功率，但槽位级分析揭示了局部增益与预算分配陷阱。
- **原始摘要**: arXiv:2609.02889v1 Announce Type: new Abstract: A growing body of work improves frozen large language models (LLMs) as agents by evolving their harness: the textual scaffolding around the model, inclu...

### 13. Contamination Inflates Scores but Rarely Reorders Large Language Model Leaderboards
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02899
- **AI 摘要**: 本文研究基准污染对LLM排行榜的影响，区分污染是否膨胀绝对分数与是否改变模型排名。通过对比原始与改写题目的表现差异，发现污染虽提升分数但很少改变排名顺序。
- **原始摘要**: arXiv:2609.02899v1 Announce Type: new Abstract: Benchmark contamination, the leakage of test items into training data, is widely described as a threat to the reliability of large language model (LLM)...

### 14. Judging LLM-as-a-Judge: Concerning Rubric Artifacts in LLM-based Automated Text Generation Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02942
- **AI 摘要**: 本文研究LLM作为评判者的可靠性，发现仅基于评分标准文本训练的分类器能预测评判输出，表明评分标准编码了可恢复的评估信号。反事实扰动显示评判者常无法可靠更新决策，引发对基于评分标准的LLM评估的担忧。
- **原始摘要**: arXiv:2609.02942v1 Announce Type: new Abstract: LLM-as-a-Judge pipelines are increasingly used to evaluate AI-generated text, based on the assumption that judgments arise from reasoning over candidate...

### 15. Unifying Conformal Language Tasks with In-Context Ensembles
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03005
- **AI 摘要**: 本文提出Conformal Relevance框架，利用上下文学习示例策展和集成创建评分函数，在保持覆盖率的同时提高简洁性，减少人工提示工程，应用于七个NLP任务并理论分析多样性影响。
- **原始摘要**: arXiv:2609.03005v1 Announce Type: new Abstract: Many NLP tasks, such as summarization and extractive question answering, reduce to retrieving relevant content from documents under two constraints: cov...

### 16. SHELF: A Synthetic Harness for Multi-Task Bibliographic Benchmarking
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03047
- **AI 摘要**: SHELF是一个用于多任务书目基准测试的合成工具，通过生成受控基准数据和评估任务，系统测试图书馆和档案管理中的分类、聚类、检索等任务，并比较不同方法的表现。
- **原始摘要**: arXiv:2609.03047v1 Announce Type: new Abstract: Libraries and archives manage large collections with limited staff and computing budgets, yet common benchmarks do not systematically test their bibliog...

### 17. Counterfactual Fairness Audits of Multi-Step Clinical LLM Agents Require a Measured Per-Action Instability Floor
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03221
- **AI 摘要**: 本文指出临床LLM代理的反事实公平审计中翻转率不可单独解释，需考虑每次动作的不稳定性下限，多数投票可减少39%的不稳定性，并建议采用测量下限进行审计。
- **原始摘要**: arXiv:2609.03221v1 Announce Type: new Abstract: Counterfactual audits are the standard tool for checking whether a clinical agent treats demographically distinct but clinically identical patients diff...

### 18. What Else Needs Fixing? Exploring Cost-Effective Test-Time Compute for Revision Propagation in Artifacts Generated Through Conversation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03254
- **AI 摘要**: 本文研究LLM在对话生成工件中传播修订的能力，引入新基准并评估九种修订方法，发现基线准确率68.3-93%，最经济的方法是选择性并行采样。
- **原始摘要**: arXiv:2609.03254v1 Announce Type: new Abstract: Large Language Models (LLMs) often help users generate artifacts through iterative cycles of generation and revision in conversation. A challenge here i...

### 19. How Perturbations Propagate: A Multi-Level Analysis of Robustness in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03322
- **AI 摘要**: 研究六种输入扰动在解码器语言模型中的传播，从输出行为、隐藏状态几何和注意力头功能三个层面分析，发现扰动类型产生可区分的度量轮廓。
- **原始摘要**: arXiv:2609.03322v1 Announce Type: new Abstract: Language models encounter typos, corrupted text, altered words, and disrupted token order, yet robustness is usually evaluated only through output behav...

### 20. FPCO-Dialog: A Multi-Turn False-Premise Benchmark for Correction and Cooperation in Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03331
- **AI 摘要**: 介绍FPCO-Dialog基准，用于评估视觉语言模型在重复错误前提下的纠正与合作行为，包含1080张图像和10800个问题轮次。
- **原始摘要**: arXiv:2609.03331v1 Announce Type: new Abstract: Vision-language models (VLMs) are increasingly deployed in multi-turn settings where users may describe visual content with incorrect assumptions. Yet e...

### 21. FrameBench:A Language Understanding Benchmark Based on Frame Semantics
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03370
- **AI 摘要**: 提出FrameBench基准，基于框架语义学，测试模型是否区分同一动词在不同语境中唤起的框架，涵盖英语和日语。
- **原始摘要**: arXiv:2609.03370v1 Announce Type: new Abstract: In frame semantics, sentence comprehension is assumed to proceed by relating lexical meaning to background knowledge called semantic frames, thereby ena...

### 22. Chiaroscuro for Emotions: A Contrastive Emotion Benchmark Grounded in Appraisal Theory
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03394
- **AI 摘要**: 介绍CHIARO基准，包含1000条人工标注句子，用于对比情绪推断，基于评价理论，测试模型对同一事件引发不同情绪的理解。
- **原始摘要**: arXiv:2609.03394v1 Announce Type: new Abstract: Emotion recognition benchmarks often predict one emotion per text, missing many real-world scenarios where two people arrive at opposing emotions from a...

### 23. To What Extent Do Large Language Models Understand Bangla Idioms?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03410
- **AI 摘要**: 构建孟加拉语习语基准数据集，评估LLM在释义、习语跨度检测和意义识别任务上的表现，发现不同模型各有优势。
- **原始摘要**: arXiv:2609.03410v1 Announce Type: new Abstract: Idiomatic expressions are an integral part of natural language, reflecting cultural nuances and posing unique challenges for computational models, parti...

### 24. Decoupled Analysis-Judging: An Automated Creativity Evaluator Using LLMs in Complex Multi-step Creativity Tasks
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03432
- **AI 摘要**: 本文提出CreaEval，一种用于复杂多步创造力任务的自动化评估器，将LLM评判解耦为分析和判断两阶段，通过记忆增强分析和基于证据的判断减少偏差，提高评估可靠性。
- **原始摘要**: arXiv:2609.03432v1 Announce Type: new Abstract: Automated evaluation of creativity tasks remains challenging for LLM-as-a-Judge, as LLM is susceptible to biases such as verbosity bias and leniency bia...

### 25. When Users Don't Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03467
- **AI 摘要**: 本文提出LOCOMO-CONV对话记忆基准，评估五种记忆系统在四种查询风格下的检索和响应质量，发现对话框架暴露了QA基准忽视的检索差距，且强检索不完全转化为响应质量。
- **原始摘要**: arXiv:2609.03467v1 Announce Type: new Abstract: Large language models (LLMs) are increas- ingly deployed as long-horizon conversational agents, motivating growing interest in mem- ory systems. However...

### 26. Beyond BLEU: A Case for Redefining Sign Language Translation Benchmarks
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03734
- **AI 摘要**: 本文指出BLEU-4指标不足以评估手语翻译质量，因其允许模型利用口语先验而非真正理解手语。作者提出基于开放权重LLM问答协议的新评估方法，更贴近人类排序且对释义更具鲁棒性，能更好地衡量内容保留。
- **原始摘要**: arXiv:2609.03734v1 Announce Type: new Abstract: BLEU-4 is the standard metric for evaluating sign language translation (SLT), but spoken-language metrics may not adequately reflect sign language profi...

### 27. IndicSafeEval: Safety Robustness of Large Language Models under Multilingual Persuasive Jailbreak Attacks
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03781
- **AI 摘要**: 本文提出IndicSafeEval，一个针对印度语言的多语言说服式越狱攻击评估框架，涵盖四种语言、十类风险内容和六种说服策略，共7200个对抗提示。黑盒评估显示LLM安全行为因语言和提示风格而异，并非均衡安全。
- **原始摘要**: arXiv:2609.03781v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used in multilingual settings, yet their safety is still evaluated primarily in English. This limits our u...

### 28. Evaluating Criterion-Conditioned Behaviour of Large Language Models in Content Moderation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03814
- **AI 摘要**: 本文引入DECO基准，用于诊断性评估LLM在内容审核中是否具备条件化行为。发现模型在标准基准上表现良好，但在特定审核标准层面存在显著失败，尤其当正确决策取决于内容的具体方面而非整体有害性时。
- **原始摘要**: arXiv:2609.03814v1 Announce Type: new Abstract: Large language models (LLMs) demonstrate strong performance on standard content moderation benchmarks. However, these benchmarks often aggregate multipl...

### 29. Beyond Majority Vote: Multi-Perspective Adjudication for Medical Hallucination Detection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03953
- **AI 摘要**: 本文开发多视角标注研究检测医学聊天机器人回复中的事实错误，结合首轮标注、LLM法官候选发现和两种裁决方式。发现首轮标注常遗漏错误，LLM法官单独不足，多源裁决可提高基准完整性。
- **原始摘要**: arXiv:2609.03953v1 Announce Type: new Abstract: Understanding the frequency of factual errors in chatbot-generated text and evaluating systems that detect these errors is critical for determining chat...

### 30. Two-Stage Reinforcement Learning for Sound and Adversarial Test Generation in Code LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03955
- **AI 摘要**: 本文提出TCS，一个两阶段强化学习框架用于自动生成测试用例。第一阶段生成与参考解一致的测试，第二阶段聚焦当前失败模式学习反例测试。在TACO和LiveCodeBench上，TCS提升了pass@1和推理能力。
- **原始摘要**: arXiv:2609.03955v1 Announce Type: new Abstract: Reinforcement learning (RL) has substantially advanced code generation with large language models (LLMs) through executable feedback. The feedback for c...

### 31. Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04194
- **AI 摘要**: 本文质疑思维链推理痕迹的可解释性，提出用优势（advantage）衡量推理步骤的重要性，并通过蒙特卡洛模拟估计。实验发现LLM法官识别高优势步骤的能力有限，远未达到噪声上限，表明文本可读性不等于功能可解释性。
- **原始摘要**: arXiv:2609.04194v1 Announce Type: new Abstract: Reasoning traces from chain-of-thought models appear to offer a legible window into how a model arrives at its answer. A growing body of work treats the...

### 32. ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04197
- **AI 摘要**: 本文提出ESPO（错误结构化提示优化）方法，通过诊断、多样化和稳定化三阶段解决进化提示优化器的提示膨胀问题。在七个NLP基准上，ESPO平均准确率提升3.76个百分点，提示长度缩短47%，推理速度更快。
- **原始摘要**: arXiv:2609.04197v1 Announce Type: new Abstract: Evolutionary prompt optimizers such as GEPA suffer from prompt bloat: each iteration appends rules and caveats, producing prompts up to 3$\times$ longer...

### 33. It's the Problem, Not the Path: Budget and Difficulty Confounds in LLM Reasoning Trajectories
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03436
- **AI 摘要**: 本文通过重启控制的截断探针研究LLM推理轨迹，区分前缀价值与计算预算效应。在178个问题-模型组合中仅1个为前缀受限，重启剂量反应可区分计算受限与能力受限模型，且当预算匹配时继续自身前缀优于重启。
- **原始摘要**: arXiv:2609.03436v1 Announce Type: cross Abstract: Reasoning traces of large language models are widely read as containing "breakthrough" moments and early-legible fates. Both readings rest on measurem...

### 34. HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03580
- **AI 摘要**: 本文提出HalluPeer基准，用于检测科学同行评审中的幻觉。提供论文内容、人类评审和注入幻觉的评审三元组，并标注检测、分类和定位。在12K论文和38K评审上的实验表明现有检测器难以区分幻觉与合理批评。
- **原始摘要**: arXiv:2609.03580v1 Announce Type: cross Abstract: The growing scale of academic peer review has motivated the use of Large Language Models (LLMs) as review assistants, yet LLMs can generate fluent but...

### 35. Select, Compress, Reinvest: A Controlled Study of Visual-Token Allocation in Long-Video MLLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03820
- **AI 摘要**: 本文系统研究长视频多模态大模型中视觉令牌分配策略，通过控制变量实验发现帧选择是最大性能杠杆，查询选择的8帧优于均匀采样的16帧，经典稀疏近似算法OMP表现与专用选择器相当。
- **原始摘要**: arXiv:2609.03820v1 Announce Type: cross Abstract: Long-video language models cannot look at every frame: an hour sampled once per second is 3,600 images, and a system keeps only a small fixed slice of...

### 36. VestigeKV: The NoPE-MLA KV Cache Carries Its Own Eviction Signal in a Vestigial Branch
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03949
- **AI 摘要**: 本文提出VestigeKV方法，利用NoPE MLA模型中解耦分支的残留信号进行KV缓存驱逐，无需训练或量化。在Kimi Linear上实现8倍压缩下检索保持1.00，32倍下0.92，且无性能损失。
- **原始摘要**: arXiv:2609.03949v1 Announce Type: cross Abstract: The problem. A long-lived KV cache must be compressed before the queries that will read it exist; selection by observed attention (H2O, SnapKV) collap...

### 37. The Dice Roll Method: A Standardized Protocol for Repeated-Query Auditing of Large Language Model Brand Recommendations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04047
- **AI 摘要**: 本文形式化骰子滚动方法，作为重复查询审计LLM品牌推荐的标准化协议，包括迭代次数设置、稳定性指标和可靠性阈值，并分解总方差为采样、提示措辞等成分。
- **原始摘要**: arXiv:2609.04047v1 Announce Type: cross Abstract: Background: Researchers increasingly use repeated identical prompts to audit stochastic variation in large language model (LLM) brand recommendations,...

### 38. When Models Edit Too Much: On the Fidelity of Minimal Code Edits
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04061
- **AI 摘要**: 研究大语言模型在代码编辑中的过度编辑问题，构建了基于BigCodeBench的评估框架，发现即使GPT-5.5等强模型也存在过度编辑。通过保留指令可显著减少不必要的编辑，降低认知复杂度并提升修复准确率。
- **原始摘要**: arXiv:2609.04061v1 Announce Type: cross Abstract: Large language models (LLMs) are increasingly used to edit existing code, but correctness alone is not enough: useful repairs should also be minimal,...

### 39. EasySteer: A Unified Framework for High-Performance and Extensible LLM Steering
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.25175
- **AI 摘要**: 提出EasySteer，一个基于vLLM的高性能可扩展大语言模型引导统一框架。采用模块化架构，支持分析和学习方法，提供预计算引导向量和交互演示系统，相比现有框架实现10.8-22.3倍加速。
- **原始摘要**: arXiv:2509.25175v3 Announce Type: replace Abstract: Large language model (LLM) steering has emerged as a promising paradigm for controlling model behavior at inference time through targeted manipulati...

### 40. SuperValid: Capability-Aligned OOD Validation for Generalizable Downstream Scaling
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.28179
- **AI 摘要**: 本文提出SuperValid框架，通过合成能力对齐的分布外验证数据来预测下游任务性能。该框架在能力层面研究缩放规律，避免基准特定噪声和分布内验证损失的限制，在16个基准测试中表现优异。
- **原始摘要**: arXiv:2605.28179v2 Announce Type: replace Abstract: Scaling laws guide large language model training by relating compute to cross-entropy loss, and recent work further extends them to predict downstre...

### 41. Fixing FOLIO and MALLS: Verified Annotations and an LLM-assisted Framework to Focus Human Relabeling
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.02837
- **AI 摘要**: 本文系统审计了FOLIO和MALLS数据集，发现约42%的条目存在错误的一阶逻辑形式化。作者开发并发布了修正后的标注，并提出了一个LLM辅助框架以聚焦人工重新标注，提高数据集质量。
- **原始摘要**: arXiv:2606.02837v2 Announce Type: replace Abstract: Accurate translation from Natural Language to First-Order Logic (NL-to-FOL) underpins neurosymbolic AI systems and Natural Language Inference (NLI),...

### 42. EDIT: Evidence-Diagnosed Intervention Training for Rule-Faithful LLM Grading
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.06350
- **AI 摘要**: 本文提出EDIT框架，用于训练更符合评分标准的LLM评分器。该框架通过内部信号定位推理错误步骤并修正，同时使用信念引导的奖励塑造来校准评分器，提高评分与评分标准的一致性。
- **原始摘要**: arXiv:2606.06350v2 Announce Type: replace Abstract: Reliable rubric grading requires more than accurate score prediction. Each judgement must be grounded in the mark scheme and evidence from the stude...

### 43. SV-Detect: AI-generated Text Detection with Steering Vectors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.07313
- **AI 摘要**: 本文提出SV-Detect，一种基于冻结语言模型隐藏表示中提取的引导向量的AI生成文本检测器。该方法在分布内和分布偏移下均表现优异，包括跨域、跨模型和编辑攻击场景，并具有可解释性。
- **原始摘要**: arXiv:2606.07313v2 Announce Type: replace Abstract: Detecting AI-generated text is especially difficult under distribution shift, such as transfer across domains, source models, and editing attacks. W...

### 44. Uncertainty Is Not a Safety Net for Clinical VQA, but Can It Anticipate Model Failure?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.16583
- **AI 摘要**: 本文评估了临床视觉语言模型中不确定性估计方法的可靠性。发现UE质量随模型精度变化，在模型最弱处失效；在NOTA扰动下，模型准确率崩溃但不确定性变化不大，然而未扰动输入的不确定性可预测模型在NOTA下的失败。
- **原始摘要**: arXiv:2606.16583v2 Announce Type: replace Abstract: Safe deployment of clinical vision-language models (VLMs) requires reliable uncertainty estimation (UE): a signal indicating when predictions should...

### 45. Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.20954
- **AI 摘要**: 提出LRE方法，一种轻量级、CPU-only的评分器，通过学习识别任务关键历史信息并逐字保留，解决长时运行语言模型上下文溢出时的信息遗忘问题，在准确性和成本上优于现有基线。
- **原始摘要**: arXiv:2606.20954v2 Announce Type: replace Abstract: Long-running language-model systems accumulate interaction history that outgrows the context window, so they must continually evict. When an evictio...

### 46. TRACE: A Self-Evolving Skill Bank for Consistent, Limit-Aware LLM Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 20 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.22793
- **AI 摘要**: 提出TRACE方法，通过轨迹对比进化构建自进化技能库，提升LLM智能体在车载助手等场景中的一致性和限制感知能力，弥合单次成功与多次一致成功之间的差距。
- **原始摘要**: arXiv:2608.22793v2 Announce Type: replace Abstract: Reliable deployment of LLM agents in user-facing products depends not on raw task-solving ability but on consistency and limit-awareness: behaving t...

### 47. JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 20 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.25593
- **AI 摘要**: 提出JIT-Agent，一种即时进化智能体框架，训练模型自动生成和修复任务适配的智能体外部框架，提升任意LLM的推理能力，超越更强模型。
- **原始摘要**: arXiv:2608.25593v2 Announce Type: replace Abstract: Agent capability is not determined by the model alone. The agent harness, encompassing memory management, planning strategy, action protocol, and to...

### 48. MIRA: A Bilingual Benchmark for Medical Information Response Audit
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.28025
- **AI 摘要**: 本文提出MIRA，一个双语医学信息响应审计基准，评估大语言模型在不同用户表述下是否提供可比的医学信息。发现模型对低健康素养用户存在信息稀释现象，并提出知识引导的缓解方法。
- **原始摘要**: arXiv:2605.28025v2 Announce Type: replace-cross Abstract: Existing safety evaluations for large language models overlook whether responses preserve comparable medical information across different user...

### 49. Attend to Evidence: Evidence-Anchored Spatial Attention Supervision for Multimodal RLVR
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.30912
- **AI 摘要**: 本文提出EASE方法，为多模态强化学习提供基于证据的空间注意力监督。通过将标注证据区域转化为平滑视觉令牌目标，引导模型关注相关视觉证据，提升视觉问答的可靠性和准确性。
- **原始摘要**: arXiv:2605.30912v2 Announce Type: replace-cross Abstract: Reinforcement learning with verifiable rewards (RLVR) improves vision-language models (VLMs) by optimizing outcome rewards derived from final...

### 50. LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.18388
- **AI 摘要**: 本文提出LLMZero，一种基于LLM代理的智能体系统，通过树搜索诊断训练病理并协调参数调整，自动发现自适应RL后训练策略。在多个GRPO任务上显著优于基线和网格搜索，揭示容量与正则化参数的不同动态模式。
- **原始摘要**: arXiv:2606.18388v2 Announce Type: replace-cross Abstract: RL post-training strategies are dataset-dependent and reveal a recurring empirical pattern: capacity parameters accumulate monotonically acros...

### 51. Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.31002
- **AI 摘要**: 该研究探讨了自然语言到Lean语句形式化的忠实性评估问题，提出结合Lean编译与GPT-5.2和Gemini-2.5-Pro语义共识的严格标准。研究发现所有系统都存在编译-忠实度差距，范围从3.0到29.0个百分点，表明编译成功并不代表语义忠实。
- **原始摘要**: arXiv:2606.31002v2 Announce Type: replace-cross Abstract: Lean verifies that a generated declaration is well typed, but not that it expresses the statement a user intended. We study two questions for...

### 52. K-Bench: measuring model performance on real scientific agent requests
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 20 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.21601
- **AI 摘要**: 该论文介绍K-Bench 01评估基准，基于真实科学用户请求构建，由九个前沿模型在相同沙箱中端到端运行，共完成1602次代理运行。三位盲审语言模型法官按八维评分标准评估，结果显示没有模型能达到领域科学家可接受的水平，gpt-5.6-sol得分最高但存在不确定性。
- **原始摘要**: arXiv:2608.21601v2 Announce Type: replace-cross Abstract: Benchmarks for scientific artificial intelligence are mostly written to be scored: multiple-choice questions, curated agent tasks with referen...

### 53. SVG-Score: Human-Aligned Evaluation of Text-to-SVG Generation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03806
- **AI 摘要**: 本文提出SVG-Score，一种面向文本生成SVG任务的人类对齐评估框架。研究发现CLIPScore对SVG生成错误不敏感，VLM评估器响应不均。作者构建了语义对齐的人工标注数据集，用于更准确地衡量生成SVG的语义保真度。
- **原始摘要**: arXiv:2609.03806v1 Announce Type: new Abstract: Scalable Vector Graphics (SVG) generation is attracting increasing attention as generative models improve in expressiveness and controllability. Progres...

### 54. Spurious Advantage Hidden in GRPO
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04063
- **AI 摘要**: 本文识别GRPO算法中因猜测得到正确答案而获得高优势分数的虚假优势问题，出现在有界答案任务等场景。提出SIGNBALANCE方法，通过保留验证器符号、使用全局尺度及逐类停止梯度重缩放来消除该偏差。
- **原始摘要**: arXiv:2609.04063v1 Announce Type: new Abstract: Group Relative Policy Optimization (GRPO) is widely studied for reinforcement learning with verifiable rewards, where its advantage estimator assigns ea...

### 55. DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04094
- **AI 摘要**: 本文提出DRACO方法，用于长时程智能体训练中的细粒度信用分配。该方法在训练中动态生成多准则评分标准，对完整轨迹评分后将判断重新分配到各步骤，生成差异化优势信号，无需训练归因模块，在AppWorld上显著提升性能。
- **原始摘要**: arXiv:2609.04094v1 Announce Type: new Abstract: Reinforcement Learning from Verifiable Rewards works well when a task has a programmatic checker, but most long-horizon agent domains have none. We work...

### 56. Subspace Inference Enables Efficient Active Reward Learning from Preferences
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04066
- **AI 摘要**: 提出PreferenceEKF方法，通过子空间推断和扩展卡尔曼滤波实现高效的主动偏好学习，用于RLHF中的奖励模型不确定性量化。
- **原始摘要**: arXiv:2609.04066v1 Announce Type: cross Abstract: Reinforcement learning from human feedback (RLHF) has emerged as a powerful yet sample-inefficient approach for learning reward models from human pref...

### 57. TAP-Path: Task-Adaptive Structural and Token Pruning for Efficient and Trustworthy Pathology Foundation Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04071
- **AI 摘要**: 提出TAP-Path框架，通过任务自适应结构剪枝和令牌剪枝压缩病理基础模型，减少参数和计算量，同时保持高准确率。
- **原始摘要**: arXiv:2609.04071v1 Announce Type: cross Abstract: Pathology foundation models improve transferable representation learning for histopathology, but recent gains often rely on encoders with hundreds of...

### 58. GeoNatureAgent Benchmark: Benchmarking LLM Agents for Environmental Geospatial Analysis Across Frontier and Open-Weight Foundation Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.12821
- **AI 摘要**: 介绍GeoNatureAgent基准，首个通过结构化工具调用真实地理空间API评估环境分析AI智能体的基准，含93个任务、18个类别。评估9种前沿和开源LLM，Claude Sonnet 4能力最高达60.8%，DeepSeek V3.2紧随其后。
- **原始摘要**: arXiv:2606.12821v2 Announce Type: replace Abstract: Environmental scientists spend disproportionate effort on data wrangling rather than analysis. New AI agents can be a helpful tool, but no benchmark...

### 59. DE-Venus: A Data-Efficient RLVR Framework for Large Language Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03324
- **AI 摘要**: 本文提出DE-Venus，一个数据高效的RLVR统一框架，将监督视为演化状态，包含主动数据选择、弱监督构建和训练时监督细化三个模块，支持七种方法。
- **原始摘要**: arXiv:2609.03324v1 Announce Type: new Abstract: Reinforcement learning with verifiable rewards (RLVR) improves large language model reasoning, but its practical scaling is constrained by expensive on-...

### 60. Efficient Constant Optimization for Symbolic Regression with GPU-Accelerated Tree-Based Genetic Programming
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03352
- **AI 摘要**: 本文提出GPU加速的批处理Levenberg-Marquardt求解器，用于符号回归中树形遗传编程的常数优化，通过反向模式自动微分和双精度保护，显著提升优化效率，在A100上每秒处理大量表达式树。
- **原始摘要**: arXiv:2609.03352v1 Announce Type: cross Abstract: Constant optimization refines the numerical coefficients of candidate expressions in tree-based genetic programming for symbolic regression. But its p...

### 61. FedPS: Federated Preprocessing for structured data via aggregated Statistics
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2602.10870
- **AI 摘要**: 提出FedPS框架，用于联邦学习中的结构化数据预处理，通过聚合统计和数据草图技术实现特征缩放、编码、离散化和缺失值填充，兼顾隐私与通信效率。
- **原始摘要**: arXiv:2602.10870v2 Announce Type: replace Abstract: Federated Learning (FL) enables multiple parties to collaboratively train machine learning models without sharing raw data. However, before training...

### 62. Repetition Mismatch: Why Data Mixture Experiments Don't Scale and How to Fix Them
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.07597
- **AI 摘要**: 揭示预训练数据混合实验中的重复失配问题，即高质量数据重复率随训练预算变化导致外推失败，提出匹配重复率的子采样方法，用小规模实验准确预测最优混合。
- **原始摘要**: arXiv:2606.07597v2 Announce Type: replace Abstract: Pre-training data mixtures are commonly tuned by running small-scale experiments and extrapolating to the target training budget. When high-quality...

### 63. KernelFoundry: Hardware-aware evolutionary GPU kernel optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.12440
- **AI 摘要**: KernelFoundry是一个硬件感知的进化GPU内核优化框架，结合MAP-Elites质量多样性搜索、元提示进化和模板参数优化，高效探索内核空间。在Kernel-Bench等任务上生成SYCL内核，优于现有LLM方法。
- **原始摘要**: arXiv:2603.12440v2 Announce Type: replace-cross Abstract: GPU kernel optimization challenges LLMs beyond standard coding tasks, as it requires an understanding of hardware architecture, parallel compu...

### 64. R2S-Eval: Robot Evaluation with Real-to-Sim Calibration via Vision-Language Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03276
- **AI 摘要**: 本文提出R2S-Eval评估流水线，结合真实到仿真校准与视觉语言模型偏好评估，在仿真中生成滚动视频并自动评估机器人操作策略，减少人工干预，提供超越成功率的执行质量信息。
- **原始摘要**: arXiv:2609.03276v1 Announce Type: new Abstract: Evaluating robot manipulation policies is becoming increasingly important as generalist models, particularly vision-language-action (VLA) models, are de...

### 65. FailBench: How Reliable are VLMs at Judging Robot Task Success?
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03611
- **AI 摘要**: 提出FailBench基准，包含2197次机器人操作尝试，评估13个VLM在失败检测上的表现，发现最佳模型平均平衡准确率仅0.77，且微调模型不如通用VLM。
- **原始摘要**: arXiv:2609.03611v1 Announce Type: new Abstract: Vision-Language Models (VLMs) are increasingly used to evaluate robot manipulation outcomes, but existing benchmarks offer limited evidence of cross-dom...

### 66. Predictive Zonotope Reduction: Precise Runtime Monitoring under Uncertainty
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03699
- **AI 摘要**: 提出预测性Zonotope缩减方法，将缩减器选择建模为最优控制问题，用束搜索模型预测控制求解，并蒸馏为小神经网络，提高运行时监控的精度。
- **原始摘要**: arXiv:2609.03699v1 Announce Type: new Abstract: Robots operating in physical environments make control decisions based on uncertain sensor measurements, which can lead to unsafe or suboptimal actions....

### 67. Confidence-Gated Admission for Hardware Prefetching: When the Gate Matters More Than the Predictor
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04040
- **AI 摘要**: 本文研究硬件预取中的置信门控准入策略，发现门控比预测器更重要。在SPEC CPU2017上，门控移除35%预取，准确率从11%提升至15%，但DRAM读取仅变化0.07%。
- **原始摘要**: arXiv:2609.04040v1 Announce Type: new Abstract: Learned cache prefetchers are typically evaluated against classical predictors that always issue requests, confounding the prediction model with the adm...

### 68. RACE-AIMC: Selective Inference for Heterogeneous Analog In-Memory Accelerators at the Edge
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.03149
- **AI 摘要**: 本文介绍RACE-AIMC框架，用于异构模拟存内计算加速器的选择性推理。通过离线研究物理加速器池，选择最佳芯片，以统计方法平衡能耗和准确性，避免盲目信任或全用。
- **原始摘要**: arXiv:2609.03149v1 Announce Type: cross Abstract: Analog in-memory computing (AIMC) speeds up neural-network inference by doing the arithmetic directly inside a memory array, instead of shuttling weig...

### 69. AI-Assisted Design of a Post-Quantum Cryptographic Accelerator: A Deployed-Silicon Case Study
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.04058
- **AI 摘要**: 本文通过AI辅助设计后量子密码加速器，发现标准KAT测试无法检测ML-DSA缺陷。采用字节精确黄金参考和随机对抗浸泡，完成301,343次签名，零逃逸，确保硅片安全。
- **原始摘要**: arXiv:2609.04058v1 Announce Type: cross Abstract: Post-quantum migration is mandated on published timelines, and silicon that ships with a defect cannot be patched remotely. The standard acceptance ga...

### 70. Sim-FA: A GPGPU Simulator Framework for Fine-Grained Asynchronous Pipeline Analysis
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.00555
- **AI 摘要**: 本文构建Sim-F，一个GPGPU模拟器框架，支持细粒度异步流水线分析，集成NVIDIA新特性如TMA，提供周期精确模拟和准确分析模型，用于AI基础设施和架构研究。
- **原始摘要**: arXiv:2605.00555v4 Announce Type: replace Abstract: To efficiently support Large Language Models (LLMs), modern GPGPU architectures have introduced new features and programming paradigms, such as warp...

### 71. NVIDIA PAIR Virtual Inference Router Expands Available Compute on Your Local Network
- **来源**: NVIDIA Technical Blog (TIER1)
- **发布日期**: 2026-09-03T16:00:00Z (今天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/
- **AI 摘要**: NVIDIA PAIR虚拟推理路由器扩展了本地网络上的可用计算资源，支持AI代理协同工作，主代理将复杂任务分解为子任务并分配给专门的子代理执行。
- **原始摘要**: AI agents are learning to do more by working together. A lead agent can break a complex task into smaller jobs and assign those jobs to specialized subagents.......

### 72. Safety overview: GPT-6 AstraSafetySep 3, 2026
- **来源**: OpenAI News (TIER1)
- **发布日期**: 2026-09-03T00:00:00.000Z
- **类型**: news
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://openai.com/index/safety-overview-gpt-6-astra/
- **AI 摘要**: 文章为GPT-6 Astra的安全概述，讨论AI模型的安全评估和防护措施，属于AI安全实践。

### 73. Path to Astra: critical capabilities and frontier safeguardsSafetySep 1, 2026
- **来源**: OpenAI News (TIER1)
- **发布日期**: 2026-09-01T13:00
- **类型**: news
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://openai.com/index/path-to-astra/
- **AI 摘要**: 文章讨论通往Astra的关键能力与前沿安全防护，涉及AI模型的安全评估和部署。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
