# RSS 聚合报告 - AI模型

**生成时间**: 2026-09-01 07:13:39
**文章数量**: 86 篇

---

### 1. Sliding-window attention beats linear on long-context reasoning [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-31T16:35:42+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/
- **AI 摘要**: 文章探讨了在长上下文推理任务中，滑动窗口注意力机制相比线性注意力机制的表现更优。作者通过实验对比了两种注意力机制在长序列推理任务上的效果，指出滑动窗口注意力在保持局部信息的同时能更好地处理长距离依赖，而线性注意力虽然计算效率高但在复杂推理任务中性能下降。文章为长上下文模型设计提供了实证参考。
- **原始摘要**: Sliding Window Attention with sinks, one of the simplest existing fixes for the quadratic-cost problem in LLMs, holds up as well or better than the linear-attention variants labs have been spending po...

### 2. Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27549
- **AI 摘要**: 本文提出Code-as-World范式，将物理世界表示为可执行代码，包括物理组成、动态演化和视觉外观，通过溯因推理的智能体发现循环，从多模态观测构建紧凑、可量化、可控的世界表示，用于物理推理。
- **原始摘要**: arXiv:2608.27549v1 Announce Type: new Abstract: Physical understanding and reasoning depend on forming compact and generalizable representations of the world. While modern vision-language models can r...

### 3. What Can Low Resource Languages Learn From Each Other?
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27753
- **AI 摘要**: 本文研究低资源语言在OCR任务中的适应问题，发现传统微调存在性能上限，且低层特征冗余。提出PSMC框架（预训练、特化、合并、协同训练），通过跨语言共享低层特征提升数据效率。
- **原始摘要**: arXiv:2608.27753v1 Announce Type: new Abstract: Despite the rapid advancement of Vision-Language Models (VLMs), their linguistic reach remains largely confined to high-resource languages, leaving the...

### 4. Visual Token Coding for Video Multimodal Large Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28008
- **AI 摘要**: 本文提出视觉令牌编码（VTC）范式，受视频编码原理启发，通过预测I/P帧并计算残差估计令牌冗余，实现视频MLLM的令牌压缩。动态设计（DyRSO、DyTA、SC-TopK）在50%令牌预算下保持100.1%性能。
- **原始摘要**: arXiv:2608.28008v1 Announce Type: new Abstract: In this paper, we propose a new token compression paradigm for video Multimodal Large Language Models (MLLMs), termed Visual Token Coding (VTC). Inspire...

### 5. Dynamic Alignment Compensation for Hallucination Mitigation in Large Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28058
- **AI 摘要**: 本文提出动态对齐补偿（DAC）方法，一种无需训练的推理时方法，检测跨模态表示在解码层间的退化和生成步骤间的漂移，通过层间语义补偿和序列语义校正选择性应用轻量残差补偿，减少LVLM幻觉。
- **原始摘要**: arXiv:2608.28058v1 Announce Type: new Abstract: Large Vision-Language Models (LVLMs) remain prone to hallucinations, producing responses that are irrelevant or inconsistent with the multimodal input....

### 6. Token-Budget Distillation: Transferring Full-Token Semantics to Compressed Video Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28138
- **AI 摘要**: 提出Token-Budget蒸馏框架，在固定token预算下通过冻结骨干网络、更新LoRA适配器并集成FlashVID压缩，采用双路径师生设计保留全token语义，减少视频视觉语言模型微调和推理成本。
- **原始摘要**: arXiv:2608.28138v1 Announce Type: new Abstract: Adapting video vision-language models (VLMs) is computationally expensive because video inputs produce a large number of visual tokens, making both fine...

### 7. Dual-Stream Semantic Guidance with Prototype Anchor Calibration for Source-Fully-Free Adaptation of Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28145
- **AI 摘要**: 针对源完全自由域适应中的双重语义漂移问题，提出DSSG框架，包含双流语义引导模块和动态跨模态知识蒸馏，以协调视觉语言模型的细粒度可塑性与全局稳定性。
- **原始摘要**: arXiv:2608.28145v1 Announce Type: new Abstract: Source-Fully-Free Domain Adaptation (SFF-DA) has emerged as a strategic paradigm to adapt Vision-Language Models (VLMs) without any access to source dat...

### 8. Locate Anything in Videos: Rethinking Efficient Generative Spatio-Temporal Video Grounding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28192
- **AI 摘要**: 提出并行管解码方法，将时空视频定位分解为时间块和条件空间块并行解码，消除依赖并固定解码深度，配合解耦块注意力和定位感知策略优化，提升生成式视频定位效率。
- **原始摘要**: arXiv:2608.28192v1 Announce Type: new Abstract: Spatio-temporal video grounding (STVG) requires models to identify when a referred event occurs and localize the target entity throughout that interval....

### 9. Post-Training VLMs for Video Mistake Detection
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28406
- **AI 摘要**: 提出视频错误检测的问答协议和基准MD-VQA，并首次提出视频语言模型后训练技术，使模型学习通用错误概念而非特定步骤细节，适用于未见动作。
- **原始摘要**: arXiv:2608.28406v1 Announce Type: new Abstract: Human mistakes are inevitable when following instructions, yet they can lead to severe consequences. As such, there has been an increased interest in de...

### 10. Fully Unleashing the Multimodal Attacker: Meta-Adaptive Jailbreaking of Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27531
- **AI 摘要**: 提出元自适应多模态越狱方法MAMJ，通过优化攻击策略提示和攻击者权重，在MM-SafetyBench上对GPT-4o等模型实现高攻击成功率，显著超越基线。
- **原始摘要**: arXiv:2608.27531v1 Announce Type: cross Abstract: The safety of large vision-language models is increasingly stress-tested by multimodal jailbreaks, yet existing attacks remain largely static at the m...

### 11. Do Medical Vision Models Reason About Anatomy? Probing the Spatial Inductive Biases of Learned Visual Representations
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28092
- **AI 摘要**: 本文提出SPAR-Bench基准，用于探测医学视觉模型的空间归纳偏差。通过八个探针测试CT图像中的坐标定位、关系推理和空间查询，发现模型在切片内比较任务上表现接近随机，且预训练规模、微调或架构均无法弥补差距，表明模型依赖典型解剖记忆而非图像计算。
- **原始摘要**: arXiv:2608.28092v1 Announce Type: cross Abstract: Interpreting a CT scan means comparing structures on either side, judging how far apart organs sit, and knowing where each one belongs. Medical vision...

