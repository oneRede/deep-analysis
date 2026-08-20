# RSS 聚合报告 - AI模型

**生成时间**: 2026-08-20 11:21:51
**文章数量**: 125 篇

---

### 1. Same GRPO recipe on three from-scratch LLMs (353M/316M/672M) gave three different outcomes, with no clean relationship to scale [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T21:30:26+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vszsit/same_grpo_recipe_on_three_fromscratch_llms/
- **AI 摘要**: 作者从零训练了三个不同规模的LLM，并用相同的SFT和GRPO流程进行后训练。预训练表现正常，但GRPO对两个较大模型产生了负面影响，且结果与模型规模无清晰关系，原因不明。
- **原始摘要**: <!-- SC_OFF --><div class="md"><p>I trained three LLMs from scratch in raw PyTorch then post-trained each one with SFT and then GRPO. Same process every time: same synthetic arithmetic curriculum, sam...

### 2. How much of the weight-space perception gap is actually symmetry? Evidence from ~1.8M fitted SIRENs [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T19:24:12+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vswdnf/how_much_of_the_weightspace_perception_gap_is/
- **AI 摘要**: 本文探讨权重空间学习中参数对称性对语义读取的影响。通过约180万拟合SIRENs实验，发现独立拟合网络权重语义崩溃主要源于对称性，而非其他因素，为理解权重空间感知差异提供新证据。
- **原始摘要**: <!-- SC_OFF --><div class="md"><p>I’ve been looking at a fairly basic question in weight-space learning that I don’t think gets separated cleanly enough:<br /> Why does reading semantics directly from...

### 3. v1.6.0: Mistrall goes Small 3.1 with vision
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2025-03-20T15:03:08Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.6.0
- **AI 摘要**: Mistral Inference v1.6.0版本发布，新增对Mistral Small 3.1模型的支持，该模型具备视觉能力，同时修复了缺失换行符的问题。
- **原始摘要**: <h2>What's Changed</h2>
<ul>
<li>Missing new line by <a class="user-mention notranslate" href="https://github.com/theophilegervet">@theophilegervet</a> in <a class="issue-link js-issue-link" href="htt...

### 4. v1.4.0: Pixtral 👀
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-09-13T13:10:17Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.4.0
- **AI 摘要**: Mistral AI发布v1.4.0版本，推出Pixtral多模态模型，支持视觉理解能力。用户可通过pip升级mistral_inference库（>=1.4.0）并使用Hugging Face下载模型。
- **原始摘要**: <p><strong>Pixtral</strong></p>
<p>Mistral models can now 👀 !</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto"><pre>pip install --upgrade mistral_inference...

### 5. v1.3.0 Mistral-Nemo
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-18T15:45:30Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.3.0
- **AI 摘要**: Mistral与NVIDIA合作推出Mistral-Nemo模型，并发布了v1.3.0版本，提供安装和下载指南。
- **原始摘要**: <h1>Welcome Mistral-Nemo from Mistral 🤝 NVIDIA</h1>
<p>Read more about <strong>Mistral-Nemo</strong> <a href="https://mistral.ai/news/mistral-nemo/" rel="nofollow">here</a>.</p>
<p><strong>Install</st...

### 6. v1.2.0 Add Mamba
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-16T18:41:37Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.2.0
- **AI 摘要**: Mistral AI发布v1.2.0版本，新增Codestral-Mamba和Mathstral模型，支持通过pip安装相关依赖包，提供代码生成和数学推理能力。
- **原始摘要**: <h1>Welcome 🐍 Codestral-Mamba and 🔢 Mathstral</h1>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>pip install mistral-inference&gt;=1...

### 7. v1.0.4 - Mistral-inference
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-05-24T18:32:35Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.0.4
- **AI 摘要**: Mistral-inference是Mistral AI官方发布的推理库，支持7B、8x7B、8x22B等所有Mistral模型。用户可通过pip安装，并提供了简单的运行方式。该库旨在简化Mistral模型的推理部署流程。
- **原始摘要**: <p>Mistral-inference is the official inference library for all Mistral models: 7B, 8x7B, 8x22B.</p>
<p>Install with:</p>
<div class="highlight highlight-source-python notranslate position-relative ove...

### 8. v1.1.0 Add LoRA
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-05-24T18:32:10Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.1.0
- **AI 摘要**: mistral-inference v1.1.0新增对LoRA模型的支持，这些模型通过mistral-finetune训练。用户可加载7B基础LoRA模型并运行推理，具体用法见代码示例。
- **原始摘要**: <p>mistral-inference==1.1.0 supports running LoRA models that were trained with: <a href="https://github.com/mistralai/mistral-finetune">https://github.com/mistralai/mistral-finetune</a></p>
<p>Having...

### 9. Counterfactual Anatomy-guided Spatial-Temporal Decoding for Annotation-Free Hallucination Mitigation in Medical VLMs
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17427
- **AI 摘要**: 本文提出一种基于解剖学引导的时空解码方法，用于减少医学视觉语言模型中的幻觉，无需标注数据，通过解剖结构感知提升临床可靠性。
- **原始摘要**: arXiv:2608.17427v1 Announce Type: new 
Abstract: Medical vision-language models (Med-VLMs) have demonstrated strong performance on medical visual question answering, yet they remain prone to hallucina...

### 10. NGS-Marker: Robust Native Watermarking for 3D Gaussian Splatting
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17447
- **AI 摘要**: 针对3D高斯泼溅技术，提出一种鲁棒的原生水印方法NGS-Marker，以解决现有技术仅保护渲染图像而忽视3D高斯原语、难以应对部分侵权的问题。
- **原始摘要**: arXiv:2608.17447v1 Announce Type: new 
Abstract: With the rapid development and adoption of 3D Gaussian Splatting (3DGS), the need for effective copyright protection has become increasingly critical....

### 11. SE-MoLoRA: Shared-Expert LoRA Adapters for Domain-Specific Photographic Assessment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17514
- **AI 摘要**: SE-MoLoRA是一种模块化参数高效适配框架，用于领域特定摄影评估。它通过始终激活的共享LoRA专家和路由适配器，将通用摄影知识与专业残余判断分离，解决视觉语言模型在摄影批评中语义与美学纠缠的问题。
- **原始摘要**: arXiv:2608.17514v1 Announce Type: new 
Abstract: Vision-language models can describe images fluently, but they often fail to provide actionable photographic critique because semantic content and aesth...

### 12. Where a New Concept Must Enter: Entry Point Gates Cross-Task Usability in Unified Multimodal Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17564
- **AI 摘要**: 统一多模态模型（UMMs）旨在通过理解与生成相互增强，但对照实验发现添加生成目标后理解能力并未提升。联合训练无法解决争议，因为重叠监督下无法区分架构与数据的影响。本文进一步探究UMMs中两个方向的关系。
- **原始摘要**: arXiv:2608.17564v1 Announce Type: new 
Abstract: Unified multimodal models (UMMs) are motivated by the hope that understanding and generation reinforce each other but controlled ablations repeatedly f...

### 13. From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Generalist Image Generation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18076
- **AI 摘要**: 本文提出一种以能力为中心的数据基础设施，用于通用图像生成。它强调根据生成能力间的依赖关系组织异构监督数据，而非孤立优化各任务数据集，以促进能力的协同进化。
- **原始摘要**: arXiv:2608.18076v1 Announce Type: new 
Abstract: Large-scale image generation has benefited from advances in data scale, quality, rebalancing, and recaptioning, yet conventional pipelines typically op...

### 14. Vision-Language Enhanced Foundation Model for Semi-Supervised Medical Image Segmentation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2511.19759
- **AI 摘要**: 本文提出将视觉语言模型集成到半监督医学图像分割中，通过添加视觉语言增强的半监督分割助手，利用VLM的泛化能力减少对专家标注的依赖，提升分割性能。
- **原始摘要**: arXiv:2511.19759v3 Announce Type: replace 
Abstract: Semi-supervised learning (SSL) has emerged as an efficient paradigm for medical image segmentation, reducing the reliance on extensive expert annot...

