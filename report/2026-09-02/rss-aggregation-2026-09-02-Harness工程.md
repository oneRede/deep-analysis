# RSS 聚合报告 - Harness工程

**生成时间**: 2026-09-03 10:15:49
**文章数量**: 114 篇

---

### 1. 还在为大模型洗数据熬夜？蚂蚁拿下VLDB工业最佳论文，一套宽表搞定35PB语料，效率狂飙5.6倍
- **来源**: 量子位 (TIER3)
- **发布日期**: Wed, 02 Sep 2026 06:20:17 +0000 (昨天)
- **类型**: news
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.qbitai.com/2026/09/483104.html
- **AI 摘要**: 蚂蚁集团研发的统一宽表系统OmniTable获VLDB 2026工业赛道最佳论文，该系统管理超35PB、3050亿条大模型训练数据。OmniTable采用逻辑统一、物理分离的设计，将数据组织为逻辑宽表，通过Catalog管理特征和血缘，支持列级依赖解析和记录级故障隔离。在真实SFT任务中，端到端周期从14天缩短至2.5天，手工步骤从45步降至12步，显著提升数据准备效率。
- **原始摘要**: 蚂蚁集团推出统一宽表系统OmniTable，论文获评VLDB 2026工业赛道最佳论文

### 2. Most open-source AI detectors can't hold a 0.5% false-positive rate [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-09-02T12:04:39+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w58erw/most_opensource_ai_detectors_cant_hold_a_05/
- **AI 摘要**: 本文指出大多数开源AI检测器无法将误报率控制在0.5%以下。AI检测器常用于识别AI生成的内容（如文本、图像）。文章可能通过测试多个开源检测器，发现它们在保持低误报率方面表现不佳，这可能导致误判人类内容为AI生成。该问题对内容审核、学术诚信等领域有重要影响。发布在Reddit上，可能引发对AI检测技术可靠性的讨论。
- **原始摘要**: We needed to know where the open-source AI-detection field actually stands, so we ran every notable open detector through the same protocol. Setup: - Public data only: Jabarian & Imas 2025 (NBER), Lia...

### 3. What kinds of ML bottlenecks are a good fit for Triton? [Manning giveaway] [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-09-02T12:02:59+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1w58dib/what_kinds_of_ml_bottlenecks_are_a_good_fit_for/
- **AI 摘要**: 本文讨论哪些类型的机器学习瓶颈适合使用Triton（一种GPU编程语言）来解决。文章可能列举了计算密集、内存访问模式复杂或需要自定义内核的场景，并说明Triton如何简化开发并提升性能。内容可能面向ML工程师，提供实用建议。文章还提到Manning赠书活动，可能作为推广。发布在Reddit上，可能引发关于GPU编程工具选择的讨论。
- **原始摘要**: Hi r/MachineLearning, Stjepan from Manning here, posting with the mods’ permission. We’ve recently released GPU Programming with Triton by Harshwardhan Fartale in early access. It’s a practical guide...

### 4. Researchers easily trick Fortune-500 companies' AI agents into running arbitrary code — supply-chain attack via llms.txt guidance file illustrates how data has become code
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 02 Sep 2026 10:20:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-easily-trick-fortune-500-companies-ai-agents-into-running-arbitrary-code-supply-chain-attack-via-llms-txt-guidance-file-illustrates-how-data-has-become-code
- **AI 摘要**: 研究人员利用llms.txt引导文件对多家财富500强公司的AI代理发起供应链攻击，成功诱导其执行任意代码。该研究揭示了AI代理信任数据文件的安全隐患，表明数据正成为代码执行的一部分，凸显了AI系统安全防护的紧迫性。
- **原始摘要**: Researchers easily trick Fortune-500 companies' AI agents into running arbitrary code. This supply-chain attack, done via using data in public llms.txt guidance files, illustrates the dangers of data...

### 5. When Edge AI Lies: Fault Injection and False State in Live Perception Pipelines
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Wed, 02 Sep 2026 07:02:10 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/fault-injection-and-false-state-in-live-perception-pipelines/
- **AI 摘要**: 本文由Keysight发布，研究边缘AI系统中的故障注入和虚假状态问题。文章指出边缘AI系统在摄像头、机器人等设备中实时决策，但持续运行不代表感知可信。研究针对商业边缘AI感知管线进行故障注入，使用Rockchip RK3568平台运行YOLOv5s_ReLU模型，通过在NPU电源轨上注入精确的电压毛刺，并利用电磁测量映射执行时间线，发现模型执行后期（颈部/头部阶段）是最有效的攻击窗口，可能导致系统静默接受错误环境视图。
- **原始摘要**: In edge AI, the most dangerous failure may not be a system that stops working, but one that continues operating while quietly accepting the wrong version of reality. The post When Edge AI Lies: Fault...

### 6. The Evolution Of Intelligent Systems: From Optimization To Automation to AI
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Wed, 02 Sep 2026 07:01:59 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/the-evolution-of-intelligent-systems-from-optimization-to-automation-to-ai/
- **AI 摘要**: 本文由Siemens EDA撰写，探讨智能系统从优化到自动化再到AI的演进。文章指出传统信号和电源完整性分析方法已不足，需转向集成系统以增强决策、执行和适应性。文章以HyperLynx平台为参考，将这一转变框架化为优化、自动化和AI三个相互关联的领域，强调工程方法论正朝着更集成和智能的方向发展。
- **原始摘要**: Engineering methodologies are evolving toward more integrated and intelligent approaches across three interconnected domains: optimization, automation, and AI. The post The Evolution Of Intelligent Sy...

### 7. Security Sign-Off Is Coming For Chips — But Standards May Not Be Enough
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Wed, 02 Sep 2026 07:01:38 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/security-sign-off-is-coming-for-chips-but-standards-may-not-be-enough/
- **AI 摘要**: 本文是半导体工程圆桌讨论的摘录，探讨芯片安全签核的必然性。文章指出随着AI驱动的密码分析、后量子密码迁移、芯粒和定制硅扩大攻击面，半导体安全正从孤立防护转向全栈验证。专家认为安全签核必须务实、分层并集成到现有设计流程中。行业向异构系统、定制AI硬件和碎片化标准发展，使得端到端芯片和系统安全更难定义、验证和执行。
- **原始摘要**: As AI, post-quantum cryptography, chiplets, and custom silicon expand the attack surface, semiconductor security is shifting from isolated safeguards to full-stack verification. The post Security Sign...

### 8. Distributed Implicit Harm: A Compositional Safety Blind Spot in MLLM-Based Video Moderation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00206
- **AI 摘要**: 本文揭示多模态大模型在视频审核中的组合安全盲点——分布式隐式危害，即由看似无害组件组合产生的有害含义。研究了时间分布和跨模态两种类型，并开发多智能体合成方法生成数据以缓解该问题。
- **原始摘要**: arXiv:2609.00206v1 Announce Type: new Abstract: Despite their growing use in video moderation, multimodal large language models (MLLMs) exhibit a compositional safety blind spot: videos composed of se...

### 9. Beyond Language Priors: Diagnosing and Fixing Visual-Origin Hallucinations in Multimodal LLM
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00231
- **AI 摘要**: 本文挑战了多模态大模型对象幻觉主要源于语言先验的观点，提出视觉来源幻觉，源于视觉特征提取错误和图文嵌入不对齐。通过诊断分析，提出对抗对比微调方法，利用对抗性幻觉属性翻转来修复该问题。
- **原始摘要**: arXiv:2609.00231v1 Announce Type: new Abstract: Existing research on object hallucination in multimodal large language models (MLLMs) predominantly attributes the problem to language priors such as ov...

### 10. Beyond Blind Compliance: Benchmarking Task Verification in OCR Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00232
- **AI 摘要**: 本文研究OCR推理中的任务验证问题，提出VeriOCRBench基准，包含1800个样本和1600个陷阱注入的无效任务。模型需先判断图像前提、文本前提和问题是否共同构成可执行任务，弥补现有评估假设所有任务有效的缺陷。
- **原始摘要**: arXiv:2609.00232v1 Announce Type: new Abstract: Multimodal Large Language Models (MLLMs) have achieved strong performance on OCR-centric document understanding and text-rich visual reasoning benchmark...