### 12. Talk in Pieces, See in Whole: Disentangled and Hierarchical Representation Learning in Language-based Object Detection
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2509.24192
- **AI 摘要**: 本文提出TaSe框架，用于语言基础的目标检测。通过将文本标记解耦为对象、属性和关系三个核心组件，并聚合为层级结构的句子级表示，以处理复杂查询。框架包含层级合成字幕数据集、三组件解耦模块和新的解耦损失，提升模型对描述性属性和关系子句的理解。
- **原始摘要**: arXiv:2509.24192v2 Announce Type: replace Abstract: Vision-language models (VLMs) have advanced multimodal perception, demonstrated by open-vocabulary object detection with simple language queries. St...

### 13. Don't Let the Video Speak: Audio-Contrastive Preference Optimization for Audio-Visual Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.14129
- **AI 摘要**: 本文提出音频对比偏好优化（ACPO）框架，用于缓解音视频语言模型中的跨模态幻觉，特别是视频驱动的音频幻觉。通过输出对比和输入对比双重目标，惩罚将视觉描述伪装成音频事实以及忽略真实音频信号的生成，实验证明ACPO显著提升音频接地性并减少幻觉。
- **原始摘要**: arXiv:2604.14129v2 Announce Type: replace Abstract: While Audio-Visual Language Models (AVLMs) have achieved remarkable progress over recent years, their reliability is bottlenecked by cross-modal hal...

### 14. GraSP-VL: Length as a Semantic Granularity Interface for Vision-Language Representations
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.17727
- **AI 摘要**: 本文提出GraSP-VL，通过学习共享近正交前缀变换，将嵌入长度转化为可控的语义粒度接口。短前缀对应粗粒度语义，长前缀逐步暴露更细的语言接地区分，在COCO/Flickr30K数据集上达到53.01的阶梯分数和89.76的硬负样本选择性，同时保持原始VLM空间几何。
- **原始摘要**: arXiv:2605.17727v2 Announce Type: replace Abstract: Frozen vision-language embeddings contain signals at multiple semantic resolutions, from object identity to attributes, relations, and full-caption...

### 15. Spectral Query-Key Product Weight Steering for Training-Free VLM Hallucination Mitigation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.20419
- **AI 摘要**: 本文提出QK Product Steering，一种无需数据、无需训练、零推理成本的权重编辑方法，通过抑制选定中间层中查询-键乘积的主导奇异模式来减少视觉语言模型的对象幻觉。该方法兼容分组查询注意力，在三个GQA模型上平均降低CHAIRs 4.0%。
- **原始摘要**: arXiv:2606.20419v2 Announce Type: replace Abstract: Vision-language models (VLMs) often generate fluent but visually unsupported descriptions, especially by mentioning objects absent from the image. W...

### 16. Transformer-Based Autonomous Driving Models and Deployment-Oriented Compression: A Survey
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2023年04月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2304.10891
- **AI 摘要**: 综述基于Transformer的自动驾驶模型及其部署导向的压缩技术。从任务角色、传感配置和架构设计角度分类，重点分析量化、剪枝、知识蒸馏等压缩策略如何应对延迟、内存和能耗约束，为实际部署提供指导。
- **原始摘要**: arXiv:2304.10891v4 Announce Type: replace-cross Abstract: Transformer-based models are becoming a central paradigm in autonomous driving because they can capture long-range spatial dependencies, multi...

### 17. Amortizing intractable inference in diffusion models for vision, language, and control
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2024年05月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2405.20971
- **AI 摘要**: 研究扩散模型作为先验时的难解后验推断问题，提出相对轨迹平衡目标用于训练扩散模型进行摊销后验采样，并证明其渐近正确性。该方法利用生成流网络视角和强化学习技术，提升模式覆盖，适用于视觉、语言和控制任务。
- **原始摘要**: arXiv:2405.20971v3 Announce Type: replace-cross Abstract: Diffusion models have emerged as effective distribution estimators in vision, language, and reinforcement learning, but their use as priors in...

### 18. The Effect of Emotional Context on Large Language Models' Endorsement of Premature Decisions: Comparing Emotional Vulnerability Across Six Commercial Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27465
- **AI 摘要**: 本文研究了情绪语境对六种商业大语言模型支持用户草率决策的影响。通过控制对话轮次和事实内容，对比冷、中性和痛苦三种情绪条件，发现情绪表达可能增加模型对不成熟决策的支持，引发安全担忧。
- **原始摘要**: arXiv:2608.27465v1 Announce Type: new Abstract: As large language models (LLMs) are increasingly used for everyday decision-making advice, whether a model shifts the direction of its advice according...

### 19. INSPIRE: An Internalize-Then-Improve Approach for Example-Driven Mathematical Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27501
- **AI 摘要**: 本文提出INSPIRE方法，通过“内化-改进”两阶段策略增强大语言模型的示例驱动数学推理能力，特别是构造反例的能力。方法包括参考引导的学生内化和渐进式偏好优化，以提升模型对数学概念的深层理解。
- **原始摘要**: arXiv:2608.27501v1 Announce Type: new Abstract: Mathematical reasoning has seen rapid progress in large language models (LLMs), yet existing methods optimize predominantly for final-answer correctness...

### 20. Trajectory-Level Speculative Decoding for Diffusion Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27514
- **AI 摘要**: 本文针对扩散语言模型提出轨迹级投机解码框架，通过置信分层树探索构建草稿去噪轨迹，并利用块级并行评估和双向注意力掩码验证，支持跨块投机，显著提升吞吐量，同时分析了精确性和轨迹漂移问题。
- **原始摘要**: arXiv:2608.27514v1 Announce Type: new Abstract: Diffusion-based language models (dLLMs) enable parallel token generation through iterative denoising, but existing decoding strategies collapse to singl...

