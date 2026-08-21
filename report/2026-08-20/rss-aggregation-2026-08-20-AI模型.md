# RSS 聚合报告 - AI模型

**生成时间**: 2026-08-21 15:54:49
**文章数量**: 90 篇

---

### 1. Is KV Cache in a high dimensional vector space? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T18:18:10+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtrdem/is_kv_cache_in_a_high_dimensional_vector_space_d/
- **AI 摘要**: 作者研究KV缓存是否处于高维向量空间，认为推理时KV缓存是模型工作记忆的重要部分，并非扁平列表，而是具有可导航几何结构的向量集合，键携带模型学习到的关联关系。
- **原始摘要**: I've been doing some research on this question: At inference time a large part of a model's working memory lives in the KV cache, plus whatever external memory the harness bolts on. I've been poking a...

### 2. Mapping intrinsic rank and informational gravity in complex tabular data: I developed a non-parametric, model-agnostic, information-theoretic diagnostic to bypass the limits of linear, rank, and Euclidean baselines. [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T13:34:28+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtjotb/mapping_intrinsic_rank_and_informational_gravity/
- **AI 摘要**: 作者开发了一种非参数、模型无关的信息论诊断方法，用于映射复杂表格数据的内在秩和信息引力，以克服线性、秩和欧几里得基线的局限性。提供了预印本和开源代码。
- **原始摘要**: Links: Preprint: https://doi.org/10.5281/zenodo.22028087 Entropic Scree Function v1.0.0 / GitHub: https://github.com/tjleestjohn/Entropic-Scree TL;DR: Standard PCA fundamentally fractures non-linear d...

### 3. The spectral neuron - an ML primitive for scalable and interpretable models [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T10:20:47+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtfimo/the_spectral_neuron_an_ml_primitive_for_scalable/
- **AI 摘要**: 作者在Yahoo广告团队工作期间，探索是否存在既简单、可扩展、可解释又可控制的模型。通过博客和预印本形式，提出了“光谱神经元”这一ML原语，旨在实现可扩展且可解释的模型。
- **原始摘要**: Worked some time ago on one of the ad teams at Yahoo, and this grew out of a question I kept returning to while there are there "simple" models that are both simple, scalable, interpretable, and contr...

### 4. About the impact of grouping classes in multiclass classification [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T07:42:20+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtctaz/about_the_impact_of_grouping_classes_in/
- **AI 摘要**: 作者询问在多分类问题中将多个类别分组是否会有害，希望了解相关研究或共识。作者已做初步调研，认为问题有一定深度，适合在专业社区讨论。
- **原始摘要**: A premise: I hope this question is "worth" of this subreddit, I did a decent amount of research before posting, I thought it was potentially interesting enough for it, but possibly not basic enough fo...

### 5. Same GRPO recipe on three from-scratch LLMs (353M/316M/672M) gave three different outcomes, with no clean relationship to scale [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T21:30:26+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vszsit/same_grpo_recipe_on_three_fromscratch_llms/
- **AI 摘要**: 作者用相同GRPO配方训练三个不同规模的LLM（353M/316M/672M），结果差异显著且与规模无清晰关系。预训练正常，但GRPO后训练对两个较大模型产生负面影响，原因不明。
- **原始摘要**: I trained three LLMs from scratch in raw PyTorch then post-trained each one with SFT and then GRPO. Same process every time: same synthetic arithmetic curriculum, same reward function, same hyperparam...

### 6. How much of the weight-space perception gap is actually symmetry? Evidence from ~1.8M fitted SIRENs [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T19:24:12+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vswdnf/how_much_of_the_weightspace_perception_gap_is/
- **AI 摘要**: 本文探讨权重空间学习中一个基本问题：为何共享初始化的网络权重可读语义，而独立拟合时失效。作者通过约180万拟合SIRENs实验，质疑参数对称性是否为解释差距的主要原因，并提供证据表明对称性并非全部原因。
- **原始摘要**: I’ve been looking at a fairly basic question in weight-space learning that I don’t think gets separated cleanly enough: Why does reading semantics directly from neural network weights work pretty well...

### 7. Trained an diffusion model that runs on 264KB of RAM [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-18T09:26:21+00:00 (3 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vrk7t5/trained_an_diffusion_model_that_runs_on_264kb_of/
- **AI 摘要**: 作者训练了一个仅需264KB RAM即可运行的扩散模型，并展示了相关成果。该模型在极低内存环境下运行，可能适用于资源受限的设备或嵌入式场景。
- **原始摘要**: I recently bought a Shrike lite which has got 264KB of SRAM. I decided to train an image generation model that generates 32*32 pixel images. The microcontroller also has an FPGA onboard which I used t...

### 8. Revisiting the Efficient Channel Attention paper (2019, 12k citations) - the central hypothesis isn't quite right [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-16T10:13:44+00:00 (5 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/
- **AI 摘要**: 重新审视2019年高效通道注意力（ECA）论文，该论文被引超1.2万次。ECA通过一维卷积替代SE的降维，效果显著优于SE。但作者指出其核心假设并不完全正确，并进行了深入分析。
- **原始摘要**: ECA was positioned as a successor to SE. The idea behind ECA is quite simple. Unlike SE which reduces the channel means into a smaller hidden layer, it directly uses a 1d convolution kernel on the cha...

### 9. Up to 3.2x Faster Inference with LFM2.5-DSpark
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Thu, 20 Aug 2026 16:52:57 GMT (今天)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/LiquidAI/lfm25-dspark
- **AI 摘要**: LFM2.5-DSpark模型通过优化推理流程，实现了最高3.2倍的推理速度提升，显著降低延迟，适用于大规模部署场景。

