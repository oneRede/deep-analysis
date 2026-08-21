# RSS 聚合报告 - AI模型

**生成时间**: 2026-08-21 11:22:50
**文章数量**: 127 篇

---

### 1. Is KV Cache in a high dimensional vector space? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T18:18:10+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtrdem/is_kv_cache_in_a_high_dimensional_vector_space_d/
- **AI 摘要**: 文章探讨KV缓存是否处于高维向量空间，指出推理时模型工作记忆主要存储在KV缓存中，其并非扁平列表，而是具有可导航几何结构的向量集合，键携带模型学习到的关联语义。
- **原始摘要**: I've been doing some research on this question: At inference time a large part of a model's working memory lives in the KV cache, plus whatever external memory the harness bolts on. I've been poking a...

### 2. Mapping intrinsic rank and informational gravity in complex tabular data: I developed a non-parametric, model-agnostic, information-theoretic diagnostic to bypass the limits of linear, rank, and Euclidean baselines. [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T13:34:28+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtjotb/mapping_intrinsic_rank_and_informational_gravity/
- **AI 摘要**: 作者开发了一种非参数、模型无关的信息论诊断方法，用于映射复杂表格数据的内在秩和信息引力，以克服线性、秩和欧几里得基线的限制，并提供了预印本和开源代码。
- **原始摘要**: Links: Preprint: https://doi.org/10.5281/zenodo.22028087 Entropic Scree Function v1.0.0 / GitHub: https://github.com/tjleestjohn/Entropic-Scree TL;DR: Standard PCA fundamentally fractures non-linear d...

### 3. The spectral neuron - an ML primitive for scalable and interpretable models [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T10:20:47+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtfimo/the_spectral_neuron_an_ml_primitive_for_scalable/
- **AI 摘要**: 文章探讨了在广告领域构建既简单、可扩展、可解释又可控制的机器学习模型的可能性，并提出了“谱神经元”这一新的ML原语，相关研究已形成预印本。
- **原始摘要**: Worked some time ago on one of the ad teams at Yahoo, and this grew out of a question I kept returning to while there are there "simple" models that are both simple, scalable, interpretable, and contr...

### 4. About the impact of grouping classes in multiclass classification [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T07:42:20+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtctaz/about_the_impact_of_grouping_classes_in/
- **AI 摘要**: 文章探讨多分类问题中将多个类别合并为一个类别的影响，询问是否有相关共识或指示，并讨论其潜在危害。
- **原始摘要**: A premise: I hope this question is "worth" of this subreddit, I did a decent amount of research before posting, I thought it was potentially interesting enough for it, but possibly not basic enough fo...

### 5. Same GRPO recipe on three from-scratch LLMs (353M/316M/672M) gave three different outcomes, with no clean relationship to scale [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T21:30:26+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vszsit/same_grpo_recipe_on_three_fromscratch_llms/
- **AI 摘要**: 作者从零训练了三个不同规模的LLM，并用相同的SFT和GRPO流程进行后训练。预训练表现正常，但GRPO对两个较大模型产生了负面影响，且结果与模型规模无清晰关联，原因不明。
- **原始摘要**: I trained three LLMs from scratch in raw PyTorch then post-trained each one with SFT and then GRPO. Same process every time: same synthetic arithmetic curriculum, same reward function, same hyperparam...

### 6. How much of the weight-space perception gap is actually symmetry? Evidence from ~1.8M fitted SIRENs [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T19:24:12+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vswdnf/how_much_of_the_weightspace_perception_gap_is/
- **AI 摘要**: 文章探讨权重空间学习中参数对称性对语义读取的影响，通过约180万SIRENs实验，发现独立拟合的网络权重语义读取崩溃，而共享初始化的网络表现良好，挑战了对称性作为主要解释的观点。
- **原始摘要**: I’ve been looking at a fairly basic question in weight-space learning that I don’t think gets separated cleanly enough: Why does reading semantics directly from neural network weights work pretty well...

### 7. Trained an diffusion model that runs on 264KB of RAM [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-18T09:26:21+00:00 (3 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vrk7t5/trained_an_diffusion_model_that_runs_on_264kb_of/
- **AI 摘要**: 作者训练了一个可在264KB RAM上运行的扩散模型，展示了极低资源下的AI推理能力，可能涉及模型压缩或轻量化技术。
- **原始摘要**: I recently bought a Shrike lite which has got 264KB of SRAM. I decided to train an image generation model that generates 32*32 pixel images. The microcontroller also has an FPGA onboard which I used t...

### 8. Revisiting the Efficient Channel Attention paper (2019, 12k citations) - the central hypothesis isn't quite right [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-16T10:13:44+00:00 (5 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/
- **AI 摘要**: 本文重新审视ECA注意力机制论文，指出其核心假设可能不准确。ECA通过一维卷积替代SE的降维操作，提升性能，但作者认为其跨通道交互的假设存在问题。
- **原始摘要**: ECA was positioned as a successor to SE. The idea behind ECA is quite simple. Unlike SE which reduces the channel means into a smaller hidden layer, it directly uses a 1d convolution kernel on the cha...

### 9. How can we solve long-range recall in linear attention? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-16T07:47:09+00:00 (5 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/
- **AI 摘要**: 文章探讨线性注意力在长序列（如DNA）中的长程召回问题。作者在基准测试中发现模型长程召回性能不佳，并寻求解决方案。
- **原始摘要**: Recently, I started working on DNA sequence modeling and decided to explore linear attention, mainly because DNA sequences can easily reach 1M tokens, making standard softmax attention extremely expen...

### 10. Multi-Vector (Late Interaction) Embedding Models with Sentence Transformers
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Tue, 18 Aug 2026 00:00:00 GMT (3 天前)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/multi-vector-encoder
- **AI 摘要**: 文章介绍多向量（晚期交互）嵌入模型在句子转换器中的应用，探讨其原理、优势及实现方法，以提升文本检索和语义匹配性能。

### 11. Up to 3.2x Faster Inference with LFM2.5-DSpark
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Thu, 20 Aug 2026 16:52:57 GMT (今天)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/LiquidAI/lfm25-dspark
- **AI 摘要**: 文章标题提及LFM2.5-DSpark，但摘要内容为空，无法提供具体信息。

### 12. v1.6.0: Mistrall goes Small 3.1 with vision
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2025-03-20T15:03:08Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.6.0
- **AI 摘要**: Mistral AI发布v1.6.0版本，为mistral-inference库新增对Mistral Small 3.1模型的支持，该模型具备视觉能力，同时修复了缺失换行问题。
- **原始摘要**: What's Changed Missing new line by @theophilegervet in #234 Add support to Mistral Small 3.1 by @juliendenize in #239 Remove file refs by @juliendenize in #240 Release 1.6.0 by @juliendenize in #241 N...

### 13. v1.4.0: Pixtral 👀
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-09-13T13:10:17Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.4.0
- **AI 摘要**: Mistral AI发布v1.4.0版本，推出Pixtral多模态模型，支持视觉理解能力。用户可通过pip升级安装mistral_inference，并从Hugging Face下载模型。
- **原始摘要**: Pixtral Mistral models can now 👀 ! pip install --upgrade mistral_inference # >= 1.4.0 Download: from huggingface_hub import snapshot_download from pathlib import Path mistral_models_path = Path.home()...

### 14. v1.3.0 Mistral-Nemo
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-18T15:45:30Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.3.0
- **AI 摘要**: Mistral与NVIDIA合作推出Mistral-Nemo模型，提供安装和下载指南，用户可通过pip安装mistral-inference>=1.3.0获取该模型。
- **原始摘要**: Welcome Mistral-Nemo from Mistral 🤝 NVIDIA Read more about Mistral-Nemo here. Install pip install mistral-inference>=1.3.0 Download export NEMO_MODEL=$HOME/12B_NEMO_MODEL wget https://models.mistralcd...