### 21. When Tokenizers Fail: Byte-Level Chunking for Zero-Shot Transfer to Low-Resource Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27658
- **AI 摘要**: 本文提出一种自适应层次网络框架，通过从冻结子词模型的表示初始化字节嵌入，并应用块对齐损失和词性标注，解决字节级模型在低资源语言零样本迁移中的粒度不匹配问题，无需大量训练数据。
- **原始摘要**: arXiv:2608.27658v1 Announce Type: new Abstract: Subword tokenization hinders low-resource language processing by imposing frequency patterns from dominant languages onto script-sharing variants. Byte-...

### 22. First Make It Playable, Then Make It Good: Staged Interaction Learning for Small Dialogue-Game Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27672
- **AI 摘要**: 本文提出Qwen-GuidePlay-2B对话游戏智能体，采用三阶段微调：成功轨迹SFT、加权轮次SFT和教师引导SFT。在Playpen基准上取得优异成绩，验证了分阶段交互学习方法的有效性，并发现重放修复等复杂方法效果不佳。
- **原始摘要**: arXiv:2608.27672v1 Announce Type: new Abstract: We present Qwen-GuidePlay-2B, a 2B-parameter language model for dialogue-game interaction. We fine-tune Qwen3.5-2B using three steps: a) SFT on only suc...

### 23. Informational Antilocality and the Locality Bias in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27760
- **AI 摘要**: 本文研究Transformer语言模型学习k-反局部语言的能力，构造不同k值的无互信息语言。发现模型最终损失相当，但反局部性越强收敛越慢，支持非局部依赖更难学习的观点，但证据来自学习速度而非最终成功率。
- **原始摘要**: arXiv:2608.27760v1 Announce Type: new Abstract: We consider the ability of transformer-based language models (LLMs) to learn what we call k-antilocal languages, i.e., languages that have no mutual inf...

### 24. Representation of syntax in LLMs through the lens of linear distance and similarity-aware entropy
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27813
- **AI 摘要**: 本文通过按标签分解无向依存得分，研究LLM句法表示。发现线性距离和相似性熵两个因素能预测大部分UASL变异性，结果跨模型规模和架构一致，揭示了句法关系重建的差异及其影响因素。
- **原始摘要**: arXiv:2608.27813v1 Announce Type: new Abstract: Structural probes were introduced by Hewitt and Manning to reconstruct syntactic trees from a neural language model's latent representations. They are e...

### 25. PersonaEdit: Representative Sample Selection for Personalized Model Editing
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27816
- **AI 摘要**: 本文提出PersonaEdit，一种基于隐藏表示聚类的代表性样本选择策略，用于个性化模型编辑。通过比例分层抽样选择编辑样本，实验证明模型编辑对个性化有效，且该策略保留大部分性能，减少计算成本和编辑干扰。
- **原始摘要**: arXiv:2608.27816v1 Announce Type: new Abstract: Personalization has attracted growing interest in LLM applications, yet existing retrieval-based approaches depend heavily on retrieval quality and degr...

### 26. Beyond Global Scalars: Synergizing Token-Level Statistics and Deep Semantics for Adversarial AIGC Text Detection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28009
- **AI 摘要**: 针对对抗性AIGC文本检测，提出MOSAIC基准和NeuroStat框架，结合token级统计与深度语义，弥补全局标量与纯语义方法的不足，提升对抗场景下的检测鲁棒性。
- **原始摘要**: arXiv:2608.28009v1 Announce Type: new Abstract: The rapid evolution of large language models necessitates robust machine-generated text detection. Existing paradigms typically follow two isolated trac...

### 27. Twin Worlds: Equivariance-Based Abstention for Evidence-Grounded Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28018
- **AI 摘要**: 提出Twin Worlds框架，通过等变性弃权机制提升知识密集型推理的可靠性。不同于不变性要求输出不变，等变性要求输出随实体替换相应变换，从而检测推理是否真正基于证据。
- **原始摘要**: arXiv:2608.28018v1 Announce Type: new Abstract: Knowledge-intensive reasoning requires Large Language Models (LLMs) to ground answers in provided evidence. When evidence is insufficient, it is desirab...

### 28. H-Scale: Hessian-Guided Scale Refinement for NVFP4 Sub-Byte LLM Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28113
- **AI 摘要**: 提出H-Scale方法，用于NVFP4格式的逐组缩放因子优化。利用二阶代理直接优化层输出扰动，而非最小化权重重建误差，提升Blackwell架构上LLM推理的量化性能。
- **原始摘要**: arXiv:2608.28113v1 Announce Type: new Abstract: The NVIDIA Blackwell architecture, with native support for the ultra-fine-grained NVFP4 format, opens new opportunities for accelerating large language...

### 29. Nested Byte-Level Vocabularies Are Cheap to Deploy and Expensive to Share: A Pre-Registered Negative Result
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28151
- **AI 摘要**: 研究字节级BPE词表的嵌套前缀部署。切片模型可精确复现完整模型输出并减少66%权重，但共享模型性能落后于固定大小专家模型，预注册的负结果验证了部署与共享的权衡。
- **原始摘要**: arXiv:2608.28151v1 Announce Type: new Abstract: A byte-level BPE tokenizer is an ordered list of merge rules, so applying only a prefix yields a vocabulary whose token identifiers are the first rows o...

### 30. When Linguistic and Internal Confidence Diverge in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28382
- **AI 摘要**: 研究大语言模型的语言置信度与内部置信度是否一致，通过分类和生成任务比较，发现两者常出现分歧，指令微调模型置信度更高但校准更差，提示设计影响置信度分布。
- **原始摘要**: arXiv:2608.28382v1 Announce Type: new Abstract: Users often ask large language models (LLMs) to report how confident they are, but it is unclear whether such linguistic confidence tracks the model's i...

### 31. Sliding-window beats linear attention
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28444
- **AI 摘要**: 研究滑动窗口注意力（SWA）与线性注意力在LLM中的性能对比，发现SWA在多种下游任务上表现相当或更好，尤其在长上下文推理任务中优势明显，质疑线性注意力的必要性。
- **原始摘要**: arXiv:2608.28444v1 Announce Type: new Abstract: Due to the nature of quadratic attention, Large Language Models (LLMs) consume a lot of memory and energy. Every new token costs more than the previous...