### 15. Know3D: Prompting 3D Generation with Knowledge from Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.22782
- **AI 摘要**: 本文提出Know3D，利用视觉-语言模型的知识来引导3D生成，以解决单视图观察的模糊性和有限3D训练数据导致的全局结构先验不足问题，从而生成更符合用户意图且几何合理的3D资产。
- **原始摘要**: arXiv:2603.22782v2 Announce Type: replace 
Abstract: Recent advances in 3D generation have improved the fidelity and geometric details of synthesized 3D assets. However, due to the inherent ambiguity...

### 16. Repurposing 3D Generative Model for Autoregressive Layout Generation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.16299
- **AI 摘要**: LaviGen框架将3D生成模型用于3D布局生成，直接在原生3D空间中通过自回归过程建模物体间几何关系和物理约束，生成连贯且物理上合理的3D场景，无需依赖文本描述。
- **原始摘要**: arXiv:2604.16299v2 Announce Type: replace 
Abstract: We introduce LaviGen, a framework that repurposes 3D generative models for 3D layout generation. Unlike previous methods that infer object layouts...

### 17. Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.09520
- **AI 摘要**: 本文首次系统剖析边缘设备上VLM推理的能耗，发现视觉处理并非主要能耗瓶颈，颠覆了现有优化假设。研究覆盖五种模型、三种架构，为边缘AI能效优化提供新方向。
- **原始摘要**: arXiv:2607.09520v2 Announce Type: replace 
Abstract: Vision-Language Models (VLMs) are the perceptual backbone of embodied AI, but their energy footprint on edge hardware remains poorly understood. Ex...

### 18. AVA-Encoder: Towards Agent-Native Video Representation Learning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12313
- **AI 摘要**: AVA-Encoder是一种新型自编码框架，旨在为视频智能体提供结构化表示，使其能从高质量人类影片中学习并生成电影级视频，解决现有表示缺乏保真度和可操作性的问题。
- **原始摘要**: arXiv:2608.12313v2 Announce Type: replace 
Abstract: Video creative agents still lack an effective way to learn from high-quality human films, limiting their ability to produce cinematic-grade videos....

### 19. Alaya-EVOKE: From Linear-Scaling Supervision to Endless World
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.13546
- **AI 摘要**: Alaya-EVOKE提出交互式世界模型，解决持久记忆、响应交互和长程生成的冲突需求，通过新方法避免历史维护成本，实现低延迟交互。
- **原始摘要**: arXiv:2608.13546v2 Announce Type: replace 
Abstract: Interactive world models must support persistent memory, responsive interaction, and long-horizon generation, yet these requirements place conflict...

### 20. GLaQ: Grounding Latent Queries in Visual Evidence for Multimodal Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.15517
- **AI 摘要**: 本文提出GLaQ方法，通过将潜在查询锚定到视觉证据上，增强多模态大语言模型在推理过程中对细粒度视觉信息的保留与重用，无需外部工具，提升多模态推理能力。
- **原始摘要**: arXiv:2608.15517v2 Announce Type: replace 
Abstract: Chain-of-thought reasoning has substantially improved the problem-solving capabilities of multimodal large language models. Fine-grained visual evi...

### 21. Accelerating GPT-5.6 Sol UltrafastAugust 13, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ust 13, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai
- **AI 摘要**: 文章标题提及GPT-5.6 Sol超快加速，但摘要内容为空，无法提取具体信息。

### 22. The Economics of AI ReasoningJune 17, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 17, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/the-economics-of-ai-reasoning
- **AI 摘要**: 文章探讨了AI推理的经济学，分析了推理成本、效率与性能之间的权衡，并提出了优化推理资源分配的策略，以平衡模型能力与实际应用需求。

### 23. Open Sourcingπ0February 4, 2025We are releasing the weights and code for π0 as well as our new π0-FAST autoregressive model.
- **来源**: Physical Intelligence (TIER1)
- **发布日期**: ril 16, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.physicalintelligence.company/blog/openpi
- **AI 摘要**: 文章宣布开源π0模型及其权重和代码，并推出新的π0-FAST自回归模型。

### 24. The GPU Is Being Split in HalfMarch 26, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: rch 26, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/disaggregated-inference
- **AI 摘要**: 文章探讨GPU架构正在被分割为两半，可能指计算与内存或专用与通用部分的分离，以适应AI工作负载需求，反映硬件设计趋势。

### 25. REAP: One-Shot Pruning for Trillion-Parameter Mixture-of-Experts ModelsOctober 16, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 16, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/reap
- **AI 摘要**: REAP是一种针对万亿参数混合专家模型的一次性剪枝方法，旨在高效压缩模型规模，同时保持性能。该方法通过识别并移除冗余专家，显著降低计算成本，适用于大规模MoE模型的部署与优化。

### 26. MoE Math Demystified: What Does 8x7B Actually Mean?October 14, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 14, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/moe-guide-calculator
- **AI 摘要**: 本文解析了MoE（混合专家）模型中“8x7B”的含义，解释了其参数计算方式、推理机制及实际性能表现，澄清了常见误解。

### 27. Thinking Inside the Box: The Implicit Chain Transformer for Efficient State TrackingDecember 12, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 12, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/thinking-inside-the-box-the-implicit-chain-transformer-for-efficient-state-tracking
- **AI 摘要**: 文章摘要为空，无法提供具体内容。

### 28. Jais 2: A Blueprint for Sovereign AIDecember 09, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 09, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/jais2
- **AI 摘要**: Jais 2是主权AI的蓝图，展示了如何构建自主可控的AI系统，强调数据主权、模型训练和部署的独立性，为国家和组织提供AI战略参考。

### 29. Cerebras at NeurIPS 2025: Nine Papers From Pretraining to InferenceDecember 04, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 04, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/cerebras-at-neurips-2025-nine-papers-from-pretraining-to-inference
- **AI 摘要**: Cerebras在NeurIPS 2025上发表了九篇论文，涵盖从预训练到推理的多个方面，展示了其在AI领域的创新成果。

### 30. Why speed wins: faster inference is about more than just quicker answers–it’s the new path to accuracyFebruary 19, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/speedandaccuracyblog
- **AI 摘要**: 文章指出，AI推理速度的提升不仅带来更快的响应，更是实现更高准确性的新途径。通过加速推理过程，模型能够进行更多次迭代或更深入的思考，从而提升答案质量，强调速度在AI系统中的战略价值。

### 31. Introducing OpenAI GPT-5.3-Codex-Spark Powered by CerebrasFebruary 12, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 12, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/openai-codexspark
- **AI 摘要**: OpenAI发布GPT-5.3-Codex-Spark，由Cerebras提供算力支持，旨在提升代码生成与执行效率，并可能集成到开发工具中。

### 32. This new model is smarter than Sonnet 4.5…and 20X faster?January 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7-migration-guide
- **AI 摘要**: 文章介绍了一款新模型，声称其性能优于Sonnet 4.5，且速度快20倍，发布于2026年1月8日。该模型可能带来显著的效率提升，但具体细节未在摘要中提及。

### 33. GLM-4.7: Frontier intelligence at record speed — now available on CerebrasJanuary 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7
- **AI 摘要**: GLM-4.7模型在Cerebras平台上发布，实现了创纪录的速度，展示了前沿智能。文章可能介绍了该模型的性能、应用场景及其在AI领域的意义。

### 34. 2026: Fast Inference Finds its GrooveJanuary 06, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 06, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/2026Insights
- **AI 摘要**: 文章预测2026年AI推理将迎来快速发展，强调推理速度与效率的提升成为关键，并探讨了相关技术趋势与行业影响。

