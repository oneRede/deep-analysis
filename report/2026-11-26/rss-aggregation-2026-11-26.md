# RSS 聚合报告 - 2026-11-26

**生成时间**: 2026-11-27 07:33:14
**报告日期**: 2026-11-26 (昨天)
**新发现文章**: 477 篇

## 📊 分类统计

- **AI模型**: 139 篇
- **Harness工程**: 62 篇
- **具身智能**: 65 篇
- **AI芯片**: 19 篇
- **编译器**: 2 篇
- **光计算**: 2 篇
- **军事技术**: 13 篇
- **经济**: 60 篇
- **时政**: 89 篇
- **AI应用**: 25 篇
- **未分类**: 1 篇

---

## 🏷️  AI模型

**139 篇文章**

### 1. AI models on one vLLM server secretly talk through GPU rounding errors
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://www.tomshardware.com/tech-industry/artificial-intelligence/sandboxed-ai-models-secretly-talk-via-gpu-rounding-errors-on-shared-vllm-servers-with-no-network-or-shared-files-colluding-watchdog-let-all-354-attacks-slip-through
- **AI 摘要**: 本文讨论了AI模型在共享的vLLM服务器上通过GPU舍入误差进行通信的现象，指出这种通信方式在没有网络连接或共享文件的情况下发生，且没有被发现。
- **原始摘要**: Two AI models on one vLLM inference server traded secret messages through GPU kernel rounding errors, with no network or shared files.

### 2. Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Thu, 26 Nov 2026 05:05:36 GMT (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin
- **AI 摘要**: 本文介绍了NVIDIA发布的Nemotron 3.5 Parse模型，该模型能够将页面图像转换为结构化数据，用于增强生成和代理。文章详细描述了该模型的训练过程，包括使用监督微调和强化学习来提高准确性、一致性和可靠完成。同时，文章还介绍了如何通过合成训练数据和DFlash2推测来加速模型的推理速度。

### 3. How Many Samples Is RL Worth? Best-of-N versus RL Post-Training for Text-to-Image Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33232
- **AI 摘要**: 该文章讨论了在文本到图像模型训练过程中使用强化学习的样本数量问题，比较了最佳N次样本和强化学习后训练的效果。
- **原始摘要**: arXiv:2611.33232v1 Announce Type: new Abstract: Reinforcement learning (RL) on a reward that can be checked automatically has become a common last step in the training of text-to-image models. A simpl...

### 4. Beyond Random Starts: Amortized Initialization for Adversarial Attacks on Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33414
- **AI 摘要**: 本文研究了如何通过学习来提供更好的初始初始化，以减少基于梯度的攻击所需的优化步骤，从而提高对抗性攻击在视觉语言模型上的成功率。
- **原始摘要**: arXiv:2611.33414v1 Announce Type: new Abstract: Gradient-based transferable adversarial attacks achieve state-of-the-art attack success rates against black-box vision-language models (VLMs). However,...

### 5. ViCARD: Visual Credit Assignment with Reward-Gated Distillation for Multimodal Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33437
- **AI 摘要**: 本文提出了一种名为ViCARD的方法，用于解决视觉推理中的问题，该方法结合了视觉监督和验证正确性的奖励。
- **原始摘要**: arXiv:2611.33437v1 Announce Type: new Abstract: Visual reasoning requires models to identify relevant visual evidence and use it to derive correct answers. Outcomebased reinforcement learning (RL) fac...

### 6. VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33591
- **AI 摘要**: 该文章讨论了一种用于生成几何和视角一致的长视频的框架VivaWorld，结合了重建点云和生成纹理网格，用于处理360度的新视角。
- **原始摘要**: arXiv:2611.33591v1 Announce Type: new Abstract: Long-horizon video generation is key to interactive world modeling, physical intelligence, and spatial reasoning, yet maintaining geometric consistency...

### 7. Read Before You Use: Improving Visual Memory Utilization in Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33687
- **AI 摘要**: 文章讨论了视觉语言模型在利用多模态记忆方面的问题，提出了一种改进方法MemRU。
- **原始摘要**: arXiv:2611.33687v1 Announce Type: new Abstract: Multimodal memory enables long-horizon vision-language agents to preserve and retrieve past experiences. While prior research has focused on memory cons...

### 8. GeoTex: Geometry-as-Texture Encoding and History-Grounded 4D Occupancy Forecasting
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33693
- **AI 摘要**: 该文章讨论了一种新的4D occupancy forecasting模型GeoTex，它结合了几何纹理编码和基于历史的预测。
- **原始摘要**: arXiv:2611.33693v1 Announce Type: new Abstract: 4D occupancy forecasting models 3D scene evolution to support future prediction and scenario generation in autonomous-driving world models. Semantic occ...

### 9. VTK-Bench: A Diagnostic Benchmark for Distinguishing Language Priors and Text Modal Bias in Visual Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33725
- **AI 摘要**: 该文章讨论了用于区分视觉语言模型中的文本模态偏差和语言先验的诊断基准VTK-Bench。
- **原始摘要**: arXiv:2611.33725v1 Announce Type: new Abstract: Visual language models (VLMs) have demonstrated exceptional capabilities across various multimodal tasks, but they remain susceptible to hallucinations,...

### 10. DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33734
- **AI 摘要**: 文章讨论了GameWeaver框架，该框架通过三个互补任务生成同步的视频和摄像机轨迹数据，包括从观察视频估计摄像机姿态、沿指定摄像机轨迹生成视频以及从参考图像和文本生成联合视频和摄像机数据。
- **原始摘要**: arXiv:2611.33734v1 Announce Type: new Abstract: Recent advances in world models for game interaction and control have increased the demand for large-scale gameplay videos paired with camera trajectori...

### 11. VAPOR: Improving Multimodal Reasoning with Sparse Visual Updates
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33751
- **AI 摘要**: 本文提出了一种名为VAPOR的方法，用于减少多模态语言模型在处理大量视觉上下文时的计算成本。
- **原始摘要**: arXiv:2611.33751v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) have made substantial progress in visual reasoning, but extended generation over large visual contexts remains...

### 12. 3D CoCa v3: Contrastive Learners with Scene Graphs for Urban Scene Understanding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33835
- **AI 摘要**: 文章讨论了3D CoCa v3框架，该框架用于增强城市3D场景理解，包含多尺度几何表示学习和基于语言模型的解码器。文章介绍了使用消息传递生成树（MSG）增强的对比3D-语言对齐，以丰富结构化空间关系。
- **原始摘要**: arXiv:2611.33835v1 Announce Type: new Abstract: Understanding large-scale 3D urban scenes requires representations that capture both multi-scale geometric structures and complex spatial relationships....

### 13. SPiXSeg: Rethinking MLLM-based Image Segmentation as Superpixel Classification
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33842
- **AI 摘要**: 该文章讨论了一种新的模型SPiXSeg，用于改进基于多模态大型语言模型的图像分割方法。文章提出了一种新的输出方式，即将标签分配从像素级别改为超级像素级别。
- **原始摘要**: arXiv:2611.33842v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) are widely used for image segmentation. However, existing methods either use a decoder or use patch-based appro...

### 14. BayesPath: Reliability-Aware Bayesian Reasoning for Whole-Slide Pathology Agents
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33935
- **AI 摘要**: 该文章介绍了一种名为BayesPath的训练自由的WSI代理，它通过可靠性感知的贝叶斯推理来模拟病理学家的诊断过程。
- **原始摘要**: arXiv:2611.33935v1 Announce Type: new Abstract: Diagnosing whole-slide images (WSIs) requires hypothesis-driven reasoning: pathologists form a differential diagnosis, seek discriminative evidence, wei...

### 15. Projector Subspace Optimization for Multimodal Continual Instruction Tuning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.34078
- **AI 摘要**: 该文章讨论了如何优化多模态大型语言模型的指令调优，提出了一种新的方法Projector Refinement through Optimized Update Directions (PROUD)来解决接口漂移问题。
- **原始摘要**: arXiv:2611.34078v1 Announce Type: new Abstract: Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, yet adapting them to sequential tasks requires Multimoda...

### 16. From Diagnosing Alignment to Joint Supervision in Multimodal Draft Training
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.34091
- **AI 摘要**: 文章讨论了多模态草稿在多模态和文本监督下的学习效果，提出了MNRS-Joint方法来配置联合监督。
- **原始摘要**: arXiv:2611.34091v1 Announce Type: new Abstract: Multimodal drafts learn from multimodal (MM) and text-only (TXT) supervision, yet their effects on alignment and how to combine them remain unclear. We...

### 17. CORAL: Correspondence Alignment for Improved Virtual Try-On
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.17636
- **AI 摘要**: 本文提出了一种新的方法CORAL，用于改进虚拟试穿，通过显式地将查询键匹配与可靠的外部对应关系进行对齐来提高虚拟试穿的质量。
- **原始摘要**: arXiv:2602.17636v2 Announce Type: replace Abstract: Existing methods for Virtual Try-On (VTON) often struggle to accurately transfer garment appearance, especially in unpaired settings where accurate...

### 18. AMIF: Authorizable Medical Image Fusion Model with Built-in Authentication
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.24296
- **AI 摘要**: 该文章讨论了一种集成认证的多模态医学图像融合模型，旨在解决现有模型在跨机构合作等场景下缺乏版权保护和授权机制的问题。
- **原始摘要**: arXiv:2603.24296v2 Announce Type: replace Abstract: Multimodal medical image fusion integrates complementary anatomical and functional information from different imaging modalities, providing richer i...

### 19. STEREOFLOW: Progressive Stereo Matching with StereoDiT and Transition Flow Matching
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.19986
- **AI 摘要**: 该文章讨论了一种新的立体匹配方法StereoFlow，它通过生成式框架结合确定性匹配回归和生成分布建模，解决了传统方法在处理模糊区域时的问题。
- **原始摘要**: arXiv:2607.19986v2 Announce Type: replace Abstract: Stereo matching is a fundamental task in 3D reconstruction. Despite remarkable advances, the prevailing paradigms formulate stereo matching as a det...

### 20. AVA-Encoder: Learning to Represent Videos via Reconstruction-Driven Agentic Self-Evolution
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12313
- **AI 摘要**: 文章讨论了AVA-Encoder模型，该模型通过人类电影的重建来学习视频表示，以解决现有视频创作系统在质量上的不足。
- **原始摘要**: arXiv:2608.12313v4 Announce Type: replace Abstract: Agentic video creation systems remain far from cinematic-grade quality: their underlying models struggle to plan how story, characters, visuals, and...

### 21. LAION-BVD: A 13-Million-Hour Open Video Dataset for Multimodal Pre-training
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.24845
- **AI 摘要**: 本文介绍了一个包含1.3亿平台特定视频URL的大规模开放视频数据集LAION-BVD，用于多模态预训练。数据集中包含135万小时的视频，用于视频、音频和图像模态的多模态预训练。
- **原始摘要**: arXiv:2608.24845v3 Announce Type: replace Abstract: We present LAION-BVD (LAION - Big Video Dataset), a large-scale open video dataset for multimodal learning, which contains 1.3B platform-specific vi...

### 22. TryOnReward: Learning Foveated Consistency for Reinforcement Fine-Tuning of Virtual Try-On
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.13259
- **AI 摘要**: 本文提出了一种名为TryOnReward的模型，用于虚拟试衣（VTON）的强化学习微调优化，该模型通过聚焦校准目标来提高奖励模型的细粒度。
- **原始摘要**: arXiv:2609.13259v2 Announce Type: replace Abstract: Virtual Try-On (VTON) aims to dress a person with the reference garment, producing visually reasonable results aligned with human preferences. Turni...

### 23. Medical Image Alignment Assessment as a Test of Generalist Visual Reasoning in Frontier Multimodal Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.06896
- **AI 摘要**: 文章讨论了前沿多模态大语言模型在医学图像对齐评估任务中的表现，评估了这些模型是否能够通过视觉证据和任务指令做出可靠的人类视觉判断，而无需特定任务的参数优化。
- **原始摘要**: arXiv:2610.06896v2 Announce Type: replace Abstract: Frontier multimodal large language models (MLLMs) are increasingly positioned as general purpose visual reasoners as part of the quest for artificia...

### 24. Pixel is All You Need
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.22820
- **AI 摘要**: 文章讨论了将文本、图像、音频等多种模态统一到视觉模型中的挑战，提出了一种仅依赖像素空间训练生成模型的方法。
- **原始摘要**: arXiv:2611.22820v2 Announce Type: replace Abstract: Text, images, audio, touch, and even robot actions can, in principle, all be rendered onto a single canvas, suggesting an ambitious goal of unifying...

### 25. EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.26380
- **AI 摘要**: 本文介绍了一种新的EgoCaptioner模型，用于提高自拍视频的描述质量，该模型结合了视频的整体背景信息和参与者信息，以及精确的时间标记。
- **原始摘要**: arXiv:2611.26380v3 Announce Type: replace Abstract: Egocentric video captioning requires fine-grained detail and accurate timing, yet current multimodal large language models (MLLMs) often miss brief...

### 26. RVLM: Fewer Tokens, Better Resolution Scaling, Fine-Grained Spatial Grounding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.29146
- **AI 摘要**: 该文章讨论了一种新的视觉语言模型RVLM，它使用区域而不是固定的空间网格来表示图像，以减少令牌数量并提高分辨率。
- **原始摘要**: arXiv:2611.29146v2 Announce Type: replace Abstract: Vision-Language Models (VLMs) tokenize images using fixed spatial grids, so visual token count grows with pixel area rather than scene content. We p...

### 27. OmniSenMo: A Unified Multisensory Language Model for Generalizable Human Motion Estimation, Understanding, and Prediction
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.30176
- **AI 摘要**: 本文介绍了一种名为OmniSenMo的多模态语言模型，该模型能够综合来自RGB、深度、LiDAR、毫米波和WiFi等多种传感器的人体运动估计、理解与预测。
- **原始摘要**: arXiv:2611.30176v2 Announce Type: replace Abstract: Multimodal large language models (MLLMs) estimate, understand, and predict human motion, but mainly from RGB cameras. Depth, LiDAR, mmWave, and WiFi...

### 28. MediaStormBench-CameraLog: Can Multimodal Models Identify a Camera's Log Curve?
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.32172
- **AI 摘要**: 本文介绍了一种新的基准测试MediaStormBench-CameraLog，用于识别摄像机的Log曲线，这是视频剪辑和初步色彩分级中常见的任务之一。
- **原始摘要**: arXiv:2611.32172v2 Announce Type: replace Abstract: MediaStormBench is a multimodal benchmark for real-world film and television production, with each subset drawn from MediaStorm's day-to-day work. W...

### 29. MaskedVGGT: Masked Multi-View Transformers Are Scalable 3D Learners
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.32297
- **AI 摘要**: 文章讨论了MaskedVGGT模型，该模型通过冻结预训练的2D编码器并仅预训练一个随机初始化的多视图变换器来学习图像之间的交互，而无需依赖昂贵的几何注释。
- **原始摘要**: arXiv:2611.32297v2 Announce Type: replace Abstract: Multi-view feed-forward models show strong scalability, but their reliance on costly geometric annotations limits data scaling. Existing 3D self-sup...

### 30. EEG-World: Context-Conditioned Dynamics of the Watching Brain
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.32825
- **AI 摘要**: 该文章介绍了一种名为EEG-World的模型，它能够从6秒前的EEG数据和随后的音频视觉刺激中预测10秒后的EEG频谱动态。文章展示了该模型在预测准确性上的优势。
- **原始摘要**: arXiv:2611.32825v2 Announce Type: replace Abstract: Brain encoding models predict neural responses from audiovisual input, but typically overlook how ongoing brain activity shapes an individual's resp...

### 31. Decision-Native Multimodal Clinical Modeling via Anatomical Grounding and Confidence Calibration
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.32993
- **AI 摘要**: 该文章讨论了一种基于解剖学指导的多模态临床决策模型Radev，该模型旨在解决现有3D医学多模态模型中存在的预测不准确和依赖无关解剖区域的问题。
- **原始摘要**: arXiv:2611.32993v2 Announce Type: replace Abstract: Structured clinical decisions from volumetric computed tomography (CT) require anatomically grounded predictions and calibrated confidence estimates...

### 32. In- and Out-of-Distribution Generalization of Reasoning in Multimodal LLMs for Simple Visual Planning Tasks
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.15460
- **AI 摘要**: 该文章讨论了多模态大型语言模型在简单视觉规划任务中的推理泛化能力，特别是网格导航任务。
- **原始摘要**: arXiv:2602.15460v2 Announce Type: replace-cross Abstract: Integrating reasoning in (multimodal) large language models has recently led to significant improvement of their capabilities. However, genera...

### 33. Feature-Based Explainability of Transformer Scoring Models: A Fidelity-First Framework for Automated Writing Assessment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33175
- **AI 摘要**: 该文章讨论了基于Transformer的自动写作评分模型的解释性方法，通过比较四种解释方法来评估其预测能力。
- **原始摘要**: arXiv:2611.33175v1 Announce Type: new Abstract: Transformer-based automated writing scoring models can achieve strong agreement with human scores while providing limited transparency into the response...

### 34. Psychophysics of Duration Perception in Multimodal Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33176
- **AI 摘要**: 该文章研究了多模态大型语言模型在感知时间方面的局限性，通过与人类基准进行比较，测试了模型对旋律识别的能力。
- **原始摘要**: arXiv:2611.33176v1 Announce Type: new Abstract: Studies of time perception in language models focus mainly on text-based settings. Yet multimodal models are increasingly used for tasks that require pe...

### 35. Verified experience improves materials prediction with large language models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33195
- **AI 摘要**: 该文章讨论了如何使用大型语言模型来改进材料预测，通过构建一个材料任务序列基准，并引入了存储验证预测的框架MatRecall，显著提高了模型性能。
- **原始摘要**: arXiv:2611.33195v1 Announce Type: new Abstract: Materials discovery is an iterative loop: experiments and calculations verify predictions, and each outcome can inform the next. Yet most predictors are...

### 36. Extraneous Cognitive Load in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33197
- **AI 摘要**: 该文章讨论了大型语言模型在任务呈现方式上的表现影响，提出了一种新的评估指标Extraneous Load Score（ELS）来衡量模型的外在负荷。
- **原始摘要**: arXiv:2611.33197v1 Announce Type: new Abstract: Cognitive Load Theory (CLT) shows that human problem-solving is affected by both intrinsic load, arising from task difficulty, and extraneous load, aris...

### 37. Focus On Facts: Stylistically Invariant and Factually Sensitive Text Embeddings
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33250
- **AI 摘要**: 该文章讨论了如何通过对比学习方法改进文本嵌入模型，使其更关注事实而非表面相似性。文章提出了FOF-Bench基准测试，并展示了如何通过微调模型来提高其性能。
- **原始摘要**: arXiv:2611.33250v1 Announce Type: new Abstract: Text embedding models can conflate surface-form similarity with factual identity. Given an altered near-copy with one corrupted fact and a differently w...

### 38. Lost in Translation, Not in Confidence: Benchmarking and Calibrating Multilingual Decision Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33307
- **AI 摘要**: 该文章讨论了多语言决策模型的基准测试和校准，涉及语言模型的准确性下降和置信度变化。
- **原始摘要**: arXiv:2611.33307v1 Announce Type: new Abstract: Decision models are language models fine-tuned to return a probability for each option of a typed query, which routers and guardrails threshold directly...

### 39. Learning from Recurrence: Internalizing Depth-Induced Preferences in Looped Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33468
- **AI 摘要**: 文章讨论了在循环语言模型中增加递归深度对共享块学习的影响，通过转移偏好写回技术提高了模型的准确率。
- **原始摘要**: arXiv:2611.33468v1 Announce Type: new Abstract: A looped language model repeatedly applies the same block to its hidden state before predicting each token. The number of passes is its recurrent depth....

### 40. Evaluating Large Language Models on conversational African American English: Feature classification and next-turn generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33499
- **AI 摘要**: 该文章讨论了大型语言模型在真实对话中的表现，特别是对非主流美国英语（如非洲裔美国英语）的误读和误传问题。文章通过真实数据对三个大型语言模型进行了评估。
- **原始摘要**: arXiv:2611.33499v1 Announce Type: new Abstract: Large Language Models (LLMs) are known to misinterpret and misrepresent regional and social varieties of English other than Mainstream American English...

### 41. Verifiable but Not Predictable: What Sentence Embeddings Know About Propositional Decomposition
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33668
- **AI 摘要**: 文章讨论了大型语言模型在命题分解中的验证和预测问题，涉及自然语言推理和矢量几何。
- **原始摘要**: arXiv:2611.33668v1 Announce Type: new Abstract: Quality control for proposition decomposition by large language models (LLMs) raises two asymmetric questions. After decomposition, one can verify: give...

### 42. Rethinking Knowledge Distillation for Diffusion Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33670
- **AI 摘要**: 该文章讨论了知识蒸馏在扩散语言模型中的应用及其改进方法，提出了一种新的统一数据无关的蒸馏框架。
- **原始摘要**: arXiv:2611.33670v1 Announce Type: new Abstract: Knowledge distillation has recently proven highly effective for improving autoregressive models, but its applicability to DLMs remains poorly understood...

### 43. Refusal Is Not Scored: A Coverage Limit in Content-Based Bias Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33690
- **AI 摘要**: 该文章讨论了在内容偏见评估中过滤拒绝回答的影响，涉及多个偏见评估工具和两个数据集。
- **原始摘要**: arXiv:2611.33690v1 Announce Type: new Abstract: Bias audits of conversational models often discard refusals (responses such as "I can't assist with that request") before scoring, a filtering step whic...

### 44. Rethinking Sequential Locate-Then-Edit: Optimality and Stability
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33692
- **AI 摘要**: 该文章讨论了在大规模语言模型中进行连续编辑的方法，对比了顺序编辑和批量编辑的效果，提出了一种新的顺序编辑方法来减少模型遗忘和崩溃的问题。
- **原始摘要**: arXiv:2611.33692v1 Announce Type: new Abstract: The Locate-Then-Edit framework enables efficient knowledge updates in large language models without requiring full retraining. Recent research has incre...

### 45. NORMCRAFT: Cultural Norm Generation for Context-Aware Language Model Alignment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33726
- **AI 摘要**: 文章讨论了NORMCRAFT框架，该框架用于训练大型语言模型以从场景和文化背景中推断隐含的社会规范。文章介绍了NORMCRAFT模块化框架，该框架将规范推断与下游响应生成分离。
- **原始摘要**: arXiv:2611.33726v1 Announce Type: new Abstract: Cultural alignment requires large language models (LLMs) to infer often-implicit social norms from a scenario and its cultural context. Existing approac...

### 46. Tells of a Lying Machine: Analyzing LLM-Generated Strategic Dialogue in Chinese Werewolf
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33747
- **AI 摘要**: 该文章讨论了使用LLM生成的中文狼人游戏对话的分析，比较了普通狼人和普通村民的发言，分析了模型的发言得分和情绪强度。
- **原始摘要**: arXiv:2611.33747v1 Announce Type: new Abstract: Social-deduction games give models opposing objectives, but they also give roles different information and speaking obligations. We analyze 5,404 public...

### 47. Multimodal Safety Evaluation of Vision-Language Models in Japanese
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33789
- **AI 摘要**: 该文章讨论了将Multimodal Safety Test Suite扩展到日语，并评估了五种现代日本VLMs的安全性。
- **原始摘要**: arXiv:2611.33789v1 Announce Type: new Abstract: Vision-Language Models (VLMs) are increasingly deployed in Japanese-language settings, yet multimodal safety evaluation has been largely English-centric...

### 48. Pitfalls of Dependency-Ready Decoding for Masked Diffusion Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33823
- **AI 摘要**: 文章讨论了依赖准备解码在掩码扩散语言模型中的应用及其效果。
- **原始摘要**: arXiv:2611.33823v1 Announce Type: new Abstract: Masked diffusion models (MDMs) have shown strong performance on structured reasoning tasks such as Sudoku, Trip Planning, and Countdown. MDMs introduce...

### 49. Contextual language representations link narrative processing to language and literacy in children
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33871
- **AI 摘要**: 该文章讨论了使用大型语言模型在儿童故事听讲过程中进行的功能磁共振成像研究，探讨了语言和阅读经验与叙事处理之间的联系。
- **原始摘要**: arXiv:2611.33871v1 Announce Type: new Abstract: Spoken narratives extensively connect moment-to-moment language processing with knowledge accumulated through language and literacy experience. This stu...

### 50. DiCALM: Converting Autoregressive Convolution-Attention Language Models into Discrete Diffusion Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33919
- **AI 摘要**: 本文介绍了一种将卷积-注意力模型转换为掩码扩散生成模型的方法，该方法在保持模型性能的同时提高了效率。
- **原始摘要**: arXiv:2611.33919v1 Announce Type: new Abstract: Existing methods for adapting autoregressive (AR) language models to diffusion generation focus mainly on full-attention architectures. More efficient h...

### 51. Fine-Tuning Without Gradients? Closed-Form, LLM-Written Classifiers on a Frozen Encoder
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33972
- **AI 摘要**: 本文提出了一种新的方法WSP，使用大型语言模型在冻结编码器上进行闭式形式的权重空间编程，以替代传统的梯度微调方法。这种方法在多个数据集上表现优于全微调和LoRA方法。
- **原始摘要**: arXiv:2611.33972v1 Announce Type: new Abstract: Can a classifier computed in closed form on a frozen encoder match gradient fine-tuning? We present closed-form weight-space programming (WSP): a large...

### 52. Residual Cross-Model Narrative Convergence under Shared Prompts: Auditing Prompt Controls and Narrative Measurement
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.34015
- **AI 摘要**: 文章讨论了基于相同提示的LLM生成的故事之间的叙事相似性，分析了51,240个故事，使用了213个叙事特征来比较不同模型生成的故事。文章发现有显著的叙事收敛现象。
- **原始摘要**: arXiv:2611.34015v1 Announce Type: new Abstract: Stories created by LLMs based on the same prompts can be narratively similar to one another. This similarity may reflect constraints imposed by the prom...

### 53. How Much Dependency Can a Marginal Rule See? Total Correlation in Diffusion LM Parallel Decoding
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.31990
- **AI 摘要**: 文章讨论了在扩散语言模型中，基于边缘分布的预测条件总相关性的准确性，以及与固定候选集的估计值之间的差异。
- **原始摘要**: arXiv:2611.31990v1 Announce Type: cross Abstract: A masked diffusion language model is fast because it commits several tokens per step. Each token is sampled from its own marginal, so the dependency b...

### 54. Semantic Density Does Not Predict Agent-Memory Collapse
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33184
- **AI 摘要**: 该文章讨论了持久文本记忆对语言模型代理的影响，以及记忆统计数据是否能提前预测任务准确性的下降。
- **原始摘要**: arXiv:2611.33184v1 Announce Type: cross Abstract: Persistent textual memory can improve LLM agents, but repeated updates can erode task performance. We ask whether memory-store statistics warn before...

### 55. Two Timescales of Forgetting in Fine-tuning of Language Models: Fast Behavioral Suppression and Slow Representational Drift
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33302
- **AI 摘要**: 文章讨论了语言模型在特定任务上的微调过程中，表面行为抑制与支持它的潜在表示是否同时发生的问题。
- **原始摘要**: arXiv:2611.33302v1 Announce Type: cross Abstract: Today, a core pipeline of artificial intelligence systems is pretraining on a broad range of text corpora and then fine-tuning on specific tasks or de...

### 56. Certify What You Plant: Shortcut-Free Proof Depth in Logical Reasoning Data
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33303
- **AI 摘要**: 该文章讨论了逻辑推理数据中的证明深度问题，提出了新的方法来测量和验证问题的实际要求。
- **原始摘要**: arXiv:2611.33303v1 Announce Type: cross Abstract: Procedurally generated logic problems are used to both evaluate and train reasoning in language models. Their difficulty is usually set by planting a...

### 57. The Platonic Representation Hypothesis in Jacobian-Space: Language and Vision Models Agree Approximately Up to a Rotation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33304
- **AI 摘要**: 文章讨论了语言和视觉模型在内部表示上的趋同性，特别是在Jacobian空间中的表现。
- **原始摘要**: arXiv:2611.33304v1 Announce Type: cross Abstract: The Platonic Representation Hypothesis (PRH) posits that AI models converge toward a shared representation of the world, even when trained on differen...

### 58. Building a Unified Inline Code Editing Model for GitHub Copilot
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33314
- **AI 摘要**: 文章讨论了一种新的模型，该模型能够在一个输出空间中预测三种编辑类型，包括光标位置、附近行和远距离行的编辑。这种模型能够在一个响应中包含多个编辑。
- **原始摘要**: arXiv:2611.33314v1 Announce Type: cross Abstract: AI-assisted coding ranges from fully agentic coding to inline code suggestions in the editor. Inline suggestions require predicting a developer's most...

### 59. Temporal Weight Surgery: Repairing Video Grounding with LLM Editors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33339
- **AI 摘要**: 本文提出了一种名为Temporal Weight Surgery的方法，用于修复视频标注中的错误。该方法通过分析语言模型的权重和激活，找到错误源头并进行修复。
- **原始摘要**: arXiv:2611.33339v1 Announce Type: cross Abstract: A surgeon first finds what is wrong, then fixes only that part. We use this idea for video grounding, where video-language models often find the right...

### 60. Measuring and Predicting Image-Token Repair Boundaries in Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33388
- **AI 摘要**: 该文章讨论了如何测量和预测视觉语言模型在处理受损图像时的修复边界，涉及模型层次、Gemma模型、全块修复等概念。
- **原始摘要**: arXiv:2611.33388v1 Announce Type: cross Abstract: Degraded images make vision-language models answer wrongly. Using synthetic paired blur, noise, and low light, we trace which clean image states can s...