### 10. v1.6.0: Mistrall goes Small 3.1 with vision
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2025-03-20T15:03:08Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.6.0
- **AI 摘要**: Mistral推理库v1.6.0版本更新，新增对Mistral Small 3.1模型的支持，该模型具备视觉能力，并修复了换行缺失问题。
- **原始摘要**: What's Changed Missing new line by @theophilegervet in #234 Add support to Mistral Small 3.1 by @juliendenize in #239 Remove file refs by @juliendenize in #240 Release 1.6.0 by @juliendenize in #241 N...

### 11. v1.4.0: Pixtral 👀
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-09-13T13:10:17Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.4.0
- **AI 摘要**: Mistral推理库v1.4.0版本发布，新增对Pixtral多模态模型的支持，使Mistral模型具备视觉理解能力，用户可通过升级安装使用。
- **原始摘要**: Pixtral Mistral models can now 👀 ! pip install --upgrade mistral_inference # >= 1.4.0 Download: from huggingface_hub import snapshot_download from pathlib import Path mistral_models_path = Path.home()...

### 12. v1.3.0 Mistral-Nemo
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-18T15:45:30Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.3.0
- **AI 摘要**: Mistral推理库v1.3.0版本发布，引入与NVIDIA合作开发的Mistral-Nemo模型，并提供了安装和下载指南。
- **原始摘要**: Welcome Mistral-Nemo from Mistral 🤝 NVIDIA Read more about Mistral-Nemo here. Install pip install mistral-inference>=1.3.0 Download export NEMO_MODEL=$HOME/12B_NEMO_MODEL wget https://models.mistralcd...

### 13. v1.2.0 Add Mamba
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-16T18:41:37Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.2.0
- **AI 摘要**: Mistral推理库v1.2.0版本发布，新增对Codestral-Mamba和Mathstral模型的支持，并提供了相关依赖安装和下载说明。
- **原始摘要**: Welcome 🐍 Codestral-Mamba and 🔢 Mathstral pip install mistral-inference>=1.2.0 Codestral-Mamba pip install packaging mamba-ssm causal-conv1d transformers Download export MAMBA_CODE=$HOME/7B_MAMBA_CODE...

### 14. Clustering and Token Denoising for Faster and More Robust VLMs
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19285
- **AI 摘要**: 本文提出ClustRS方法，通过聚类和令牌去噪技术，减少视觉语言模型（VLM）中视觉令牌的数量，以加快推理速度并增强鲁棒性，无需重新训练即可适应架构变化，便于边缘部署。
- **原始摘要**: arXiv:2608.19285v1 Announce Type: new Abstract: Recent Visual-Language Models (VLMs) have enhanced the capabilities of pre-trained LLMs by adding vision tokens alongside text, with approaches like LLa...

### 15. Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19669
- **AI 摘要**: 本文分析多模态推理中潜在推理的两阶段训练框架（SFT和RL）的局限性，提出优化潜在视觉目标表示的方法，以改进视觉思维链教学和强化学习阶段的效率与效果。
- **原始摘要**: arXiv:2608.19669v1 Announce Type: new Abstract: Latent reasoning has advanced multimodal reasoning through a two-stage training paradigm: (1) a helper image is encoded into latent tokens to teach visu...

### 16. V-REX: Efficient Specialist VLM Training for Veterinary X-Rays
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20069
- **AI 摘要**: 本文展示在兽医X光领域，通过重新设计VLM流程（从分词、预训练到接地和推理），无需大型基础模型微调，即可从零训练出性能更优的专业模型，挑战了领域专家需大模型的假设。
- **原始摘要**: arXiv:2608.20069v1 Announce Type: new Abstract: While generalist VLMs are expensive to train, creating domain experts is widely assumed to require fine-tuning increasingly large foundation models. We...

### 17. ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20122
- **AI 摘要**: 本文提出ArmorOCR方法，通过观察转移自蒸馏实现对抗性视觉文本的定位与识别，增强大型多模态模型对对抗性OCR的鲁棒性，并引入区域感知评估基准。
- **原始摘要**: arXiv:2608.20122v1 Announce Type: new Abstract: Large multimodal models (LMMs) have demonstrated strong OCR recognition capabilities, yet remain vulnerable to adversarial visual text that is readable...

### 18. ID-VTG: Image-Disambiguated Video Temporal Grounding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20127
- **AI 摘要**: 本文提出图像消歧视频时间定位（ID-VTG）任务，利用参考图像和文本的多模态查询，解决自然语言难以准确描述细粒度视觉属性导致视频时间定位困难的问题。
- **原始摘要**: arXiv:2608.20127v1 Announce Type: new Abstract: Video Temporal Grounding (VTG) faces significant challenges when natural language queries must distinguish between multiple events involving visually si...

### 19. DPC-Net: Dual-Prior Collaborative Network for All-in-One Image Restoration
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20141
- **AI 摘要**: 本文提出双先验协作网络（DPC-Net）用于全合一图像恢复，联合利用退化建模中的图像语义和重建中的低级视觉先验，解决现有方法结构失真和语义不一致的问题。
- **原始摘要**: arXiv:2608.20141v1 Announce Type: new Abstract: All-in-One Image Restoration (AiOIR) aims to handle diverse degradations within a unified model. However, existing methods often overlook image semantic...

