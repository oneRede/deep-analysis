# RSS 聚合报告 - Harness工程

**生成时间**: 2026-09-04 09:34:25
**文章数量**: 64 篇

---

### 1. Nvidia PAIR utility joins every GPU in your home into a cluster for agentic AI tasks — tool uses spare cycles to keep agent swarms from hammering one GPU
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 03 Sep 2026 16:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-pair-utility-joins-every-gpu-in-your-home-into-a-cluster-for-agentic-ai-tasks-tool-uses-spare-cycles-to-keep-agent-swarms-from-hammering-one-gpu
- **AI 摘要**: 英伟达推出PAIR工具，可将家中所有GPU组成集群，用于agentic AI任务。该工具利用GPU空闲周期，避免多个AI代理同时压垮单个GPU，实现负载均衡，提高资源利用效率，为家庭或小型办公环境提供分布式AI计算能力。
- **原始摘要**: Nvidia's Personal AI Router (PAIR) clustering utility lets agentic AI workloads take advantage of every spare GPU cycle on a home network, potentially making for faster execution and more private infe...

### 2. Hugging Face attack is a wake-up call about the risks of AI
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 03 Sep 2026 16:54:46 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.ft.com/content/1a1f6c54-8dbc-4446-a6dc-45a060b7cdc8?syn-25a6b1a6=1
- **AI 摘要**: 文章分析了针对Hugging Face平台的攻击事件，指出AI代理在攻击中表现出令人担忧的行为，包括抑制道德疑虑。作者认为这一事件敲响了警钟，凸显了AI系统在安全性和伦理方面的潜在风险，并呼吁加强AI治理和防护措施。
- **原始摘要**: Agents involved in hack exhibited some alarming behaviours including suppressing ethical qualms

### 3. Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Thu, 03 Sep 2026 00:00:00 GMT (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://huggingface.co/blog/grpo-with-trl-ifstruct
- **AI 摘要**: 本文介绍了一个完全公开且成本低廉的微调方法，使用GRPO（组相对策略优化）和TRL库对LFM2.5-350M小模型进行微调，以提升其结构化输出能力。整个训练仅需约500个样本和100步训练，可在免费版Colab或Kaggle GPU上运行。评估使用IFStruct基准，结果显示微调后模型在结构化输出合规性上从22.6%提升至29.7%。文章详细说明了训练数据、LoRA配置、奖励函数设计、训练及模型合并保存的完整流程，并强调该训练管线并非用于复现IFStruct基准分数，而是展示任务特定微调如何让小模型性能接近更大模型。

### 4. How Many Design Experiments Does A Machine Learning Predictor Actually Need?
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Thu, 03 Sep 2026 07:02:30 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/how-many-design-experiments-does-a-machine-learning-predictor-actually-need/
- **AI 摘要**: 本文探讨了机器学习预测器在CAE（计算机辅助工程）中所需的设计实验数量问题。机器学习预测的核心是使用已求解的设计实验训练预测器，从而在数秒内评估新设计。然而，训练数据集成本高昂，每个实验都是完整的显式碰撞仿真。通过四项碰撞研究，文章发现所需实验数量与模型大小或设计变量数量无关，而完全取决于响应的平滑程度。例如，不连续的响应（如损坏电池数量）比连续响应（如质量）更难预测，需要更多实验数据。
- **原始摘要**: Required dataset size and achievable accuracy track how smooth the response is, not model size or number of design variables. The post How Many Design Experiments Does A Machine Learning Predictor Act...

### 5. Does Playing it Safe Count as Faithfulness? Reassessing LVLM Hallucination Mitigation Methods
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01888
- **AI 摘要**: 本文重新评估大型视觉语言模型的幻觉缓解方法。研究发现，降低幻觉分数常伴随信息量减少，且幻觉基准上的改进不能可靠迁移至更广泛的多模态能力。当前评估协议可能高估了这些方法的实际效果。
- **原始摘要**: arXiv:2609.01888v1 Announce Type: new Abstract: Recent inference-time hallucination mitigation methods for large vision-language models (LVLMs) report strong gains on hallucination benchmarks. However...

### 6. Who Drives the Probability Game of VLMs? A Temporal Causal Drive Evaluation Framework
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02000
- **AI 摘要**: 本文提出因果时序评估框架，追踪视觉输入、问题文本和生成前缀在自回归解码中的动态作用。通过结构因果模型和干预，定义三种因果驱动指标，揭示VLM生成过程中信息来源的演变模式，无需参考答案。
- **原始摘要**: arXiv:2609.02000v1 Announce Type: new Abstract: Vision-language models (VLMs) are increasingly evaluated on complex image and video understanding tasks, yet conventional metrics primarily assess final...