### 15. v1.2.0 Add Mamba
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-16T18:41:37Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.2.0
- **AI 摘要**: Mistral AI发布v1.2.0版本，新增Codestral-Mamba和Mathstral模型。Codestral-Mamba基于Mamba架构，支持代码生成；Mathstral专注于数学推理。用户可通过pip安装相关依赖使用。
- **原始摘要**: Welcome 🐍 Codestral-Mamba and 🔢 Mathstral pip install mistral-inference>=1.2.0 Codestral-Mamba pip install packaging mamba-ssm causal-conv1d transformers Download export MAMBA_CODE=$HOME/7B_MAMBA_CODE...

### 16. v1.1.0 Add LoRA
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-05-24T18:32:10Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.1.0
- **AI 摘要**: mistral-inference 1.1.0版本新增对LoRA模型的支持，可运行通过mistral-finetune训练的LoRA模型。用户可基于7B基础模型加载LoRA权重进行推理，简化了微调模型的部署流程。
- **原始摘要**: mistral-inference==1.1.0 supports running LoRA models that were trained with: https://github.com/mistralai/mistral-finetune Having trained a 7B base LoRA, you can run mistral-inference as follows: fro...

### 17. TTSD-FAR: Test-Time Self-Distillation with Fisher-Anchored Restoration for Missing-Modality Emotion Recognition in LVLMs
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18386
- **AI 摘要**: 本文提出TTSD-FAR方法，用于大型视频语言模型在多模态情感识别中处理测试时模态缺失问题。通过测试时自蒸馏和Fisher锚定恢复，缓解部分观测导致的分布偏移，提升鲁棒性。
- **原始摘要**: arXiv:2608.18386v1 Announce Type: new Abstract: Large video-language models (LVLMs) have shown remarkable performance on multimodal tasks like multimodal emotion recognition (ER) in the wild. ER is in...

### 18. Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18484
- **AI 摘要**: 本文提出一种无需训练的块稀疏注意力方法，用于加速视频生成和世界模型。通过优化分区几何，改善查询支持重叠和残差可预测性，从而在保留注意力质量的同时提升效率。
- **原始摘要**: arXiv:2608.18484v1 Announce Type: new Abstract: Training-free block-sparse attention can accelerate video transformers, but row-wise attention concentration does not by itself specify an executable sp...

### 19. PCQA-R1: Advancing Generalized 3D Point Cloud Quality Assessment with Reinforcement Learning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18627
- **AI 摘要**: 本文提出PCQA-R1，利用强化学习提升三维点云质量评估的泛化能力。针对现有LMM方法依赖监督微调、跨数据集泛化差的问题，引入强化学习策略，使模型能适应不同MOS尺度，实现更通用的无参考点云质量评估。
- **原始摘要**: arXiv:2608.18627v1 Announce Type: new Abstract: No-reference point cloud quality assessment (PCQA) has been an active topic in recent years and is used to measure and optimize the visual experience of...

### 20. CL4D: Contrastive Language-4D Pretraining for Vision-Language Reasoning in Dynamic Scenes
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18734
- **AI 摘要**: CL4D提出首个对比语言-4D预训练框架，用于动态场景中的视觉-语言推理。它联合建模时空结构和运动演化，弥补现有编码器在动态环境中的不足，提升具身AI的4D理解能力。
- **原始摘要**: arXiv:2608.18734v1 Announce Type: new Abstract: 4D understanding and reasoning is a fundamental capability for embodied AI agents operating in dynamic physical environments. However, existing vision e...

### 21. TractoGraphVLM: A Unified Vision-Language Framework for White Matter Tractography
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18166
- **AI 摘要**: TractoGraphVLM是一个统一的视觉语言框架，用于白质纤维束成像，支持束分类、文本到束检索、解剖描述和视觉问答四项任务，基于共享GPS架构和训练流程，以处理纤维束的复杂拓扑结构。
- **原始摘要**: arXiv:2608.18166v1 Announce Type: cross Abstract: Vision language models have transformed 2D medical imaging, yet extending them to 3D white matter tractography remains challenging due to the complex...

### 22. Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned Objectives for MPC Planning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18746
- **AI 摘要**: 本文提出决策度量对齐概念，用于JEPA式潜在世界模型中的MPC规划。引入Plan-Real Spearman和CEM-stage Spearman指标，诊断潜在-真实排名不一致，并设计动作条件目标以提升规划性能。
- **原始摘要**: arXiv:2608.18746v1 Announce Type: cross Abstract: JEPA-style latent world models can use Euclidean distance to a goal latent as the cost for model-predictive control (MPC). Strong decoding of task var...

### 23. WorldPack: Dynamic Frame Compression for Long-context Video World Modeling
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2512.02473
- **AI 摘要**: 本文提出WorldPack，一种用于长上下文视频世界建模的动态帧压缩方法。现有方法未显式考虑3D视点几何或仅检索少量空间相关帧，难以实现长时间跨度的时空一致生成。WorldPack通过动态压缩过去帧，提升长时程视频生成的时空一致性。
- **原始摘要**: arXiv:2512.02473v3 Announce Type: replace Abstract: Video world models have attracted significant attention for their ability to produce high-fidelity future visual observations conditioned on past ob...

### 24. OccDirector: Language-Guided Behavior and Interaction Generation in 4D Occupancy Space
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.22240
- **AI 摘要**: OccDirector是一个在4D占用空间中生成自动驾驶动态的框架，通过语言引导实现复杂多智能体交互，弥补了语义与时空之间的差距。
- **原始摘要**: arXiv:2604.22240v2 Announce Type: replace Abstract: Generative world models increasingly rely on 4D occupancy for realistic autonomous driving simulation. However, existing generation frameworks depen...

### 25. PEEK: Picking Essential frames via Efficient Knowledge distillation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.31029
- **AI 摘要**: PEEK提出一种高效的动态帧采样方法，用于视频字幕生成。它通过知识蒸馏选择关键帧，在保持性能的同时降低计算成本，优于均匀采样和现有自适应方法。
- **原始摘要**: arXiv:2605.31029v2 Announce Type: replace Abstract: Video-language models can process only a limited number of frames, making frame selection a key bottleneck for efficient video captioning. Most capt...

### 26. Look Clearly Before Answering: Mitigating Hallucinations in LVLMs via Saliency-Driven Perceptual Realignment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.16841
- **AI 摘要**: 本文提出基于显著性驱动的感知重对齐方法，以缓解大型视觉语言模型中的幻觉问题，通过重新对齐视觉感知与记忆来减少跨模态偏差。
- **原始摘要**: arXiv:2607.16841v2 Announce Type: replace Abstract: Large vision-language models (LVLMs) have demonstrated remarkable capabilities in multimodal understanding. However, they remain prone to hallucinat...

### 27. SE-MoLoRA: Shared-Expert LoRA Adapters for Domain-Specific Photographic Assessment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17514
- **AI 摘要**: SE-MoLoRA是一种模块化参数高效适配框架，用于领域特定的摄影评估。它通过始终激活的共享LoRA专家和路由适配器，将通用摄影知识与专家残差判断分离，提升视觉语言模型在摄影批评方面的能力。
- **原始摘要**: arXiv:2608.17514v2 Announce Type: replace Abstract: Vision-language models can describe images fluently, but they often fail to provide actionable photographic critique because semantic content and ae...

### 28. Accelerating GPT-5.6 Sol UltrafastAugust 13, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ust 13, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai
- **AI 摘要**: 文章介绍GPT-5.6 Sol的加速技术，可能涉及模型优化或推理加速方法，旨在提升性能与效率。

### 29. The Economics of AI ReasoningJune 17, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 17, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/the-economics-of-ai-reasoning
- **AI 摘要**: 文章探讨了AI推理的经济学，分析了推理成本、计算资源分配及模型效率对AI系统部署的影响，并提出了优化推理策略以平衡性能与成本的方法。

### 30. Which is faster: Kimi K2.6 on Cerebras or Gemini Flash?June 05, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 05, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/which-is-faster-gemini-3-5-flash-or-kimi-k2-6-on-cerebras
- **AI 摘要**: 文章对比了Kimi K2.6在Cerebras平台与Gemini Flash的性能，评估了推理速度与效率，为开发者选择模型提供参考。