### 20. Zoom-IQA: Image Quality Assessment with Reliable Region-Aware Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.02918
- **AI 摘要**: 本文提出Zoom-IQA方法，通过可靠的区域感知推理，改进基于视觉语言模型的图像质量评估，解决现有方法推理不可靠和评分不精确的问题。
- **原始摘要**: arXiv:2601.02918v4 Announce Type: replace Abstract: Image Quality Assessment (IQA) is a long-standing problem in computer vision. Previous methods typically focus on predicting numerical scores withou...

### 21. Video Evidence to Reasoning Efficient Video Understanding via Explicit Evidence Grounding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.07761
- **AI 摘要**: 本文提出Chain of Evidence（CoE）框架，通过架构上解耦感知基础和推理效率，解决大型视觉语言模型在视频推理中计算成本与幻觉风险之间的困境。
- **原始摘要**: arXiv:2601.07761v2 Announce Type: replace Abstract: Large Vision-Language Models (LVLMs) face a fundamental dilemma in video reasoning: they are caught between the prohibitive computational costs of v...

### 22. Reinforcing Egocentric Spatial Perception in Multimodal Large Language Models via Ego Scene Augmentation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.14497
- **AI 摘要**: 本文针对多模态大语言模型在复杂自我中心场景中空间推理能力不足的问题，提出了自我中心场景增强（ESA）框架，以增强MLLMs的自我中心空间感知能力，提升其在自我中心视觉问答任务中的表现。
- **原始摘要**: arXiv:2607.14497v2 Announce Type: replace Abstract: Egocentric Visual Question Answering (VQA) has attracted widespread attention as an important task for enabling Multimodal Large Language Models (ML...

### 23. Deep Multimodal Fusion Detection through Spatial Mask and Channel Fusion
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.02092
- **AI 摘要**: 本文提出了一种基于空间掩码和通道融合的深度多模态融合检测方法，通过注意力驱动的互补性机制，解决现有特征级融合方法在双骨干架构中过度拟合单一模态统计特性的问题，提升目标检测性能。
- **原始摘要**: arXiv:2608.02092v2 Announce Type: replace Abstract: Deep multimodal fusion for object detection has demonstrated good performance through mining modal characteristics. However, existing feature-level...

### 24. Gemma 4 on Cerebras—The Fastest Inference is Now MultimodalJune 29, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 29, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/gemma-4-on-cerebras-the-fastest-inference-is-now-multimodal
- **AI 摘要**: 介绍Gemma 4模型在Cerebras平台上的运行，宣称其推理速度最快，并支持多模态输入，标志着推理性能的新突破。

### 25. Which is faster: Kimi K2.6 on Cerebras or Gemini Flash?June 05, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 05, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/which-is-faster-gemini-3-5-flash-or-kimi-k2-6-on-cerebras
- **AI 摘要**: 文章对比了Kimi K2.6在Cerebras平台与Gemini Flash的推理速度，通过基准测试展示Cerebras在性能上的优势。

### 26. Why the AI Race Shifted to SpeedMarch 20, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: rch 20, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/why-the-ai-race-shifted-to-speed
- **AI 摘要**: 文章分析了AI竞赛为何转向速度竞争，指出推理速度已成为决定模型实用性和用户体验的关键指标，并探讨了速度提升对AI产业格局的深远影响。

### 27. The world’s fastest GLM-4.6 – now available on CerebrasNovember 18, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 18, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm
- **AI 摘要**: Cerebras平台现已支持全球最快的GLM-4.6模型，提供超高速推理性能，满足大规模AI应用需求。

### 28. REAP: One-Shot Pruning for Trillion-Parameter Mixture-of-Experts ModelsOctober 16, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 16, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/reap
- **AI 摘要**: REAP是一种一次性剪枝方法，专为万亿参数混合专家模型设计，能在保持性能的同时大幅减少计算资源消耗。

### 29. MoE Math Demystified: What Does 8x7B Actually Mean?October 14, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 14, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/moe-guide-calculator
- **AI 摘要**: 本文解释混合专家模型中8x7B参数的含义，澄清MoE架构的规模表示，帮助读者理解其计算和内存特性。

### 30. Thinking Inside the Box: The Implicit Chain Transformer for Efficient State TrackingDecember 12, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 12, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/thinking-inside-the-box-the-implicit-chain-transformer-for-efficient-state-tracking
- **AI 摘要**: 提出一种隐式链式Transformer架构，用于高效状态跟踪，通过内部状态管理减少计算开销，提升长序列任务中的推理效率，为Transformer模型优化提供新思路。

### 31. Jais 2: A Blueprint for Sovereign AIDecember 09, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 09, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/jais2
- **AI 摘要**: 介绍Jais 2模型，作为主权AI的蓝图，强调其在阿拉伯语等低资源语言上的能力，以及如何通过本地化训练和部署实现数据主权和自主可控的AI系统。

### 32. Why speed wins: faster inference is about more than just quicker answers–it’s the new path to accuracyFebruary 19, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/speedandaccuracyblog
- **AI 摘要**: 文章阐述了更快推理速度的重要性，指出速度不仅带来更快的响应，更是提升AI准确性的新途径，通过快速迭代和搜索实现更高精度。

### 33. Introducing OpenAI GPT-5.3-Codex-Spark Powered by CerebrasFebruary 12, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 12, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/openai-codexspark
- **AI 摘要**: OpenAI推出由Cerebras驱动的GPT-5.3-Codex-Spark模型，结合Cerebras高速推理硬件，旨在提供极速代码生成和AI应用体验，标志着大模型与专用芯片的深度合作。

### 34. This new model is smarter than Sonnet 4.5…and 20X faster?January 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7-migration-guide
- **AI 摘要**: 介绍一款新模型，其智能水平超越Sonnet 4.5，且推理速度快20倍，文章分析该模型的性能优势、技术特点及其对AI应用和推理效率的潜在影响。

### 35. GLM-4.7: Frontier intelligence at record speed — now available on CerebrasJanuary 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7
- **AI 摘要**: GLM-4.7模型在Cerebras平台上发布，以创纪录的速度提供前沿智能，强调其推理速度和性能优化，展示Cerebras硬件对大型语言模型推理的加速作用。

### 36. Transformer Models for Text Summarization: A Comparative Study of BART, BERT, and RoBERTa
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19200
- **AI 摘要**: 本文比较了BART、BERT和RoBERTa三种Transformer模型在文本摘要任务上的表现，探讨了抽取式、生成式和混合式摘要方法，为自动文本摘要技术提供了对比分析。
- **原始摘要**: arXiv:2608.19200v1 Announce Type: new Abstract: Text summarization refers to the task of condensing a document into a shorter version while preserving its key information. Automatic text summarization...

### 37. Asymmetric Attention Heads: Structured Head-Wise Context Allocation for Transformer Attention
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19203
- **AI 摘要**: 本文提出非对称注意力头（AAH）框架，为Transformer的不同注意力头分配不同的上下文长度，以适配其不同的上下文角色，如局部语法或长距离关系，提升注意力机制的效率。
- **原始摘要**: arXiv:2608.19203v1 Announce Type: new Abstract: Standard multi-head attention (MHA) gives every head the same full causal context span, although heads can serve different contextual roles. Some heads...

### 38. When Irrelevant Text Matters: Affine Margin Shifts in Multimodal Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19208
- **AI 摘要**: 本文研究多模态大语言模型中任务无关文本对视觉判断的影响，通过受控干预发现无关文本会一致性地引入偏差，揭示了辅助上下文对模型行为的潜在影响。
- **原始摘要**: arXiv:2608.19208v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) are frequently exposed to auxiliary textual context, the impact of which on visually grounded tasks remains und...