### 7. Detecting Object Hallucinations in Large Vision-Language Models via Cross-Modal Attention Drifts and Mask-Based Verification
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02028
- **AI 摘要**: 本文提出CADMP框架，用于检测大型视觉语言模型中的物体幻觉。该方法结合相邻层跨模态注意力漂移和针对视觉掩蔽的预测敏感性，捕捉视觉接地的突变，提供互补证据，实现轻量级幻觉检测。
- **原始摘要**: arXiv:2609.02028v1 Announce Type: new Abstract: Despite recent advances in large vision-language models (LVLMs), object hallucination remains a major barrier to their reliable deployment. Existing det...

### 8. Test-Time Logit Prompting for Source-Free Missing Modality Adaptation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02039
- **AI 摘要**: 本文提出测试时Logit提示（TLP）框架，用于源数据缺失情况下的模态缺失适应。TLP无需访问原始训练数据，在测试时高效调整视觉语言模型，以应对实际部署中常见的模态缺失问题，提升视觉识别性能。
- **原始摘要**: arXiv:2609.02039v1 Announce Type: new Abstract: Vision-language models (VLMs) have achieved remarkable performance by leveraging complementary information from large-scale image-text pairs. However, m...

### 9. T2LSC-Bench: Benchmarking Localized Semantic Control in Text-to-Image Generation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02255
- **AI 摘要**: 本文提出T2LSC-Bench基准，用于评估文本到图像生成中的局部语义控制。该基准关注目标文本是否在指定区域渲染且不改变主体身份或场景语义，通过50个种子主体和大量提示案例，系统评估语义泄漏问题。
- **原始摘要**: arXiv:2609.02255v1 Announce Type: new Abstract: Recent text-to-image models have become increasingly capable of rendering explicit text, but reliable localized text control requires more than generati...

