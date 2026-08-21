# RSS 聚合报告 - AI模型

**生成时间**: 2026-08-21 09:50:05
**文章数量**: 118 篇

---

### 1. Is KV Cache in a high dimensional vector space? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T18:18:10+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtrdem/is_kv_cache_in_a_high_dimensional_vector_space_d/
- **AI 摘要**: 文章探讨KV缓存在高维向量空间中的结构，指出其并非扁平列表，而是具有可导航几何结构的向量集合，键携带模型学习到的关联关系，用于推理时的存储与检索。
- **原始摘要**: I've been doing some research on this question: At inference time a large part of a model's working memory lives in the KV cache, plus whatever external memory the harness bolts on. I've been poking a...

### 2. The spectral neuron - an ML primitive for scalable and interpretable models [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T10:20:47+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtfimo/the_spectral_neuron_an_ml_primitive_for_scalable/
- **AI 摘要**: 文章探讨了在广告团队中寻找既简单又可扩展、可解释、可控的模型，提出了“谱神经元”这一ML原语，并基于博客内容发布了预印本。
- **原始摘要**: Worked some time ago on one of the ad teams at Yahoo, and this grew out of a question I kept returning to while there are there "simple" models that are both simple, scalable, interpretable, and contr...

### 3. About the impact of grouping classes in multiclass classification [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T07:42:20+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtctaz/about_the_impact_of_grouping_classes_in/
- **AI 摘要**: 本文探讨多分类问题中合并类别的影响，询问是否有关于此做法危害性的共识或指导，属于机器学习方法论讨论。
- **原始摘要**: A premise: I hope this question is "worth" of this subreddit, I did a decent amount of research before posting, I thought it was potentially interesting enough for it, but possibly not basic enough fo...

### 4. Same GRPO recipe on three from-scratch LLMs (353M/316M/672M) gave three different outcomes, with no clean relationship to scale [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T21:30:26+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vszsit/same_grpo_recipe_on_three_fromscratch_llms/
- **AI 摘要**: 作者从零训练三个不同规模的LLM，采用相同的SFT和GRPO后训练流程，发现GRPO对较大模型（V2和V3）产生负面影响，且结果与模型规模无清晰关联，原因不明。
- **原始摘要**: I trained three LLMs from scratch in raw PyTorch then post-trained each one with SFT and then GRPO. Same process every time: same synthetic arithmetic curriculum, same reward function, same hyperparam...

### 5. How much of the weight-space perception gap is actually symmetry? Evidence from ~1.8M fitted SIRENs [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T19:24:12+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vswdnf/how_much_of_the_weightspace_perception_gap_is/
- **AI 摘要**: 文章探讨了权重空间学习中参数对称性对语义读取的影响，通过约180万拟合SIRENs实验，分离了对称性与非对称性因素，揭示了独立拟合网络权重语义崩溃的原因。
- **原始摘要**: I’ve been looking at a fairly basic question in weight-space learning that I don’t think gets separated cleanly enough: Why does reading semantics directly from neural network weights work pretty well...

### 6. Trained an diffusion model that runs on 264KB of RAM [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-18T09:26:21+00:00 (3 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vrk7t5/trained_an_diffusion_model_that_runs_on_264kb_of/
- **AI 摘要**: 作者训练了一个能在264KB RAM上运行的扩散模型，展示了极致的模型压缩技术，使其适用于资源受限的嵌入式设备。
- **原始摘要**: I recently bought a Shrike lite which has got 264KB of SRAM. I decided to train an image generation model that generates 32*32 pixel images. The microcontroller also has an FPGA onboard which I used t...

### 7. Revisiting the Efficient Channel Attention paper (2019, 12k citations) - the central hypothesis isn't quite right [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-16T10:13:44+00:00 (4 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/
- **AI 摘要**: 本文重新审视了高效通道注意力（ECA）论文，指出其核心假设可能不完全正确。ECA通过一维卷积直接处理通道均值，避免降维，优于SE。作者质疑其跨通道交互的假设，并探讨了更合理的解释。
- **原始摘要**: ECA was positioned as a successor to SE. The idea behind ECA is quite simple. Unlike SE which reduces the channel means into a smaller hidden layer, it directly uses a 1d convolution kernel on the cha...

### 8. How can we solve long-range recall in linear attention? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-16T07:47:09+00:00 (5 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/
- **AI 摘要**: 作者在DNA序列建模中采用线性注意力，但面临长程召回问题。在Needle-in-a-Haystack基准测试中，模型表现不佳，提示线性注意力在长距离依赖上的局限。
- **原始摘要**: Recently, I started working on DNA sequence modeling and decided to explore linear attention, mainly because DNA sequences can easily reach 1M tokens, making standard softmax attention extremely expen...

### 9. Multi-Vector (Late Interaction) Embedding Models with Sentence Transformers
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Tue, 18 Aug 2026 00:00:00 GMT (3 天前)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/multi-vector-encoder
- **AI 摘要**: 本文介绍多向量（后期交互）嵌入模型在句子转换器中的应用，探讨其原理、优势及实现方法，以提升语义搜索和文本匹配性能。

### 10. Up to 3.2x Faster Inference with LFM2.5-DSpark
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Thu, 20 Aug 2026 16:52:57 GMT (今天)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/LiquidAI/lfm25-dspark
- **AI 摘要**: 文章介绍LFM2.5-DSpark模型，通过优化推理流程实现高达3.2倍的推理加速，提升性能与效率。

### 11. v1.6.0: Mistrall goes Small 3.1 with vision
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2025-03-20T15:03:08Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.6.0
- **AI 摘要**: Mistral Inference v1.6.0发布，新增对Mistral Small 3.1模型的支持，并修复了缺失换行的问题。
- **原始摘要**: What's Changed Missing new line by @theophilegervet in #234 Add support to Mistral Small 3.1 by @juliendenize in #239 Remove file refs by @juliendenize in #240 Release 1.6.0 by @juliendenize in #241 N...

### 12. v1.4.0: Pixtral 👀
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-09-13T13:10:17Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.4.0
- **AI 摘要**: Mistral AI发布v1.4.0版本，推出Pixtral模型，支持视觉功能。用户可通过升级mistral_inference库（>=1.4.0）并使用Hugging Face下载来使用该模型。
- **原始摘要**: Pixtral Mistral models can now 👀 ! pip install --upgrade mistral_inference # >= 1.4.0 Download: from huggingface_hub import snapshot_download from pathlib import Path mistral_models_path = Path.home()...

### 13. v1.3.0 Mistral-Nemo
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-18T15:45:30Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.3.0
- **AI 摘要**: Mistral与NVIDIA合作推出Mistral-Nemo模型，版本v1.3.0，提供安装和下载指引，用户可通过pip安装mistral-inference库获取。
- **原始摘要**: Welcome Mistral-Nemo from Mistral 🤝 NVIDIA Read more about Mistral-Nemo here. Install pip install mistral-inference>=1.3.0 Download export NEMO_MODEL=$HOME/12B_NEMO_MODEL wget https://models.mistralcd...

### 14. v1.2.0 Add Mamba
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-16T18:41:37Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.2.0
- **AI 摘要**: Mistral AI发布v1.2.0版本，新增Codestral-Mamba代码生成模型和Mathstral数学推理模型，支持通过pip安装使用，提供下载和部署指南。
- **原始摘要**: Welcome 🐍 Codestral-Mamba and 🔢 Mathstral pip install mistral-inference>=1.2.0 Codestral-Mamba pip install packaging mamba-ssm causal-conv1d transformers Download export MAMBA_CODE=$HOME/7B_MAMBA_CODE...