### 11. Separating perception from reasoning in vision-language models: a model-free render ceiling for crystal structures
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00663
- **AI 摘要**: 本文引入渲染天花板（render ceiling）作为无模型参考，用于分离视觉语言模型中的感知与推理错误。通过逆向相机和重解跨视角对应，证明在2160个晶体结构上模型缺陷完全归因于模型自身，并揭示提取阶段的伪造问题。
- **原始摘要**: arXiv:2609.00663v1 Announce Type: new Abstract: Multimodal evaluations cannot say whether a vision-language model misread an image or misreasoned about it, because every existing method for separating...

### 12. Visual Attention Faithfulness in Vision-Language Models is Heterogeneous
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00830
- **AI 摘要**: 通过因果扰动分析，发现视觉语言模型中的视觉注意力忠实度具有异质性，表现为三种模式：忠实充分、忠实分布和非焦点。人类标注区域仅在约60%情况下满足充分性，表明模型推理与注意力存在差异。
- **原始摘要**: arXiv:2609.00830v1 Announce Type: new Abstract: Whether attention weights faithfully reflect model reasoning has been actively debated in NLP, yet this question remains largely unexplored for the visu...

### 13. Benchmarking Vision-Language Models for Automated Pathology Diagnosis and Report Generation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00866
- **AI 摘要**: 本文引入泛亚全切片图像-报告数据集（约10500对）并建立REG 2025基准，系统评估多种多模态模型。结果表明，结构化报告表示和层次化专家模型等设计比单纯使用视觉语言模型更有效。
- **原始摘要**: arXiv:2609.00866v1 Announce Type: new Abstract: The rapid advancement of vision-language models (VLMs) has accelerated progress in computational pathology; however, whole-slide image (WSI)-based patho...

### 14. Fi-ImageNet-1k: An OOD Benchmark From the Inside of the ImageNet-1k Validation Set
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01027
- **AI 摘要**: Fi-ImageNet-1k是一个从ImageNet-1k验证集内部构建的分布外检测基准，包含655张来自522个类别的图像，经专家人工标注和多模型证据验证，比常见OOD基准更具挑战性。
- **原始摘要**: arXiv:2609.01027v1 Announce Type: new Abstract: Out-of-distribution (OOD) detection predicts whether a test image belongs to none of the predefined classes. To evaluate this task, benchmarks need imag...

### 15. Compressing AI Traffic: Standardized Neural Network Coding of Visual-Token Representations in Split Vision-Language Inference
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01200
- **AI 摘要**: 本文研究在分离式视觉语言推理中，使用标准化神经网络编码（NNC）压缩视觉token嵌入（AI流量）。实验表明，在Qwen3-VL-8B上可压缩高达98%的BF16张量而保持精度，之后性能才崩溃。
- **原始摘要**: arXiv:2609.01200v1 Announce Type: new Abstract: When the visual encoder and the language decoder of a vision-language model (VLM) run on different compute nodes, the intermediate visual-token embeddin...

### 16. ExBind: A Controlled Diagnostic Benchmark for Visual-to-Executable Correspondence
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01344
- **AI 摘要**: 介绍ExBind，一个受控诊断基准，用于评估多模态编码和编辑系统中视觉到可执行对象的对应关系。它隔离语义定位与动作执行层，通过确定性映射生成SVG、DOM等案例，并仅要求模型输出严格引用以进行结构约束评分。
- **原始摘要**: arXiv:2609.01344v1 Announce Type: new Abstract: Multimodal coding and editing systems must map a visible or semantic referent to the exact executable object that can be edited. A wrong reference may s...

### 17. HarnessEval-W: Agentifying the Evaluation of Visual Worlds
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 19 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.16859
- **AI 摘要**: 介绍HarnessEval-W，一种智能体化的世界模型评估流水线，将LLM生态的harness范式引入世界模型基准测试。通过分解评估问题并生成专业子智能体，提供可验证的推理链。
- **原始摘要**: arXiv:2608.16859v2 Announce Type: replace Abstract: A benchmark should deliver more than a scalar score: what makes an evaluation trustworthy is the reasoning that justifies the score. This is especia...

