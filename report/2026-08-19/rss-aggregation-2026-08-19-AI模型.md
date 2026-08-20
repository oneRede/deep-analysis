# RSS 聚合报告 - AI模型

**生成时间**: 2026-08-20 15:19:28
**文章数量**: 112 篇

---

### 1. Same GRPO recipe on three from-scratch LLMs (353M/316M/672M) gave three different outcomes, with no clean relationship to scale [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T21:30:26+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vszsit/same_grpo_recipe_on_three_fromscratch_llms/
- **AI 摘要**: 作者从零训练了三个不同规模的LLM（353M/316M/672M），使用相同的SFT和GRPO后训练流程，发现GRPO对两个较大模型产生负面影响，且结果与模型规模无清晰关系，原因不明。
- **原始摘要**: I trained three LLMs from scratch in raw PyTorch then post-trained each one with SFT and then GRPO. Same process every time: same synthetic arithmetic curriculum, same reward function, same hyperparam...

### 2. How much of the weight-space perception gap is actually symmetry? Evidence from ~1.8M fitted SIRENs [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T19:24:12+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vswdnf/how_much_of_the_weightspace_perception_gap_is/
- **AI 摘要**: 研究探讨权重空间感知中对称性对语义读取的影响，通过约180万拟合SIRENs实验，分离参数对称性与实际感知差距，揭示共享初始化下语义读取有效而独立拟合时失效的原因。
- **原始摘要**: I’ve been looking at a fairly basic question in weight-space learning that I don’t think gets separated cleanly enough: Why does reading semantics directly from neural network weights work pretty well...

### 3. Trained an diffusion model that runs on 264KB of RAM [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-18T09:26:21+00:00 (2 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vrk7t5/trained_an_diffusion_model_that_runs_on_264kb_of/
- **AI 摘要**: 作者训练了一个可在264KB RAM上运行的扩散模型，展示了极低资源消耗的AI模型可能性，可能涉及模型压缩或轻量化技术。
- **原始摘要**: I recently bought a Shrike lite which has got 264KB of SRAM. I decided to train an image generation model that generates 32*32 pixel images. The microcontroller also has an FPGA onboard which I used t...

### 4. Revisiting the Efficient Channel Attention paper (2019, 12k citations) - the central hypothesis isn't quite right [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-16T10:13:44+00:00 (4 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/
- **AI 摘要**: 文章重新审视了高效通道注意力（ECA）论文，指出其核心假设可能不完全正确。ECA作为SE的改进，通过一维卷积避免降维，效果优于SE，但作者认为其跨通道交互的假设存在问题。
- **原始摘要**: ECA was positioned as a successor to SE. The idea behind ECA is quite simple. Unlike SE which reduces the channel means into a smaller hidden layer, it directly uses a 1d convolution kernel on the cha...

### 5. How can we solve long-range recall in linear attention? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-16T07:47:09+00:00 (4 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/
- **AI 摘要**: 作者在DNA序列建模中采用线性注意力处理长序列，但遇到长程召回问题。在Needle-in-a-Haystack基准测试中，模型表现不佳，引发对线性注意力长程依赖能力的探讨。
- **原始摘要**: Recently, I started working on DNA sequence modeling and decided to explore linear attention, mainly because DNA sequences can easily reach 1M tokens, making standard softmax attention extremely expen...

### 6. Survival of the Fitted: Qwen3.6-27B’s Jacobian lens reads and steers Qwen3.8-27B with zero refitting [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-15T18:24:00+00:00 (4 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vpa5cv/survival_of_the_fitted_qwen3627bs_jacobian_lens/
- **AI 摘要**: 本文介绍了一种名为Jacobian lens的技术，能够在不重新训练的情况下，利用Qwen3.6-27B模型读取并引导Qwen3.8-27B模型的行为，实现跨模型的知识迁移和操控，展示了模型间可移植性的新方法。
- **原始摘要**: Interpretability lenses get fitted to one exact checkpoint, and as far as I can tell nobody had tested what a version update does to one. So this was my question: when a model line updates, does the f...

### 7. BDH-CQ: IN-CONTEXT LEARNING WITH RECURRENT LATENT REASONING [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-15T06:18:15+00:00 (5 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vov5r5/bdhcq_incontext_learning_with_recurrent_latent/
- **AI 摘要**: 本文提出BDH-CQ方法，通过循环潜在推理增强上下文学习能力，在少样本场景下提升模型性能。
- **原始摘要**: We introduce BDH-CQ, a reasoning system that brings these capabilities together. Demonstrations of a previously unseen task update recurrent memory; the query is then solved through iterative computat...

### 8. I compiled Doom's renderer into a 21B-parameter transformer -- no training anywhere [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-14T15:50:11+00:00 (5 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1voazhm/i_compiled_dooms_renderer_into_a_21bparameter/
- **AI 摘要**: 作者将Doom渲染算法移植到21B参数Transformer中，通过自研编译器将计算图转换为模型权重，无需训练即可运行，生成的标准检查点可直接在Hugging Face加载。
- **原始摘要**: This is the project my last two posts were building towards (this is the last of this silliness). I ported the Doom rendering algorithm to run inside a transformer. Instead of training a model, I used...

### 9. Intel's next-gen Nova Lake chips may skip game-boosting X3D cache rival for mobile SKUs and debut on Razor Lake-HX instead, leaker claims — new rumor says Razor Lake family reportedly uses TSMC's N2X node
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Tue, 18 Aug 2026 14:18:57 +0000 (2 天前)
- **类型**: news
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://www.tomshardware.com/pc-components/cpus/intels-next-gen-nova-lake-chips-may-skip-bllc-for-mobile-skus-and-debut-on-razor-lake-hx-instead-leaker-claims-new-rumor-says-razor-lake-family-reportedly-uses-tsmcs-n2x-node
- **AI 摘要**: 据传英特尔下一代Nova Lake台式机芯片将独占bLLC缓存技术，对标AMD X3D，而移动端则可能由Razor Lake-HX首发，并采用台积电N2X工艺。
- **原始摘要**: Nova Lake desktop CPUs look to be the exclusive recipient of bLLC, Intel's answer to AMD's X3D, as the company looks to debut bLLC on mobile with Razor Lake-HX, and possibly Razor Lake-AX. As such, th...

### 10. Multi-Vector (Late Interaction) Embedding Models with Sentence Transformers
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Tue, 18 Aug 2026 00:00:00 GMT (2 天前)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/multi-vector-encoder
- **AI 摘要**: 文章介绍多向量（后期交互）嵌入模型在句子转换器中的应用，通过对比查询与文档的token级相似度提升检索精度，并讨论其实现与性能权衡。

### 11. State of Open Models: Summer 2026 Observations
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Fri, 14 Aug 2026 00:00:00 GMT (6 天前)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/state-of-open-models-summer-2026
- **AI 摘要**: 文章概述了2026年夏季开源模型的最新进展，包括模型性能提升、社区生态发展及未来趋势，强调开源在AI领域的重要性和影响力。

### 12. v1.6.0: Mistrall goes Small 3.1 with vision
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2025-03-20T15:03:08Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.6.0
- **AI 摘要**: Mistral推理库v1.6.0版本发布，新增对Mistral Small 3.1模型的支持，该模型具备视觉能力，同时修复了缺失换行符的问题。
- **原始摘要**: What's Changed Missing new line by @theophilegervet in #234 Add support to Mistral Small 3.1 by @juliendenize in #239 Remove file refs by @juliendenize in #240 Release 1.6.0 by @juliendenize in #241 N...