### 35. Margin-Regularized Structured Semantic Alignment for Brain-Language Correspondence
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.16975
- **AI 摘要**: 本文提出MD-SigLIP模型，通过边缘正则化的结构化语义对齐方法，提升大脑-语言解码的神经表征真实性，减少语言模型自身重构的干扰，增强可解释性。
- **原始摘要**: arXiv:2608.16975v1 Announce Type: new 
Abstract: With the rapid advancement of large language models, brain-language decoding has achieved remarkable progress. However, it remains unclear whether deco...

### 36. Cross-Model Memory Transfer via Target-Side Reader Adaptation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17050
- **AI 摘要**: 本文提出跨模型记忆迁移方法，通过目标端阅读器适配，将Engram式哈希记忆从源模型迁移至目标模型，以提升知识利用效率，兼顾检索灵活性与参数化效率。
- **原始摘要**: arXiv:2608.17050v1 Announce Type: new 
Abstract: Methods for improving knowledge use in large language models typically fall into two regimes. Non-parametric retrieval offers flexible access to extern...

### 37. Uncertainty-Aware Decision Making in Multimodal Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17084
- **AI 摘要**: 本文探讨多模态大语言模型在决策中的不确定性，指出其错误不仅源于语言，还涉及视觉、文本等多模态证据，并提出了不确定性感知的决策方法。
- **原始摘要**: arXiv:2608.17084v1 Announce Type: new 
Abstract: Multimodal large language models (MLLMs) increasingly answer questions whose correctness depends on visual, textual, temporal, acoustic, document, char...

### 38. There is No Theoretical Curse of Multilinguality For Embedding Space Structure
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17088
- **AI 摘要**: 本文探讨多语言NLP中的“多语言诅咒”现象，即增加语言覆盖会降低模型性能。作者提出多语言嵌入空间在结构上并非天生无法实现完美对齐，挑战了现有理论假设。
- **原始摘要**: arXiv:2608.17088v1 Announce Type: new 
Abstract: A central goal of multilingual NLP is to achieve high monolingual performance per language and cross-lingual alignment for large-scale language coverag...

### 39. Children, but not language models, show accelerating returns in word learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17120
- **AI 摘要**: 儿童词汇学习呈加速累积特征，每增加语言经验学习效果递增；而语言模型即使规模更大，也未表现出类似加速学习模式，揭示两者学习机制的差异。
- **原始摘要**: arXiv:2608.17120v1 Announce Type: new 
Abstract: Children learn hundreds of words over the first years of their lives, in a process that begins slowly but quickly picks up speed. Prior models describe...

### 40. Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17153
- **AI 摘要**: 本文探讨了检索增强生成（RAG）系统易受知识投毒攻击的问题，即检索文档中的错误信息可能影响模型输出。研究发现，即使LLM能识别文档错误，仍可能受其影响。文章提出仅允许具备系统2思维能力的代理访问不可信文档，以提高安全性。
- **原始摘要**: arXiv:2608.17153v1 Announce Type: new 
Abstract: Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to...

### 41. Which Source Wins? Task-Dependent Reliance in Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17205
- **AI 摘要**: 本文研究视觉语言模型在图像与文本冲突时如何根据任务调整对两种模态的依赖。通过控制图像或文本的清晰度，观察模型偏好变化，发现模型会动态重新分配注意力，且依赖程度受任务类型影响。
- **原始摘要**: arXiv:2608.17205v1 Announce Type: new 
Abstract: Vision-language models (VLMs) combine images and text, but when the two conflict and one becomes harder to read, it is unclear how a model shifts its r...

### 42. Q-Interference: Memory-Efficient Phase-Aware Quantum-Inspired Attention
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17288
- **AI 摘要**: 本文提出Q-Interference，一种受量子启发的经典注意力机制，为查询和键特征添加振幅与学习相位，以显式建模特征间的增强或抑制关系，用于自回归语言建模，提升记忆效率。
- **原始摘要**: arXiv:2608.17288v1 Announce Type: new 
Abstract: GPT attention measures token compatibility through dot-product similarity. This mechanism is simple, effective, and memory-efficient. But it does not e...

### 43. What Tokens are Learned when Tokenization is Optimized Jointly with Language Modeling?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17325
- **AI 摘要**: 本文研究了当分词与语言建模联合优化时，模型会学习到哪些词元。通过对比无分词器方法与固定分词器在18种语言上的表现，分析了分词对模型性能的影响。
- **原始摘要**: arXiv:2608.17325v1 Announce Type: new 
Abstract: Tokenization is a fundamental component of language modeling pipelines. Despite its importance, it is often fixed, even though it significantly impacts...

### 44. ArborMem: Navigating Interaction States with Memory Forests
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17534
- **AI 摘要**: 大型语言模型作为持久对话助手需要记忆以保持连续性。现有方法通过长上下文、选择性检索和结构化组织改善历史访问，但多数系统未先确定相关先验意图。ArborMem提出记忆森林导航交互状态，以改进记忆访问。
- **原始摘要**: arXiv:2608.17534v1 Announce Type: new 
Abstract: Large language models increasingly serve as persistent conversational assistants, requiring memory that preserves relevant experience and maintains con...

### 45. Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17605
- **AI 摘要**: 对话式AI正从孤立文本提示转向持续的多模态交互，用户会澄清目标、修改请求、打断响应、切换话题并引入新证据，系统需跨轮次保持上下文。文章探讨了多轮对话的数据、模型、评估及开放挑战。
- **原始摘要**: arXiv:2608.17605v1 Announce Type: new 
Abstract: Conversational AI is moving beyond isolated text prompts toward sustained, multimodal interaction. In real conversations, users clarify goals, revise r...

### 46. Whether LLMs Can Navigate Beliefs and Facts Depends on How You Phrase It
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17809
- **AI 摘要**: 研究表明，大型语言模型（LLM）处理用户信念与事实的能力受提问方式影响。人类日常交流常将信念与事实交织，而LLM在用户持有错误信念时表现出系统性弱点，提示需改进其信念追踪能力。
- **原始摘要**: arXiv:2608.17809v1 Announce Type: new 
Abstract: Humans naturally form and express beliefs in daily communication, e.g., "I think the answer is 3" or "I suppose that's right." Such beliefs inevitably...

### 47. BayesPrompt: human readable prompts that make sense
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17866
- **AI 摘要**: 本文提出BayesPrompt方法，通过贝叶斯视角重构提示优化任务，生成人类可读的提示，避免传统方法产生的伪提示，同时保持LLM的期望行为。
- **原始摘要**: arXiv:2608.17866v1 Announce Type: new 
Abstract: Reconstructing prompts that can elicit a desired answer or behaviour in an LLM is an open and important research topic. Optimisation methods which aim...

### 48. Do Large Language Models Play Six Degrees of Separation? Measuring Topological Compression in Long-Context Manifolds
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17950
- **AI 摘要**: 本文通过分析隐藏状态流形的动态几何，绕过注意力权重，直接研究大语言模型在多跳推理中的内部机制，提出拓扑压缩概念，以解释模型在长上下文中的远距离认知跳跃能力。
- **原始摘要**: arXiv:2608.17950v1 Announce Type: new 
Abstract: Large Language Models (LLMs) demonstrate remarkable multi-hop reasoning capabilities over long contexts, yet the internal mechanisms enabling these dis...

### 49. Chain-of-Experience for Continual LLM Improvement
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18027
- **AI 摘要**: 本文提出Chain-of-Experience（CoE）方法，研究大语言模型在测试时通过迭代交互积累经验，实现持续改进，模拟人类从经验中学习的过程。
- **原始摘要**: arXiv:2608.18027v1 Announce Type: new 
Abstract: Humans continuously learn from experience, whereas conventional large language model (LLM) evaluations ignore the models' ability to improve through in...