### 15. v1.0.4 - Mistral-inference
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-05-24T18:32:35Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.0.4
- **AI 摘要**: Mistral-inference是Mistral官方推理库，支持7B、8x7B、8x22B模型，可通过pip安装并运行。
- **原始摘要**: Mistral-inference is the official inference library for all Mistral models: 7B, 8x7B, 8x22B. Install with: pip install mistral-inference Run with: from mistral_inference.model import Transformer from...

### 16. v1.1.0 Add LoRA
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-05-24T18:32:10Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.1.0
- **AI 摘要**: mistral-inference v1.1.0版本新增对LoRA模型的支持，可运行通过mistral-finetune训练的7B基础LoRA模型，并提供了相应的Python调用示例。
- **原始摘要**: mistral-inference==1.1.0 supports running LoRA models that were trained with: https://github.com/mistralai/mistral-finetune Having trained a 7B base LoRA, you can run mistral-inference as follows: fro...

### 17. TTSD-FAR: Test-Time Self-Distillation with Fisher-Anchored Restoration for Missing-Modality Emotion Recognition in LVLMs
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18386
- **AI 摘要**: 本文提出TTSD-FAR方法，用于大型视频语言模型在多模态情感识别中应对测试时模态缺失或噪声问题。通过测试时自蒸馏和Fisher锚定恢复，缓解部分观测导致的分布偏移，提升识别鲁棒性。
- **原始摘要**: arXiv:2608.18386v1 Announce Type: new Abstract: Large video-language models (LVLMs) have shown remarkable performance on multimodal tasks like multimodal emotion recognition (ER) in the wild. ER is in...

### 18. Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18484
- **AI 摘要**: 本文提出一种免训练的块稀疏注意力方法，用于加速视频生成和世界模型。通过优化分区几何，改善查询支持重叠和残差可预测性，从而在保持性能的同时提升效率。
- **原始摘要**: arXiv:2608.18484v1 Announce Type: new Abstract: Training-free block-sparse attention can accelerate video transformers, but row-wise attention concentration does not by itself specify an executable sp...

### 19. PCQA-R1: Advancing Generalized 3D Point Cloud Quality Assessment with Reinforcement Learning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18627
- **AI 摘要**: 本文提出PCQA-R1，利用强化学习提升三维点云质量评估的泛化能力，解决不同数据集MOS尺度不一致的问题，并首次探索大语言模型在该领域的应用。
- **原始摘要**: arXiv:2608.18627v1 Announce Type: new Abstract: No-reference point cloud quality assessment (PCQA) has been an active topic in recent years and is used to measure and optimize the visual experience of...

### 20. Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned Objectives for MPC Planning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18746
- **AI 摘要**: 本文提出决策度量对齐概念，用于JEPA风格潜在世界模型中的MPC规划。引入Plan-Real Spearman和CEM-stage Spearman指标，诊断潜在表示与真实任务进度的排名一致性，并改进动作条件目标以提升规划性能。
- **原始摘要**: arXiv:2608.18746v1 Announce Type: cross Abstract: JEPA-style latent world models can use Euclidean distance to a goal latent as the cost for model-predictive control (MPC). Strong decoding of task var...

### 21. Eyes on the Image: Gaze Supervised Multimodal Learning for Chest X-ray Diagnosis and Report Generation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年08月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2508.13068
- **AI 摘要**: 本文提出一种基于MIMIC-Eye数据集的两阶段多模态框架，用于胸部X光诊断和报告生成。第一阶段引入凝视标记分类器，融合图像块、边界框掩码、转录嵌入和放射科医生注视数据，并通过课程调度和信任校准提升性能。
- **原始摘要**: arXiv:2508.13068v2 Announce Type: replace Abstract: Medical vision-language models still struggle to match radiologists' attention and to verbalize findings with explicit spatial grounding. We address...

### 22. WorldPack: Dynamic Frame Compression for Long-context Video World Modeling
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2512.02473
- **AI 摘要**: 本文提出WorldPack，一种用于长上下文视频世界建模的动态帧压缩方法。现有方法未显式考虑3D视角几何或仅检索少量空间相关帧。WorldPack通过动态压缩历史帧，提升长时程视频生成的时空一致性。
- **原始摘要**: arXiv:2512.02473v3 Announce Type: replace Abstract: Video world models have attracted significant attention for their ability to produce high-fidelity future visual observations conditioned on past ob...

### 23. OccDirector: Language-Guided Behavior and Interaction Generation in 4D Occupancy Space
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.22240
- **AI 摘要**: OccDirector是一个在4D占据空间中生成动态场景的框架，通过语言引导行为与交互生成，解决现有方法依赖刚性轨迹或简单文本、难以编排复杂多智能体交互的问题。
- **原始摘要**: arXiv:2604.22240v2 Announce Type: replace Abstract: Generative world models increasingly rely on 4D occupancy for realistic autonomous driving simulation. However, existing generation frameworks depen...

### 24. PEEK: Picking Essential frames via Efficient Knowledge distillation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.31029
- **AI 摘要**: PEEK是一种高效的动态帧采样方法，用于视频字幕生成。它通过知识蒸馏选择信息量最大的帧，避免均匀采样的盲目性和现有自适应方法的计算开销，提升视频语言模型的效率。
- **原始摘要**: arXiv:2605.31029v2 Announce Type: replace Abstract: Video-language models can process only a limited number of frames, making frame selection a key bottleneck for efficient video captioning. Most capt...

### 25. Look Clearly Before Answering: Mitigating Hallucinations in LVLMs via Saliency-Driven Perceptual Realignment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.16841
- **AI 摘要**: 本文提出一种基于显著性驱动的感知重对齐方法，以缓解大型视觉语言模型中的幻觉问题。该方法通过重新对齐视觉感知与语言生成，减少语言先验偏差和跨模态不平衡，从而提升模型对视觉证据的忠实度。
- **原始摘要**: arXiv:2607.16841v2 Announce Type: replace Abstract: Large vision-language models (LVLMs) have demonstrated remarkable capabilities in multimodal understanding. However, they remain prone to hallucinat...

### 26. SE-MoLoRA: Shared-Expert LoRA Adapters for Domain-Specific Photographic Assessment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17514
- **AI 摘要**: SE-MoLoRA是一种模块化参数高效适配框架，用于领域特定的摄影评估。它通过始终激活的共享LoRA专家和路由适配器，将通用摄影知识与专家残差判断分离，以提升视觉语言模型在摄影批评方面的能力。
- **原始摘要**: arXiv:2608.17514v2 Announce Type: replace Abstract: Vision-language models can describe images fluently, but they often fail to provide actionable photographic critique because semantic content and ae...

### 27. Accelerating GPT-5.6 Sol UltrafastAugust 13, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ust 13, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai
- **AI 摘要**: 文章标题提及加速GPT-5.6 Sol Ultra，但摘要内容为空，无法生成具体摘要。

### 28. The Economics of AI ReasoningJune 17, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 17, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/the-economics-of-ai-reasoning
- **AI 摘要**: 本文探讨AI推理的经济学，分析推理成本、计算资源分配及模型规模对推理效率的影响，讨论如何在性能与成本间取得平衡，并展望未来推理技术的发展趋势。

### 29. REAP: One-Shot Pruning for Trillion-Parameter Mixture-of-Experts ModelsOctober 16, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 16, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/reap
- **AI 摘要**: REAP是一种针对万亿参数混合专家模型的一次性剪枝方法，旨在高效压缩大规模MoE模型，在保持性能的同时显著减少计算和存储开销。