### 32. Stranger, Fan, or Peer? A Systematic Study on the Role of Interlocutor in Persona-Based Dialogue Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28467
- **AI 摘要**: 系统研究对话中说话者传记可见性对基于人格对话生成的影响，区分训练、推理和评估三个阶段，发现训练时可见性比推理时更影响人格表达，并揭示复制传记文本的问题。
- **原始摘要**: arXiv:2608.28467v1 Announce Type: new Abstract: Persona-based dialogue systems are usually conditioned on speaker biography, but dialogues involve at least two participants, and who has access to whos...

### 33. Ladders in Chaos: When, How, (and Perhaps Why) Does Test-Time Scaling Improve LLM Machine Translation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28496
- **AI 摘要**: 研究测试时扩展对LLM机器翻译的影响，发现顺序采样比并行采样有更高性能上限，能提升翻译流畅性和自然度，但可能降低准确性，并初步解释其机制。
- **原始摘要**: arXiv:2608.28496v1 Announce Type: new Abstract: Two forms of test-time scaling for Large Language Models (LLMs) have emerged as effective and widely adopted paradigms: sequential, in which later answe...

### 34. A Formal Limitation on Learning Human Language From Textual Corpora
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28560
- **AI 摘要**: 从信息论角度证明，仅凭话语形式无法完全恢复说话者意图，存在不可约的不确定性，任何基于文本的表示（包括LLM）都无法超越此限制，实验支持理论结论。
- **原始摘要**: arXiv:2608.28560v1 Announce Type: new Abstract: Can a listener recover what a speaker means from the form of an utterance alone? We answer this question information-theoretically, and for a listener g...

### 35. Fast Weight Attention for Continual Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27763
- **AI 摘要**: 提出快速权重注意力用于持续学习，推导归一化一阶更新规则，包括Falcon系列变体，处理前缀预测目标下的在线学习。
- **原始摘要**: arXiv:2608.27763v1 Announce Type: cross Abstract: Recurrent fast-weight memories and selective state-space models compress an expanding context into a fixed-size recurrent state, making the state tran...

### 36. AI Alignment through a Game-theoretic Lens: A Survey
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27910
- **AI 摘要**: 综述从博弈论视角研究AI对齐，围绕偏好多样性、对齐优先级和时间动态三大挑战，分析现有方法的适用性与局限。
- **原始摘要**: arXiv:2608.27910v1 Announce Type: cross Abstract: As large language models and increasingly capable AI agents are deployed in high-risk settings, aligning them with complex human values has become a c...

### 37. AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28312
- **AI 摘要**: 研究多模态大语言模型在无保留图像情况下的身份遗忘问题。发现身份与视觉感知问题在隐藏状态中分布不同，提出AIM两阶段方法，通过锚定身份遗忘目标并匹配视觉编码器，实现身份知识抑制。
- **原始摘要**: arXiv:2608.28312v1 Announce Type: cross Abstract: Multimodal large language models (MLLMs) can memorize identity-specific facts about people in their fine-tuning data, creating privacy risks when a pe...

### 38. Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28383
- **AI 摘要**: 研究视觉Transformer注意力头，发现其分化为对象和背景专家角色，提出语义头特化指数量化此现象。基于此设计Ariadne Attention混合注意力，在22个图像视频任务上匹配全注意力性能，计算量减少6.5倍。
- **原始摘要**: arXiv:2608.28383v1 Announce Type: cross Abstract: Hybrid attention dominates frontier LLMs, yet Vision Transformers (ViTs) in multimodal LLMs lack a satisfactory hybrid design, with no consensus on wh...

### 39. Pruning Laws for Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2504.04342
- **AI 摘要**: 提出剪枝定律，建立剪枝后LLM性能与未剪枝性能和剪枝率之间的可解释缩放关系。在十个LLM、三种剪枝策略和八个任务上验证，平均外推误差小于7%，可靠预测剪枝影响。
- **原始摘要**: arXiv:2504.04342v2 Announce Type: replace Abstract: Scaling up model parameters and training data consistently improves the performance of large language models (LLMs), but at the cost of rapidly grow...

### 40. Steering Multimodal Large Language Models Decoding for Context-Aware Safety
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2509.19212
- **AI 摘要**: 针对多模态大语言模型在上下文感知安全决策上的不足，提出SafeCoDe轻量级解码框架，通过对比解码和全局感知令牌调制，动态调整生成，平衡过度敏感与不足敏感，提升安全对齐性能。
- **原始摘要**: arXiv:2509.19212v2 Announce Type: replace Abstract: Multimodal Large Language Models (MLLMs) are increasingly deployed in real-world applications, yet their ability to make context-aware safety decisi...

### 41. Think-at-Hard: Dynamic Looped Transformers for Improved Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2511.08577
- **AI 摘要**: 针对循环Transformer的潜在过度思考问题，提出Think-at-Hard方法，通过轻量神经决策器仅对可能出错的令牌触发潜在迭代，并采用深度感知LoRA优化，提升推理准确率。
- **原始摘要**: arXiv:2511.08577v4 Announce Type: replace Abstract: Improving the reasoning abilities of Large Language Models (LLMs), especially under parameter constraints, is crucial for real-world applications. L...

### 42. Learning a Single Token to Replace Long System Prompts in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2511.23271
- **AI 摘要**: 提出轻量训练框架，学习单个行为等价令牌[BE]替代长系统提示，通过重构和蒸馏保留行为效果，无需更新模型权重，实现高达3000倍压缩比并保持约98%下游性能。
- **原始摘要**: arXiv:2511.23271v2 Announce Type: replace Abstract: Long system prompts are widely used to steer Large Language Models (LLMs), but repeatedly processing them at inference time is inefficient and consu...

### 43. Tracing the complexity profiles of different linguistic phenomena through the intrinsic dimension of LLM representations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.03779
- **AI 摘要**: 探索大语言模型表示的内在维度作为语言复杂性标记，实验显示不同句法现象（如并列与从属、右分支与中心嵌入）在层间ID差异上一致反映，且峰值位置不同，表明ID可区分语言处理步骤。
- **原始摘要**: arXiv:2601.03779v3 Announce Type: replace Abstract: We explore intrinsic dimension (ID) of LLM representations as a marker of linguistic complexity. Specifically, we test whether ID differences across...