### 50. Language Has Two Parameters: Narrative-Induced Semantic Plasticity and Phase-Sensitive Interpretation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18041
- **AI 摘要**: 本文提出语言具有两个参数：振幅（词共现频率）和相位（语义间组合方式）。相位决定共激活意义的组合，可反转意义，弥补传统词嵌入和注意力权重的不足。
- **原始摘要**: arXiv:2608.18041v1 Announce Type: new 
Abstract: Language has two parameters. Count how often words occur together and you estimate amplitude, the strength of association. Word embeddings and attentio...

### 51. J-Miner: Recovering Executable Decision Knowledge from Language-Model Classifiers
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17063
- **AI 摘要**: 本文研究如何从微调后的语言模型分类器中挖掘内部决策知识，并将其编码为可执行表示，以便检查、验证和复用。
- **原始摘要**: arXiv:2608.17063v1 Announce Type: cross 
Abstract: Large language models can be fine-tuned into specialized classifiers that perform well across diverse text tasks and make complex judgments, but they...

### 52. MoNe: Modular Neural Memory for Efficient Long Context Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17616
- **AI 摘要**: MoNe是一种轻量级模块化神经记忆，可附加到冻结的预训练Transformer上，无需重训练即可实现长上下文推理。它通过测试时学习和局部梯度更新分段读取上下文，推理时仅从查询令牌生成键值，无需重读上下文，解耦了推理过程。
- **原始摘要**: arXiv:2608.17616v1 Announce Type: cross 
Abstract: We present MoNe, a lightweight modular neural memory that attaches to any frozen pretrained Transformer to enable long-context inference without retr...

### 53. How Do Large Language Models Learn Concepts During Continual Pre-Training?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.03570
- **AI 摘要**: 本文研究大型语言模型在持续预训练过程中如何获取、保留和遗忘概念，以及概念间的干扰与协同作用，旨在理解概念学习的机制。
- **原始摘要**: arXiv:2601.03570v2 Announce Type: replace 
Abstract: Human beings primarily understand the world through concepts (e.g., dog), abstract mental representations that structure perception, reasoning, and...

### 54. Language Family Matters: Evaluating LLM-Based ASR Across Linguistic Boundaries
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.18899
- **AI 摘要**: 本文提出一种基于语言家族成员关系的连接器共享策略，用于LLM驱动的语音识别系统。该方法为每个语言家族训练一个连接器，而非每种语言单独训练，从而提升跨语言性能并减少资源消耗。
- **原始摘要**: arXiv:2601.18899v3 Announce Type: replace 
Abstract: Large Language Model (LLM)-powered Automatic Speech Recognition (ASR) systems achieve strong performance with limited resources by linking a frozen...

### 55. Speak in Context: Multilingual ASR with Speech Context Alignment via Contrastive Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.06505
- **AI 摘要**: 本文提出一种上下文感知的多语言自动语音识别方法，通过对比学习对齐语音与上下文表示，解决多语言支持和表示对齐两大挑战。
- **原始摘要**: arXiv:2603.06505v2 Announce Type: replace 
Abstract: Automatic speech recognition (ASR) has benefited from advances in pretrained speech and language models, yet most systems remain constrained to mon...

### 56. N-gram-like Language Models Predict Naturalistic Reading Time Best
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.09872
- **AI 摘要**: 近期研究发现，当代语言模型如transformer在预测下一个词方面表现优异，但其概率计算在预测自然阅读时间上效果不佳。本文提出，阅读时间受简单n-gram统计影响，而非复杂transformer模型所学统计。实验表明，n-gram类语言模型最能预测自然阅读时间。
- **原始摘要**: arXiv:2603.09872v2 Announce Type: replace 
Abstract: Recent work has found that contemporary language models such as transformers can become so good at next-word prediction that the probabilities they...

### 57. Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.24472
- **AI 摘要**: 自蒸馏作为LLM的后训练范式，通常能提升性能并缩短推理链。但在数学推理中，它可能降低响应长度并损害性能，原因在于抑制了认知言语化（模型表达不确定性的过程）。
- **原始摘要**: arXiv:2603.24472v4 Announce Type: replace 
Abstract: Self-distillation has emerged as an effective post-training paradigm for LLMs, often improving performance while shortening reasoning traces. Howev...

### 58. Attention Flows: Tracing LLM Conceptual Engagement via Story Summaries
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.06416
- **AI 摘要**: 本文研究大型语言模型在长文本理解上的表现，通过比较人类与LLM生成的小说摘要，评估模型是否反映人类的概念参与模式。
- **原始摘要**: arXiv:2604.06416v2 Announce Type: replace 
Abstract: Although LLM context lengths have grown, there is evidence that their ability to integrate information across long-form texts has not kept pace. We...

### 59. Convergent Evolution: How Different Language Models Learn Similar Number Representations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.20817
- **AI 摘要**: 研究发现不同架构的语言模型在表示数字时均使用周期特征，主导周期为2、5、10。这些特征存在两级层次：多种模型都能学习傅里叶域中的周期尖峰，但仅部分模型能学习可线性分类的几何可分特征。
- **原始摘要**: arXiv:2604.20817v2 Announce Type: replace 
Abstract: Language models trained on natural text learn to represent numbers using periodic features with dominant periods at $T=2, 5, 10$. In this paper, we...

### 60. SOD: Step-wise On-policy Distillation for Small Language Model Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.07725
- **AI 摘要**: 本文提出SOD（逐步在线蒸馏）方法，用于提升小语言模型在工具集成推理中的能力。通过教师模型在学生生成轨迹上提供逐步的密集监督，解决了传统强化学习奖励稀疏和长程工具交互不稳定的问题，实现了更高效的知识蒸馏。
- **原始摘要**: arXiv:2605.07725v3 Announce Type: replace 
Abstract: Tool-integrated reasoning (TIR) is difficult to scale to small language models due to instability in long-horizon tool interactions and limited mod...

### 61. H$^{2}$MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.24930
- **AI 摘要**: 本文提出H2MT，一种语义层次感知的层次记忆Transformer，旨在解决长输入下Transformer上下文窗口有限、预填充延迟和内存增长的问题。通过层次记忆和语义感知处理，减少无关计算，提升长文本处理效率。
- **原始摘要**: arXiv:2605.24930v2 Announce Type: replace 
Abstract: Transformer-based LLMs achieve strong results on many language tasks; however, long inputs remain challenging because context windows are finite, a...

### 62. When to Plan, When to Polish: Noise Level as a Granularity Axis for Diffusion Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.21802
- **AI 摘要**: 本文提出以噪声水平作为粒度轴，用于扩散语言模型。标准词元级扩散在去噪过程中保持词元粒度，高噪声时难以形成早期粗略结构。本文方法无需额外规划器或块潜在变量，通过调整噪声粒度实现规划与润色的分离。
- **原始摘要**: arXiv:2606.21802v2 Announce Type: replace 
Abstract: Standard tokenwise diffusion LMs keep training corruption and inference commitment at token granularity throughout denoising. At high noise, this l...

### 63. Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.04728
- **AI 摘要**: 本文提出一种插件式方法，将LLM强化学习后训练中的离策略token转化为在策略token，以解决重要性采样在长序列中方差爆炸的问题，从而提升对齐效果。
- **原始摘要**: arXiv:2607.04728v2 Announce Type: replace 
Abstract: Reinforcement learning (RL) post-training for large language models (LLMs) follows a efficient paradigm of "rollout then update", which inevitably...

### 64. DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.08642
- **AI 摘要**: 本文提出DominoTree，一种基于Domino的条件树结构草稿方法，用于推测解码。它结合GRU因果校正，使草稿令牌分布具有路径依赖性，克服了DDTree因子化表示的局限，从而加速LLM推理。
- **原始摘要**: arXiv:2607.08642v3 Announce Type: replace 
Abstract: Speculative decoding accelerates LLM inference by drafting tokens and verifying them in parallel. Block-diffusion drafters such as DFlash model onl...