### 18. [AI Ecosystem] The real bottleneck: Data, not compute
- **来源**: SK hynix Newsroom (TIER1)
- **发布日期**: Wed, 02 Sep 2026 23:59:52 +0000 (今天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://news.skhynix.com/en/ai-ecosystem-series-ep2/
- **AI 摘要**: 随着AI工作负载向推理和智能体AI演进，系统性能标准正在改变。算力不再是唯一瓶颈，数据存储位置、移动速度和高效处理能力成为新的关键因素。
- **原始摘要**: As AI workloads evolve toward inference and agentic AI, the criteria for system performance are also changing. Computing power alone is no longer enough. Where data is stored, how quickly it moves, an...

### 19. trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00038
- **AI 摘要**: 研究LLM智能体评估中仅看结果的盲区，通过故障注入实验比较多种评估器，发现结果导向评估器漏检静默故障，步骤评估器更优。
- **原始摘要**: arXiv:2609.00038v1 Announce Type: new Abstract: Outcome-only evaluation is the production default for LLM agents: show a judge the request and the final reply and ask whether it was handled well. The...

### 20. RePro: Proof-Verified Benchmark Rewriting for Reliable Evaluation of LLM Mathematical Problem Solving
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00062
- **AI 摘要**: 提出RePro框架，集成Lean定理证明器到基准改写中，确保数学问题改写后的有效性和答案正确性，用于可靠评估LLM。
- **原始摘要**: arXiv:2609.00062v1 Announce Type: new Abstract: Data contamination undermines the reliable evaluation of large language models (LLMs) on mathematical problem solving. While rewriting-based evaluation...

### 21. Medical Causal Hypothesis Verification with Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00063
- **AI 摘要**: 初步研究评估LLM验证医学因果假设并用同行评审文献支撑的能力，提出系统评估框架，测试八个LLM在17个假设上的表现。
- **原始摘要**: arXiv:2609.00063v1 Announce Type: new Abstract: The growing use of large language models (LLMs) for search and information retrieval underscores the need to evaluate their reliability in high-stakes d...

### 22. Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00077
- **AI 摘要**: 诊断代码级自主研究循环中的算法模式坍缩，发现表面编辑多样性稳定但语义多样性崩溃，影响泛化能力。
- **原始摘要**: arXiv:2609.00077v1 Announce Type: new Abstract: Code-level autonomous research loops (ARLs) have recently emerged as a concrete object of study in automated machine learning research. In such loops, a...

### 23. Do General NLP Embeddings Capture Ontological Reasoning?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00177
- **AI 摘要**: 引入AVA框架评估NLP嵌入模型对本体论推理的捕捉能力，发现现有模型在逻辑敏感关系上表现有限，最佳模型准确率仅0.739，硬负例准确率低至0.135，微调虽提升但迁移性差。
- **原始摘要**: arXiv:2609.00177v1 Announce Type: new Abstract: General-purpose NLP embedding models perform well on linguistic tasks, but their ability to capture symbolic ontological structure remains unclear. We i...

### 24. Synthetic Worlds for Temporal Evaluation and Knowledge Updating in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00184
- **AI 摘要**: 提出合成世界框架ParallelEvents和Synapse训练框架，用于评估和更新LLM知识，避免污染并保持一致性。Synapse通过模型生成数据实现可扩展知识集成，性能提升14.23%。
- **原始摘要**: arXiv:2609.00184v1 Announce Type: new Abstract: Large language models (LLMs) rely on static pretraining corpora, causing their knowledge to become outdated over time. Existing approaches for evaluatin...

### 25. Toward Workflow-Aware Benchmarking for Healthcare NLP Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00296
- **AI 摘要**: 针对医疗NLP智能体的评估多局限于静态问答，本文提出基于情节的评估协议，区分模型、智能体和模拟工作流行为，定义状态连续性、证据可追溯性和升级决策的评分，提供可复现的中间评估层。
- **原始摘要**: arXiv:2609.00296v1 Announce Type: new Abstract: Large language model (LLM) agents are increasingly proposed for healthcare tasks such as clinical documentation, evidence retrieval, patient messaging,...

### 26. Topic Matching in the Wild: Benchmark and Lessons from Real-World ASR Transcripts
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00330
- **AI 摘要**: 针对呼叫中心实时助手任务，构建了真实ASR转录的主题-话语匹配基准，比较正则、嵌入和LLM匹配器，发现轻量LLM匹配器在自然语言描述下性能最优。
- **原始摘要**: arXiv:2609.00330v1 Announce Type: new Abstract: In contact centers, real-time agent-assist tools determine, for each of many predefined topics, whether a live customer utterance is relevant and displa...

### 27. Detecting Hidden Behaviors in LLMs via Activation-matched Finetuning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00351
- **AI 摘要**: 提出激活匹配微调的无监督方法，检测LLM中隐藏行为（如后门、沙袋效应）。通过微调公开锚模型复现可疑模型激活，计算残差识别触发提示及其语义邻居。
- **原始摘要**: arXiv:2609.00351v1 Announce Type: new Abstract: Large language models can hide hidden behaviors that activate only under narrow conditions, such as backdoor triggers, sleeper-agent deployment cues, sa...

### 28. Neurosymbolics for Data Engineering: Achieving Long Context Token Reduction Without Finetuning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00367
- **AI 摘要**: 提出一种神经符号层，集成到LLM骨干中提升逻辑推理并缓解长上下文计算瓶颈。无需微调即可在BIRD-CRITIC等基准上平均提升85%准确率，同时降低二次复杂度。
- **原始摘要**: arXiv:2609.00367v1 Announce Type: new Abstract: Large Language Models are increasingly deployed for sophisticated data engineering tasks such as generating structured queries from natural language, Te...

### 29. TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00470
- **AI 摘要**: 提出TRIS三层检索完整性筛，作为中间件防御RAG系统中的知识投毒攻击。通过跨嵌入空间聚类、结构过滤和LLM一致性验证，利用投毒文档需同时满足多种约束的脆弱性，有效降低攻击成功率。
- **原始摘要**: arXiv:2609.00470v1 Announce Type: new Abstract: Retrieval-Augmented Generation (RAG) grounds large language models in external corpora, but implicit trust in retrieved documents creates a critical att...

### 30. Are Near-Tied LLM Rankings Robust to Family-DIF-Guided Benchmark Recomposition?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00482
- **AI 摘要**: 研究基准测试项目组成对LLM排名的影响。使用无标签谱近似MIRT识别低DIF项目，发现近并列的跨模型对在低DIF子测试中排名反转比例显著高于随机子测试，质疑小差距排名的稳健性。
- **原始摘要**: arXiv:2609.00482v1 Announce Type: new Abstract: Small leaderboard gaps are often interpreted as evidence that one language model is better than another, but their sign may depend on which benchmark it...

### 31. EvoFlint: An Evolutionary Atlas of Multi-Turn LLM Vulnerabilities
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00487
- **AI 摘要**: 提出EvoFlint，将多轮LLM红队攻击视为搜索问题而非生成问题。采用进化质量多样性搜索，演化分阶段对话计划，通过帕累托适应度和风险索引档案生成多样化的攻击策略图谱。
- **原始摘要**: arXiv:2609.00487v1 Announce Type: new Abstract: Frontier language models that refuse harmful single-turn prompts often comply when the same intent is reached gradually over many turns, making multi-tu...

### 32. Human-Anchored Factuality Evaluation with Strategic Annotation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00494
- **AI 摘要**: 研究有限标注预算下以人类为锚的事实性评估。提出基于失败空间分析的标注策略设计流程，利用结构化失败模式预测人机判断不一致，结合选择性采样获得统计有效且无偏的评估结果。
- **原始摘要**: arXiv:2609.00494v1 Announce Type: new Abstract: LLM-based factuality judges provide scalable evaluation signals, but their metrics are often systematically biased relative to human judgments. We study...

### 33. Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00549
- **AI 摘要**: 提出技能跟随概念和RAE指标，评估检索增强LLM代理中技能实际使用效果。发现模型常出现正向聚合检索提升但负向RAE的矛盾现象，揭示评估悖论。
- **原始摘要**: arXiv:2609.00549v1 Announce Type: new Abstract: Large Language Model (LLM) agents increasingly rely on external skills, yet standard evaluations obscure whether retrieving these skills actually helps....

### 34. Enoki: Efficient Multi-Level Hallucination Detection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00581
- **AI 摘要**: 提出Enoki开放信息抽取框架，用于多层级幻觉检测。通过共享表示实现声明级验证和跨度级定位，支持多种抽取机制，平衡准确性和推理成本。
- **原始摘要**: arXiv:2609.00581v1 Announce Type: new Abstract: Ensuring factuality remains a critical challenge for deploying LLMs in high-stakes settings. Existing hallucination detectors usually operate at a singl...

### 35. Investigating Assistant Bias in LLM User Simulators Using a Role Vector
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00608
- **AI 摘要**: 研究LLM用户模拟器中的助手偏见，通过角色向量分析激活差异。发现用户方向可识别且能引发用户行为，但过度强化可能夸大用户行为。
- **原始摘要**: arXiv:2609.00608v1 Announce Type: new Abstract: LLM-based user simulators are increasingly used to evaluate autonomous agents at scale, in place of costly human evaluations. Despite this promise, thes...

### 36. Trust Your Guide Only When Certain: Uncertainty-Aware Sparse Alignment at Inference Time
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00624
- **AI 摘要**: 提出TUSA方法，基于不确定性的稀疏对齐。通过仲裁机制仅在监督器自信且标记语义显著时干预，过滤噪声和冗余监督，提升推理时对齐效果。
- **原始摘要**: arXiv:2609.00624v1 Announce Type: new Abstract: A prominent paradigm in inference-time alignment employs lightweight supervisors to steer Large Language Models (LLMs). Through empirical analysis, we i...

### 37. SCoNE: Selective Context-aware Neuron Editing for Robust Retrieval-Augmented Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00689
- **AI 摘要**: 提出SCoNE选择性上下文感知神经元编辑方法，无需训练即可增强RAG对检索噪声的鲁棒性。通过强化高归因和高跨输入变异的FFN神经元，提升问答性能。
- **原始摘要**: arXiv:2609.00689v1 Announce Type: new Abstract: Retrieval-Augmented Generation (RAG) is highly sensitive to retrieval noise: when retrieved documents mix informative and irrelevant context, LLMs are e...

### 38. Compile, Don't Memorize: A Context Compilation Architecture (CCA) for In-Context Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00759
- **AI 摘要**: 本文提出上下文编译架构（CCA），通过类型化中间表示显式编译上下文，解决大模型在长上下文学习中的脆弱性问题。实验显示该方法优于现有长上下文策略，提升了任务完成率。
- **原始摘要**: arXiv:2609.00759v1 Announce Type: new Abstract: Large language models (LLMs) increasingly handle in-context learning (ICL) tasks where a long, novel context defines the rules, knowledge, and output sc...

### 39. SFAD: Speculative Factuality-Aware Decoding
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00796
- **AI 摘要**: 本文提出SFAD投机解码框架，通过训练上下文忠实草稿模型和推理时检测机制，在不降低推理效率的前提下提升大模型的事实一致性，解决了对比解码计算开销大的问题。
- **原始摘要**: arXiv:2609.00796v1 Announce Type: new Abstract: As one of the most critical challenges in large language models, contextual faithfulness directly determines their reliability in knowledge-intensive ap...

### 40. Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00925
- **AI 摘要**: 本文审计GRPO、SFT和DPO等后训练方法对上下文遵循能力的影响，发现多数方法增益有限，DPO效果最好，且增益主要依赖已有机制而非新机制。
- **原始摘要**: arXiv:2609.00925v1 Announce Type: new Abstract: Language models can ignore prompt evidence when it conflicts with memorized knowledge. Post-training can make models follow such evidence more reliably,...

### 41. Calibration is the Bottleneck: An Action-Class Diagnostic of Multi-Turn Tool-Calling
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00949
- **AI 摘要**: 提出一种面向多轮工具调用的动作类诊断框架，将失败分解为动作类校准错误和执行失败两种模式，并引入自揭示上界Acc≤GAR来识别状态评分器掩盖的校准问题，以评估开放权重模型与闭源前沿模型的性能差距。
- **原始摘要**: arXiv:2609.00949v1 Announce Type: new Abstract: Multi-turn tool calling is a core evaluation scenario for large language model (LLM) agents. On public tool-calling benchmarks, open-weight models now a...

### 42. Disclosure-Gated User Simulation for Companion-Agent Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00982
- **AI 摘要**: 提出一种基于披露门控的用户模拟器，用于同伴智能体评估。通过五级门控阶梯控制信息释放，训练模拟器学习门控行为，解决模拟用户过度合作导致评估失真的问题，并在CompanionBench基准上验证。
- **原始摘要**: arXiv:2609.00982v1 Announce Type: new Abstract: Using a large language model to play the user is now standard in scalable evaluation. It has a repeatedly diagnosed failure: the simulated user is exces...

### 43. PCoMoE: Shifting MoE Inference from Monolithic Expert Selection to Fine-Grained Path Composition
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01024
- **AI 摘要**: 提出PCoMoE，一种路径组合执行框架，将MoE推理从粗粒度专家选择转变为细粒度路径组合，包含路径级公式、兼容性感知层剪枝和硬件友好执行引擎，以利用子专家结构并降低计算冗余。
- **原始摘要**: arXiv:2609.01024v1 Announce Type: new Abstract: Mixture-of-Experts (MoE) architectures scale Large Language Model (LLM) capacity efficiently by activating a sparse subset of experts per token. However...

### 44. OUTLETS: Output-Length Prediction from Speculative Decoding Backbones
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01068
- **AI 摘要**: 提出OUTLETS方法，利用投机解码骨干（如EAGLE-3）的草稿表示预测LLM输出长度，无需外部代理模型，实现高效且高保真的长度预测，以改善资源供应和集群调度。
- **原始摘要**: arXiv:2609.01068v1 Announce Type: new Abstract: The heavy-tailed distribution of output lengths in Large Language Model (LLM) serving poses major challenges for resource provisioning and cluster sched...

### 45. Post-hoc Alignment of LLM-judges to Human Judgment Distribution
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01073
- **AI 摘要**: 研究LLM作为评判者（LLMaJ）在预测聚合硬标签和人类判断分布软标签上的表现，发现硬标签接近人类水平但软标签较差，提出轻量级事后对齐方法NAPHA，通过熵感知融合匹配人类判断分布。
- **原始摘要**: arXiv:2609.01073v1 Announce Type: new Abstract: The LLM-as-a-judge (LLMaJ) framework offers a cost-effective and reproducible solution for automatic evaluation. However, current evaluation practices t...

### 46. ClinTraceBench: Source-Verifiable Longitudinal Clinical Reasoning over EHR-Derived Dialogues
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01111
- **AI 摘要**: 本文介绍ClinTraceBench基准，用于评估临床LLM助手在多就诊患者轨迹推理中的表现，包含385个对话和九任务分类，评估了八种历史表示策略在四个骨干模型上的效果，发现压缩会损害纵向临床推理能力。
- **原始摘要**: arXiv:2609.01111v1 Announce Type: new Abstract: Clinical LLM assistants must reason over multi-visit patient trajectories, yet whether the compact history representations used to scale them---retrieva...

### 47. EDRAC: Benchmarking Arabic Dialect Reading Comprehension
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01113
- **AI 摘要**: 本文介绍EDRAC，首个大规模阿拉伯语方言机器阅读理解基准，覆盖五种主要方言，包含499个段落和4977个问答对，通过人机协作流程构建，评估了多种LLM的性能，揭示了方言理解上的显著差距。
- **原始摘要**: arXiv:2609.01113v1 Announce Type: new Abstract: Dialectal Arabic (DA) remains under-resourced compared to Modern Standard Arabic (MSA), particularly for machine reading comprehension (MRC) and questio...

### 48. Does task decomposition improve automatic NLG evaluation?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01139
- **AI 摘要**: 本文系统比较了有无任务分解的LLM-as-a-judge方法在多个NLG数据集上的表现，发现任务分解并未带来性能提升，先前报告的优势源于使用人工标签作为训练数据，而非分解本身。
- **原始摘要**: arXiv:2609.01139v1 Announce Type: new Abstract: The LLM-as-a-judge (LLMaJ) framework has emerged as a promising solution for cheap, reproducible, reference-free Natural Language Generation (NLG) evalu...

### 49. CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01195
- **AI 摘要**: 本文提出CaRL-EM，一个成本感知的强化学习控制器，用于管理LLM实体匹配操作，能自适应选择不同操作符和模型容量以最大化质量-成本目标，且控制器可跨不同LLM后端复用。
- **原始摘要**: arXiv:2609.01195v1 Announce Type: new Abstract: Entity matching (EM) requires fine-grained contextual understanding and domain knowledge. Recent work shows that large language models (LLMs) can serve...

### 50. CHARM: Character Hallucination for Multicultural Role Play Benchmark
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01352
- **AI 摘要**: 提出CHARM基准，用于评估角色扮演LLM的角色幻觉，区分边界感知与边界遵从，涵盖多文化角色，发现幻觉主要由边界识别失败驱动。
- **原始摘要**: arXiv:2609.01352v1 Announce Type: new Abstract: Role-playing large language models (LLMs) are expected to adopt a character's style while also respecting that character's knowledge boundaries. Prior e...

### 51. Investigating Linear Probe Robustness to Linguistic Register, Medical Specialty, and Corpus Shifts in Medical QA
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01361
- **AI 摘要**: 研究线性探针在医学问答中面对语体、专科和语料库变化时的鲁棒性，构建基准隔离三类变化，发现探针性能受输入偏移影响。
- **原始摘要**: arXiv:2609.01361v1 Announce Type: new Abstract: Linear classifiers trained on hidden states of a large language model (LLM), linear probes, can flag factual errors from a single forward pass. Geometri...

### 52. How Correct Is Your Answer? A Semantic Correctness Framework for Open QA Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01369
- **AI 摘要**: 提出开放问答语义正确性分类体系，将答案分为八类，发布CAP-Correctness和CAP-Statements基准，改进评估准确性。
- **原始摘要**: arXiv:2609.01369v1 Announce Type: new Abstract: Reliable evaluation of open-ended question answering remains a bottleneck for measuring answer correctness of modern LLMs. Unlike multiple-choice tasks,...

### 53. InSight: A Benchmark for Agentic Claim Verification in Interactive Visualizations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01383
- **AI 摘要**: 提出InSight基准，用于评估智能体在交互式可视化环境中验证声明的能力，包含2万多个基于人类叙述的声明，要求智能体主动探索环境。
- **原始摘要**: arXiv:2609.01383v1 Announce Type: new Abstract: Vision Language Models have demonstrated remarkable proficiency in interpreting static visual artifacts, but modern data analysis is inherently dynamic,...

### 54. From Rollouts to Recipes: Self-Contained Post-Training for LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01422
- **AI 摘要**: 提出Self-Routing后训练框架，根据模型行为状态（正确性和置信度）将样本路由到不同优化方法，在数学推理任务上优于统一训练方法。
- **原始摘要**: arXiv:2609.01422v1 Announce Type: new Abstract: Post-training large language models usually applies a single training recipe to all samples, even though the model's own rollouts reveal different sampl...

### 55. SDARE-Bench: Evaluating Large Language Models on Conversational Stigma Detection and Response in Dyadic and Group Dialogue
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01548
- **AI 摘要**: 本文提出SDARE-Bench基准，用于评估大语言模型在二元和群体对话中的污名检测与回应能力。实验发现模型在群体对话中识别污名成分能力差，且更易表达污名、给出不现实建议。
- **原始摘要**: arXiv:2609.01548v1 Announce Type: new Abstract: Large Language Models (LLMs) are increasingly used in advice seeking and decision making that may affect social judgements. Despite stigma's profound ef...

### 56. From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection for Text Classification
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01564
- **AI 摘要**: 本文提出一个无需微调的框架，用于解决大语言模型在大量语义相似标签分类中的混淆问题。该框架识别易混淆标签对、扩展候选集并生成区分规则，在三个基准上提升了分类性能，且规则可迁移至小模型。
- **原始摘要**: arXiv:2609.01564v1 Announce Type: new Abstract: Large language models (LLMs) struggle to classify text into taxonomies with many semantically similar labels, as the distinctions are domain-specific an...

### 57. From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers the Corporate Request Mix
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01572
- **AI 摘要**: 本文介绍如何通过生产流量分析，将200多个内部应用的流量整合到单一自托管大语言模型上。通过分轴训练GRPO专家并两阶段SLERP合并，解决了指令遵循、函数调用和任务分布的质量差距，超越了非推理模式基线。
- **原始摘要**: arXiv:2609.01572v1 Announce Type: new Abstract: Data-residency constraints force enterprises to self-host LLMs, but continuous adoption of newer models without decommissioning their predecessors expan...

### 58. Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01573
- **AI 摘要**: 本文研究大语言模型后训练中SFT与RL注释预算分配问题，提出近最优区域概念。实验表明该区域随模型规模扩大而变宽，且可从代理模型可靠迁移到目标模型，从而避免大规模搜索。
- **原始摘要**: arXiv:2609.01573v1 Announce Type: new Abstract: How to divide a fixed annotation budget between supervised fine-tuning (SFT) and reinforcement learning (RL) during LLM post-training remains an open pr...

### 59. CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01600
- **AI 摘要**: 本文介绍CordisBench基准，包含1200个问题，评估语言模型在动态智能体环境中推理组件生命周期（依赖、清理、重配置）的能力。实验显示模型在小系统上表现良好，但随交互增多可靠性下降。
- **原始摘要**: arXiv:2609.01600v1 Announce Type: new Abstract: Dynamic agent harnesses let language models change the software that shapes their own execution. This flexibility brings a new reasoning burden: a local...

### 60. InteractBench: Benchmarking LLMs on Competitive Programming under Unrevealed Information
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 19 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.29632
- **AI 摘要**: 本文提出InteractBench基准，包含322个高质量交互式编程问题，评估大语言模型在信息未完全揭示时的算法推理能力。每个问题配有可执行交互器，要求模型在严格协议和查询预算下进行多轮交互。
- **原始摘要**: arXiv:2608.29632v1 Announce Type: cross Abstract: Competitive programming is increasingly being used to evaluate the algorithmic reasoning capabilities of large language models (LLMs). However, existi...

### 61. AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00052
- **AI 摘要**: 本文提出AgentProv，首个基于工具调用行为的智能体LLM API身份审计方法。利用智能体后训练将工具使用内化到权重中，通过策略探针验证API提供商是否替换或修改了声称的基础模型，规避了文本通道的脆弱性。
- **原始摘要**: arXiv:2609.00052v1 Announce Type: cross Abstract: Commercial LLM APIs advertise a specific foundation model, but the served backbone may be silently substituted, quantized, or wrapped, for example to...

### 62. Commit-first LLM judging inherits the judge's own errors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00088
- **AI 摘要**: 本文审计了八个主流评估框架的默认LLM裁判配置，发现没有实现commit-first策略，多数采用无效变体。实验表明，普通best-of-N搜索可轻易优化系统以欺骗此类裁判，接受大量错误候选。
- **原始摘要**: arXiv:2609.00088v1 Announce Type: cross Abstract: LLM judges, models that score another system's output, can be gamed by the systems they score. Recent work identifies one defence that works: the judg...

### 63. SAGE: State-Grounded, Abstention-Aware Evaluation of Task-Oriented Dialogue Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00434
- **AI 摘要**: 本文提出SAGE评估框架，将任务型对话的工作流状态差异编译为原子标准，通过符号和编码器验证器级联，支持弃权，以低成本实现准确的状态导向评估。
- **原始摘要**: arXiv:2609.00434v1 Announce Type: cross Abstract: Evaluating task-oriented dialogue agents requires judging not merely whether a reply reads well but whether each turn advances the underlying workflow...

### 64. Predicting Program Exit Code with LLMs and Programming Language Semantics
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00579
- **AI 摘要**: 本文提出程序可执行性预测任务（PrEx），研究LLM在代码生成中是否理解编程语言语义。通过生成有效和无效程序，评估开源编码模型在两种语义形式下的表现，探讨模型是依赖预训练先验还是给定语义规则。
- **原始摘要**: arXiv:2609.00579v1 Announce Type: cross Abstract: Large language models (LLMs) have shown proficiency in various software engineering tasks, such as code generation and translation. However, a key lim...

### 65. Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00621
- **AI 摘要**: 本文提出控制-数据流分离方法，将多智能体LLM系统中执行关键协议表示为类型化程序对象，而任务相关内容保持可优化的数据流，避免提示优化破坏协议导致流水线失败，提高系统稳定性和可优化性。
- **原始摘要**: arXiv:2609.00621v1 Announce Type: cross Abstract: Prompt optimization can improve multi-agent LLM systems, but the prompts being optimized often serve two entangled roles: generating task-relevant con...

### 66. SciTrue: Reliable Scientific Claim Validation with Frontier and Open Language Models at the NTCIR SciClaimEval Task
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00654
- **AI 摘要**: 本文描述SciTrue团队在NTCIR SciClaimEval任务中的参与，基准测试11个前沿和开放多模态模型，结合轻量后处理。在官方盲测中，四个证据类别/子任务组合中三项排名第一，一项并列第一，并分析成功因素。
- **原始摘要**: arXiv:2609.00654v1 Announce Type: cross Abstract: We describe the SciTrue team's participation in both subtasks of the NTCIR-19 SciClaimEval task~\cite{sciclaimeval}, which asks systems to verify scie...

### 67. Replacing Training with Memory: Listwise Selection for Text-to-SQL
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00834
- **AI 摘要**: 本文提出MaP-SQL，一种免微调的列表式选择器用于Text-to-SQL。通过构建可复用的结构化记忆替代学习选择标准，并聚合多个排序以缓解位置偏差，无需微调即可有效选择最佳候选查询。
- **原始摘要**: arXiv:2609.00834v1 Announce Type: cross Abstract: Modern Text-to-SQL systems often follow generate-execute-select pipelines, generating multiple candidate queries then selecting the best one. Listwise...

### 68. MemoryWalker: Stop Training Agents on Contexts They Never Saw
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00865
- **AI 摘要**: 本文提出MemoryWalker框架，解决智能体在上下文压缩训练中的条件化问题。通过LogitTree和4D注意力掩码实现精确梯度修正，并引入SDCC变分松弛方法，在每次驱逐时最小化压缩学生与教师模型间的KL散度，提升训练效率。
- **原始摘要**: arXiv:2609.00865v1 Announce Type: cross Abstract: Production agent harnesses such as Claude Code and Qwen-Agent compress context during rollout, but training under compression creates a conditioning p...

### 69. RPCBench: A Benchmark for Proactive Premise Critique in LLM-based Recommendation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00918
- **AI 摘要**: 本文提出RPCBench基准，评估LLM推荐助手识别和批判推荐请求中错误前提的能力。覆盖五个推荐领域和十种前提失败类型，提供证据基础的测试实例和细粒度评估框架，衡量主动检测、诊断和处理能力。
- **原始摘要**: arXiv:2609.00918v1 Announce Type: cross Abstract: Large language models are increasingly used as interactive recommender assistants. Their evaluation should therefore go beyond plausible item recommen...

### 70. VIBE-Bench: Evaluating Personalized Large Language Models When Profiles Don't Mean Preferences
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00921
- **AI 摘要**: 本文提出VIBE-Bench基准，研究个性化LLM在档案线索与查询偏好概念错位时的表现。包含心理学基础任务、3504个人物和12239个对话，实验表明现有PLLM依赖浅层语义关联，在跨概念偏好推理上表现不佳。
- **原始摘要**: arXiv:2609.00921v1 Announce Type: cross Abstract: Personalized Large Language Models (PLLMs) aim to tailor responses to individual users, where a central challenge is preference reasoning: inferring q...

### 71. WorldBench: Culturally Grounded Benchmark for Multilingual Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01056
- **AI 摘要**: 本文提出WorldBench，一个多语言、文化扎根的智能体基准，含1600个任务覆盖七种语言和八种文化。引入约束任务成功率指标，结合指令和测试环境评估任务完成度，实验显示前沿模型在跨文化场景中仍有挑战。
- **原始摘要**: arXiv:2609.01056v1 Announce Type: cross Abstract: Despite the growing use of LLM-powered agents to solve multi-step tasks in complex environments, existing benchmarks rarely test state preservation, p...

### 72. IntroConformal: Conformal Factuality Guarantees for Large Vision-Language Models via Introspective Signals
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01375
- **AI 摘要**: 本文提出IntroConformal框架，利用模型内部信号（如层间语义稳定性和验证概率）提供无需训练的有限样本事实性保证，有效控制大型视觉语言模型的幻觉。
- **原始摘要**: arXiv:2609.01375v1 Announce Type: cross Abstract: Large Vision-Language Models (LVLMs) have achieved strong multimodal performance, yet ensuring the factual correctness of generated content remains ch...

### 73. HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01437
- **AI 摘要**: 本文提出HarnessDev基准，评估LLM创建和演化自身代理执行基础设施的能力，涵盖创建和演化两阶段，以可运行基础设施为评估单元，填补该领域空白。
- **原始摘要**: arXiv:2609.01437v1 Announce Type: cross Abstract: As agents move from research prototypes to deployed tools, their capability increasingly depends on model-external execution infrastructure, commonly...

### 74. Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01567
- **AI 摘要**: 本文提出SAGE框架，通过熵不确定性选择查询VLM教师，利用环境优势加权蒸馏指导，学习轻量RL策略，在稀疏奖励任务中实现无需VLM的自主决策。
- **原始摘要**: arXiv:2609.01567v1 Announce Type: cross Abstract: Vision-Language Models (VLMs) provide useful priors for interactive decision-making, but using them directly as policies is expensive and brittle: the...

### 75. Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01601
- **AI 摘要**: 本文提出ACToR方法，自适应识别代码生成中的关键token，并针对性检索仓库上下文，提升仓库级代码生成的准确性和一致性。
- **原始摘要**: arXiv:2609.01601v1 Announce Type: cross Abstract: The repository-level code generation task requires synthesizing code that satisfies task requirements while remaining consistent with the target repos...

### 76. GuidedBench: Measuring and Mitigating the Evaluation Discrepancies of In-the-wild LLM Jailbreak Methods
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2502.16903
- **AI 摘要**: 本文提出GuidedBench基准和GuidedEval评估系统，通过案例级指南减少LLM越狱方法评估的差异，提高评估准确性和可复现性。
- **原始摘要**: arXiv:2502.16903v3 Announce Type: replace Abstract: Despite the growing interest in jailbreaks as an effective red-teaming tool for building safe and responsible large language models (LLMs), flawed e...

### 77. Evaluating Style-Personalized Text Generation: Challenges and Directions
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2508.06374
- **AI 摘要**: 批判性评估风格个性化文本生成中常用指标（如BLEU、嵌入、LLM评判）的有效性，提出风格判别基准，涵盖八个写作任务，揭示现有指标的局限性。
- **原始摘要**: arXiv:2508.06374v4 Announce Type: replace Abstract: With the surge of large language models (LLMs) and their ability to produce customized output, style-personalized text generation--"write like me"--...

### 78. BiasGym: A Simple and Generalizable Framework for Analyzing and Removing Biases through Injection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2508.08855
- **AI 摘要**: 提出BiasGym框架，通过注入特定偏见并利用Scope或Steer方法识别和抑制模型中的偏见组件，实现低成本、可泛化的偏见分析与消除。
- **原始摘要**: arXiv:2508.08855v5 Announce Type: replace Abstract: Understanding biases and stereotypes encoded in the weights of Large Language Models (LLMs) is crucial for developing effective mitigation strategie...

### 79. Camellia: Benchmarking Cultural Biases in LLMs for Asian Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2510.05291
- **AI 摘要**: 介绍Camellia基准，评估九种亚洲语言中LLM的文化偏见，包含大量人工标注实体和掩码上下文，发现多语言模型存在文化偏见倾向。
- **原始摘要**: arXiv:2510.05291v3 Announce Type: replace Abstract: As Large Language Models (LLMs) develop stronger multilingual capabilities, their sensitivity to culturally diverse entities becomes increasingly im...

### 80. AdaSearch: Balancing Parametric Knowledge and Search in Large Language Models via Reinforcement Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2512.16883
- **AI 摘要**: 本文提出AdaSearch，一种两阶段、结果驱动的强化学习框架，用于平衡LLM的参数量知识与外部搜索，通过显式决策过程减少不必要的搜索开销，提升搜索代理性能。
- **原始摘要**: arXiv:2512.16883v2 Announce Type: replace Abstract: Equipping large language models (LLMs) with search engines via reinforcement learning (RL) promises effective search agents. However, adaptively bal...

### 81. Beyond Tokens: Semantic-Aware Speculative Decoding for Efficient Inference by Probing Internal States
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2602.03708
- **AI 摘要**: 本文提出SemanticSpec，一种语义感知的投机解码框架，通过探测模型内部隐藏状态验证整个语义序列而非单个token，加速LLM推理，在DeepSeekR1-32B上实现最高2.7倍加速。
- **原始摘要**: arXiv:2602.03708v3 Announce Type: replace Abstract: Large Language Models (LLMs) achieve strong performance across many tasks but suffer from high inference latency due to autoregressive decoding. The...

### 82. Is Knowledge Distillation Actually Greener? A Case Study in Machine Translation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2602.09691
- **AI 摘要**: 本文通过机器学习生命周期评估工具，研究知识蒸馏在机器翻译中的环境成本，发现部署量需求随服务场景和批处理变化，可相差多个数量级，并提供选择、开发和评估KD方法的指导。
- **原始摘要**: arXiv:2602.09691v2 Announce Type: replace Abstract: Knowledge distillation (KD) is a technique to compress a larger teacher system into a smaller student. In machine translation, KD is commonly evalua...

### 83. Suffix-Constrained Greedy Search Algorithms for Causal Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.01243
- **AI 摘要**: 本文提出后缀约束生成问题，即仅约束响应结尾符合语法，并基于贪心搜索设计多种算法，支持LLM自由推理后生成特定格式输出，实验验证其有效性。
- **原始摘要**: arXiv:2603.01243v3 Announce Type: replace Abstract: Large language models (LLMs) are powerful tools that have found applications beyond human-machine interfaces and chatbots. Beside free-form generati...

### 84. MineDraft: A Framework for Batch Parallel Speculative Decoding
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.18016
- **AI 摘要**: 提出MineDraft批并行投机解码框架，通过两批请求重叠草稿与验证阶段，隐藏草稿延迟。理论分析证明其效率优于标准SD，实验显示吞吐量提升75%，端到端延迟降低39%。
- **原始摘要**: arXiv:2603.18016v3 Announce Type: replace Abstract: Speculative decoding (SD) accelerates large language model inference by using a smaller draft model to propose draft tokens that are subsequently ve...

### 85. MusTBench: Benchmarking and Advancing Temporal Grounding in Music LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.29300
- **AI 摘要**: 本文提出MusTBench基准，用于评估音乐大语言模型的时间定位能力，并设计MusT四阶段优化方案。实验表明现有模型在精确时间定位上存在困难，而MusT能显著提升该能力。
- **原始摘要**: arXiv:2605.29300v2 Announce Type: replace Abstract: Recent Large Audio-Language Models (LALMs) have demonstrated promising abilities in understanding musical content. However, whether their responses...

### 86. FineVerify: Scaling Test-Time Compute with Fine-Grained Self-Verification for Agentic Search
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.00660
- **AI 摘要**: 本文提出FineVerify，一种细粒度自验证框架，通过将问题分解为可检查的子问题来提升智能体搜索的测试时计算扩展效果。实验表明该方法在多个基准上优于标准基线，显著提升模型准确率。
- **原始摘要**: arXiv:2606.00660v2 Announce Type: replace Abstract: Agentic search requires language model agents to explore many sources and answer complex information-seeking questions. Scaling test-time compute is...

### 87. PlanarBench: Evaluating LLM Spatial Reasoning via Planar Graph Drawing
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.02010
- **AI 摘要**: 本文介绍PlanarBench基准，用于评估LLM通过平面图绘制进行空间推理的能力。研究发现边数比顶点数更能预测任务难度，该基准为分离这两个难度轴提供了受控环境。
- **原始摘要**: arXiv:2606.02010v2 Announce Type: replace Abstract: Existing LLM graph benchmarks typically ask models to answer graph-theoretic questions or compute symbolic solutions rather than construct spatial l...

### 88. Who Annotates in NLP? A Large-scale Assessment of Human Annotation Reporting between 2018 and 2025
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.02255
- **AI 摘要**: 本文对2018至2025年间NLP领域的人工标注报告实践进行了大规模审计，提出了统一的标注报告分类法，并验证了LLM辅助提取管道的有效性，构建了涵盖ACL会议论文的数据集。
- **原始摘要**: arXiv:2606.02255v2 Announce Type: replace Abstract: Human annotation is the empirical foundation of much NLP research, from dataset construction to model evaluation, but papers often leave unclear who...

### 89. Evaluating Second-Order Bias of LLMs Through Epistemic Entitlement
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.17506
- **AI 摘要**: 本文提出二阶偏见概念，即LLM在评判偏见内容时表现出的社会偏见，并通过基于认识论权利的推理任务和两个指标来评估。研究发现模型在推断人口统计信息时存在系统性偏见。
- **原始摘要**: arXiv:2606.17506v2 Announce Type: replace Abstract: Evaluations of social bias in LLMs largely focus on whether models generate or imply biased content. However, as LLMs are increasingly used as judge...

### 90. ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.18237
- **AI 摘要**: 本文提出ReproRepo，一个利用GitHub issue作为自然监督信号的可扩展可复现性评估框架。在1149篇论文上的实验表明，LLM代理无需执行代码即可识别出许多真实世界的可复现性问题。
- **原始摘要**: arXiv:2606.18237v2 Announce Type: replace Abstract: Reproducing research results from papers and released code is central to scientific progress. Existing works have introduced benchmarks to evaluate...

### 91. Can LLMs Reliably Self-Report Adversarial Prefills, and How?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.23671
- **AI 摘要**: 本文研究LLM能否可靠地识别自身输出是否由对抗性前缀注入引发。实验发现模型无法可靠识别，平均声称率为25.3%，且内部意图与外部篡改的提问框架会引发不同响应。
- **原始摘要**: arXiv:2606.23671v5 Announce Type: replace Abstract: Prior work shows that large language models (LLMs) exhibit varying degrees of introspective capability on benign tasks. We extend the question to sa...

### 92. Zero Hallucination, by Construction: Hallucination-Aware Layered Oversight for Trustworthy Enterprise AI
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.17883
- **AI 摘要**: 提出HALO架构，将幻觉视为可遏制而非可消除的故障模式，通过六层防御实现企业级AI的零幻觉保证。强调零幻觉是系统属性而非模型属性，提供可信赖的AI部署方案。
- **原始摘要**: arXiv:2607.17883v2 Announce Type: replace Abstract: Enterprises will not deploy AI agents they cannot trust, and the most-cited reason for distrust is hallucination: confident, fluent output that is s...

### 93. A Classifier That Teaches Itself: Self-Improving, Frozen-gate Training (SIFT) for Dynamic Document Classification
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.18358
- **AI 摘要**: 提出SIFT动态文档分类服务，采用廉价CPU管道加LLM法官的自我改进训练。低置信度页面升级至LLM，其判断回写扩充语料，使昂贵模型持续教导廉价模型，降低升级率并提升准确性。
- **原始摘要**: arXiv:2607.18358v2 Announce Type: replace Abstract: Document classification is a solved problem in the laboratory and an unsolved one in the enterprise. The blocker is rarely model architecture; it is...

### 94. FormalTCS: Benchmarking End-to-End Frontier Formal Theoretical Computer Science Research of Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 19 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.20153
- **AI 摘要**: 本文提出FormalTCS基准，用于评估大语言模型在前沿理论计算机科学研究中的端到端能力。基准包含143个来自STOC等顶会论文的实例，并配有专家验证的Lean形式化证明。评估显示当前模型难以完成完整研究流程，其中自动形式化是最主要瓶颈。
- **原始摘要**: arXiv:2608.20153v2 Announce Type: replace Abstract: Large language models (LLMs) have shown growing potential for automated theoretical computer science (TCS) research, yet existing benchmarks remain...

### 95. MAS-ProVe: Understanding the Process Verification of Multi-Agent Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2602.03053
- **AI 摘要**: 本文对多智能体系统的过程验证进行系统实证研究，涵盖三种验证范式、两种验证粒度、五个验证器和四种上下文管理策略。研究发现过程级验证并不能一致地提升多智能体系统性能，挑战了其作为协调工具的普遍有效性假设。
- **原始摘要**: arXiv:2602.03053v2 Announce Type: replace-cross Abstract: Multi-Agent Systems (MAS) built on Large Language Models (LLMs) often exhibit high variance in their reasoning trajectories. Process verificat...

### 96. The Importance of Being Statistically Earnest: A Critical Re-evaluation of GSM-Symbolic
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.28700
- **AI 摘要**: 本文对GSM-Symbolic基准的统计有效性进行批判性再评估。使用自助广义线性混合模型重新分析20个开源模型，发现仅8个模型存在统计显著的性能变化。同时发现GSM-Symbolic数据集中整数分布系统性偏向更大值，控制该效应后剩余案例中一半的显著性消失。
- **原始摘要**: arXiv:2605.28700v3 Announce Type: replace-cross Abstract: The GSM-Symbolic benchmark (Mirzadeh et al., 2025) reported consistent performance drops across 25 Large Language Models (LLMs) when tested on...

### 97. RECAP: Regression Evaluation for Continual Adaptation of Prompts
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.06698
- **AI 摘要**: 本文提出RECAP基准，用于评估生产环境中智能体系统在约束动态变化下的持续适应能力，采用严格的主动适应-再测试协议，衡量提示优化方法在约束层面的遗忘、回归和正向迁移现象。
- **原始摘要**: arXiv:2606.06698v4 Announce Type: replace-cross Abstract: Production agentic systems routinely face evolving constraints and must comply from the very next interaction. Scenarios like a tool-call noti...

### 98. Debiased Inference for AI-Generated Data without Gold-Standard Labels: Identification via Multiple Imperfect Measurements
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 19 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18294
- **AI 摘要**: 本文提出DMM框架，利用多个不完美的AI测量结果进行去偏推断，无需金标准标签即可获得有效的下游统计推断，解决AI测量误差导致的偏差和置信区间无效问题。
- **原始摘要**: arXiv:2608.18294v2 Announce Type: replace-cross Abstract: An increasing number of scholars use AI to measure variables they subsequently include in downstream analyses. Although AI-measured variables...

### 99. S^3martCirc: Self-supervised Smart Circuit Discovery
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00755
- **AI 摘要**: 本文提出S^3martCirc，一种自监督智能电路发现方法，用于大语言模型的机制可解释性。它统一了电路发现和功能解释两个阶段，解决组件重要性与功能角色相互依赖的问题，克服了传统两阶段范式的局限。
- **原始摘要**: arXiv:2609.00755v1 Announce Type: new Abstract: Large Language Models (LLMs) have demonstrated remarkable performance across diverse tasks, from text summarization to question answering. Despite these...

### 100. AgentFactory: Towards Automated Agentic System Design and Optimization
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01045
- **AI 摘要**: 本文提出AgentFactory框架，联合优化智能体系统中的基础模型和工作流结构，同时考虑性能、成本和效率多目标。利用高级LLM作为优化器，通过三阶段优化搜索配置空间，提升系统适应性和可扩展性。
- **原始摘要**: arXiv:2609.01045v1 Announce Type: new Abstract: Large Language Models (LLMs) have demonstrated remarkable capabilities as powerful components in agentic systems, enabling sophisticated reasoning and c...

### 101. ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01058
- **AI 摘要**: 本文提出ARISE-RL，一种基于规则的全周期自进化框架，通过任务/规则生成器与推理求解器的协同进化，解决开放任务中奖励稀疏和不稳定的问题。引入奖励门控自进化机制，提升长程智能体训练效果。
- **原始摘要**: arXiv:2609.01058v1 Announce Type: new Abstract: Training open-ended agents via reinforcement learning (RL) is hindered by the lack of verifiable gold answers and scalable rubrics. Moreover, even near...

### 102. A Composable Evaluation System for Reproducible Omni-Modal Foundation Model Evaluation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01315
- **AI 摘要**: 本文提出OmniEvaluator，一个可组合的全模态基础模型评估系统，统一文本、图像、视频和音频的评估接口，连接多个推理后端和评估框架，记录完整配置以实现可复现性，并支持联邦模式共享GPU。
- **原始摘要**: arXiv:2609.01315v1 Announce Type: new Abstract: Building an omni-modal foundation model means evaluating it across text, image, video, and audio. Excellent evaluation toolkits exist for each modality,...

### 103. Bandits in Prod: Hyperparameter Optimization at Inference Time
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01335
- **AI 摘要**: 本文形式化在线超参数优化问题，提出IMABO框架结合任意bandit策略与提议oracle，并实例化IMOSS算法，证明期望累积分位数遗憾界，适用于生产系统推理时配置选择。
- **原始摘要**: arXiv:2609.01335v1 Announce Type: cross Abstract: Many production systems can assess a configuration only by using it on live requests and observing noisy feedback. Modern agentic systems are a promin...

### 104. VectorGym: A Multi-Task Benchmark for SVG Code Generation, Sketching and Editing
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.29852
- **AI 摘要**: 本文介绍VectorGym，一个全面的SVG基准测试套件，涵盖文本/草图生成、复杂编辑和视觉理解。包含四个专家标注任务，并提供基于GRPO和课程学习的多任务RL基线，以联合优化所有任务。
- **原始摘要**: arXiv:2603.29852v2 Announce Type: replace-cross Abstract: We introduce VectorGym, a comprehensive benchmark suite for Scalable Vector Graphics (SVG) that spans generation from text and sketches, compl...

### 105. Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00097
- **AI 摘要**: 本文提出Faster Flash Decoding（FFD），一种硬件算法协同设计的框架，通过融合选择器与计算器、低比特量化和top-delta策略，利用注意力稀疏性实现高效长上下文解码，突破内存墙限制。
- **原始摘要**: arXiv:2609.00097v1 Announce Type: new Abstract: The development of long-context Large Language Models (LLMs) is constrained by the memory bandwidth bottleneck and quadratic complexity of the attention...

### 106. WHALE: A Simple Recipe for Joint Harness-Weight Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00196
- **AI 摘要**: 本文提出WHALE方法，交替更新模型参数和可执行harness代码，通过在线拒绝采样微调和Meta-Harness搜索，实现智能体性能的联合优化，解决单一优化瓶颈问题。
- **原始摘要**: arXiv:2609.00196v1 Announce Type: new Abstract: Agent performance depends jointly on the model parameters and the executable harness code that manages context and control flow. Optimizing either compo...

### 107. HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design for Accurate LLM Inference
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00450
- **AI 摘要**: 本文提出分层块量化（HBQ），通过硬件效率感知的设计空间探索，采用大块和分层缩放策略，在保持硬件效率的同时提升LLM低精度推理的准确性，优于传统块量化方法。
- **原始摘要**: arXiv:2609.00450v1 Announce Type: new Abstract: Block Quantization (BQ) is a promising approach for efficient deployment of large language models (LLMs), enabling low-precision computation with contro...

### 108. HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00829
- **AI 摘要**: HarnessEvolve是一个自进化智能体框架，通过参考轨迹学习实现可靠进化。它将执行与进化流程解耦，分配独立模块负责执行、评估、优化和门控，解决信用分配失败、捷径学习和灾难性遗忘问题，提升智能体泛化与稳定性。
- **原始摘要**: arXiv:2609.00829v1 Announce Type: new Abstract: Self-evolving agents advance toward autonomy by optimizing their harness---prompts, skills, tools, and execution logic---based on environmental feedback...

### 109. Efficiently Estimating Optimal Hyperparameter Scaling Laws through Power-Law Entropy Search
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01431
- **AI 摘要**: 本文提出Power-Law Entropy Search (PLES)，一种基于多保真贝叶斯优化的采集函数，用于高效估计大语言模型训练中超参数的最优缩放定律，避免昂贵的穷举搜索，通过自适应实验减少缩放定律估计的不确定性。
- **原始摘要**: arXiv:2609.01431v1 Announce Type: new Abstract: Optimal hyperparameter scaling laws describe how the best hyperparameters for large language model (LLM) training change with model and data scale, enab...

### 110. SOVER: Formal Certification of Optimization Reformulations via LLM-Assisted SMT Verification
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00728
- **AI 摘要**: 本文提出SOVER，一种LLM辅助的SMT验证框架，分离语义映射与形式验证，使用Z3和dReal检查优化问题重构的等价性，并引入NLEquiv-150基准测试，实现高精度分类。
- **原始摘要**: arXiv:2609.00728v1 Announce Type: cross Abstract: Large Language Models (LLMs) have shown remarkable promise in translating and reformulating complex mathematical optimization problems across modeling...

### 111. DualStake: Dual-Path Confidence Calibration in Deep Research Agents
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00935
- **AI 摘要**: 本文针对深度研究智能体过度自信问题，提出DualStake双路径置信度校准方法，通过检索后步骤置信度引导和边际裁剪的奖励机制，联合校准证据置信度与答案置信度，提升可靠性。
- **原始摘要**: arXiv:2609.00935v1 Announce Type: cross Abstract: Deep Research agents tackle knowledge-intensive tasks through multi-round retrieval and decision-oriented generation. However, these agents suffer fro...

### 112. Exact Risk-Complexity Laws for Projective Boundaries in Scenario Optimization and Distribution-Free Certification
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01355
- **AI 摘要**: 本文研究情景优化和分布自由认证中的风险-复杂度精确规律，识别投影边界机制，推导边界大小随机时的风险分布律，为决策和预测集的违规风险保证提供理论支撑。
- **原始摘要**: arXiv:2609.01355v1 Announce Type: cross Abstract: Scenario optimization, conformal prediction, and related distribution-free certification methods use finite samples to construct decisions or predicti...

### 113. Online Regime-aware Calibration for Black-box Social Simulators via Posterior-assisted Evolutionary Dynamic Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2601.19481
- **AI 摘要**: 本文针对黑盒模拟器的在线校准问题，提出PosEDO方法。该方法将动态目标由观测和变化校准窗口驱动，而非显式变量，通过观测条件参数空间信号增强基于适应度的进化动态优化，在线学习模拟器参数的后验分布，以应对环境变化。
- **原始摘要**: arXiv:2601.19481v2 Announce Type: replace-cross Abstract: Evolutionary dynamic optimization (EDO) commonly assumes that environmental changes can be detected from fitness variations and handled throug...

### 114. LLM-PRISM: Characterizing Silent Data Corruption from Permanent GPU Faults in LLM Training
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.10390
- **AI 摘要**: 提出LLM-PRISM方法，结合RTL级GPU故障模拟和随机注入引擎，表征LLM预训练对硬件永久故障的韧性，发现故障影响高度不均匀，特定精度格式可导致灾难性发散。
- **原始摘要**: arXiv:2604.10390v2 Announce Type: replace Abstract: Large-scale LLM training is increasingly susceptible to hardware defects stemming from manufacturing escapes and silicon aging. These defects manife...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