### 31. The world’s fastest GLM-4.6 – now available on CerebrasNovember 18, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 18, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm
- **AI 摘要**: Cerebras宣布其平台现已支持GLM-4.6模型，号称全球最快，该模型在推理速度上具有显著优势，适用于高性能AI应用场景。

### 32. REAP: One-Shot Pruning for Trillion-Parameter Mixture-of-Experts ModelsOctober 16, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 16, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/reap
- **AI 摘要**: 本文介绍REAP，一种针对万亿参数混合专家模型的一次性剪枝方法，旨在高效压缩模型规模，同时保持性能，适用于大规模AI模型部署。

### 33. MoE Math Demystified: What Does 8x7B Actually Mean?October 14, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 14, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/moe-guide-calculator
- **AI 摘要**: 文章解释了MoE（混合专家）模型中“8x7B”的含义，即8个专家模型，每个有70亿参数，但推理时仅激活部分专家，从而在保持性能的同时降低计算成本。

### 34. Thinking Inside the Box: The Implicit Chain Transformer for Efficient State TrackingDecember 12, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 12, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/thinking-inside-the-box-the-implicit-chain-transformer-for-efficient-state-tracking
- **AI 摘要**: 文章提出了一种名为Implicit Chain Transformer的新方法，用于高效状态跟踪。该方法通过隐式链式推理，在保持性能的同时降低计算成本，适用于需要实时状态跟踪的应用场景。

### 35. Jais 2: A Blueprint for Sovereign AIDecember 09, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 09, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/jais2
- **AI 摘要**: Jais 2是G42与Cerebras合作开发的主权AI模型，基于Condor Galaxy 2超级计算机训练，采用双语数据优化阿拉伯语和英语能力，并提供API和本地部署选项，旨在为阿拉伯世界提供自主可控的AI基础设施。

### 36. Cerebras at NeurIPS 2025: Nine Papers From Pretraining to InferenceDecember 04, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 04, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/cerebras-at-neurips-2025-nine-papers-from-pretraining-to-inference
- **AI 摘要**: Cerebras公司将在NeurIPS 2025大会上展示九篇论文，涵盖从预训练到推理的多个AI技术领域，展示了其在AI研究和工程方面的最新进展。

### 37. Why speed wins: faster inference is about more than just quicker answers–it’s the new path to accuracyFebruary 19, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/speedandaccuracyblog
- **AI 摘要**: 文章探讨了AI推理速度的重要性，指出更快的推理不仅意味着更快的响应，更是实现更高准确性的新途径。通过加速推理过程，可以支持更复杂的算法和迭代优化，从而提升AI系统的整体性能。

### 38. This new model is smarter than Sonnet 4.5…and 20X faster?January 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7-migration-guide
- **AI 摘要**: 文章介绍了一款新模型，声称比Sonnet 4.5更智能且速度快20倍，可能涉及模型性能提升和推理加速技术。

### 39. GLM-4.7: Frontier intelligence at record speed — now available on CerebrasJanuary 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7
- **AI 摘要**: GLM-4.7模型在Cerebras平台上发布，以创纪录的速度提供前沿智能。该模型可能具备高性能和快速推理能力，适用于多种AI应用场景。

### 40. 2026: Fast Inference Finds its GrooveJanuary 06, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 06, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/2026Insights
- **AI 摘要**: 2026年，AI推理速度迎来重大突破，快速推理技术成为主流。文章探讨了推理优化、模型压缩及硬件加速等进展，强调其在实时应用中的关键作用，并展望了未来发展趋势。

### 41. Entity tracking emerges in sub-billion parameter language models and exceeds human performance in naturalistic narratives
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18083
- **AI 摘要**: 该研究评估了语言模型和人类在自然叙事中的实体追踪能力，发现亚十亿参数模型能进行实体追踪，且表现超过人类。
- **原始摘要**: arXiv:2608.18083v1 Announce Type: new Abstract: Understanding language requires tracking entities across discourse - i.e., knowing where things are and how they change, even when not explicitly stated...

### 42. Persona-Guided LLM Agents for Task-Oriented Dialogue
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18085
- **AI 摘要**: 本文研究大型语言模型在任务导向对话中能否表达个性特质且不影响任务完成，以及适应用户个性是否提升交互质量。通过多轮交互实验，探讨个性引导的LLM代理在目标导向对话中的表现。
- **原始摘要**: arXiv:2608.18085v1 Announce Type: new Abstract: Prior work has shown that large language models (LLMs) can express diverse personality traits in open-ended text generation. However, it remains unclear...

### 43. NE-BERT: A Multilingual Language Model for Nine Northeast Indian Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18094
- **AI 摘要**: NE-BERT是一个针对印度东北部九种低资源语言的多语言编码器模型，基于约830万句子训练，并包含印地语和英语作为锚定语言，以提升这些语言的自然语言处理能力。
- **原始摘要**: arXiv:2608.18094v1 Announce Type: new Abstract: Large pretrained language models have demonstrated remarkable capabilities across diverse languages, yet critically underrepresented low-resource langua...

### 44. Backdoor Learning in Language Models and Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18095
- **AI 摘要**: 本文探讨了语言模型和视觉语言模型中的后门攻击，分析了其安全威胁，并提出了检测与防御方法，旨在提升可信AI和高效多模态表示学习。
- **原始摘要**: arXiv:2608.18095v1 Announce Type: new Abstract: Recent advances in deep learning have significantly enhanced the capabilities of Natural Language Processing (NLP) and Vision-Language Models (VLMs). Ho...

### 45. Fractional Decay KV-Cache: Ownership-Aware Memory Management for Improved Inference Relevancy in Dialog Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18098
- **AI 摘要**: 针对对话系统中KV缓存管理粗放、无法适应话题演变的问题，提出FD-KVC算法，采用双通道评分机制（累积注意力与衰减）动态评估缓存重要性，实现细粒度缓存管理，提升推理相关性与效率。
- **原始摘要**: arXiv:2608.18098v1 Announce Type: new Abstract: Key-value (KV) caching is essential for efficient autoregressive inference in transformer based dialog systems, yet existing strategies treat all cached...

### 46. BERTilda: Explainable Topic Lifecycle Tracking with Split/Merge Detection via Similarity-and-Flow Temporal Graphs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18101
- **AI 摘要**: BERTilda是一个可解释的框架，用于追踪纵向文本流中的主题生命周期，包括主题的诞生、消亡以及分裂和合并等结构重组。它独立发现每个时间窗口的主题，并通过相似性和流时间图实现时间对应。
- **原始摘要**: arXiv:2608.18101v1 Announce Type: new Abstract: Longitudinal text streams exhibit topic birth and death, but also discrete structural reorganizations in which themes split into subtopics or merge into...

### 47. Alignment Is All You Need: Instruction-Free Training for General Audio-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18132
- **AI 摘要**: 本文探讨多模态大语言模型构建中，是否可省略跨模态对齐和监督微调等任务特定训练步骤。作者提出无指令训练方法，利用预训练LLM的推理和指令遵循能力，实现通用音频语言模型的高效构建。
- **原始摘要**: arXiv:2608.18132v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) are typically built through a multi-stage pipeline consisting of cross-modal alignment, supervised fine-tuning...

### 48. Language Models for Portuguese: A Systematic Mapping Study
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18138
- **AI 摘要**: 本文对葡萄牙语语言模型进行了系统性映射研究，概述了近年来学术界和工业界在开发葡萄牙语模型及数据资源方面的努力，并分析了该领域的研究现状与发展趋势。
- **原始摘要**: arXiv:2608.18138v1 Announce Type: new Abstract: In recent years, the rapid development of language models has transformed the field of Natural Language Processing through a wide range of applications....

### 49. WhiteMatter: All-to-All Cross-Layer Connections via KV Mixing
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18486
- **AI 摘要**: WhiteMatter提出一种新的Transformer架构，通过KV混合实现所有注意力层的全连接，使浅层消费层能利用深层表示，提升模型性能。
- **原始摘要**: arXiv:2608.18486v1 Announce Type: new Abstract: In a Transformer, each layer attends to past tokens only through KV produced at its own depth, despite the presence of deeper representations during aut...