### 39. Represented but Ignored: A Causal Account of Prosodic Underuse in Audio-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19211
- **AI 摘要**: 本文从因果角度分析音频语言模型对韵律信息利用不足的问题，区分了声学信息丢失与错误解释等失败原因，为改进模型的表达性语音理解提供了依据。
- **原始摘要**: arXiv:2608.19211v1 Announce Type: new Abstract: Human speech is richly expressive, with prosody carrying linguistic and emotional information beyond the lexical content. A capable large audio-language...

### 40. Linguistic Holonomy and Statistical Watermarks: Inner Geometry of Meaning-Preserving Transformations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19369
- **AI 摘要**: 本文探讨语言模型统计水印与意义保持变换的关系，指出水印易被保留内容但改变形式的变换侵蚀，并批评现有文献仅通过端点语义相似度衡量变换，提出更全面的分析框架。
- **原始摘要**: arXiv:2608.19369v1 Announce Type: new Abstract: Statistical watermarks for language models live in the freedom of the signifier: they choose among tokens that are nearly equivalent in meaning, and the...

### 41. Are LLMs becoming similarly creative? Evidence from three years of models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19437
- **AI 摘要**: 本文分析三年间大型语言模型在开放式创造性任务上的表现趋势，关注创造力、原创性和多样性，发现模型创造性输出随时间的变化，为理解LLM在创意工作中的演进提供初步证据。
- **原始摘要**: arXiv:2608.19437v1 Announce Type: new Abstract: Many benchmarks track Large Language Model (LLM) performance on tasks with verifiable answers, but less is known about how LLM performance is evolving o...

### 42. When Machines Speak: A Unified Generative Framework for Integrating Machine-Native Symbols into Pretrained Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19529
- **AI 摘要**: 本文提出UniLang统一生成框架，将机器原生符号集成到预训练语言模型中，弥合语言建模与结构化预测的鸿沟，使LLM能处理离散符号表示的实体和行为。
- **原始摘要**: arXiv:2608.19529v1 Announce Type: new Abstract: Many real-world AI systems represent entities, behaviors, and structured information using discrete machine-native symbols rather than natural language....

### 43. Projector Is All You Train
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19726
- **AI 摘要**: 本文研究多模态大语言模型训练中是否必须微调主干网络。通过3D MLLM实验发现，仅训练投影器即可达到强多模态性能，挑战了传统训练范式。
- **原始摘要**: arXiv:2608.19726v1 Announce Type: new Abstract: The typical training process of a multimodal large language model (MLLM) involves adapting both the language model backbone and the projector between th...

### 44. Interrupting the Loop: Periodic Subject Changes Raise Judged Surprise and Connection in Base Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19893
- **AI 摘要**: 本文拆解认知启发的生成循环，发现周期性主题注入（中断）是主要效果来源，LLM评判能感知这种中断带来的惊奇和连接感。
- **原始摘要**: arXiv:2608.19893v1 Announce Type: new Abstract: Where does the novelty a base language model produces with no task come from, and what can an LLM judge of a long stream actually see? We dismantle a co...

### 45. Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization for Multimodal Sarcasm Detection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19942
- **AI 摘要**: 本文提出动态门控跨模态融合与讽刺感知对比正则化方法，用于多模态讽刺检测，解决模态贡献依赖实例和表面语义一致掩盖矛盾意图的挑战。
- **原始摘要**: arXiv:2608.19942v1 Announce Type: new Abstract: Multimodal sarcasm detection aims to identify sarcastic intent from multimodal content, where inconsistencies between literal meaning and contextual cue...