### 13. v1.4.0: Pixtral 👀
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-09-13T13:10:17Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.4.0
- **AI 摘要**: Mistral AI发布v1.4.0版本，推出Pixtral多模态模型，支持视觉能力。用户可通过pip升级mistral_inference库（>=1.4.0）并使用Hugging Face下载模型。
- **原始摘要**: Pixtral Mistral models can now 👀 ! pip install --upgrade mistral_inference # >= 1.4.0 Download: from huggingface_hub import snapshot_download from pathlib import Path mistral_models_path = Path.home()...

### 14. v1.3.0 Mistral-Nemo
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-18T15:45:30Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.3.0
- **AI 摘要**: Mistral与NVIDIA合作推出Mistral-Nemo模型，提供安装和下载指南，用户可通过pip安装mistral-inference库获取该模型。
- **原始摘要**: Welcome Mistral-Nemo from Mistral 🤝 NVIDIA Read more about Mistral-Nemo here. Install pip install mistral-inference>=1.3.0 Download export NEMO_MODEL=$HOME/12B_NEMO_MODEL wget https://models.mistralcd...

### 15. v1.2.0 Add Mamba
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-16T18:41:37Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.2.0
- **AI 摘要**: Mistral AI 发布 v1.2.0 更新，新增 Codestral-Mamba 和 Mathstral 模型。Codestral-Mamba 基于 Mamba 架构，需安装相关依赖包。文章提供了安装和下载指南。
- **原始摘要**: Welcome 🐍 Codestral-Mamba and 🔢 Mathstral pip install mistral-inference>=1.2.0 Codestral-Mamba pip install packaging mamba-ssm causal-conv1d transformers Download export MAMBA_CODE=$HOME/7B_MAMBA_CODE...

### 16. v1.0.4 - Mistral-inference
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-05-24T18:32:35Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.0.4
- **AI 摘要**: Mistral-inference是Mistral官方推理库，支持7B、8x7B、8x22B等模型。可通过pip安装，并提供了简单的运行方式。
- **原始摘要**: Mistral-inference is the official inference library for all Mistral models: 7B, 8x7B, 8x22B. Install with: pip install mistral-inference Run with: from mistral_inference.model import Transformer from...

### 17. TTSD-FAR: Test-Time Self-Distillation with Fisher-Anchored Restoration for Missing-Modality Emotion Recognition in LVLMs
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18386
- **AI 摘要**: 本文提出TTSD-FAR方法，用于大型视频语言模型在多模态情感识别中处理测试时模态缺失问题。通过测试时自蒸馏和Fisher锚定恢复，缓解部分观测导致的分布偏移，提升鲁棒性。
- **原始摘要**: arXiv:2608.18386v1 Announce Type: new Abstract: Large video-language models (LVLMs) have shown remarkable performance on multimodal tasks like multimodal emotion recognition (ER) in the wild. ER is in...

### 18. Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18484
- **AI 摘要**: 本文提出一种免训练的块稀疏注意力方法，用于加速视频生成和世界模型。研究发现分区几何影响支持集和残差可预测性，通过优化分区和重建残差，在无需训练的情况下提升稀疏注意力性能。
- **原始摘要**: arXiv:2608.18484v1 Announce Type: new Abstract: Training-free block-sparse attention can accelerate video transformers, but row-wise attention concentration does not by itself specify an executable sp...

### 19. MR-IQA-2: Faithful Image Quality Reflection via Fine-Grained Credit Assignment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18579
- **AI 摘要**: 本文提出MR-IQA-2方法，通过细粒度信用分配提升多模态大语言模型在图像质量评估中的推理忠实度，解决共享奖励导致监督来源模糊的问题。
- **原始摘要**: arXiv:2608.18579v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) have shown strong potential for image quality assessment (IQA) by improving consistency between quality ratings...

### 20. PCQA-R1: Advancing Generalized 3D Point Cloud Quality Assessment with Reinforcement Learning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18627
- **AI 摘要**: 本文提出PCQA-R1，利用强化学习提升三维点云质量评估的泛化能力。针对现有基于大语言模型的方法依赖监督微调、难以跨数据集泛化的问题，PCQA-R1通过强化学习优化评分策略，在异构MOS尺度下表现更优。
- **原始摘要**: arXiv:2608.18627v1 Announce Type: new Abstract: No-reference point cloud quality assessment (PCQA) has been an active topic in recent years and is used to measure and optimize the visual experience of...

### 21. TractoGraphVLM: A Unified Vision-Language Framework for White Matter Tractography
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18166
- **AI 摘要**: TractoGraphVLM提出统一视觉语言框架，用于脑白质纤维束的四个任务：束分类、文本到束检索、解剖描述和视觉问答。该框架基于共享GPS架构、训练流程和读出设计，以处理纤维束的复杂拓扑结构。
- **原始摘要**: arXiv:2608.18166v1 Announce Type: cross Abstract: Vision language models have transformed 2D medical imaging, yet extending them to 3D white matter tractography remains challenging due to the complex...

### 22. WorldPack: Dynamic Frame Compression for Long-context Video World Modeling
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2512.02473
- **AI 摘要**: 本文提出WorldPack，一种用于长上下文视频世界模型的动态帧压缩方法。现有方法未显式考虑3D视角几何或仅检索少量空间相关帧，导致长时程生成在时空一致性上存在挑战。WorldPack通过动态压缩历史帧，提升长时程视频生成的时空一致性。
- **原始摘要**: arXiv:2512.02473v3 Announce Type: replace Abstract: Video world models have attracted significant attention for their ability to produce high-fidelity future visual observations conditioned on past ob...

### 23. OccDirector: Language-Guided Behavior and Interaction Generation in 4D Occupancy Space
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.22240
- **AI 摘要**: OccDirector是一个在4D占用空间中生成动态场景的框架，通过语言引导实现复杂多智能体交互，弥补了现有生成模型在语义和时空动态上的不足。
- **原始摘要**: arXiv:2604.22240v2 Announce Type: replace Abstract: Generative world models increasingly rely on 4D occupancy for realistic autonomous driving simulation. However, existing generation frameworks depen...

### 24. PEEK: Picking Essential frames via Efficient Knowledge distillation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.31029
- **AI 摘要**: PEEK是一种高效的动态帧采样方法，用于视频字幕生成。它通过知识蒸馏选择关键帧，在保持性能的同时降低计算成本，优于均匀采样和现有自适应方法。
- **原始摘要**: arXiv:2605.31029v2 Announce Type: replace Abstract: Video-language models can process only a limited number of frames, making frame selection a key bottleneck for efficient video captioning. Most capt...

### 25. How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.16094
- **AI 摘要**: 本文分析视觉语言模型在组合式视觉问答中的失败机制，通过检查失败与特定推理操作的关系，揭示视觉-操作错位问题。
- **原始摘要**: arXiv:2607.16094v2 Announce Type: replace Abstract: Compositional visual question answering requires Vision-Language Models (VLMs) to execute multiple reasoning operations like object selection, spati...