### 65. Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and Tigrinya
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.15209
- **AI 摘要**: 针对Ge'ez文字的低资源语言（阿姆哈拉语和提格里尼亚语），提出VEXMLM，扩展XLM-R词汇表，训练语言特定的SentencePiece分词器，以降低OOV率和子词碎片化，提升多语言预训练模型性能。
- **原始摘要**: arXiv:2607.15209v2 Announce Type: replace 
Abstract: Multilingual pre-trained language models such as XLM-R perform well for major languages but struggle with low-resource Ge'ez-script languages, larg...

### 66. SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.13538
- **AI 摘要**: SAEVerbalizer框架通过将稀疏自编码器解码器方向注入语言模型表示，生成特征解释，减少对外部观察的依赖，提高计算效率。
- **原始摘要**: arXiv:2608.13538v2 Announce Type: replace 
Abstract: Sparse autoencoders (SAEs) are proposed to extract numerous features from large language model (LLM) representations, yet explaining these features...

### 67. RecurrentGPT: Expressive Depth through Recurrent Modulation in Transformers
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.15062
- **AI 摘要**: 本文提出RecurrentGPT，一种通过循环调制在Transformer中实现深度表达的方法，以解决扩展语言模型时表达性与内存效率之间的权衡问题。
- **原始摘要**: arXiv:2608.15062v2 Announce Type: replace 
Abstract: Scaling transformer language models creates an inherent tension between expressivity and memory efficiency. While unique weights across layers pres...

### 68. Palmyra x6 Technical Report: An Agentic, Tool-Use Model Post-Trained via Anchored Supervised Fine-Tuning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.16620
- **AI 摘要**: Palmyra x6是一个面向企业代理任务的大型语言模型，通过对混合专家基础模型进行锚定监督微调，使用紧凑的合成工具使用轨迹语料库，并采用Muon+Adam混合优化器。训练策略保守且受控，包括626条轨迹、单轮训练、低学习率和KL锚定。
- **原始摘要**: arXiv:2608.16620v2 Announce Type: replace 
Abstract: Palmyra x6 is a large language model optimized for use with enterprise-oriented agentic tasks. The model was built by post-training a Mixture-of-Ex...

### 69. Evidence of conceptual mastery in the application of rules by Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2503.00992
- **AI 摘要**: 本文通过五项实验测试13个大语言模型在应用规则时的概括能力，包括规则文本与目的指向不同结果的情况，以探究模型是否真正掌握概念而非仅记忆或依赖偶然特征。
- **原始摘要**: arXiv:2503.00992v3 Announce Type: replace-cross 
Abstract: Background. Evidence that large language models (LLMs) reproduce human judgments does not establish conceptual mastery: the correspondence ma...

### 70. Self-Distillation as a Performance Recovery Mechanism for LLMs: Counteracting Compression and Catastrophic Forgetting
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.15794
- **AI 摘要**: 本文提出基于自蒸馏微调（SDFT）的性能恢复框架，用于解决大语言模型在监督微调、量化和剪枝中出现的灾难性遗忘和性能下降问题，有效恢复模型能力。
- **原始摘要**: arXiv:2604.15794v2 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs) have achieved remarkable success, underpinning diverse AI applications. However, they often suffer from performa...

### 71. Decided Upstream, Written Late: Locating and Pricing the Cross-Lingual Refusal Circuit of a Multilingual MoE
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.08032
- **AI 摘要**: 本文研究多语言混合专家模型的安全对齐不均问题，发现模型对英语有害请求的拒绝机制在低资源语言中失效。通过机制分析，定位到跨语言拒绝电路，并探讨其定价与定位，为提升多语言模型安全性提供见解。
- **原始摘要**: arXiv:2608.08032v2 Announce Type: replace-cross 
Abstract: Safety alignment in multilingual models is uneven: a model that reliably refuses a harmful request in English will often comply with the same...

### 72. Geometric and Behavioral Stratification in Transformer Residual Streams
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12447
- **AI 摘要**: 本文研究了Transformer模型残差流中的几何与行为分层现象，发现预测方向作为内容定义的优先锚点，残差流变异在几何上围绕该锚点呈现特定结构。
- **原始摘要**: arXiv:2608.12447v2 Announce Type: replace-cross 
Abstract: Trained transformer models develop privileged bases: coordinate axes whose statistics differ from the rest of the residual stream. But what k...

### 73. Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12746
- **AI 摘要**: 多模态大语言模型中的对象幻觉源于语言先验和语料共现偏差超过视觉证据。现有解码干预仅在短标题中有效，监督微调虽延长标题但超40%仍提及不存在的对象。本文提出双流跨锚点校正方法，并探讨对象级锚点的领域限制。
- **原始摘要**: arXiv:2608.12746v2 Announce Type: replace-cross 
Abstract: Object hallucination in multimodal large language models arises when language priors and corpus co-occurrence bias outweigh the visual eviden...

### 74. SignalReasoner: Assessing the Upper Bound of 3B Models for Signal Mathematical Reasoning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17301
- **AI 摘要**: 本文探讨了将强化微调策略应用于Qwen2.5-3B-Base模型，以解决研究生级别的信号数学问题，评估了3B模型在信号推理上的上限，并展示了监督思维链微调与可验证奖励强化学习的效果。
- **原始摘要**: arXiv:2608.17301v1 Announce Type: new 
Abstract: Post-training with supervised chain-of-thought fine-tuning and reinforcement learning from verifiable rewards has substantially improved the mathematic...

### 75. LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17393
- **AI 摘要**: 本文提出LEGO-RL，一种面向编码智能体的强化学习框架，旨在解决智能体执行环境与策略梯度训练之间的错配问题，包括环境崩溃、奖励黑客和训练推理差异，以提升训练效果。
- **原始摘要**: arXiv:2608.17393v1 Announce Type: new 
Abstract: Reinforcement learning for coding agents increasingly relies on long-running agent harnesses to manage tool integration, repository contexts, and execu...

### 76. Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17499
- **AI 摘要**: 本文提出面向多轮用户交互的智能体改进方法，认为下一轮用户输入不仅是上下文，还提供关于前一轮用户-用户段落的局部时序反馈信号。引入反馈感知机制，以提升智能体在对话与工具使用中的协调能力。
- **原始摘要**: arXiv:2608.17499v1 Announce Type: new 
Abstract: User-facing tool agents must coordinate dialogue and tool use as user goals unfold over multiple turns. Yet interactive reinforcement learning typicall...

### 77. Towards Zero-Shot Task Transfer with Neurosymbolic World Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17959
- **AI 摘要**: 本文提出一种神经符号世界模型，用于零样本任务迁移。该方法结合符号表示与神经网络，学习可解释的潜在表征，使模型能泛化到新任务，优于现有任务依赖的模型。
- **原始摘要**: arXiv:2608.17959v1 Announce Type: new 
Abstract: State-of-the-art model-based reinforcement learning methods learn neural world models that allow policy improvement by planning in a latent space, with...

### 78. From Abductive Explanations to Global Logical Rules for Node Classification in SGCs
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17103
- **AI 摘要**: 本文提出从图神经网络（GNN）节点分类的溯因解释中提取全局逻辑规则的方法。针对现有方法如LogicXGNN依赖的子图可能包含冗余结构信息的问题，该方法旨在生成更简洁、通用的规则，提升解释的全局性和可理解性。
- **原始摘要**: arXiv:2608.17103v1 Announce Type: cross 
Abstract: Graph Neural Networks (GNNs) have achieved remarkable performance in node classification tasks, motivating growing interest in methods capable of exp...

### 79. Q-Learning With World Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17163
- **AI 摘要**: 本文探讨了基于世界模型的离策略强化学习，通过预测状态变化而非仅动作，提升样本效率，并应用于视觉-语言-动作模型的微调，以生成可靠高效策略。
- **原始摘要**: arXiv:2608.17163v1 Announce Type: cross 
Abstract: Off-policy reinforcement learning (RL) has become increasingly sample-efficient, enabling applications such as RL fine-tuning of Vision-Language-Acti...