### 46. When Text and Numbers Disagree: Evidence Arbitration in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20116
- **AI 摘要**: 本文研究大语言模型在文本摘要、数值观察和外部工具输出冲突时如何仲裁证据。通过引入受控合成基准，生成潜在风险轨迹对应的数值时间序列和自然语言摘要，构造冲突场景，以探究模型在支持对立决策时的行为。
- **原始摘要**: arXiv:2608.20116v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used in settings where textual summaries, numerical observations, and external tool outputs may provide co...

### 47. PEA-DPO: Perception-Enhanced Alignment Direct Preference Optimization for MLLMs Alignment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19598
- **AI 摘要**: 本文提出PEA-DPO方法，通过感知增强对齐直接偏好优化，解决多模态大模型在偏好优化中的视觉不敏感问题，提升模型区分关键视觉上下文的能力。
- **原始摘要**: arXiv:2608.19598v1 Announce Type: cross Abstract: Direct Preference Optimization (DPO) has emerged as an effective approach for aligning large language models (LLMs) with human preferences. However, i...

### 48. Let's Scale Step by Step: Compute-Efficient Hyperparameter Transfer for Large-Scale Mixture-of-Experts
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20061
- **AI 摘要**: 本文提出一种计算高效的两步超参数迁移框架，用于大规模混合专家模型。通过估计最优学习率，避免极端规模下的穷举搜索，显著降低计算成本。
- **原始摘要**: arXiv:2608.20061v1 Announce Type: cross Abstract: Mixture-of-Experts (MoE) architectures significantly expand model capacity without a proportional increase in computational cost. However, optimizing...

### 49. Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20210
- **AI 摘要**: 本文介绍Daedalus-150M，一个专为CPU推理设计的卷积-注意力混合小语言模型。模型在18个块中仅6个使用全注意力，其余12个采用短卷积，内存占用不随对话长度增长，适合单用户单token的CPU推理场景。
- **原始摘要**: arXiv:2608.20210v1 Announce Type: cross Abstract: Small language models are usually built like large ones and then squeezed onto a CPU afterwards. We did the opposite: we fixed the target first, one u...

### 50. TS-Reasoner: Aligning Time Series Foundation Models with LLM Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2510.03519
- **AI 摘要**: 本文提出TS-Reasoner，将时间序列基础模型与LLM推理对齐，以弥补TSFM在高级推理和背景知识上的不足，应用于金融、能源等领域。
- **原始摘要**: arXiv:2510.03519v3 Announce Type: replace Abstract: Time series reasoning is crucial to decision-making in diverse domains, including finance, energy, and scientific discovery. While existing time ser...

### 51. Remask, Don't Replace: Token-to-Mask Refinement in Diffusion Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.18738
- **AI 摘要**: 提出Token-to-Mask（T2M），一种无需训练的推理时修正方法，解决扩散语言模型同一步生成位置间不一致的问题。
- **原始摘要**: arXiv:2604.18738v3 Announce Type: replace Abstract: Diffusion language models (dLLMs) generate text through iterative denoising, filling multiple masked positions at each step. Positions filled in the...

### 52. Language Has Two Parameters: Narrative-Induced Semantic Plasticity and Phase-Sensitive Interpretation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18041
- **AI 摘要**: 本文提出语言具有两个参数：叙事诱导的语义可塑性和相位敏感解释。阅读叙事会改变读者，产生个体和共享历史，而群体训练的语言模型不一定保留这些变化，模型只能复述上下文中的后果。
- **原始摘要**: arXiv:2608.18041v2 Announce Type: replace Abstract: Reading fiction or encountering narrative generally does not merely add information. The encounter changes the reader. This paper proposes that enco...

### 53. Towards Audio Token Compression in Large Audio Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2511.20973
- **AI 摘要**: 本文探讨大型音频语言模型中音频令牌压缩技术，通过无监督分割、均匀平均池化等方法减少音频令牌数量，以降低注意力计算成本，提升模型可扩展性。
- **原始摘要**: arXiv:2511.20973v2 Announce Type: replace-cross Abstract: Large Audio Language Models (LALMs) deliver strong performance across speech and audio tasks, but their audio encoders generate high-rate toke...

### 54. Transformer See, Transformer Do: Copying as an Intermediate Step in Learning Analogical Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.06501
- **AI 摘要**: 本文研究Transformer在类比推理中的学习机制，使用元学习组合性方法训练模型完成字母串类比任务，发现复制作为中间步骤有助于提升泛化能力，并评估其表现。
- **原始摘要**: arXiv:2604.06501v2 Announce Type: replace-cross Abstract: Analogical reasoning is a hallmark of human intelligence, enabling us to solve new problems by transferring knowledge from one situation to an...

### 55. Geometric and Behavioral Stratification in Transformer Residual Streams
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12447
- **AI 摘要**: 本文研究Transformer残差流中的几何与行为分层，发现预测方向作为内容定义的优先锚点，残差流变化在几何上呈现特定结构，为理解模型内部表示提供新视角。
- **原始摘要**: arXiv:2608.12447v3 Announce Type: replace-cross Abstract: Trained transformer models develop privileged bases: coordinate axes whose statistics differ from the rest of the residual stream. But what ki...

### 56. Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19684
- **AI 摘要**: 本文研究利用预收集数据集提升强化学习策略性能与样本效率，提出两阶段策略：先从数据集中提取多样技能作为低层策略，再训练高层策略解决特定任务，并采用离线质量-多样性强化学习方法学习分层技能策略。
- **原始摘要**: arXiv:2608.19684v1 Announce Type: new Abstract: Recent studies investigate how to leverage pre-collected datasets to improve the policy performance and sample efficiency of RL. One promising approach...