### 26. Look Clearly Before Answering: Mitigating Hallucinations in LVLMs via Saliency-Driven Perceptual Realignment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.16841
- **AI 摘要**: 大型视觉语言模型（LVLMs）在多模态理解中表现出色，但易产生与视觉证据不符的幻觉。现有缓解方法多针对语言先验偏差或跨模态不平衡，而感知与记忆中的渐进视觉退化未被充分探索。本文提出基于显著性驱动的感知重新对齐方法，以缓解幻觉。
- **原始摘要**: arXiv:2607.16841v2 Announce Type: replace Abstract: Large vision-language models (LVLMs) have demonstrated remarkable capabilities in multimodal understanding. However, they remain prone to hallucinat...

### 27. SE-MoLoRA: Shared-Expert LoRA Adapters for Domain-Specific Photographic Assessment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17514
- **AI 摘要**: SE-MoLoRA是一种模块化参数高效适配框架，用于领域特定的摄影评估。它通过共享LoRA专家和路由适配器，分离通用摄影知识与专业残留判断，解决视觉语言模型在摄影批评中语义与美学纠缠的问题。
- **原始摘要**: arXiv:2608.17514v2 Announce Type: replace Abstract: Vision-language models can describe images fluently, but they often fail to provide actionable photographic critique because semantic content and ae...

### 28. Accelerating GPT-5.6 Sol UltrafastAugust 13, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ust 13, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai
- **AI 摘要**: 文章标题提及GPT-5.6 Sol Ultrafast加速，但摘要内容为空，无法提炼具体信息。

### 29. The Economics of AI ReasoningJune 17, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 17, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/the-economics-of-ai-reasoning
- **AI 摘要**: 文章探讨了AI推理的经济学，分析了推理成本、效率与价值之间的关系，并提出了优化推理资源分配的策略，以平衡性能与成本。

### 30. Open Sourcingπ0February 4, 2025We are releasing the weights and code for π0 as well as our new π0-FAST autoregressive model.
- **来源**: Physical Intelligence (TIER1)
- **发布日期**: ril 16, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.physicalintelligence.company/blog/openpi
- **AI 摘要**: 文章宣布开源π0模型及其权重和代码，并发布新的π0-FAST自回归模型。

### 31. REAP: One-Shot Pruning for Trillion-Parameter Mixture-of-Experts ModelsOctober 16, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 16, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/reap
- **AI 摘要**: 文章介绍REAP，一种针对万亿参数混合专家模型的一次性剪枝方法，旨在高效压缩模型，减少计算资源消耗，同时保持性能。

### 32. MoE Math Demystified: What Does 8x7B Actually Mean?October 14, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 14, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/moe-guide-calculator
- **AI 摘要**: 文章解析MoE（混合专家）模型中“8x7B”的含义，澄清其并非80亿参数模型，而是8个70亿参数的专家网络，总参数量约560亿，但推理时仅激活部分专家，实际计算量远小于此。

### 33. Thinking Inside the Box: The Implicit Chain Transformer for Efficient State TrackingDecember 12, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 12, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/thinking-inside-the-box-the-implicit-chain-transformer-for-efficient-state-tracking
- **AI 摘要**: 文章标题为“Thinking Inside the Box: The Implicit Chain Transformer for Efficient State Tracking”，发表于2025年12月12日，但未提供摘要内容。因此无法生成摘要。

### 34. Jais 2: A Blueprint for Sovereign AIDecember 09, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 09, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/jais2
- **AI 摘要**: 本文介绍了Jais 2，一个主权AI蓝图，强调在AI发展中保持国家自主性和文化价值观，通过开源模型和本地化部署实现技术独立。

### 35. Cerebras at NeurIPS 2025: Nine Papers From Pretraining to InferenceDecember 04, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 04, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/cerebras-at-neurips-2025-nine-papers-from-pretraining-to-inference
- **AI 摘要**: Cerebras在NeurIPS 2025上发表了九篇论文，涵盖从预训练到推理的多个方面，展示了其在AI领域的创新研究。

### 36. This new model is smarter than Sonnet 4.5…and 20X faster?January 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7-migration-guide
- **AI 摘要**: 文章介绍了一款新模型，声称其性能优于Sonnet 4.5，且速度快20倍。该模型可能代表了推理效率或架构上的重大突破，但具体细节未在摘要中提供。

### 37. 2026: Fast Inference Finds its GrooveJanuary 06, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 06, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/2026Insights
- **AI 摘要**: 文章预测2026年AI推理将迎来快速发展，强调推理效率与成本优化成为关键，并探讨了相关技术趋势与行业影响。

### 38. Entity tracking emerges in sub-billion parameter language models and exceeds human performance in naturalistic narratives
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18083
- **AI 摘要**: 该研究评估了语言模型和人类在自然叙事中的实体追踪能力，发现亚十亿参数模型也能实现实体追踪，且其表现超过人类。
- **原始摘要**: arXiv:2608.18083v1 Announce Type: new Abstract: Understanding language requires tracking entities across discourse - i.e., knowing where things are and how they change, even when not explicitly stated...

### 39. NE-BERT: A Multilingual Language Model for Nine Northeast Indian Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18094
- **AI 摘要**: NE-BERT是一个针对印度东北部九种低资源语言及印地语、英语的多语言编码器模型，基于约830万句子训练，旨在提升这些语言的自然语言处理能力。
- **原始摘要**: arXiv:2608.18094v1 Announce Type: new Abstract: Large pretrained language models have demonstrated remarkable capabilities across diverse languages, yet critically underrepresented low-resource langua...

### 40. Backdoor Learning in Language Models and Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18095
- **AI 摘要**: 本文探讨了深度学习中语言模型和视觉语言模型面临的后门攻击安全威胁，从可信AI和高效多模态表示学习两个维度，分析、检测并设计防御方法，以增强模型安全性。
- **原始摘要**: arXiv:2608.18095v1 Announce Type: new Abstract: Recent advances in deep learning have significantly enhanced the capabilities of Natural Language Processing (NLP) and Vision-Language Models (VLMs). Ho...

### 41. Fractional Decay KV-Cache: Ownership-Aware Memory Management for Improved Inference Relevancy in Dialog Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18098
- **AI 摘要**: 本文提出分数衰减KV缓存算法（FD-KVC），通过双通道评分机制（累积注意力与衰减）动态管理缓存条目，提升对话系统推理相关性与效率，适应话题演变。
- **原始摘要**: arXiv:2608.18098v1 Announce Type: new Abstract: Key-value (KV) caching is essential for efficient autoregressive inference in transformer based dialog systems, yet existing strategies treat all cached...

### 42. Different Facets of Verbalised Overconfidence: an Interpretability Study
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18106
- **AI 摘要**: 大型语言模型常表现出过度自信，在证据不足时仍给出肯定回答。本文通过控制推理场景，研究Qwen3-4B在语言标记、弃权、数值置信度三种不确定性表达方式上的过度自信行为，证实了该倾向。
- **原始摘要**: arXiv:2608.18106v1 Announce Type: new Abstract: Large language models tend to overconfidence, giving assertive answers when the evidence suggests hedging or abstention. Using controlled reasoning scen...

### 43. Alignment Is All You Need: Instruction-Free Training for General Audio-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18132
- **AI 摘要**: 本文提出一种免指令训练的方法，用于构建通用音频-语言模型，挑战传统多阶段训练流程，利用预训练LLM的推理与指令跟随能力，减少任务特定监督。
- **原始摘要**: arXiv:2608.18132v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) are typically built through a multi-stage pipeline consisting of cross-modal alignment, supervised fine-tuning...