### 50. DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18524
- **AI 摘要**: 本文提出DART-SD方法，通过钻石拓扑感知的检索与自蒸馏，解决多轮工具调用智能体中因全轨迹模仿导致的拓扑崩溃问题，提升LLM在复杂任务上的性能。
- **原始摘要**: arXiv:2608.18524v1 Announce Type: new Abstract: Equipping Large Language Models (LLMs) with multi-turn tool-calling capabilities is essential for building autonomous agents. However, progress is funda...

### 51. Shared Circuits for Shared Grammar: Tracing Subject-Verb Agreement Across Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18545
- **AI 摘要**: 多语言大模型常跨语言泛化，但内部机制何时共享尚不明确。本文研究现在时主谓一致这一跨语言差异显著的形态句法过程，探讨其共享是否随语法操作的显性实现而变化。
- **原始摘要**: arXiv:2608.18545v1 Announce Type: new Abstract: Multilingual large language models often generalize across languages, and prior work suggests that their internal mechanisms can overlap cross-lingually...

### 52. From Storage to Access: Verifiable Activation of Parametric Knowledge in LLMs via Explicit Priming and Implicit Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18581
- **AI 摘要**: 本文提出VAKE框架，通过显式提示和隐式推理分离知识提取与推理，实现LLM参数化知识的可验证激活，提升事实问答的可靠性。
- **原始摘要**: arXiv:2608.18581v1 Announce Type: new Abstract: Although Large Language Models (LLMs) encode rich factual knowledge in their parameters, reliably recalling and verifying such knowledge remains a key b...

### 53. X2Streaming-TTS: Causal Token-Level Text-to-Speech from Streaming Text with Speech-State Inheritance
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18661
- **AI 摘要**: X2Streaming-TTS是一种因果式流式文本转语音框架，能从异步到达的文本令牌生成语音，无需等待完整句子，实现真正的令牌级合成，同时保持感知连续性和有界上下文。
- **原始摘要**: arXiv:2608.18661v1 Announce Type: new Abstract: Streaming text-to-speech is essential for low-latency spoken dialogue systems, yet many systems wait for sentence-level text and are therefore only pseu...

### 54. MemFuse: Multi-Source Memory Fusion from Fragmented Observations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18704
- **AI 摘要**: MemFuse提出多源记忆融合方法，解决代理在跨应用、设备和用户场景中整合分散观察的问题，构建连贯情景记忆并保留来源信息。
- **原始摘要**: arXiv:2608.18704v1 Announce Type: new Abstract: Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on si...

### 55. Gradient Mirage: Trainable yet Label-Unidentifiable Gradients in Large Language Model Split Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18767
- **AI 摘要**: 本文提出Gradient Mirage防御方法，针对大语言模型拆分学习中的梯度匹配攻击，通过破坏梯度与标签目标的一致性，防止服务器从梯度中恢复私有标签，保护客户端数据隐私。
- **原始摘要**: arXiv:2608.18767v1 Announce Type: new Abstract: Gradient matching attacks (GMAs) in LLM split learning (SL) rely on a critical yet underexplored assumption: the gradient exposed at the split interface...

### 56. Readable, Faithful, Used: Three Dissociable Properties of Demographic Identity in a Language Model
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18768
- **AI 摘要**: 本文研究大型语言模型中的群体身份表征，通过表征相似性分析，发现其编码的群体意见结构在可读性、忠实性和使用性上存在分离，模型虽能编码但未必使用这些信息。
- **原始摘要**: arXiv:2608.18768v1 Announce Type: new Abstract: Large language models are widely used to simulate survey respondents, yet their answers are homogeneous and unfaithful to real inter-group differences....

### 57. Do Large Language Models Hallucinate Electric Fata Morganas?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18816
- **AI 摘要**: 本文探讨大语言模型幻觉的哲学意义，认为其不仅是工程缺陷，还关乎机器意识问题，并分析幻觉的已知成因。
- **原始摘要**: arXiv:2608.18816v1 Announce Type: new Abstract: AI hallucinations - that is, outputs which are made up, cannot be verified, or contradict the source material - are generally regarded as an engineering...