### 57. TT-net: Quantum Inspired Tensor Network Denoising in Conditional GANs
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19789
- **AI 摘要**: 本文提出TT-net，将量子物理中的张量网络方法（特别是张量列车）应用于条件生成对抗网络，用于图像去噪。该方法利用奇异值分解等线性代数工具，为机器学习提供新的去噪途径。
- **原始摘要**: arXiv:2608.19789v1 Announce Type: new Abstract: Developed as a workhorse for classical simulations of quantum algorithms and quantum many-body systems, Tensor Network methods have entered the scientif...

### 58. SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19842
- **AI 摘要**: 本文提出SAPO，一种单次rollout的自回归策略优化方法，用于智能体强化学习。该方法克服现有无评论家方法需要多次rollout的局限，减少内存开销，提升长程交互任务性能。
- **原始摘要**: arXiv:2608.19842v1 Announce Type: new Abstract: Agentic reinforcement learning (RL) has become a critical stage in the post-training of large language models. Existing critic-free, group-relative meth...

### 59. Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20256
- **AI 摘要**: 本文研究推理语言模型如何自适应分配推理努力，通过模型在响应首token选择不同思考模式（如快速回答、短思考等），以优化测试时计算分配，避免简单问题过度计算和困难问题计算不足。
- **原始摘要**: arXiv:2608.20256v1 Announce Type: new Abstract: Reasoning language models trained with reinforcement learning typically operate under a fixed token budget rather than an explicitly adaptive one, which...

### 60. MidTool: Mid-training Data Synthesis for Agentic Tool Use
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20314
- **AI 摘要**: 本文提出MidTool，一种用于智能体工具使用的中期训练数据合成方法。研究强调中期训练对塑造大语言模型能力的关键作用，并针对通用工具使用这一较少探索的智能体能力进行强化。
- **原始摘要**: arXiv:2608.20314v1 Announce Type: new Abstract: Mid-training is increasingly recognized as a critical stage for shaping the capabilities of large language models. Recent work has shown that targeted m...

### 61. Fairness-Aware Network Embeddings: Methods, Applications, and Challenges
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19381
- **AI 摘要**: 本文综述了公平感知的网络嵌入方法，探讨了现实网络中的结构性不平等如何被嵌入方法编码和放大，并介绍了公平感知嵌入的方法、应用与挑战。
- **原始摘要**: arXiv:2608.19381v1 Announce Type: cross Abstract: Network embedding methods learn low-dimensional representations of graph-structured data to support downstream tasks such as node classification, link...

### 62. HiRA-CAM: Preserving Fine-Grained Spatial Relevance in Gradient-Based Visual Explanations
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19407
- **AI 摘要**: 本文提出HiRA-CAM，一种改进的基于梯度的CNN可视化解释方法，在LayerCAM基础上保留细粒度空间相关性，以提升深度学习模型的可解释性。
- **原始摘要**: arXiv:2608.19407v1 Announce Type: cross Abstract: Deep Learning models can include billions of parameters or more, making it difficult to explain their internal transformations and outputs. However, e...

### 63. Open-Vocabulary 3D Object Detection with Co-Distillation Discovery and Dual Guidance Robust Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19973
- **AI 摘要**: 本文提出一种开放词汇3D目标检测方法，采用协同蒸馏发现和双引导鲁棒训练，以解决现有两阶段流程中定位不准确和分类不匹配的问题，提升对未见目标的检测能力。
- **原始摘要**: arXiv:2608.19973v1 Announce Type: cross Abstract: Recently, open-vocabulary 3D object detection (3D-OVD) has gained increasing attention for its ability to detect unseen objects in 3D scenes. Existing...

### 64. Towards Efficient Pareto Set Approximation via Mixture of Experts Based Model Fusion
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2024年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2406.09770
- **AI 摘要**: 本文提出基于专家混合的模型融合方法，高效逼近大规模深度神经网络的Pareto前沿，支持多任务学习和权衡分析，降低计算成本。
- **原始摘要**: arXiv:2406.09770v2 Announce Type: replace-cross Abstract: Solving multi-objective optimization problems for large deep neural networks is a challenging task due to the complexity of the loss landscape...

### 65. VISD: Enhancing Video Reasoning via Structured Self-Distillation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.06094
- **AI 摘要**: 本文提出VISD方法，通过结构化自蒸馏增强视频大语言模型的复杂推理能力，解决序列级奖励稀疏和细粒度信用分配问题，提升训练效率。
- **原始摘要**: arXiv:2605.06094v5 Announce Type: replace-cross Abstract: Training VideoLLMs for complex reasoning remains challenging due to sparse sequence level rewards and the lack of fine grained credit assignme...

### 66. A Distributional Robustness Margin For Pathology Foundation Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.25497
- **AI 摘要**: 本文针对病理基础模型中的非生物变异导致的捷径学习问题，提出分布鲁棒性边际，改进鲁棒性指数，实现跨模型可靠比较。
- **原始摘要**: arXiv:2607.25497v3 Announce Type: replace-cross Abstract: Pathology foundation models encode non-biological variation introduced by tissue preparation, staining and scanning, enabling shortcut learnin...

### 67. Anatomy Contextualized Adaptation of CT Foundation Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.27154
- **AI 摘要**: 本文提出解剖学上下文化适配方法，用于CT基础模型，在保留全局上下文的同时增强细粒度解剖特征对齐，提升下游任务性能。
- **原始摘要**: arXiv:2607.27154v2 Announce Type: replace-cross Abstract: CT vision-language foundation models have demonstrated promising performance across downstream tasks, but are typically trained with whole-vol...