### 44. Language Models for Portuguese: A Systematic Mapping Study
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18138
- **AI 摘要**: 本文系统梳理了葡萄牙语语言模型的发展现状，指出近年来学术界和产业界在葡萄牙语模型开发及数据资源建设方面投入增加，但发展不均衡，并总结了相关进展与挑战。
- **原始摘要**: arXiv:2608.18138v1 Announce Type: new Abstract: In recent years, the rapid development of language models has transformed the field of Natural Language Processing through a wide range of applications....

### 45. The Deontic Gap: Large Language Models and the Modal Language of Obligation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18144
- **AI 摘要**: 本文研究大语言模型是否复现人类道义情态动词（如must、should）的使用模式。通过多个语料库和受控实验发现，AI生成文本持续少用正面道义情态动词，存在“道义鸿沟”。
- **原始摘要**: arXiv:2608.18144v1 Announce Type: new Abstract: Modal auxiliaries such as must, should, and have to mark necessity and obligation within the contexts of speaker authority and interpersonal stance. We...

### 46. WhiteMatter: All-to-All Cross-Layer Connections via KV Mixing
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18486
- **AI 摘要**: WhiteMatter提出一种新架构，使Transformer的每个注意力层都能通过KV混合访问更深层表示，打破传统仅使用本层KV的限制，实现全对全跨层连接，提升解码效率。
- **原始摘要**: arXiv:2608.18486v1 Announce Type: new Abstract: In a Transformer, each layer attends to past tokens only through KV produced at its own depth, despite the presence of deeper representations during aut...

### 47. DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18524
- **AI 摘要**: 本文提出DART-SD方法，针对多轮工具调用智能体训练中因全轨迹模仿导致的拓扑崩溃问题，利用钻石拓扑感知的检索与自蒸馏技术，提升模型在复杂任务上的泛化能力。
- **原始摘要**: arXiv:2608.18524v1 Announce Type: new Abstract: Equipping Large Language Models (LLMs) with multi-turn tool-calling capabilities is essential for building autonomous agents. However, progress is funda...

### 48. Shared Circuits for Shared Grammar: Tracing Subject-Verb Agreement Across Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18545
- **AI 摘要**: 本文研究多语言大模型跨语言共享内部机制的现象，以现在时主谓一致这一形态句法过程为例，探讨共享是否出现及其是否随语法操作的显性实现而变化。
- **原始摘要**: arXiv:2608.18545v1 Announce Type: new Abstract: Multilingual large language models often generalize across languages, and prior work suggests that their internal mechanisms can overlap cross-lingually...

### 49. From Storage to Access: Verifiable Activation of Parametric Knowledge in LLMs via Explicit Priming and Implicit Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18581
- **AI 摘要**: 大型语言模型参数中编码了丰富事实知识，但可靠回忆与验证仍是关键瓶颈。现有端到端方法混淆知识激发与推理，难以判断答案来源。为此，提出VAKE方法，通过显式提示与隐式推理实现参数化知识的可验证激活，以提升事实问答的可靠性。
- **原始摘要**: arXiv:2608.18581v1 Announce Type: new Abstract: Although Large Language Models (LLMs) encode rich factual knowledge in their parameters, reliably recalling and verifying such knowledge remains a key b...

### 50. X2Streaming-TTS: Causal Token-Level Text-to-Speech from Streaming Text with Speech-State Inheritance
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18661
- **AI 摘要**: X2Streaming-TTS提出了一种因果式流式文本转语音框架，能够从不完整文本前缀生成语音，同时保持感知连续性，适用于低延迟对话系统。
- **原始摘要**: arXiv:2608.18661v1 Announce Type: new Abstract: Streaming text-to-speech is essential for low-latency spoken dialogue systems, yet many systems wait for sentence-level text and are therefore only pseu...

### 51. MemFuse: Multi-Source Memory Fusion from Fragmented Observations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18704
- **AI 摘要**: MemFuse提出多源记忆融合方法，解决智能体在跨应用、设备、用户和时间中整合碎片化观察的问题，构建连贯情景记忆并保留来源信息。
- **原始摘要**: arXiv:2608.18704v1 Announce Type: new Abstract: Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on si...

### 52. Gradient Mirage: Trainable yet Label-Unidentifiable Gradients in Large Language Model Split Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18767
- **AI 摘要**: 本文提出Gradient Mirage防御方法，针对大语言模型拆分学习中的梯度匹配攻击。该攻击依赖梯度与标签训练目标一致性的假设，而Gradient Mirage通过破坏这种一致性，使服务器无法从暴露的梯度中恢复私有标签，从而保护客户端数据隐私。
- **原始摘要**: arXiv:2608.18767v1 Announce Type: new Abstract: Gradient matching attacks (GMAs) in LLM split learning (SL) rely on a critical yet underexplored assumption: the gradient exposed at the split interface...

### 53. Readable, Faithful, Used: Three Dissociable Properties of Demographic Identity in a Language Model
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18768
- **AI 摘要**: 大型语言模型用于模拟调查受访者时，回答同质化且不忠实于真实群体差异。本文通过表征相似性分析，在169个人口统计单元中，对1089个读出位置进行评分，探究人口统计身份在LLM中的位置、几何结构对真实群体意见结构的忠实度，以及模型是否使用其编码。
- **原始摘要**: arXiv:2608.18768v1 Announce Type: new Abstract: Large language models are widely used to simulate survey respondents, yet their answers are homogeneous and unfaithful to real inter-group differences....

### 54. Do Large Language Models Hallucinate Electric Fata Morganas?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18816
- **AI 摘要**: 本文探讨大语言模型幻觉的哲学意义，认为其不仅是工程缺陷，还与机器意识问题相关，并分析幻觉的已知成因。
- **原始摘要**: arXiv:2608.18816v1 Announce Type: new Abstract: AI hallucinations - that is, outputs which are made up, cannot be verified, or contradict the source material - are generally regarded as an engineering...