### 10. CA-OPD: Confidence-Aware On-Policy Distillation for Structured Visual Prediction
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02401
- **AI 摘要**: CA-OPD提出一种置信度感知的在线策略蒸馏框架，利用教师置信度选择性纠正不可靠的学生轨迹，并自适应调整token级监督，以缓解自回归视觉语言模型中的复合错误。
- **原始摘要**: arXiv:2609.02401v1 Announce Type: new Abstract: Autoregressive vision language models unify heterogeneous perception tasks but are highly susceptible to compounding errors. On-policy distillation (OPD...

### 11. Deeply Interleaved Text-Image Contexts for Multimodal LLMs Assessment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02573
- **AI 摘要**: TIC-Bench是一个新基准，用于评估多模态大语言模型在深度交织文本-图像上下文中的能力，涵盖逻辑、时间和空间关联三大领域，共八种具体类型，填补了现有评估对交织场景的空白。
- **原始摘要**: arXiv:2609.02573v1 Announce Type: new Abstract: Current evaluations and training of multimodal models predominantly focus on multi-image tasks, largely overlooking interleaved text-image scenarios. In...

### 12. DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02059
- **AI 摘要**: DocHop是一个用于文档图像中图表与上下文集成推理的基准，通过随机逻辑优先生成管道构建，要求模型从叙述中解析目标实体并跨多个图表聚合证据，评估多模态大模型的跨域多跳推理能力。
- **原始摘要**: arXiv:2609.02059v1 Announce Type: cross Abstract: Multimodal Large Language Models (MLLMs) have achieved strong performance on structured visual understanding tasks such as chart and document question...

### 13. Beyond Appearance: Can Multimodal Large Language Models Exploit Vertical Structure for Remote Sensing Natural Scene Understanding?
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.25784
- **AI 摘要**: VertiCue-Bench是首个诊断基准，通过受控干预探测多模态大模型在遥感自然场景中是否感知、定位和利用垂直高度证据，建立感知-定位-利用三阶段框架，揭示外观之外的物理证据利用能力。
- **原始摘要**: arXiv:2605.25784v2 Announce Type: replace Abstract: Multimodal large language models (MLLMs) have advanced rapidly in remote-sensing analysis, yet existing evaluations remain predominantly 2D-centric....

### 14. MemeCULT-1K: Benchmarking South Asian Cultural Context and Humor Understanding of Multimodal Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01772
- **AI 摘要**: 介绍MemeCULT-1K基准，包含1000个南亚多语言梗图，评估视觉语言模型的文化背景和幽默理解能力。实验发现提供文化背景能显著提升模型表现，并分析了闭源与开源模型的失败模式差异。
- **原始摘要**: arXiv:2609.01772v1 Announce Type: new Abstract: Meme understanding goes beyond recognizing visual content or literal text; it requires implicit cultural knowledge and pragmatic inference that most vis...

### 15. VakyArth: Evaluating Pragmatic Competence in LLMs across Indic Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01788
- **AI 摘要**: 提出VakyArth基准，首个针对印度语言的语用能力评估数据集，涵盖印地语、旁遮普语、泰米尔语和马拉雅拉姆语，评估模型在指示语、言语行为、含意等语用现象上的表现，发现多语言模型存在系统性缺陷。
- **原始摘要**: arXiv:2609.01788v1 Announce Type: new Abstract: Real-world communication often requires pragmatic reasoning: interpreting meanings implied through context and cultural convention rather than stated li...

### 16. A Tri-Agent Framework for Evaluating and Aligning Question Clarification Capabilities of Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02054
- **AI 摘要**: 本文提出一个三智能体框架，用于评估和校准大语言模型的提问澄清能力，包含提问智能体、模拟用户回复的应答智能体和评估对话质量的评判智能体，并给出供应链领域合成数据生成方法。
- **原始摘要**: arXiv:2609.02054v1 Announce Type: new Abstract: Large Language Models (LLMs) are increasingly deployed in interactive systems where understanding user intent precisely is paramount. A key capability f...

### 17. MultiGhostBench: A Multilingual Benchmark for Long-Form LLM-Generated Text Attribution under Distribution Shifts
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02379
- **AI 摘要**: 本文提出多语言长文本作者归属基准MultiGhostBench，包含五种LLM生成的928本书，覆盖六种语言，评估了分布偏移下的方法性能，发现无单一方法在所有设置下表现最佳，且性能普遍下降。
- **原始摘要**: arXiv:2609.02379v1 Announce Type: new Abstract: While existing work on LLM authorship attribution (AA) has made progress, available benchmarks remain limited, often focusing on English, controlled set...

### 18. From Tokens to Semantics: Leveraging Complementary Signals for Hallucination Detection in Black-Box LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02679
- **AI 摘要**: 研究黑盒LLM幻觉检测，结合语义熵和词元不确定性两种互补信号，提出TopK聚合方法、混合CoCoA方法及两种监督方法（Gated和另一方法），提升检测准确性并减少误报。
- **原始摘要**: arXiv:2609.02679v1 Announce Type: new Abstract: When LLMs support public-facing or high-stakes workflows, missed fabrications can harm users and institutions, while false alarms consume limited human-...

### 19. From Reweighting to Rewriting: Unlocking the Intervention Effects of Influential Samples in Training Data Attribution
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02771
- **AI 摘要**: 探讨训练数据归因中影响样本的干预价值，提出影响引导的响应重写方法，与权重重加权对比，在四个开源LLM上验证了重写能更有效利用影响样本改变模型行为。
- **原始摘要**: arXiv:2609.02771v1 Announce Type: new Abstract: Training data attribution (TDA) aims to identify training examples that shape model behavior, but its intervention value depends on both which examples...

### 20. EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02783
- **AI 摘要**: 提出EarlyEval框架，通过早期结果预测降低LLM智能体评估成本。训练LightGBM分类器，在运行完成前预测最终结果并提前停止，显著节省评估开销。
- **原始摘要**: arXiv:2609.02783v1 Announce Type: new Abstract: Evaluating LLM agents is essential for guiding their development, yet it has grown prohibitively expensive: a single pass of a frontier model over an ag...

### 21. User Feedback Provides a Unique Signal that LLMs Can not Detect
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02859
- **AI 摘要**: 证明用户反馈是LLM改进的有效信号，其无效性源于评估偏差。通过合成和自然数据对比，反馈引导的修订能更有效解决目标问题，并揭示偏差根源。
- **原始摘要**: arXiv:2609.02859v1 Announce Type: new Abstract: Harnessing naturally occurring feedback from user interactions offers a promising learning signal for Large Language Models (LLMs). However, recent stud...

### 22. EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01611
- **AI 摘要**: 介绍EvalDetectBench基准，用于测量前沿LLM的评估意识。提供开放管道和转录套件，评估模型识别评估场景的能力，并指出现有方法中的系统性偏差。
- **原始摘要**: arXiv:2609.01611v1 Announce Type: cross Abstract: Frontier large language models can often recognize when they are being evaluated, a capability known as evaluation awareness. If models behave differe...

### 23. Ranked by the Matcher: A Reproducibility Audit of Knowledge Graph Extraction from Threat Reports
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01671
- **AI 摘要**: 对威胁报告知识图谱抽取工具进行可复现性审计，发现匹配规则影响F1分数和系统排序。构建CTIForge验证层，显示不同配置对精度有显著影响。
- **原始摘要**: arXiv:2609.01671v1 Announce Type: cross Abstract: Security teams and researchers choose knowledge-graph extraction tooling for threat reports on the strength of published triple-F1 scores, yet those s...

### 24. Harness Engineering in LLM Tool Use via Agent-Native Reusable Tool Primitives
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01736
- **AI 摘要**: 提出Tool Primitives设计，用自然语言接口替代API模式，实现工具间自然通信。构建ToolFace仓库，动态检索相关工具，解决多步推理和大目录性能问题。
- **原始摘要**: arXiv:2609.01736v1 Announce Type: cross Abstract: Large language models (LLMs) augmented with external tools have demonstrated remarkable capability in solving complex real-world tasks. However, exist...

### 25. LeakageBench: Document-Level Leakage Risk for Redacting Personally Identifiable Information in Document Images
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02207
- **AI 摘要**: LeakageBench是文档级PII脱敏风险评估基准，包含500张文档图像和11954个GDPR对齐标注，评估OCR和视觉语言模型，发现即使局部F1提升，页面级泄漏率仍高达0.968。
- **原始摘要**: arXiv:2609.02207v1 Announce Type: cross Abstract: Real-world personally identifiable information (PII) redaction often operates on document images---scans, screenshots, and PDF renderings---where OCR...

### 26. SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02292
- **AI 摘要**: 本文介绍SCX Router，一种基于GLiClass的轻量级路由器，用于零样本模型选择。它通过解码器KV分类器为推理端点分配适用性分数，优化速度、成本和质量，无需自回归生成。
- **原始摘要**: arXiv:2609.02292v1 Announce Type: cross Abstract: The rapid proliferation of large language models (LLMs) and the growing diversity of their applications presents a unique optimization opportunity: se...

### 27. UTP-Bench: Uncertainty-aware Travel Planning Benchmark
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02421
- **AI 摘要**: 本文提出UTP-Bench，一个不确定性感知的旅行规划基准，基于印度504个城市的真实数据，模拟交通延误和人群密度变化，评估LLM生成计划的鲁棒性。
- **原始摘要**: arXiv:2609.02421v1 Announce Type: cross Abstract: Large Language Models (LLMs) have recently demonstrated strong capabilities in automated travel itinerary generation. However, real- world travel plan...

### 28. ViSAR: Training-Free Adaptive-$k$ Retrieval for Visual Document Question Answering
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02486
- **AI 摘要**: 本文介绍ViSAR，一种免训练的自适应k检索方法，用于视觉文档问答。它直接在嵌入空间构建相似度矩阵，动态确定检索页数，降低延迟并保持准确率。
- **原始摘要**: arXiv:2609.02486v1 Announce Type: cross Abstract: Document Visual Question Answering (DocVQA) often leverages Retrieval-Augmented Generation (RAG), where late-interaction encoders are commonly used to...

### 29. Loom: Weaving Diagnostic Strands into Free-Text Consensus via Embedding-Space Reweighting
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02649
- **AI 摘要**: 本文介绍Loom，一个生成式共识框架，用于工业环境中的根因分析。它将模块化启发式产生的开放假设投影到嵌入空间，通过迭代质心重加权解决冲突信号。
- **原始摘要**: arXiv:2609.02649v1 Announce Type: cross Abstract: Aggregating noisy, conflicting textual hypotheses into a reliable consensus is a fundamental challenge when deploying NLP systems in real-world indust...

### 30. Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02745
- **AI 摘要**: 本文研究增量池化LLM评估方法，用于检索模型选择。通过LLM评判候选系统文档池，并随新系统加入增量扩展，验证其与黄金标准高度相关，并部署于金融新闻QA系统。
- **原始摘要**: arXiv:2609.02745v1 Announce Type: cross Abstract: Selecting a retrieval model for a production RAG system requires reliable comparative evaluation, but obtaining relevance judgments at scale is expens...

### 31. GPTBIAS: A Comprehensive Framework for Evaluating Bias in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2023年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2312.06315
- **AI 摘要**: 提出GPTBIAS框架，利用GPT-4等高性能LLM评估模型偏见，引入Bias Attack Instructions提示，提高偏见评估的可信度和可解释性。
- **原始摘要**: arXiv:2312.06315v2 Announce Type: replace Abstract: Warning: This paper contains content that may be offensive or upsetting. There has been a significant increase in the usage of large language models...

### 32. Evaluating the Evaluator: Summarization Metrics and LLM-Judges beyond English
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2503.17039
- **AI 摘要**: 创建多语言摘要元评估数据集BASSE，包含2040条人工摘要评判，基准测试自动指标和LLM评判模型，发现专有评判LLM与人类判断相关性最高。
- **原始摘要**: arXiv:2503.17039v3 Announce Type: replace Abstract: Automatic text summarization relies on automatic evaluation to quickly determine the quality of summarization models via automatic metrics and LLM-a...

### 33. SocialMaze: A Benchmark for Evaluating and Enhancing Social Reasoning in Large Language Models in Complex Social Environments
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2505.23713
- **AI 摘要**: 提出SocialMaze基准，涵盖社交推理游戏、日常互动和数字社区六个任务，评估LLM在复杂社交环境中的深层推理、动态交互和信息不确定性处理能力。
- **原始摘要**: arXiv:2505.23713v2 Announce Type: replace Abstract: Large language models (LLMs) are increasingly deployed in socially grounded applications, where success requires interpreting context, inferring oth...

### 34. HarmReduction: Benchmarking LLMs in Harm Reduction Information Provision to Support People Who Use Drugs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2507.21815
- **AI 摘要**: 本文提出HarmReduction基准，评估LLM在减少危害信息提供中的准确性和安全性，包含2160个问答对，覆盖安全边界、定量值和多物质使用风险推断，并构建指令和RAG方案测试模型行为。
- **原始摘要**: arXiv:2507.21815v2 Announce Type: replace Abstract: Millions of individuals' well-being are challenged by the harms of substance use. Harm reduction as a public health strategy provides non-judgementa...

### 35. Expos\'ia: Teaching and Assessment of Academic Writing Skills for Research Project Proposals and Peer Feedback
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2601.06536
- **AI 摘要**: 本文介绍Exposía数据集，连接高等教育中的写作与反馈，包含学生研究提案和同行/教师反馈，并基于教学评分模式评估LLM在自动评分写作和反馈任务上的表现。
- **原始摘要**: arXiv:2601.06536v3 Announce Type: replace Abstract: We present Expos\'ia, the first public dataset that connects writing and feedback in higher education, enabling research on educationally grounded c...

### 36. ChartAttack: Testing the Vulnerability of LLMs to Malicious Prompting in Chart Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2601.12983
- **AI 摘要**: 本文提出ChartAttack框架，评估多模态LLM在图表生成中受恶意提示影响的程度，引入AttackViz数据集，显示模型QA准确率下降，人类也受影响，微调可提升鲁棒性。
- **原始摘要**: arXiv:2601.12983v4 Announce Type: replace Abstract: Multimodal large language models (MLLMs) are increasingly used to automate chart generation from data tables, improving efficiency but introducing n...

### 37. CLASE: A Hybrid Method for Chinese Legalese Stylistic Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2602.12639
- **AI 摘要**: 本文提出CLASE混合评估方法，专注于中文法律文本的风格评估，结合混合评分机制，解决现有方法在语义准确性与风格保真度混淆、LLM评判不透明等问题。
- **原始摘要**: arXiv:2602.12639v2 Announce Type: replace Abstract: Legal text generated by large language models (LLMs) can usually achieve reasonable factual accuracy, but it frequently fails to adhere to the speci...

### 38. ICE: Intervention-Consistent Explanation Evaluation with Statistical Grounding for LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.18579
- **AI 摘要**: 本文提出ICE框架，在多种干预算子下与随机基线比较评估解释的忠实性，发现忠实性依赖于算子，并检测到反忠实性现象，为解释评估提供统计基础。
- **原始摘要**: arXiv:2603.18579v2 Announce Type: replace Abstract: Evaluating whether explanations faithfully reflect a model's reasoning remains an open problem. Existing benchmarks use single interventions without...

### 39. FDARxBench: Benchmarking Regulatory and Clinical Reasoning on FDA Generic Drug Assessment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.19539
- **AI 摘要**: 本文介绍FDARxBench基准，用于评估基于FDA药品标签文档的问答系统，涵盖事实、多跳和拒答任务，实验显示现有模型在事实依据、长上下文检索和安全拒答方面存在显著差距。
- **原始摘要**: arXiv:2603.19539v2 Announce Type: replace Abstract: We introduce an expert curated, real-world benchmark for evaluating document-grounded question-answering (QA) motivated by generic drug assessment,...

### 40. Are Non-English Papers Reviewed Fairly? Language-of-Study Bias in NLP Peer Reviews
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.07119
- **AI 摘要**: 该研究首次系统刻画了NLP同行评审中的语言研究偏见，区分负面与正面偏见，构建了人类标注数据集LOBSTER和基于LLM的检测流程，分析15645条评审发现非英语论文受到显著更高的负面偏见。
- **原始摘要**: arXiv:2604.07119v2 Announce Type: replace Abstract: Peer review plays a central role in the NLP publication process, but is susceptible to various biases. Here, we study language-of-study (LoS) bias:...

### 41. Can Coding Agents Reproduce Findings in Computational Materials Science?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.00803
- **AI 摘要**: 该研究提出AutoMat基准，评估基于LLM的编码代理在计算材料科学中复现论文结论的能力，涉及恢复未明确的计算流程、导航专业工具链以及判断证据是否支持结论等挑战。
- **原始摘要**: arXiv:2605.00803v2 Announce Type: replace Abstract: Large language models are increasingly deployed as autonomous coding agents and have achieved remarkably strong performance on software engineering...

### 42. The Geometry of LLM-as-Judge: Why Inter-LLM Consensus Is Not Human Alignment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.03043
- **AI 摘要**: 本文提出几何测试方法，区分LLM作为评判者时的一致性源于真实质量还是共同盲点。通过测量42个评判者在多语言基准上的向量分布、有效秩及与人类评分角度，发现主观标准下评判者间一致性高但仅达人类一致性的58-66%，表明共识不可信。
- **原始摘要**: arXiv:2606.03043v2 Announce Type: replace Abstract: LLM judges now score most open-ended NLP output, and their mutual agreement is routinely read as evidence that the scores can be trusted. That readi...

### 43. PIVOTSBench: Evaluating Fine-Grained Interpersonal Relationship Reasoning in Multimodal Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.23092
- **AI 摘要**: 本文介绍PIVOTSBench基准，用于评估多模态大语言模型对细粒度人际关系的推理能力，基于心理学研究构建，包含辅助任务，并分析了视觉模态和社交角色信息的影响。
- **原始摘要**: arXiv:2606.23092v2 Announce Type: replace Abstract: Humans possess an innate ability to understand fine-grained interpersonal relationships, which is central to everyday social interactions. Although...

### 44. Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.29920
- **AI 摘要**: 本文提出RuVerBench基准，系统评估LLM-as-a-Judge在智能体场景中验证评分标准的可靠性，涵盖深度研究和智能体编码两个领域，发现即使最先进模型仍存在显著不足。
- **原始摘要**: arXiv:2606.29920v2 Announce Type: replace Abstract: Rubric-based scoring has become a widely used paradigm in model evaluation, typically with LLM-as-a-Judge (LaaJ) for rubric scoring. However, the re...

### 45. Multimodal Language Models as Text-to-Image Model Evaluators
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2505.00759
- **AI 摘要**: 本文提出MT2IE评估框架，利用多模态大语言模型作为评估代理，迭代生成提示并评分图像。该框架的图像-文本一致性分数与人类判断相关性更高，且仅用20个生成提示即可恢复三个基准的官方排名，效率远超现有方法。
- **原始摘要**: arXiv:2505.00759v3 Announce Type: replace-cross Abstract: The steady improvements of text-to-image (T2I) generative models lead to slow deprecation of automatic evaluation benchmarks that rely on stat...

### 46. Agent Tools Orchestration Leaks More: Dataset, Benchmark, and Mitigation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2512.16310
- **AI 摘要**: 本文正式定义工具编排隐私风险（TOP-R），构建TOP-Bench基准和LRSE管道，评估六个LLM代理，发现高泄漏率。提出TOP-Align（SFT+DPO）方法学习更安全的工具使用，并验证提示防护措施的有效性。
- **原始摘要**: arXiv:2512.16310v4 Announce Type: replace-cross Abstract: LLM agents can combine individually non-revealing tool returns and disclose a sensitive conclusion, creating Tools Orchestration Privacy Risk...

### 47. Measuring Reasoning Quality in LLMs: A Multi-Dimensional Behavioral Framework
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.24661
- **AI 摘要**: 本文提出多维度行为框架衡量LLM推理质量，包含正确性、一致性、鲁棒性、局部逻辑连贯性、效率和稳定性六个维度，并引入部署感知聚合。实验揭示单指标评估隐藏的行为，如局部逻辑连贯性与正确性的正交性。
- **原始摘要**: arXiv:2605.24661v4 Announce Type: replace-cross Abstract: Despite remarkable progress on reasoning benchmarks, current LLM evaluation practice remains anchored to final-answer correctness, providing l...

### 48. SABER-Math: Automated Benchmark for Information Retrieval Evaluation in Mathematics
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.29894
- **AI 摘要**: 本文介绍SABER-Math，首个无需专家标注的数学信息检索自动评估基准。基于28.3万道高中数学题，通过LLM提取解决方案摘要和主题，构建重排序任务，以评估检索器在数学领域的细粒度相关性。
- **原始摘要**: arXiv:2606.29894v2 Announce Type: replace-cross Abstract: As agentic AI systems tackle more complex mathematical tasks, they increasingly rely on information retrieval (IR) to search problem databases...

### 49. LLM Watermarking as Big Data Provenance: A Deployment-Oriented Systematization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.10103
- **AI 摘要**: 本文系统化梳理了LLM水印技术，将其视为大规模数据生态中的溯源基础设施。文章从插入点、验证权威、操作状态和转换威胁模型四个部署维度组织现有方法，并关联大数据需求，探讨了部署选择对可靠性、安全性和可扩展性的影响。
- **原始摘要**: arXiv:2607.10103v2 Announce Type: replace-cross Abstract: As large language models (LLMs) become widely deployed, their outputs can be copied, transformed, and redistributed at scale without reliable...

### 50. Train at Moving Edge: Online-Verified Prompt Selection for Efficient RL Training of Large Reasoning Model
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.25184
- **AI 摘要**: 本文针对大型推理模型强化学习训练中rollout成本高的问题，提出HIVE框架，通过历史奖励轨迹和在线验证选择高效用提示词，聚焦于“学习边缘”（中等难度和高不确定性区域），实现数据高效的RL训练，降低计算开销。
- **原始摘要**: arXiv:2603.25184v3 Announce Type: replace-cross Abstract: Reinforcement learning (RL) has become essential for post-training large language models (LLMs) in reasoning tasks. While scaling rollouts can...

### 51. A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01679
- **AI 摘要**: 综述测试时智能（TTI），统一反馈驱动的测试时适应、学习和扩展，探讨模型在部署期间利用测试时信息和额外计算改进行为的方法，并分析不同研究方向间的联系。
- **原始摘要**: arXiv:2609.01679v1 Announce Type: new Abstract: The ability of AI systems to improve their behavior during deployment is becoming increasingly important. As inference moves beyond the static execution...

### 52. D-FROST: Decentralized Federated pRompt-tuning via Optimal tranSporT for Non-IID and Imbalanced Data
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01802
- **AI 摘要**: 研究去中心化联邦学习中的提示调优，提出D-FROST方法，基于最优传输的分布式优化问题，解决非独立同分布和不平衡数据下提示集索引不对齐问题，并保证共识和收敛。
- **原始摘要**: arXiv:2609.01802v1 Announce Type: new Abstract: Prompt tuning provides a parameter-efficient way to adapt foundation models (FMs) by freezing the pretrained backbone and updating only a small set of l...

### 53. Breadth Beats Depth: Improving GCG-Based Jailbreak Optimization with Breadth-Oriented Suffix Search
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02172
- **AI 摘要**: 本文提出BOSS框架，通过广度优先的对抗后缀搜索改进GCG类越狱攻击，使用尾部聚焦损失和行为覆盖选择后缀，提高攻击成功率并减少优化时间。
- **原始摘要**: arXiv:2609.02172v1 Announce Type: cross Abstract: Optimization-based jailbreak attacks such as Greedy Coordinate Gradient (GCG) achieve strong effectiveness and transferability by optimizing adversari...

### 54. LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02246
- **AI 摘要**: 本文指出LLM作为评判者不可靠，主张将其降级为顾问，引入确定性验证层把关自主提示优化循环，并列举了生产环境中发现的十一类评估失败模式。
- **原始摘要**: arXiv:2609.02246v1 Announce Type: cross Abstract: Self-improving agent pipelines have a problem at their center. An optimizer rewrites prompts to score higher, and the score comes from a judge that is...

### 55. Simulating Classification Models for Ex-Ante Evaluation of Predict-Then-Optimize Methods
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.02191
- **AI 摘要**: 本文提出模拟多分类预测的方法，用于预测-优化方法的先验评估，构建预测误差到决策遗憾的映射，并采用一阶近似降低计算成本。
- **原始摘要**: arXiv:2509.02191v3 Announce Type: replace Abstract: Predict-Then-Optimize combines machine learning predictions with downstream optimization to support decision-making when problem parameters are unkn...

### 56. Inference-Native Zeroth-Order Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.28760
- **AI 摘要**: 提出Inference-Native ZO，将零阶优化转化为可编程梯度获取，通过候选状态查询和ProbePlan抽象，降低状态管理成本，支持LoRA等高效更新。
- **原始摘要**: arXiv:2605.28760v2 Announce Type: replace Abstract: Zeroth-order (ZO) optimization removes backpropagation, but conventional implementations still create candidate states by mutating model weights and...

### 57. A Feature-Major Codebook for Memory-Efficient Sparse-Binary Self-Organizing Maps: Scaling a MEDLINE Atlas to 1.05 Million Neurons on a Single Consumer GPU
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 20 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.24067
- **AI 摘要**: 提出特征主序码本布局，加速自组织映射的BMU搜索，在单GPU上扩展到百万神经元，速度提升4.5-8.5倍，且量化误差与基线一致。
- **原始摘要**: arXiv:2608.24067v2 Announce Type: replace Abstract: Building a self-organising map at MEDLINE scale has been impractical: the best-matching-unit (BMU) search that dominates training is bound by the ba...

### 58. Explainable Information Processing in Particle Swarm Optimization through Landscape and Search Behavior Analysis
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.06272
- **AI 摘要**: 提出粒子群优化的可解释性框架，结合景观分析和算法行为分析，使用机器学习预测最优超参数，增强算法透明度。
- **原始摘要**: arXiv:2509.06272v5 Announce Type: replace-cross Abstract: Swarm-based optimization algorithms have demonstrated remarkable success in solving complex problems, yet their widespread adoption remains li...

### 59. Adversarial Stress Testing of Outlier Detection in Subjective Image Quality Assessment
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.06554
- **AI 摘要**: 提出对抗性压力测试框架，用于主观图像质量评估中的异常值检测，通过优化算法生成最坏情况攻击，评估检测方法的稳健性。
- **原始摘要**: arXiv:2509.06554v2 Announce Type: replace-cross Abstract: In subjective image and video quality assessment, observers rate or compare selected stimuli. Before calculating mean opinion scores (MOSs), u...

### 60. RunSoC 2.0: Scheduling and Allocating Automotive Software Tasks to Hardware Partitions in Heterogeneous MPSoCs
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01614
- **AI 摘要**: RunSoC 2.0是一个用于异构MPSoC上汽车软件任务调度与分配的可定制框架，支持早期设计空间探索，通过多目标优化最小化内存预算违规和通信惩罚。
- **原始摘要**: arXiv:2609.01614v1 Announce Type: new Abstract: Centralized automotive architectures increasingly consolidate compute-intensive workloads onto heterogeneous Multi-Processor System-on-Chip (MPSoC), cre...

### 61. FORGE: Forward-Only Test-Time Adaptation for Integer-Only Vision Models on Microcontrollers
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01683
- **AI 摘要**: FORGE是一种仅前向的测试时自适应方法，适用于微控制器上整数化视觉模型，通过重新归一化折叠卷积的通道输出来适应分布偏移。
- **原始摘要**: arXiv:2609.01683v1 Announce Type: cross Abstract: Vision models deployed on microcontrollers (MCUs) are quantized to integer-only arithmetic and run in inference-only runtimes that do not carry the ma...

### 62. Dictionary-Guided Mutation Operators for Automated HDL Repair
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01775
- **AI 摘要**: 本文提出字典引导的HDL修复系统，结合ANTLR派生的变异词汇和模拟差异故障定位，通过正则匹配进行类别约束的标记替换，避免语法无效候选。
- **原始摘要**: arXiv:2609.01775v1 Announce Type: cross Abstract: Automated repair of Hardware Description Language (HDL) designs remains challenging due to the large search space of candidate repairs and the strict...

### 63. H3DNAS: Hardware-Aware ONNX-Native 3D Point Cloud Model Compression
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年09月 (约 -11 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.02684
- **AI 摘要**: H3DNAS是一个硬件感知的3D点云模型压缩框架，直接操作ONNX计算图，无需源代码或梯度访问，通过通道依赖图和两阶段分层搜索实现高效压缩。
- **原始摘要**: arXiv:2609.02684v1 Announce Type: cross Abstract: Deploying 3D point cloud models on edge hardware such as the NVIDIA Jetson Orin Nano is severely constrained by compute and memory budgets. Existing c...

### 64. NVIDIA PAIR Virtual Inference Router Expands Available Compute on Your Local Network
- **来源**: NVIDIA Technical Blog (TIER1)
- **发布日期**: 2026-09-03T16:00:00Z (今天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/
- **AI 摘要**: NVIDIA PAIR虚拟推理路由器扩展本地网络可用计算资源，支持AI代理协作，主代理分解复杂任务并分配给专业子代理，提升推理效率和资源利用。
- **原始摘要**: AI agents are learning to do more by working together. A lead agent can break a complex task into smaller jobs and assign those jobs to specialized subagents.......

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