### 68. Triangular Fuzzy Rescaling Distance
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19234
- **AI 摘要**: 本文提出三角模糊数距离度量方法，针对不同尺度属性需归一化的问题，引入三角模糊重缩放距离，以处理复杂系统中的不确定信息。
- **原始摘要**: arXiv:2608.19234v1 Announce Type: new Abstract: Decision-making in complex systems often involves dealing with imprecise or uncertain information, frequently represented using fuzzy sets, particularly...

### 69. Empirical Characterization of Learning Geometry in Hybrid Quantum Forecasting Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19497
- **AI 摘要**: 本文通过对比混合量子预测模型与经典基线，利用神经正切核动力学分析学习动态，在谐波混合和非平稳啁啾基准上评估核目标对齐、谱集中度等指标。
- **原始摘要**: arXiv:2608.19497v1 Announce Type: new Abstract: We characterize the learning dynamics of a compact hybrid quantum forecasting model through comparison with a structurally aligned classical baseline. U...

### 70. K\"ahler landscapes for complex neural network descents and guarantees including a search and destroy of the Calabi-Yau manifold
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19584
- **AI 摘要**: 本文研究复参数化神经网络的损失景观，从信息论流形视角出发，利用Kähler信息度量与Wirtinger Hessian分析下降路径，并探讨Calabi-Yau流形上的优化保证。
- **原始摘要**: arXiv:2608.19584v1 Announce Type: new Abstract: We study landscapes for complex-parameterized networks. Our approach is motivated with an information-theoretic manifold perspective of the parameter an...

### 71. Unregularized Convergence of Single-Loop, Entropy-Regularized Natural Actor-Critic
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19587
- **AI 摘要**: 本文分析单循环熵正则化自然演员-评论家算法，在兼容线性函数近似下，证明其未正则化目标的收敛性，弥补了理论与实践之间的差距。
- **原始摘要**: arXiv:2608.19587v1 Announce Type: new Abstract: While entropy regularization is widely used to stabilize and accelerate Natural Policy Gradient methods, its ability to yield faster convergence rates f...

### 72. Demons on a Budget: Adaptive Measurement Placement at the Entanglement Phase Transition
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19248
- **AI 摘要**: 本文研究量子电路纠缠相变中的测量放置策略，固定测量预算，比较随机、手工设计及学习策略在砖墙随机Clifford电路中的表现。
- **原始摘要**: arXiv:2608.19248v1 Announce Type: cross Abstract: Monitored quantum circuits exhibit a measurement-induced phase transition between volume-law and area-law entanglement as a function of the measuremen...

### 73. Quantum Gaussian processes for prediction of channel observations
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19306
- **AI 摘要**: 本文扩展量子高斯过程回归框架至非酉演化，证明未知量子通道输出收敛性，用于预测泡利可观测量期望值，减少测量次数。
- **原始摘要**: arXiv:2608.19306v1 Announce Type: cross Abstract: Given a set of input states, we consider the task of predicting the expectation value of a Pauli observable at the output of an unknown quantum evolut...

### 74. A Layered Simplex Architecture for Large Alphabets
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19908
- **AI 摘要**: 本文介绍了一种用于大字母表概率估计的新型贝叶斯估计器，其构造简单，通过坐标乘法和重归一化实现，深度是唯一结构参数，平均深度可消除超参数。
- **原始摘要**: arXiv:2608.19908v1 Announce Type: cross Abstract: Probability estimation over large alphabets under log loss is a well-studied problem, with celebrated methods such as the Good-Turing estimator. We in...

### 75. ProteinZero: Self-Improving Protein Generation via Online Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2506.07459
- **AI 摘要**: ProteinZero是一个在线强化学习框架，用于逆向折叠模型，通过计算高效的反馈实现可扩展、自动化的持续自我改进，提高蛋白质生成的成功率。
- **原始摘要**: arXiv:2506.07459v4 Announce Type: replace Abstract: Protein generative models have shown remarkable promise in protein design, yet their success rates remain constrained by reliance on curated sequenc...

### 76. Maximum Likelihood Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.02710
- **AI 摘要**: 本文指出当反馈是终端且二值时，模型隐式诱导正确轨迹的似然，最大似然是自然框架，但RL用于解决不可微性，并证明了相关理论。
- **原始摘要**: arXiv:2602.02710v2 Announce Type: replace Abstract: Reinforcement learning (RL) is the method of choice for training models in setups where the objective function can only be evaluated by sampling fro...

### 77. Higher Resolution, Better Generalization: Unlocking Visual Scaling in Deep Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.10546
- **AI 摘要**: 本文研究表明，像素级深度强化学习智能体使用更高分辨率的观测可以显著提升性能和泛化能力，前提是网络架构能处理高分辨率输入。
- **原始摘要**: arXiv:2605.10546v2 Announce Type: replace Abstract: Pixel-based deep reinforcement learning agents are typically trained on heavily downsampled visual observations, a convention inherited from early b...

### 78. The Price of Hidden Curvature: Improved Lower Bounds for Bandit Convex Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.18652
- **AI 摘要**: 本文建立了随机带状凸优化的最小最大遗憾下界，证明其本质上比线性带状更难，首次超过d√n依赖。
- **原始摘要**: arXiv:2607.18652v3 Announce Type: replace-cross Abstract: We establish improved lower bounds on the minimax expected regret of stochastic bandit convex optimization for $1$-Lipschitz functions on the...