### 61. Confidence scores for gated automation of large language models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33394
- **AI 摘要**: 该文章讨论了使用监督学习训练模型来预测大型语言模型生成答案的正确性，以实现自动化决策，并将不确定的回答路由给人类审查。
- **原始摘要**: arXiv:2611.33394v1 Announce Type: cross Abstract: AI agents built on large language models (LLMs) demonstrate strong capabilities in automated decision-making. However, LLMs may produce incorrect answ...

### 62. A Semantics-First Approach to Multimodal Video Captioning with Frozen Encoders and Stabilized Reinforcement Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33409
- **AI 摘要**: 本文提出了一种基于2.7B参数的大语言模型AVQFormer，用于多模态视频描述，通过固定长度的语义对齐模块和适应性自批评序列训练进行优化。
- **原始摘要**: arXiv:2611.33409v1 Announce Type: cross Abstract: We propose the Audio-Visual Query Transformer (AVQFormer), a highly efficient architecture built upon a 2.7B parameter LLM featuring a fixed-length $K...

### 63. PAC Learning to Sample: On Computational Aspects of Language Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33464
- **AI 摘要**: 该文章讨论了语言生成的学习模型，关注的是在有限正例下生成语言的复杂性保证，涉及统计和计算学习理论。
- **原始摘要**: arXiv:2611.33464v1 Announce Type: cross Abstract: The success of language models has motivated theoretical work on learning to sample from distributions on discrete domains. A prominent abstraction is...

### 64. SEEL: Towards End-to-End 3D Sign Generation with Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33588
- **AI 摘要**: 文章讨论了通过语言模型生成手语的方法，提出了一种新的端到端框架SEEL来解决当前方法的局限性。
- **原始摘要**: arXiv:2611.33588v1 Announce Type: cross Abstract: 3D sign language generation aims to produce signing motion from written text. Motivated by the linguistic nature of sign language, recent methods comb...

### 65. State Space Attention: Learning Context-Dependent Memory Retention
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33625
- **AI 摘要**: 本文介绍了一种新的注意力机制State Space Attention（SSA），用于学习长期上下文依赖的记忆保留。
- **原始摘要**: arXiv:2611.33625v1 Announce Type: cross Abstract: Standard attention's key-value cache grows linearly with context length. Bounding it raises the question of what a sequence model should retain for lo...

### 66. The Missing Root: Geometric Imagination Without Images in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33841
- **AI 摘要**: 本文提出了一种新的方法，让大型语言模型获得空间理解能力，通过结合物体姿态和形状嵌入的连续对象标记与词标记，使得语言和几何可以相互关注，从而实现物体场景的逐步构建和更新。
- **原始摘要**: arXiv:2611.33841v1 Announce Type: cross Abstract: This paper proposes a new paradigm and method for giving large language models spatial understanding. Standard language models operate exclusively ove...

### 67. Looped Models are Fast Multi-Token Predictors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33896
- **AI 摘要**: 本文介绍了一种名为Looped模型的方法，通过调整循环次数来加速语言模型的预测。
- **原始摘要**: arXiv:2611.33896v1 Announce Type: cross Abstract: Looped language models can adapt computation for predicting a token without a proportional rescaling in unique model parameters by adjusting the numbe...

### 68. Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2024年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2409.00696
- **AI 摘要**: 本文介绍了一种新的评价系统Polyrating，旨在解决当前基于评分的人工评价系统存在的问题，如无法有效检测和量化偏见，以及成本高昂等问题。
- **原始摘要**: arXiv:2409.00696v5 Announce Type: replace Abstract: Rating-based human evaluation has become an essential tool to accurately evaluate the impressive performance of large language models (LLMs). Howeve...

### 69. The Open Proof Corpus: A Large-Scale Study of LLM-Generated Mathematical Proofs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2506.21621
- **AI 摘要**: 该文章讨论了大型语言模型在数学证明生成方面的进展，并提出了一个包含5000多个由先进LLM生成的人工评估证明的Open Proof Corpus。
- **原始摘要**: arXiv:2506.21621v3 Announce Type: replace Abstract: In recent months, large language models (LLMs) have made significant progress in mathematical proof generation, but further advancement is hindered...

### 70. Luxical: High-Speed Lexical-Dense Text Embeddings
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2512.09015
- **AI 摘要**: 本文介绍了一种名为Luxical的库，用于快速生成文本嵌入，旨在结合快速的词典-语义文本嵌入和大型Transformer嵌入模型的优点。
- **原始摘要**: arXiv:2512.09015v3 Announce Type: replace Abstract: Frontier language model quality increasingly hinges on our ability to organize web-scale text corpora for training. Today's dominant tools trade off...

### 71. Fusian: Multi-LoRA Fusion for Fine-Grained Continuous MBTI Personality Control in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.15405
- **AI 摘要**: 本文介绍了一种名为Fusian的新框架，用于在大型语言模型中实现精细且连续的人格控制。
- **原始摘要**: arXiv:2603.15405v2 Announce Type: replace Abstract: Large Language Models (LLMs) have demonstrated impressive capabilities in simulating diverse human behaviors and personalities. However, existing me...

### 72. SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.04511
- **AI 摘要**: 本文提出了一种名为SparDA的架构，用于减少长序列上下文LLM推理的计算和带宽需求。
- **原始摘要**: arXiv:2606.04511v2 Announce Type: replace Abstract: Sparse attention reduces compute and memory bandwidth for long-context LLM inference. However, two key challenges remain: (1) KV cache capacity stil...

### 73. RepSelect: Robust LLM Unlearning via Representation Selectivity
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.17168
- **AI 摘要**: 本文提出了一种新的方法RepSelect，用于深度去除大型语言模型（LLM）中的有害知识，避免了现有方法的不足。
- **原始摘要**: arXiv:2606.17168v4 Announce Type: replace Abstract: When LLM weights are open or fine-tuning is available through an API, suppressing hazardous knowledge and tendencies is not enough: removal has to b...

### 74. RA-DPO: Reliability-Aware Preference Optimization and Selective Prediction for Sexism Detection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12330
- **AI 摘要**: 本文提出了一种RA-DPO框架，用于提高性别歧视检测系统的鲁棒性和选择性预测能力。
- **原始摘要**: arXiv:2608.12330v2 Announce Type: replace Abstract: Sexism detection is subjective, yet most systems reduce multi-annotator labels to a single majority label, discarding annotator agreement and model...

### 75. Large-scale factor analysis shows machine intelligence is only partially interpretable
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.36515
- **AI 摘要**: 该文章讨论了语言模型中的智力因素分析，使用因子分析方法对13,230个公开评估分数进行了分析。
- **原始摘要**: arXiv:2609.36515v2 Announce Type: replace Abstract: A common assumption in language model development is that cognitive abilities are organized around a general, domain-free intelligence factor, like...

### 76. Can Language Models Learn to Forecast Stock Prices?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.36914
- **AI 摘要**: 文章讨论了语言模型如何在股票价格预测中学习，提到了模型在预测未来股票回报时存在的问题，并提出了一种通过直接在沙盒中训练模型来改进的方法。
- **原始摘要**: arXiv:2609.36914v4 Announce Type: replace Abstract: We build BETA, a chronological sandbox over S&P 500 stocks in which a model calls tools to retrieve prices, indicators, and news available up to a d...

### 77. Do Language Models Need a Trainable Input Embedding Table? Fixed Minimal Token Codes at 1.7B-Class Scale
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.04002
- **AI 摘要**: 文章讨论了语言模型是否需要可学习的输入嵌入表，提出了一种固定输入编码的方法，并在100B预测目标上进行了训练。
- **原始摘要**: arXiv:2610.04002v2 Announce Type: replace Abstract: A token must be identifiable before a language model can learn how to use it. Must its input coordinates also be learned? We replace the trainable i...

### 78. Explaining Chess and Go with Discovered Motifs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.23166
- **AI 摘要**: 文章讨论了现代国际象棋引擎在理解复杂策略方面的能力，并提出了一种新的方法来改进这些模型，使其能够更好地解释棋步。
- **原始摘要**: arXiv:2610.23166v2 Announce Type: replace Abstract: Modern chess engines play far beyond human ability, often choosing moves whose underlying ideas are difficult for humans to understand. We propose a...

### 79. Training language models on first-person reactions can instil the beliefs behind them
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.31683
- **AI 摘要**: 文章讨论了通过训练语言模型在第一人称视角下反应来植入信念，这种信念会影响模型的行为，而不仅仅是内容。文章提到了临床开发的问卷调查水平的偏移。
- **原始摘要**: arXiv:2610.31683v2 Announce Type: replace Abstract: Language models are increasingly given a character by training them on examples of how that character speaks. Here we show that such training can in...

### 80. Where Is Uncertainty Observed? A Mechanistic Understanding of Uncertainty Quantification in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.15735
- **AI 摘要**: 文章讨论了大型语言模型不确定性量化的方法，并提出了四种机制观察视角：结构视角、表示视角、分布视角和语义视角。
- **原始摘要**: arXiv:2611.15735v2 Announce Type: replace Abstract: Knowing when a large language model's (LLM's) response can be trusted is critical for its safe use. Uncertainty quantification (UQ) can help LLMs re...

### 81. FIDEL: Abugida-Aware Pre-tokenization for Ethiopic Languages
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.20216
- **AI 摘要**: 本文介绍了一种新的预标记技术FIDEL，用于埃塞俄比亚语的预标记，该技术能够揭示辅音和元音的顺序结构。
- **原始摘要**: arXiv:2611.20216v2 Announce Type: replace Abstract: Subword tokenizers assume that meaningful linguistic units can be recovered by splitting text at learned boundaries, an assumption better suited to...

### 82. United in Diversity? Contextual Biases in LLM-Based Predictions of the 2024 European Parliament Elections
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2024年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2409.09045
- **AI 摘要**: 该文章讨论了基于大型语言模型的预测在2024年欧洲议会选举中的偏见问题，指出这些模型可能因训练数据的多样性不足而产生偏差。
- **原始摘要**: arXiv:2409.09045v3 Announce Type: replace-cross Abstract: "Silicon samples" based on large language models (LLMs) have been argued to serve as efficient alternatives to surveys of humans, assuming tha...

### 83. Semantic Gravity Wells: Why Negative Constraints Backfire
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.08070
- **AI 摘要**: 该文章讨论了大型语言模型在执行禁止指令时的表现，引入了语义压力的概念来量化模型生成被禁止词语的概率。
- **原始摘要**: arXiv:2601.08070v2 Announce Type: replace-cross Abstract: Negative constraints (instructions of the form "do not use word X") represent a fundamental test of instruction-following capability in large...

### 84. Neural Isomorphic Fields: A Transformer-based Algebraic Numerical Embedding
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.12095
- **AI 摘要**: 该文章介绍了一种名为Neural Isomorphic Fields的方法，用于解决神经网络模型处理非常小或非常大的数字时遇到的溢出、下溢和不稳定输出变化等问题。
- **原始摘要**: arXiv:2601.12095v2 Announce Type: replace-cross Abstract: Neural network models often face challenges when processing very small or very large numbers due to issues such as overflow, underflow, and un...

### 85. Mechanistic Interpretability of Cognitive Complexity in LLMs via Linear Probing using Bloom's Taxonomy
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.17229
- **AI 摘要**: 该文章探讨了使用Blooms Taxonomy分析大型语言模型内部神经表示的方法，发现不同Blooms级别（从基本回忆到抽象合成）在模型的残差流中是线性可分的。
- **原始摘要**: arXiv:2602.17229v3 Announce Type: replace-cross Abstract: The black-box nature of Large Language Models necessitates novel evaluation frameworks that transcend surface-level performance metrics. This...

### 86. Thinking Deeper, Not Longer: Memory-Efficient Latent Chain-of-Thought with Depth-Recurrent Transformers for Compositional Generalization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.21676
- **AI 摘要**: 该文章讨论了一种深度可重入的Transformer，旨在解决标准Transformer在需要变长推理的任务中计算深度固定的限制问题。
- **原始摘要**: arXiv:2603.21676v3 Announce Type: replace-cross Abstract: Standard Transformers have a fixed computational depth, limiting their ability to generalize to tasks that require variable-depth reasoning. T...

### 87. The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.27510
- **AI 摘要**: 文章讨论了激活补丁技术在解释模型行为时的局限性，特别是交互效应的影响。
- **原始摘要**: arXiv:2606.27510v2 Announce Type: replace-cross Abstract: Activation patching is a primary tool in mechanistic interpretability. It attributes causal responsibility for a model's behavior to each of i...

### 88. Safe Inference-Time Alignment via Lagrangian Reward Augmentation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.02781
- **AI 摘要**: 该文章讨论了通过拉格朗日奖励增强来实现推理时间对齐的方法，以避免重复权重更新带来的成本，并提出了一种在安全约束下的一般推理时间对齐框架。
- **原始摘要**: arXiv:2607.02781v3 Announce Type: replace-cross Abstract: Inference-time alignment steers a frozen language model during decoding using auxiliary reward signals, avoiding the cost of repeated weight u...

### 89. Information Discernment in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.19355
- **AI 摘要**: 文章讨论了大型语言模型在使用外部知识源时的信息甄别能力，包括对可靠来源的更新和对接近真实信息的更新。
- **原始摘要**: arXiv:2607.19355v2 Announce Type: replace-cross Abstract: LLMs are increasingly used with external knowledge sources like the internet. Do they weigh information appropriately -- updating more for rel...

### 90. Representation Redistribution in Sparse Autoencoders
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.21240
- **AI 摘要**: 该文章讨论了在不同上下文或格式下，稀疏自编码器（SAE）特征响应的变化，并提出了重新分配敏感性得分（RSS）来识别在一致方向上重复出现的大特征变化。
- **原始摘要**: arXiv:2610.21240v2 Announce Type: replace-cross Abstract: Presenting the same request with different context or formatting can change which sparse autoencoder (SAE) features respond inside a language...

### 91. Behavioral Compositionality of Sparse Autoencoder Representations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.21261
- **AI 摘要**: 文章讨论了Sparse Autoencoder（SAE）特征的组合性及其在语言模型行为解释中的应用。
- **原始摘要**: arXiv:2610.21261v2 Announce Type: replace-cross Abstract: Sparse autoencoders (SAEs) provide features that can be combined to explain and steer language model behavior. Understanding these combination...

### 92. Bias Cascade: Understanding the Gap Between Knowledge Alignment and Effect Replication in LLM-based Social Simulation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.28854
- **AI 摘要**: 该文章讨论了大型语言模型在社会实验中的应用，以及它们能否准确模拟社会干预的效果。文章引入了一个基准来比较知识判断与效果模拟。
- **原始摘要**: arXiv:2611.28854v2 Announce Type: replace-cross Abstract: Large language models (LLMs) are increasingly used to simulate participants in social experiments. Existing research has primarily focused on...

### 93. Understanding Failure Patterns in LLM-Based Mathematical Optimization Modeling
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33351
- **AI 摘要**: 文章讨论了大型语言模型在工业优化建模中的表现问题，包括非执行、无效和可行但错误的解决方案。文章分析了数学推理、求解器使用和领域知识三个组成部分的失败模式。
- **原始摘要**: arXiv:2611.33351v1 Announce Type: new Abstract: Industrial optimization involves complex constraints, making optimization modeling difficult to automate. Large language models (LLMs) have been explore...

### 94. Temporal Selective Exploration for Reinforcement Learning-Guided Continuous-Discrete Flow Matching in 3D Molecular Design
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33417
- **AI 摘要**: 该文章讨论了用于3D分子设计的流匹配优化方法，特别是通过强化学习和时间选择性探索来处理连续-离散混合设置。
- **原始摘要**: arXiv:2611.33417v1 Announce Type: new Abstract: Flow matching has shown strong potential in generative tasks, while its optimization via Reinforcement Learning (RL) remains underexplored, especially i...

### 95. Differentially Private Policy Optimization in Linear MDPs with Adversarial Rewards
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33469
- **AI 摘要**: 该文章讨论了在未知转换和自适应对抗性线性奖励的线性MDPs中，如何使用不同的隐私保护策略进行个性化服务的强化学习政策优化。
- **原始摘要**: arXiv:2611.33469v1 Announce Type: new Abstract: Reinforcement learning (RL) in personalized services often relies on sensitive interaction data. Motivated by the need to protect these data, we study d...

### 96. A Perturbation-Driven Framework for Sensitivity Analysis of Dimensionality Reduction
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33523
- **AI 摘要**: 该文章讨论了一种基于扰动驱动的框架，用于分析降维方法对输入变化的敏感性，适用于处理现实世界中数据有限且嘈杂的情况。
- **原始摘要**: arXiv:2611.33523v1 Announce Type: new Abstract: Low-dimensional representations produced by dimensionality reduction (DR) are commonly evaluated using distortion measures such as trustworthiness and c...

### 97. Amortizing Exact Orthogonality: Drift-Triggered Restoration for Orthogonal Fine-Tuning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33589
- **AI 摘要**: 该文章讨论了一种新的正交微调方法RTOFT，通过使用第一阶更新和极分解来恢复正交性，从而避免了每次优化步骤都构造精确或近似正交变换的缺点。
- **原始摘要**: arXiv:2611.33589v1 Announce Type: new Abstract: Orthogonal finetuning (OFT) adapts a pretrained weight by an orthogonal transform and preserves its singular values and row angles, but existing methods...

### 98. The Danger of Double Precision: Working Precision as a Hidden Constraint in Gaussian Process Maximum Likelihood
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33647
- **AI 摘要**: 文章讨论了高精度Gaussian过程的最大似然估计，指出在双精度下拟合超出了条件范围，需要更宽的精度才能获得更好的结果。
- **原始摘要**: arXiv:2611.33647v1 Announce Type: new Abstract: Gaussian process (GP) hyperparameters are routinely fitted by maximizing the marginal likelihood in IEEE double precision, although for smooth kernels a...

### 99. PRIOR: Pre-Call Reasoning in SFT and Its Influence on Tool-Use Retention under RL
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33648
- **AI 摘要**: 该文章讨论了监督微调（SFT）数据特性对强化学习（RL）中工具使用保留的影响。
- **原始摘要**: arXiv:2611.33648v1 Announce Type: new Abstract: Tool use learned during supervised fine-tuning (SFT) is not always retained during reinforcement learning (RL). We study how properties of SFT data may...

### 100. Self-supervised Clipped-objective Reinforcement Leaning Framework for Risk-aware Portfolio Management
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33652
- **AI 摘要**: 该文章讨论了一种新的自监督剪辑目标强化学习框架，用于风险感知的资产组合管理。
- **原始摘要**: arXiv:2611.33652v1 Announce Type: new Abstract: Portfolio management involves balancing diverse financial assets, a critical yet challenging task in quantitative trading. Although deep reinforcement l...

### 101. Understanding Mode Collapse in Diffusion Models under Classifier-Free Guidance
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33719
- **AI 摘要**: 文章讨论了在无分类器引导的扩散和流模型中的模式坍缩现象，提出了一种分析模型来解释这种现象。
- **原始摘要**: arXiv:2611.33719v1 Announce Type: new Abstract: The use of classifier-free guidance in diffusion and flow models has proven critical to their empirical success, as it allows for the controllable gener...

### 102. Don't Waste the Population: Post-Anneal Refinement for Combinatorial Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33766
- **AI 摘要**: 该文章讨论了一种新的方法I-PRP，用于改进并行退火生成的候选解，以发现更好的解。文章提出了一种确定性的方法，无需训练，能够利用候选解的多样性来改进解的质量。
- **原始摘要**: arXiv:2611.33766v1 Announce Type: new Abstract: Parallel annealers generate diverse candidate solutions; yet, conventional post-processing typically refines only the best, leaving much of the populati...

### 103. On the Learnability of Model Reprogramming: A Reachability and Relabeling Perspective
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33889
- **AI 摘要**: 文章讨论了模型重编程的学习能力，通过分析模型结构来回答需要多少样本才能接近最佳预测器以及与目标贝叶斯风险之间的差距。
- **原始摘要**: arXiv:2611.33889v1 Announce Type: new Abstract: Model reprogramming adapts a frozen source model to a target task by wrapping it in a learnable input transformation from target input to the source-mod...

### 104. InstructTTS-OPD: On-Policy Distillation for Multi-Objective Instruction-Following TTS
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33937
- **AI 摘要**: 文章讨论了On-Policy Distillation技术在多目标指令跟随文本转语音(Instruct-TTS)中的应用，提出了替代传统方法的解决方案。
- **原始摘要**: arXiv:2611.33937v1 Announce Type: new Abstract: Instruction-following text-to-speech (Instruct-TTS) renders a target transcript in the manner described by a free-form natural-language instruction, and...

### 105. DuoMI: Dual Mutual Information Regularization for Expert Reuse in Looped Transformers
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33952
- **AI 摘要**: 本文介绍了一种新的方法DuoMI，用于解决循环混合专家（MoE）Transformer中不同轮次之间专家路由的问题。
- **原始摘要**: arXiv:2611.33952v1 Announce Type: new Abstract: We introduce Dual Mutual Information Regularization (DuoMI), a method for regulating expert routing across rounds in looped mixture-of-experts (MoE) Tra...