### 30. MoE Math Demystified: What Does 8x7B Actually Mean?October 14, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 14, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/moe-guide-calculator
- **AI 摘要**: 本文解析MoE（混合专家）模型中“8x7B”的含义，说明其并非80亿参数模型，而是8个70亿参数的专家网络，实际参数量更大但推理时仅激活部分专家，实现高效计算。

### 31. Thinking Inside the Box: The Implicit Chain Transformer for Efficient State TrackingDecember 12, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 12, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/thinking-inside-the-box-the-implicit-chain-transformer-for-efficient-state-tracking
- **AI 摘要**: 文章提出隐式链式Transformer（ICT），通过内部状态跟踪替代显式思维链，提升推理效率，在状态跟踪任务中实现高效计算。

### 32. Introducing OpenAI GPT-5.3-Codex-Spark Powered by CerebrasFebruary 12, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 12, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/openai-codexspark
- **AI 摘要**: OpenAI发布GPT-5.3-Codex-Spark，由Cerebras提供算力支持，旨在提升代码生成与推理能力，并优化推理性能。

### 33. This new model is smarter than Sonnet 4.5…and 20X faster?January 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7-migration-guide
- **AI 摘要**: 文章介绍了一款新模型，声称其性能优于Sonnet 4.5，且速度快20倍。该模型可能在推理效率或架构上有所创新，但具体细节未在摘要中提及。

### 34. GLM-4.7: Frontier intelligence at record speed — now available on CerebrasJanuary 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7
- **AI 摘要**: GLM-4.7模型在Cerebras平台上发布，以创纪录的速度提供前沿智能，强调推理性能与效率提升，适用于多种AI应用场景。

### 35. Entity tracking emerges in sub-billion parameter language models and exceeds human performance in naturalistic narratives
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18083
- **AI 摘要**: 本文研究语言模型在自然叙事中的实体追踪能力，发现亚十亿参数模型已具备该能力，且表现超过人类。现有评估多基于人工任务，缺乏与人类对比，本文通过自然主义叙事任务填补了这一空白。
- **原始摘要**: arXiv:2608.18083v1 Announce Type: new Abstract: Understanding language requires tracking entities across discourse - i.e., knowing where things are and how they change, even when not explicitly stated...

### 36. NE-BERT: A Multilingual Language Model for Nine Northeast Indian Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18094
- **AI 摘要**: NE-BERT是一个针对印度东北部九种语言及印地语、英语的多语言编码器模型，基于约830万句子训练，旨在提升低资源语言的自然语言处理能力。
- **原始摘要**: arXiv:2608.18094v1 Announce Type: new Abstract: Large pretrained language models have demonstrated remarkable capabilities across diverse languages, yet critically underrepresented low-resource langua...

### 37. Backdoor Learning in Language Models and Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18095
- **AI 摘要**: 本文探讨了深度学习在NLP和视觉语言模型中的后门攻击漏洞，聚焦于可信AI与高效多模态表示学习，涉及后门攻击的分析、检测与防御。
- **原始摘要**: arXiv:2608.18095v1 Announce Type: new Abstract: Recent advances in deep learning have significantly enhanced the capabilities of Natural Language Processing (NLP) and Vision-Language Models (VLMs). Ho...

### 38. Fractional Decay KV-Cache: Ownership-Aware Memory Management for Improved Inference Relevancy in Dialog Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18098
- **AI 摘要**: 提出分数衰减KV缓存算法，通过双通道评分管理缓存条目，提升对话系统推理相关性，适应话题演变。
- **原始摘要**: arXiv:2608.18098v1 Announce Type: new Abstract: Key-value (KV) caching is essential for efficient autoregressive inference in transformer based dialog systems, yet existing strategies treat all cached...

### 39. BERTilda: Explainable Topic Lifecycle Tracking with Split/Merge Detection via Similarity-and-Flow Temporal Graphs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18101
- **AI 摘要**: BERTilda是一个可解释的框架，用于跟踪文本流中主题的生命周期，包括主题的诞生、消亡以及分裂和合并等结构重组。它通过相似性和流时间图，在每个时间窗口独立发现主题，并解决时间对应问题。
- **原始摘要**: arXiv:2608.18101v1 Announce Type: new Abstract: Longitudinal text streams exhibit topic birth and death, but also discrete structural reorganizations in which themes split into subtopics or merge into...

### 40. Different Facets of Verbalised Overconfidence: an Interpretability Study
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18106
- **AI 摘要**: 本文研究大语言模型过度自信行为，通过控制推理场景操纵逻辑必然性与可能性，在Qwen3-4B上考察口头认知标记、弃权及数值置信度三种不确定性表达方式，证实模型倾向过度自信，尤其在提示引导下。
- **原始摘要**: arXiv:2608.18106v1 Announce Type: new Abstract: Large language models tend to overconfidence, giving assertive answers when the evidence suggests hedging or abstention. Using controlled reasoning scen...

### 41. Alignment Is All You Need: Instruction-Free Training for General Audio-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18132
- **AI 摘要**: 本文提出一种无需指令微调的训练方法，用于通用音频-语言模型。该方法利用预训练LLM的推理和指令跟随能力，通过跨模态对齐等步骤，减少任务特定监督，提升模型泛化能力。
- **原始摘要**: arXiv:2608.18132v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) are typically built through a multi-stage pipeline consisting of cross-modal alignment, supervised fine-tuning...

### 42. Language Models for Portuguese: A Systematic Mapping Study
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18138
- **AI 摘要**: 本文对葡萄牙语语言模型进行了系统性综述，回顾了近年来学术界和工业界在开发葡萄牙语模型及数据资源方面的努力，并总结了相关进展。
- **原始摘要**: arXiv:2608.18138v1 Announce Type: new Abstract: In recent years, the rapid development of language models has transformed the field of Natural Language Processing through a wide range of applications....

### 43. The Deontic Gap: Large Language Models and the Modal Language of Obligation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18144
- **AI 摘要**: 本文研究大型语言模型是否再现人类道义情态动词的使用模式。通过多个语料库和受控复制实验，发现AI生成文本持续少用积极道义情态词，揭示了模型在表达义务和必要性方面的差异。
- **原始摘要**: arXiv:2608.18144v1 Announce Type: new Abstract: Modal auxiliaries such as must, should, and have to mark necessity and obligation within the contexts of speaker authority and interpersonal stance. We...

### 44. WhiteMatter: All-to-All Cross-Layer Connections via KV Mixing
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18486
- **AI 摘要**: WhiteMatter提出一种新架构，通过KV混合实现所有注意力层间的全连接跨层交互，使浅层消费层能利用深层表示，优于固定连接模式的反馈架构。
- **原始摘要**: arXiv:2608.18486v1 Announce Type: new Abstract: In a Transformer, each layer attends to past tokens only through KV produced at its own depth, despite the presence of deeper representations during aut...

### 45. DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18524
- **AI 摘要**: 本文提出DART-SD方法，通过钻石拓扑感知的检索与自蒸馏，解决多轮工具调用智能体中因全轨迹模仿导致的拓扑崩溃问题，提升LLM自主代理能力。
- **原始摘要**: arXiv:2608.18524v1 Announce Type: new Abstract: Equipping Large Language Models (LLMs) with multi-turn tool-calling capabilities is essential for building autonomous agents. However, progress is funda...