### 44. Aligning Agentic World Models via Knowledgeable Experience Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.13247
- **AI 摘要**: 提出WorldMind框架，通过知识经验学习自动构建符号世界知识库，统一过程经验与物理规则，使大语言模型智能体获得物理世界程序性知识，减少物理幻觉，避免昂贵重训练。
- **原始摘要**: arXiv:2601.13247v2 Announce Type: replace Abstract: Current Large Language Models (LLMs) exhibit a critical modal disconnect: they possess vast semantic knowledge but lack the procedural grounding to...

### 45. The Company You Keep: How LLMs Respond to Dark Triad Traits
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.04299
- **AI 摘要**: 本文研究LLM对暗黑三合一人格特质（马基雅维利主义、自恋、精神病态）用户提示的响应。发现模型普遍表现出纠正行为，但部分模型会产生强化或矛盾输出，行为随严重程度和情感变化，强调需要更安全的对话系统来检测和应对从良性到有害的请求。
- **原始摘要**: arXiv:2603.04299v5 Announce Type: replace Abstract: LLMs often exhibit highly agreeable conversational styles, also known as AI sycophancy. This pattern may become problematic when interacting with us...

### 46. Diverging Transformer Predictions for Human Sentence Processing: A Comprehensive Analysis of Agreement Attraction Effects
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.16574
- **AI 摘要**: 本文使用基于惊奇度的链接机制，系统评估了11个不同规模和架构的自回归Transformer在英语一致吸引配置上的表现。结果显示，在介词短语配置上与人类阅读时间一致，但在宾语提取关系从句配置上性能显著下降，模型间预测分歧大，无法复制人类的不对称干扰模式。
- **原始摘要**: arXiv:2603.16574v2 Announce Type: replace Abstract: Transformers underlie almost all state-of-the-art language models in computational linguistics, yet their cognitive adequacy as models of human sent...

### 47. Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.17070
- **AI 摘要**: 本文分析大型推理LLM在跨语言知识迁移中的不足，发现主要障碍是文字脚本差异而非语言或语系。回归分析显示脚本匹配是知识迁移失败的主要预测因子。提供源语言关键实体能显著改善跨脚本问题，并开发合成生成流程设计SFT样本以增强推理。
- **原始摘要**: arXiv:2603.17070v2 Announce Type: replace Abstract: In this work, we analyze shortcomings in cross-lingual knowledge transfer in large, modern reasoning LLMs. We demonstrate that the perceived gap in...

### 48. Why are all LLMs Obsessed with Japanese Culture? On the Hidden Cultural and Regional Biases of LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.21751
- **AI 摘要**: 本文提出CROQ数据集，涵盖24种语言的文化开放问题，评估LLM的文化偏见。结果显示LLM在回答中明显偏向日本等国家，高资源语言提示产生更多样输出，低资源语言则更倾向于强调本国文化，揭示了隐藏的文化和区域偏见。
- **原始摘要**: arXiv:2604.21751v2 Announce Type: replace Abstract: LLMs have limitations when it comes to cultural coverage and competence, and in some cases, show specific cultural biases. Although prior studies ha...

### 49. G-Loss: Graph-Guided Fine-Tuning of Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.25853
- **AI 摘要**: 本文提出G-Loss，一种图引导的损失函数，通过半监督标签传播和文档相似度图捕捉全局语义结构，用于微调预训练语言模型。在五个基准数据集上，G-Loss在多数实验设置中收敛更快，产生语义连贯的嵌入空间，提升了判别性和鲁棒性。
- **原始摘要**: arXiv:2604.25853v4 Announce Type: replace Abstract: Traditional loss functions, including cross-entropy, contrastive, triplet, and su pervised contrastive losses, used for fine-tuning pre-trained lang...

### 50. Do LLM Agents Mirror Socio-Cognitive Effects in Power-Asymmetric Conversations?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.17694
- **AI 摘要**: 本文研究LLM在权力不对称对话中是否表现出社会认知效应，如语言协调、代词使用、权威偏见和有害服从。通过模拟不同职业身份的多轮对话，发现LLM表现出关键的社会认知效应，但存在细微差别和变异性，将模拟互动与理想和危险行为联系起来。
- **原始摘要**: arXiv:2605.17694v3 Announce Type: replace Abstract: Power differences shape human communication through well documented socio cognitive effects, including language coordination, pronoun usage, authori...

### 51. Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.28802
- **AI 摘要**: 本文研究LLM能否学习并复现标注者特定的解释行为。通过两个句子对任务，发现标注者模式在单标注层面弱，但聚合后可检测。提出跨标注者偏好优化（CAPO），对比目标标注者响应与其他有效标注，实验显示提示方法受限，CAPO能更好学习标注者特定行为。
- **原始摘要**: arXiv:2605.28802v2 Announce Type: replace Abstract: Free-text explanations extend human label variation (HLV) beyond label disagreement by revealing the reasoning and preferences behind annotators' de...

### 52. Where Steering Signals Come From: Activation Source Selection in Activation Steering
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.25270
- **AI 摘要**: 本文研究激活引导中信号来源的选择，发现执行边界状态产生强信号，而非简单依赖源文本中目标行为是否出现。
- **原始摘要**: arXiv:2607.25270v2 Announce Type: replace Abstract: Activation steering controls language models by adding vectors or features to hidden states at inference time, but the upstream source of these stee...

### 53. A Declarative-Procedural Perspective on Expert Routing in Bilingual Mixture-of-Experts Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.15102
- **AI 摘要**: 本文研究双语混合专家模型中专家路由的语言结构，发现课程训练模型在特定层显示类别依赖路由，但无课程基线表现出更强的聚合特化。
- **原始摘要**: arXiv:2608.15102v2 Announce Type: replace Abstract: We investigate whether Mixture-of-Experts (MoE) language models develop linguistically structured expert routing during bilingual language acquisiti...

### 54. Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.23873
- **AI 摘要**: 本文提出一种名为Semantic Overlays的通用引导技术，通过在冻结模型的残差流上应用小型学习适配器，为文本跨度添加带外注释通道，以缓解提示注入攻击。该方法优于传统转向向量，可训练、可适应且选择性应用。
- **原始摘要**: arXiv:2608.23873v2 Announce Type: replace-cross Abstract: Everything a language model sees is tokens. The serving stack knows what each span is -- user input, tool output, instructions -- but the mode...