### 80. Task Specialization Fine-Tuning for Contextual Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17180
- **AI 摘要**: 本文提出一种上下文强化学习的新方法：先预训练一个具有良好初始性能的策略，再针对不同任务进行微调，以替代从零开始的多任务或多策略训练，实现任务覆盖最大化。
- **原始摘要**: arXiv:2608.17180v1 Announce Type: cross 
Abstract: Contextual Reinforcement Learning (CRL) seeks to generalize classical RL by maximizing task coverage across a context space of related tasks. While p...

### 81. Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17253
- **AI 摘要**: 本文提出Co-RL方法，通过多智能体强化学习中的多样化群体，使无监督推理能力自然涌现，减少对人工标注奖励的依赖。
- **原始摘要**: arXiv:2608.17253v1 Announce Type: cross 
Abstract: Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its strongest succ...

### 82. Rethinking Irregular Time Series Forecasting from the Perspective of Basis Functions
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17284
- **AI 摘要**: 不规则时间序列预测在医疗和气象等领域至关重要，但稀疏观测和非均匀采样使其充满挑战。现有方法将不规则观测聚合为固定维度估计响应系数，本文从基函数视角重新思考该问题，提出新方法以提升预测准确性。
- **原始摘要**: arXiv:2608.17284v1 Announce Type: cross 
Abstract: Irregular time series forecasting is crucial in many domains, such as healthcare and meteorological observation. However, due to the inherent charact...

### 83. MoFE: A Novel Mixture-of-Experts Framework with Fourier Neural Operators for Cryptocurrency Forecasting
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17342
- **AI 摘要**: MoFE是一个结合傅里叶神经算子与混合专家框架的加密货币预测模型，旨在解决价格预测中的非平稳性、突变和多尺度依赖问题，减少传统模型的相位滞后。
- **原始摘要**: arXiv:2608.17342v1 Announce Type: cross 
Abstract: Forecasting cryptocurrency prices remains a formidable challenge due to inherent non-stationarity, abrupt regime shifts, and multi-scale stochastic d...

### 84. Inductively Scalable, Single-Step Neural Surrogates for Wave-Scattering Inverse Problems
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17344
- **AI 摘要**: 本文提出一种可归纳扩展的单步神经网络替代模型，用于波散射逆问题，突破了传统非递归单步替代模型仅能处理少量变量的限制，实现更快求解。
- **原始摘要**: arXiv:2608.17344v1 Announce Type: cross 
Abstract: Neural network surrogates are an emerging alternative to traditional electromagnetic wave simulators like finite-difference time-domain (FDTD); their...

### 85. Integrating Novelty and Surprise for Experience Prioritization and Exploration in Image-Based Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17373
- **AI 摘要**: 本文提出一种结合新颖性和惊喜度的经验优先级排序与探索机制，用于图像强化学习，以提高样本效率。通过优先选择信息丰富的经验并鼓励有效探索，减少冗余更新，加速学习过程。
- **原始摘要**: arXiv:2608.17373v1 Announce Type: cross 
Abstract: Sample efficiency is a central challenge in reinforcement learning (RL), particularly in image-based domains where agents must learn from high-dimens...

### 86. Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18008
- **AI 摘要**: 本文形式化了混合LLM规划器与RL控制器的架构，将其建模为目标增强马尔可夫决策过程，并证明当LLM的逐状态进度分数作为有界势函数时，所得到的塑形项能保持最优策略集不变。
- **原始摘要**: arXiv:2608.18008v1 Announce Type: cross 
Abstract: Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is oft...

### 87. Solving nonconvex Hamilton--Jacobi--Isaacs equations with PINN-based policy iteration
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2025年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2507.15455
- **AI 摘要**: 提出一种无网格策略迭代框架，结合经典动态规划与物理信息神经网络，求解随机微分博弈和鲁棒控制中的高维非凸Hamilton-Jacobi-Isaacs方程。方法交替求解固定策略下的线性二阶PDE，并通过逐点极小极大优化更新控制。
- **原始摘要**: arXiv:2507.15455v3 Announce Type: replace-cross 
Abstract: We propose a mesh-free policy iteration framework that combines classical dynamic programming with physics-informed neural networks (PINNs) t...

### 88. VISOR: Agentic Visual Retrieval-Augmented Generation via Iterative Search and Over-horizon Reasoning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.09508
- **AI 摘要**: 本文提出VISOR，一种智能体视觉检索增强生成框架，通过迭代搜索和超视距推理解决视觉证据稀疏和跨页推理难题，提升复杂视觉文档问答能力。
- **原始摘要**: arXiv:2604.09508v3 Announce Type: replace-cross 
Abstract: Visual Retrieval-Augmented Generation (VRAG) empowers Vision-Language Models to retrieve and reason over visually rich documents. To tackle c...