### 46. Shared Circuits for Shared Grammar: Tracing Subject-Verb Agreement Across Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18545
- **AI 摘要**: 该研究探讨多语言大模型内部机制是否跨语言共享，以及这种共享是否随语法操作的显式实现而变化。以现在时主谓一致为案例，该形态句法过程在不同语言中差异显著，且仅被弱化。
- **原始摘要**: arXiv:2608.18545v1 Announce Type: new Abstract: Multilingual large language models often generalize across languages, and prior work suggests that their internal mechanisms can overlap cross-lingually...

### 47. Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18578
- **AI 摘要**: 本文研究后训练量化（PTQ）对大型语言模型主动干扰（PI）的影响。通过FP16、INT8、INT4/NF4三种精度评估，发现量化会放大PI，导致模型性能下降。
- **原始摘要**: arXiv:2608.18578v1 Announce Type: new Abstract: Proactive interference (PI) is a documented failure mode in large language models in which retrieval of a repeatedly overwritten value degrades as prior...

### 48. From Storage to Access: Verifiable Activation of Parametric Knowledge in LLMs via Explicit Priming and Implicit Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18581
- **AI 摘要**: 本文提出VAKE方法，用于验证大语言模型参数化知识的激活。通过显式提示和隐式推理，将知识提取与推理分离，以确定答案源自参数知识还是输入上下文，提升事实问答的可靠性。
- **原始摘要**: arXiv:2608.18581v1 Announce Type: new Abstract: Although Large Language Models (LLMs) encode rich factual knowledge in their parameters, reliably recalling and verifying such knowledge remains a key b...

### 49. TranslatePsy-AfriSLM: High-Quality Data Scaling For Low-Resource Machine Translation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18655
- **AI 摘要**: 本文介绍TranslatePsy-AfriSLM，一个开源高质量平行数据集集合，旨在解决非洲语言机器翻译数据稀缺问题，提升小语言模型在低资源场景下的翻译性能，缩小AI在非洲的数字鸿沟。
- **原始摘要**: arXiv:2608.18655v1 Announce Type: new Abstract: The rapid progress in Artificial Intelligence has largely bypassed African languages, creating a digital divide that limits AI adoption on the continent...

### 50. X2Streaming-TTS: Causal Token-Level Text-to-Speech from Streaming Text with Speech-State Inheritance
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18661
- **AI 摘要**: X2Streaming-TTS提出了一种因果式流式文本转语音框架，能从异步到达的文本令牌生成语音，无需等待完整句子，实现真正的令牌级合成，同时保持感知连续性和有界上下文。
- **原始摘要**: arXiv:2608.18661v1 Announce Type: new Abstract: Streaming text-to-speech is essential for low-latency spoken dialogue systems, yet many systems wait for sentence-level text and are therefore only pseu...

### 51. MemFuse: Multi-Source Memory Fusion from Fragmented Observations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18704
- **AI 摘要**: MemFuse提出多源记忆融合方法，解决代理在跨应用、设备和用户间碎片化观察中整合长期记忆的问题，同时保留来源信息，以构建连贯的情景记忆。
- **原始摘要**: arXiv:2608.18704v1 Announce Type: new Abstract: Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on si...

### 52. Gradient Mirage: Trainable yet Label-Unidentifiable Gradients in Large Language Model Split Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18767
- **AI 摘要**: 本文提出Gradient Mirage防御方法，针对LLM拆分学习中的梯度匹配攻击，破坏梯度与标签目标的一致性，防止服务器恢复私有标签。
- **原始摘要**: arXiv:2608.18767v1 Announce Type: new Abstract: Gradient matching attacks (GMAs) in LLM split learning (SL) rely on a critical yet underexplored assumption: the gradient exposed at the split interface...

### 53. Readable, Faithful, Used: Three Dissociable Properties of Demographic Identity in a Language Model
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18768
- **AI 摘要**: 大型语言模型模拟调查受访者时，回答同质化且不忠实于真实群体差异。本文通过表征相似性分析，在169个人口统计单元中，对1089个读取位置进行评分，探究人口统计身份在LLM中的位置、几何结构是否反映真实群体意见结构，以及模型是否利用这些编码。
- **原始摘要**: arXiv:2608.18768v1 Announce Type: new Abstract: Large language models are widely used to simulate survey respondents, yet their answers are homogeneous and unfaithful to real inter-group differences....

### 54. Do Large Language Models Hallucinate Electric Fata Morganas?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18816
- **AI 摘要**: 本文探讨大语言模型幻觉的哲学意义，认为其不仅是工程缺陷，还涉及机器意识问题，并分析幻觉的已知成因。
- **原始摘要**: arXiv:2608.18816v1 Announce Type: new Abstract: AI hallucinations - that is, outputs which are made up, cannot be verified, or contradict the source material - are generally regarded as an engineering...