### 55. SeMoCo: A Semantic-First Motion Codec for Motion Language Modeling
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.24334
- **AI 摘要**: 本文介绍SeMoCo，一种语义优先的运动编解码器，用于语言条件运动生成。每个运动令牌包含一个语义令牌和残差运动令牌序列，并构建大规模多源人体运动数据集Ω-MotionVerse。实验表明SeMoCo在重建精度上优于其他编解码器。
- **原始摘要**: arXiv:2608.24334v2 Announce Type: replace-cross Abstract: Discrete motion representations have substantially advanced autoregressive text-to-motion generation. However, most motion tokenizers are opti...

### 56. Marginal Coverage Credit Reduces Redundant Exploration in Parallel State-Entropy Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27507
- **AI 摘要**: 本文提出MCC-PGPSE方法，通过边际覆盖信用和状态所有者专业化，为并行状态熵最大化的策略梯度算法分配非冗余探索信用，减少冗余探索，促进互补覆盖，并在多个基准测试中验证了有效性。
- **原始摘要**: arXiv:2608.27507v1 Announce Type: new Abstract: Policy Gradient for Parallel State Entropy maximization (PGPSE) expands state-space coverage by training independently parameterized policies in replica...

### 57. Beyond Non-IID: Learner--Client Distribution Mismatch in Federated Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27715
- **AI 摘要**: 本文研究联邦学习中学习者与客户端数据分布不匹配的问题，提出在学习者持有小代理数据集的情况下，理解并缓解客户端贡献差异，以改进联邦学习性能。
- **原始摘要**: arXiv:2608.27715v1 Announce Type: new Abstract: Federated learning systems are increasingly deployed to facilitate collaborative model training across a heterogeneous client population. Existing pract...

### 58. A Method for Layer Bit-Width Allocation in LLM Quantization via Performance Maximization Under a Quality-Degradation Constraint
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28003
- **AI 摘要**: 本文提出一种LLM量化层位宽分配方法，将问题建模为在质量退化约束下的性能最大化，基于层敏感性配置，在TensorRT-LLM中实现，并在RTX 5090上测量了多种变体的时钟速度。
- **原始摘要**: arXiv:2608.28003v1 Announce Type: new Abstract: This paper proposes a layer bit allocation method for Gemma-3-1B, formulating the problem as performance maximization (latency decrease) given a degrada...

### 59. When Can Conditional Flow Matching Replace Pointwise Negative Log-Likelihood?
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28010
- **AI 摘要**: 本文研究条件流匹配何时可以替代逐点负对数似然，通过线性高斯路径的精确分解，分析了CFM损失作为NLL估计的有效性条件，并指出在训练和策略对齐中的偏差问题。
- **原始摘要**: arXiv:2608.28010v1 Announce Type: new Abstract: Flow matching enables likelihood-free training, yet alignment methods increasingly reuse conditional flow matching (CFM) losses as endpoint negative log...

### 60. The Approximation Rank of Softmax Attention: Sharp Geometric Laws and Robust Interaction Dimension
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28150
- **AI 摘要**: 本文研究softmax注意力的近似秩，揭示了支持几何对秩复杂度的控制规律，并提出了鲁棒交互维度的概念，通过理论分析和BERT-base校准集验证了结果的尖锐性。
- **原始摘要**: arXiv:2608.28150v1 Announce Type: new Abstract: Which geometry controls the rank complexity of normalized softmax attention? We study maximum-row-$\ell_1$ approximation rank, exactly the least unrestr...

### 61. Biologically Inspired Mechanisms for Facilitating Grokking in Multilayer Perceptrons
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28184
- **AI 摘要**: 本文研究受生物启发的机制（如稳态、结构可塑性等）如何促进多层感知机中的“顿悟”现象（从记忆到泛化的延迟转变）。通过系统消融实验发现，稳态机制对泛化贡献最大，结构稀疏化也有帮助。
- **原始摘要**: arXiv:2608.28184v1 Announce Type: new Abstract: Grokking is a delayed transition from memorization to generalization that is often accompanied by substantial reorganization of internal representations...

### 62. Deriving Scaling Laws for OpenEuroLLM Models: Learning Rate, Batch Size and Loss
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28308
- **AI 摘要**: 本文研究OpenEuroLLM模型预训练中学习率、批量大小与损失之间的缩放规律。探讨了最优超参数随模型容量和数据规模的变化，以及学习率退火带来的收益，并评估了新的缩放形式对欠训练和过训练状态的捕捉能力。
- **原始摘要**: arXiv:2608.28308v1 Announce Type: new Abstract: We study the scaling behavior of learning rate and batch size in pretraining dense large language models on English-prevalent corpora. Beyond scaling \t...

### 63. Curvature-Conditioned Multiscale Momentum with Sphere Constraints for LLM Pretraining
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28442
- **AI 摘要**: 本文提出一种曲率条件的多尺度动量方法，结合球面约束，用于加速大语言模型预训练。该方法仅在平坦方向应用多尺度动量，结合慢衰减和快衰减分量，有效改善病态曲率问题，提升训练效率。
- **原始摘要**: arXiv:2608.28442v1 Announce Type: new Abstract: Pretraining accounts for a large fraction of the total computational cost in LLM training. However, noise-dominant gradients and the highly ill-conditio...

### 64. Blog: Survey of Optimizers
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28557
- **AI 摘要**: 本文综述了2025-2026年神经网络优化器的发展，从坐标级扩展到矩阵级和层级，从固定训练周期到时间策略，从数学更新规则到状态表示。按时间估计、更新几何、周期管理和表示系统四个独立轴组织，并讨论了矩阵感知方法的实际进展。
- **原始摘要**: arXiv:2608.28557v1 Announce Type: new Abstract: Neural-network optimization in 2025-2026 is no longer well described as a succession of new Adam variants. The design space has expanded from coordinate...