### 89. BRo-JEPA: Learning Modular Transformations in Latent Space
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.01372
- **AI 摘要**: BRo-JEPA研究神经网络能否从视觉输入学习代数规则，通过JEPA世界模型结合模块化变换，在MNIST上执行模运算，优于基线，能泛化到未见操作。
- **原始摘要**: arXiv:2606.01372v2 Announce Type: replace-cross 
Abstract: Can neural networks learn algebraic rules from visual inputs, or do they merely fit observed patterns? We study this question using MNIST (or...

### 90. NICE: Scale-Stable Perturbations for Graph Neural Network Explanations via Noise Corruption
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.16038
- **AI 摘要**: 本文提出NICE方法，通过噪声破坏生成尺度稳定的扰动，用于图神经网络解释。该方法减少扰动引起的分布偏移，提高解释可靠性，并稳定模型预测。
- **原始摘要**: arXiv:2608.16038v2 Announce Type: replace-cross 
Abstract: Post-hoc Graph Neural Network (GNN) explainers commonly follow a Perturb-Query paradigm, inferring the importance of graph elements based on...

### 91. Data-DPO: Direct Preference Optimization for Target Model Data Selection in LLM Post-Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.16926
- **AI 摘要**: Data-DPO提出面向目标模型的SFT数据选择方法，通过直接偏好优化考虑数据与模型能力分布的兼容性，从大规模候选中选取高效样本，降低训练成本并保持性能。
- **原始摘要**: arXiv:2608.16926v1 Announce Type: new 
Abstract: Data selection in supervised fine-tuning aims to select a small set of effective samples from large-scale candidate data, reducing training cost while...

### 92. EMAN: Optimization-Driven Capacity Growth through Path Emergence in Multi-Task Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.16930
- **AI 摘要**: 现有多任务学习方法依赖硬共享、多路径或专家、自适应共享及动态扩展，但容量变化受限于预定义结构或任务边界。本文提出EMAN方法，使网络从单路径计算出发，仅在出现持续优化证据时生长新独立路径，实现优化驱动的容量增长。
- **原始摘要**: arXiv:2608.16930v1 Announce Type: new 
Abstract: Existing multi-task learning methods rely on hard sharing, multiple paths or experts, adaptive sharing, and dynamic expansion. However, their capacity...

### 93. DOW-KE: Anchor-Free Multi-Layer Knowledge Editing via Direct End-to-End Weight Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.16932
- **AI 摘要**: 本文提出DOW-KE方法，用于多层知识编辑。现有方法先优化锚点再逐层更新权重，但未优化联合效应。DOW-KE通过直接端到端权重优化，改进知识编辑效果。
- **原始摘要**: arXiv:2608.16932v1 Announce Type: new 
Abstract: Multi-layer locate-then-edit methods for knowledge editing first optimize target residual-stream activations (anchors) at selected layers, then realize...

### 94. Causal Discovery in Equal Variance Linear Gaussian DAGs via SURE-Tuned Ridge Regression
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17132
- **AI 摘要**: 本文提出一种基于SURE调优岭回归的等方差线性高斯DAG因果发现方法，解决连续优化方法在样本有限和计算受限场景下的不足，通过迭代梯度下降恢复结构方程模型的有向无环图。
- **原始摘要**: arXiv:2608.17132v1 Announce Type: new 
Abstract: Recovering the directed acyclic graph (DAG) of a structural equation model (SEM) from observational data is a central problem in causal discovery. The...

### 95. Iterative tensor network transformations for element-wise evaluation of elementary and filtering functions
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17135
- **AI 摘要**: 本文提出迭代张量网络变换（ITNTs），一种通用算法框架，用于对张量训练（TT）编码的数据进行逐元素评估初等和非线性滤波函数，克服了张量网络在非线性操作上的困难。
- **原始摘要**: arXiv:2608.17135v1 Announce Type: new 
Abstract: Tensor networks are powerful formats for compressing large-scale data. However, their application to general data processing has been limited by the di...

### 96. How smoothing the affinity matrix affects neighborhood preservation in t-SNE
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17190
- **AI 摘要**: 本文研究t-SNE中亲和矩阵的锐度对邻域保持的影响，通过平滑概率分布来改进降维效果。
- **原始摘要**: arXiv:2608.17190v1 Announce Type: new 
Abstract: Dimensionality reduction methods are instrumental to visualize high-dimensional data, and t-SNE stands as one of the most widely used methods due to it...

### 97. Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17268
- **AI 摘要**: 本文通过分析课程学习在大型语言模型后训练中引发的优化动态，探讨其在不同推理任务上效果差异的原因，揭示决定课程学习有效性的关键因素。
- **原始摘要**: arXiv:2608.17268v1 Announce Type: new 
Abstract: Curriculum learning has been widely adopted in the post-training of large language models by organizing training data from easy to hard. However, its e...

### 98. Abra: Scaling Diffusion Image Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17286
- **AI 摘要**: 本文提出Abra，一个受控的流匹配Transformer家族，用于文本到图像扩散模型的系统缩放定律研究，计算预算从10^19到10^22 FLOPs，远超以往工作，旨在指导视觉生成模型的训练。
- **原始摘要**: arXiv:2608.17286v1 Announce Type: new 
Abstract: Compute-optimal scaling laws guide the training of frontier language models yet remain largely unexplored for visual generation. We present a systemati...

### 99. Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17310
- **AI 摘要**: 本文提出Agentic ESOpt方法，利用进化策略微调长时程LLM智能体，以极低GPU需求替代传统强化学习，解决其训练成本高和信用分配难的问题。
- **原始摘要**: arXiv:2608.17310v1 Announce Type: new 
Abstract: Reinforcement Learning (RL) has been promising in single-turn LLM fine-tuning. However, long-horizon agentic reasoning introduces increasingly branchin...

### 100. GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17411
- **AI 摘要**: 本文提出GUPO方法，针对GRPO在LLM后训练中组梯度冲突导致策略更新低效的问题，通过梯度不确定性感知的策略优化来改进训练效果。
- **原始摘要**: arXiv:2608.17411v1 Announce Type: new 
Abstract: Group Relative Policy Optimization (GRPO) has become a widely used approach for post-training Large Language Models (LLMs) for reasoning. In GRPO, the...

### 101. Efficient Resource Optimization for Split Federated Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17849
- **AI 摘要**: 分割联邦学习（SFL）在边缘模型训练中具有优势，但涉及离散决策变量和资源分配，形成混合整数问题。现有优化方案要么启发式，要么计算效率低，难以应对大规模用户。本文旨在解决这一局限性。
- **原始摘要**: arXiv:2608.17849v1 Announce Type: new 
Abstract: Split federated learning (SFL) has emerged as a powerful paradigm for model training at the edge. However, SFL inherently involves discrete decision va...

### 102. Optimize Your Sampling: Tuned Diffusion Sampling with Bayesian Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18040
- **AI 摘要**: 本文提出利用贝叶斯优化来调整扩散模型的采样时间步，以提升生成效率和质量，相比传统固定采样策略更具优势。
- **原始摘要**: arXiv:2608.18040v1 Announce Type: new 
Abstract: Sampling from a diffusion model typically requires many forward passes through a large neural network, making generation computationally expensive. Whi...

### 103. Policy Optimization and Statistical Inference for Online Contextual Matrix Games
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17173
- **AI 摘要**: 本文研究在线决策中动态上下文与战略互动的结合问题，如竞争定价中酒店需考虑上下文因素和对手反应。现有方法仅处理单方面，本文提出在线上下文矩阵博弈的策略优化与统计推断方法。
- **原始摘要**: arXiv:2608.17173v1 Announce Type: cross 
Abstract: Online decision making often requires navigating a landscape shaped by both dynamic contexts and strategic interactions. In competitive pricing, for...

### 104. Adaptive surrogate modeling for high-dimensional spatio-temporal output
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17250
- **AI 摘要**: 本文提出一种自适应代理建模方法，用于处理高维时空输出的问题。该方法旨在替代计算昂贵的物理模型，在不确定性量化和优化等需要大量评估的分析中提高计算效率。
- **原始摘要**: arXiv:2608.17250v1 Announce Type: cross 
Abstract: This paper develops an adaptive surrogate modeling method for problems with very high-dimensional spatio-temporal outputs. The analysis of spatio-tem...

### 105. Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17423
- **AI 摘要**: 本文提出Prism-GRPO，一种加速视觉-语言-动作（VLA）策略强化学习的方法。针对GRPO中同结果组（全成功或全失败）导致零优势被丢弃的问题，通过拆分这些组来更高效利用采样，提升训练速度。
- **原始摘要**: arXiv:2608.17423v1 Announce Type: cross 
Abstract: GRPO is increasingly used for reinforcement learning of vision-language-action (VLA) policies because, unlike PPO, it does not require training a cri...

### 106. Online Generalized Sparse Regression: How Does Overparametrization Help?
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17466
- **AI 摘要**: 本文研究在线广义稀疏回归问题，探讨过参数化如何帮助应对动态正则化调整、存储内存管理及实时计算等挑战，提出闭式更新方法以提升在线学习效率。
- **原始摘要**: arXiv:2608.17466v1 Announce Type: cross 
Abstract: Regularized sparse regression has been extensively studied in the offline setting, but online formulation remains relatively under-explored. This gap...

### 107. Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17687
- **AI 摘要**: 本文探讨利用混合专家（MoE）模型检测大语言模型幻觉。现有方法多在答案或句子层面检测，而本文提出在token级别进行检测，以定位幻觉片段并支持细粒度干预。研究表明MoE块包含强幻觉检测信号。
- **原始摘要**: arXiv:2608.17687v1 Announce Type: cross 
Abstract: Despite their widespread use, Large Language Models (LLMs) remain limited by a fundamental problem: the generation of plausible but false content, kn...

### 108. Gradient Heterogeneity Complements Hessian Heterogeneity in Transformer Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2502.00213
- **AI 摘要**: 本文通过梯度异质性视角分析Transformer优化，发现梯度异质性补充了Hessian异质性，解释了Adam优于SGD的原因，为优化器选择提供理论依据。
- **原始摘要**: arXiv:2502.00213v5 Announce Type: replace 
Abstract: Transformers are difficult to optimize with stochastic gradient descent (SGD) and largely rely on adaptive optimizers such as Adam. Despite extensi...

### 109. Scientific Machine Learning of Chaotic Systems Learns Reduced-Order Equations for Neural Populations
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2507.03631
- **AI 摘要**: 本文提出PEM-UDE方法，结合预测误差与通用微分方程，从含噪混沌数据中发现控制方程，平滑优化问题，实现可解释建模。
- **原始摘要**: arXiv:2507.03631v5 Announce Type: replace 
Abstract: Extracting interpretable mathematical models from complex dynamical systems is difficult, especially for chaotic dynamics observed with noisy exper...

### 110. Exact Reformulation and Optimization for Direct Metric Optimization in Binary Imbalanced Classification
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2507.15240
- **AI 摘要**: 本文针对不平衡分类中直接度量优化问题，提出精确重构与优化方法，以处理类别重要性不同或需达到指定指标的场景，超越传统平衡准确率优化。
- **原始摘要**: arXiv:2507.15240v2 Announce Type: replace 
Abstract: For classification with imbalanced class frequencies, i.e., imbalanced classification (IC), standard accuracy is known to be misleading as a perfor...

### 111. TiMi: Empower Time Series Transformers with Multimodal Mixture of Experts
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.21693
- **AI 摘要**: 本文提出TiMi框架，通过多模态混合专家技术增强时间序列Transformer，有效整合文本等模态信息，解决模态对齐难题，提升预测准确性。
- **原始摘要**: arXiv:2602.21693v2 Announce Type: replace 
Abstract: Multimodal time series forecasting has garnered significant attention for its potential to provide more accurate predictions than traditional singl...

### 112. TabCausal: Pretraining Across Causal Environments for Tabular Causal Discovery
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.31156
- **AI 摘要**: 本文提出TabCausal，一种用于表格因果发现的预训练模型，通过跨因果环境预训练，直接映射数据集到因果图，避免逐数据集搜索，提升因果发现效率与准确性。
- **原始摘要**: arXiv:2605.31156v2 Announce Type: replace 
Abstract: Causal discovery aims to recover directed causal relations from observational and interventional data, providing a basis for mechanistic understand...

### 113. Online Learning of Scale Parameters in Score-Driven Filters
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.09218
- **AI 摘要**: 本文研究得分驱动滤波器中尺度参数（增益）的在线学习，将其视为决策变量，通过选择增益来优化一步预测密度，实现参数的自适应更新。
- **原始摘要**: arXiv:2608.09218v2 Announce Type: replace 
Abstract: Score-driven filters update a time-varying parameter by multiplying a scaled log-likelihood score by a scale parameter that controls the magnitude...

### 114. Federated Compositional Muon Optimizer for Matrix-Wise Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12710
- **AI 摘要**: 本文提出FedCoMuon优化器，用于解决分布式矩阵组合优化问题。该优化器基于Muon，适用于矩阵模型，并针对层次结构问题进行了改进，在AI领域具有应用价值。
- **原始摘要**: arXiv:2608.12710v2 Announce Type: replace 
Abstract: Muon, a more recently developed optimizer, is useful for matrix-wise models in AI areas. Although many works have studied Muon and its variants, th...

### 115. On Stability in Optimistic Bilevel Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2024年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2408.13323
- **AI 摘要**: 本文研究乐观双层优化问题中解对数据变化的稳定性。通过构造提升公式，在温和假设下（不涉及凸性或光滑性）实现理想稳定性，适用于含整数约束和析取约束的上下层问题。
- **原始摘要**: arXiv:2408.13323v3 Announce Type: replace-cross 
Abstract: Solutions of bilevel optimization problems tend to suffer from instability under changes to problem data. In the optimistic setting, we const...

### 116. Large Language Models: A Mathematical Formulation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.22170
- **AI 摘要**: 本文为大型语言模型（LLM）提供数学框架，涵盖文本序列的token编码、下一token预测模型的架构定义，以及模型的学习过程，旨在从数学角度系统化理解LLM。
- **原始摘要**: arXiv:2601.22170v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) process and predict sequences containing text to answer questions, and address tasks including document summariz...