### 58. Identifying Implicit Premises for Logical Reconstruction of Argument Graphs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18821
- **AI 摘要**: 本文探讨从自然语言文本中逻辑重构论证图的挑战，重点解决省略式论证（隐含前提）的识别问题。文章结合自然语言处理方法和基于溯因推理的符号方法，提出生成隐含前提以完善逻辑表示的新方法。
- **原始摘要**: arXiv:2608.18821v1 Announce Type: new Abstract: The logical reconstruction of argument graphs from natural language text is challenging because of the prevalence of enthymemes (i.e., arguments with im...

### 59. Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18931
- **AI 摘要**: 测试时扩展通过增加推理计算提升模型输出，在数学和代码任务上效果显著，但现有研究多聚焦于验证简单的场景。文章首次对五种测试时扩展方法进行计算归一化比较，探讨其在实际应用中的瓶颈。
- **原始摘要**: arXiv:2608.18931v1 Announce Type: new Abstract: Test-time scaling (TTS) improves language model outputs by spending additional inference compute - generating multiple candidates, searching over partia...

### 60. MedUAG: Unified Understanding and Generation for Medical Multimodal Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18937
- **AI 摘要**: 本文提出MedUAG，一个面向医疗多模态大模型的统一理解与生成框架。针对现有统一范式在医疗领域缺乏训练评估基准和验证模型的问题，构建了MedUAGCorpus语料库，并开发了统一的医疗模型，为医疗UAG提供全面基础。
- **原始摘要**: arXiv:2608.18937v1 Announce Type: new Abstract: Recent Multimodal Large Language Models (MLLMs) are rapidly evolving into unified understanding and generation (UAG) frameworks. However, extending thes...

### 61. DeepWeaver: Bridging the Evidence Synthesis Gap in Open-Ended Question Answering
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18988
- **AI 摘要**: 本文提出DeepWeaver框架，旨在弥合开放域问答中的证据综合差距。该框架通过检索-生成流程，组织嘈杂碎片化证据，生成全面且引用规范的答案，解决直接生成中证据利用不足、引用错位及信息浅层化问题。
- **原始摘要**: arXiv:2608.18988v1 Announce Type: new Abstract: Retrieve-then-generate pipelines are commonly used to produce deep-research answers for open-ended questions, but retrieval alone is insufficient: LLMs...

### 62. SPADE: Self-Play in Adaptive Synthetic Executable Environments
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19197
- **AI 摘要**: SPADE是一个自对弈强化学习框架，让单个LLM同时扮演环境设计者和求解者，通过自适应生成可执行环境来持续提升语言智能体的能力，解决现有训练环境池目标分布固定的问题。
- **原始摘要**: arXiv:2608.19197v1 Announce Type: new Abstract: Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training environme...

### 63. From Inference to Adaptation: A Unified Optimal Transport View of Vision Language Model
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18339
- **AI 摘要**: 视觉语言模型在推理时对分布偏移敏感，现有测试时适应方法依赖原始嵌入相似度产生的噪声伪标签，在偏移下不可靠。本文提出统一最优传输视角，从推理到适应，以缓解噪声放大问题。
- **原始摘要**: arXiv:2608.18339v1 Announce Type: cross Abstract: Vision-language models (VLMs) have demonstrated remarkable zero-shot capabilities yet remain sensitive to real-world distribution shifts during infere...

### 64. When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18628
- **AI 摘要**: 本文探讨了视觉语言模型在安全对齐下，面对相同图像问题时，安全指令会导致模型拒绝回答本可正确回答的问题，质疑安全对齐是否抑制了感知基础。
- **原始摘要**: arXiv:2608.18628v1 Announce Type: cross Abstract: Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking...

### 65. MLREF: Efficient Module Reuse for Reward Design in Reinforcement Learning via Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18827
- **AI 摘要**: 本文提出模块级奖励进化框架（MLREF），利用大语言模型将奖励函数分解为可复用模块，避免整体重写，提升强化学习奖励设计的稳定性和效率。
- **原始摘要**: arXiv:2608.18827v1 Announce Type: cross Abstract: Reward function design remains a bottleneck in reinforcement learning. While large language models (LLMs) have enabled automated reward generation, ex...

### 66. Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18940
- **AI 摘要**: 本文针对单步逆合成反应的一对多特性，提出Top-K提示训练与推理范式，以捕捉多样且合理的反应预测。作者构建了含4560万条验证反应的超大规模数据集CREED-CCV-2+USPTO-XL，用于训练化学合理性感知的大语言模型。
- **原始摘要**: arXiv:2608.18940v1 Announce Type: cross Abstract: Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by...

### 67. What is Missing from AI Post-Training AI: An Empirical Analysis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19072
- **AI 摘要**: 本文探讨了LLM智能体端到端后训练的能力，区分了执行级能力（在选定策略内迭代）与策略级能力（根据实验证据修订高层判断），指出当前AI后训练中缺失的是策略级能力。
- **原始摘要**: arXiv:2608.19072v1 Announce Type: cross Abstract: Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downst...

### 68. ReWEIGH the Evidence: Calibrating Token-Level Ordinal Visual Evidence to Mitigate Hallucinations in Large Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19075
- **AI 摘要**: 大型视觉语言模型常产生幻觉，生成图像不支持的内容。本文提出一种方法，利用模型视觉令牌状态，通过输出头投影来校准令牌级序数视觉证据，以在解码时减轻幻觉。
- **原始摘要**: arXiv:2608.19075v1 Announce Type: cross Abstract: Large vision-language models (LVLMs) often hallucinate, generating content that the input image does not support. Preventing such content during decod...

### 69. Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19098
- **AI 摘要**: 本文研究了多教师在线策略蒸馏（M-OPD）中能力失衡的诊断与修复问题，提出Open-MOPD方法，以优化多教师能力整合的动态过程，并提供可复现的实践方案。
- **原始摘要**: arXiv:2608.19098v1 Announce Type: cross Abstract: Multi-teacher on-policy distillation (M-OPD) has emerged as a promising paradigm for consolidating domain-specialized reinforcement learning (RL) expe...

### 70. Future Policy Approximation for Offline Reinforcement Learning in LLM Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2509.19893
- **AI 摘要**: 本文探讨了离线强化学习在大型语言模型推理中的应用，提出未来策略近似方法以提升离线算法的性能，减少在线RL的不稳定性与计算开销。
- **原始摘要**: arXiv:2509.19893v3 Announce Type: replace Abstract: Reinforcement learning (RL) has emerged as a key driver of post-training for complex reasoning in large language models (LLMs), yet online RL introd...

### 71. Making Implicit Premises Explicit in Logical Understanding of Enthymemes
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.06114
- **AI 摘要**: 本文探讨了省略三段论（enthymemes）的逻辑理解问题，指出NLP方法无法解码其潜在逻辑，而逻辑方法依赖知识库。文章旨在使隐含前提显式化，以提升逻辑推理能力。
- **原始摘要**: arXiv:2603.06114v3 Announce Type: replace Abstract: Real-world arguments in text and dialogues are normally enthymemes (i.e. some of their premises and/or claims are implicit). Natural language proces...

### 72. KA2L: A Knowledge-Aware Active Learning Framework for LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.17566
- **AI 摘要**: KA2L框架通过知识感知主动学习，评估并提升大语言模型对特定领域知识的掌握程度，填补了该领域研究空白。
- **原始摘要**: arXiv:2603.17566v2 Announce Type: replace Abstract: Fine-tuning large language models (LLMs) with high-quality knowledge has been shown to enhance their performance effectively. However, there is a pa...

### 73. Self-Improvement of Large Language Models: A Technical Overview and Future Outlook
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.25681
- **AI 摘要**: 本文综述了大语言模型自我改进的技术现状与未来展望，探讨了在人类监督成本高、可扩展性受限的背景下，模型通过自主决策与执行实现自我提升的潜力与挑战。
- **原始摘要**: arXiv:2603.25681v2 Announce Type: replace Abstract: As large language models (LLMs) continue to advance, improving them solely through human supervision is becoming increasingly costly and limited in...

### 74. Phantom Transitions in Language Model Fine-Tuning: A Density-Matrix Analysis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.07559
- **AI 摘要**: 语言模型微调中，正确完成需超越近义竞争对手时，交叉熵损失单调下降但正确token排名未超越，导致静默失败。研究五种Transformer架构、十个上下文，分析密度矩阵。
- **原始摘要**: arXiv:2606.07559v3 Announce Type: replace Abstract: Language models fine-tuned where the correct completion must outrank a near-synonym competitor often fail silently. The cross-entropy loss falls mon...

### 75. First-Token Broadcasters: Mechanistic Origins of Language Identity and Distributed Robustness in Transformers
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.22361
- **AI 摘要**: 本文通过语言身份头消融（LIHA）方法，因果干预GPT-2的注意力头，识别出少量“首令牌广播头”控制多语言模型的语言选择，揭示语言身份机制及分布式鲁棒性。
- **原始摘要**: arXiv:2606.22361v2 Announce Type: replace Abstract: Why do multilingual language models sometimes generate in the wrong language, and why is this so hard to fix? We introduce Language Identity Head Ab...

### 76. Cross-Model Memory Transfer via Target-Side Reader Adaptation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17050
- **AI 摘要**: 本文提出了一种跨模型记忆迁移方法，通过目标端阅读器适配，将Engram式哈希记忆从源模型迁移至目标模型，以改善知识使用，兼具参数化与非参数化方法的优点。
- **原始摘要**: arXiv:2608.17050v2 Announce Type: replace Abstract: Methods for improving knowledge use in large language models typically fall into two regimes. Non-parametric retrieval offers flexible access to ext...

### 77. Demystifying Training-Time Augmentation for Data-Constrained Language Model Pretraining
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.16246
- **AI 摘要**: 本文探讨数据受限下语言模型预训练，提出训练时数据增强方法以应对多轮训练过拟合问题。
- **原始摘要**: arXiv:2606.16246v3 Announce Type: replace-cross Abstract: As AI labs approach a data ceiling where compute capacity outpaces the rate of new high-quality text generation, language model pretraining is...

### 78. Trace, Verify, and Correct: A Training-Free Framework for Spatial Reasoning in Multimodal LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.04759
- **AI 摘要**: 多模态大语言模型在空间推理中可能产生与输入图像不一致的中间判断，导致错误传播。现有方法依赖训练或额外空间信息，未考虑推理过程本身对图像的忠实性。本文提出一种无需训练的框架，通过追踪、验证和纠正来提升空间推理的准确性。
- **原始摘要**: arXiv:2608.04759v2 Announce Type: replace-cross Abstract: Although Multimodal Large Language Models (MLLMs) have made substantial progress, their spatial reasoning may still produce intermediate judgm...

### 79. Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12746
- **AI 摘要**: 多模态大语言模型中的对象幻觉源于语言先验和语料共现偏差。解码时干预效果有限，监督微调虽延长描述但仍有超40%提及不存在对象。本文提出双流跨锚点校正方法，并探讨对象级锚点的域限制。
- **原始摘要**: arXiv:2608.12746v3 Announce Type: replace-cross Abstract: Object hallucination in multimodal large language models arises when language priors and corpus co-occurrence bias outweigh the visual evidenc...

### 80. RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18682
- **AI 摘要**: 本文提出RTPO方法，通过理论分析识别多轮RL训练不稳定的根源，并采用反向策略优化稳定训练，防止性能随轮次增加而下降。
- **原始摘要**: arXiv:2608.18682v1 Announce Type: new Abstract: Training multi-turn agentic workflows with reinforcement learning (RL) enables large language models to perform complex reasoning, use external tools, a...

### 81. Bidirectional representational alignment between biological and artificial neural networks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18244
- **AI 摘要**: 本文研究生物与人工神经网络之间的表征对齐不对称性，即模型表征预测神经反应优于反向预测。作者假设训练中引导表征几何可系统性地改善双向对齐，并探索其机制与效果。
- **原始摘要**: arXiv:2608.18244v1 Announce Type: cross Abstract: Recent work has shown that representational alignment between biological and artificial neural networks is asymmetric: model representations predict n...

### 82. OptiModNet: A UNet-Transformer Hybrid with Grouped-Query and Channel Attention for Optic Disc and Cup Segmentation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18516
- **AI 摘要**: 本文提出OptiModNet，一种结合UNet与Transformer的混合模型，用于视盘和视杯分割。通过分组查询和通道注意力机制，在保持低计算需求的同时实现高精度分割，有助于青光眼的早期检测和大规模筛查。
- **原始摘要**: arXiv:2608.18516v1 Announce Type: cross Abstract: Precise segmentation of the optic disc and cup is critical for the early detection and diagnosis of glaucoma. However, achieving consistently high per...

### 83. A Critical Synthesis of Uncertainty Quantification and Foundation Models for Semantic Segmentation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18709
- **AI 摘要**: 本文综述了基础模型在语义分割中的不确定性量化方法，旨在解决其过度自信和领域偏移问题，提升安全关键应用的可靠性。
- **原始摘要**: arXiv:2608.18709v1 Announce Type: cross Abstract: Foundation models are increasingly breaking what seemed to be impossible not long ago by enabling unprecedented accuracy and cross-domain generalizati...

### 84. Forgetting, plasticity, and co-observation: a third facet of continual learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18803
- **AI 摘要**: 本文指出持续学习中的灾难性遗忘和可塑性丧失无法完全解释顺序训练与联合训练的性能差距，提出数据共同观察作为第三个影响因素，并探讨其作用机制。
- **原始摘要**: arXiv:2608.18803v1 Announce Type: cross Abstract: Efficient continual learning remains a fundamental challenge for deep neural networks. While catastrophic forgetting and loss of plasticity are widely...

### 85. Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.26643
- **AI 摘要**: 本文重新思考大语言模型智能体的自进化过程，提出将技能视为可训练状态，并采用约束探索-利用过程来缓解技能过拟合问题，以提升模型在真实环境中的泛化能力。
- **原始摘要**: arXiv:2607.26643v2 Announce Type: replace Abstract: Enabling large language model (LLM) agents to accumulate and reuse experience from past interactions remains a central challenge in real-world appli...

### 86. Hybrid LLM-Augmented Reinforcement Learning Agents for Complex Sequential Decision Tasks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.03502
- **AI 摘要**: 本文提出混合LLM增强的强化学习智能体，结合LLM的推理规划能力与RL的精确控制，用于解决复杂序列决策任务，弥补LLM在长时程交互中的不足。
- **原始摘要**: arXiv:2608.03502v2 Announce Type: replace Abstract: Large Language Models (LLMs) have recently shown strong capabilities in reasoning, planning, and tool-use, enabling new forms of autonomous agents....

### 87. FiLoRA: Focus-and-Ignore LoRA for Controllable Feature Reliance
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.02060
- **AI 摘要**: FiLoRA提出一种名为“聚焦与忽略”的低秩适配方法，通过显式调节模型对不同内部特征路径的依赖，实现对多模态基础模型预测的可控干预，以应对捷径和虚假相关行为。
- **原始摘要**: arXiv:2602.02060v2 Announce Type: replace-cross Abstract: Multimodal foundation models integrate heterogeneous signals across modalities, yet it remains unclear whether their predictions can be contro...

### 88. Structure-Informed Estimation for Pilot-Limited MIMO Channels via Tensor Decomposition
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.04083
- **AI 摘要**: 本文提出一种结构信息混合估计器，将导频受限的MIMO信道估计建模为低秩张量补全问题，利用张量分解从稀疏导频观测中恢复信道，解决了以往方法需完全观测张量的限制。
- **原始摘要**: arXiv:2602.04083v3 Announce Type: replace-cross Abstract: Accurate channel state information in wideband MIMO systems is constrained by pilot overhead, a challenge intensifying as bandwidths scale tow...

### 89. Hybrid ANN-SNN Pipeline with Local Plasticity
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.20151
- **AI 摘要**: 本文提出一种混合ANN-SNN流水线，利用预训练人工神经网络（如EfficientNet）的丰富嵌入，通过速率编码转换为脉冲序列，训练局部可塑性的SNN分类器，实现高性能脉冲神经网络。
- **原始摘要**: arXiv:2606.20151v2 Announce Type: replace-cross Abstract: This work proposes a hybrid ANN-SNN pipeline that effectively leverages the rich embeddings of pretrained artificial neural networks (ANNs) to...

### 90. Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17253
- **AI 摘要**: 本文提出Co-RL方法，通过多智能体强化学习中的多样群体协作，使无监督推理能力自然涌现，减少对人工标注奖励的依赖，提升推理性能。
- **原始摘要**: arXiv:2608.17253v2 Announce Type: replace-cross Abstract: Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its stronge...

### 91. Safe Domain Adaptation for Physics: Overcoming Nuisances, Label Shifts, and Simulation Priors
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18190
- **AI 摘要**: 本文探讨物理领域中的域适应问题，指出传统假设（域间仅存在干扰且目标量分布一致）在物理中不成立，因为模拟可能错误且目标量分布（如能谱、红移分布）常是测量本身。文章提出安全域适应方法以应对这些挑战。
- **原始摘要**: arXiv:2608.18190v1 Announce Type: new Abstract: Domain adaptation is widely used to make neural networks trained on simulations applicable to experimental data. Its premise is that the two domains dif...

### 92. The Road Taken: The Role of Optimizers at the Edge of Stability
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18415
- **AI 摘要**: 本文探讨深度学习优化器在稳定性边缘的现象，即损失函数Hessian特征值超过经典下降引理预测的不稳定阈值时仍保持稳定。研究发现多种一阶方法（如梯度下降）显著违反该预测，并分析了优化器在此边缘状态下的行为。
- **原始摘要**: arXiv:2608.18415v1 Announce Type: new Abstract: The edge of stability refers to a phenomenon in deep learning with gradient-based optimizers where the Hessian eigenvalues of the loss remain stable abo...

### 93. Infrared Universality of Collective Dynamics across Transformer and State-Space Architectures
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18592
- **AI 摘要**: 本文探讨不同神经架构是否发展出共同的集体动力学。研究发现Transformer语言模型具有近平坦、弱红外增强的时间尺度态密度，与近边缘长记忆动力学相关。文章进一步检验Mamba模型是否表现出类似组织，其选择性状态空间动力学提供了根本不同的微观机制。
- **原始摘要**: arXiv:2608.18592v1 Announce Type: new Abstract: Whether distinct neural architectures develop common collective dynamics remains an open question. Recent analysis of Transformer language models reveal...

### 94. To Go Far, Go Together: Diverse Preferences Induce a Curriculum for Reward Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18770
- **AI 摘要**: 本文从公平性角度出发，指出仅靠数据高效且准确的每用户奖励模型不足以实现AI与个体用户的对齐，提出多样化偏好可诱导奖励优化的课程学习，以更好地捕捉少数群体偏好。
- **原始摘要**: arXiv:2608.18770v1 Announce Type: new Abstract: Learning a reward model from human feedback and optimizing a policy against it is one approach to aligning AI systems with individual users. From a fair...

### 95. GraphK: Variable-Size Graph Generation with Efficient Edge Construction
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18777
- **AI 摘要**: GraphK是一种新型图生成框架，采用编码器-采样器-解码器结构，通过结构灵活性和计算效率解决现有模型在可扩展性、灵活性和结构建模方面的局限，避免自回归方法受词汇量限制的问题。
- **原始摘要**: arXiv:2608.18777v1 Announce Type: new Abstract: Graph generation models have advanced significantly with deep learning, yet they remain limited in scalability, flexibility, and ability to model underl...

### 96. A Unifying Relational Perspective on Expressive Lottery Tickets
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18819
- **AI 摘要**: 本文提出统一关系视角，研究稀疏性对关系图神经网络和时序图神经网络表达力的影响，将强表达彩票假设推广到多关系与时序域，证明存在保持WL表达力的稀疏网络。
- **原始摘要**: arXiv:2608.18819v1 Announce Type: new Abstract: Graph neural networks (GNNs) are widely used, but how parameter sparsity affects the expressivity of relational (RGNNs) and temporal (TGNNs) variants is...

### 97. GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18849
- **AI 摘要**: GEAR是一个两阶段蒸馏框架，将表格基础模型（TFM）蒸馏为轻量级MLP或树模型，以降低推理延迟和内存成本。第一阶段使用合成协变量进行生成扩展，第二阶段通过真实锚定进行校准，使模型能在CPU上高效部署。
- **原始摘要**: arXiv:2608.18849v1 Announce Type: new Abstract: Tabular foundation models (TFMs) achieve strong performance through in-context learning, but context-dependent inference imposes substantial latency and...

### 98. On the Slow Convergence to Trivial Solutions of Algorithms for Hard Optimization Problems
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18910
- **AI 摘要**: 本文研究NP难组合优化问题算法收敛缓慢的现象，通过随机实例平均情况分析，探讨在困难实例（如高约束密度）下算法性能的负面结果，揭示算法求解的固有挑战。
- **原始摘要**: arXiv:2608.18910v1 Announce Type: new Abstract: Hard combinatorial optimization problems, many of which are NP-hard, present fundamental algorithmic challenges. Average-case analysis on random instanc...

### 99. Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19151
- **AI 摘要**: 本文研究多变量霍克斯驱动随机微分方程的随机控制问题，针对非马尔可夫设置，提出有限维马尔可夫化程序和算法来近似多变量霍克斯过程，并利用机器学习算法求解。
- **原始摘要**: arXiv:2608.19151v1 Announce Type: new Abstract: We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting....

### 100. Self-supervised In-context Operator Learning for Stochastic Mean-Field Control
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18282
- **AI 摘要**: 本文提出将随机平均场控制（MFC）问题建模为算子学习问题，并开发了首个网格无关的深度学习方法，以解决现有方法需针对每个实例重新优化的问题。
- **原始摘要**: arXiv:2608.18282v1 Announce Type: cross Abstract: Stochastic mean-field control (MFC) provides a fundamental framework for coordinating large populations of interacting agents under uncertainty, with...

### 101. Coupled-cluster molecular properties across the main group that extrapolate beyond training size
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18346
- **AI 摘要**: 本文提出MEHnet-MG，一种等变神经网络，从廉价的B3LYP/def2-SVP计算预测有效单电子哈密顿量，从而推导多种分子性质，兼顾耦合簇精度与密度泛函效率，解决精度与成本矛盾。
- **原始摘要**: arXiv:2608.18346v1 Announce Type: cross Abstract: Coupled-cluster theory defines the accuracy standard for molecular electronic-structure properties but scales too steeply for routine application, whe...

### 102. Which Negatives Matter? Ask Your Text Encoder: Adaptive Similarity Margins for Dense-Caption Retrieval
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18521
- **AI 摘要**: 本文针对密集字幕检索中InfoNCE目标在强预训练初始化下过早饱和的问题，提出自适应相似度边距方法，通过利用文本编码器区分负样本，改进对比微调，提升检索性能。
- **原始摘要**: arXiv:2608.18521v1 Announce Type: cross Abstract: Dense-caption retrieval has recently been improved by introducing segmentation, edge maps, LLM-filtered captions, and cross-modal modules into contras...

### 103. Sharper Regret Bounds for Time-Varying Gaussian Process Bandits with Constant Exploration
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18863
- **AI 摘要**: 本文研究时变高斯过程老虎机中的贝叶斯优化，利用每轮局部置信事件，证明GP-UCB可在常数探索参数下获得期望遗憾界，优于现有方法。
- **原始摘要**: arXiv:2608.18863v1 Announce Type: cross Abstract: We study Bayesian optimization in a time-varying environment where the unknown reward function evolves according to a Gaussian process drift model. Ex...

### 104. Quantum Tensor Network Learning with DMRG
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18901
- **AI 摘要**: 张量网络是新兴的机器学习方法，受量子多体物理模拟启发。本文引入全局归一化条件使矩阵乘积态表示量子态，并研究两种局部优化方法。
- **原始摘要**: arXiv:2608.18901v1 Announce Type: cross Abstract: Tensor Networks are a relatively new machine learning approach. The architectures proposed initially are inspired by approaches from quantum many-body...

### 105. Breaking the weakest link to evade vision language models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18938
- **AI 摘要**: 本文研究了视觉语言模型（VLMs）在多模态对齐中的对抗性鲁棒性，重点探讨了逃避攻击的脆弱性，并提出了通过攻击最薄弱环节来规避VLMs的方法。
- **原始摘要**: arXiv:2608.18938v1 Announce Type: cross Abstract: Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual...

### 106. Robust Risk Under Evolving Uncertainty: A Wasserstein Counterpart of the Entropic Value-at-Risk
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19073
- **AI 摘要**: 本文提出一种在演化不确定性下的稳健风险度量方法，利用最优传输球替代相对熵球，以覆盖名义模型认为不可能但可能发生的灾难情景，从而在智能体学习环境时平衡谨慎与自信。
- **原始摘要**: arXiv:2608.19073v1 Announce Type: cross Abstract: An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a...

### 107. Contrasting Cost-Agnostic and Cost-Sensitive Losses under Limited Model Capacity via $\mathcal H$-consistency
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2502.19522
- **AI 摘要**: 本文探讨机器学习中任务无关损失（如交叉熵）与任务相关损失（如加权交叉熵）的争论，指出在无限数据和容量下两者等价，但实际有限容量下存在差异，通过H一致性分析对比两者性能。
- **原始摘要**: arXiv:2502.19522v2 Announce Type: replace Abstract: There is a prevalent debate in machine learning about whether practitioners should train models to optimize a task-agnostic objective (e.g., cross e...

### 108. Escaping Local Minima Provably in Non-convex Matrix Sensing: A Deterministic Framework via Simulated Lifting
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.05887
- **AI 摘要**: 本文提出一种确定性框架，通过模拟提升将非凸矩阵感知中的局部最小值转化为严格鞍点，从而证明梯度方法可逃离局部最优，为低秩矩阵感知提供理论保证。
- **原始摘要**: arXiv:2602.05887v3 Announce Type: replace Abstract: Low-rank matrix sensing is a fundamental yet challenging nonconvex problem whose optimization landscape typically contains numerous spurious local m...

### 109. Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.01499
- **AI 摘要**: 该研究比较了进化策略（ES）与GRPO在LLM后训练中的表现，发现ES在单任务准确率上相当或更优，但在参数空间解上存在差异，并探讨了持续学习场景下的性能。
- **原始摘要**: arXiv:2604.01499v3 Announce Type: replace Abstract: Evolution Strategies (ES) have emerged as a scalable gradient-free alternative to reinforcement learning based LLM fine-tuning, but it remains uncle...

### 110. LionMuon: Alternating Spectral and Sign Descent for Efficient Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.19811
- **AI 摘要**: LionMuon优化器结合Lion的廉价更新和Muon的强方向，交替使用谱矩阵符号和符号梯度下降，在保持效果的同时大幅降低平均每步成本，适用于大规模训练。
- **原始摘要**: arXiv:2605.19811v3 Announce Type: replace Abstract: In large-scale optimization, the cheapness and effectiveness of update steps are the most crucial factors for a successful optimizer. Sign-based opt...

### 111. GQ-FSL: Green Quantized Federated Split Learning Framework for Wireless Edge Networks
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.29659
- **AI 摘要**: 针对无线边缘部署深度神经网络受限于设备能源和资源的问题，提出绿色量化联邦分割学习框架，通过卸载工作负载至边缘服务器减轻设备计算负担，同时减少中间激活、梯度和子模型交换带来的能耗。
- **原始摘要**: arXiv:2607.29659v2 Announce Type: replace Abstract: Deploying state-of-the-art deep neural networks (DNNs) at the wireless edge is severely bottlenecked by the strict energy and resource constraints o...

### 112. A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.11917
- **AI 摘要**: 本文提出一种基于Forney因子图的多输出高斯过程回归方法，通过最近邻链将候选输入排序，以降低计算复杂度，并处理不同输出在不同输入观测的情况。
- **原始摘要**: arXiv:2608.11917v2 Announce Type: replace Abstract: Multi-output Gaussian process regression scales cubically in the number of observations times outputs, and dense kernel-matrix methods need bespoke...

### 113. Conformal Policy Control
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.02196
- **AI 摘要**: 本文提出了一种利用安全参考策略作为概率调节器的方法，以平衡智能体探索与安全约束，防止在高风险环境中因行为变化过大而违反安全规则。
- **原始摘要**: arXiv:2603.02196v4 Announce Type: replace-cross Abstract: An agent must try new behaviors to explore and improve. In high-stakes environments, an agent that violates safety constraints may cause harm...

### 114. SHANG++: Robust Stochastic Acceleration under Multiplicative Noise
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.09355
- **AI 摘要**: 本文针对乘性噪声下Nesterov加速的敏感性，提出两种加速随机梯度下降方法。通过离散化Hessian驱动的Nesterov加速梯度流，得到SHANG及其改进版本，在乘性噪声条件下提升稳定性。
- **原始摘要**: arXiv:2603.09355v2 Announce Type: replace-cross Abstract: Under the multiplicative noise scaling (MNS) condition, original Nesterov acceleration is provably sensitive to noise and may diverge when gra...

### 115. Pre-Training for Simulation-Based Science: A Study on Jet Foundation Model Training Objectives
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.14870
- **AI 摘要**: 本文系统比较了基于模拟的科学领域基础模型的预训练目标，利用大量带标签的模拟数据，探索自监督掩码预训练与监督预训练的效果，为科学基础模型预训练提供新思路。
- **原始摘要**: arXiv:2606.14870v2 Announce Type: replace-cross Abstract: Foundation models (FMs) trained on large datasets and fine-tuned on downstream tasks have emerged as a powerful paradigm in AI for science. In...

### 116. Untrainable elements determine what physical learning remembers
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.00097
- **AI 摘要**: 物理学习规则如平衡传播、耦合学习等通过局部测量训练电阻网络，其学习功能取决于训练落在解流形上的位置。电路在缩放电导下的不变性与规则对质量K的守恒决定了学习结果，两者尚未被分离研究。
- **原始摘要**: arXiv:2608.00097v2 Announce Type: replace-cross Abstract: Physical learning rules such as equilibrium propagation (EP), coupled learning (CL), and adjoint coupled learning (AL) train resistive network...

### 117. Counterfactual Behavior Cloning: Offline Imitation Learning from Imperfect Human Demonstrations
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2025年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2505.10760
- **AI 摘要**: 本文提出反事实行为克隆方法，用于从不完美的人类演示中学习离线模仿。针对人类演示中的噪声和次优行为，该方法通过反事实推理改进学习效果，克服传统行为匹配的局限。
- **原始摘要**: arXiv:2505.10760v2 Announce Type: replace Abstract: Learning from humans is challenging because people are imperfect teachers. When everyday humans show the robot a new task they want it to perform, h...

### 118. OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17633
- **AI 摘要**: 本文提出OVIP-SG方法，解决开放词汇感知在3D场景图中导致实例碎片化和合并问题，提升小物体映射与检索的实例一致性。
- **原始摘要**: arXiv:2608.17633v2 Announce Type: replace Abstract: Integrating open-vocabulary perception into object-level 3D scene graphs is a double-edged sword. While vision-language detectors recover long-tail...

### 119. A Fault-Tolerant Spike-Time Interface for Approximate Agreement in Distributed Neuromorphic Systems
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18151
- **AI 摘要**: 本文研究分布式神经形态系统中，当通信仅携带标记脉冲时间且最多f个发送者标签可能拜占庭时，各处理瓦片如何减少共享控制参数（如阈值参考）的分歧。
- **原始摘要**: arXiv:2608.18151v1 Announce Type: new Abstract: Large neuromorphic systems contain many processing tiles that may replicate a shared control parameter such as a threshold reference. If these copies di...

### 120. Aug 12, 2026Introducing Grok 4.6
- **来源**: xAI Blog (TIER1)
- **发布日期**: Aug 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://x.ai/news/grok-4-6
- **AI 摘要**: 文章介绍了Grok 4.6的发布，但摘要内容缺失，无法提供具体信息。

### 121. Qwen-Image-Edit: Image Editing with Higher Quality and Efficiency
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image-edit/
- **AI 摘要**: Qwen团队推出Qwen-Image-Edit，基于20B参数的Qwen-Image模型，扩展其文本渲染能力至图像编辑，支持精确文本编辑。该模型同时将输入图像送入Qwen2.5-VL进行视觉语义控制和VAE编码器进行视觉外观控制，实现高质量、高效的图像编辑。
- **原始摘要**: QWEN CHAT GITHUB HUGGING FACE MODELSCOPE DISCORD We are excited to introduce Qwen-Image-Edit, the image editing version of Qwen-Image. Built upon our 20B Qwen-Image model, Qwen-Image-Edit successfully...

### 122. Qwen-Image: Crafting with Native Text Rendering
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image/
- **AI 摘要**: Qwen团队发布Qwen-Image，一个20B参数的MMDiT图像基础模型，在复杂文本渲染和精确图像编辑方面取得显著进展。该模型支持多行布局、段落级语义和细粒度细节，并支持字母文字。用户可通过Qwen Chat体验。
- **原始摘要**: GITHUB HUGGING FACE MODELSCOPE DEMO DISCORD We are thrilled to release Qwen-Image, a 20B MMDiT image foundation model that achieves significant advances in complex text rendering and precise image edi...

### 123. GSPO: Towards Scalable Reinforcement Learning for Language Models
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/gspo/
- **AI 摘要**: 强化学习是扩展语言模型能力的关键，但现有算法如GRPO在长训练中不稳定，导致模型崩溃。本文提出GSPO算法，旨在实现可扩展的强化学习，提升训练稳定性与性能。
- **原始摘要**: PAPER DISCORD Introduction Reinforcement Learning (RL) has emerged as a pivotal paradigm for scaling language models and enhancing their deep reasoning and problem-solving capabilities. To scale RL, t...

### 124. New Kimi K2 Models & Updated Pricing
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/Kimi_API_Newsletter
- **AI 摘要**: 文章介绍了新的Kimi K2模型及其更新的定价策略，可能涉及模型性能提升和价格调整，旨在为用户提供更高效、经济的AI服务。

### 125. Kimi K2: Open Agentic Intelligence
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/k2-report
- **AI 摘要**: Kimi K2是Moonshot AI推出的新一代开源模型，专注于智能体能力，支持工具调用、代码生成和复杂任务执行，旨在推动AI代理的广泛应用。

### 126. VLAs that Train Fast, Run Fast, and Generalize Better
- **来源**: Physical Intelligence (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.physicalintelligence.company/research/knowledge_insulation
- **AI 摘要**: 该文章探讨了视觉语言模型（VLAs）在训练速度、运行效率和泛化能力方面的改进，提出了一种新的方法或架构，旨在实现快速训练、高效推理和更好的泛化性能。

### 127. VLAs with Long and Short-Term Memory
- **来源**: Physical Intelligence (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.physicalintelligence.company/research/memory
- **AI 摘要**: 该文章探讨了具有长期和短期记忆的VLAs（视觉语言动作模型），旨在提升AI在复杂任务中的表现。通过结合长期记忆的稳定性和短期记忆的适应性，模型能够更有效地处理动态环境，增强决策和行动能力。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