### 65. Tensor-Accelerated Eager Multi-Resolution Grids for Evolving Large-Scale Substrates
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27612
- **AI 摘要**: 本文针对神经进化中的ES-HyperNEAT方法，探讨其四叉树递归细分机制难以张量化的问题。由于深度依赖父节点方差、不同CPPN产生不同细分模式以及可变叶数不兼容JAX静态形状要求，导致JAX重实现加速有限。
- **原始摘要**: arXiv:2608.27612v1 Announce Type: cross Abstract: In neuroevolution, indirect encoding generates neural network connectivity from a compact genome rather than specifying each connection. ES-HyperNEAT...

### 66. On the Computational and Statistical Efficiency of the Empirical Maximum Entropy on the Mean Method
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27705
- **AI 摘要**: 本文研究了经验最大熵方法（MEM）的计算和统计效率，建立了期望收敛率O(n^-1/2)，优于此前O(n^-1/4)的保证。通过原始和对偶问题的稳定性分析，并将MEM对偶问题转化为期望风险最小化，使其适用于随机优化框架。
- **原始摘要**: arXiv:2608.27705v1 Announce Type: cross Abstract: The Maximum Entropy on the Mean (MEM) method provides a flexible computational framework for solving inverse problems by combining data fidelity with...

### 67. Beyond Procrustes distances: a multilinear Gromov-Wasserstein distance capturing chirality
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27774
- **AI 摘要**: 本文提出一种多线性Gromov-Wasserstein距离，能够区分形状及其镜像（手性），弥补了现有形状分析指标的不足。在温和假设下该目标构成距离，并开发了高效算法，通过将耦合投影到低维空间来优化计算。
- **原始摘要**: arXiv:2608.27774v1 Announce Type: cross Abstract: Efficiently and robustly analyzing shape data is critical across many scientific disciplines. While chirality is a fundamental property in numerous ap...

### 68. Localizing Global Discrepancies: Marginal Contributions and Contextual Anomaly Detection
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28375
- **AI 摘要**: 本文开发了一个框架，通过为每个观测分配其在随机统计上下文中的条件或边际贡献，来定位全局差异的来源。该框架连接了重采样诊断、数据估值和事件级异常检测，并提供了更高效的估计器。
- **原始摘要**: arXiv:2608.28375v1 Announce Type: cross Abstract: Global goodness-of-fit and discrepancy statistics can establish that a sample departs from a reference distribution without identifying which observat...

### 69. Quantum Federated Learning Based on Bures--Uhlmann Geometry for Heterogeneous Noisy Clients
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28379
- **AI 摘要**: 本文提出基于Bures-Uhlmann几何的量子联邦学习方法，针对异构噪声客户端。利用混合态的Bures度量作为局部预条件器，并通过平均Uhlmann曲率开发可达到精度的聚合规则，以处理参数不兼容性和噪声影响。
- **原始摘要**: arXiv:2608.28379v1 Announce Type: cross Abstract: Quantum federated learning enables collaborative model training across quantum devices without sharing raw data, and it faces the data and hardware he...

### 70. Diffusion models as plug-and-play priors
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2022年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2206.09012
- **AI 摘要**: 本文提出将扩散模型作为即插即用先验，通过迭代微分固定去噪网络进行近似推断，以解决高维数据推断问题，可应用于条件生成、图像分割等新领域和任务。
- **原始摘要**: arXiv:2206.09012v4 Announce Type: replace Abstract: We consider the problem of inferring high-dimensional data $\mathbf{x}$ in a model that consists of a prior $p(\mathbf{x})$ and an auxiliary differe...

### 71. Attention as Conditioning: What Classical Learning Theory Predicts About Linear Transformers
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2508.08289
- **AI 摘要**: 本文揭示了线性注意力家族的状态更新与动物学习理论模型一一对应，如线性注意力实现Hebbian邻近性，DeltaNet实现Rescorla-Wagner误差修正，从而将条件作用现象转化为对线性Transformer上下文行为的可测试预测。
- **原始摘要**: arXiv:2508.08289v3 Announce Type: replace Abstract: Attention is widely understood as an associative memory, but that description alone does not predict how the memory will behave. Predictive theories...

### 72. Large Reasoning Models Learn Better Alignment from Flawed Thinking
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2510.00938
- **AI 摘要**: 本文提出RECAP方法，一种基于强化学习的后训练方法，通过训练模型覆盖有缺陷的推理轨迹并重路由到安全响应，提高安全性和越狱鲁棒性，减少过度拒绝，同时保持推理能力。
- **原始摘要**: arXiv:2510.00938v3 Announce Type: replace Abstract: Large reasoning models (LRMs) "think" by generating structured chain-of-thought (CoT) before producing a final answer, yet they still lack the abili...

### 73. Aspiration-based Perturbed Learning Automata in Games with Noisy Utility Measurements. Part A: Stochastic Stability in Non-zero-Sum Games
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2511.11602
- **AI 摘要**: 本文提出基于抱负的扰动学习自动机（APLA），一种新的基于收益的学习方案，用于多玩家弱非循环博弈中的分布式优化，解决标准强化学习在非势博弈和协调博弈中无法保证收敛到纯纳什均衡的问题。
- **原始摘要**: arXiv:2511.11602v3 Announce Type: replace Abstract: Reinforcement-based learning has attracted considerable attention both in modeling human behavior as well as in engineering, for designing measureme...

### 74. InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.18031
- **AI 摘要**: 本文提出InfoMamba，一种无注意力混合架构，用概念瓶颈线性过滤层替代token级自注意力，并通过信息最大化融合与选择性循环流集成，以平衡局部建模和长程依赖捕获，提高序列建模效率。
- **原始摘要**: arXiv:2603.18031v2 Announce Type: replace Abstract: Balancing fine-grained local modeling with long-range dependency capture under computational constraints remains a central challenge in sequence mod...