### 55. Identifying Implicit Premises for Logical Reconstruction of Argument Graphs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18821
- **AI 摘要**: 本文针对自然语言文本中论证图的逻辑重构难题，聚焦于隐含前提（省略三段论）的识别。文章结合自然语言处理与基于溯因的符号方法，提出生成隐含前提以完善论证逻辑的新方法。
- **原始摘要**: arXiv:2608.18821v1 Announce Type: new Abstract: The logical reconstruction of argument graphs from natural language text is challenging because of the prevalence of enthymemes (i.e., arguments with im...

### 56. MedUAG: Unified Understanding and Generation for Medical Multimodal Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18937
- **AI 摘要**: 本文提出MedUAG，为医学多模态大模型构建统一理解与生成框架。通过构建MedUAGCorpus基准数据集，解决训练评估基准缺失和模型验证不足的问题，推动医学领域UAG模型发展。
- **原始摘要**: arXiv:2608.18937v1 Announce Type: new Abstract: Recent Multimodal Large Language Models (MLLMs) are rapidly evolving into unified understanding and generation (UAG) frameworks. However, extending thes...

### 57. SPADE: Self-Play in Adaptive Synthetic Executable Environments
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19197
- **AI 摘要**: SPADE提出一种自对弈强化学习框架，让单个LLM同时扮演环境设计者和求解者，在自适应合成可执行环境中生成多样化目标，实现持续自我改进。
- **原始摘要**: arXiv:2608.19197v1 Announce Type: new Abstract: Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training environme...

### 58. From Inference to Adaptation: A Unified Optimal Transport View of Vision Language Model
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18339
- **AI 摘要**: 本文提出了一种统一的最优传输视角，将视觉语言模型的推理与适应相结合，以应对测试时的分布偏移问题，避免噪声伪标签误导适应过程。
- **原始摘要**: arXiv:2608.18339v1 Announce Type: cross Abstract: Vision-language models (VLMs) have demonstrated remarkable zero-shot capabilities yet remain sensitive to real-world distribution shifts during infere...

### 59. When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18628
- **AI 摘要**: 本文探讨了视觉语言模型在安全对齐下，即使输入相同，也常拒绝回答默认指令下可正确回答的问题，质疑安全对齐是否抑制了感知基础，并研究了视觉影响与安全对齐之间的动态关系。
- **原始摘要**: arXiv:2608.18628v1 Announce Type: cross Abstract: Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking...

### 60. MLREF: Efficient Module Reuse for Reward Design in Reinforcement Learning via Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18827
- **AI 摘要**: 针对强化学习中奖励函数设计困难的问题，本文提出模块级奖励进化框架（MLREF），利用大语言模型将奖励函数分解为可复用模块，避免整体程序修改导致的不稳定性，提升奖励设计的效率和性能。
- **原始摘要**: arXiv:2608.18827v1 Announce Type: cross Abstract: Reward function design remains a bottleneck in reinforcement learning. While large language models (LLMs) have enabled automated reward generation, ex...

### 61. Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18940
- **AI 摘要**: 本文提出Top-K提示作为训练和推理范式，以更好地捕捉单步逆合成中多样且合理的反应预测，并构建了包含约4560万条验证反应的大规模数据集CREED-CCV-2+USPTO-XL。
- **原始摘要**: arXiv:2608.18940v1 Announce Type: cross Abstract: Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by...

### 62. What is Missing from AI Post-Training AI: An Empirical Analysis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19072
- **AI 摘要**: 本文探讨了AI后训练中缺失的能力，区分了执行级能力（在选定策略内迭代）和策略级能力（根据实验证据调整高层判断），并进行了实证分析。
- **原始摘要**: arXiv:2608.19072v1 Announce Type: cross Abstract: Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downst...

### 63. ReWEIGH the Evidence: Calibrating Token-Level Ordinal Visual Evidence to Mitigate Hallucinations in Large Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19075
- **AI 摘要**: 本文提出ReWEIGH方法，通过校准令牌级序数视觉证据来减少大型视觉语言模型（LVLMs）的幻觉。该方法利用视觉令牌状态通过输出头投影，衡量图像对候选令牌的支持强度，从而在解码时抑制不支持的生成内容。
- **原始摘要**: arXiv:2608.19075v1 Announce Type: cross Abstract: Large vision-language models (LVLMs) often hallucinate, generating content that the input image does not support. Preventing such content during decod...

### 64. Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19098
- **AI 摘要**: 本文研究多教师在线策略蒸馏（M-OPD）中能力失衡的诊断与修复问题，提出Open-MOPD方法，通过分析优化动态并给出可复现方案，以提升多专家整合为通用学生模型的性能。
- **原始摘要**: arXiv:2608.19098v1 Announce Type: cross Abstract: Multi-teacher on-policy distillation (M-OPD) has emerged as a promising paradigm for consolidating domain-specialized reinforcement learning (RL) expe...

### 65. Future Policy Approximation for Offline Reinforcement Learning in LLM Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2509.19893
- **AI 摘要**: 本文探讨了离线强化学习在大语言模型推理中的应用，提出了一种未来策略近似方法，以提升离线策略梯度算法的性能，减少在线RL的不稳定性与计算开销。
- **原始摘要**: arXiv:2509.19893v3 Announce Type: replace Abstract: Reinforcement learning (RL) has emerged as a key driver of post-training for complex reasoning in large language models (LLMs), yet online RL introd...

### 66. Making Implicit Premises Explicit in Logical Understanding of Enthymemes
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.06114
- **AI 摘要**: 本文探讨了省略三段论（enthymemes）的逻辑理解问题，指出NLP方法无法解码其潜在逻辑，而逻辑方法依赖知识库。文章旨在使隐含前提显式化，以提升论证的逻辑理解能力。
- **原始摘要**: arXiv:2603.06114v3 Announce Type: replace Abstract: Real-world arguments in text and dialogues are normally enthymemes (i.e. some of their premises and/or claims are implicit). Natural language proces...

### 67. KA2L: A Knowledge-Aware Active Learning Framework for LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.17566
- **AI 摘要**: KA2L框架通过知识感知主动学习评估并提升大语言模型对特定领域知识的掌握程度，弥补了现有研究在领域知识深度理解和针对性学习方面的不足。
- **原始摘要**: arXiv:2603.17566v2 Announce Type: replace Abstract: Fine-tuning large language models (LLMs) with high-quality knowledge has been shown to enhance their performance effectively. However, there is a pa...

### 68. Self-Improvement of Large Language Models: A Technical Overview and Future Outlook
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.25681
- **AI 摘要**: 本文综述了大语言模型自我改进的技术现状与未来展望，指出人类监督成本高且扩展性有限，而模型自主决策能力增强使其能够自我改进，并探讨了相关方法、挑战及未来方向。
- **原始摘要**: arXiv:2603.25681v2 Announce Type: replace Abstract: As large language models (LLMs) continue to advance, improving them solely through human supervision is becoming increasingly costly and limited in...

### 69. Phantom Transitions in Language Model Fine-Tuning: A Density-Matrix Analysis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.07559
- **AI 摘要**: 本文研究语言模型微调中的“幻影转变”现象：交叉熵损失下降但正确token排名未超越近义竞争者。作者在五个Transformer架构、十个上下文上分析，发现该现象与嵌入重叠有关，并可能通过密度矩阵分析解释。
- **原始摘要**: arXiv:2606.07559v3 Announce Type: replace Abstract: Language models fine-tuned where the correct completion must outrank a near-synonym competitor often fail silently. The cross-entropy loss falls mon...

### 70. First-Token Broadcasters: Mechanistic Origins of Language Identity and Distributed Robustness in Transformers
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.22361
- **AI 摘要**: 本文通过语言身份头消融（LIHA）方法，识别出GPT-2中导致多语言模型错误生成语言的关键注意力头，即“首令牌广播头”，并揭示其机制与分布式鲁棒性。
- **原始摘要**: arXiv:2606.22361v2 Announce Type: replace Abstract: Why do multilingual language models sometimes generate in the wrong language, and why is this so hard to fix? We introduce Language Identity Head Ab...

### 71. Cross-Model Memory Transfer via Target-Side Reader Adaptation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17050
- **AI 摘要**: 本文提出一种跨模型记忆迁移方法，通过目标端阅读器适配，将哈希记忆（如Engram风格）从源模型迁移至目标模型，以改善知识利用，兼顾参数化与非参数化方法的优势。
- **原始摘要**: arXiv:2608.17050v2 Announce Type: replace Abstract: Methods for improving knowledge use in large language models typically fall into two regimes. Non-parametric retrieval offers flexible access to ext...

### 72. Demystifying Training-Time Augmentation for Data-Constrained Language Model Pretraining
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.16246
- **AI 摘要**: 文章探讨在数据受限、计算充裕的预训练环境下，标准自回归预训练会过拟合。研究训练时数据增强方法，以提升固定语料库上多轮训练的效果。
- **原始摘要**: arXiv:2606.16246v3 Announce Type: replace-cross Abstract: As AI labs approach a data ceiling where compute capacity outpaces the rate of new high-quality text generation, language model pretraining is...

### 73. Trace, Verify, and Correct: A Training-Free Framework for Spatial Reasoning in Multimodal LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.04759
- **AI 摘要**: 本文提出一种无需训练的框架，用于提升多模态大语言模型的空间推理能力。该框架通过追踪、验证和纠正推理步骤，确保中间判断与输入图像一致，防止错误传播，从而提高最终答案的准确性。
- **原始摘要**: arXiv:2608.04759v2 Announce Type: replace-cross Abstract: Although Multimodal Large Language Models (MLLMs) have made substantial progress, their spatial reasoning may still produce intermediate judgm...

### 74. Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12746
- **AI 摘要**: 本文针对多模态大语言模型中的物体幻觉问题，提出双流跨锚点校正方法，利用对象级锚点改进长描述生成，并探讨其领域限制。
- **原始摘要**: arXiv:2608.12746v3 Announce Type: replace-cross Abstract: Object hallucination in multimodal large language models arises when language priors and corpus co-occurrence bias outweigh the visual evidenc...

### 75. RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18682
- **AI 摘要**: 本文提出RTPO方法，通过理论分析识别多轮RL训练不稳定的根源，并采用反向策略优化稳定训练，防止性能随轮次增加而退化。
- **原始摘要**: arXiv:2608.18682v1 Announce Type: new Abstract: Training multi-turn agentic workflows with reinforcement learning (RL) enables large language models to perform complex reasoning, use external tools, a...

### 76. Bidirectional representational alignment between biological and artificial neural networks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18244
- **AI 摘要**: 本文研究生物与人工神经网络之间的表征对齐不对称性，即模型表征预测神经反应优于反向预测。作者假设训练中引导表征几何可系统性改善双向对齐，并探索其机制与效果。
- **原始摘要**: arXiv:2608.18244v1 Announce Type: cross Abstract: Recent work has shown that representational alignment between biological and artificial neural networks is asymmetric: model representations predict n...

### 77. OptiModNet: A UNet-Transformer Hybrid with Grouped-Query and Channel Attention for Optic Disc and Cup Segmentation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18516
- **AI 摘要**: 本文提出OptiModNet，一种结合UNet与Transformer的混合模型，用于视盘和视杯分割。该模型引入分组查询和通道注意力机制，在保持低计算需求的同时实现高分割性能，有助于青光眼的早期检测和大规模筛查。
- **原始摘要**: arXiv:2608.18516v1 Announce Type: cross Abstract: Precise segmentation of the optic disc and cup is critical for the early detection and diagnosis of glaucoma. However, achieving consistently high per...

### 78. A Critical Synthesis of Uncertainty Quantification and Foundation Models for Semantic Segmentation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18709
- **AI 摘要**: 本文综合探讨了基础模型在语义分割中的不确定性量化（UQ）问题，旨在解决模型过度自信、可解释性差及对域漂移敏感等挑战，为安全关键应用提供可靠保障。
- **原始摘要**: arXiv:2608.18709v1 Announce Type: cross Abstract: Foundation models are increasingly breaking what seemed to be impossible not long ago by enabling unprecedented accuracy and cross-domain generalizati...

### 79. Forgetting, plasticity, and co-observation: a third facet of continual learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18803
- **AI 摘要**: 本文指出灾难性遗忘和可塑性丧失不足以解释顺序训练与联合训练的性能差距，提出数据共同观察是影响持续学习性能的第三个因素。
- **原始摘要**: arXiv:2608.18803v1 Announce Type: cross Abstract: Efficient continual learning remains a fundamental challenge for deep neural networks. While catastrophic forgetting and loss of plasticity are widely...

### 80. Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.26643
- **AI 摘要**: 本文重新思考大语言模型智能体的自我进化过程，提出将技能视为可训练状态，并采用受限的探索-利用过程来缓解技能过拟合问题，以提升模型在真实环境中的泛化能力。
- **原始摘要**: arXiv:2607.26643v2 Announce Type: replace Abstract: Enabling large language model (LLM) agents to accumulate and reuse experience from past interactions remains a central challenge in real-world appli...

### 81. Hybrid LLM-Augmented Reinforcement Learning Agents for Complex Sequential Decision Tasks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.03502
- **AI 摘要**: 本文提出一种混合LLM与强化学习的智能体框架，用于复杂序列决策任务。LLM负责高层抽象与任务分解，RL负责精确动作优化与环境交互，以克服LLM在长时程决策中的不足。
- **原始摘要**: arXiv:2608.03502v2 Announce Type: replace Abstract: Large Language Models (LLMs) have recently shown strong capabilities in reasoning, planning, and tool-use, enabling new forms of autonomous agents....

### 82. FiLoRA: Focus-and-Ignore LoRA for Controllable Feature Reliance
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.02060
- **AI 摘要**: FiLoRA提出一种名为Focus-and-Ignore LoRA的方法，通过显式调节多模态基础模型对不同内部特征路径的依赖，实现对预测的控制，以应对捷径和虚假相关行为，优于现有事后分析或数据级干预方法。
- **原始摘要**: arXiv:2602.02060v2 Announce Type: replace-cross Abstract: Multimodal foundation models integrate heterogeneous signals across modalities, yet it remains unclear whether their predictions can be contro...

### 83. Structure-Informed Estimation for Pilot-Limited MIMO Channels via Tensor Decomposition
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.04083
- **AI 摘要**: 本文提出一种结构信息混合估计器，将导频受限的MIMO信道估计建模为低秩张量补全问题，利用张量分解从稀疏导频观测中恢复信道，解决了以往方法需完全观测张量的限制。
- **原始摘要**: arXiv:2602.04083v3 Announce Type: replace-cross Abstract: Accurate channel state information in wideband MIMO systems is constrained by pilot overhead, a challenge intensifying as bandwidths scale tow...

### 84. Hybrid ANN-SNN Pipeline with Local Plasticity
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.20151
- **AI 摘要**: 本文提出一种混合ANN-SNN流水线，利用预训练人工神经网络的丰富嵌入来提升脉冲神经网络性能。架构将预训练的EfficientNet编码器与CoLaNET脉冲分类器耦合，通过速率编码将激活转换为脉冲序列，并使用局部生物启发规则训练SNN分类器。
- **原始摘要**: arXiv:2606.20151v2 Announce Type: replace-cross Abstract: This work proposes a hybrid ANN-SNN pipeline that effectively leverages the rich embeddings of pretrained artificial neural networks (ANNs) to...

### 85. Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17253
- **AI 摘要**: 本文提出Co-RL方法，通过多智能体强化学习中的多样化群体协作，使模型无需人工标注即可自主涌现推理能力，减少对可验证奖励的依赖，提升推理泛化性。
- **原始摘要**: arXiv:2608.17253v2 Announce Type: replace-cross Abstract: Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its stronge...

### 86. Safe Domain Adaptation for Physics: Overcoming Nuisances, Label Shifts, and Simulation Priors
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18190
- **AI 摘要**: 本文探讨物理领域中的域适应问题，指出传统假设（仅存在干扰且目标分布一致）在物理中不成立，因为模拟可能错误且目标分布本身是测量对象。文章提出安全域适应方法，以应对干扰、标签偏移和模拟先验。
- **原始摘要**: arXiv:2608.18190v1 Announce Type: new Abstract: Domain adaptation is widely used to make neural networks trained on simulations applicable to experimental data. Its premise is that the two domains dif...

### 87. The Road Taken: The Role of Optimizers at the Edge of Stability
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18415
- **AI 摘要**: 本文研究深度学习优化器在稳定性边缘的现象，发现梯度下降等一阶方法显著违反经典下降引理预测的不稳定阈值，并探讨了优化器在此边缘状态下的作用机制。
- **原始摘要**: arXiv:2608.18415v1 Announce Type: new Abstract: The edge of stability refers to a phenomenon in deep learning with gradient-based optimizers where the Hessian eigenvalues of the loss remain stable abo...

### 88. Infrared Universality of Collective Dynamics across Transformer and State-Space Architectures
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18592
- **AI 摘要**: 本文探讨不同神经架构是否具有共同的集体动力学。针对Transformer语言模型发现的近边缘长记忆动力学，研究Mamba模型的选择性状态空间机制，检验其是否呈现类似的红外增强时间尺度态密度。
- **原始摘要**: arXiv:2608.18592v1 Announce Type: new Abstract: Whether distinct neural architectures develop common collective dynamics remains an open question. Recent analysis of Transformer language models reveal...

### 89. To Go Far, Go Together: Diverse Preferences Induce a Curriculum for Reward Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18770
- **AI 摘要**: 本文从公平性角度探讨奖励模型学习，指出仅追求数据高效和准确的用户级奖励模型不足，需考虑多样化偏好以优化策略，提出偏好多样性可引导奖励优化的课程学习。
- **原始摘要**: arXiv:2608.18770v1 Announce Type: new Abstract: Learning a reward model from human feedback and optimizing a policy against it is one approach to aligning AI systems with individual users. From a fair...

### 90. GraphK: Variable-Size Graph Generation with Efficient Edge Construction
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18777
- **AI 摘要**: GraphK是一种新型图生成框架，通过编码器-采样器-解码器结构，克服了自回归方法在规模、灵活性和结构建模上的局限，实现了高效且灵活的图生成。
- **原始摘要**: arXiv:2608.18777v1 Announce Type: new Abstract: Graph generation models have advanced significantly with deep learning, yet they remain limited in scalability, flexibility, and ability to model underl...

### 91. A Unifying Relational Perspective on Expressive Lottery Tickets
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18819
- **AI 摘要**: 本文提出统一关系视角，研究稀疏性对关系图神经网络（RGNNs）和时序图神经网络（TGNNs）表达力的影响，将强表达彩票假设（SELTH）推广到多关系与时序领域，证明存在保持WL表达力的稀疏网络。
- **原始摘要**: arXiv:2608.18819v1 Announce Type: new Abstract: Graph neural networks (GNNs) are widely used, but how parameter sparsity affects the expressivity of relational (RGNNs) and temporal (TGNNs) variants is...

### 92. On the Slow Convergence to Trivial Solutions of Algorithms for Hard Optimization Problems
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18910
- **AI 摘要**: 本文探讨了硬组合优化问题（多为NP难）的算法收敛缓慢现象。通过随机实例的平均情况分析，研究揭示了在足够困难的实例下，算法收敛到平凡解的缓慢过程，为理解算法性能提供了新视角。
- **原始摘要**: arXiv:2608.18910v1 Announce Type: new Abstract: Hard combinatorial optimization problems, many of which are NP-hard, present fundamental algorithmic challenges. Average-case analysis on random instanc...

### 93. Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19151
- **AI 摘要**: 本文研究多变量Hawkes驱动随机微分方程在非马尔可夫环境下的随机控制问题，提出有限维马尔可夫化算法近似多变量Hawkes过程，并利用机器学习方法求解。
- **原始摘要**: arXiv:2608.19151v1 Announce Type: new Abstract: We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting....

### 94. Self-supervised In-context Operator Learning for Stochastic Mean-Field Control
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18282
- **AI 摘要**: 本文提出将随机平均场控制问题转化为算子学习问题，并开发了首个基于自监督上下文学习的网格无关方法，可高效解决多实例问题，无需重新优化。
- **原始摘要**: arXiv:2608.18282v1 Announce Type: cross Abstract: Stochastic mean-field control (MFC) provides a fundamental framework for coordinating large populations of interacting agents under uncertainty, with...

### 95. Coupled-cluster molecular properties across the main group that extrapolate beyond training size
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18346
- **AI 摘要**: 本文提出MEHnet-MG，一种等变网络，从廉价的B3LYP/def2-SVP计算预测有效单电子哈密顿量，并推导多种分子性质，解决了耦合簇理论计算成本高与密度泛函理论精度不足的矛盾。
- **原始摘要**: arXiv:2608.18346v1 Announce Type: cross Abstract: Coupled-cluster theory defines the accuracy standard for molecular electronic-structure properties but scales too steeply for routine application, whe...

### 96. Which Negatives Matter? Ask Your Text Encoder: Adaptive Similarity Margins for Dense-Caption Retrieval
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18521
- **AI 摘要**: 本文针对密集字幕检索中InfoNCE损失在强预训练初始化下过早饱和的问题，提出自适应相似性边距方法，利用文本编码器识别负样本的重要性，以改善对比微调效果。
- **原始摘要**: arXiv:2608.18521v1 Announce Type: cross Abstract: Dense-caption retrieval has recently been improved by introducing segmentation, edge maps, LLM-filtered captions, and cross-modal modules into contras...

### 97. Sharper Regret Bounds for Time-Varying Gaussian Process Bandits with Constant Exploration
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18863
- **AI 摘要**: 本文研究时变环境下高斯过程多臂老虎机的贝叶斯优化，提出使用恒定探索参数的GP-UCB算法，通过局部置信事件获得更紧的期望遗憾界。
- **原始摘要**: arXiv:2608.18863v1 Announce Type: cross Abstract: We study Bayesian optimization in a time-varying environment where the unknown reward function evolves according to a Gaussian process drift model. Ex...

### 98. Quantum Tensor Network Learning with DMRG
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18901
- **AI 摘要**: 张量网络是一种新兴的机器学习方法，受量子多体物理模拟启发。本文提出矩阵乘积态的全局归一化条件，使其表示量子态，并研究两种局部优化方法。
- **原始摘要**: arXiv:2608.18901v1 Announce Type: cross Abstract: Tensor Networks are a relatively new machine learning approach. The architectures proposed initially are inspired by approaches from quantum many-body...

### 99. Breaking the weakest link to evade vision language models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18938
- **AI 摘要**: 本文研究视觉语言模型（VLMs）在多模态对齐中的对抗性鲁棒性，重点探索针对该对齐的逃避攻击，揭示其脆弱性，为提升模型安全性提供见解。
- **原始摘要**: arXiv:2608.18938v1 Announce Type: cross Abstract: Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual...

### 100. Robust Risk Under Evolving Uncertainty: A Wasserstein Counterpart of the Entropic Value-at-Risk
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19073
- **AI 摘要**: 本文提出一种在演化不确定性下的稳健风险度量方法，通过最优传输球替代相对熵球，以覆盖名义模型认为不可能但可能发生的灾难情景，为仍在学习环境的智能体提供更安全的对冲策略。
- **原始摘要**: arXiv:2608.19073v1 Announce Type: cross Abstract: An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a...

### 101. Contrasting Cost-Agnostic and Cost-Sensitive Losses under Limited Model Capacity via $\mathcal H$-consistency
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2502.19522
- **AI 摘要**: 本文探讨了在有限模型容量下，任务无关损失（如交叉熵）与任务相关损失（如加权交叉熵）的对比。理想情况下两者等价，但实际中模型容量有限，文章通过H一致性理论分析了两者的差异，为实践提供指导。
- **原始摘要**: arXiv:2502.19522v2 Announce Type: replace Abstract: There is a prevalent debate in machine learning about whether practitioners should train models to optimize a task-agnostic objective (e.g., cross e...

### 102. Escaping Local Minima Provably in Non-convex Matrix Sensing: A Deterministic Framework via Simulated Lifting
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.05887
- **AI 摘要**: 本文提出一种确定性框架，通过模拟提升将低秩矩阵感知中的局部极小值转化为严格鞍点，从而证明梯度方法可全局收敛，为过参数化提升的优化理论提供新视角。
- **原始摘要**: arXiv:2602.05887v3 Announce Type: replace Abstract: Low-rank matrix sensing is a fundamental yet challenging nonconvex problem whose optimization landscape typically contains numerous spurious local m...

### 103. Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.01499
- **AI 摘要**: 本文比较了进化策略（ES）与GRPO在LLM后训练中的表现，发现ES在单任务准确率上相当或更优，但在参数空间解上存在差异，并探讨了持续学习场景下的影响。
- **原始摘要**: arXiv:2604.01499v3 Announce Type: replace Abstract: Evolution Strategies (ES) have emerged as a scalable gradient-free alternative to reinforcement learning based LLM fine-tuning, but it remains uncle...

### 104. LionMuon: Alternating Spectral and Sign Descent for Efficient Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.19811
- **AI 摘要**: LionMuon是一种新的优化器，结合了Lion的廉价更新和Muon的强方向，通过交替使用谱矩阵符号和符号下降，在保持效果的同时降低平均每步成本，适用于大规模优化。
- **原始摘要**: arXiv:2605.19811v3 Announce Type: replace Abstract: In large-scale optimization, the cheapness and effectiveness of update steps are the most crucial factors for a successful optimizer. Sign-based opt...

### 105. A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.11917
- **AI 摘要**: 本文提出一种基于Forney因子图的多输出高斯过程回归方法，通过最近邻链将候选输入排序，实现可扩展计算，处理不同输出在不同输入观测的情况。
- **原始摘要**: arXiv:2608.11917v2 Announce Type: replace Abstract: Multi-output Gaussian process regression scales cubically in the number of observations times outputs, and dense kernel-matrix methods need bespoke...

### 106. Conformal Policy Control
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.02196
- **AI 摘要**: 本文提出一种利用安全参考策略作为概率调节器的方法，以平衡智能体探索与安全约束，防止高风险环境中因行为变化过大导致违规，从而在保证安全的同时促进有效学习。
- **原始摘要**: arXiv:2603.02196v4 Announce Type: replace-cross Abstract: An agent must try new behaviors to explore and improve. In high-stakes environments, an agent that violates safety constraints may cause harm...

### 107. SHANG++: Robust Stochastic Acceleration under Multiplicative Noise
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.09355
- **AI 摘要**: 本文针对乘法噪声下Nesterov加速的脆弱性，提出两种加速随机梯度下降方法。通过离散化Hessian驱动的Nesterov加速梯度流，导出SHANG及其改进版本，显著提升噪声鲁棒性。
- **原始摘要**: arXiv:2603.09355v2 Announce Type: replace-cross Abstract: Under the multiplicative noise scaling (MNS) condition, original Nesterov acceleration is provably sensitive to noise and may diverge when gra...

### 108. Pre-Training for Simulation-Based Science: A Study on Jet Foundation Model Training Objectives
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.14870
- **AI 摘要**: 本文系统比较了基于模拟的科学领域中基础模型的不同预训练目标，利用丰富且带标签的模拟数据，探索了监督预训练与自监督掩码预训练的效果，为科学AI基础模型训练提供了新视角。
- **原始摘要**: arXiv:2606.14870v2 Announce Type: replace-cross Abstract: Foundation models (FMs) trained on large datasets and fine-tuned on downstream tasks have emerged as a powerful paradigm in AI for science. In...

### 109. Untrainable elements determine what physical learning remembers
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.00097
- **AI 摘要**: 本文研究物理学习规则如平衡传播、耦合学习等训练电阻网络时，学习函数由训练落点决定，并受电路尺度不变性和质量守恒两个属性影响，探讨了不可训练元素对物理学习记忆的影响。
- **原始摘要**: arXiv:2608.00097v2 Announce Type: replace-cross Abstract: Physical learning rules such as equilibrium propagation (EP), coupled learning (CL), and adjoint coupled learning (AL) train resistive network...

### 110. Counterfactual Behavior Cloning: Offline Imitation Learning from Imperfect Human Demonstrations
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2025年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2505.10760
- **AI 摘要**: 本文提出反事实行为克隆方法，用于从不完美人类演示中进行离线模仿学习。该方法通过生成反事实示例，避免匹配错误行为，提升学习效果。
- **原始摘要**: arXiv:2505.10760v2 Announce Type: replace Abstract: Learning from humans is challenging because people are imperfect teachers. When everyday humans show the robot a new task they want it to perform, h...

### 111. Aug 12, 2026Introducing Grok 4.6
- **来源**: xAI Blog (TIER1)
- **发布日期**: Aug 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://x.ai/news/grok-4-6
- **AI 摘要**: 文章标题为“Aug 12, 2026 Introducing Grok 4.6”，但未提供摘要内容，因此无法生成摘要。

### 112. Qwen3Guard: Real-time Safety for Your Token Stream
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen3guard/
- **AI 摘要**: Qwen3Guard是Qwen家族首个安全护栏模型，基于Qwen3微调，用于提示和响应的安全检测，提供风险等级和分类，实现精确审核，确保负责任的AI交互。
- **原始摘要**: Tech Report GitHub Hugging Face ModelScope DISCORD Introduction We are excited to introduce Qwen3Guard, the first safety guardrail model in the Qwen family. Built upon the powerful Qwen3 foundation mo...

### 113. Qwen-Image-Edit: Image Editing with Higher Quality and Efficiency
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image-edit/
- **AI 摘要**: Qwen团队推出Qwen-Image-Edit，基于20B参数的Qwen-Image模型，扩展其文本渲染能力至图像编辑，实现精确文本编辑。该模型同时利用Qwen2.5-VL进行视觉语义控制和VAE编码器进行视觉外观控制，提升编辑质量和效率。
- **原始摘要**: QWEN CHAT GITHUB HUGGING FACE MODELSCOPE DISCORD We are excited to introduce Qwen-Image-Edit, the image editing version of Qwen-Image. Built upon our 20B Qwen-Image model, Qwen-Image-Edit successfully...

### 114. Qwen-Image: Crafting with Native Text Rendering
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image/
- **AI 摘要**: Qwen团队发布Qwen-Image，一个20B参数的MMDiT图像基础模型，在复杂文本渲染和精确图像编辑方面取得显著进展，支持多行布局、段落级语义和细粒度细节，并支持字母文字。
- **原始摘要**: GITHUB HUGGING FACE MODELSCOPE DEMO DISCORD We are thrilled to release Qwen-Image, a 20B MMDiT image foundation model that achieves significant advances in complex text rendering and precise image edi...

### 115. GSPO: Towards Scalable Reinforcement Learning for Language Models
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/gspo/
- **AI 摘要**: 文章提出GSPO方法，旨在解决现有RL算法（如GRPO）在长训练中的不稳定性和模型崩溃问题，以实现语言模型的可扩展强化学习，提升推理和问题解决能力。
- **原始摘要**: PAPER DISCORD Introduction Reinforcement Learning (RL) has emerged as a pivotal paradigm for scaling language models and enhancing their deep reasoning and problem-solving capabilities. To scale RL, t...

### 116. Qwen-MT: Where Speed Meets Smart Translation
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-mt/
- **AI 摘要**: Qwen-MT更新基于Qwen3，利用万亿级多语言和翻译数据，结合强化学习，提升92种语言的翻译准确性和流畅度。
- **原始摘要**: DEMO API DISCORD Introduction Here we introduce the latest update of Qwen-MT (qwen-mt-turbo) via Qwen API. This update builds upon the powerful Qwen3, leveraging trillions multilingual and translation...

### 117. New Kimi K2 Models & Updated Pricing
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/Kimi_API_Newsletter
- **AI 摘要**: 本文介绍了新的Kimi K2模型及其更新的定价策略，可能涉及模型性能提升和价格调整，旨在为用户提供更高效、经济的AI服务。

### 118. Kimi K2: Open Agentic Intelligence
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/k2-report
- **AI 摘要**: 本文介绍Kimi K2，一个面向智能体应用的开源模型，强调其在复杂任务中的自主决策与工具调用能力，旨在推动开放智能体生态发展。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