### 117. Fermi-Dirac thermal measurements: A framework for quantum hypothesis testing and semidefinite optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.04061
- **AI 摘要**: 本文提出费米-狄拉克热测量框架，将量子测量算子特征值约束与泡利不相容原理类比，用于量子假设检验和半定优化，为量子态信息恢复提供新方法。
- **原始摘要**: arXiv:2603.04061v2 Announce Type: replace-cross 
Abstract: Quantum measurements are the means by which we recover messages encoded into quantum states. They are at the forefront of quantum hypothesis...

### 118. Non-KKT Accumulation in Entropic Mirror Descent
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.01658
- **AI 摘要**: 本文研究镜像下降算法中累积点是否必然满足KKT条件。通过构造反例，证明在Legendre核下，有界镜像下降序列的累积点可能不满足KKT平稳性，解决了该领域的长期难题。
- **原始摘要**: arXiv:2608.01658v3 Announce Type: replace-cross 
Abstract: For mirror descent generated by a Legendre kernel, perhaps one of the most basic question in optimization is this: must every accumulation po...

### 119. Efficient Hessian-Free Methods for Multi-Objective Bilevel Optimization with Nonconvex Lower Level
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12704
- **AI 摘要**: 多目标双层优化在AI领域应用广泛，但现有方法依赖凸下层问题。本文针对非凸下层问题，提出高效的无Hessian方法，解决实际中普遍存在的非凸多目标双层学习问题。
- **原始摘要**: arXiv:2608.12704v2 Announce Type: replace-cross 
Abstract: Multi-objective bilevel optimization has wide applications in the AI area such as automated learning and multi-task meta-learning. Although r...

### 120. Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17347
- **AI 摘要**: 本文提出即时回合重复（IER）机制，受人类学习中的重复原理启发，通过在环境交互中立即重复成功回合的动作序列，提升强化学习的样本效率。该方法简单新颖，与常规方法不同。
- **原始摘要**: arXiv:2608.17347v1 Announce Type: cross 
Abstract: Repetition is a fundamental mechanism in human learning, where revisiting successful experiences strengthens memory, consolidates skills, and improve...

### 121. Qwen-Image-Edit: Image Editing with Higher Quality and Efficiency
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image-edit/
- **AI 摘要**: Qwen团队推出Qwen-Image-Edit，基于20B参数的Qwen-Image模型，扩展了文本渲染能力至图像编辑，支持精确文本编辑。该模型同时利用Qwen2.5-VL进行视觉语义控制和VAE编码器进行外观控制，实现高质量高效编辑。
- **原始摘要**: QWEN CHAT GITHUB HUGGING FACE MODELSCOPE DISCORD
We are excited to introduce Qwen-Image-Edit, the image editing version of Qwen-Image. Built upon our 20B Qwen-Image model, Qwen-Image-Edit successfully...

### 122. Qwen-Image: Crafting with Native Text Rendering
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image/
- **AI 摘要**: Qwen团队发布Qwen-Image，一个200亿参数的MMDiT图像基础模型，在复杂文本渲染和精确图像编辑方面取得显著进展，支持多行布局、段落级语义和细粒度细节，并支持字母文字。
- **原始摘要**: GITHUB HUGGING FACE MODELSCOPE DEMO DISCORD
We are thrilled to release Qwen-Image, a 20B MMDiT image foundation model that achieves significant advances in complex text rendering and precise image edi...

### 123. GSPO: Towards Scalable Reinforcement Learning for Language Models
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/gspo/
- **AI 摘要**: 本文提出GSPO，一种面向语言模型的可扩展强化学习算法，旨在解决现有RL算法（如GRPO）在长训练中的不稳定性和模型崩溃问题，以提升训练稳定性和性能。
- **原始摘要**: PAPER DISCORD
Introduction Reinforcement Learning (RL) has emerged as a pivotal paradigm for scaling language models and enhancing their deep reasoning and problem-solving capabilities. To scale RL, t...

### 124. Qwen-MT: Where Speed Meets Smart Translation
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-mt/
- **AI 摘要**: Qwen-MT更新基于Qwen3，利用多语言和翻译数据，结合强化学习，提升翻译准确性和流畅度，支持92种语言。
- **原始摘要**: DEMO API DISCORD
Introduction Here we introduce the latest update of Qwen-MT (qwen-mt-turbo) via Qwen API. This update builds upon the powerful Qwen3, leveraging trillions multilingual and translation...

### 125. New Kimi K2 Models & Updated Pricing
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/Kimi_API_Newsletter
- **AI 摘要**: 文章介绍了Kimi K2模型的更新及其定价调整，可能涉及新功能、性能提升或价格变化，旨在为用户提供更优的AI服务体验。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