### 55. Identifying Implicit Premises for Logical Reconstruction of Argument Graphs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18821
- **AI 摘要**: 本文针对自然语言文本中论证图的逻辑重建难题，特别是省略式论证（enthymemes）的隐含前提识别。现有方法包括基于NLP的识别和基于溯因的符号推理，但缺乏生成隐含前提的方法。文章旨在提出新方法以完善论证图重建。
- **原始摘要**: arXiv:2608.18821v1 Announce Type: new Abstract: The logical reconstruction of argument graphs from natural language text is challenging because of the prevalence of enthymemes (i.e., arguments with im...

### 56. MedUAG: Unified Understanding and Generation for Medical Multimodal Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18937
- **AI 摘要**: 本文提出MedUAG，为医学多模态大模型建立统一理解与生成框架。构建了大规模训练与评估基准MedUAGCorpus，并验证了统一模型在医学任务上的有效性，填补了该领域空白。
- **原始摘要**: arXiv:2608.18937v1 Announce Type: new Abstract: Recent Multimodal Large Language Models (MLLMs) are rapidly evolving into unified understanding and generation (UAG) frameworks. However, extending thes...

### 57. SPADE: Self-Play in Adaptive Synthetic Executable Environments
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19197
- **AI 摘要**: SPADE提出一种自对弈强化学习框架，让单个LLM同时扮演环境设计者和求解者，通过自适应生成可执行环境来持续扩展目标分布，实现语言代理的连续自我改进。
- **原始摘要**: arXiv:2608.19197v1 Announce Type: new Abstract: Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training environme...

### 58. From Inference to Adaptation: A Unified Optimal Transport View of Vision Language Model
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18339
- **AI 摘要**: 本文提出一种统一的最优传输视角，将视觉语言模型的推理与适应相结合，以应对测试时的分布偏移，避免噪声伪标签误导适应过程。
- **原始摘要**: arXiv:2608.18339v1 Announce Type: cross Abstract: Vision-language models (VLMs) have demonstrated remarkable zero-shot capabilities yet remain sensitive to real-world distribution shifts during infere...

### 59. When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18628
- **AI 摘要**: 本文探讨了视觉语言模型在安全约束下拒绝回答本可正确回答的问题的现象，质疑安全对齐是否抑制了感知基础，并研究了视觉影响与安全对齐之间的动态关系。
- **原始摘要**: arXiv:2608.18628v1 Announce Type: cross Abstract: Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking...

### 60. Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18940
- **AI 摘要**: 本文针对单步逆合成中一对多映射问题，提出Top-K提示训练与推理范式，并构建含4560万验证反应的超大规模数据集CREED-CCV-2+USPTO-XL，以提升化学合理性感知的LLM预测多样性。
- **原始摘要**: arXiv:2608.18940v1 Announce Type: cross Abstract: Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by...

### 61. What is Missing from AI Post-Training AI: An Empirical Analysis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19072
- **AI 摘要**: 本文分析了大语言模型智能体端到端后训练的能力，区分了执行级能力（在选定策略内迭代）和策略级能力（根据实验证据修正高层判断），并指出当前AI-for-AI的局限。
- **原始摘要**: arXiv:2608.19072v1 Announce Type: cross Abstract: Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downst...

### 62. ReWEIGH the Evidence: Calibrating Token-Level Ordinal Visual Evidence to Mitigate Hallucinations in Large Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19075
- **AI 摘要**: 本文提出ReWEIGH方法，通过校准令牌级序数视觉证据来减少大型视觉语言模型（LVLMs）的幻觉。该方法利用视觉令牌状态通过输出头投影，评估图像对候选令牌的支持强度，从而在解码时抑制不支持的内容。
- **原始摘要**: arXiv:2608.19075v1 Announce Type: cross Abstract: Large vision-language models (LVLMs) often hallucinate, generating content that the input image does not support. Preventing such content during decod...

### 63. Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19098
- **AI 摘要**: 本文研究了多教师在线策略蒸馏（M-OPD）中能力失衡的诊断与修复问题，提出Open-MOPD方法，通过分析优化动力学并提供可复现的配方，以提升多专家整合为通用学生的效果。
- **原始摘要**: arXiv:2608.19098v1 Announce Type: cross Abstract: Multi-teacher on-policy distillation (M-OPD) has emerged as a promising paradigm for consolidating domain-specialized reinforcement learning (RL) expe...

### 64. Future Policy Approximation for Offline Reinforcement Learning in LLM Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2509.19893
- **AI 摘要**: 本文重新审视策略梯度式离线强化学习在大型语言模型推理中的应用，提出未来策略近似方法，以提升离线算法性能，减少在线RL的不稳定性与计算开销。
- **原始摘要**: arXiv:2509.19893v3 Announce Type: replace Abstract: Reinforcement learning (RL) has emerged as a key driver of post-training for complex reasoning in large language models (LLMs), yet online RL introd...

### 65. Making Implicit Premises Explicit in Logical Understanding of Enthymemes
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.06114
- **AI 摘要**: 本文探讨了真实世界论证中省略式（enthymemes）的隐含前提显式化问题。现有NLP方法能识别省略式但无法解码其逻辑，而逻辑方法依赖知识库进行溯因。文章旨在弥合这一差距，提升论证的逻辑理解。
- **原始摘要**: arXiv:2603.06114v3 Announce Type: replace Abstract: Real-world arguments in text and dialogues are normally enthymemes (i.e. some of their premises and/or claims are implicit). Natural language proces...

### 66. KA2L: A Knowledge-Aware Active Learning Framework for LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.17566
- **AI 摘要**: 本文提出KA2L框架，用于评估大语言模型对特定知识的掌握程度，并应用主动学习策略提升其领域专业性，弥补了现有研究在领域知识深度理解和针对性学习方面的不足。
- **原始摘要**: arXiv:2603.17566v2 Announce Type: replace Abstract: Fine-tuning large language models (LLMs) with high-quality knowledge has been shown to enhance their performance effectively. However, there is a pa...

### 67. Self-Improvement of Large Language Models: A Technical Overview and Future Outlook
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.25681
- **AI 摘要**: 本文概述了大语言模型自我改进的技术现状与未来展望，指出人类监督成本高且扩展性有限，模型自主决策能力增强，为自我改进提供了可能。
- **原始摘要**: arXiv:2603.25681v2 Announce Type: replace Abstract: As large language models (LLMs) continue to advance, improving them solely through human supervision is becoming increasingly costly and limited in...

### 68. Phantom Transitions in Language Model Fine-Tuning: A Density-Matrix Analysis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.07559
- **AI 摘要**: 本文研究了语言模型微调中正确完成项未能超越近义竞争项的静默失败现象，跨五种架构和十个上下文，通过密度矩阵分析揭示交叉熵损失下降但排名不变的问题。
- **原始摘要**: arXiv:2606.07559v3 Announce Type: replace Abstract: Language models fine-tuned where the correct completion must outrank a near-synonym competitor often fail silently. The cross-entropy loss falls mon...

### 69. First-Token Broadcasters: Mechanistic Origins of Language Identity and Distributed Robustness in Transformers
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.22361
- **AI 摘要**: 本文通过语言身份头消融（LIHA）因果干预方法，识别出GPT-2中一组“首令牌广播”注意力头，它们决定多语言模型生成语言的身份，并揭示其分布式鲁棒性机制。
- **原始摘要**: arXiv:2606.22361v2 Announce Type: replace Abstract: Why do multilingual language models sometimes generate in the wrong language, and why is this so hard to fix? We introduce Language Identity Head Ab...

### 70. Cross-Model Memory Transfer via Target-Side Reader Adaptation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17050
- **AI 摘要**: 本文提出一种跨模型记忆迁移方法，通过目标侧阅读器适配，实现参数化记忆在不同模型间的有效转移，兼顾推理效率与可更新性，为大型语言模型知识利用提供新思路。
- **原始摘要**: arXiv:2608.17050v2 Announce Type: replace Abstract: Methods for improving knowledge use in large language models typically fall into two regimes. Non-parametric retrieval offers flexible access to ext...

### 71. Demystifying Training-Time Augmentation for Data-Constrained Language Model Pretraining
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.16246
- **AI 摘要**: 本文探讨数据受限环境下语言模型预训练的训练时数据增强方法。研究发现标准自回归预训练在此场景下严重过拟合，提出训练时数据增强策略以提升多轮训练效果。
- **原始摘要**: arXiv:2606.16246v3 Announce Type: replace-cross Abstract: As AI labs approach a data ceiling where compute capacity outpaces the rate of new high-quality text generation, language model pretraining is...

### 72. Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12746
- **AI 摘要**: 多模态大语言模型中的对象幻觉源于语言先验和语料共现偏差压倒视觉证据。解码时干预仅在短标题中有效，而基于丰富语料的有监督微调虽延长标题，但超40%仍提及不存在的对象。本文提出双流跨锚点校正方法，并探讨对象级锚点的领域限制。
- **原始摘要**: arXiv:2608.12746v3 Announce Type: replace-cross Abstract: Object hallucination in multimodal large language models arises when language priors and corpus co-occurrence bias outweigh the visual evidenc...

### 73. RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18682
- **AI 摘要**: 本文提出RTPO方法，用于稳定多轮智能体强化学习训练。通过理论分析识别出训练不稳定的根源，并引入反向策略优化，有效缓解性能退化，提升多轮任务表现。
- **原始摘要**: arXiv:2608.18682v1 Announce Type: new Abstract: Training multi-turn agentic workflows with reinforcement learning (RL) enables large language models to perform complex reasoning, use external tools, a...

### 74. Bidirectional representational alignment between biological and artificial neural networks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18244
- **AI 摘要**: 本文研究了生物与人工神经网络之间的表征对齐不对称性，即模型表征预测神经反应优于反向预测。作者假设训练中引导表征几何可系统性改善双向对齐，并探索其机制与效果。
- **原始摘要**: arXiv:2608.18244v1 Announce Type: cross Abstract: Recent work has shown that representational alignment between biological and artificial neural networks is asymmetric: model representations predict n...

### 75. OptiModNet: A UNet-Transformer Hybrid with Grouped-Query and Channel Attention for Optic Disc and Cup Segmentation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18516
- **AI 摘要**: OptiModNet提出一种结合UNet与Transformer的混合架构，采用分组查询和通道注意力机制，用于视盘和视杯的精确分割，旨在实现跨数据集的高性能与低计算需求，助力青光眼早期筛查。
- **原始摘要**: arXiv:2608.18516v1 Announce Type: cross Abstract: Precise segmentation of the optic disc and cup is critical for the early detection and diagnosis of glaucoma. However, achieving consistently high per...

### 76. A Critical Synthesis of Uncertainty Quantification and Foundation Models for Semantic Segmentation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18709
- **AI 摘要**: 本文综述了基础模型在语义分割中的不确定性量化方法，旨在解决其过度自信和领域偏移问题，提升安全关键应用的可靠性。
- **原始摘要**: arXiv:2608.18709v1 Announce Type: cross Abstract: Foundation models are increasingly breaking what seemed to be impossible not long ago by enabling unprecedented accuracy and cross-domain generalizati...

### 77. A Few Cases Are All You Need: An Empirical Study of Annotation-Efficient LoRA Fine-Tuning of MedSAM3
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18731
- **AI 摘要**: 本文实证研究了MedSAM3在医学图像分割中的少样本微调，通过LoRA技术减少标注需求，对比不同标注量下的性能，发现少量标注即可达到较好效果，为医学基础模型的高效适配提供了依据。
- **原始摘要**: arXiv:2608.18731v1 Announce Type: cross Abstract: Medical image segmentation is essential for clinical workflows such as treatment planning and disease assessment. While specialist tools like TotalSeg...

### 78. Forgetting, plasticity, and co-observation: a third facet of continual learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18803
- **AI 摘要**: 本文指出灾难性遗忘和可塑性丧失无法完全解释持续学习性能差距，提出数据共同观察作为第三个影响因素，并探讨其对持续学习的影响。
- **原始摘要**: arXiv:2608.18803v1 Announce Type: cross Abstract: Efficient continual learning remains a fundamental challenge for deep neural networks. While catastrophic forgetting and loss of plasticity are widely...

### 79. Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.26643
- **AI 摘要**: 本文重新思考大语言模型智能体的自进化过程，提出将技能视为可训练状态并优化，但数据驱动的技能优化易过拟合于有限轨迹。为此，引入约束探索-利用过程以缓解技能过拟合问题。
- **原始摘要**: arXiv:2607.26643v2 Announce Type: replace Abstract: Enabling large language model (LLM) agents to accumulate and reuse experience from past interactions remains a central challenge in real-world appli...

### 80. Hybrid LLM-Augmented Reinforcement Learning Agents for Complex Sequential Decision Tasks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.03502
- **AI 摘要**: 本文提出混合LLM增强强化学习代理，用于复杂序列决策任务。结合LLM的推理规划能力与RL的精确控制，解决长时域决策难题，提升任务分解和优化性能。
- **原始摘要**: arXiv:2608.03502v2 Announce Type: replace Abstract: Large Language Models (LLMs) have recently shown strong capabilities in reasoning, planning, and tool-use, enabling new forms of autonomous agents....

### 81. FiLoRA: Focus-and-Ignore LoRA for Controllable Feature Reliance
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.02060
- **AI 摘要**: FiLoRA提出一种名为“聚焦与忽略”的LoRA方法，通过显式调节多模态基础模型对不同内部特征路径的依赖，实现对预测行为的可控干预，以应对捷径和虚假相关行为。
- **原始摘要**: arXiv:2602.02060v2 Announce Type: replace-cross Abstract: Multimodal foundation models integrate heterogeneous signals across modalities, yet it remains unclear whether their predictions can be contro...

### 82. Structure-Informed Estimation for Pilot-Limited MIMO Channels via Tensor Decomposition
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.04083
- **AI 摘要**: 本文针对宽带MIMO系统中导频开销限制信道估计精度的问题，提出一种结构信息混合估计器，将导频受限的信道估计建模为低秩张量补全问题，利用张量分解从稀疏观测中恢复信道，避免传统方法需完全观测张量的假设。
- **原始摘要**: arXiv:2602.04083v3 Announce Type: replace-cross Abstract: Accurate channel state information in wideband MIMO systems is constrained by pilot overhead, a challenge intensifying as bandwidths scale tow...

### 83. Hybrid ANN-SNN Pipeline with Local Plasticity
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.20151
- **AI 摘要**: 本文提出一种混合ANN-SNN流水线，利用预训练人工神经网络（如EfficientNet）的丰富嵌入，通过速率编码转换为脉冲序列，并采用局部可塑性规则训练脉冲分类器（CoLaNET），实现高性能且生物合理的脉冲神经网络。
- **原始摘要**: arXiv:2606.20151v2 Announce Type: replace-cross Abstract: This work proposes a hybrid ANN-SNN pipeline that effectively leverages the rich embeddings of pretrained artificial neural networks (ANNs) to...

### 84. Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17253
- **AI 摘要**: 本文提出Co-RL方法，通过多智能体强化学习中的多样群体协作，使无监督推理能力自然涌现，减少对可验证奖励等人工监督的依赖，为语言和视觉语言模型推理提供新途径。
- **原始摘要**: arXiv:2608.17253v2 Announce Type: replace-cross Abstract: Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its stronge...

### 85. The Road Taken: The Role of Optimizers at the Edge of Stability
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18415
- **AI 摘要**: 本文研究深度学习优化器在稳定性边缘的现象，即Hessian特征值超过经典下降引理预测的阈值时仍保持稳定。作者发现多种一阶方法（如梯度下降）显著违反该预测，并探讨了优化器在此边缘状态下的作用机制。
- **原始摘要**: arXiv:2608.18415v1 Announce Type: new Abstract: The edge of stability refers to a phenomenon in deep learning with gradient-based optimizers where the Hessian eigenvalues of the loss remain stable abo...

### 86. Infrared Universality of Collective Dynamics across Transformer and State-Space Architectures
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18592
- **AI 摘要**: 本文探讨不同神经架构是否具有共同的集体动力学。研究发现Transformer语言模型具有近平坦、弱红外增强的时间尺度态密度，与近边缘长记忆动力学相关。本文进一步检验Mamba模型是否出现类似组织，其选择性状态空间动力学提供了根本不同的微观机制。
- **原始摘要**: arXiv:2608.18592v1 Announce Type: new Abstract: Whether distinct neural architectures develop common collective dynamics remains an open question. Recent analysis of Transformer language models reveal...

### 87. To Go Far, Go Together: Diverse Preferences Induce a Curriculum for Reward Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18770
- **AI 摘要**: 本文探讨了从人类反馈中学习奖励模型以对齐AI系统的问题，指出仅追求数据高效和准确的用户奖励模型并不足够，需考虑多样偏好以促进奖励优化的课程式学习。
- **原始摘要**: arXiv:2608.18770v1 Announce Type: new Abstract: Learning a reward model from human feedback and optimizing a policy against it is one approach to aligning AI systems with individual users. From a fair...

### 88. GraphK: Variable-Size Graph Generation with Efficient Edge Construction
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18777
- **AI 摘要**: GraphK是一种新型图生成框架，采用编码器-采样器-解码器结构，通过结构灵活性和计算效率克服现有模型在可扩展性、灵活性和结构建模上的局限，避免了自回归方法受词汇量限制的问题。
- **原始摘要**: arXiv:2608.18777v1 Announce Type: new Abstract: Graph generation models have advanced significantly with deep learning, yet they remain limited in scalability, flexibility, and ability to model underl...

### 89. A Unifying Relational Perspective on Expressive Lottery Tickets
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18819
- **AI 摘要**: 本文提出统一关系视角，研究稀疏性对关系图神经网络（RGNNs）和时序图神经网络（TGNNs）表达能力的影响，将强表达彩票假设（SELTH）从静态图推广到多关系与时序领域，证明存在保持Weisfeiler-Leman表达力的稀疏网络。
- **原始摘要**: arXiv:2608.18819v1 Announce Type: new Abstract: Graph neural networks (GNNs) are widely used, but how parameter sparsity affects the expressivity of relational (RGNNs) and temporal (TGNNs) variants is...

### 90. GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18849
- **AI 摘要**: GEAR是一种两阶段蒸馏框架，将表格基础模型（TFM）蒸馏为轻量级MLP或树模型，以降低推理延迟和内存成本。第一阶段用合成协变量作为教学信号，第二阶段用真实锚定，使模型在CPU上高效部署。
- **原始摘要**: arXiv:2608.18849v1 Announce Type: new Abstract: Tabular foundation models (TFMs) achieve strong performance through in-context learning, but context-dependent inference imposes substantial latency and...

### 91. On the Slow Convergence to Trivial Solutions of Algorithms for Hard Optimization Problems
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18910
- **AI 摘要**: 本文探讨了硬组合优化问题（多为NP难）的算法收敛缓慢现象。通过随机实例的平均情况分析，研究算法在困难实例上的典型性能，并指出在足够密集的约束下，已知算法收敛到平凡解的速度极慢，揭示了算法性能的局限性。
- **原始摘要**: arXiv:2608.18910v1 Announce Type: new Abstract: Hard combinatorial optimization problems, many of which are NP-hard, present fundamental algorithmic challenges. Average-case analysis on random instanc...

### 92. Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19151
- **AI 摘要**: 本文研究非马尔可夫环境下多元霍克斯随机微分方程的随机控制问题，提出有限维马尔可夫化算法近似霍克斯过程，并利用机器学习方法求解。
- **原始摘要**: arXiv:2608.19151v1 Announce Type: new Abstract: We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting....

### 93. Self-supervised In-context Operator Learning for Stochastic Mean-Field Control
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18282
- **AI 摘要**: 本文提出将随机平均场控制问题建模为算子学习问题，并开发了首个网格无关的深度学习方法，以高效解决任务变化时的MFC问题。
- **原始摘要**: arXiv:2608.18282v1 Announce Type: cross Abstract: Stochastic mean-field control (MFC) provides a fundamental framework for coordinating large populations of interacting agents under uncertainty, with...

### 94. Which Negatives Matter? Ask Your Text Encoder: Adaptive Similarity Margins for Dense-Caption Retrieval
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18521
- **AI 摘要**: 密集字幕检索通过引入分割、边缘图、LLM过滤字幕和跨模态模块得到改进，但现有方法沿用InfoNCE目标，在强预训练初始化下会过早饱和，导致损失快速下降且梯度归零。文章提出自适应相似度边际方法，利用文本编码器判断负样本重要性，以优化训练。
- **原始摘要**: arXiv:2608.18521v1 Announce Type: cross Abstract: Dense-caption retrieval has recently been improved by introducing segmentation, edge maps, LLM-filtered captions, and cross-modal modules into contras...

### 95. Sharper Regret Bounds for Time-Varying Gaussian Process Bandits with Constant Exploration
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18863
- **AI 摘要**: 本文研究时变环境下高斯过程多臂老虎机的贝叶斯优化，提出使用恒定探索参数的GP-UCB算法，通过局部置信事件获得更紧的期望遗憾界。
- **原始摘要**: arXiv:2608.18863v1 Announce Type: cross Abstract: We study Bayesian optimization in a time-varying environment where the unknown reward function evolves according to a Gaussian process drift model. Ex...

### 96. Quantum Tensor Network Learning with DMRG
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18901
- **AI 摘要**: 本文介绍张量网络作为机器学习方法，提出矩阵乘积态的全局归一化条件，使其表示量子态，并研究两种局部优化方法。
- **原始摘要**: arXiv:2608.18901v1 Announce Type: cross Abstract: Tensor Networks are a relatively new machine learning approach. The architectures proposed initially are inspired by approaches from quantum many-body...

### 97. Breaking the weakest link to evade vision language models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18938
- **AI 摘要**: 视觉语言模型（VLMs）在多模态AI系统中至关重要，但其对抗鲁棒性研究不足。本文聚焦于针对多模态对齐的逃避攻击，探索最薄弱环节以规避VLM，揭示其安全漏洞。
- **原始摘要**: arXiv:2608.18938v1 Announce Type: cross Abstract: Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual...

### 98. Robust Risk Under Evolving Uncertainty: A Wasserstein Counterpart of the Entropic Value-at-Risk
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19073
- **AI 摘要**: 本文提出一种在演化不确定性下的稳健风险度量方法，利用最优传输球替代相对熵球，以覆盖名义模型认为不可能但可能发生的灾难事件，从而在智能体学习环境时平衡谨慎与自信。
- **原始摘要**: arXiv:2608.19073v1 Announce Type: cross Abstract: An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a...

### 99. Automated Computational Energy Minimization of ML Algorithms using Constrained Bayesian Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2024年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2407.05788
- **AI 摘要**: 本文提出使用约束贝叶斯优化自动最小化机器学习算法的计算能耗，在优化预测性能的同时兼顾能源效率，为可持续AI提供新方法。
- **原始摘要**: arXiv:2407.05788v2 Announce Type: replace Abstract: Bayesian optimization (BO) is an efficient framework for optimization of black-box objectives when function evaluations are costly and gradient info...

### 100. Contrasting Cost-Agnostic and Cost-Sensitive Losses under Limited Model Capacity via $\mathcal H$-consistency
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2502.19522
- **AI 摘要**: 本文探讨了在有限模型容量下，任务无关损失（如交叉熵）与任务相关损失（如加权交叉熵）的对比，通过H一致性理论分析，指出在理想条件下两者等价，但实际中容量限制会影响性能。
- **原始摘要**: arXiv:2502.19522v2 Announce Type: replace Abstract: There is a prevalent debate in machine learning about whether practitioners should train models to optimize a task-agnostic objective (e.g., cross e...

### 101. Escaping Local Minima Provably in Non-convex Matrix Sensing: A Deterministic Framework via Simulated Lifting
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.05887
- **AI 摘要**: 本文提出一种确定性框架，通过模拟提升将低秩矩阵感知中的局部极小值转化为严格鞍点，从而证明梯度方法可逃离局部极小并收敛到全局最优，为过参数化提升方法提供了理论保证。
- **原始摘要**: arXiv:2602.05887v3 Announce Type: replace Abstract: Low-rank matrix sensing is a fundamental yet challenging nonconvex problem whose optimization landscape typically contains numerous spurious local m...

### 102. Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.01499
- **AI 摘要**: 本文比较了进化策略（ES）与GRPO在LLM后训练中的表现，发现ES在单任务准确率上相当或更优，但在参数空间解上存在差异，并探讨了持续学习场景下的影响。
- **原始摘要**: arXiv:2604.01499v3 Announce Type: replace Abstract: Evolution Strategies (ES) have emerged as a scalable gradient-free alternative to reinforcement learning based LLM fine-tuning, but it remains uncle...

### 103. LionMuon: Alternating Spectral and Sign Descent for Efficient Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.19811
- **AI 摘要**: 本文提出LionMuon优化器，结合Lion的廉价更新与Muon的强方向，交替使用谱矩阵符号和符号下降，大幅降低平均每步成本，同时保持训练效率。
- **原始摘要**: arXiv:2605.19811v3 Announce Type: replace Abstract: In large-scale optimization, the cheapness and effectiveness of update steps are the most crucial factors for a successful optimizer. Sign-based opt...

### 104. A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.11917
- **AI 摘要**: 本文提出一种基于Forney因子图的多输出高斯过程回归方法，通过最近邻链将候选输入排序，使计算复杂度从三次方降为线性，并支持不同输出在不同输入点的观测。
- **原始摘要**: arXiv:2608.11917v2 Announce Type: replace Abstract: Multi-output Gaussian process regression scales cubically in the number of observations times outputs, and dense kernel-matrix methods need bespoke...

### 105. Conformal Policy Control
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.02196
- **AI 摘要**: 本文提出了一种利用安全参考策略作为概率调节器的方法，以控制智能体行为变化幅度，在保证安全的同时鼓励探索，适用于高风险环境中的策略优化。
- **原始摘要**: arXiv:2603.02196v4 Announce Type: replace-cross Abstract: An agent must try new behaviors to explore and improve. In high-stakes environments, an agent that violates safety constraints may cause harm...

### 106. SHANG++: Robust Stochastic Acceleration under Multiplicative Noise
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.09355
- **AI 摘要**: 本文提出两种加速随机梯度下降方法SHANG和SHANG++，通过离散化Hessian驱动的Nesterov加速梯度流，在乘法噪声缩放条件下提升稳定性，解决原始Nesterov加速对噪声敏感的问题。
- **原始摘要**: arXiv:2603.09355v2 Announce Type: replace-cross Abstract: Under the multiplicative noise scaling (MNS) condition, original Nesterov acceleration is provably sensitive to noise and may diverge when gra...

### 107. Pre-Training for Simulation-Based Science: A Study on Jet Foundation Model Training Objectives
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.14870
- **AI 摘要**: 本文系统比较了基于模拟的科学领域中基础模型的预训练目标，利用大量带标签的模拟数据，探索自监督掩码训练与监督预训练的效果，为科学基础模型预训练提供新思路。
- **原始摘要**: arXiv:2606.14870v2 Announce Type: replace-cross Abstract: Foundation models (FMs) trained on large datasets and fine-tuned on downstream tasks have emerged as a powerful paradigm in AI for science. In...

### 108. Untrainable elements determine what physical learning remembers
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 5 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.00097
- **AI 摘要**: 本文研究了物理学习规则（如平衡传播、耦合学习等）在电阻网络中的训练行为，发现不可训练元素决定了物理学习所记忆的内容，并区分了电路不变性与规则守恒性对学习结果的影响。
- **原始摘要**: arXiv:2608.00097v2 Announce Type: replace-cross Abstract: Physical learning rules such as equilibrium propagation (EP), coupled learning (CL), and adjoint coupled learning (AL) train resistive network...

### 109. Qwen-Image-Edit: Image Editing with Higher Quality and Efficiency
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image-edit/
- **AI 摘要**: Qwen-Image-Edit是基于Qwen-Image的图像编辑模型，扩展了文本渲染能力，支持精确文本编辑。它同时利用Qwen2.5-VL进行视觉语义控制和VAE编码器进行视觉外观控制，实现高质量高效编辑。
- **原始摘要**: QWEN CHAT GITHUB HUGGING FACE MODELSCOPE DISCORD We are excited to introduce Qwen-Image-Edit, the image editing version of Qwen-Image. Built upon our 20B Qwen-Image model, Qwen-Image-Edit successfully...

### 110. Qwen-Image: Crafting with Native Text Rendering
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image/
- **AI 摘要**: Qwen团队发布Qwen-Image，一个200亿参数的MMDiT图像基础模型，在复杂文本渲染和精确图像编辑方面取得显著进展，支持多行布局、段落级语义和细粒度细节。
- **原始摘要**: GITHUB HUGGING FACE MODELSCOPE DEMO DISCORD We are thrilled to release Qwen-Image, a 20B MMDiT image foundation model that achieves significant advances in complex text rendering and precise image edi...

### 111. GSPO: Towards Scalable Reinforcement Learning for Language Models
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/gspo/
- **AI 摘要**: 本文提出GSPO，一种面向语言模型的可扩展强化学习算法，旨在解决现有RL算法（如GRPO）在长训练中的不稳定性和模型崩溃问题，以支持更大规模的计算和性能提升。
- **原始摘要**: PAPER DISCORD Introduction Reinforcement Learning (RL) has emerged as a pivotal paradigm for scaling language models and enhancing their deep reasoning and problem-solving capabilities. To scale RL, t...

### 112. VLAs that Train Fast, Run Fast, and Generalize Better
- **来源**: Physical Intelligence (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.physicalintelligence.company/research/knowledge_insulation
- **AI 摘要**: 文章探讨了视觉语言模型（VLAs）在训练速度、运行效率和泛化能力上的改进方法，提出新架构或训练策略，以实现更快的训练和推理，同时提升模型在新场景中的泛化性能。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