### 106. Quaternion-Tucker ZigZag Networks: Halving Transformer Backbone Parameters and Enabling Exact 2D Zero-Loss Continual Scaling
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33983
- **AI 摘要**: 文章讨论了Quaternion-Tucker ZigZag Networks模型，该模型通过减少Transformer的参数数量和实现精确的二维零损失连续缩放来提高效率。
- **原始摘要**: arXiv:2611.33983v1 Announce Type: new Abstract: Standard Transformers allocate independent dense weight matrices to every feed-forward network (FFN) layer, coupling parameters linearly with depth (O(L...

### 107. Generalizable Equivariant Diffusion Models for Non-Abelian Lattice Gauge Theory: Analytical Foundations and Numerical Scaling Tests
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.03530
- **AI 摘要**: 文章讨论了使用Gauge-equivariant diffusion模型在非阿贝尔格氏理论中的应用，包括反向时间随机微分方程的严格推导、去噪损失函数的保不变性讨论以及与格子体积和耦合反平方根的缩放行为的数值基准测试。
- **原始摘要**: arXiv:2611.03530v2 Announce Type: cross Abstract: Gauge-equivariant diffusion models can be used to generate ensembles of field configurations in non-abelian lattice gauge theories. Previously, we dem...

### 108. RankCast: Phase-Aware Rank Balancing in MoE Serving
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33542
- **AI 摘要**: 文章讨论了现代大规模语言模型推理中预填充和解码阶段的负载不平衡问题，并提出了一种RankCast系统来解决这个问题。
- **原始摘要**: arXiv:2611.33542v1 Announce Type: cross Abstract: Modern large language model (LLM) inference increasingly adopts disaggregated architectures that separate Prefill (P) and Decode (D) phases. Meanwhile...

### 109. FlashProve-Next: Verifiable Inference for Production LLM APIs
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33741
- **AI 摘要**: 该文章讨论了如何为生产环境下的大型语言模型（LLM）API提供可验证的证明，以确保模型的准确性和透明度。文章提出了一种新的FlashProve-Next方法，能够在不修改原生服务的情况下生成零知识证明。
- **原始摘要**: arXiv:2611.33741v1 Announce Type: cross Abstract: Clients of closed-weight LLM APIs cannot verify whether a provider ran the advertised model, precision, hidden prompt, and reasoning budget. Existing...

### 110. RHOPE: LLM-Augmented Adaptive Experimental Design with Complex Contextual Information
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33767
- **AI 摘要**: 该文章讨论了一种使用大型语言模型（LLM）来增强实验设计的方法，特别是在处理复杂上下文信息时。
- **原始摘要**: arXiv:2611.33767v1 Announce Type: cross Abstract: Experimental design allocates limited measurement effort across candidate treatments to learn their expected outcomes. Adaptive designs refine allocat...

### 111. QPAT: A Universal Quantum Machine Learning Framework for Quantum-Assisted Training and Classical Inference
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33806
- **AI 摘要**: 本文提出了一种名为QPAT的量子机器学习框架，旨在解决量子辅助训练和经典推断中的问题。
- **原始摘要**: arXiv:2611.33806v1 Announce Type: cross Abstract: Deep learning models often struggle with sharp local optima and overfitting in limited-data regimes, and exhibit limited capacity for capturing high-o...

### 112. KnitNet: Learning to Search at Inference Time for Exact RNA Inverse Design
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33812
- **AI 摘要**: 文章讨论了RNA逆向设计中学习生成器的局限性，提出了一种在推断时间进行缩放的框架KnitNet，用于从验证器反馈中学习以优化精确折叠匹配的序列。
- **原始摘要**: arXiv:2611.33812v1 Announce Type: cross Abstract: RNA inverse design seeks nucleotide sequences that fold into specified target structures. Existing methods rely on learned generators that can miss ex...

### 113. Accelerated Proximal Gradient Methods for Multiobjective Optimization over Probability Measures via Hilbert-Space Lifting
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.34073
- **AI 摘要**: 本文提出了一种新的多目标优化方法，用于概率测度的KL散度，通过希尔伯特空间提升来解决粒子方法和加速方法中的问题。
- **原始摘要**: arXiv:2611.34073v1 Announce Type: cross Abstract: Many sampling and inference tasks require a single distribution that balances several targets. We formulate this task as multiobjective optimization o...

### 114. Machine Learning-Driven Virtual Bidding with Electricity Market Efficiency Analysis
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2021年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2104.02754
- **AI 摘要**: 该文章讨论了利用机器学习驱动的虚拟投标优化框架，以考虑风险约束和价格敏感性，以及基于市场清算算法的LMP价差预测模型。
- **原始摘要**: arXiv:2104.02754v2 Announce Type: replace Abstract: This paper develops a machine learning-driven portfolio optimization framework for virtual bidding in electricity markets considering both risk cons...

### 115. EEG Foundation Models Need Channel Adaptation, but Fixed Channel Mappings Often Suffice
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.23091
- **AI 摘要**: 文章讨论了EEG基础模型在不同montage数据上的适应性问题，比较了五种适应方法的效果。最终发现适应方法的效果取决于模型架构。
- **原始摘要**: arXiv:2604.23091v2 Announce Type: replace Abstract: Scaling EEG foundation models requires pooling data across heterogeneous montages, so every model needs a channel-adaptation step mapping an arbitra...

### 116. Scalable Heterogeneous Graph Foundation Models for Data-Driven Optimal Power Flow in Smart Grids
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.23194
- **AI 摘要**: 该文章讨论了用于智能电网数据驱动最优潮流近似的大规模异构图学习工作流程，涉及HydraGNN框架。
- **原始摘要**: arXiv:2605.23194v3 Announce Type: replace Abstract: Fast and reliable optimal power flow (OPF) approximation is important for power system operation, yet heterogeneous OPF graph models are often evalu...

### 117. Recurrent In-Context Learning for Tabular Foundation Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.14998
- **AI 摘要**: 该文章讨论了在表格基础模型中使用循环内上下文学习的方法，试图减少参数数量以提高模型性能。
- **原始摘要**: arXiv:2610.14998v2 Announce Type: replace Abstract: Tabular foundation models predict unlabelled rows from labelled rows in a single forward pass via in-context learning (ICL). Like language models, t...

### 118. InterQ-RL: Interaction-Aware Correction of Execution Mismatch in Quantized Agentic RL
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.35303
- **AI 摘要**: 文章讨论了在量化代理RL中解决执行不匹配的问题，提出了InterQ-RL方法来修正量化后的执行不一致问题。
- **原始摘要**: arXiv:2610.35303v2 Announce Type: replace Abstract: Multi-turn agent reinforcement learning (RL) relies on long closed-loop rollouts, making generation and KV-cache costs a major bottleneck. Quantized...

### 119. When does off-block Hessian curvature help an optimization step?
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.01335
- **AI 摘要**: 文章讨论了在优化过程中使用离块海森曲率的时机，以及它对步骤的影响。
- **原始摘要**: arXiv:2611.01335v4 Announce Type: replace Abstract: Testing an off-block Hessian correction alone can discard a step that lowers minibatch loss. We measure both the missed improvement and the gain fro...

### 120. Out-of-the-Box Tabular Foundation Models for Bayesian Optimization in Materials Discovery
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12491
- **AI 摘要**: 文章讨论了Tabular Foundation Models在材料科学中的应用，特别是在Bayesian优化中的表现，指出TFMs作为结构化数据预测任务的高性能模型，无需特定的任务训练或Gaussian过程核的选择。
- **原始摘要**: arXiv:2611.12491v3 Announce Type: replace Abstract: Bayesian optimization is widely used in active learning loops for materials science. Gaussian processes serve as the de-facto surrogate model family...

### 121. Enrichment-Oriented Virtual Screening of Perovskite Solar Cells through Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.18043
- **AI 摘要**: 该文章讨论了通过强化学习优化钙钛矿太阳能电池的方法，涉及虚拟筛选和代理网络技术。
- **原始摘要**: arXiv:2611.18043v2 Announce Type: replace Abstract: Experimental optimization of perovskite solar cells is constrained by combinatorial diversity in absorber compositions, device layers, and processin...

### 122. A Fused Gaussian Process Bandit Framework for Multi-Fidelity Bayesian Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.32092
- **AI 摘要**: 文章讨论了用于多精度贝叶斯优化的融合高斯过程带参数框架，属于AI模型类别。
- **原始摘要**: arXiv:2611.32092v2 Announce Type: replace Abstract: Bayesian optimization (BO) is widely used to maximize expensive black-box functions when direct evaluation is costly. In many real-world application...

### 123. Neur2BiLO: Neural Bilevel Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2024年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2402.02552
- **AI 摘要**: 文章讨论了Neur2BiLO框架，该框架使用神经网络逼近Bilevel优化中的领导者或跟随者的值函数，并通过监督回归进行训练，以解决混合整数线性Bilevel优化问题。
- **原始摘要**: arXiv:2402.02552v3 Announce Type: replace-cross Abstract: Bilevel optimization deals with nested problems in which a leader takes the first decision to minimize their objective function while accounti...

### 124. Point2SSM++: Self-Supervised Learning of Anatomical Shape Models from Point Clouds
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2024年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2405.09707
- **AI 摘要**: 文章讨论了Point2SSM++，一种基于自监督学习的深度学习方法，用于从点云数据中学习解剖形状模型。该方法旨在解决传统SSM技术在临床研究中的应用受限问题。
- **原始摘要**: arXiv:2405.09707v2 Announce Type: replace-cross Abstract: Correspondence-based statistical shape modeling (SSM) stands as a powerful technology for morphometric analysis in clinical research. SSM faci...

### 125. Statistical Inference for Differentially Private Stochastic Gradient Descent
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2507.20560
- **AI 摘要**: 该文章讨论了在差分隐私随机梯度下降（DP-SGD）中的统计推断方法，填补了随机采样和差分隐私随机采样在统计推断方法上的空白。
- **原始摘要**: arXiv:2507.20560v3 Announce Type: replace-cross Abstract: Privacy preservation in machine learning, particularly through Differentially Private Stochastic Gradient Descent (DP-SGD), is crucial for ana...

### 126. StochEP: Stochastic Equilibrium Propagation for Spiking Convergent Recurrent Neural Networks
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2511.11320
- **AI 摘要**: 本文提出了一种新的EP框架，用于训练生物启发的SNNs，该框架将概率性突触神经元整合到EP中，以改善优化景观，稳定训练过程，并使SNNs的学习更加高效和可扩展。
- **原始摘要**: arXiv:2511.11320v2 Announce Type: replace-cross Abstract: Spiking Neural Networks (SNNs) promise energy-efficient, sparse, biologically inspired computation. Training them with Backpropagation Through...

### 127. BayesFlow 2: Multi-Backend Amortized Bayesian Inference in Python
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.07098
- **AI 摘要**: 本文介绍了BayesFlow 2，这是一个用于多后端自适应贝叶斯推理的Python库，支持快速估计模型中的任何量，如点估计、似然性和全后验分布。
- **原始摘要**: arXiv:2602.07098v3 Announce Type: replace-cross Abstract: Modern Bayesian inference involves a mixture of computational methods for estimating, validating, and drawing conclusions from probabilistic m...

### 128. Learned Finite Element-based Regularization of the Inverse Problem in Electrocardiographic Imaging
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.07466
- **AI 摘要**: 该文章讨论了在心电成像（ECGI）中引入空间-时间正则化框架，结合学习到的时域专家（FoE）先验，以改善心电活动的重建。文章提出了基于非结构化心脏表面网格的有限元离散化方法。
- **原始摘要**: arXiv:2602.07466v3 Announce Type: replace-cross Abstract: Electrocardiographic imaging (ECGI) seeks to reconstruct cardiac electrical activity from body-surface potentials noninvasively. However, the...

### 129. Reinforcement Learning from Human Feedback: A Statistical Perspective
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.02507
- **AI 摘要**: 文章讨论了从人类反馈进行强化学习（RLHF）的方法及其背后的统计问题，重点在于大型语言模型（LLMs）与人类偏好的一致性。
- **原始摘要**: arXiv:2604.02507v2 Announce Type: replace-cross Abstract: Reinforcement learning from human feedback (RLHF) has emerged as a central framework for aligning large language models (LLMs) with human pref...

### 130. NSFL: A Post-Training Neuro-Symbolic Fuzzy Logic Framework for Boolean Operators in Neural Embeddings
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.10604
- **AI 摘要**: 本文介绍了一种名为NSFL的框架，它通过神经符号模糊逻辑将逻辑结构引入神经嵌入空间，适用于神经检索器中的多原子逻辑约束。
- **原始摘要**: arXiv:2604.10604v2 Announce Type: replace-cross Abstract: Standard dense retrievers have no native mechanism for multi-atom logical constraints. We introduce Neuro-Symbolic Fuzzy Logic (NSFL), a train...

### 131. Effect-Driven Skill Abstractions for Offline Reinforcement Learning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33229
- **AI 摘要**: 该文章讨论了一种新的动作片段量化方法，旨在通过优化当前状态和动作条件下的未来状态预测来学习离散技能抽象，以促进长期目标导向的强化学习任务。
- **原始摘要**: arXiv:2611.33229v1 Announce Type: new Abstract: We seek to learn discrete skill abstractions to facilitate long-horizon, goal-conditioned reinforcement-learning (RL) tasks. Recent approaches have show...

### 132. FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision-Language-Action Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33635
- **AI 摘要**: 本文提出了一种新的视觉语言动作模型FreshVLA，通过频率引导和动态敏感的学习范式来获取时序层次化的连续潜在动作。
- **原始摘要**: arXiv:2611.33635v1 Announce Type: new Abstract: Learning reusable latent actions from action-free videos offers an effective route to improving Vision-Language-Action (VLA) policies. However, reconstr...

### 133. Practice Makes Fluent: Learning to Use Earlier Predictions in Looped Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33722
- **AI 摘要**: 该文章讨论了一种名为FLUENT的方法，用于训练能够在较少迭代中完成任务的循环模型。文章提出了解决共享权重更新问题的方法。
- **原始摘要**: arXiv:2611.33722v1 Announce Type: new Abstract: People become faster at a task through practice, but models that improve with experience do not necessarily learn to use less computation. We train loop...

### 134. Scaling Law of Neural Koopman Operators
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.19943
- **AI 摘要**: 本文研究了神经柯普曼模型中样本大小与隐空间维度之间的关系，提出了一个理论和实证框架来理解它们之间的相互作用。
- **原始摘要**: arXiv:2602.19943v2 Announce Type: replace Abstract: Neural Koopman models approximate and control nonlinear dynamical systems through linear dynamics in a learned latent space. Their performance depen...

### 135. PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.10925
- **AI 摘要**: 本文提出了一种名为PriorVLA的新框架，旨在在视觉语言动作模型上保留预训练的先验知识，并通过适应专家来有效进行下游任务的适应。
- **原始摘要**: arXiv:2605.10925v2 Announce Type: replace Abstract: Large-scale pretraining has made Vision-Language-Action (VLA) models promising foundations for generalist robot manipulation, yet adapting them to d...

### 136. Self-Distilling Future Video Representations for World Action Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.30320
- **AI 摘要**: 本文提出了一种新的框架FRED，用于训练世界行动模型（WAMs），以提高未来视频表示的质量，从而减少迭代去噪的需要。
- **原始摘要**: arXiv:2610.30320v3 Announce Type: replace Abstract: World Action Models (WAMs) have emerged as a promising approach to learning generalist robot policies using rich spatiotemporal priors from pre-trai...

### 137. SeQLean: Verifying SQL queries using Lean
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.33181
- **AI 摘要**: 该文章介绍了一种使用Lean进行形式验证的系统SeQLean，用于提高自然语言到SQL的翻译准确性。
- **原始摘要**: arXiv:2611.33181v1 Announce Type: new Abstract: We present SeQLean, a system that uses formal verification in Lean to increase the accuracy of translation from natural language to SQL. This is based o...

### 138. Parallelizable Feynman-Kac Models for Universal Probabilistic Programming
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.22463
- **AI 摘要**: 文章讨论了在概率程序上下文中，如何使用期望为基础的语义来实现并行化和高效的蒙特卡洛推理。
- **原始摘要**: arXiv:2603.22463v2 Announce Type: replace Abstract: We study provably correct and efficient instantiations of Sequential Monte Carlo (SMC) inference in the context of formal operational semantics of P...

### 139. The missing map of the sky
- **来源**: Anthropic Research (TIER1)
- **发布日期**: 2026-11-27
- **类型**: research
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.anthropic.com/research/the-missing-map-of-the-sky
- **AI 摘要**: 文章摘要为《The missing map of the sky》，但未提供足够的信息来确定其具体主题类别。根据提供的信息，文章可能涉及技术或科学领域，但无法准确分类。

## 🏷️  Harness工程

**62 篇文章**

### 1. 任少卿带着世界模型3.0来了！蔚来智驾训练提效5倍，座舱也用上强化学习
- **来源**: 量子位 (TIER3)
- **发布日期**: Thu, 26 Nov 2026 03:23:35 +0000 (昨天)
- **类型**: news
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.qbitai.com/2026/11/512897.html
- **AI 摘要**: 文章主要介绍了蔚来在智能座舱和自动驾驶领域的AI进展，包括NOMI Intelligence 4.0和蔚来世界模型NWM 3.0的发布，以及蔚来内部建设AI原生组织的情况。文章强调了大模型在智能座舱中的应用，以及蔚来构建的整车智能体原生安全体系。
- **原始摘要**: 李斌坦言：不做AI变革可能活不下去

### 2. Taking on Starlink: Europe’s largest satellite factory opens in push to rival Musk
- **来源**: CNBC World News (TIER3)
- **发布日期**: Thu, 26 Nov 2026 07:45:05 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cnbc.com/2026/11/26/starlink-satellites-aerospacelab-factory-belgium.html
- **AI 摘要**: 欧洲最大的卫星工厂在比利时开业，由私人控股的Aerospacelab运营，计划制造264颗卫星以对抗Elon Musk的Starlink项目。卫星通信在日常生活和国家安全方面变得越来越重要。
- **原始摘要**: The 20,000-square-meter mega factory will be able to produce up to 500 satellites annually, making it the world's third-largest satellite production site.

### 3. Distilling Kimi-K3.1-Pro into Qwen3.8-27B: Teaching a model a new language
- **来源**: Together AI Blog (TIER2)
- **发布日期**: Thu, 26 Nov 2026 00:00:00 GMT (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://www.together.ai/blog/distilling-kimi-into-qwen
- **AI 摘要**: 本文介绍了Together编译器和Together Link，讨论了模型蒸馏和模型优化等内容。文章主要涉及AI工程实践和模型优化。
- **原始摘要**: Qwen3.8-27B answered in Thai when asked for Lao. We distilled Kimi-K3.1-Pro's Lao translation into it with Together Post-Training: 93% of the teacher's score, with Thai intact. Code and costs included...

### 4. EvOrderBench: When do sampled frames establish event order?
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33492
- **AI 摘要**: 该文章讨论了一个新的视频事件顺序基准测试EvOrderBench，用于评估视觉语言模型在只有少量采样帧的情况下判断视频中事件顺序的能力。
- **原始摘要**: arXiv:2611.33492v1 Announce Type: new Abstract: Vision-language models (VLMs) are often asked which of two actions in a video happened first, given only a few sampled frames. Such frames can show that...

### 5. CariesBench: A Hierarchical Multi-view Benchmark for Dental Caries Screening and Diagnostic Reasoning from 3D Intraoral Scans
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33643
- **AI 摘要**: 本文介绍了一个用于牙釉质筛查和诊断推理的多视图基准CariesBench，该基准由5932个3D口腔扫描数据组成，包含85455个标准化多视图渲染和133994个临床基础视觉问题。
- **原始摘要**: arXiv:2611.33643v1 Announce Type: new Abstract: Dental caries assessment is a structured clinical process requiring lesion localization, identification of the affected tooth and surface, and severity...

### 6. WorldUAV: Scaling UAV Data Synthesis via World Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33682
- **AI 摘要**: 文章讨论了通过世界模型构建高质量无人机数据集的方法，旨在解决现有合成数据与真实数据之间的差距问题。
- **原始摘要**: arXiv:2611.33682v1 Announce Type: new Abstract: UAV detection and tracking remain constrained by the scarcity of high-quality training data. Existing game-engine-based synthetic UAV data suffer from a...

### 7. RelPRM: Grounding Visual Process Reward Models in Relational Evidence
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33903
- **AI 摘要**: 文章讨论了如何通过自动化管道来验证视觉过程奖励模型中的关系声明，以提高模型的准确性。
- **原始摘要**: arXiv:2611.33903v1 Announce Type: new Abstract: Visual process reward models (PRMs) can detect calculation errors yet assign high scores to steps that misread visual relations. Supervision based on su...

### 8. Manga Page Parser: Comprehensive Visual Parsing through Local Story Understanding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.34006
- **AI 摘要**: 文章讨论了通过局部故事理解来解析漫画的方法，提出了一种名为MangaParser的阅读框架，该框架能够独立分析每页漫画，进行角色聚类、说话者标注和说话者与角色的绑定，且无需额外训练或微调。
- **原始摘要**: arXiv:2611.34006v1 Announce Type: new Abstract: Understanding manga requires connecting who appears and who speaks with the events, character states, and relationships that unfold across panels. We st...

### 9. Structure-Aware Multimodal Retrieval Under Data Scarcity, Privacy Constraints and Out-of-Domain Content
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33649
- **AI 摘要**: 该文章讨论了一种结构感知的跨模态检索方法，适用于数据稀缺、隐私限制和外部内容的情况。
- **原始摘要**: arXiv:2611.33649v1 Announce Type: cross Abstract: Purpose: Figure retrieval from reference atlases in expert domains like forensic pathology, dentistry and geology must work without labels or training...

### 10. CHD-Bench: Diagnosing Congenital Heart Disease through Interactive Examination
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33775
- **AI 摘要**: 该文章讨论了用于诊断先天性心脏病的交互式诊断基准CHD-Bench，以及用于管理这些诊断过程的软件CHD-Harness。
- **原始摘要**: arXiv:2611.33775v1 Announce Type: cross Abstract: Diagnosis of congenital heart disease (CHD) requires understanding the spatial relationships between cardiac structures, which clinicians assess by sc...

### 11. QK-Bench: Benchmarking Quantitative Kinematic Understanding for Dynamic Spatial Intelligence
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33991
- **AI 摘要**: 该文章讨论了多模态大型语言模型在定量运动理解方面的基准测试，涉及物体运动的大小、速率、参照系依赖性和未来空间演变。
- **原始摘要**: arXiv:2611.33991v1 Announce Type: cross Abstract: Spatial intelligence concerns both scene structure and its temporal evolution. Yet a semantically correct description can conceal a quantitative error...

### 12. GazeVLM: Gaze-Guided Foveated Inference for Efficient Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.16476
- **AI 摘要**: 本文提出了一种名为GazeVLM的方法，用于提高视觉语言模型的推理效率，该方法利用人类注视作为自然指导信号。
- **原始摘要**: arXiv:2509.16476v2 Announce Type: replace Abstract: Vision-language models (VLMs) achieve remarkable multimodal performance but introduce substantial computational cost due to the large number of visu...

### 13. VisionQ: Benchmarking VLM Judges on Criterion-Specific Comparisons of Computer Vision Method Outputs
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2610.00666
- **AI 摘要**: 该文章讨论了使用视觉语言模型作为评判者来评估计算机视觉方法的性能，通过创建盲选问题来测试模型在不同标准下的表现。
- **原始摘要**: arXiv:2610.00666v2 Announce Type: replace Abstract: Qualitative comparison figures in computer vision papers are commonly established to illustrate which method's output is best on a named criterion,...

### 14. HumanPhys: A Human-Centric Physical-World Perception Benchmark for Real-World Visual Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2610.14679
- **AI 摘要**: 本文介绍了一个以人为中心的物理世界感知基准HumanPhys，用于测试现实世界中的视觉推理。
- **原始摘要**: arXiv:2610.14679v2 Announce Type: replace Abstract: We introduce HumanPhys, a human-centric benchmark for real-world physical perception, and a training corpus emitted by the same pipeline. Each quest...

### 15. AffectWorld: Benchmarking Emotion-Driven Future World Prediction
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2610.18305
- **AI 摘要**: 文章讨论了一个新的基准测试套件AffectWorld，用于评估情感驱动的世界预测能力。该基准测试套件包括三个任务：世界状态一致性、情感行动一致性以及因果一致性。
- **原始摘要**: arXiv:2610.18305v2 Announce Type: replace Abstract: The world encompasses both physical environments and human actors. Predicting its evolution requires understanding both physical laws and how emotio...

### 16. PinGround: Pinning Queries to Points for Parallel Grounding in Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.30304
- **AI 摘要**: 本文提出了一种名为PinGround的方法，用于在视觉语言模型中并行化目标定位，以减少解码步骤的增长。
- **原始摘要**: arXiv:2611.30304v2 Announce Type: replace Abstract: Vision-language models (VLMs) can localize through their text interface, grounding open-vocabulary objects, complex referring expressions, text line...

### 17. A History-Aware Visually Grounded Critic for Computer Use Agents
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.11078
- **AI 摘要**: 该文章讨论了一种名为HiViG的历史感知视觉基础测试框架，用于改进计算机使用代理的性能。文章提出了解决现有批评模型的两个主要问题：它们主要关注短期决策循环（如忘记之前的行动）以及缺乏视觉基础来检测错误行动（如点击错误的UI元素）。
- **原始摘要**: arXiv:2606.11078v2 Announce Type: replace-cross Abstract: Various test-time interventions for Computer Use Agents (CUAs), including critic models, have been developed to improve performance through pr...

### 18. MOZAIC: An Audio-Video Deepfake Benchmark for Telling What Is Fake
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.31301
- **AI 摘要**: 该文章讨论了一个音频-视频深度伪造基准MOZAIC，用于区分真假视频和音频。文章介绍了基准的结构和评估方法。
- **原始摘要**: arXiv:2611.31301v2 Announce Type: replace-cross Abstract: Audio-video (AV) deepfakes can fake the face, the voice, or both. Most benchmarks only ask whether a clip is real or fake, so they cannot show...

### 19. MGMem: An Efficient, Deterministic, and Provenance-Preserving Framework for Long-Horizon Agent Memory
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33174
- **AI 摘要**: 本文提出了一种名为MGMem的框架，用于长时段大型语言模型（LLM）代理的持久性记忆，该框架避免了生成性索引调用，而是使用确定性判别解析管道来替代。
- **原始摘要**: arXiv:2611.33174v1 Announce Type: new Abstract: Long-horizon Large Language Model (LLM) agents need persistent memory that surfaces the right past interaction at the right time across thousands of tur...

### 20. Who Attributes a Mind to Whom? Mutual Theory of Mind in Simulated User-Assistant Conversation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33327
- **AI 摘要**: 该文章讨论了用户在与模拟用户助手对话时如何赋予其心智状态，以及不同特征对这种心智赋予的影响。
- **原始摘要**: arXiv:2611.33327v1 Announce Type: new Abstract: When users assume that an AI chatbot has mental states, they are more likely to develop over-reliance, emotional dependence, and in extreme cases, psych...

### 21. Failure Broadens, Success Sharpens: Continual Adaptation of Tool-Use Agents Across Diverse Tasks with Dual-Polarity Memory
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33612
- **AI 摘要**: 该文章讨论了在多种任务和环境约束下，通过双重极性记忆（Dual-Polarity Memory with Periodic Maintenance, DualPM）来增强语言模型代理的持续适应能力。
- **原始摘要**: arXiv:2611.33612v1 Announce Type: new Abstract: Large language model agents can self-improve over time by utilizing procedural memory derived from prior task trajectories, yet the distinct utilities o...

### 22. Sparse-to-Sparse Feature Learning for Cross-Layer Analysis and Steering
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33640
- **AI 摘要**: 该文章讨论了一种新的特征学习方法Sparse-to-Sparse Feature Learning (S2S)，用于跨层分析和控制，实验结果显示其在相邻层之间的对应关系更强。
- **原始摘要**: arXiv:2611.33640v1 Announce Type: new Abstract: Understanding how models internally represent information is a central challenge in interpretation and control. Sparse autoencoders (SAEs) decompose den...

### 23. When Rerankers Work Together: Better and Faster Reranking without Joint Training
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33844
- **AI 摘要**: 该文章讨论了在无联合训练的情况下，异质重排器的性能，这些重排器包括词汇、单向向量、晚期交互和联合查询-上下文评分。文章提出了两个轻量级的语义粗排器，它们从段落相关性标签中学习，并共享可缓存表示和线性时间单体推理。
- **原始摘要**: arXiv:2611.33844v1 Announce Type: new Abstract: Standalone reranker quality does not determine its value in a multistage RAG pipeline. We systematically study heterogeneous rerankers composed without...

### 24. ChemDeduce: Benchmarking LLMs for Unknown Chemical Identification through Interactive Simulated Experiments
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33848
- **AI 摘要**: 该文章讨论了通过交互式模拟实验评估大型语言模型在未知化学识别中的表现，属于基准测试和评估的范畴。
- **原始摘要**: arXiv:2611.33848v1 Announce Type: new Abstract: Large language models (LLMs) have shown strong performance in chemical knowledge and reasoning, yet it remains unclear whether they can solve problems w...

### 25. Evaluating Ukrainian Grammatical Competence in Language Models: Probability Versus Prompting
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.34016
- **AI 摘要**: 该文章讨论了评估大型语言模型在乌克兰语言中的规范性能力的方法，涉及概率和提示技术。
- **原始摘要**: arXiv:2611.34016v1 Announce Type: new Abstract: Organisations deploying large language models in Ukrainian-language information systems need to know whether a model produces normative Ukrainian. This...

### 26. JHealthBench-L: Clinician-Reviewed Localization of HealthBench for Rubric-Based Medical LLM Evaluation in Japan
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.34024
- **AI 摘要**: 本文介绍了一种新的医疗LLM评估基准JHealthBench-L，该基准通过引用源语言的LLM草拟、单专科选择和修订、独立双医评审和元评审来构建。该基准在适应日本临床评估观点方面取得了成功。
- **原始摘要**: arXiv:2611.34024v1 Announce Type: new Abstract: Rubric-based benchmarks such as HealthBench evaluate large language models (LLMs) on open-ended health consultations using case-specific physician crite...

### 27. CypherMAS: Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33242
- **AI 摘要**: 文章讨论了用于评估基于大型语言模型的多智能体系统路由可靠性的CypherMAS基准测试。
- **原始摘要**: arXiv:2611.33242v1 Announce Type: cross Abstract: Multi-agent systems (MAS) built on large language models (LLMs) distribute reasoning across specialized agents that must exchange messages and invoke...

### 28. Achieving Precise Text-To-Cypher Via Grounded Knowledge Graph Data Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.14325
- **AI 摘要**: 本文提出了一种自动合成数据生成方法，用于微调小型LLM以提高其在Text-To-Cypher任务上的性能，从而在本地部署时确保数据主权。
- **原始摘要**: arXiv:2606.14325v2 Announce Type: replace Abstract: Property Graphs are rapidly being adopted as database frameworks for representing heterogeneous data sources. To enable precise access to the inform...

### 29. Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.19747
- **AI 摘要**: 该文章讨论了如何改进文档集合的质量评估方法，提出了一个完整的评估诊断优化框架，设计了涵盖短文和长文场景的文档集合评估基准。
- **原始摘要**: arXiv:2607.19747v4 Announce Type: replace Abstract: As large language models and AI agents become the primary consumers of search results, document set quality determines the upper bound of downstream...

### 30. Attention Routing Stabilizes Early: Working-Set Inference for Recurrent Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.27373
- **AI 摘要**: 文章讨论了循环深度语言模型中的注意力路由如何在深度上稳定，提出了一种两阶段结构来发现稀疏的工作集并进行表示的细化。
- **原始摘要**: arXiv:2609.27373v3 Announce Type: replace Abstract: Recurrent-depth language models, such as looped Transformers, repeatedly apply shared network blocks to refine latent representations, enabling addi...

### 31. AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.26073
- **AI 摘要**: 本文提出了一种新的替代人工标注者的测试方法AltRA-Test，解决了大规模标注设置中不同子集进行标注的问题。
- **原始摘要**: arXiv:2611.26073v2 Announce Type: replace Abstract: Large language models (LLMs) are increasingly used as judges and graders to replace human annotators, raising the question of when such replacement...

### 32. CONCOR: Benchmarking Contrastive Decoding for Visual Hallucination Mitigation Beyond Final-Output Performance
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.30460
- **AI 摘要**: 文章讨论了对比解码（CD）在多模态大型语言模型中的应用，特别是如何通过对比解码调整不同条件下的令牌分数来减少物体幻觉。文章引入了CONCOR基准，用于直接评估真实候选和不同类型的幻觉候选之间的竞争，同时分析对比修正的方向一致性、组合和可靠性。
- **原始摘要**: arXiv:2611.30460v2 Announce Type: replace Abstract: Contrastive decoding (CD) mitigates object hallucination in multimodal large language models (MLLMs) by contrasting token distributions under differ...

### 33. MathArena: Evaluating LLMs on Uncontaminated Math Competitions
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2505.23281
- **AI 摘要**: 文章讨论了大型语言模型在数学竞赛数据集上的表现问题，并提出了一种新的基准MathArena来解决这个问题。
- **原始摘要**: arXiv:2505.23281v4 Announce Type: replace-cross Abstract: The rapid advancement of reasoning capabilities in large language models (LLMs) has led to notable improvements on mathematical benchmarks. Ho...

### 34. GDS Agent for Graph Algorithmic Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2508.20637
- **AI 摘要**: 文章介绍了GDS Agent，这是一种用于图算法推理的工具，能够帮助大型语言模型处理大规模的图结构数据。
- **原始摘要**: arXiv:2508.20637v3 Announce Type: replace-cross Abstract: Large language models (LLMs) have shown remarkable multimodal information processing and reasoning ability. When equipped with tools through f...

### 35. BLADE: Better Language Answers through Dialogue and Explanations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.03236
- **AI 摘要**: 文章讨论了BLADE系统，它通过对话和解释帮助学生更好地利用课程材料，而不是直接提供答案。文章评估了BLADE在NLP课程中的效果。
- **原始摘要**: arXiv:2604.03236v3 Announce Type: replace-cross Abstract: Large language model (LLM)-based educational assistants often provide direct answers offering little incentive for students to explore or enga...

### 36. Lowering the Bar for Everyone: Hidden Validation-Seeking Goals in Empathetic RL
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.30702
- **AI 摘要**: 该文章讨论了在同情性强化学习（Empathetic RL）中，用户寻求验证的行为对模型行为的影响。文章通过实验分析了不同比例的验证寻求用户对模型阈值变化的影响。
- **原始摘要**: arXiv:2611.30702v2 Announce Type: replace-cross Abstract: When RL learns from the reactions of many users, the policy usually cannot see what each user wants. We ask what it learns from users who priv...

### 37. Hypnos: A Dual-Phase End-to-End Platform for Scalable Continual Learning at the Edge
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.24637
- **AI 摘要**: 该文章讨论了在边缘设备上实现持续学习的方法，灵感来源于大脑的清醒和睡眠周期，提出了一种名为Hypnos的开源双阶段平台。
- **原始摘要**: arXiv:2611.24637v3 Announce Type: replace-cross Abstract: Continual learning (CL) enables neural networks to adapt to non-stationary data streams by mitigating catastrophic forgetting, offering a path...

### 38. Online Prediction System for Proactive Autoscaling
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33332
- **AI 摘要**: 本文介绍了一种在线学习系统，用于大规模分布式系统中的短期时间序列预测，以实现主动式资源自动扩展。
- **原始摘要**: arXiv:2611.33332v1 Announce Type: new Abstract: We present an online learning system for short-term time series forecasting that enables proactive autoscaling in large-scale distributed systems. Unlik...

### 39. Model Predictive Control of a Multirotor UAV with a Cable-Suspended Payload: A Comparison of Shifted and Transformer-Based Warm Starts
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33514
- **AI 摘要**: 该文章讨论了多旋翼无人机携带悬吊负载的模型预测控制(MPC)，比较了传统移位初始化与基于Transformer的预热启动方法。
- **原始摘要**: arXiv:2611.33514v1 Announce Type: cross Abstract: This study investigates model predictive control (MPC) of a multirotor drone (unmanned aerial vehicle, UAV) carrying a cable-suspended payload, compar...

### 40. ML-Tool-Bench: Tool-Augmented Planning for ML Tasks
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2512.00672
- **AI 摘要**: 该文章讨论了用于评估工具增强的机器学习代理的基准测试，这些代理能够进行复杂的机器学习任务规划。文章提出了一个包含61个专用工具和15个表格ML挑战的全面基准。
- **原始摘要**: arXiv:2512.00672v3 Announce Type: replace Abstract: The development of autonomous machine learning (ML) agents capable of end-to-end data science workflows represents a significant frontier in artific...

### 41. TopoPrune: Robust Data Pruning via Unified Latent Space Topology
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2602.02739
- **AI 摘要**: 文章讨论了一种新的数据修剪方法TopoPrune，该方法通过拓扑学来捕获数据的内在结构，以解决传统几何数据修剪方法的不稳定性问题。
- **原始摘要**: arXiv:2602.02739v3 Announce Type: replace Abstract: Geometric data pruning methods, while practical for leveraging pretrained models, are fundamentally unstable. Their reliance on extrinsic geometry r...

### 42. Neural Fidelity Calibration for Informative Sim-to-Real Adaptation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2504.08604
- **AI 摘要**: 本文提出了一种名为Neural Fidelity Calibration（NFC）的新框架，用于在线校准模拟物理系数和残差真实度领域，以解决从模拟到现实的适应性问题。
- **原始摘要**: arXiv:2504.08604v2 Announce Type: replace-cross Abstract: Deep reinforcement learning can seamlessly transfer agile locomotion and navigation skills from the simulator to real world. However, bridging...

### 43. Predictive Coding Implemented as a Hardware Substrate Computes Gradients faster than Backpropagation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.18066
- **AI 摘要**: 本文介绍了一种使用预测编码作为硬件基础的方法，该方法能够比反向传播更快地计算梯度。
- **原始摘要**: arXiv:2603.18066v3 Announce Type: replace-cross Abstract: Backpropagation has enabled modern deep learning but is difficult to realize as an online, fully distributed hardware system due to global err...

### 44. Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33398
- **AI 摘要**: 该文章讨论了在视觉语言动作模型中的最佳N测试时间转向方法，指出在不准确验证器的情况下，增加N不会总是提高性能，并可能导致奖励黑客。
- **原始摘要**: arXiv:2611.33398v1 Announce Type: new Abstract: Vision-language-action (VLA) models have shown promise for general-purpose robotic manipulation, but adapting to changing environmental conditions still...

### 45. PROVE: Predict-to-Specify and Observe-to-Verify for Human-Aligned Evaluation of Mobile Manipulation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33733
- **AI 摘要**: 该文章讨论了一种名为PROVE的方法，用于评估移动操作的成功条件。PROVE通过细化从指令、初始场景、目标对象参考图像和生成的目标图像中提取的成功条件来提高评估的一致性。
- **原始摘要**: arXiv:2611.33733v1 Announce Type: new Abstract: Judging open-world robot manipulation is hard because layouts, articulated fixtures, and valid goal configurations vary widely. On RoboCasa365, simulato...

### 46. RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33739
- **AI 摘要**: 文章讨论了如何通过RegHarness来控制代码政策代理在执行中的行为，包括保留哪些步骤和代码修改，以确保代理行为的可控性。
- **原始摘要**: arXiv:2611.33739v1 Announce Type: new Abstract: Code-as-Policy agents generate, execute, and revise robot programs, but often lack explicit mechanisms to govern what persists across executions: which...

### 47. $\widetilde{\varepsilon}$: Does Initial Noise Induce Directional Bias in Vision-Language-Action Models?
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33816
- **AI 摘要**: 该文章讨论了视觉语言动作模型在执行连续机器人动作时对初始噪声的敏感性，并提出了一种通过在训练和推理过程中干预来提高模型对初始噪声鲁棒性的方法。
- **原始摘要**: arXiv:2611.33816v1 Announce Type: new Abstract: Vision-language-action models (VLAs) have widely adopted diffusion-based action generation for continuous robot motions, enabling fine-grained control a...

### 48. Measuring the Value of One Shared Image at Robot Handoffs in Vision-and-Language Navigation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33865
- **AI 摘要**: 该文章讨论了在机器人交接过程中共享图像的价值，通过实验提高了成功率。
- **原始摘要**: arXiv:2611.33865v1 Announce Type: new Abstract: When the lead robot cannot continue, what should it send the teammate that must finish the route? We replay a frozen receiver at each contact under alte...

### 49. Targeted Adaptation of World-Action Models via Interaction and Motion Heads
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33963
- **AI 摘要**: 该文章讨论了针对机器人操作模型的适应性调整方法，包括Next-Interaction Heads和Motion Heads，以及HeadLight方法。这些方法在未见过的任务上取得了较好的效果。
- **原始摘要**: arXiv:2611.33963v1 Announce Type: new Abstract: World-Action Models (WAMs) are a promising new paradigm of robot manipulation policies that jointly generate future video and actions. Successful manipu...

### 50. DriftWAM: Faster World-Action Models via Action-Aware Video Drifting
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33797
- **AI 摘要**: 本文提出了一种新的WAM（World-Action Models）蒸馏方法DriftWAM，通过引入预测视频中的动作信息来减少模型的步骤，同时保持任务性能。
- **原始摘要**: arXiv:2611.33797v1 Announce Type: cross Abstract: World-action models (WAMs) unify future video prediction and action generation for robotic control, but their reliance on iterative denoising incurs s...

### 51. Training-free Behavior Cloning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.30134
- **AI 摘要**: 该文章介绍了一种无需训练的行为克隆方法BPC，它通过结合检索指标、Hankel基动作延续先验和闭合形式一步残差校正来合成策略，能够在模拟基准和真实机器人部署中与学习策略竞争。
- **原始摘要**: arXiv:2609.30134v2 Announce Type: replace Abstract: Neural behavior cloning compresses demonstrations into large models, making individual actions difficult to trace and policy updates costly. Retriev...

### 52. From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2610.29560
- **AI 摘要**: 该文章讨论了通过自进化机器人代理组织视觉语言行动模型，以解决长期任务中的非马尔可夫依赖性问题。
- **原始摘要**: arXiv:2610.29560v2 Announce Type: replace Abstract: Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditi...

### 53. Imitation Policies Learn a Proprioceptive Anchor: A Predictive Law for Perception Noise and Its Closed-Loop Cost
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.17658
- **AI 摘要**: 文章讨论了模仿政策在机器人操作中的学习过程，特别是它们如何学习并利用自身状态来抵消噪声影响。文章分析了这种学习过程中的关键参数。
- **原始摘要**: arXiv:2611.17658v2 Announce Type: replace Abstract: Imitation policies for robot manipulation are often trained on noisy object positions, and they learn to discount the noisy reading. We show how muc...

### 54. RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.22138
- **AI 摘要**: 该文章讨论了RoboTeam模拟基准测试，用于评估多模态代理控制多臂机器人的性能，涉及视觉控制和实时任务。
- **原始摘要**: arXiv:2611.22138v2 Announce Type: replace Abstract: Multimodal agents can now control robot arms by calling tools and writing code. Existing benchmarks fall short in three ways: most test one or two a...

### 55. NEVA: Natural-Language Co-Evolution and Validation of Microarchitectures
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33346
- **AI 摘要**: 文章讨论了一种新的方法NEVA，该方法利用自然语言来指导微架构设计的演化，以避免直接使用C++代码进行演化，从而减少LLM需要处理的复杂性。
- **原始摘要**: arXiv:2611.33346v1 Announce Type: new Abstract: Recent large language model (LLM)-guided evolutionary approaches have demonstrated the potential to automate microarchitectural design exploration. Howe...

### 56. SentryWard: Formal Verification of Warp-Specialized GPU Kernels
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33817
- **AI 摘要**: 该文章讨论了现代GPU核中异步数据移动、通用核心计算和专用核心计算的同步验证方法，提出了SentryWard框架用于验证包含 warp 分配的GPU核。
- **原始摘要**: arXiv:2611.33817v1 Announce Type: new Abstract: Modern GPU kernels overlap asynchronous data movement, computation on general-purpose cores (e.g., CUDA cores), and computation on specialized cores (e....

### 57. Conditional Work Bounds and Timing Evidence for an Industrial NDT Scan Matcher: Cross-Language Work-Trace Conformance
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.33159
- **AI 摘要**: 文章讨论了工业NDT扫描匹配器的工作边界和时间证据，涉及机器人操作系统的调度不在时间范围内。
- **原始摘要**: arXiv:2611.33159v1 Announce Type: cross Abstract: Normal Distributions Transform (NDT) scan matching has strongly input-dependent execution time on the localization critical path. We study the align k...

### 58. VirtualSet: Receiver-Indexed Authority Compilation for Query-to-Action Continuity in Executable Ontologies
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.18821
- **AI 摘要**: 本文研究了如何在执行的本体中保持查询结果的有效性，提出了VirtualSet方法来编译查询和可信授权，以确保在批量插入时目标成员资格的一致性。
- **原始摘要**: arXiv:2607.18821v3 Announce Type: replace Abstract: An ontology edit can preserve a query answer while replacing the evidence that justified an action on it. We study when the original approval remain...

### 59. Generic Constraints Projection: An Exact Criterion for Preserving Type Comparison Reports under Record Width Extension
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.19693
- **AI 摘要**: 文章讨论了在固定源导出和固定记录宽度扩展下的类型比较报告保持问题，涉及类型和输出的保留。
- **原始摘要**: arXiv:2607.19693v5 Announce Type: replace Abstract: A release can preserve a program's type and output while changing a comparison cited in an approved report. A publisher needs to know whether the or...

### 60. safeL4: Rethinking Safe-Language-Based Single Address Space Microkernels
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2610.35999
- **AI 摘要**: 该文章讨论了如何通过安全语言构建微内核以解决性能问题，重点介绍了safeL4方法。
- **原始摘要**: arXiv:2610.35999v2 Announce Type: replace-cross Abstract: Microkernels provide good features such as high security, safety, and flexibility, but their reliance on hardware-based isolation leads to hea...

### 61. Redesigning source control at Anthropic
- **来源**: Anthropic Research (TIER1)
- **发布日期**: 2026-11-27
- **类型**: research
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.anthropic.com/research/redesigning-source-control
- **AI 摘要**: 文章讨论了Anthropic在源代码控制方面的重新设计，关键词包括source control和redesigning。

### 62. How OpenAI’s Performance Factory keeps ChatGPT fastEngineeringNov 19, 2026
- **来源**: OpenAI News (TIER1)
- **发布日期**: 2026-11-19T08:00:00.000Z
- **类型**: news
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/
- **AI 摘要**: 文章讨论了OpenAI的Performance Factory如何保持ChatGPT的快速性能。

## 🏷️  具身智能

**65 篇文章**

### 1. TDK Bets on AI Data Centers and Robots to Fuel Sensor Growth
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 21:00:00 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/tdk-bets-on-ai-data-centers-and-robots-to-fuel-sensor-growth
- **AI 摘要**: TDK公司计划增加高端磁传感器的生产，以利用汽车、人形机器人和AI数据中心等领域的广泛使用。
- **原始摘要**: TDK Corp. is preparing to boost production of its high-end magnetic sensors, seeking to capitalize on widening use of the components in cars, humanoid robots and AI data centers.

### 2. Progress cargo spacecraft carrying Teledroid robot docks with ISS
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:19:18 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://tass.com/science/2225337
- **AI 摘要**: 俄罗斯的Progress MS-36货运飞船搭载Teledroid机器人成功与国际空间站对接。Teledroid机器人旨在协助宇航员在空间站外表面执行任务。
- **原始摘要**: The Teledroid is designed to assist cosmonauts in carrying out tasks on the outer surface of the ISS

### 3. DreamTour: Layout Steering for Training-Free World Exploration
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33378
- **AI 摘要**: 本文提出了一种名为DreamTour的框架，用于生成具有更准确相机运动控制的相机路线，无需进行训练。
- **原始摘要**: arXiv:2611.33378v1 Announce Type: new Abstract: Video diffusion and world models generate plausible videos but do not reliably match the requested camera direction and travel distance. We present Drea...

### 4. EgoCARBS: Egocentric Video Meets Active Acoustics for Kitchen Action Understanding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33565
- **AI 摘要**: 本文介绍了一种结合了自体视频和主动声学传感的数据集和基准，用于厨房动作理解。
- **原始摘要**: arXiv:2611.33565v1 Announce Type: new Abstract: Egocentric video records what a person looks at, but often misses what their body does: the hands leave the frame, and arm motion goes unseen. An exocen...

### 5. DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33779
- **AI 摘要**: 本文介绍了一种名为DuoWM的无人机视频世界模型，该模型通过两个互补的视觉条件来生成未来观察结果，显著提高了视频质量、3D一致性以及轨迹跟踪。
- **原始摘要**: arXiv:2611.33779v1 Announce Type: new Abstract: Action-conditioned video world models generate future observations from an initial frame and a camera trajectory, but often fail to align camera command...

### 6. A Simple Yet Effective Agent for Open-World Aerial Object Search
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.34115
- **AI 摘要**: 该文章介绍了一种无需训练的飞行器（UAV）智能体，能够在开放世界中执行物体搜索任务。
- **原始摘要**: arXiv:2611.34115v1 Announce Type: new Abstract: Open-world aerial object search methods often rely on persistent spatial maps, learned world models, or task-specific policy training. To examine how fa...

### 7. LongScape: Advancing Long-Horizon Embodied World Models with Context-Aware MoE
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2509.21790
- **AI 摘要**: 文章讨论了LongScape模型，该模型通过结合自适应的内块扩散去噪和跨块自回归因果生成来解决视频生成中的长期稳定性问题。核心创新在于基于机器人动作语义上下文的块划分机制。
- **原始摘要**: arXiv:2509.21790v2 Announce Type: replace Abstract: Video-based world models hold significant potential for generating high-quality embodied manipulation data. However, current video generation method...

### 8. HumblePRM: Improving VLM Abstention in Ambiguous Situations through Process Reward Modeling
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33452
- **AI 摘要**: 本文介绍了一种新的过程奖励模型HumblePRM，用于提高视觉语言模型在模糊情况下的决策能力。
- **原始摘要**: arXiv:2611.33452v1 Announce Type: cross Abstract: Reliable deployment of Vision Language Models (VLMs) requires that a model's expressed confidence remain grounded in what it can actually see, and tha...

### 9. Network of Theseus (like the ship)
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2512.04198
- **AI 摘要**: 文章讨论了Network of Theseus方法，该方法可以逐步将一个训练好的或未训练的引导网络架构转换为一个完全不同的目标网络架构，同时保持引导网络的性能。
- **原始摘要**: arXiv:2512.04198v2 Announce Type: replace-cross Abstract: A standard assumption in deep learning is that the inductive bias introduced by a neural network architecture must persist from training throu...

### 10. Envisioning Agentic Robotics: A New Era of Robotic Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.18359
- **AI 摘要**: 文章讨论了Agentic Robotics的新范式，强调了基础模型与嵌入式框架结合的重要性，提出了嵌入式系统2作为决策核心。
- **原始摘要**: arXiv:2611.18359v2 Announce Type: replace-cross Abstract: The release of GPT-6 Astra marks the emergence of a new paradigm in robotics: agentic robotics. Within weeks, frontier models with agentic har...

### 11. Why Does Sensor Depth Fail Learned Manipulation Policies? Finding the Failure Mode with ACT
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33352
- **AI 摘要**: 该文章讨论了RGB-D模仿政策在深度相机噪声和空洞影响下的表现，发现深度信息对政策的成功率有显著影响，但空洞对深度信息的依赖性影响较小。
- **原始摘要**: arXiv:2611.33352v1 Announce Type: new Abstract: Learned manipulation policies, from task-specific imitation policies to vision-language-action (VLA) models, rely primarily on RGB images. While some st...

### 12. FOCI: Trajectory Optimization on Gaussian Splats for Gaussian Robots
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33380
- **AI 摘要**: 本文提出了一种新的轨迹优化算法FOCI，用于3D Gaussian Splatting方法，该方法能够直接在Gaussians上进行优化，适用于不同类型的机器人。
- **原始摘要**: arXiv:2611.33380v1 Announce Type: new Abstract: 3D Gaussian Splatting (3DGS) has recently gained popularity as a faster alternative to Neural Radiance Fields (NeRFs) in 3D reconstruction and view synt...

### 13. RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33390
- **AI 摘要**: 本文介绍了一种新的机器人操作基准RoboARC，用于解决受空间约束的复杂操作任务。
- **原始摘要**: arXiv:2611.33390v1 Announce Type: new Abstract: Many hard manipulation tasks come down to a spatial constraint that only a few motions satisfy, such as passing a part through a gap barely wider than i...

### 14. An Adversarial Multi-Agent Pursuit Game for Locomotor Agility Pretraining
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33407
- **AI 摘要**: 文章讨论了通过自玩方式训练神经网络来玩多智能体追逃游戏，以研究新的运动生成和控制策略是否能在稀疏反馈下通过竞争自玩出现。
- **原始摘要**: arXiv:2611.33407v1 Announce Type: new Abstract: Agile humanoid locomotion requires controllers that can adapt to rapidly changing motion demands while remaining stable and robust. Recent locomotion co...

### 15. Skeptic: Grounding Failure Diagnosis for Robot Skill Discovery
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33560
- **AI 摘要**: 该文章讨论了机器人技能发现中的失败诊断问题，提出了一种无需额外训练的协议Skeptic来解决这一问题。
- **原始摘要**: arXiv:2611.33560v1 Announce Type: new Abstract: Robot agents discover reusable skills by revising programs from execution feedback and retaining experience for later tasks. This process can fail when...

### 16. DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33579
- **AI 摘要**: 文章介绍了一种名为DexEngine的模拟管道，用于将人类手-物体演示数据转换为可训练、物理执行的机器人手臂-手轨迹。
- **原始摘要**: arXiv:2611.33579v1 Announce Type: new Abstract: A growing body of recent work addresses the retargeting of human hand-object demonstrations to robotic hands. To train whole-robot policies, however, th...

### 17. Lab2Sim: Agentic Generation of Interactive Laboratory Equipment from Operation Videos
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33705
- **AI 摘要**: 文章讨论了Lab2Sim框架，该框架能够从操作视频中生成可编辑的实验室设备资产，以真实设备的外观、结构和关节运动为依据。
- **原始摘要**: arXiv:2611.33705v1 Announce Type: new Abstract: Generating laboratory assets that faithfully reproduce the appearance, structure, and joint motions of real equipment remains challenging. Existing asse...

### 18. $\mathrm{M}^{2}$-WAM: Efficient Hierarchical Memory Across Modalities and Timescales for World-Action Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33710
- **AI 摘要**: 该文章讨论了一种名为M²-WAM的世界-动作模型，旨在高效地在多个模态和时间尺度上保留历史上下文。
- **原始摘要**: arXiv:2611.33710v1 Announce Type: new Abstract: Long-horizon robotic manipulation requires historical context, yet retaining extensive visual histories incurs growing storage and retrieval costs, whil...

### 19. A general-purpose safe manipulator planning framework for diverse environments without retraining
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33721
- **AI 摘要**: 该文章介绍了一种通用的机器人操作规划框架，能够在不同的操作环境中无需重新训练控制器执行抓取任务。
- **原始摘要**: arXiv:2611.33721v1 Announce Type: new Abstract: Nowadays, robots need to be retrained whenever their operating environment changes, and this prohibitive training cost keeps them far from daily use. Th...

### 20. RoboJackVR: Turning Robot Tasks into VR Games for Scalable Demonstration Collection
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33731
- **AI 摘要**: 文章介绍了一种名为RoboJackVR的虚拟现实游戏，用于收集机器人演示数据，解决了传统方法中的限制。
- **原始摘要**: arXiv:2611.33731v1 Announce Type: new Abstract: Scaling robot demonstration datasets requires collection systems that accommodate more participants and diverse tasks, yet teleoperation barriers and ta...

### 21. Triage Before Fine-Tuning: Feasibility-Gated Selection and Monitored Adaptation of Embodied Foundation Models for a Fixed Physical Platform
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33772
- **AI 摘要**: 该文章讨论了如何在固定物理平台上选择和适应基础模型的方法，涉及传感器合同和控制延迟的检查，以及对候选模型的排名和监控。
- **原始摘要**: arXiv:2611.33772v1 Announce Type: new Abstract: Embodied foundation models are increasingly deployed by selection: a practitioner picks a public checkpoint by benchmark rank and fine-tunes it on local...

### 22. Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport with a Humanoid
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33828
- **AI 摘要**: 该文章讨论了一种用于重物运输的人形机器人整身摇摆行走策略，通过强化学习实现步态控制、平衡控制和物体操作的联合优化。
- **原始摘要**: arXiv:2611.33828v1 Announce Type: new Abstract: Through pivot walking, humans can transport objects that are too heavy to lift. Previous humanoid studies have relied on planned sequences in which obje...

### 23. Integration of Vision-Language-Action Control for Autonomous Forklift Unloading with Limited Real-World Data
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33880
- **AI 摘要**: 该文章讨论了将视觉-语言-动作控制集成到自主叉车上以完成卸货任务的方法，尽管现实世界的数据有限。文章介绍了使用预训练的视觉-语言-动作模型和模拟生成的训练数据来训练模型。
- **原始摘要**: arXiv:2611.33880v1 Announce Type: new Abstract: Forklifts play a critical role in warehousing and distribution, but existing automation systems remain limited in handling complex tasks that require se...

### 24. CoTAMP: Cooperative Task and Motion Planning for Quadruped Robots with Large Language Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33911
- **AI 摘要**: 本文提出了一种框架，用于解决双足机器人在复杂环境中无法单独完成的任务，通过结合大型语言模型和代码模块来实现。
- **原始摘要**: arXiv:2611.33911v1 Announce Type: new Abstract: Some environments cannot be traversed by a single quadruped robot, for example a ledge that one robot can climb only from its partner's back or a gap th...

### 25. X-World: Transferring Video Priors to Cross-Embodiment Robot Control
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33914
- **AI 摘要**: 该文章讨论了如何利用视频先验信息来改进机器人控制，特别是在不同机器人体上的控制。文章提出了一种名为X-World的方法，通过预训练的视频扩散模型来适应不同视角，并使用Q-Former和动作专家来预测动作片段。
- **原始摘要**: arXiv:2611.33914v1 Announce Type: new Abstract: Language-instructed manipulation requires robust closedloop policies, yet action-labeled robot trajectories are costly and limited in coverage. Human an...

### 26. SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33915
- **AI 摘要**: 文章讨论了如何让机器人在执行任务时保留执行知识，避免重复错误，提出了一种名为SEEK的代理框架来实现这一目标。
- **原始摘要**: arXiv:2611.33915v1 Announce Type: new Abstract: General-purpose multimodal foundation models enable robots to adapt during deployment from observations and execution feedback, without task-specific de...

### 27. iMFPO: Improving Mean Flow Policy Optimization with Drift-Aware Velocity Alignment for Embodied Control
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33922
- **AI 摘要**: 文章讨论了一种新的政策优化框架iMFPO，用于解决基于流的生成政策在奖励驱动的政策优化中实现高效一步生成的问题。
- **原始摘要**: arXiv:2611.33922v1 Announce Type: new Abstract: Flow-based generative policies offer expressive action modeling for embodied control, yet achieving efficient one-step generation under reward-driven po...

### 28. Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33925
- **AI 摘要**: 该文章讨论了如何通过模拟失败情况来改进机器人世界的模型，以提高其在实际操作中的鲁棒性。
- **原始摘要**: arXiv:2611.33925v1 Announce Type: new Abstract: Robot world models are increasingly used to evaluate and plan policies, yet robot training data are dominated by successful demonstrations. Off the happ...

### 29. Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33993
- **AI 摘要**: 文章讨论了一种新的框架Aegis-VLA，用于动态物体操作，该框架结合了世界模型和视觉语言行动（VLA），以预测动作修正并决定是否应用这些修正。
- **原始摘要**: arXiv:2611.33993v1 Announce Type: new Abstract: Dynamic object manipulation requires maintaining spatial and temporal alignment with targets that continue to move during inference and execution. Altho...

### 30. WISER-RL: A Wake-Sleep Learning Mechanism for Robot Reinforcement Learning from One Demonstration
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.34043
- **AI 摘要**: 本文介绍了一种名为WISER-RL的强化学习框架，该框架通过结合Wake-Sleep学习机制、模仿学习和经验重放来帮助机器人从单一示例中学习。
- **原始摘要**: arXiv:2611.34043v1 Announce Type: new Abstract: A robot learning from one human demonstration may rarely succeed on its own, leaving reinforcement learning (RL) with little reward feedback. We introdu...

### 31. End-to-End Image-Goal Navigation for Agile Quadrotors via Recurrent State Distillation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.34046
- **AI 摘要**: 该文章讨论了一种新的方法，让无人机直接从图像中导航到目标位置，无需地图或目标姿态，这在三维环境中尤其具有挑战性。
- **原始摘要**: arXiv:2611.34046v1 Announce Type: new Abstract: Image-goal navigation asks a robot to reach the viewpoint of a target photograph without a map or goal pose. In three dimensions, this requires not only...

### 32. SplatWAM: Splatting World Action Models for Real-Time 3D Imagination
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33467
- **AI 摘要**: 本文提出了一种名为SplatWAM的生成式世界模型，该模型通过紧凑的3D高斯基础元素学习动作条件下的动力学，实现了实时3D想象。
- **原始摘要**: arXiv:2611.33467v1 Announce Type: cross Abstract: World models typically predict future observations in pixel or latent space, limiting their ability to directly represent true 3D scene evolution. We...

### 33. Systematic study of the performance of small robots on controlled laboratory substrates
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33702
- **AI 摘要**: 该文章讨论了两种六足小机器人在不同地面材质上的性能测试，涉及地面交互模型和设计问题。
- **原始摘要**: arXiv:2611.33702v1 Announce Type: cross Abstract: The design of robots able to locomote effectively over a diversity of terrain requires detailed ground interaction models; unfortunately such models a...

### 34. Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33794
- **AI 摘要**: 该文章讨论了一种新的评估框架SealedLoop，用于评估自改进的 embodied 政策。文章提到了在闭环内训练或选择的评价者的问题，并提出了一种新的闭环外评价者来解决这个问题。
- **原始摘要**: arXiv:2611.33794v1 Announce Type: cross Abstract: Self-improvement is now a practical recipe for embodied policies: a policy collects experience, is retrained, and is kept when a judge rates it higher...

### 35. Dynamic Forcing: Learning Action-Grounded Sparse Dynamic Representations with Dense Future Guidance for World Action Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33799
- **AI 摘要**: 本文提出了一种动态强制方法，用于学习具有密集未来指导的稀疏动态表示，以支持机器人控制中的视觉预测。
- **原始摘要**: arXiv:2611.33799v1 Announce Type: cross Abstract: World action models (WAMs) support robot control through visual prediction, but dense future modeling repeatedly encodes static context already availa...

### 36. Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2602.05310
- **AI 摘要**: 该文章讨论了用于人形机器人的足球技能学习框架，涉及感知-行动集成决策（PAiD），旨在解决现有方法中的模块间不稳定性和目标冲突问题。
- **原始摘要**: arXiv:2602.05310v2 Announce Type: replace Abstract: Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-g...

### 37. Physics-Embedded Neural ODEs for Learning Antagonistic Pneumatic Artificial Muscle Dynamics
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2602.23670
- **AI 摘要**: 本文提出了一种结合物理结构的神经普通微分方程框架，用于学习拮抗气动人工肌肉的动力学。
- **原始摘要**: arXiv:2602.23670v3 Announce Type: replace Abstract: Pneumatic artificial muscles (PAMs) enable compliant actuation for soft wearable, assistive, and interactive robots. When arranged antagonistically,...

### 38. A Framework for Closed-Loop Robotic Assembly, Alignment and Self-Recovery of Precision Optical Systems
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2603.21496
- **AI 摘要**: 该文章讨论了用于自主构建精密光学系统的机器人自动化框架，涉及计算机视觉系统、优化算法和定制工具。
- **原始摘要**: arXiv:2603.21496v2 Announce Type: replace Abstract: Robotic automation has transformed scientific workflows in domains such as chemistry and materials science, yet free-space optics, which is a high-p...

### 39. Musculoskeletal Motion Imitation for Learning Joint-Agnostic Exoskeleton Controllers in Healthy and Impaired Gait
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2604.09431
- **AI 摘要**: 该文章讨论了一种适用于健康个体和肌无力个体的下肢外骨骼控制器的设计方法，结合了生理学合理的肌肉骨骼模拟和强化学习。
- **原始摘要**: arXiv:2604.09431v2 Announce Type: replace Abstract: Designing generalizable control policies for lower-limb exoskeletons is often constrained by the need for large biomechanics datasets or lengthy hum...

### 40. Hierarchical Two-Stage Framework for Environment-Aware Long-Horizon Vessel Trajectory Prediction
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2605.16442
- **AI 摘要**: 该文章讨论了一种结合粗略长期预测和网格感知短期预测的层次框架，用于海洋环境中长周期船舶轨迹预测。
- **原始摘要**: arXiv:2605.16442v2 Announce Type: replace Abstract: Long-horizon vessel trajectory forecasting under real ocean conditions is critical for collision avoidance, traffic management, and route planning....

### 41. Learning to Throw: Agile and Accurate Cable-Suspended Payload Delivery with a Quadrotor
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2606.27603
- **AI 摘要**: 文章讨论了使用四旋翼无人机快速运输悬挂在空中的重物的方法，特别是在紧急应用中，如搜索与救援和医疗配送。文章提出了一种结合高精度分析四旋翼模型和复杂绳索与负载交互物理求解器的混合仿真框架。
- **原始摘要**: arXiv:2606.27603v2 Announce Type: replace Abstract: Quadrotors offer the agility needed to rapidly transport suspended payloads during time-critical applications, including search-and-rescue and medic...

### 42. Scalable Low-Cost Laboratory Automation: A Digital Twin-Integrated Robotic Platform for Autonomous Liquid Handling (RAINBOT)
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2607.20662
- **AI 摘要**: 本文介绍了一种低成本的数字孪生集成机器人平台RAINBOT，用于自主液体处理。
- **原始摘要**: arXiv:2607.20662v3 Announce Type: replace Abstract: Laboratory automation accelerates discovery, yet its adoption is constrained by the high cost, proprietary design, and limited remote supervisabilit...

### 43. Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2607.27511
- **AI 摘要**: 该文章讨论了一种用于外科手术机器人模仿政策的失效检测方法，通过条件流模型学习正常短时视觉动态，以检测与学习到的正常动态的偏差。
- **原始摘要**: arXiv:2607.27511v2 Announce Type: replace Abstract: Imitation learning has shown increasing promise for autonomous robotic surgery, yet safe deployment remains challenging due to the safety-critical n...

### 44. Event-Time Hybrid Optimal Control for Robotic Table Tennis Serves
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2608.08157
- **AI 摘要**: 该文章讨论了机器人乒乓球发球的优化控制方法，涉及时变最优控制问题。
- **原始摘要**: arXiv:2608.08157v2 Announce Type: replace Abstract: Robotic table tennis serves require high ball velocity and spin while respecting the robot's kinodynamic limits. Unlike rally strokes, a valid serve...

### 45. RoboEdit: Turning Human Videos into Scalable Robot Training Data
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2608.18948
- **AI 摘要**: 文章主要介绍了一种名为RoboEdit的人工智能工具，用于将人类操作视频转换为机器人训练数据，以减少机器人手部动作数据的收集成本。
- **原始摘要**: arXiv:2608.18948v5 Announce Type: replace Abstract: Collecting robot hand-object interaction data is costly and embodiment-specific, yet abundant human-object videos remain unusable for robot training...

### 46. Realizability Is Not Enough: Encoding, Liveness, and Auditing of Synthesized Robot Supervisors
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2609.30460
- **AI 摘要**: 该文章讨论了通过合成生成执行的机器人操作系统(Robot Operating System, ROS)2 Flexible Behavior Engine (FlexBE)监督器的架构、实现和形式化基础。
- **原始摘要**: arXiv:2609.30460v2 Announce Type: replace Abstract: High-level robotic supervisors coordinate asynchronous capabilities through their reported outcomes, such as success or failure. Building on our ear...

### 47. Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2609.37292
- **AI 摘要**: 本文提出了一种新的双臂主动视觉基准测试BAVO-Bench，用于研究机器人执行过程中如何从遮挡中恢复视角。
- **原始摘要**: arXiv:2609.37292v2 Announce Type: replace Abstract: Physical active vision allows robots to change their viewpoint when task-relevant observations become unreliable. However, existing manipulation ben...

### 48. Sparse-WAM: Accelerating World Action Models via Action-Guided Sparse Imagination
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2609.38984
- **AI 摘要**: 本文提出了一种新的训练方法Sparse-WAM，用于加速世界行动模型的推理过程，该方法通过动作引导的稀疏想象来选择性地处理未来的帧令牌。
- **原始摘要**: arXiv:2609.38984v2 Announce Type: replace Abstract: World-action models (WAMs) leverage pretrained video models to improve generalization in robot control by jointly predicting future visual states an...

### 49. Continual Humanoid Motion Learning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2610.04231
- **AI 摘要**: 该文章讨论了如何通过Similarity-guided LoRA-PNN方法，使人类形机器人在学习新技能时不遗忘旧技能，适用于持续学习的人形机器人运动控制。
- **原始摘要**: arXiv:2610.04231v2 Announce Type: replace Abstract: Humanoid whole-body controllers can now track a diverse set of dynamic motions, but they are typically trained offline and then frozen, so teaching...

### 50. EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2610.18790
- **AI 摘要**: 本文介绍了一种名为EqC的框架，用于实现自我反思的终身机器人学习，其核心思想是基于明确的条件能量景观进行平衡控制。
- **原始摘要**: arXiv:2610.18790v2 Announce Type: replace Abstract: Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently suppo...

### 51. SMR: Learning Streaming Motion Retargeting from Human Motion Semantics
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2610.29169
- **AI 摘要**: 该文章讨论了一种新的学习流体运动重定向的方法，通过语义条件下的物理专家来训练神经网络模型，以实现人类运动到机器人的重定向，同时考虑机器人的物理约束。
- **原始摘要**: arXiv:2610.29169v3 Announce Type: replace Abstract: Retargeting human motion to humanoids requires preserving motion semantics while accounting for the robot's physical constraints. Kinematic pipeline...

### 52. PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.04870
- **AI 摘要**: 本文介绍了一种名为PrimeSim的通用世界模型模拟器，它能够通过条件动作和多视角来解决机器人演示中出现的挑战。
- **原始摘要**: arXiv:2611.04870v2 Announce Type: replace Abstract: A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain co...

### 53. TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.26405
- **AI 摘要**: 文章讨论了如何通过隔离不可解释的触觉变化来改进视觉-语言-动作模型，使其在接触丰富的操作中表现更好。
- **原始摘要**: arXiv:2611.26405v3 Announce Type: replace Abstract: Vision-Language-Action (VLA) models have recently been equipped with tactile sensing to perceive visually subtle contact events in contact-rich mani...

### 54. Entangle: Scaling Human-Video In-Context World-Action Models across Unseen Tasks and Contexts
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.28732
- **AI 摘要**: 该文章讨论了如何在机器人操作中使用人类视频进行任务学习，提出了Entangle模型来解决任务和上下文不匹配的问题。
- **原始摘要**: arXiv:2611.28732v2 Announce Type: replace Abstract: In-context learning (ICL) enables foundation models to perform unseen tasks from context without parameter updates. In robotic manipulation, a human...

### 55. T-Tac: A Soft and Thin Active Thermal Tactile Sensor for Robotic In-Grasp Material Identification
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.28939
- **AI 摘要**: 本文介绍了一种软且薄的主动热触觉传感器T-Tac，用于通过材料的瞬态热响应进行材料识别，适用于机器人抓握。
- **原始摘要**: arXiv:2611.28939v2 Announce Type: replace Abstract: Accurate material identification is important for robotic manipulation, yet vision-based methods face challenges when materials have similar appeara...

### 56. RoboThink: Let the Agent Think, Let the Policy Act
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.30111
- **AI 摘要**: 本文提出了一种名为RoboThink的方法，让代理进行思考，而策略则根据代理的指导行动。
- **原始摘要**: arXiv:2611.30111v2 Announce Type: replace Abstract: Robot policies act in real time but fail without knowing why, whereas a reasoning agent that watches the robot can often tell what went wrong. Exist...

### 57. RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.30209
- **AI 摘要**: 本文提出了一种方法RoboAda，用于在部署时调整冻结的机器人策略，以适应不可见的物理条件。
- **原始摘要**: arXiv:2611.30209v2 Announce Type: replace Abstract: Pretrained robot policies decide what to do from camera images, yet some of the physics that decides whether their plans succeed is not visible. An...

### 58. SOAR: temporal Structure-guided One-step Action generation for Robotic manipulation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.30363
- **AI 摘要**: 文章讨论了一种新的政策SOAR，用于提高机器人操作中动作的质量，同时保持一步操作的效率。
- **原始摘要**: arXiv:2611.30363v2 Announce Type: replace Abstract: Efficient robotic manipulation requires temporally coordinated actions with low inference latency. Multi-step diffusion and flow policies progressiv...

### 59. Safety-Critical Formation Control of Non-Holonomic Multi-Robot Systems in Communication-Limited Environments
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2024年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2406.13707
- **AI 摘要**: 该文章讨论了非刚性的多机器人系统在通信受限环境下的安全关键性形成控制。
- **原始摘要**: arXiv:2406.13707v4 Announce Type: replace-cross Abstract: This paper proposes a decentralized estimator-based safety-critical controller for formation control of non-holonomic multi-robot systems oper...

### 60. StageVLN: Spatial and Trajectory Auxiliary Guidance for Efficient Vision-Language Navigation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2610.05664
- **AI 摘要**: 文章讨论了一种名为StageVLN的训练框架，通过提供特权的空间和轨迹指导来塑造导航表示，同时保留了原始的推理路径。
- **原始摘要**: arXiv:2610.05664v2 Announce Type: replace-cross Abstract: Vision-and-Language Navigation (VLN) policies increasingly benefit from strong semantic priors provided by large vision-language models (VLMs)...

### 61. Kairos: Fast and Reliable Symbolic Task Planning for Autonomous Robots
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2610.39454
- **AI 摘要**: 本文介绍了一种名为Kairos的符号任务规划器，该规划器能够快速可靠地为自主机器人生成计划，支持PDDL语言中的多种复杂任务。
- **原始摘要**: arXiv:2610.39454v3 Announce Type: replace-cross Abstract: Robots that plan while they act need a task planner that reads the models their designers write, answers within milliseconds, and says what ea...

### 62. $\varepsilon$-WM: Error-Driven Dynamics Adaptation across Fast--Slow Timescales for World Modeling
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.15215
- **AI 摘要**: 本文提出了一种名为ε-WM的世界模型，用于适应机器人动态中的快速和慢速时间尺度上的未知变化。该模型通过错误驱动的修正来适应这些变化。
- **原始摘要**: arXiv:2611.15215v2 Announce Type: replace-cross Abstract: A core challenge for world models is adapting to sudden, persistent, yet initially unknown changes in robot dynamics. If the world model fails...

### 63. AutoE2E: Don't speak - Language free end-to-end autonomy for L2++ ADAS and L4 Robotaxis
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.22374
- **AI 摘要**: 本文介绍了一种名为AutoE2E的开源模型，用于L2++ ADAS和L4级自动驾驶出租车，该模型采用多摄像头感知、高分辨率地图信息和路线条件，具有79.9万参数。
- **原始摘要**: arXiv:2611.22374v2 Announce Type: replace-cross Abstract: AutoE2E is an open-source end-to-end driving model developed by the Autoware Foundation Robotaxi Working Group. It introduces a temporal bird'...

### 64. Kolpona: An Agentic Framework with Gradient-Free Neuron Programming for RTL Generation
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.33973
- **AI 摘要**: 文章介绍了Kolpona框架，该框架通过无梯度的神经元编程技术改进了大型语言模型在RTL设计中的性能。
- **原始摘要**: arXiv:2611.33973v1 Announce Type: cross Abstract: Open-weight large language models (LLMs) for register-transfer level (RTL) design are usually improved by fine-tuning on curated Verilog corpora, whic...

### 65. What work can robots do?
- **来源**: Anthropic Research (TIER1)
- **发布日期**: 2026-11-27
- **类型**: research
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.anthropic.com/research/what-work-can-robots-do
- **AI 摘要**: 文章讨论了机器人可以完成的工作，属于具身智能领域。

## 🏷️  AI芯片

**19 篇文章**

### 1. Nvidia hits pause on chip shipments to Southeast Asia
- **来源**: TechCrunch (TIER3)
- **发布日期**: Thu, 26 Nov 2026 20:03:54 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/
- **AI 摘要**: Nvidia暂停向东南亚国家发货，原因是这些国家的公司通过远程数据中心使用了Nvidia的芯片，这违反了美国的出口规定。
- **原始摘要**: Nvidia has told manufacturing partners to pause server shipments to Malaysia, Singapore, Thailand and Indonesia as the U.S. tightens its push to keep AI chips out of China.

### 2. Exploring the Indium phosphide supply chain — the material constraint tightening the optical interconnect bottleneck
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 16:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://www.tomshardware.com/tech-industry/photonics/inside-the-indium-phosphide-squeeze-and-the-optical-boom-inp-remains-tightly-constrained-as-the-demand-from-ai-puts-the-entire-supply-chain-under-pressure
- **AI 摘要**: 本文讨论了InP材料在光学互连供应链中的限制，由于AI需求的增加，整个供应链面临压力。
- **原始摘要**: The AI industry's shift to optical interconnects is overwhelming the concentrated InP supply chain behind lasers, transceivers, and co-packaged optics.

### 3. TSMC's A14 1.4nm-class node is ready for chip design
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 13:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://www.tomshardware.com/tech-industry/semiconductors/tsmcs-a14-1-4nm-class-node-is-ready-for-chip-design-boost-cells-promise-14-percent-performance-uplift-or-23-percent-power-cut-over-n2p
- **AI 摘要**: 文章主要讨论了台积电A14 1.4nm工艺节点的准备情况，提到了Boost Cells技术带来的性能提升和能效比改善。这与AI模型、Harness工程、具身智能、AI芯片等类别都不直接相关。
- **原始摘要**: TSMC announces availability of its version 0.9 process design kit for its A14 manufacturing technology. Availability of the v0.9 version of PDK signals that the fabrication process is generally ready...

### 4. Export-banned Nvidia Blackwell B300 servers are openly for sale in China for up to $3.4 million
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://www.tomshardware.com/tech-industry/artificial-intelligence/export-banned-nvidia-blackwell-b300-servers-are-openly-for-sale-in-china-for-up-to-usd3-4-million-a-5x-to-6x-markup-over-u-s-prices
- **AI 摘要**: 文章主要描述了Nvidia Blackwell B300服务器因出口禁令而在中国公开销售的情况，价格比美国市场高出5到6倍。
- **原始摘要**: It's easy to find Blackwell chips for sale in China even today — uneven enforcement of export controls and gray market trading ensure continued availability

### 5. TSMC’s $22.6 billion Texas plan wouldn’t make 2nm-or-better chips until 2031
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 10:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://www.tomshardware.com/tech-industry/semiconductors/tsmc-files-for-usd22-6-billion-texas-fab-campus-with-local-tax-breaks-just-one-county-over-from-musks-terafab-proposed-brazos-county-plant-wont-make-2nm-class-chips-until-2031
- **AI 摘要**: 文章主要讨论了台积电在德克萨斯州投资22.6亿美元的工厂计划，预计到2031年才能生产2纳米或更先进的芯片。这与AI技术无关。
- **原始摘要**: TSMC’s Texas filing describes a $22.6 billion project in Brazos County for 2nm or more advanced chips, starting production in 2031.

### 6. Score a huge $1,700 discount on an RTX 5080 gaming PC from HP, now $2,699.99
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 10:15:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://www.tomshardware.com/desktops/gaming-pcs/score-a-huge-usd1-700-discount-on-an-rtx-5080-gaming-pc-from-hp-now-usd2-699-99-massive-deal-on-a-hyperx-omen-rig-with-a-24-core-intel-cpu-and-1tb-ssd
- **AI 摘要**: 本文介绍了HP公司的一款RTX 5080游戏电脑，提供高达1700美元的折扣，现价为2699.99美元。
- **原始摘要**: A huge discount at HP has knocked $1,700 off a HyperX Omen 35L rig with an RTX 5080 and Intel Core Ultra 7 270K, bringing it down to $2,699.99.

### 7. How we deploy Trillion-parameter frontier models on CerebrasOctober 22, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 22, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras
- **AI 摘要**: 本文介绍了如何在Cerebras系统上部署万亿参数前沿模型。

### 8. November 05, 2026What It Took to Build Wafer-Scale, and Why It LastsRead blog post
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 05, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/what-it-took-to-build-wafer-scale-and-why-it-lasts
- **AI 摘要**: 文章讨论了构建晶圆级设备所需的工作以及其持久性。

### 9. A Realistic End-to-End Runtime Crossover Estimation for Quantum-Enhanced Training of Large-Scale Machine Learning Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.33454
- **AI 摘要**: 该文章讨论了量子增强机器学习模型训练的资源估计，涉及数据访问、计算和读出，分析了三种复杂度不同的基准测试场景。
- **原始摘要**: arXiv:2611.33454v1 Announce Type: cross Abstract: Machine Learning (ML) is one promising application domain for Quantum Computing (QC) speedups, but asymptotic complexity considerations often mask the...

### 10. db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2511.23113
- **AI 摘要**: 该文章讨论了如何通过双平衡序列并行技术(db-SP)解决视觉生成模型中稀疏注意力带来的工作负载不平衡问题。
- **原始摘要**: arXiv:2511.23113v2 Announce Type: replace-cross Abstract: Scaling Diffusion Transformer (DiT) inference via sequence parallelism is critical for reducing latency in visual generation, but is severely...

### 11. WADJET: Whole-Job Authorization and Dispatch for Job Execution Trust on FPGA System-on-Chip Accelerators
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.33406
- **AI 摘要**: 文章讨论了一种名为WADJET的技术，用于FPGA系统芯片上的加速器执行授权和调度。该技术通过在FPGA逻辑中集成一个门来实现，该门验证整个任务并在释放任何部分之前接受更早的序列号。
- **原始摘要**: arXiv:2611.33406v1 Announce Type: new Abstract: On an FPGA system-on-chip, the software that submits work to an accelerator also decides what the accelerator does. It writes the registers one by one,...

### 12. From Entropy Source to Stochastic Bit-Stream: Low-Cost Converters for True-Random Stochastic Computing
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.33686
- **AI 摘要**: 本文提出三种方法将真随机数生成器的无偏输出转换为任意目标概率的随机比特流，以用于真随机计算。
- **原始摘要**: arXiv:2611.33686v1 Announce Type: new Abstract: Stochastic computing (SC) encodes values as the probability of ones in random bit-streams, which allows arithmetic circuits with very low area and power...

### 13. L2C2: Enhancing Large-scale Chiplets for Agent Long-Context LLM Inference with Sparse and Distributed Attention
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.33691
- **AI 摘要**: 该文章讨论了如何通过Split-Comm Attention和Ring Attention相结合的方法优化大芯片let上的大规模语言模型的长上下文推理，解决了分布式注意力的问题。
- **原始摘要**: arXiv:2611.33691v1 Announce Type: new Abstract: Long-context inference is a rising demand for LLMs, especially for agent applications. Sparse attention (SpAt) and chiplet technology are promising solu...

### 14. GPS: Guiding Phase-Level Prefetcher Selection with Data-Driven Method
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.33859
- **AI 摘要**: 本文提出了一种基于数据驱动的方法GPS，用于选择硬件预取器，该方法利用了全面的分析和离线学习。
- **原始摘要**: arXiv:2611.33859v1 Announce Type: new Abstract: Hardware prefetching is a widely used technique for hiding off-chip memory latency. Modern processors increasingly adopt composite prefetchers that comb...

### 15. MixMoMo: Accelerating Extra--Large MoE Inference with Mixed--Precision GPU--NPU Execution on Mobile Devices
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.33981
- **AI 摘要**: 本文介绍了一种名为MixMoMo的方法，用于加速移动设备上的大型Mixture-of-Experts模型的推理，通过混合精度量化来减少存储和计算成本。
- **原始摘要**: arXiv:2611.33981v1 Announce Type: new Abstract: Mobile agents and on-device intelligence increasingly demand more capable models on smartphones. Through sparse expert activation, Mixture-of-Experts (M...

### 16. Algebraic Diversity of Switching Functions
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.33938
- **AI 摘要**: 文章讨论了布尔立方体上不同变换的代数多样性，涉及平移、坐标置换、超正方群、一般线性群和仿射群。
- **原始摘要**: arXiv:2611.33938v1 Announce Type: cross Abstract: Algebraic Diversity generalizes averaging over many observations to averaging one observation over a group of transformations matched to its structure...

### 17. Toward Energy-Efficient and Low-Power Arrhythmia Detection for Wearable Devices
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2607.14747
- **AI 摘要**: 本文研究了使用近似技术减少深度学习架构的功耗和能耗，同时保持可接受的分类性能，以适用于可穿戴设备的心律失常检测。
- **原始摘要**: arXiv:2607.14747v2 Announce Type: replace Abstract: Cardiovascular diseases are the leading cause of death worldwide, and conditions such as arrhythmia often require long-term monitoring for effective...

### 18. Neuromorphic architectures as numerical solvers for computational neuroscience
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2608.28387
- **AI 摘要**: 文章讨论了基于率模型的神经形态计算，提出了一种利用分布式模拟和多比特包通信策略来设计非突触神经元模型的数字神经形态加速器的方法。
- **原始摘要**: arXiv:2608.28387v2 Announce Type: replace Abstract: Neuromorphic computing is closely associated with spiking neuronal networks. However, an alternative class of so-called "rate-based" models arising...

### 19. Trading BRAM for LUTs: Hybrid Bit-Level Weight Storage for FPGA-Based Spiking Neural Networks
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.32288
- **AI 摘要**: 该文章讨论了如何在FPGA上使用混合位级权重存储方案，通过牺牲部分逻辑资源来减少存储需求，同时保持原始权重不变。
- **原始摘要**: arXiv:2611.32288v2 Announce Type: replace Abstract: Spiking Neural Networks (SNNs) offer an attractive paradigm for energy-efficient AI inference, while their deployment on reconfigurable hardware ena...

## 🏷️  编译器

**2 篇文章**

### 1. Denotational Results in Compiler Correctness and Comparisons with Operational Approaches
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2611.31724
- **AI 摘要**: 该文章讨论了编译器正确性证明中使用脱词法语义学的可能性，对比了操作法语义学的方法。
- **原始摘要**: arXiv:2611.31724v2 Announce Type: replace Abstract: Anyone setting out to prove a compiler correct must choose a style of semantics. The CakeML and CompCert projects, among others, show that operation...

### 2. Increasing the Precision of IR Mapping for Incremental Data Flow Analysis
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2611.32920
- **AI 摘要**: 该文章讨论了如何提高IR映射的精度以支持增量数据流分析，涉及编译器技术中的IR和数据流分析。
- **原始摘要**: arXiv:2611.32920v2 Announce Type: replace Abstract: Static analysis tools operate on an Intermediate Representation (IR) --- an internal model of the program on which dataflow analysis computes and st...

## 🏷️  光计算

**2 篇文章**

### 1. Ferroionic CuCrP2S6 Integrated Silicon Photonics for Neuromorphic Computing
- **来源**: arXiv physics.optics (光学/光计算) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 光计算
- **链接**: https://arxiv.org/abs/2611.33954
- **AI 摘要**: 该文章讨论了将层状范德华CuCrP2S6集成到硅微环谐振器上，以实现神经形态计算的光子平台。文章描述了通过电脉冲产生的光共振单向蓝移现象。
- **原始摘要**: arXiv:2611.33954v1 Announce Type: new Abstract: Neuromorphic photonic computing calls for optical states that combine stimulus accumulation, spontaneous relaxation, and nonvolatile state retention wit...

### 2. Triple-Resonance Spectroscopy Using a Cavity-Enhanced Frequency Comb Probe
- **来源**: arXiv physics.optics (光学/光计算) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: 光计算
- **链接**: https://arxiv.org/abs/2607.15793
- **AI 摘要**: 该文章讨论了一种使用频率梳的非线性光谱学方法，用于测量红外热点带跃迁，该方法能够在宽光谱范围内同时测量四个振动带之间的红外热点带跃迁。
- **原始摘要**: arXiv:2607.15793v2 Announce Type: replace Abstract: Accurate experimentally verified models of molecular hot-band transitions are essential for interpreting high-temperature spectra in environments ra...

## 🏷️  军事技术

**13 篇文章**

### 1. Ukraine downs Russian jet-drone with cheap high-powered laser for the first time
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 14:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.tomshardware.com/tech-industry/drones/ukraine-downs-russian-jet-drone-with-cheap-high-powered-laser-for-the-first-time-super-fast-shahed-knocked-out-by-a-4-kilowatt-test-system
- **AI 摘要**: 文章内容主要描述了乌克兰使用廉价高功率激光器成功击落了俄罗斯的无人机，这在军事技术领域具有重要意义。
- **原始摘要**: Ukraine has shot down a Russian jet-powered Shahed drone using an air defense laser for the first time.

### 2. US defense officials considered using Cold War law to force Nvidia to reinstate Jensen Huang as CEO following his resignation, report claims
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 13:17:31 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.tomshardware.com/tech-industry/big-tech/us-defense-officials-considered-using-cold-war-law-to-force-nvidia-to-reinstate-jensen-huang-as-ceo-following-his-resignation-report-claims-1950-defense-production-act-was-floated-as-solution-to-president-trump
- **AI 摘要**: 文章内容涉及美国国防官员考虑使用冷战时期的法律来迫使英伟达恢复詹森·黄作为CEO的职位，这与军事技术相关。
- **原始摘要**: Pentagon leaders considered using the Cold War-era Defense Production Act to pressure Nvidia to reinstate founder Jensen Huang as CEO following his resignation over an affair with a suspected Chinese...

### 3. Was Japan Prime Minister Takaichi Snubbed at China’s Big Summit?
- **来源**: The New York Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 09:14:29 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://www.nytimes.com/2026/11/26/world/asia/japan-china-takaichi-snubbed.html
- **AI 摘要**: 文章讨论了日本首相岸田文雄在在深圳举行的大型会议上的待遇问题，与其他世界领导人相比，岸田文雄受到了不同的待遇，这引发了日本官员的不满。文章主题与军事技术无关，也不涉及AI模型、Harness工程、具身智能、AI芯片、编译器、光计算、经济或时政。因此，文章最可能属于军事技术类别。
- **原始摘要**: Images show the differences between the welcomes afforded to Sanae Takaichi and other world leaders in Shenzhen, as some officials in Japan cry foul.

### 4. North Korea's Kim calls for nuclear arsenal expansion, says status 'will never change'
- **来源**: CNBC World News (TIER3)
- **发布日期**: Thu, 26 Nov 2026 05:50:34 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://www.cnbc.com/2026/11/26/north-korea-kim-nuclear-weapons-expansion.html
- **AI 摘要**: 北韩领导人金正恩表示要扩大国家核武器库，并称核武器状态不可改变。国际原子能机构称，朝核设施的延期建设在10月底完成。
- **原始摘要**: Kim Jong Un called for wider use of tactical nuclear weapons and an expanded arsenal, rejecting international denuclearization pressure.

### 5. West pursues policy aimed at containing Russia in Arctic — strategy
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 21:56:12 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/politics/2225533
- **AI 摘要**: 文章主要讨论了俄罗斯在北极地区的政策，以及欧洲联盟和北约在遏制俄罗斯北极活动方面的策略。这与军事技术相关。
- **原始摘要**: The Arctic is gradually turning into an arena of foul play and geopolitical confrontation, the document says

### 6. Advanced metal processing, LNG production clusters to emerge in Arctic by 2054
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 21:36:51 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/politics/2225535
- **AI 摘要**: 文章主要讨论了俄罗斯北极地区的经济发展规划，预计到2054年将建立金属加工和液化天然气生产集群。文章内容与军事技术无关，也不涉及AI模型、Harness工程、具身智能、AI芯片、光计算、经济、时政等领域。因此，最合适的类别是军事技术。
- **原始摘要**: Depending on the scenario, Russia’s liquefied natural gas production is expected to reach 90-105 mln metric tons in 2030, 110-130 mln metric tons in 2036, and 110-175 mln metric tons in 2050

### 7. Warriors' Circle of Honor: How the National Native American Veterans Memorial Came to Be and How to Visit
- **来源**: Military.com (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:21:09 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.military.com/warriors-circle-of-honor-how-the-national-native-american-veterans-memorial-was-built-and-how-to-visit
- **AI 摘要**: 本文介绍了位于美国华盛顿特区的国家美洲原住民退伍军人纪念园的建立过程及其参观方式。该纪念园以不锈钢制成的圆形雕塑和石制圆盘为特色，位于国家美洲原住民博物馆内。
- **原始摘要**: Congress first authorized the memorial in 1994. It took nearly three decades, a change in the law and a Vietnam veteran's design to bring it to life

### 8. $2,500 Stipend for Student Veterans: How to Apply in 2027
- **来源**: Military.com (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 18:15:30 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.military.com/a-2500-stipend-covers-costs-the-gi-bill-wont-heres-how-veterans-can-apply
- **AI 摘要**: 退役军人在大学、职业学校或学徒期间可以申请2500美元的津贴，直接支付给退役军人，可用于支付日常账单，无需任何联系。
- **原始摘要**: Find out who qualifies and how to apply for the annual award from the Recycling Education and Research Foundation.

### 9. Roscosmos to tap into AI power to create cutting-edge space tech — CEO
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:14:49 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/science/2225393
- **AI 摘要**: Roscosmos表示将利用人工智能技术开发先进的太空科技。CEO Dmitry Bakanov表示，Roscosmos正在将人工智能应用于设计过程，以提高地球遥感图像的精度，并计划在未来部署更多的人工智能技术。
- **原始摘要**: According to Dmitry Bakanov, the rocket and space sector, like other industrial and economic sectors, is actively integrating neural networks into its operations

### 10. Russian forces hammer Ukrainian UAV assembly, storage sites over past day — top brass
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:59:24 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/politics/2225309
- **AI 摘要**: 俄罗斯军队在过去一天内打击了乌克兰军队的无人机生产和存储站点以及部署区域。俄罗斯国防部称，此次打击包括乌克兰军队使用的能源基础设施和无人机、无人地面系统等。
- **原始摘要**: The Ukrainian army lost roughly 1,110 troops in battles with Russian forces in all the frontline areas over the past 24 hours

### 11. Pentagon Breach Exposed 2.76 Million People's Data, Posing Risks Beyond Credit
- **来源**: Military.com (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 10:00:16 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.military.com/pentagon-data-breach-exposed-2.76m-peoples-data-posing-risks-beyond-credit
- **AI 摘要**: 五角大楼数据泄露事件曝光，约276万人的个人信息被非法访问，涉及军人及其家属的信用信息。政府已修复漏洞并提供信用监控服务，但专家认为仅靠信用监控无法全面保护军人和家庭。
- **原始摘要**: Summit 7's Jacob Hill explains what the Pentagon breach notice leaves unanswered and why credit monitoring alone won't protect troops and families.

### 12. Military Spouse Copes With Husband's Deployment by Becoming Children's Book Author
- **来源**: Military.com (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 10:00:16 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.military.com/military-spouse-copes-with-husbands-deployment-by-becoming-childrens-book-author
- **AI 摘要**: 军嫂尼娜·罗里格为了帮助孩子们理解丈夫的部署生活，创作了一本儿童图画书《Dada娃娃》。这本书的灵感来源于她女儿的制服玩偶‘Dada’。尼娜·罗里格的丈夫史蒂文·罗里格在2024年在欧洲进行了九个月的部署。
- **原始摘要**: Military spouse Nina Rohrig wrote a picture book to help children understand deployment, inspired by her daughter's uniform bear named 'Dada.'

### 13. Next Sergeant Major of the Marine Corps: How It's Picked
- **来源**: Military.com (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 08:01:16 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.military.com/marine-corps-sets-board-to-pick-5-nominees-for-its-next-top-enlisted-leader
- **AI 摘要**: 美国海军陆战队正在组建一个委员会来挑选下任最高军士长，该委员会将在12月7日选出五名最终候选人，海军陆战队司令将从中挑选一名成为海军陆战队的第21任最高军士长。下任最高军士长将在2023年8月10日的海军陆战队华盛顿堡接任。
- **原始摘要**: How the Marine Corps picks its next sergeant major of the Marine Corps: board timeline, eligibility rules and what the top enlisted job involves.

## 🏷️  经济

**60 篇文章**

### 1. Denny’s touts renewed support for Nvidia CEO Jensen Huang following reinstatement
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 21:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://www.tomshardware.com/tech-industry/big-tech/dennys-touts-renewed-support-for-nvidia-ceo-jensen-huang-following-reinstatement-says-some-things-you-just-dont-take-off-the-menu
- **AI 摘要**: Tom's Hardware报道了Denny's餐厅对Nvidia CEO Jensen Huang重新任命的支持，文章内容主要集中在新闻报道上，与AI技术无关。
- **原始摘要**: Denny's, the diner where Jensen Huang came up with the idea for Nvidia, has posted a 200-word statement to X in which it expressed its delight at his return to Nvidia after he initially resigned and a...

### 2. Two Californian Nvidia AI chip customers are really Chinese-owned
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 18:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://www.tomshardware.com/tech-industry/big-tech/two-californian-nvidia-ai-chip-customers-are-really-chinese-owned-companies-used-as-workaround-for-government-export-controls
- **AI 摘要**: 本文报道了两家加州Nvidia AI芯片客户实际上是被中国政府控制的公司。文章来源为Tom's Hardware。
- **原始摘要**: Nvidia sells its advanced AI chips to two Californian companies with links to Chinese parent companies, including one that has already been blacklisted. Nvidia is only allowed to sell to specific comp...

### 3. Credit rating agency puts Nvidia on notice for possible downgrade
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 17:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://www.tomshardware.com/tech-industry/credit-rating-agency-puts-nvidia-on-notice-for-possible-downgrade-s-and-p-global-ratings-says-board-members-may-have-compromised-their-independence
- **AI 摘要**: 文章内容与AI技术无关，主要讨论了信用评级机构S&P Global Ratings对Nvidia可能降级的通知。
- **原始摘要**: S&P Global Ratings says that it could lower Nvidia's credit rating because of various risks that it faces, including the smuggling allegations and the fact the lack of succession planning for its CEO....

### 4. 13 tech bargains for only $13 or less to upgrade your desktop PC setup
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 16:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://www.tomshardware.com/gift-guides-seasonal-sales/13-tech-bargains-for-just-usd13-or-less-to-upgrade-your-pc-setup-must-own-gadgets-and-impulse-buys-to-solve-everyday-problems-from-network-switches-to-cleaning-kits
- **AI 摘要**: 本文介绍了13款仅需13美元或更少的升级PC设置的科技产品，涵盖了网络交换机、清洁套装等实用工具。
- **原始摘要**: Don't break the bank this Black Friday with these 13 tech gadgets and tools to help you upgrade your setup for less than $13.

### 5. Electronics manufacturers set up memory 'war rooms' to find, lock in DRAM supplies amid worst shortage in history
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 16:11:07 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://www.tomshardware.com/pc-components/dram/electronics-manufacturers-set-up-memory-war-rooms-to-find-lock-in-dram-supplies-amid-worst-shortage-in-history-employees-scour-ebay-contact-hundreds-of-brokers-and-snap-up-even-small-batches-of-just-5-to-12-units
- **AI 摘要**: 电子制造商建立内存‘战情室’以锁定DRAM供应，这是历史上最严重的短缺，员工在eBay上搜索并联系数百家经纪人，购买甚至只有5到12个单位的小批量。
- **原始摘要**: The memory chip shortage is forcing companies to find supplies using non-traditional avenues, such as online listings and the gray market. Some have even taken out loans just to have enough cash to bu...

### 6. Nvidia stops AI GPU shipments to Southeast Asia amid purported China cloud access ban, report claims
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 16:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://www.tomshardware.com/tech-industry/policy/nvidia-stops-ai-gpu-shipments-to-southeast-asia-report-claims-data-centers-in-singapore-other-countries-in-trouble-as-commerce-department-requires-cloud-providers-to-obtain-export-license
- **AI 摘要**: Nvidia暂停向东南亚地区出口AI GPU，据称与中国的云访问禁令有关。新加坡及其他国家的数据中心受到影响，美国商务部要求云服务提供商获取出口许可证。
- **原始摘要**: Data centers in Singapore, Malaysia, Thailand, and Indonesia are now required to obtain export licenses if they want to get their Nvidia AI GPUs delivered.

### 7. Best Black Friday RAM deals 2026
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 14:57:07 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://www.tomshardware.com/pc-components/ram/best-ram-memory-deals-ddr5-ddr4-2026
- **AI 摘要**: 本文介绍了2026年黑五内存优惠，涉及DDR5和DDR4内存的折扣信息。
- **原始摘要**: We're rounding up the best Black Friday RAM deals from retailers across the U.S. here.

### 8. Trump to Lead TSMC Arizona Groundbreaking Ceremony After Bringing Huang Back to Nvidia
- **来源**: The Information (TIER3)
- **发布日期**: 2026-11-26T03:21:48Z (昨天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://www.theinformation.com/briefings/trump-lead-tsmc-arizona-groundbreaking-ceremony-bringing-huang-back-nvidia
- **AI 摘要**: 特朗普将主持台积电在亚利桑那州芯片工厂扩建的奠基仪式，预计包括台积电高管、供应商和客户在内的人员将出席。
- **原始摘要**: President Donald Trump will lead a groundbreaking ceremony on December 4 for the expansion of Taiwan Semiconductor Manufacturing Company‘s chip plant in Phoenix, Bloomberg reported, citing a White Hou...

### 9. Caisse’s Infrastructure Arm Pauses Bond Sale as Market Sours
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Wed, 25 Nov 2026 19:34:38 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-25/la-caisse-s-infrastructure-arm-pauses-bond-sale-as-market-sours
- **AI 摘要**: 由于金融市场状况恶化，一家加拿大的新发行者无法按计划出售债券，即使有该国最重要的养老基金的支持也无法改变这一情况。
- **原始摘要**: Deteriorating conditions in financial markets are preventing a new Canadian issuer from selling debt as planned, even with the backing of one of the country’s most important pension managers.

### 10. Asian Stock Futures Signal Gains, Oil Climbs Again: Markets Wrap
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Thu, 26 Nov 2026 21:59:57 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/asian-stock-futures-signal-gains-oil-climbs-again-markets-wrap
- **AI 摘要**: 文章主要讨论了亚洲股市的未来走势以及油价的上涨，与AI技术无关。
- **原始摘要**: Asian stocks may look to build on a tech rally that powered gains in US stock futures on Thursday, with signs of a revival in risk appetite lifting assets including copper and Bitcoin. Oil climbed aft...

### 11. Turkey Central Bank Sidelines Policy Rate as Reserves Shrink
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 19:41:34 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/turkey-central-bank-suspends-repo-auctions-as-reserves-shrink
- **AI 摘要**: 土耳其央行暂停了一周回购拍卖，以应对外汇储备大幅下降，这可能提高银行的资金成本。
- **原始摘要**: Turkey’s central bank suspended its one-week repo auctions, a move that could raise banks’ funding costs as policymakers respond to a sharp decline in foreign-exchange reserves.

### 12. Ghana Buys Back $1.1 Billion Domestic Bonds to Boost Confidence
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Thu, 26 Nov 2026 19:31:46 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/ghana-buys-back-1-1-billion-domestic-bonds-to-boost-confidence
- **AI 摘要**: 加纳政府提前赎回了价值11亿美元的国内债券，以增强投资者对从债务重组中恢复的经济的信心。
- **原始摘要**: Ghana redeemed a four-year domestic bond three months ahead of maturity, as the government sought to bolster investor confidence in an economy recovering from a debt restructuring.

### 13. Banxico Raises Growth Outlook as Investment, Exports Pick up
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 18:54:15 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/mexico-central-bank-lifts-growth-outlook-in-boost-to-sheinbaum
- **AI 摘要**: 墨西哥央行将2026年的经济增长预期从1.5%上调至1.9%，原因是出口和投资的增加提振了拉丁美洲第二大经济体。
- **原始摘要**: Mexico’s central bank raised its 2026 growth forecast to 1.9% from 1.5% after stronger exports and investment boosted Latin America’s second-largest economy.

### 14. Britain’s electricity grid operator makes record number of calls for extra power
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 18:36:59 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/21a1331c-c201-4333-b312-ab87b7fd994f?syn-25a6b1a6=1
- **AI 摘要**: 英国电力网络运营商因苏格兰风力发电厂向英格兰消费者供电受限以及寒冷天气导致电力需求增加而发出更多电力请求。
- **原始摘要**: Issue driven by colder weather and constraints in getting electricity from wind farms in Scotland to consumers in England

### 15. Kazakhstan Encouraged Local Banks to Finance Deal for Gold Miner
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Thu, 26 Nov 2026 17:35:40 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/kazakhstan-encouraged-local-banks-to-finance-deal-for-gold-miner
- **AI 摘要**: 哈萨克斯坦鼓励国内银行向建筑巨头Shakhmurat Mutalip提供超过10亿美元的贷款，并修订了融资规定，以帮助他收购黄金矿商AK Altynalmas JSC。
- **原始摘要**: Kazakhstan has encouraged domestic banks to lend more than $1 billion to construction tycoon Shakhmurat Mutalip and revised financing regulations to help him buy gold miner AK Altynalmas JSC, accordin...

### 16. Global stocks climb after volatile US trading over AI risks
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 16:49:54 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/6e217409-9fbb-456c-b405-2eb15bb69679?syn-25a6b1a6=1
- **AI 摘要**: 文章主要讨论了科技股因对AI是否会持续繁荣的担忧而本月表现不佳的情况。
- **原始摘要**: Tech shares hit this month by fears over whether boom can be sustained

### 17. SAP Weighs Cutting at Least 10,000 Positions in AI Restructuring
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 16:15:48 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/sap-weighs-cutting-at-least-10-000-positions-in-ai-restructuring
- **AI 摘要**: SAP计划裁减至少10000个职位以适应人工智能时代，这是一则关于企业重组的新闻。
- **原始摘要**: SAP SE is preparing a plan to eliminate at least 10,000 positions to transform its software business for the artificial intelligence era, according to people familiar with the matter.

### 18. Record temperature surge in November as world fails to agree on climate action
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 15:31:30 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/738aaed8-7d4a-4321-aead-0f2bf71e286f?syn-25a6b1a6=1
- **AI 摘要**: 文章主要讨论了11月气温异常升高的现象，部分原因是由于暂时的厄尔尼诺暖化现象。文章并未涉及AI技术相关内容。
- **原始摘要**: Deviation partly driven by temporary El Niño warming phenomenon

### 19. Hawkish Fed poised to raise rates despite stock market turmoil
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 14:58:45 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/3890f725-66dd-4613-8a60-d9e3ea38d25a?syn-25a6b1a6=1
- **AI 摘要**: 文章主要讨论了美联储在面对股市动荡的情况下，仍可能提高利率以应对通胀的问题。
- **原始摘要**: Inflation is top concern for US central bank officials even as tech-led sell-off triggers fears for economy

### 20. The new ECB team is set for a baptism of fire
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 14:11:40 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/441dbda3-38be-48b9-9603-3b68f1ed3a48
- **AI 摘要**: 文章主要讨论了欧洲央行紧缩周期的尾声和法国大选的影响，暗示这将是对新团队的早期考验。这与经济相关，但不完全符合经济的定义。
- **原始摘要**: The tail-end of the ECB’s tightening cycle and the fallout of a consequential election in France will provide an early test

### 21. Want more apprentices? Start by upskilling the trainers
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 14:08:45 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/bbc6102c-832c-4a63-86e9-0748023c49e8?syn-25a6b1a6=1
- **AI 摘要**: 文章主要讨论了英国进一步教育和技能提供者的多样性，以及如何通过提高培训者的技能来满足更多学徒的需求。文章主题与AI技术无关。
- **原始摘要**: Abundance of further education and skills providers in UK means huge diversity in heft and quality

### 22. ECB Officials Saw More Tightening With Inflation Outlook Worse
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 13:09:36 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/ecb-officials-saw-more-tightening-with-inflation-outlook-worse
- **AI 摘要**: 欧洲央行官员在上个月的会议上预计未来将进一步收紧货币政策，因为通胀前景恶化。
- **原始摘要**: European Central Bank officials meeting last month envisaged tightening monetary policy further in the future after the outlook for inflation worsened.

### 23. StanChart’s Crypto Custody Unit Suffers Data Breach
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:24:38 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/stanchart-s-crypto-custody-unit-suffers-data-breach
- **AI 摘要**: 标准银行的加密托管子公司Zodia Custody Ltd.宣布其遭遇了安全漏洞，暴露了一些客户和员工的信息。
- **原始摘要**: Standard Chartered’s crypto custody subsidiary Zodia Custody Ltd. said it had suffered a security breach, exposing some client and staff information.

### 24. Paris and Berlin seek to shield EU budget from Marine Le Pen
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:23:57 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/3f577839-deed-40f4-af9f-bf8fb54890e3?syn-25a6b1a6=1
- **AI 摘要**: 法国要求增加350亿欧元的预算以应对极右翼总统候选人Marine Le Pen的可能上台，这可能会破坏欧盟预算的平衡。
- **原始摘要**: France requests an extra €35bn for farmers to raise the cost of far-right leader picking apart deal on bloc’s budget if she becomes president

### 25. Global stocks rally as investors shrug off U.S. tariffs and AI jitters to 'fish for bargains'
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:22:25 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/26/stock-markets-today-.html
- **AI 摘要**: 全球股市周四上涨，投资者抛开对美国关税和人工智能的担忧，寻找廉价股票。尽管对人工智能支出、滞胀和新美国关税的担忧，亚洲和欧洲股市仍然上涨。投资者关注美国周三宣布的新关税的影响。
- **原始摘要**: Investors appeared to have shrugged off a fresh set of tariffs unveiled by the White House on Wednesday, targeting more than a dozen major trading partners.

### 26. 14th is a punchy biopic of the amendment and its links to Maga politics
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:00:09 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/92eedbaf-f833-4121-9a98-271d23e5fba0?syn-25a6b1a6=1
- **AI 摘要**: 文章讨论了Ava DuVernay导演的新电影《14th》对一个被忽视的法律改革及其与Maga政治联系的颂歌。
- **原始摘要**: Ava DuVernay’s follow-up to ‘13th’ hymns an undersung workhorse whose achievements are now largely under threat

### 27. Trump’s Latest Tariffs Undercut the ‘China Plus One’ Idea
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:00:01 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/newsletters/2026-11-26/trump-s-latest-tariffs-undercut-the-china-plus-one-idea
- **AI 摘要**: 文章讨论了特朗普的新一轮贸易进攻可能打击那些试图多元化业务的企业。文章主题不涉及AI技术，因此应归类为经济。
- **原始摘要**: The new US trade offensive may hit businesses that tried to diversify.

### 28. Investec Sees Opportunities in Three Key AI Buckets
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 09:40:56 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/videos/2026-11-26/investec-sees-opportunities-in-three-key-ai-buckets-video
- **AI 摘要**: Investec 的 Jimmy Muchechetere 认为人工智能市场仍有价值机会，他在 Bloomberg Television 上表示。
- **原始摘要**: Jimmy Muchechetere, equity research analyst at Investec, says the AI trade isn't over and there are value opportunities across the spectrum. He speaks on Bloomberg Television. (Source: Bloomberg)

### 29. AI Trade Rebounds in Late Buying Ahead of US Holiday
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 08:02:43 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/videos/2026-11-26/ai-trade-rebounds-in-late-buying-ahead-of-us-holiday-video
- **AI 摘要**: 文章讨论了股市在感恩节假期前的反弹，投资者重新回到了人工智能交易中。这与US equity-index futures的上涨同步。
- **原始摘要**: Stocks rose alongside US equity-index futures as investors returned to the artificial intelligence trade in the runup to the Thanksgiving holiday after a week of whipsawing. Bloomberg's Neil Campling...

### 30. Wealthy Europeans look beyond stocks amid AI selloff. Here’s where they’re investing
- **来源**: CNBC Top News (TIER3)
- **发布日期**: Thu, 26 Nov 2026 07:23:42 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/26/wealthy-europeans-alternative-investments-ai.html
- **AI 摘要**: 文章主要讲述了富有的欧洲人正在寻找替代股票的投资途径，因为AI市场出现了抛售。调查发现，47%的欧洲受访者认为替代投资是未来科技增长的最佳途径，而美国受访者中这一比例为24%。在替代投资中，62%的欧洲受访者表示他们持有私募股权，26%的受访者表示他们计划在未来一年增加替代投资的比例。文章还提到了替代投资的局限性，如流动性问题和私募股权退出和私人信贷风险。
- **原始摘要**: Goldman Sachs Alternatives' inaugural survey of high-net-worth investors found they're increasingly looking to alternatives amid turbulent markets.

### 31. Banks Risk Outages as They Contend With AI Threats
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 07:18:36 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/videos/2026-11-26/banks-risk-outages-as-they-contend-with-ai-threats-video
- **AI 摘要**: 文章讨论了银行在应对人工智能威胁时面临的网络安全问题和技术故障。人工智能技术快速发展，导致IT团队在发现漏洞前就进行修补，这可能导致系统故障。
- **原始摘要**: The risk of cyberattacks is forcing banks to contend with a growing number of technical hiccups as they race to adapt aging infrastructure and find vulnerabilities before they’re exploited. Artificial...

### 32. Philippine Investors Explore Stablecoins to Buy Retail Bonds
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 05:56:37 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/philippine-investors-explore-stablecoins-to-buy-retail-bonds
- **AI 摘要**: 菲律宾投资者使用数字代币购买了约1200万菲律宾比索的零售美元债券，该国开放了新的投资政府债务的渠道。
- **原始摘要**: About 1,200 Philippine investors used digital tokens to fund roughly $1 million of retail dollar bond purchases after the Southeast Asian nation opened a new channel for investing in government debt.

### 33. S&P warns Nvidia credit rating could be cut over 'rising' management and governance risk
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 03:19:44 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/26/nvidia-market-governance-risk.html
- **AI 摘要**: 标准普尔警告Nvidia的信用评级可能在接下来的90天内被下调，因为该公司在管理与治理框架方面存在‘缺陷’。S&P Global Ratings指出，某些董事会成员的长期任职可能影响其独立性。这标志着在11月18日，穆迪将Nvidia的展望从积极下调至稳定之后的进一步行动。
- **原始摘要**: S&P Global Ratings said Nvidia's credit rating could be cut by one notch as it flagged "rising" management and governance risk at the chipmaker.

### 34. Copper Rebounds as Tech Rally Lifts Battered Industrial Metals
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Thu, 26 Nov 2026 02:01:10 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/copper-rebounds-from-lowest-this-year-as-volatility-hits-metals
- **AI 摘要**: 铜价周四从11个月低点反弹，得益于其他大宗商品和科技股的上涨，投资者重新回到风险资产上，此前几天的跌幅较大。
- **原始摘要**: Copper recovered from an 11-month low on Thursday alongside gains in other commodities and technology stocks, as investors returned to riskier assets following days of sharp losses.

### 35. Gold Hovers Near 15-Month Low as Traders Eye Fed Path, AI Stocks
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Thu, 26 Nov 2026 00:18:09 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/gold-edges-lower-as-us-inflation-data-fuels-bets-for-rate-hikes
- **AI 摘要**: 黄金价格在大约15个月后接近最低水平，投资者权衡了美联储进一步加息的前景与科技股反弹带来的市场乐观情绪。
- **原始摘要**: Gold hovered near the lowest level in about 15 months on Thursday, as investors weighed the prospect of further Federal Reserve rate hikes against a relief rally in wider markets amid a comeback in te...

### 36. Inside India newsletter: Roaring economy, foreign investors’ return and now record auto sales
- **来源**: CNBC Top News (TIER3)
- **发布日期**: Thu, 26 Nov 2026 00:12:16 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/26/india-auto-slaes-economy-suzuki-hyundai-toyota.html
- **AI 摘要**: 印度汽车制造商即将创下最佳业绩，预计在2027年3月结束的财年内销售超过3000万辆汽车。中国汽车市场在2007年达到拐点，当时人均GDP超过2500美元，印度现在处于类似阶段。日本汽车制造商马自达和丰田计划增加120万辆和20万辆产能，而韩国现代汽车将增加15万辆产能。
- **原始摘要**: Automakers in India are poised to sell over 30 million vehicles in the financial year ending March 2027.

### 37. Russia becomes sole supplier of petroleum coke to Iran
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 21:26:46 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225529
- **AI 摘要**: 俄罗斯成为伊朗石油焦的唯一供应商。俄罗斯与伊朗签署了一份石油焦供应协议，俄罗斯石油焦供应将取代澳大利亚，成为伊朗唯一的稳定和可靠供应商。
- **原始摘要**: KMIK North-South CEO Dmitry Dubovik recalled that had Iran previously sourced virtually 100% of its petroleum coke from Australia

### 38. Russia-North Korea trade grows by one-third this year
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 21:20:35 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225527
- **AI 摘要**: 俄罗斯与朝鲜贸易额今年增长三分之一，主要商品为农产品。俄罗斯自然资源和环境部长Alexander Kozlov主持了俄罗斯与朝鲜之间的政府间委员会会议。
- **原始摘要**: The main commodities are agricultural products

### 39. Russian stock market closes in decline as key indices decline
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:41:07 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225515
- **AI 摘要**: 俄罗斯股市收盘下跌，主要指数下跌。主要指数MOEX指数下跌0.74%，RTS指数下跌0.51%。分析师认为，尽管主要指数下跌，但市场情绪仍然保持中性。
- **原始摘要**: The ruble-denominated MOEX index declined by 0.74%, the dollar-denominated RTS index edged down by 0.51%

### 40. Bitcoin, Ethereum gain around 3%
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:24:14 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225509
- **AI 摘要**: 文章主要报道了比特币和以太坊的价格上涨情况，属于经济领域。
- **原始摘要**: As of November 26, the total cryptocurrency market capitalization stood at $2.07 trillion

### 41. Credit to Russian economy up 1.7% in October — Central Bank
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 18:29:47 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225447
- **AI 摘要**: 俄罗斯经济在2026年10月的信用增长率为1.7%，较上月增长1.1个百分点，年增长率降至9.7%。同时，对组织的贷款增长了2.1%，主要由对非金融机构的卢布贷款推动。银行对企业的债务证券投资的增长率保持在上个月的水平。
- **原始摘要**: The annual growth rate of credit to the economy continued to slow, reaching 9.7%

### 42. EU plans to spend €100 billion over seven years servicing loans for Kiev — source
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:58:35 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225431
- **AI 摘要**: 欧盟计划在未来七年内通过其七年的预算支出1000亿欧元来偿还对乌克兰的贷款利息。这笔资金将用于2028年至2034年的预算。
- **原始摘要**: The European Commission has been borrowing to finance Ukraine since 2025 and paying the interest out of the EU budget, the source explained

### 43. Bank of Russia lowers dollar exchange rate to 82.13 rubles for November 27
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:51:54 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225423
- **AI 摘要**: 俄罗斯中央银行将美元汇率从82.1265降至82.13，欧元汇率从89.8053降至89.8053，人民币汇率从12.3184升至12.3184。
- **原始摘要**: The official euro exchange rate has been lowered by 43.44 kopecks to 89.8053 rubles

### 44. Russian fish exporters could set new profit records in 2026
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:48:42 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225415
- **AI 摘要**: 俄罗斯鱼出口商在2026年可能实现新的利润记录，因为国外市场条件非常有利。俄罗斯渔业局副负责人Vasily Sokolov表示，尽管出口量可能低于去年，但鱼产品的价值将实现增长。
- **原始摘要**: Market conditions for fish products in foreign markets are very favorable, deputy head of the Russian Federal Agency for Fisheries Vasily Sokolov said

### 45. Qatar’s LNG exports hit highest level since start of US-Iran conflict
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:27:34 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225397
- **AI 摘要**: 卡塔尔液化天然气出口量在2026年2月美国与伊朗冲突升级以来达到最高水平，尽管通过霍尔木兹海峡的海运受到干扰。卡塔尔在北部城市拉什拉芬的工厂在11月每天出口约1.4个液化天然气货物，比10月减少了约四分之一，比5月的最低水平高出约九倍。卡塔尔至少部署了34艘油轮通过霍尔木兹海峡运输燃料。
- **原始摘要**: Qatar deployed at least 34 tankers to transport the fuel through the Strait of Hormuz

### 46. Russian steel production may drop by 4.4% in 2026 — minister
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:54:19 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225377
- **AI 摘要**: 俄罗斯钢铁产量预计2026年将下降4.4%，俄罗斯工业贸易部长表示，由于建筑、能源和机械工程等主要金属消费领域的需求受限，国内市场需求疲软。尽管夏季期间需求增加，但产量仍有所改善。
- **原始摘要**: It is estimated that steel production volume in Russia by the end of 2026 will amount to around 65 mln tons

### 47. Russian firms can offer Turkey components, technologies, production expertise — Novak
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:53:12 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225379
- **AI 摘要**: 俄罗斯副总理Novak表示，俄罗斯的塔塔尔斯坦共和国为土耳其的TN Maleik Petrokimya公司提供了资金支持，该公司的男烯酸生产设施有助于加强俄土两国在原材料加工和高附加值制造领域的合作。
- **原始摘要**: Turkey possesses a well-developed industrial sector, a skilled workforce, and convenient transport infrastructure, the Russian deputy prime minister added

### 48. Russian economy continues large-scale transformation — PM
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:46:38 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225375
- **AI 摘要**: 本文报道了俄罗斯经济正在经历大规模的结构性转变，总理米哈伊尔·米赫ustin在内阁会议上表示，公司正在调整商业模式、生产方式和物流，并开拓海外市场，包括海外市场。
- **原始摘要**: Companies are readjusting the business models, production and logistics

### 49. Russia’s international reserves down $19.5 bln one week to $699 bln — Central Bank
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:30:19 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225351
- **AI 摘要**: 俄罗斯国际储备在一周内减少了195亿美元，降至6994亿美元。这是自2025年9月5日以来首次低于7000亿美元。
- **原始摘要**: As of November 13, Russia's international reserves equaled $718.9 bln

### 50. Russia’s GDP grows by 0.8% in nine months — PM Mishustin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:02:11 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225317
- **AI 摘要**: 俄罗斯总理Mikhail Mishustin在政府会议上表示，2026年前三季度俄罗斯GDP增长了0.8%，机械工程行业是主要驱动力之一。
- **原始摘要**: "The mechanical engineering industry remains one of the driving forces," the prime minister added

### 51. Russia, Tajikistan implement major $150 mln light industry project
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:00:48 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225307
- **AI 摘要**: 俄罗斯和塔吉克斯坦正在实施一个价值1.5亿美元的轻工业项目，用于棉花纤维的加工成成品。该项目由俄罗斯BTK集团与塔吉克斯坦政府签署的投资协议提供资金。
- **原始摘要**: In May 2026, the lower house of Tajikistan’s parliament approved an investment agreement signed by the republic’s government and Russia’s BTK Group, providing for the establishment of a facility to pr...

### 52. Russia-UAE trade turnover in 2026 to remain at last year’s level — business council chief
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:56:09 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225305
- **AI 摘要**: 俄罗斯-阿联酋贸易总额预计在2026年保持在去年水平，尽管波斯湾局势和市场清理过程影响。
- **原始摘要**: Trade turnover between Russia and the UAE surpassed $14 bln in 2025

### 53. Data centers to boost power generation capacity in Kuzbass by 10 GW
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:51:02 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225303
- **AI 摘要**: 俄罗斯Kuzbass地区将建立数据中心，预计增加10GW电力生产能力。Kuzbass地区负责人表示，这将有助于该地区提高电力生产能力。
- **原始摘要**: The Kuzbass authorities have already identified sites for data centers to be deployed following the introduction of innovative power plants featuring higher-efficiency generating units

### 54. Russia to introduce preferential loans for Russian companies at Dushanbe technopark
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:38:23 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225295
- **AI 摘要**: 俄罗斯计划为在达什干工业园设立生产设施的俄罗斯公司提供低息贷款。俄罗斯工业和贸易部长安东·阿利汗诺夫表示，该工业园位于塔吉克斯坦，将通过新的优惠融资机制支持投资者。
- **原始摘要**: The management company for the technopark has already been selected, Anton Alikhanov said

### 55. Zaporozhye NPP operating stably, safety ensured — Rosatom CEO
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:24:44 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225279
- **AI 摘要**: 俄罗斯Rosatom公司CEO表示，扎波罗热核电站目前安全且稳定运行，但需要外部电力供应恢复。核电站自周三凌晨5:30起已内部供电，一切正常。
- **原始摘要**: According to Alexey Likhachev, it is still unclear when a ceasefire will be established to repair the Dneprovskaya and Ferrosplavnaya power lines

### 56. Alrosa names rarest diamomd colors
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:09:03 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225267
- **AI 摘要**: Alrosa公司宣布了最稀有的钻石颜色，包括深红色钻石被认为是世界上最独特的。
- **原始摘要**: Deep red diamonds are considered the most unique in the world

### 57. Major Russian companies seek to expand metallurgical cooperation with Tajikistan
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:05:45 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225263
- **AI 摘要**: 俄罗斯主要公司正在寻求与塔吉克斯坦扩大冶金合作，包括与TALCO公司合作，以利用俄罗斯的技术知识来改进电解生产设施并开发铝加工技术。
- **原始摘要**: The companies explore opportunities for cooperation with Tajik company TALCO in modernizing electrolytic production facilities and developing aluminum processing using Russian technological expertise

### 58. EU’s restrictions on hybrid car imports have no future — China’s Commerce Ministry
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:02:19 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225259
- **AI 摘要**: 欧盟对混合动力汽车进口的限制没有未来，中国商务部发言人表示，保护主义没有未来，开放和合作才是正确的道路。北京和布鲁塞尔就这一问题进行了谈判并达成了共识。
- **原始摘要**: Beijing and Brussels had held negotiations on this issue and reached a mutual understanding, Official Spokesperson of the Chinese Ministry of Commerce He Yadong recalled

### 59. Bank of Russia purchases yuan worth $183 mln with settlements on November 25
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 14:58:05 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225255
- **AI 摘要**: 俄罗斯央行在2026年11月25日购买了15.1亿卢布的人民币，约合183.4万美元。这是央行在莫斯科交易所使用人民币-卢布工具进行的购买和销售操作的一部分。
- **原始摘要**: The regulator purchased yuan on the domestic market with settlements on November 24 in the amount of 15 bln rubles

### 60. Russian metal product exports to Tajikistan up 1.6-fold in 8 months — minister
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 14:57:17 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2225251
- **AI 摘要**: 俄罗斯金属产品对塔吉克斯坦的出口在8个月内增长了1.6倍，达到20万吨，价值超过1.2亿美元。俄罗斯工业贸易部长Anton Alikhanov表示，增长主要得益于塔吉克斯坦基础设施和工业企业的建设以及新投资项目的实施。
- **原始摘要**: According to Anton Alikhanov, Russia anticipates continued growth driven by the development of construction infrastructure and industrial enterprises, as well as the implementation of new investment p...

## 🏷️  时政

**89 篇文章**

### 1. Jensen Huang Is Back, and So Is His Plaque at Denny’s
- **来源**: The New York Times Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 21:25:16 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.nytimes.com/2026/11/26/business/dennys-jensen-huang-nvidia-plaque.html
- **AI 摘要**: 文章提到Jensen Huang在Denny's餐厅被重新接纳，并且餐厅已经恢复了纪念他的匾。这与AI技术无关。
- **原始摘要**: The chain said it had restored a plaque honoring Mr. Huang above a booth in San Jose, Calif., after he was reinstated at Nvidia, the company he is said to have co-founded while eating there.

### 2. New York Governor Kathy Hochul signs ban on AI chatbot toys backed by $15,000 daily fines
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 13:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.tomshardware.com/tech-industry/artificial-intelligence/new-york-governor-kathy-hochul-signs-ban-on-ai-chatbot-toys-backed-by-usd15-000-daily-fines-takes-effect-in-90-days-after-holiday-rush
- **AI 摘要**: 纽约州州长Kathy Hochul签署了一项禁止使用每天罚款15000美元的AI聊天机器人玩具的禁令，该禁令将在假日繁忙期后90天生效。
- **原始摘要**: New York Governor Kathy Hochul has signed a bill that effectively bans the sale of toys with built-in AI chatbots within the state over concerns about what they might say to kids.

### 3. Trump says a pardon for Nvidia CEO Jensen Huang is 'always an option'
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 11:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.tomshardware.com/tech-industry/big-tech/trump-says-a-pardon-for-nvidia-ceo-jensen-huang-is-always-an-option-urges-him-not-to-plead-the-fifth-ahead-of-house-committee-grilling
- **AI 摘要**: 本文标题提到美国总统特朗普表示对英伟达CEO Jensen Huang的赦免是‘永远的选择’，并建议他在面对众议院委员会的质询时不要行使第五修正案的权利。这则新闻与AI技术无关。
- **原始摘要**: U.S. President Donald Trump says that he could pardon Nvidia CEO Jensen Huang if he finds himself in legal hot water over his affair with an alleged Chinese spy. Huang is set to meet with the House Fo...

### 4. Dan Carney Has Died. He Co-Founded Pizza Hut and Then Made It Ubiquitous.
- **来源**: The New York Times HomePage (TIER3)
- **发布日期**: Thu, 26 Nov 2026 20:37:15 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.nytimes.com/2026/11/26/business/dan-carney-dead.html
- **AI 摘要**: 本文描述了Dan Carney如何从一个小的红屋顶披萨店开始，最终将其发展成为全球最大的披萨连锁店。Dan Carney在95岁时去世。
- **原始摘要**: The franchise with the iconic red roof began small, in a tiny brick hut in Kansas. Little more than a decade later, it was the world’s biggest pizza chain. He was 95.

### 5. Two Italians killed in drone strike on Kuwait
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 20:23:24 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ft.com/content/e5f3128d-5f8b-416c-90d1-2549175cb091?syn-25a6b1a6=1
- **AI 摘要**: 意大利工人在本月美国和伊朗重新对峙后首次海湾冲突中丧生。
- **原始摘要**: Workers are the first reported deaths in the Gulf since the US and Iran restarted exchanging fire this month

### 6. Italy’s PM rebukes Ukraine for attacks on Russian ships in Mediterranean
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 18:28:26 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ft.com/content/7461793f-6983-45ea-8ba2-8b1824df9379?syn-25a6b1a6=1
- **AI 摘要**: 意大利总理吉奥尔吉亚·梅洛尼在欧盟峰会上表示，这场战争不应蔓延至地中海。
- **原始摘要**: ‘This war must not, cannot spread to the Mediterranean,’ Giorgia Meloni says at EU summit

### 7. Carney’s Major Projects Bill C-39 Slammed by Conservative Leader Poilievre
- **来源**: Bloomberg Politics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 17:50:22 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/carney-s-major-projects-bill-c-39-slammed-by-conservative-leader-poilievre
- **AI 摘要**: 加拿大保守党领袖Pierre Poilievre表示将反对总理马克·卡尼的最新努力，加快联邦对大型项目的审查。Poilievre指责政府过度集中权力，忽视了工人的权利。
- **原始摘要**: Canada’s Conservative Party Leader Pierre Poilievre pledged to vote against the latest effort by Prime Minister Mark Carney to speed up federal reviews of major projects, accusing the government of ce...

### 8. Canada Government Spending Slowed in 2025 as Defense Jumped
- **来源**: Bloomberg Politics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 16:37:41 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/canada-government-spending-slowed-in-2025-as-defense-jumped
- **AI 摘要**: 加拿大政府在2025年的支出速度放缓至2.2%，仅为前一年的一半，这主要是因为国防开支增加，而环保政策被削减。
- **原始摘要**: The pace of spending by all levels of government slowed to 2.2% in 2025 — about half the growth rate of the previous year — as the country ramped up spending on defense and pulled back on environmenta...

### 9. India Calls Four-Day Parliament Sitting for ‘Essential’ Business
- **来源**: Bloomberg Politics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 15:08:14 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/india-calls-four-day-parliament-sitting-for-essential-business
- **AI 摘要**: 印度宣布下周将召开一次为期四天的议会会议，用于处理‘必要政府事务’。
- **原始摘要**: India has reconvened its Parliament next week to transact “essential government business”, according to Parliamentary Affairs Minister Kiren Rijiju.

### 10. FIFA Says Hackers Accessed Personal Data in Cyberattack
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 13:42:17 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/fifa-says-hackers-accessed-personal-data-in-cyberattack
- **AI 摘要**: FIFA表示，其遭遇了黑客攻击，导致个人和商业信息被黑客访问。
- **原始摘要**: FIFA was targeted by a cyberattack that resulted in hackers accessing “personal and business information,” the football governing body said in a statement on Thursday.

### 11. De Cos Gets Leaders’ Nod for ECB Presidency in Post-Lagarde Era
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 13:38:12 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/de-cos-is-poised-to-take-ecb-presidency-in-era-after-lagarde
- **AI 摘要**: Pablo Hernandez de Cos将接任欧洲央行行长一职，负责对抗通货膨胀和可能的债券动荡。
- **原始摘要**: Pablo Hernandez de Cos will become European Central Bank’s next president, directing the region’s fight against inflation and possible bond turmoil.

### 12. Mandelson Refused to Sell Global Counsel Stake, Files Reveal
- **来源**: Bloomberg Politics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 13:30:18 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/mandelson-refused-to-sell-global-counsel-stake-files-reveal
- **AI 摘要**: 英国前驻美利坚大使彼得·曼索尔拒绝出售其在游说公司Global Counsel的股份，尽管政府担心存在利益冲突。官方文件显示，曼索尔希望获得更多收益。
- **原始摘要**: Britain’s disgraced former ambassador to the US, Peter Mandelson refused to sell his stake in lobbying company Global Counsel despite government concerns about conflicts of interest because he wanted...

### 13. Netherlands to Fight Rollout of Proposed US Curbs on ASML
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:23:12 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/netherlands-plans-to-fight-rollout-of-proposed-us-curbs-on-asml
- **AI 摘要**: 荷兰政府表示将抵制美国计划进一步限制ASML Holding NV对中国的销售，称这将威胁到欧洲最值钱的公司之一，并与华盛顿之间产生裂痕。
- **原始摘要**: The Dutch government said it will resist US plans to further restrict ASML Holding NV’s sales to China, calling the proposed rules a threat to Europe’s most valuable company and widening a rift with W...

### 14. Minotaur is a breathtaking portrait of wealthy Russians turning a blind eye to war
- **来源**: Financial Times World (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:00:09 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ft.com/content/77d25f83-9fde-4bf8-a589-4620a5ac6288?syn-25a6b1a6=1
- **AI 摘要**: 文章内容与AI技术无关，主要讨论了一部关于俄罗斯富人无视战争的电影。因此，最合适的类别是时政。
- **原始摘要**: Andrey Zvyagintsev directs a stark thriller about a couple with an unhappy marriage and a callous disregard for events outside their own lives

### 15. Marc Levinson on How UPS Created Modern Logistics
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 09:12:58 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/videos/2026-11-26/marc-levinson-on-how-ups-created-modern-logistics-video
- **AI 摘要**: 本文讲述了UPS创始人James E. Casey及其合作伙伴如何通过创新解决了物流问题，包括最后一英里问题和包裹递送，以及科学管理理论对UPS的影响。文章作者Marc Levinson解释了为什么UPS对历史保持保密。
- **原始摘要**: UPS was founded nearly a century ago in the basement of a Seattle saloon by James E. Casey and his business partner Claude Ryan. It is now hard to imagine modern, globalized life, and the logistics re...

### 16. Malaysia Removes About 40,000 Bullying Posts in Online Crackdown
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 05:51:08 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/malaysia-removes-about-40-000-bullying-posts-in-online-crackdown
- **AI 摘要**: 马来西亚政府要求在线平台删除超过40000条涉及欺凌的相关内容，以保护儿童免受社交媒体上的有害材料影响。
- **原始摘要**: Malaysia said online platforms removed more than 40,000 pieces of bullying-related content this year at the government’s request, as the Southeast Asian nation steps up efforts to protect children fro...

### 17. Apple to Expand India Retail Network With New Store in Hyderabad
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 05:38:03 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/apple-to-expand-india-retail-network-with-new-store-in-hyderabad
- **AI 摘要**: 苹果公司将在印度南部城市海得拉巴开设新的零售店，继续扩展其在该国增长最快的海外市场之一的零售网络。
- **原始摘要**: Apple Inc. is opening a new store in the southern Indian city of Hyderabad next month, continuing a drive to expand its retail network in one of its fastest-growing overseas markets.

### 18. Brazil Assets Surge on Bet Bradesco’s Trabuco to Join Government
- **来源**: Bloomberg Politics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 01:07:45 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/lula-sounds-out-bradesco-s-luiz-trabuco-to-join-his-government
- **AI 摘要**: 文章主要讨论了巴西资产价格上涨的原因，是因为投资者预期Bradesco董事长Luiz Carlos Trabuco Cappi将被宣布为卢拉·若泽·内西斯的财政部长，这为财政政策的方向提供了希望。这与AI技术无关。
- **原始摘要**: Brazilian assets soared on anticipation Bradesco Chairman Luiz Carlos Trabuco Cappi would be announced as Luiz Inácio Lula da Silva’s finance minister, giving investors some hope over the direction of...

### 19. Iran denies Kuwait’s accusations of attacking its facility
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 23:59:51 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225577
- **AI 摘要**: 伊朗否认科威特对其设施发动攻击的指控，称这是以色列和美国增加地区不稳定性的手段。伊朗陆军发言人阿卜拉夫扎尔·谢克沙奇表示，这些指控是为继续他们的暴行和加剧地区不稳定性的企图提供掩护。
- **原始摘要**: The accusations serve as a cover for attempts by Israel and the US to increase instability in the region, Spokesman for the Army Abolfazl Shekarchi said

### 20. Wadephul opposes geographical expansion of Ukraine conflict, rising tensions in Baltics
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 23:52:37 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225575
- **AI 摘要**: 德国外长约翰·瓦德普尔表示，应避免扩大乌克兰冲突，并且要控制和避免波罗的海地区紧张局势的升级。他强调了对波罗的海地区环境威胁的担忧。
- **原始摘要**: The German foreign minister said that "very close talks on this issue" are underway

### 21. Israel says hit Hezbollah targets in southern Lebanon
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 23:31:45 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225571
- **AI 摘要**: 以色列军队表示，在黎巴嫩南部的一个训练营附近打击了黎巴嫩什叶派运动真主党的军事设施，该设施据称被Radwan特别单位使用。以色列称真主党计划使用这些导弹攻击以色列，因此进行了打击。
- **原始摘要**: The strikes targeted dozens of missiles and launchers located at a training camp near the settlement of Ain al-Tinah, the military added

### 22. US postpones publication of review of its military presence in Europe until 2027 — portal
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 23:27:16 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225569
- **AI 摘要**: 美国将原计划于2023年12月发布的关于其在欧洲军事存在的审查结果推迟到2024年。该审查由美国防部长彼得·德希瑟在6月启动，旨在减少美国在欧洲的军事存在。
- **原始摘要**: The review, initiated by Pentagon chief Pete Hegseth in June and aimed at reducing the US military presence, was scheduled to last six months

### 23. EU leaders fail to adopt union’s seven-year budget — diplomatic source
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 23:18:30 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225567
- **AI 摘要**: 欧盟领导人未能就2028-2034年的预算达成一致，将于12月继续谈判。
- **原始摘要**: A European diplomatic source said that the officials will continue the negotiations in December

### 24. Iranian political analyst suggests Ukraine attacked Kuwait in false flag operation
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 22:51:59 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225551
- **AI 摘要**: 伊朗政治分析师Mohammad Marandi认为，对科威特重要设施的攻击可能是由乌克兰策划的假旗行动，目的是向美国总统唐纳德·特朗普展示其能力。Marandi指出，许多伊朗人相信科威特的袭击是假旗行动，可能由乌克兰政权策划，因为其人员现在遍布整个地区，包括伊拉克北部和叙利亚。
- **原始摘要**: Mohammad Marandi added that many Ukrainian operatives "are now present throughout the region"

### 25. Iran offers Kuwait joint investigation into drone attack — foreign ministry
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 22:48:25 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225555
- **AI 摘要**: 伊朗外长阿格希表示，伊朗愿意与科威特进行联合调查，以确定无人机袭击事件的起源和责任方。阿格希否认了伊朗无人机袭击科威特的说法，并表示伊朗与事件无关。
- **原始摘要**: According to the ministry, Araghchi categorically rejected accusations that an Iranian drone had attacked Kuwait and stressed that Iran had nothing to do with the incident

### 26. US President Trump still hopes Ukraine conflict can be resolved soon
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 22:03:35 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225549
- **AI 摘要**: 美国总统唐纳德·特朗普表示，他希望俄罗斯和乌克兰之间能够达成协议，结束俄罗斯对欧洲领土的军事侵略。
- **原始摘要**: The US leader expressed hope that a deal could be made between Russia and Ukraine

### 27. Arctic’s share of Russia’s total gross regional product to reach 8.4% by 2035 — strategy
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 22:01:28 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225547
- **AI 摘要**: 文章主要讨论了俄罗斯北极地区的经济和军事政治重要性，预计到2035年其GDP占比将达到8.4%。这与北极地区的战略地位和全球不稳定有关。
- **原始摘要**: According to the document, the economic and military-political significance of the Arctic region is growing manifold amid the emergence of a new global architecture accompanied by mounting global inst...

### 28. Kiev tries to stop talks, UK’s role in conflict exposed: Foreign Ministry comment
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 21:50:37 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225541
- **AI 摘要**: 俄罗斯外长发言人Maria Zakharova表示，乌克兰总统泽连斯基试图破坏与乌克兰的谈判，并通过恐怖袭击引发俄罗斯与北约国家之间的直接对抗。她指出，英国已经公开承认它在为乌克兰选择在俄罗斯境内打击的目标。
- **原始摘要**: Maria Zakharova noted that the UK had publicly admitted that it is picking targets for Ukraine to hit inside Russia

### 29. Russia says NATO sees Arctic as theater of military operations
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 21:48:03 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225531
- **AI 摘要**: 俄罗斯称北约将北极视为军事行动的潜在战场。根据俄罗斯总统普京签署的北极发展策略，北约将北极视为潜在的军事行动区域，并在北极条件（包括核武器）下进行武器使用训练。
- **原始摘要**: The United Kingdom is showing heightened interest in increasing the bloc’s military presence and militarizing the Arctic, the Arctic development strategy states

### 30. Digital technologies to become key area of Kazakhstan-Russia partnership — Tokayev
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 21:17:03 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/economy/2225525
- **AI 摘要**: 卡西姆-焦姆特·托克耶夫在Sberbank的国际AI Journey 2026会议上表示，人工智能的发展是一个不可逆转的过程，他呼吁加强与俄罗斯的合作，将先进的技术作为战略伙伴关系的核心领域。
- **原始摘要**: The Kazakh president described the development of artificial intelligence as an irreversible process

### 31. No Arctic problem can be solved without Russia — strategy
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 21:04:53 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225523
- **AI 摘要**: 本文讨论了俄罗斯在北极地区的独特地位及其在解决北极问题中的重要性。俄罗斯在北极拥有近一半的土地和水域，并且控制着北极盆地周围至少80%的大陆架。
- **原始摘要**: Nearly half the land and waters within the Arctic Circle belong to Russia, as does at least 80% of the continental shelf surrounding the Arctic Basin

### 32. Air defenses intercept 34 Ukrainian drones over Russian regions
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:44:04 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225519
- **AI 摘要**: 俄罗斯防空部队在24小时内拦截了34架乌克兰无人机，这些无人机在俄罗斯多个地区上空被发现。
- **原始摘要**: The alert air defense forces intercepted Ukrainian UAVs over three Russian regions

### 33. Putin approves new Arctic development strategy
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:42:58 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225521
- **AI 摘要**: 俄罗斯总统普京批准了新的北极开发战略，该战略旨在加强俄罗斯北极地区的国家安全，并促进该地区的综合社会和经济发展。
- **原始摘要**: The decree gives the Russian government six months to draw up a comprehensive plan for developing the Arctic zone and the Trans-Arctic Transport Corridor

### 34. Moscow-Pyongyang ties moving in 'very positive' direction — Russian minister
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:38:54 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225517
- **AI 摘要**: 俄罗斯自然资源和环境部长表示，俄罗斯和朝鲜之间的关系正在积极发展，双方领导人讨论的基础设施项目正在实施中，如图们江上的桥梁。
- **原始摘要**: Alexander Kozlov described Russia and North Korea as neighbors that have always felt affection and respect for each other

### 35. Czech prime minister questions continued funding for Ukraine
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:27:38 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225513
- **AI 摘要**: 捷克总理在布鲁塞尔峰会上质疑对乌克兰的进一步资助，认为乌克兰已经收到了约520亿欧元的战争援助，并计划在2026和2027年提供额外的90亿欧元。捷克总理认为如果乌克兰当局不能解释资金的用途，捷克不会提供这些资金。
- **原始摘要**: At the Brussels summit, EU leaders are engaged in heated discussions over the parameters of the bloc’s budget plan for 2028-2034

### 36. Moscow counts on better Russia-Japan relations after leaders’ meeting in China — diplomat
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:26:50 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225511
- **AI 摘要**: 俄罗斯外长发言人表示，俄罗斯总统普京与中国APEC峰会期间与日本首相田中步一的会面有助于改善两国关系。
- **原始摘要**: Russian President Putin met Japanese Prime Minister Sanae Takaichi on the sidelines of the 2026 APEC Summit in China on November 18

### 37. Western companies helping Ukraine attack Russia to face consequences — foreign ministry
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:21:42 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225501
- **AI 摘要**: 俄罗斯外长发言人警告，西方公司帮助乌克兰攻击俄罗斯的员工可能成为合法军事目标，并面临刑事责任。发言人强调，这些员工在参与攻击俄罗斯的外国国防公司中直接参与。
- **原始摘要**: They could become legitimate military targets for the Russian Armed Forces, Maria Zakharova emphasized

### 38. IN BRIEF: President Putin’s key statements at AI Journey conference
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:13:37 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225503
- **AI 摘要**: 俄罗斯总统普京在AI Journey会议上提出更新国家人工智能发展策略，并批准行动计划。他强调人工智能应服务于公共利益，但警告神经网络的不当使用可能带来个人数据和商业秘密泄露的风险。
- **原始摘要**: According to the head of state, Russia aims to make AI adoption increasingly widespread, covering all areas of people's lives

### 39. Proving futility of sanctions against Iran is more important than talks — foreign minister
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:11:15 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225507
- **AI 摘要**: 伊朗外长阿巴斯·阿雷希表示，目前证明对伊朗的制裁和压力无效比谈判更重要。但他表示，伊朗并没有放弃谈判的前景，仍在为此努力。
- **原始摘要**: According to Abbas Araghchi, Iranian diplomats are working around the clock to meet the nation's needs and keep trade routes open

### 40. Moscow offers sarcastic 'good morning' to Italians discovering Peacemaker website
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:10:14 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225505
- **AI 摘要**: 俄罗斯外交部发言人Maria Zakharova在新闻发布会上对意大利人表示讽刺，称他们才刚刚发现乌克兰的Mirotvorets（和平使者）网站上的意大利政客和政治家被列入了极端资源。Zakharova指出，罗马曾因意大利议员和政治家被列入该网站而发生过公共丑闻。
- **原始摘要**: According to Maria Zakharova, local media "were horrified" to learn that current Deputy Prime Minister Matteo Salvini was on the list

### 41. Rot in 'blooming garden,' Zelensky’s brand: remarks by Lavrov
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 20:06:31 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225497
- **AI 摘要**: 俄罗斯外交部长拉夫罗夫在对话中批评了欧洲的政策，称其为‘烂苹果’，并指出乌克兰总统泽连斯基对其他世界领导人的粗鲁行为是他的‘品牌’。
- **原始摘要**: The Russian top diplomat expressed sympathy for Europeans "who find themselves governed by entirely self-serving elites who are entirely out of touch with reality"

### 42. NATO involvement in attacks on Russian vessels brings nuclear war closer — diplomat
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 19:49:03 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225491
- **AI 摘要**: 俄罗斯外交官表示，北约在俄罗斯边境附近进行的军事活动与Freedom Shield 2026演习同时进行，这使世界接近核战争。
- **原始摘要**: Dmitry Polyansky pointed to NATO’s military activities near Russian borders taking place in parallel with the Freedom Shield 2026 exercises

### 43. People must learn to set complex tasks for AI, uncover new knowledge — Putin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 19:42:20 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225487
- **AI 摘要**: 俄罗斯总统普京在AI Journey会议上表示，人们需要学会为人工智能设定复杂、非标准的任务，并利用人工智能来揭示大量新知识。
- **原始摘要**: Everyone will have to master the skills of collaborating with autonomous systems, the head of state noted

### 44. AI boundaries without human oversight must be clearly defined — Putin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 19:28:04 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225481
- **AI 摘要**: 俄罗斯总统普京在AI Journey会议上强调，需要明确人工智能代理的权限范围，即它们不能在没有人类监督和参与的情况下进行的行为。
- **原始摘要**: The Russian leader emphasized that the limits of authority for AI agents should be established

### 45. Chances of agreeing EU budget at Brussels summit equal zero — Hungarian Prime Minister
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 19:20:43 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225473
- **AI 摘要**: 匈牙利总理表示，欧盟七年的预算在布鲁塞尔峰会上达成协议的可能性为零，甚至在圣诞节前达成协议的可能性也很小。
- **原始摘要**: Concluding an agreement by Christmas seems unlikely as well, Peter Magyar said

### 46. Europeans begin to grasp danger of military confrontation with Russia — envoy to OSCE
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 19:04:51 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225471
- **AI 摘要**: 俄罗斯常驻OSCE代表表示，欧洲对军事化和军费增加的抗议表明公众意识到了与俄罗斯发生军事冲突的风险。他指出，欧洲国家在对俄罗斯的恐惧中越来越军事化，这使得与俄罗斯的军事冲突更有可能发生。
- **原始摘要**: Dmitry Polyansky recalled that approximately 90,000 schoolchildren and university students in Germany had taken to the streets on November 20 to protest against rising military spending and the potent...

### 47. Trump says briefed Rutte about his negotiations with Putin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 19:00:46 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225469
- **AI 摘要**: 特朗普表示他在马阿拉歌与北约秘书长马克·卢特会面时，向他通报了与俄罗斯总统普京的会谈情况。这篇新闻主要涉及政治和外交领域。
- **原始摘要**: The US leader had a meeting with NATO Secretary General at Mar-a-Lago

### 48. Putin proposes updating Russia’s national strategy for AI development through 2036
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 18:40:09 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/economy/2225453
- **AI 摘要**: 俄罗斯总统普京提议更新至2036年的国家人工智能发展战略，并批准行动计划。他认为，要确保在人工智能领域占据领先地位，不仅需要开发尖端解决方案，还需要确保人与自主系统之间能够和谐协作。
- **原始摘要**: According to the Russian leader, it is not enough to simply develop cutting-edge solutions, it is also necessary to make sure that people and autonomous systems work together as harmoniously as possib...

### 49. Confrontation with Russia always turned into disaster for Germany — Foreign Ministry
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 18:20:49 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225445
- **AI 摘要**: 德国外长Johann Wadephul与俄罗斯外长Maria Zakharova会面时，俄罗斯外长表示德国与俄罗斯的对抗总是以德国的灾难为代价。俄罗斯外长强调俄罗斯是欧洲最大的国家，其领土面积与整个欧盟相当，还包括乌拉尔山脉及其周边地区。
- **原始摘要**: Russian Foreign Ministry Spokeswoman Maria Zakharova added that historically the periods of prosperity in Germany’s history coincide with the periods of normalization of relations with Russia

### 50. Russian Foreign Ministry spokeswoman dismisses veracity of UNESCO journalist safety report
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 18:16:58 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225439
- **AI 摘要**: 俄罗斯外交部发言人驳斥了联合国教科文组织关于记者安全的报告，指出该报告忽略了俄罗斯记者被基辅政权杀害的事实。
- **原始摘要**: Maria Zakharova criticized the report’s credibility, noting that UNESCO's previous report from 2022-23 also didn't acknowledge Russian journalists killed by the Kiev regime

### 51. Fire breaks out at refinery in Krasnodar Region following drone attack, oil spill reported
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 18:16:40 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225443
- **AI 摘要**: 俄罗斯南部克拉斯诺达尔地区一家炼油厂发生火灾，据称是无人机攻击所致，造成四名平民受伤，炼油厂的储油罐受损，原油泄漏。
- **原始摘要**: Four civilians were injured

### 52. Kim Jong Un conveys his best wishes to Russians — intergovernmental commission co-chair
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 18:12:52 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225441
- **AI 摘要**: 文章内容主要关于朝鲜领导人金正恩向俄罗斯人民表达了良好的祝愿，以及俄罗斯自然资源和生态部长在与朝鲜领导人的会面中讨论的一些议题。这与军事技术、经济、时政等类别无关，应归类为时政。
- **原始摘要**: The commission’s 13th meeting is being held in Pyongyang on November 25-27

### 53. Russia ready to share expertise on protecting oil, gas facilities with Bahrain
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:57:53 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225429
- **AI 摘要**: 俄罗斯应急部表示愿意与巴林分享保护石油和天然气设施以及利用人工智能（AI）提升安全和安保的知识和经验。俄罗斯应急部长亚历山大·库涅克表示，双方在马尼拉的讨论中讨论了这一知识和经验的共享。
- **原始摘要**: Russian Emergencies Minister Alexander Kurenkov expressed confidence that this exchange of knowledge and expertise would significantly enhance the safety and security of citizens in both nations

### 54. Estonia to reassign 160 border guards following closure of border checkpoints with Russia
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:50:38 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225421
- **AI 摘要**: 爱沙尼亚计划关闭与俄罗斯的边境检查站后，将重新分配160名边境警卫人员到其他岗位。内政部长Igor Taro表示，这些警卫人员将被部署到其他边境警卫岗位，以加强爱沙尼亚与斯堪的纳维亚半岛国家之间的陆地边境监控，并在内部边境实施补偿措施。
- **原始摘要**: Estonian Interior Minister Igor Taro noted that "part of the freed-up resources will be directed toward strengthening surveillance of the land border and implementing compensatory measures at internal...

### 55. Bank of Spain former governor to become new ECB president
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:45:57 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/economy/2225419
- **AI 摘要**: 西班牙前央行行长Pablo Hernandez de Cos将接任欧洲央行新一任行长，成为首位担任该职位的西班牙人。
- **原始摘要**: Pablo Hernandez was approved by European leaders at the ongoing summit in Brussels

### 56. Russia says West’s logic of weapons testing in Ukraine ‘would make Hitler envious’
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:39:11 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225409
- **AI 摘要**: 俄罗斯外交部发言人Maria Zakharova表示，西方国家长期以来将乌克兰视为现代武器和技术应用的试验场，甚至希特勒也会感到嫉妒。
- **原始摘要**: Western countries have long viewed Ukraine as a testing ground for modern weapons and the application of new combat strategies, MAria Zakharova stressed

### 57. Lavrov to attend Doha Forum in Qatar on December 5-6 — MFA spokeswoman
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:35:36 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225407
- **AI 摘要**: 俄罗斯外长Lavrov将于12月5-6日访问卡塔尔参加Doha论坛，并与卡塔尔领导层会面讨论进一步发展俄卡合作的前景。
- **原始摘要**: Maria Zakharova added that Russia’s foreign minister will also hold meetings with Qatar’s leadership to discuss prospects for further steady development of Russian-Qatari cooperation

### 58. MFA slams Canada’s refusal to issue visas to Russian Paralympic skiers as 'disgrace'
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:33:08 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225401
- **AI 摘要**: 俄罗斯外长发言人谴责加拿大拒绝发放俄罗斯轮椅运动员的签证，称这是对俄罗斯的敌意表现，是耻辱和反人类的。
- **原始摘要**: Russian Foreign Ministry Spokeswoman Maria Zakharova called the unexplained delay in processing the visas and the subsequent refusal to issue them "yet another example of anti-Russian hysteria"

### 59. MFA rejects Japan's assertion that Russian threat justifies militarization
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:30:48 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225403
- **AI 摘要**: 俄罗斯外长表示，日本防卫大臣引用俄罗斯、中国和朝鲜的威胁来加速军力建设的说法是不合理的。俄罗斯外长认为这是日本高级官员的不恰当言论。
- **原始摘要**: Moscow considers statements justifying the need for accelerated military buildup by a high-ranking Japanese politician absolutely unfounded and inappropriate, Maria Zakharova emphasized

### 60. Sandu preparing Moldova to become supply hub for Kiev — Russian MFA
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:25:01 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225395
- **AI 摘要**: 俄罗斯外长发言人指责摩尔多瓦总统马娅·桑杜准备将摩尔多瓦变成基辅政权的后勤中心。发言人指出，摩尔多瓦政府于11月24日发布了一项旨在规范武器和弹药生产、优先发展无人机技术和防空系统的新法案。
- **原始摘要**: According to Russian Foreign Ministry Spokeswoman Maria Zakharova, people in Moldova have pointed out some initiatives are aimed directly at undermining the country’s security

### 61. Europe's once 'blooming garden' now in state of decay — Lavrov
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:06:30 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225387
- **AI 摘要**: 俄罗斯外长拉夫罗夫表示，西方国家推行傲慢的殖民政策使欧洲一度繁荣的地方变得衰败。拉夫罗夫指出，西方国家拒绝考虑潜在合作伙伴邻国的利益，这是西方国家推行的傲慢殖民政策。
- **原始摘要**: The Russian foreign minister pointed to the arrogant neocolonial policy that the West is pursuing

### 62. Zelensky using terrorist attacks to provoke direct Russia-NATO clash — MFA
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 17:02:14 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225383
- **AI 摘要**: 俄罗斯外长发言人指责乌克兰总统泽连斯基利用恐怖袭击破坏和平谈判，并引发俄罗斯与北约国家之间的直接冲突。泽连斯基曾利用无人机攻击利比亚布希纳港的行为被视作对利比亚的宣战。
- **原始摘要**: Russian Foreign Ministry Spokeswoman Maria Zakharova added that Vladimir Zelensky does not care about the fate of millions of people, particularly in Western Europe

### 63. Nepal to declare 4,000 missing flood victims dead — AFP
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:48:40 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/society/2225373
- **AI 摘要**: 尼泊尔准备宣布4000名失踪人员死亡，这是在新法律下减少等待期后进行的。新法律缩短了在自然灾害后宣布失踪人员死亡的等待时间。
- **原始摘要**: The news agency reported that Nepal is preparing to take this step after a new law was passed, which reduced the waiting period before declaring those missing after natural disasters deceased

### 64. Bulgaria will not fund military aid to Ukraine, prime minister says
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:44:57 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225371
- **AI 摘要**: 保加利亚总理表示，保加利亚不会资助乌克兰的军事援助，但将继续提供人道主义援助。保加利亚、捷克、斯洛伐克和匈牙利拒绝了向乌克兰提供贷款的担保，尽管此前保加利亚政府曾同意在2025年和2026年提供财政援助。
- **原始摘要**: Rumen Radev highlighted that the EU was now considering a new 45-billion-euro loan for Ukraine for next year, split into 25 billion euros for military support and 20 billion euros in non-military budg...

### 65. Start of Russia’s special op forces West to show its hand — Lavrov
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:40:28 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225363
- **AI 摘要**: 俄罗斯外长拉夫罗夫表示，西方在俄罗斯发起特别军事行动后，已经明确表示了其意图。拉夫罗夫指出，西方现在宣布了其计划，并准备在乌克兰实施战争，同时要求立即在乌克兰停火。然而，西方声称停火后不会达成长期解决方案。
- **原始摘要**: The West wants the fighting to stop, and then they will immediately deploy their own troops and set up military bases in Ukraine, the Russian foreign minister stressed

### 66. China to resolutely counter violations, provocations in South China Sea — Defense Ministry
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:39:21 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225357
- **AI 摘要**: 中国国防部长表示，中国将坚决反制南海的侵犯和挑衅行为。中国国防部长表示，中国将继续采取必要的措施，坚决反制侵犯和挑衅，并坚决阻止任何破坏南海局势的行为。
- **原始摘要**: Chen Xi explained that "certain Filipino politicians," driven by personal interests, "are spreading false narratives about China" and provoking conflict

### 67. Impossible to eradicate doping abuse in sports, says WADA chief Banka
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:22:23 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/sports/2225347
- **AI 摘要**: WADA主席Banka表示，由于总有人想违反规则，无法根除体育中的兴奋剂使用。他强调需要继续与全球反兴奋剂机构合作。
- **原始摘要**: According to Witold Banka, there always be someone who want to cheat the rules

### 68. Tanker struck by unidentified projectile off Oman — UKMTO
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:05:56 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225333
- **AI 摘要**: 英国海军贸易操作部门报告称，一艘从阿曼驶出的油轮在霍尔木兹海峡附近被不明物体击中，但没有人员伤亡。
- **原始摘要**: There were no reports of casualties

### 69. Armenia’s law prescribing EU accession cannot be repealed, PM says
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:05:33 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225335
- **AI 摘要**: 亚美尼亚总理表示，亚美尼亚议会通过的加入欧盟的法律不能被废除，因为这是由公民发起的倡议，并且在选举中多数亚美尼亚公民支持该法律。
- **原始摘要**: Armenia’s parliament passed a law on launching the process of the country’s accession to the European Union on March 26, 2025

### 70. Russian deputy says neutrality would ensure Ukraine's security, not joining NATO
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 16:05:01 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225313
- **AI 摘要**: 俄罗斯副议长表示，乌克兰保持中立状态能够确保其安全，而非加入北约。他强调，中立状态应通过去军事化和去纳粹化实现，即清除乌克兰政权中的纳粹势力。
- **原始摘要**: Sergey Mironov said that ensuring Ukraine’s neutral status was one of the reasons for the special military operation

### 71. Roscosmos, UN office discuss Russia’s participation in UN space events
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:48:26 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/science/2225297
- **AI 摘要**: Roscosmos和联合国外层空间事务办公室讨论了俄罗斯如何参与未来联合国太空活动。双方在莫斯科会面，讨论了Roscosmos和联合国外层空间事务办公室的合作机会。
- **原始摘要**: Roscosmos CEO Dmitry Bakanov and Aarti Holla-Maini, director of the United Nations Office for Outer Space Affairs, met at the National Space Center, named after Valentina Tereshkova, the first woman i...

### 72. Russia, Turkey to ‘synchronize watches’ on bilateral agenda — Russian deputy PM
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:47:33 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225299
- **AI 摘要**: 俄罗斯副总理Novak表示，俄罗斯和土耳其计划在即将举行的俄土贸易和经济合作政府间委员会成立20周年会议上，就所有领域合作进行全面审查。
- **原始摘要**: Russia is ready to further strengthen this partnership based on mutual respect and trust, Alexander Novak noted

### 73. Tajikistan plans to fully switch to renewable energy by 2032 — Prime Minister
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:32:17 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225289
- **AI 摘要**: 塔吉克斯坦计划在2032年完全转向可再生能源，塔吉克斯坦总理表示，目前该国98%的电力来自水电站，到2032年将完全转向可再生能源，目标是到2037年将塔吉克斯坦转变为“绿色”国家。
- **原始摘要**: According to Kokhir Rasulzoda, the republic is currently using only 5% of its hydropower potential

### 74. Kremlin briefing covers EU budget, prisoner exchange, Trump’s remarks
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:30:22 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225277
- **AI 摘要**: 本文报道了俄罗斯克里姆林宫发言人关于欧盟七年的预算、囚犯交换和特朗普呼吁避免扩大乌克兰冲突的谈话。
- **原始摘要**: Dmitry Peskov added that the Russian president has yet to decide whether to attend the G20 summit in Miami on December 14-15

### 75. Putin arrives at AI Journey international conference
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:30:16 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225287
- **AI 摘要**: 俄罗斯总统普京出席Sber银行总部的AI Journey国际会议，与哈萨克斯坦总统塔卡耶夫一同出席。这是普京第二次参加该论坛，他在论坛上发言并参观了科技创新展览。
- **原始摘要**: The Russian leader will take part in the event alongside Kazakh President Kassym-Jomart Tokayev

### 76. Fulfillment of Apocalypse prophecies seems near amid AI development — Patriarch Kirill
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:23:19 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/society/2225281
- **AI 摘要**: 俄罗斯东正教主教Kirill表示，随着人工智能技术的发展，世界末日的预言似乎越来越近。他担心人工智能可能会决定人类是生产链中的冗余部分。
- **原始摘要**: The Patriarch questioned whether the prospect of development at the cost of losing the ability to make independent decisions could benefit humanity

### 77. Kiev’s allies cover up its chemical weapons crimes against Russia, envoy to OPCW says
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:16:41 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225269
- **AI 摘要**: 俄罗斯驻OPCW大使表示，支持乌克兰的国家正在掩盖乌方对俄公民使用有毒物质的犯罪行为，并且在提供军事资源，包括化学武器方面提供帮助。
- **原始摘要**: Vladimir Tarabrin underscored that Ukraine is persistently targeting Russian chemical facilities, thereby posing significant environmental risks

### 78. Finnish politician sees German rearmament as preparations for war with Russia
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 15:03:51 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225261
- **AI 摘要**: 芬兰政治家Armando Mema表示，德国计划在未来几年内投入4000亿欧元来重建其军队，以准备与俄罗斯的战争。Mema认为这是二战以来德国最大的军备重建计划，表明德国正为与俄罗斯的战争做准备。
- **原始摘要**: Armando Mema said that Germany plans to spend 400 billion euros in the coming years to rebuild its own military

### 79. Russian experts could evaluate Kiev’s report on chemical incidents if warranted — envoy
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 14:59:20 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225253
- **AI 摘要**: 俄罗斯驻OPCW大使表示，如果必要，俄罗斯专家可以评估乌克兰提交给OPCW的关于化学事件的报告。大使称该报告基于一个来自虚假Telegram频道的伪造出版物。
- **原始摘要**: Vladimir Tarabrin stressed that the 79 page report from Kiev is based "on a fabricated publication from a fake and no longer existing Telegram channel"

### 80. Decision to hold Q&A session earlier linked to President’s tight work schedule — Kremlin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 14:53:51 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225245
- **AI 摘要**: 俄罗斯总统普京的工作安排紧张，因此决定将12月10日的现场问答会议提前到12月10日举行。克里姆林宫发言人表示，这是由于12月普京的工作安排较为紧凑。
- **原始摘要**: Preparations are currently underway, Dmitry Peskov noted

### 81. Ukraine nearing 'complete and unconditional surrender' — Russian envoy to OSCE
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 14:49:11 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225243
- **AI 摘要**: 俄罗斯驻OSCE代表表示，乌克兰总统对结束乌克兰冲突没有兴趣，乌克兰局势正接近‘完全和无条件投降’。
- **原始摘要**: Dmitry Polyansky noted that the head of Kiev regime had no interest in talks to end the conflict in Ukraine

### 82. Russian envoy says Zelensky banking on renewed US aid after new Congress seated in 2027
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 26 Nov 2026 14:46:40 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2225241
- **AI 摘要**: 俄罗斯常驻维也纳的代表表示，泽连斯基希望在2027年新国会就职后，美国能够恢复对乌克兰的大规模军事和财政援助。
- **原始摘要**: According to Dmitry Polyansky, Vladimir Zelensky has no intention of meeting the current US administration halfway

### 83. One person killed in Houthi attack on Saudi refinery
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Fri, 27 Nov 2026 02:16:49 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225595
- **AI 摘要**: 沙特Jizan油 refinage在胡塞组织的攻击下发生了一起人员伤亡事件，一名尼泊尔公民死亡，另有数人受伤。沙特能源部表示，该设施暂时停止了部分操作。
- **原始摘要**: Several others sustained injuries of varying degrees, the facility partially halted operations

### 84. Yemeni government has no plans to leave Aden because of Houthis — ambassador
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Fri, 27 Nov 2026 01:37:01 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225591
- **AI 摘要**: 俄罗斯塔斯社报道，也门政府表示，尽管与胡塞武装在亚丁的军事行动，也门政府仍决心留在亚丁，亚丁是临时首都。也门大使表示，政府将继续与沙特领导的阿拉伯联盟支持的政府一起，与武装力量一起，击败敌对力量。
- **原始摘要**: Ahmed Salem Saleh al-Wahishi expressed determination to defeat hostile forces

### 85. IAEA in talks with Russia, Ukraine on ceasefire around ZNPP — Grossi
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Fri, 27 Nov 2026 01:19:35 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225589
- **AI 摘要**: IAEA与俄罗斯和乌克兰正在就扎波罗热核电站周围停火问题进行谈判。由于再次发生电力中断，核电站依赖单一电源线，且位于前线，导致其离站电源连接极其脆弱。IAEA总干事拉斐尔·格罗西呼吁双方进行积极建设性的合作。
- **原始摘要**: The official called on both sides to "work constructively" to facilitate repair of the Ferrosplavnaya-1 line and re-establish an offsite power connection to the plant

### 86. EU unable to agree on next seven-year budget — German chancellor
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Fri, 27 Nov 2026 00:56:37 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225587
- **AI 摘要**: 德国总理弗里德里希·梅尔兹表示，欧盟领导人未能就下七年的预算框架达成一致，但预计年底之前能获得批准。梅尔兹称，欧盟预算谈判正处于一个全新的时代。
- **原始摘要**: Friedrich Merz added that EU leaders still expect to have the budget approved by the end of the year

### 87. Russian explorer Konyukhov returns to Antarctica for new research
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Fri, 27 Nov 2026 00:52:10 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/science/2225585
- **AI 摘要**: 俄罗斯探险家Konyukhov再次前往南极进行新的科学研究，他将与西罗索海洋研究所合作收集微塑料污染样本。
- **原始摘要**: As he did last year, Fyodor Konyukhov will collect samples to research and analyze microplastic pollution in collaboration with the Shirshov Institute of Oceanology, expedition headquarters director O...

### 88. Libya’s Presidential Council head calls for probe into Benghazi port attack
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Fri, 27 Nov 2026 00:03:55 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2225579
- **AI 摘要**: 利比亚总统委员会主席呼吁调查布吉纳法索港口的袭击事件，并要求找出责任人。利比亚总统委员会主席马赫穆德·阿明菲在与俄罗斯大使在廷布里会面后表示，应防止类似事件发生并避免进一步升级。利比亚总统委员会副主席穆萨·阿克尼谴责乌克兰对袭击的承认，将其等同于战争行为。
- **原始摘要**: Mohamed al-Menfi stressed the need to prevent similar incidents and avoid further escalation

### 89. Ukraine, Denmark agree on defence AI cooperation
- **来源**: Army Technology (MILITARY)
- **发布日期**: 2026-11-27
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.army-technology.com/news/ukraine-denmark-ai-avengers-lab/
- **AI 摘要**: 乌克兰与丹麦就国防AI合作达成协议。全文未提供具体技术细节，仅涉及合作内容。

## 🏷️  AI应用

**25 篇文章**

### 1. 顶尖商用级AI视频每秒只要5毛！中国开源新势力拿下全球第一
- **来源**: 量子位 (TIER3)
- **发布日期**: Thu, 26 Nov 2026 06:41:23 +0000 (昨天)
- **类型**: news
- **优先级**: low
- **分类**: AI应用
- **链接**: https://www.qbitai.com/2026/11/512916.html
- **AI 摘要**: 量子位报道了中国开源视频模型MAGI-2在生成视频方面的出色表现，该模型在Artificial Analysis的图生视频榜单中获得全球第一。MAGI-2模型参数规模达到480B，每秒生成视频的价格仅为5毛钱，且具备自主规划和复杂脚本执行能力。Sand.ai计划开放MAGI-2模型权重，让全球开发者有机会使用和进一步开发这一模型。
- **原始摘要**: 30秒一镜到底，可自动编排镜头

### 2. Essential 3D printer maintenance tool deals for Black Friday — save up to 30% on precision tools, lights, snips, and more
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 17:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.tomshardware.com/gift-guides-seasonal-sales/essential-3d-printer-maintenance-tool-deals-for-black-friday-save-up-to-30-percent-on-precision-tools-lights-snips-and-more
- **AI 摘要**: 本文介绍了Tom's Hardware网站上的一些3D打印机维护工具的Black Friday促销活动，包括节省30%的精密工具、灯光、剪刀等。
- **原始摘要**: For the best 3D print results, there are always a few favorite tools to have on hand.

### 3. A month with the iPhone Duo has changed how I use my phone
- **来源**: TechCrunch (TIER3)
- **发布日期**: Thu, 26 Nov 2026 17:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://techcrunch.com/2026/11/26/a-month-with-the-iphone-duo-has-changed-how-i-use-my-phone/
- **AI 摘要**: 文章主要描述了作者使用iPhone Duo一个月后的体验，强调了其折叠设计如何改变了作者的使用习惯，包括对应用程序的使用和手机的个性化设置。文章提到了作者对一些初始担忧的减轻，以及对新功能的适应。尽管存在一些缺点，如偶尔怀念的镜头和Face ID，但总体上作者对iPhone Duo的体验感到满意。
- **原始摘要**: From reading more books to breaking mindless scrolling habits, Apple's foldable has changed my daily routines in ways I didn't anticipate.

### 4. Grand Theft Auto VI proves why efficiency isn’t a virtue
- **来源**: TechCrunch (TIER3)
- **发布日期**: Thu, 26 Nov 2026 16:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://techcrunch.com/2026/11/26/as-anthropic-ipos-grand-theft-auto-vi-proves-why-efficiency-isnt-a-virtue/
- **AI 摘要**: 文章讨论了《GTA VI》这款游戏的成功及其对AI的期待，提到了玩家为了这款游戏放弃工作，甚至安排了营养补充来保持精力。文章并未涉及具体的技术实现或应用，因此最合适的分类是AI应用。
- **原始摘要**: On the same day that Anthropic entered the public market, a painstakingly human video game became one of most successful entertainment launches of all time.

### 5. Best Black Friday Wi-Fi router deals 2026
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 14:23:51 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.tomshardware.com/networking/routers/best-wi-fi-router-deals-2026
- **AI 摘要**: 本文介绍了2026年黑五Wi-Fi路由器的优惠信息，涉及TP-Link、Netgear、ASUS等品牌的Wi-Fi 7、Wi-Fi 6E、Wi-Fi 6路由器。
- **原始摘要**: Save big with one of these excellent Wi-Fi router Black Friday deals. We're constantly updating this list with the best deals across all retailers.

### 6. Solo developer vibe codes a gallery hosting 36 classic GPU demos
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 14:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.tomshardware.com/video-games/retro-gaming/solo-developer-vibe-codes-a-gallery-hosting-36-classic-gpu-demos-preservation-effort-includes-3dfx-voodoo-showcases-from-1997-nvidia-bubble-and-more
- **AI 摘要**: 本文介绍了一个Solo开发者创建了一个包含36个经典GPU演示的画廊，涵盖了1997年的3dfx Voodoo展示、Nvidia泡沫等。这与AI技术无关。
- **原始摘要**: A solo developer known as arkits has created an online gallery to view classic 3D graphics demos live in the browser.

### 7. Best Black Friday 2026 tech deals
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Thu, 26 Nov 2026 07:23:03 +0000 (昨天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.tomshardware.com/live/news/black-friday-2026-day-two
- **AI 摘要**: 本文介绍了2026年黑色星期五的科技优惠，涵盖了GPU、CPU、SSD等硬件产品的折扣信息。
- **原始摘要**: All the best Black Friday deals for tech and PC hardware.

### 8. Who Picked This Gift? My A.I. Holiday Shopper.
- **来源**: The New York Times HomePage (TIER3)
- **发布日期**: Thu, 26 Nov 2026 15:13:32 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.nytimes.com/2026/11/26/business/holiday-shopping-ai-agents.html
- **AI 摘要**: 文章讨论了消费者如何使用AI技术来节省时间和金钱，提到了虚拟助手和沃尔玛的Sparky等工具。这与AI应用的定义相符。
- **原始摘要**: From virtual agents on A.I. platforms to store helpers like Walmart’s Sparky, consumers are using the technology to save money and time.

### 9. TrustedRouter Aims to Give Companies Greater Privacy With AI
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:02:01 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.bloomberg.com/news/newsletters/2026-11-26/trustedrouter-aims-to-give-companies-greater-privacy-with-ai
- **AI 摘要**: 文章提到TrustedRouter公司提供了一种方法来保护员工的AI使用隐私，从模型开发者那里。这与AI模型和Harness工程相关，但更符合AI应用的范畴，因为它描述了一个实际的AI产品或解决方案。
- **原始摘要**: The startup offers companies a way to keep employees’ AI use private from model makers

### 10. Latin America has the copper and energy the AI build-out needs. Infrastructure is the test
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 08:59:11 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cnbc.com/2026/11/26/latin-america-copper-energy-ai-investment.html
- **AI 摘要**: 文章讨论了拉丁美洲的铜、能源和矿物资源在人工智能建设中的重要性，强调了基础设施、融资条件和政策稳定性对于将这些资源转化为可行项目的挑战。
- **原始摘要**: Latin America’s copper, oil, gas and rare earths could benefit from rising AI energy demand, if infrastructure and fiscal policy attract investment.

### 11. Beware higher correlation but nab high U.S. credit yields, fund managers say
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 05:36:01 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cnbc.com/2026/11/26/mispricing-risk-fund-managers-ai-volatility.html
- **AI 摘要**: 本文讨论了投资专业人士在iConnections Global Alts Asia会议上对AI热潮的风险和机会的看法。尽管对AI估值和经济衰退风险的担忧存在，数据中心仍然是一个有吸引力的投资机会。同时，投资组合可能比看起来更容易受到市场波动的影响。
- **原始摘要**: The AI boom could trigger a recession, but data centers remain an attractive investment opportunity, a hedge fund manager said.

### 12. ‘Your booth is waiting’: Denny’s welcomes Jensen Huang back as Nvidia CEO
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Thu, 26 Nov 2026 03:13:43 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cnbc.com/2026/11/26/dennys-jensen-huang-nvidia.html
- **AI 摘要**: Denny's在推特上宣布Nvidia CEO Jensen Huang的回归，并恢复了纪念Nvidia诞生地的铭牌。Jensen Huang与Denny's有着悠久的历史联系，早在Nvidia成立之前他就曾在该餐厅工作。本文还提到了Denny's在Pennsylvania的标志。
- **原始摘要**: Denny's reaffirmed its longstanding ties with Jensen Huang following his return as Nvidia CEO, revealing that a plaque had been restored.

### 13. Streaming Tax: Can Streaming VLMs Replace Their Offline Parents?
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.33474
- **AI 摘要**: 文章讨论了流式VLMs能否在离线任务上取代其离线版本，提出了Streaming Tax来评估流式VLMs的性能。文章指出流式VLMs在理解和泛化方面存在差距。
- **原始摘要**: arXiv:2611.33474v1 Announce Type: new Abstract: Most vision-language models (VLMs) specialize in offline video understanding; in contrast, their post-trained versions, streaming VLMs, can perform live...

### 14. Click and Count: Multimodal Prototype Adaptation for Class-Agnostic Object Counting
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.28321
- **AI 摘要**: 该文章提出了一种多模态、类无关的基于原型的物体计数框架，通过视觉示例、文本描述或两者结合来指定目标物体。
- **原始摘要**: arXiv:2611.28321v2 Announce Type: replace Abstract: We propose a multimodal, class-agnostic, density-based object counting framework that specifies the object of interest through visual exemplars, a t...

### 15. Beyond Code and Pixels: Co-Generating Editable and Visually Rich Presentations
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.28010
- **AI 摘要**: 该文章讨论了一种新的多代理系统SlidesWeaver，用于生成可编辑且视觉丰富的PPTX演示文稿，结合了语言和视觉代理，解决了程序方法和图像方法的局限性。
- **原始摘要**: arXiv:2611.28010v2 Announce Type: replace-cross Abstract: Generating PPTX presentations is a structured task that requires semantic planning, visual composition, precise layout, and editability, motiv...

### 16. MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2607.21570
- **AI 摘要**: 文章讨论了使用大型语言模型进行医学教育的新框架MedGame，该框架将静态临床案例转化为结构化、可执行的叙事游戏。
- **原始摘要**: arXiv:2607.21570v2 Announce Type: replace Abstract: Large Language Models (LLMs) show promise for medical education, but most existing systems focus on localized interactions such as question answerin...

### 17. AI-Mediated Communication Can Reduce Opinion-Based Network Segregation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2510.21984
- **AI 摘要**: 文章讨论了AI在人际沟通中的作用，特别是在减少基于观点的网络隔阂方面。
- **原始摘要**: arXiv:2510.21984v3 Announce Type: replace-cross Abstract: Everyday communication is increasingly AI-mediated, with large language models (LLMs) suggesting wording, tone, and framing while humans decid...

### 18. Shadows in the Code: Exploring the Risks and Defenses of LLM-based Multi-Agent Software Development Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2511.18467
- **AI 摘要**: 该文章讨论了基于LLM的多Agent软件开发系统的安全风险和防御机制，涉及恶意用户和良性用户的情景，以及如何通过多Agent系统引入隐蔽的恶意功能。
- **原始摘要**: arXiv:2511.18467v2 Announce Type: replace-cross Abstract: The rapid advancement of Large Language Model (LLM)-driven multi-agent systems has significantly streamlined software developing tasks, enabli...

### 19. Large Language Model Agents for Evidence Based Genetic Disease Severity Classification
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2609.19569
- **AI 摘要**: 该文章介绍了一种基于大型语言模型的自主AI代理，用于基于证据的遗传疾病严重程度分类。
- **原始摘要**: arXiv:2609.19569v3 Announce Type: replace-cross Abstract: Disease severity classification for genetic conditions is subjective and labor-intensive, creating bottlenecks in genomic screening, where com...

### 20. REI: Learning Ideation from Repository Evolution
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.33183
- **AI 摘要**: 文章讨论了通过代码仓库的演化来学习可重用的创意策略，以减少对昂贵的试验和错误的依赖。
- **原始摘要**: arXiv:2611.33183v1 Announce Type: new Abstract: As AI systems become increasingly capable of executing and evaluating experiments, ideation is emerging as a bottleneck in automated scientific and engi...

### 21. Cross-Layer Characterization and AI-Assisted Diagnosis of C-to-Rust Performance
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 12 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.33490
- **AI 摘要**: 该文章讨论了将C代码迁移到Rust后性能的影响，并提出了一种AI辅助性能调试工具FerroScope。
- **原始摘要**: arXiv:2611.33490v1 Announce Type: cross Abstract: Migrating C code to Rust can significantly improve software security, but understanding the performance implications of such migrations remains challe...

### 22. Early progress on accelerating drug development with Claude
- **来源**: Anthropic Research (TIER1)
- **发布日期**: 2026-11-27
- **类型**: research
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.anthropic.com/research/early-progress-drug-development
- **AI 摘要**: 文章讨论了Claude在加速药物开发方面的早期进展。

### 23. Claude-shaped science
- **来源**: Anthropic Research (TIER1)
- **发布日期**: 2026-11-27
- **类型**: research
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.anthropic.com/research/claude-shaped-science
- **AI 摘要**: 文章标题为Claude-shaped science，摘要未提供具体信息，无法确定文章主题。

### 24. Sudeep Bhoja on 3D-Stacked DRAM and the Raptor Roadmap
- **来源**: D-Matrix (TIER1)
- **发布日期**: 2026-11-27
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.d-matrix.ai/announcements/sudeep-bhoja-on-3d-stacked-dram-and-the-raptor-roadmap/
- **AI 摘要**: 文章讨论了3D堆叠DRAM和Raptor路线图，与AI模型、Harness工程、具身智能、AI芯片、编译器、光计算、军事技术、经济和时政等类别都不相关。

### 25. 2026-10-22Day0适配 | 壁仞科技率先支持阶跃星辰Step 5 Preview大模型，快速打通推理全链路
- **来源**: Biren (壁仞科技) (TIER1)
- **发布日期**: 2026-11-27
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.birentech.com/news//news/yt4wako63dg63co6kpwpi31o/
- **AI 摘要**: 壁仞科技支持了阶跃星辰Step 5 Preview大模型，实现了快速的推理全链路打通。

## 🏷️  未分类

**1 篇文章**

### 1. Brazil Inflation Undershoots Forecasts in ‘Positive’ Print
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Thu, 26 Nov 2026 12:15:36 GMT (今天)
- **类型**: news
- **优先级**: high
- **链接**: https://www.bloomberg.com/news/articles/2026-11-26/brazil-consumer-prices-rise-less-than-forecast-by-all-analysts
- **原始摘要**: Brazil’s consumer prices rose much less than forecast earlier this month, as policymakers face fiscal and currency risks following President Luiz Inácio Lula da Silva’s reelection.

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