### 79. Learning Asymptotics with Convergence-Rate Guarantees using Linear Least Squares
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.23287
- **AI 摘要**: 本文提出渐近学习理论（ALT），结合优化与渐近分析，统一计算渐近展开中的未知常数/参数，并研究两种数值方法。
- **原始摘要**: arXiv:2607.23287v2 Announce Type: replace-cross Abstract: We introduce a new research area that is called Asymptotics Learning Theory (ALT) and combines optimization with asymptotic analysis. In parti...

### 80. Which Negatives Matter? Ask Your Text Encoder: Adaptive Similarity Margins for Dense-Caption Retrieval
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18521
- **AI 摘要**: 密集字幕检索中，现有方法使用InfoNCE目标在强预训练初始化下过早饱和。本文提出自适应相似度边际，利用文本编码器区分负样本重要性。
- **原始摘要**: arXiv:2608.18521v2 Announce Type: replace-cross Abstract: Dense-caption retrieval has recently been improved by introducing segmentation, edge maps, LLM-filtered captions, and cross-modal modules into...

### 81. Route by Kinematics, Act by Observation: Kinematics-Supervised Expert Routing in MoE-Augmented VLA
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.26807
- **AI 摘要**: MoE增强的VLA模型在专家路由上因动作运动学异质性而失效。本文发现语义不同的操作任务可归结为多种运动学原型，提出运动学监督的显式路由方法，提升专家路由效率。
- **原始摘要**: arXiv:2607.26807v2 Announce Type: replace Abstract: While MoE augments VLA via expert specialization, router suffers from ineffective expert routing owing to the kinematic heterogeneity of actions acr...

### 82. Graph Surgery and the Do-Operator: A Precise Correspondence for Acyclic Structural Causal Models
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.17634
- **AI 摘要**: 论文精确对应无环结构因果模型中的图手术与do算子，从依赖级别比较删除箭头与替换机制的操作，澄清两者在数学上的等价性条件。
- **原始摘要**: arXiv:2608.17634v2 Announce Type: replace-cross Abstract: The $\operatorname{do}$-operator is described graphically by deleting arrows into its targets and functionally by replacing their mechanisms w...

### 83. Aug 12, 2026Introducing Grok 4.6
- **来源**: xAI Blog (TIER1)
- **发布日期**: Aug 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://x.ai/news/grok-4-6
- **AI 摘要**: 正式发布Grok 4.6模型，介绍了其新特性、性能提升和适用场景，展示了在自然语言处理和多任务方面的进步。

### 84. Qwen3Guard: Real-time Safety for Your Token Stream
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen3guard/
- **AI 摘要**: Qwen3Guard是Qwen系列首个安全护栏模型，基于Qwen3微调，用于提示和响应的安全分类，提供风险等级和分类，实现精准内容审核，确保AI交互安全。
- **原始摘要**: Tech Report GitHub Hugging Face ModelScope DISCORD Introduction We are excited to introduce Qwen3Guard, the first safety guardrail model in the Qwen family. Built upon the powerful Qwen3 foundation mo...

### 85. Qwen-Image-Edit: Image Editing with Higher Quality and Efficiency
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image-edit/
- **AI 摘要**: Qwen-Image-Edit是基于Qwen-Image的图像编辑模型，扩展了文本渲染能力，结合Qwen2.5-VL和VAE编码器，实现高质量、高效的图像编辑，支持精确文本编辑。
- **原始摘要**: QWEN CHAT GITHUB HUGGING FACE MODELSCOPE DISCORD We are excited to introduce Qwen-Image-Edit, the image editing version of Qwen-Image. Built upon our 20B Qwen-Image model, Qwen-Image-Edit successfully...

### 86. Qwen-Image: Crafting with Native Text Rendering
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image/
- **AI 摘要**: Qwen-Image是一个20B参数的MMDiT图像基础模型，在复杂文本渲染和精确图像编辑方面取得显著进展，支持多行布局、段落级语义和细粒度细节，支持字母语言。
- **原始摘要**: GITHUB HUGGING FACE MODELSCOPE DEMO DISCORD We are thrilled to release Qwen-Image, a 20B MMDiT image foundation model that achieves significant advances in complex text rendering and precise image edi...

### 87. GSPO: Towards Scalable Reinforcement Learning for Language Models
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/gspo/
- **AI 摘要**: GSPO是一种可扩展的语言模型强化学习方法，解决现有RL算法（如GRPO）在长训练中的不稳定性和模型崩溃问题，通过改进训练动态，提升计算效率和性能。
- **原始摘要**: PAPER DISCORD Introduction Reinforcement Learning (RL) has emerged as a pivotal paradigm for scaling language models and enhancing their deep reasoning and problem-solving capabilities. To scale RL, t...

### 88. New Kimi K2 Models & Updated Pricing
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/Kimi_API_Newsletter
- **AI 摘要**: 发布了新的Kimi K2模型及更新后的定价方案，介绍了模型性能提升和价格调整，为用户提供更优的AI服务选择。

### 89. Kimi K2: Open Agentic Intelligence
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/k2-report
- **AI 摘要**: Kimi K2作为开放智能体智能的模型，强调了其在自主决策和任务执行方面的能力，展示了开放生态下的智能体应用前景。

### 90. Machine Learning23
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://tenstorrent.com/newsroom/newsroom/tags/machine-learning
- **AI 摘要**: 文章标题为“Machine Learning23”，可能讨论机器学习相关主题，但具体内容未提供，无法生成详细摘要。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