### 75. More Expressive Feedforward Layers: Part I. Token-Adaptive Mixing of Activations
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.26647
- **AI 摘要**: 本文提出Mixture of Activations（MoA）和可学习激活（LA）两种前馈网络设计，通过输入依赖门控混合激活函数，理论上证明MoA严格包含LA，LA严格包含固定激活FFN，提升表达力。
- **原始摘要**: arXiv:2605.26647v2 Announce Type: replace Abstract: Feedforward network (FFN) layers account for a large fraction of parameters and nonlinear expressivity in Transformer-based large language models (L...

### 76. Negligible in Size, Significant in Effect: On Scale Vectors in Large Language Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.26895
- **AI 摘要**: 本文系统研究LLM中归一化层的尺度向量，发现其虽参数占比极小但对预训练至关重要，理论上证明尺度向量不增加表达力，而是通过自放大预条件效应改善优化，并探讨了权重衰减的作用。
- **原始摘要**: arXiv:2605.26895v2 Announce Type: replace Abstract: Normalization layers in modern large language models (LLMs) consist of a deterministic normalization operation and a learnable scale vector. While t...

### 77. SpecGradFilter: A Spectral Gradient Filtering Framework for Taming Federated Heterogeneity
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.04189
- **AI 摘要**: 本文提出SpecGradFilter框架，从频域角度分析联邦学习中的客户端漂移问题，发现漂移主要集中于低频分量，通过抑制不一致的低频信号来提升联邦学习的全局收敛性能。
- **原始摘要**: arXiv:2607.04189v2 Announce Type: replace Abstract: Federated Learning (FL) is fundamentally challenged by statistical heterogeneity, where non-identically distributed (non-IID) data induces client dr...

### 78. On the Depth Scalability of Logic Gate Networks
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.21633
- **AI 摘要**: 本文研究逻辑门网络的深度扩展性，指出优化崩溃和拓扑导致的梯度退化问题，提出输入锚定逻辑门网络（IALGN），通过每个门结合私有隐藏脊和直接输入锚点，实现高达150层的稳定深度扩展。
- **原始摘要**: arXiv:2607.21633v3 Announce Type: replace Abstract: Logic Gate Networks (LGNs) compute through compositions of Boolean operations, yet existing LGNs do not reliably benefit from increased depth. We id...

### 79. RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.22849
- **AI 摘要**: 本文介绍RIBOSPAN，一个16.1亿参数的RNA基础模型，原生支持长达10240个核苷酸的上下文，结合双向自注意力、单核苷酸标记化和注意力隔离序列打包，实现全长RNA的高分辨率建模。
- **原始摘要**: arXiv:2608.22849v2 Announce Type: replace Abstract: Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-t...

### 80. Off the Normal Path: Learning Spatial Density Models of Node Mobility
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2024年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2411.10997
- **AI 摘要**: 本文研究移动节点空间密度模型的学习，引入Möbius分布来保留对称空间关系，实验表明混合Möbius分布提供可解释、简洁的模型，在稳态密度分布描述上优于现有方法。
- **原始摘要**: arXiv:2411.10997v2 Announce Type: replace-cross Abstract: We consider the problem of learning models of spatial density functions, representing the steady-state density of mobile nodes moving on a two...

### 81. Online Learning-to-Defer with Varying Experts
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.12340
- **AI 摘要**: 本文提出一种在线多类学习延迟算法，结合查询动作赌博反馈和动态变化的专家池，在流式数据、专家可用性和可靠性变化场景下，实现期望真实延迟遗憾的优化，并通过在线H一致性转移和投影在线凸优化分析验证。
- **原始摘要**: arXiv:2605.12340v5 Announce Type: replace-cross Abstract: Learning-to-Defer (L2D) methods route each query either to a predictive model or to external experts. Real-world deployments require handling...

### 82. An End-to-End Hybrid Quantum--Classical Sampling Workflow for Discrete Markov Random Fields: A Reproducible Case Study
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.09893
- **AI 摘要**: 本文研究离散马尔可夫随机场的端到端混合量子-经典采样工作流，通过振幅编码和经典预计算，对比量子采样器与经典MCMC方法，发现经典采样器在有效样本量和墙钟时间上均优于量子方法，无量子加速优势。
- **原始摘要**: arXiv:2607.09893v2 Announce Type: replace-cross Abstract: Sampling from discrete Markov random fields (MRFs) is a hard problem. We study amplitude-encoded i.i.d. sampling for small MRFs where $2^n$ ta...

### 83. Robust Chance-Constrained Optimization using a Continuous Parameter Space Wasserstein-2 Ambiguity Set of Gaussian Mixtures
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.17018
- **AI 摘要**: 本文提出一种基于高斯混合模型连续参数空间Wasserstein-2模糊集的鲁棒机会约束优化方法，利用Bures-Wasserstein度量构建模糊集，允许最坏情况分布内生决定混合分量权重，克服有限支撑分布鲁棒公式的局限性。
- **原始摘要**: arXiv:2607.17018v2 Announce Type: replace-cross Abstract: We study distributionally robust linear chance-constrained problems in which uncertainty is modeled by a Gaussian mixture model (GMM). Finite-...

### 84. Beyond Data Scaling: Representation-Centric Continued Pre-training for Vision-Language-Action Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27550
- **AI 摘要**: 提出VLAct框架，一种面向VLA模型的以表征为中心的持续预训练方法，在有限机器人数据下通过保留VLM先验和多头动作协同监督，提升跨具身动作语义共享和迁移能力。
- **原始摘要**: arXiv:2608.27550v1 Announce Type: new Abstract: Scaling robot data is crucial for building generalist Vision-Language-Action (VLA) models, yet robot trajectories are harder to scale than web-scale ima...

### 85. PHR-VLA: Planning Horizon Reasoning for Vision-Language-Action Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.27609
- **AI 摘要**: 提出PHR-VLA框架，通过特权潜在未来动态表征实现VLA模型的规划视野推理，引入轻量级辅助未来头，在训练中对齐内部表征与未来观测，提升精细操作任务成功率。
- **原始摘要**: arXiv:2608.27609v1 Announce Type: new Abstract: Vision-language-action models (VLAs) have shown strong promise for general-purpose robotic manipulation by mapping language instructions and vision obse...

### 86. DeicticVLA: Unifying Instruction Modes Based on Language and Deictic Gestures in a Single VLA
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年08月 (约 17 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.28108
- **AI 摘要**: 提出DeicticVLA，将语言指令、视觉语言指令和视觉指令统一为文本提示和指示掩码，通过文本提示完成和指示手势接地，使单个预训练VLA能处理三种指令模式。
- **原始摘要**: arXiv:2608.28108v1 Announce Type: new Abstract: Vision-Language-Action models (VLAs) allow users to specify manipulation tasks in natural language, but distinguishing a target or placement goal among...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
