# RSS 聚合报告 - AI模型

**生成时间**: 2026-08-21 14:23:17
**文章数量**: 90 篇

---

### 1. Is KV Cache in a high dimensional vector space? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T18:18:10+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtrdem/is_kv_cache_in_a_high_dimensional_vector_space_d/
- **AI 摘要**: 作者研究KV缓存是否处于高维向量空间，认为其不是扁平列表，而是具有可导航几何结构的向量集合，键携带模型学习到的关联关系，对存储和检索有影响。
- **原始摘要**: I've been doing some research on this question: At inference time a large part of a model's working memory lives in the KV cache, plus whatever external memory the harness bolts on. I've been poking a...

### 2. Mapping intrinsic rank and informational gravity in complex tabular data: I developed a non-parametric, model-agnostic, information-theoretic diagnostic to bypass the limits of linear, rank, and Euclidean baselines. [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T13:34:28+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtjotb/mapping_intrinsic_rank_and_informational_gravity/
- **AI 摘要**: 作者提出一种非参数、模型无关的信息论诊断方法，用于映射复杂表格数据的内在秩和信息引力，以克服线性、秩和欧几里得基线的局限，并发布了预印本和开源工具。
- **原始摘要**: Links: Preprint: https://doi.org/10.5281/zenodo.22028087 Entropic Scree Function v1.0.0 / GitHub: https://github.com/tjleestjohn/Entropic-Scree TL;DR: Standard PCA fundamentally fractures non-linear d...

### 3. The spectral neuron - an ML primitive for scalable and interpretable models [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T10:20:47+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtfimo/the_spectral_neuron_an_ml_primitive_for_scalable/
- **AI 摘要**: 作者在雅虎广告团队工作期间，探索是否存在既简单、可扩展、可解释又可控制的机器学习模型，并由此发展出“谱神经元”这一ML原语，相关研究已形成预印本。
- **原始摘要**: Worked some time ago on one of the ad teams at Yahoo, and this grew out of a question I kept returning to while there are there "simple" models that are both simple, scalable, interpretable, and contr...

### 4. About the impact of grouping classes in multiclass classification [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T07:42:20+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtctaz/about_the_impact_of_grouping_classes_in/
- **AI 摘要**: 讨论多分类问题中将多个类别分组对模型性能的影响，作者询问是否有相关研究或共识，以评估这种分组操作的潜在危害。
- **原始摘要**: A premise: I hope this question is "worth" of this subreddit, I did a decent amount of research before posting, I thought it was potentially interesting enough for it, but possibly not basic enough fo...

### 5. Same GRPO recipe on three from-scratch LLMs (353M/316M/672M) gave three different outcomes, with no clean relationship to scale [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T21:30:26+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vszsit/same_grpo_recipe_on_three_fromscratch_llms/
- **AI 摘要**: 作者用相同GRPO配方训练三个不同规模的LLM（353M/316M/672M），结果表现各异，且与规模无清晰关系。预训练正常，但GRPO对两个较大模型产生负面影响，原因不明。
- **原始摘要**: I trained three LLMs from scratch in raw PyTorch then post-trained each one with SFT and then GRPO. Same process every time: same synthetic arithmetic curriculum, same reward function, same hyperparam...

### 6. How much of the weight-space perception gap is actually symmetry? Evidence from ~1.8M fitted SIRENs [R]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-19T19:24:12+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vswdnf/how_much_of_the_weightspace_perception_gap_is/
- **AI 摘要**: 作者通过约180万次SIREN拟合实验，探讨权重空间感知差距中有多少源于参数对称性，发现共享初始化时权重语义读取有效，独立拟合时失效，对称性解释可能不充分。
- **原始摘要**: I’ve been looking at a fairly basic question in weight-space learning that I don’t think gets separated cleanly enough: Why does reading semantics directly from neural network weights work pretty well...

### 7. Trained an diffusion model that runs on 264KB of RAM [P]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-18T09:26:21+00:00 (3 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vrk7t5/trained_an_diffusion_model_that_runs_on_264kb_of/
- **AI 摘要**: 作者训练了一个仅需264KB RAM即可运行的扩散模型，并展示了相关成果，可能涉及模型压缩或轻量化技术。
- **原始摘要**: I recently bought a Shrike lite which has got 264KB of SRAM. I decided to train an image generation model that generates 32*32 pixel images. The microcontroller also has an FPGA onboard which I used t...

### 8. Revisiting the Efficient Channel Attention paper (2019, 12k citations) - the central hypothesis isn't quite right [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-16T10:13:44+00:00 (5 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/
- **AI 摘要**: 本文重新审视了2019年提出的高效通道注意力（ECA）论文，指出其核心假设可能不完全正确。ECA通过一维卷积直接处理通道均值，避免了降维，相比SE注意力有显著改进，但作者对跨通道交互的假设存在疑问。
- **原始摘要**: ECA was positioned as a successor to SE. The idea behind ECA is quite simple. Unlike SE which reduces the channel means into a smaller hidden layer, it directly uses a 1d convolution kernel on the cha...

### 9. How can we solve long-range recall in linear attention? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-16T07:47:09+00:00 (5 天前)
- **类型**: forum
- **优先级**: low
- **分类**: AI模型
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/
- **AI 摘要**: 本文探讨了线性注意力在长序列（如DNA序列，可达100万token）中的长程记忆问题。作者发现模型在Needle-in-a-Haystack基准上表现不佳，面临长程召回挑战，并寻求解决方案。
- **原始摘要**: Recently, I started working on DNA sequence modeling and decided to explore linear attention, mainly because DNA sequences can easily reach 1M tokens, making standard softmax attention extremely expen...

### 10. Up to 3.2x Faster Inference with LFM2.5-DSpark
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Thu, 20 Aug 2026 16:52:57 GMT (今天)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/LiquidAI/lfm25-dspark
- **AI 摘要**: 本文介绍LFM2.5-DSpark模型，通过优化推理过程，实现了最高3.2倍的推理加速，提升了模型在部署场景中的效率。

### 11. v1.6.0: Mistrall goes Small 3.1 with vision
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2025-03-20T15:03:08Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.6.0
- **AI 摘要**: Mistral推理库v1.6.0版本更新，新增对Mistral Small 3.1模型的支持，该模型具备视觉能力，并修复了换行缺失问题。
- **原始摘要**: What's Changed Missing new line by @theophilegervet in #234 Add support to Mistral Small 3.1 by @juliendenize in #239 Remove file refs by @juliendenize in #240 Release 1.6.0 by @juliendenize in #241 N...

### 12. v1.4.0: Pixtral 👀
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-09-13T13:10:17Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.4.0
- **AI 摘要**: Mistral推理库v1.4.0版本发布，正式支持Pixtral多模态模型，使Mistral模型具备视觉理解能力，用户可通过升级库进行下载使用。
- **原始摘要**: Pixtral Mistral models can now 👀 ! pip install --upgrade mistral_inference # >= 1.4.0 Download: from huggingface_hub import snapshot_download from pathlib import Path mistral_models_path = Path.home()...

### 13. v1.3.0 Mistral-Nemo
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-18T15:45:30Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.3.0
- **AI 摘要**: Mistral推理库v1.3.0版本发布，引入与NVIDIA合作开发的Mistral-Nemo模型，提供安装和下载指引。
- **原始摘要**: Welcome Mistral-Nemo from Mistral 🤝 NVIDIA Read more about Mistral-Nemo here. Install pip install mistral-inference>=1.3.0 Download export NEMO_MODEL=$HOME/12B_NEMO_MODEL wget https://models.mistralcd...

### 14. v1.2.0 Add Mamba
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-16T18:41:37Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.2.0
- **AI 摘要**: Mistral推理库v1.2.0版本发布，新增对Codestral-Mamba和Mathstral模型的支持，并提供了相关依赖安装和下载说明。
- **原始摘要**: Welcome 🐍 Codestral-Mamba and 🔢 Mathstral pip install mistral-inference>=1.2.0 Codestral-Mamba pip install packaging mamba-ssm causal-conv1d transformers Download export MAMBA_CODE=$HOME/7B_MAMBA_CODE...

### 15. Clustering and Token Denoising for Faster and More Robust VLMs
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19285
- **AI 摘要**: 本文提出ClustRS方法，通过聚类和令牌去噪技术，减少视觉语言模型（VLM）的视觉令牌数量，在无需重新训练的情况下提升边缘部署的效率和鲁棒性。
- **原始摘要**: arXiv:2608.19285v1 Announce Type: new Abstract: Recent Visual-Language Models (VLMs) have enhanced the capabilities of pre-trained LLMs by adding vision tokens alongside text, with approaches like LLa...

### 16. Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19669
- **AI 摘要**: 本文识别多模态推理中潜在视觉目标表示的两阶段训练框架的局限性，并优化SFT和RL阶段的潜在令牌，提升推理性能。
- **原始摘要**: arXiv:2608.19669v1 Announce Type: new Abstract: Latent reasoning has advanced multimodal reasoning through a two-stage training paradigm: (1) a helper image is encoded into latent tokens to teach visu...

### 17. V-REX: Efficient Specialist VLM Training for Veterinary X-Rays
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20069
- **AI 摘要**: 本文展示在兽医放射学中，通过重新设计VLM流水线（从分词到推理），小模型可从零训练超越大型基础模型，无需昂贵微调。
- **原始摘要**: arXiv:2608.20069v1 Announce Type: new Abstract: While generalist VLMs are expensive to train, creating domain experts is widely assumed to require fine-tuning increasingly large foundation models. We...

### 18. ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20122
- **AI 摘要**: 本文提出ArmorOCR，通过观察转移自蒸馏方法，增强大型多模态模型对对抗性视觉文本的定位和识别能力，并构建大规模对抗OCR基准。
- **原始摘要**: arXiv:2608.20122v1 Announce Type: new Abstract: Large multimodal models (LMMs) have demonstrated strong OCR recognition capabilities, yet remain vulnerable to adversarial visual text that is readable...

### 19. ID-VTG: Image-Disambiguated Video Temporal Grounding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20127
- **AI 摘要**: 本文提出图像消歧视频时间定位任务，利用参考图像和文本的多模态查询，解决自然语言难以准确描述视觉属性导致的事件区分难题。
- **原始摘要**: arXiv:2608.20127v1 Announce Type: new Abstract: Video Temporal Grounding (VTG) faces significant challenges when natural language queries must distinguish between multiple events involving visually si...

### 20. DPC-Net: Dual-Prior Collaborative Network for All-in-One Image Restoration
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20141
- **AI 摘要**: 本文提出双先验协作网络，联合利用退化建模和低层视觉先验，解决全合一图像恢复中结构失真和语义不一致问题，实现高质量恢复。
- **原始摘要**: arXiv:2608.20141v1 Announce Type: new Abstract: All-in-One Image Restoration (AiOIR) aims to handle diverse degradations within a unified model. However, existing methods often overlook image semantic...

### 21. Zoom-IQA: Image Quality Assessment with Reliable Region-Aware Reasoning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.02918
- **AI 摘要**: 本文提出Zoom-IQA方法，通过可靠区域感知推理，结合质量描述和分数，解决基于视觉语言模型的图像质量评估中推理不可靠问题。
- **原始摘要**: arXiv:2601.02918v4 Announce Type: replace Abstract: Image Quality Assessment (IQA) is a long-standing problem in computer vision. Previous methods typically focus on predicting numerical scores withou...

### 22. Video Evidence to Reasoning Efficient Video Understanding via Explicit Evidence Grounding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.07761
- **AI 摘要**: 本文提出证据链框架，解耦并协同优化感知基础和推理效率，解决大视觉语言模型在视频推理中计算成本高和幻觉风险的问题。
- **原始摘要**: arXiv:2601.07761v2 Announce Type: replace Abstract: Large Vision-Language Models (LVLMs) face a fundamental dilemma in video reasoning: they are caught between the prohibitive computational costs of v...

### 23. Reinforcing Egocentric Spatial Perception in Multimodal Large Language Models via Ego Scene Augmentation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.14497
- **AI 摘要**: 本文针对多模态大语言模型在复杂自我中心场景中空间推理能力不足的问题，提出了自我中心场景增强（ESA）框架，通过场景增强提升模型的空间感知能力，以改善自我中心视觉问答任务。
- **原始摘要**: arXiv:2607.14497v2 Announce Type: replace Abstract: Egocentric Visual Question Answering (VQA) has attracted widespread attention as an important task for enabling Multimodal Large Language Models (ML...

### 24. Deep Multimodal Fusion Detection through Spatial Mask and Channel Fusion
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.02092
- **AI 摘要**: 本文提出了一种基于注意力驱动的互补性重建的深度多模态融合目标检测方法，通过空间掩码和通道融合解决双骨干架构中单模态过拟合或过度专门化的问题。
- **原始摘要**: arXiv:2608.02092v2 Announce Type: replace Abstract: Deep multimodal fusion for object detection has demonstrated good performance through mining modal characteristics. However, existing feature-level...

### 25. Gemma 4 on Cerebras—The Fastest Inference is Now MultimodalJune 29, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 29, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/gemma-4-on-cerebras-the-fastest-inference-is-now-multimodal
- **AI 摘要**: Cerebras宣布Gemma 4模型在其平台上实现最快多模态推理，支持图像、文本等多种输入，显著提升处理速度。

### 26. The Economics of AI ReasoningJune 17, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 17, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/the-economics-of-ai-reasoning
- **AI 摘要**: 文章分析了AI推理的经济成本，讨论了推理计算资源消耗、成本优化策略以及如何平衡推理质量与成本，为AI系统设计提供经济视角。

### 27. The world’s fastest GLM-4.6 – now available on CerebrasNovember 18, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 18, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm
- **AI 摘要**: GLM-4.6模型在Cerebras平台上提供全球最快的推理速度，强调其性能优势，并可能吸引更多用户采用。

### 28. REAP: One-Shot Pruning for Trillion-Parameter Mixture-of-Experts ModelsOctober 16, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 16, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/reap
- **AI 摘要**: 提出REAP方法，用于万亿参数混合专家模型的一次性剪枝，显著降低计算成本并保持模型性能。

### 29. MoE Math Demystified: What Does 8x7B Actually Mean?October 14, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 14, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/moe-guide-calculator
- **AI 摘要**: 解释混合专家模型中8x7B参数的含义，澄清计算量、参数量与模型性能的关系，帮助理解MoE架构。

### 30. Thinking Inside the Box: The Implicit Chain Transformer for Efficient State TrackingDecember 12, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 12, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/thinking-inside-the-box-the-implicit-chain-transformer-for-efficient-state-tracking
- **AI 摘要**: 提出隐式链式变换器（Implicit Chain Transformer）用于高效状态跟踪，通过盒内思考方式优化模型性能，减少计算开销。

### 31. Jais 2: A Blueprint for Sovereign AIDecember 09, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 09, 2025
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/jais2
- **AI 摘要**: Jais 2模型作为主权AI的蓝图，展示了如何构建自主可控的AI系统，强调数据隐私和本地化部署的重要性。

### 32. Why speed wins: faster inference is about more than just quicker answers–it’s the new path to accuracyFebruary 19, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/speedandaccuracyblog
- **AI 摘要**: 文章强调更快推理速度不仅是响应更快，更是提升准确性的新途径，通过加速迭代和实时反馈优化模型性能。

### 33. Introducing OpenAI GPT-5.3-Codex-Spark Powered by CerebrasFebruary 12, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 12, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/openai-codexspark
- **AI 摘要**: OpenAI推出GPT-5.3-Codex-Spark模型，由Cerebras硬件驱动，主打高速推理和代码生成能力，面向开发者场景。

### 34. This new model is smarter than Sonnet 4.5…and 20X faster?January 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7-migration-guide
- **AI 摘要**: 介绍一款新模型，声称比Sonnet 4.5更智能且速度快20倍，分析其架构创新和实际性能表现。

### 35. GLM-4.7: Frontier intelligence at record speed — now available on CerebrasJanuary 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7
- **AI 摘要**: GLM-4.7模型在Cerebras平台上以创纪录速度运行，展示了前沿智能与高速推理的结合，为用户提供更高效的AI服务。

### 36. Transformer Models for Text Summarization: A Comparative Study of BART, BERT, and RoBERTa
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19200
- **AI 摘要**: 本文比较了BART、BERT和RoBERTa三种Transformer模型在文本摘要任务上的表现，探讨了自动文本摘要的分类方法及模型性能差异。
- **原始摘要**: arXiv:2608.19200v1 Announce Type: new Abstract: Text summarization refers to the task of condensing a document into a shorter version while preserving its key information. Automatic text summarization...

### 37. Asymmetric Attention Heads: Structured Head-Wise Context Allocation for Transformer Attention
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19203
- **AI 摘要**: 本文提出非对称注意力头（AAH）框架，将上下文长度作为显式资源按头分配，使不同注意力头根据角色使用不同长度的上下文，提升Transformer注意力效率。
- **原始摘要**: arXiv:2608.19203v1 Announce Type: new Abstract: Standard multi-head attention (MHA) gives every head the same full causal context span, although heads can serve different contextual roles. Some heads...

### 38. When Irrelevant Text Matters: Affine Margin Shifts in Multimodal Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19208
- **AI 摘要**: 本文研究多模态大语言模型中任务无关文本对视觉判断的影响，通过受控干预发现无关文本会一致性地引入偏差，导致仿射边际偏移。
- **原始摘要**: arXiv:2608.19208v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) are frequently exposed to auxiliary textual context, the impact of which on visually grounded tasks remains und...

### 39. Represented but Ignored: A Causal Account of Prosodic Underuse in Audio-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19211
- **AI 摘要**: 本文从因果角度分析音频语言模型对韵律信息利用不足的原因，区分是声学信息丢失还是模型未能利用，以改进表达性语音理解。
- **原始摘要**: arXiv:2608.19211v1 Announce Type: new Abstract: Human speech is richly expressive, with prosody carrying linguistic and emotional information beyond the lexical content. A capable large audio-language...

### 40. Are LLMs becoming similarly creative? Evidence from three years of models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19437
- **AI 摘要**: 本文初步分析三年间LLM在开放式任务上的创造性表现，关注创造力、原创性和多样性趋势，为理解模型在创意支持场景中的能力演变提供证据。
- **原始摘要**: arXiv:2608.19437v1 Announce Type: new Abstract: Many benchmarks track Large Language Model (LLM) performance on tasks with verifiable answers, but less is known about how LLM performance is evolving o...

### 41. When Machines Speak: A Unified Generative Framework for Integrating Machine-Native Symbols into Pretrained Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19529
- **AI 摘要**: 本文提出UniLang统一生成框架，将机器原生符号集成到预训练LLM中，弥合语言建模与结构化预测之间的鸿沟，支持真实AI系统中的离散符号表示。
- **原始摘要**: arXiv:2608.19529v1 Announce Type: new Abstract: Many real-world AI systems represent entities, behaviors, and structured information using discrete machine-native symbols rather than natural language....

### 42. Projector Is All You Train
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19726
- **AI 摘要**: 本文探究多模态大语言模型适应新模态时是否必须微调主干网络。通过在3D多模态模型上的实验，发现仅训练投影器即可达到与现有基线相当的强多模态性能。
- **原始摘要**: arXiv:2608.19726v1 Announce Type: new Abstract: The typical training process of a multimodal large language model (MLLM) involves adapting both the language model backbone and the projector between th...

### 43. Interrupting the Loop: Periodic Subject Changes Raise Judged Surprise and Connection in Base Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19893
- **AI 摘要**: 本文拆解了认知启发的生成循环，在三个基础模型上测试24种条件，发现大部分效果源于周期性注入新主题的打断操作。LLM评判员仅基于生成文本窗口评估，可感知惊讶度和连接性。
- **原始摘要**: arXiv:2608.19893v1 Announce Type: new Abstract: Where does the novelty a base language model produces with no task come from, and what can an LLM judge of a long stream actually see? We dismantle a co...

### 44. Learning how to Forget: Fine-tuning for Long-Context Sparse Attention
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19920
- **AI 摘要**: 本文提出一种针对稀疏注意力微调模型的新方法，适用于任意KV缓存策略，可在中等硬件预算（如单块A100 40GB）下运行，使模型与策略协同适应，通常优于现有方法。
- **原始摘要**: arXiv:2608.19920v1 Announce Type: new Abstract: A lot of prior work addressed key-value (KV) cache selection and compression by sparse attention to enable long-context inference for transformer langua...

### 45. PEA-DPO: Perception-Enhanced Alignment Direct Preference Optimization for MLLMs Alignment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19598
- **AI 摘要**: 本文提出PEA-DPO，一种用于多模态大语言模型对齐的感知增强直接偏好优化方法。通过表征分析发现多模态偏好优化中的视觉不敏感问题，即模型难以区分原始图像与移除关键视觉上下文的图像，并针对此进行改进。
- **原始摘要**: arXiv:2608.19598v1 Announce Type: cross Abstract: Direct Preference Optimization (DPO) has emerged as an effective approach for aligning large language models (LLMs) with human preferences. However, i...

### 46. TempJail: Temporal Jailbreak Attack against Large Vision-Language Models via Subtitle Scheduling
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19737
- **AI 摘要**: 本文提出TempJail，一种通过字幕调度对大型视觉语言模型进行时间越狱攻击的方法。研究发现越狱效果不仅取决于视频中嵌入的文本内容，还取决于信息随时间组织的方式，现有视频越狱方法忽视了这一点。
- **原始摘要**: arXiv:2608.19737v1 Announce Type: cross Abstract: Large vision-language models (LVLMs) have achieved remarkable progress in video understanding and reasoning. Despite extensive studies on text- and im...

### 47. Let's Scale Step by Step: Compute-Efficient Hyperparameter Transfer for Large-Scale Mixture-of-Experts
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20061
- **AI 摘要**: 本文提出一种计算高效的两步超参数迁移框架，用于大规模混合专家（MoE）模型的最优学习率估计。MoE架构扩展模型容量而不成比例增加计算成本，但在极端规模和token预算下通过扫描优化超参数在计算上不可行。
- **原始摘要**: arXiv:2608.20061v1 Announce Type: cross Abstract: Mixture-of-Experts (MoE) architectures significantly expand model capacity without a proportional increase in computational cost. However, optimizing...

### 48. Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20210
- **AI 摘要**: 本文介绍Daedalus-150M，一种为CPU推理设计的卷积-注意力混合小语言模型。模型在18个块中仅6个使用全注意力，其余12个使用短卷积，内存宽度固定，适合单用户单token的CPU推理场景。
- **原始摘要**: arXiv:2608.20210v1 Announce Type: cross Abstract: Small language models are usually built like large ones and then squeezed onto a CPU afterwards. We did the opposite: we fixed the target first, one u...

### 49. TS-Reasoner: Aligning Time Series Foundation Models with LLM Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2510.03519
- **AI 摘要**: 本文提出TS-Reasoner，将时间序列基础模型与LLM推理对齐，以增强时间序列推理能力，应用于金融、能源等领域。
- **原始摘要**: arXiv:2510.03519v3 Announce Type: replace Abstract: Time series reasoning is crucial to decision-making in diverse domains, including finance, energy, and scientific discovery. While existing time ser...

### 50. Remask, Don't Replace: Token-to-Mask Refinement in Diffusion Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.18738
- **AI 摘要**: 本文提出Token-to-Mask（T2M）方法，一种无需训练的推理时修正技术，用于改善扩散语言模型生成文本的一致性。
- **原始摘要**: arXiv:2604.18738v3 Announce Type: replace Abstract: Diffusion language models (dLLMs) generate text through iterative denoising, filling multiple masked positions at each step. Positions filled in the...

### 51. RepSelect: Robust LLM Unlearning via Representation Selectivity
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.17168
- **AI 摘要**: 本文提出RepSelect方法，通过表示选择性实现鲁棒的LLM遗忘，解决现有遗忘技术浅层、易被对抗性恢复且损害通用能力的问题，确保危险知识被深度移除。
- **原始摘要**: arXiv:2606.17168v3 Announce Type: replace Abstract: When LLM weights are open or fine-tuning is available through an API, suppressing hazardous knowledge and tendencies is not enough: removal has to b...

### 52. Language Has Two Parameters: Narrative-Induced Semantic Plasticity and Phase-Sensitive Interpretation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18041
- **AI 摘要**: 本文提出语言具有两个参数：叙事诱导的语义可塑性和相位敏感解释，认为叙事遭遇改变读者语义关系，产生个体和共享历史，而人口训练的语言模型未必保留这些历史。
- **原始摘要**: arXiv:2608.18041v2 Announce Type: replace Abstract: Reading fiction or encountering narrative generally does not merely add information. The encounter changes the reader. This paper proposes that enco...

### 53. Towards Audio Token Compression in Large Audio Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2511.20973
- **AI 摘要**: 本文探讨大型音频语言模型（LALM）中音频编码器产生高令牌率的问题，研究无监督分割、均匀平均池化等技术以减少音频令牌数量，降低注意力计算成本，提升模型可扩展性。
- **原始摘要**: arXiv:2511.20973v2 Announce Type: replace-cross Abstract: Large Audio Language Models (LALMs) deliver strong performance across speech and audio tasks, but their audio encoders generate high-rate toke...

### 54. Transformer See, Transformer Do: Copying as an Intermediate Step in Learning Analogical Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.06501
- **AI 摘要**: 本文研究Transformer在类比推理中的学习机制，使用元学习组合性（MLC）训练模型完成字母串类比任务，发现复制作为中间步骤有助于提升泛化能力，并评估其表现。
- **原始摘要**: arXiv:2604.06501v2 Announce Type: replace-cross Abstract: Analogical reasoning is a hallmark of human intelligence, enabling us to solve new problems by transferring knowledge from one situation to an...

### 55. Geometric and Behavioral Stratification in Transformer Residual Streams
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.12447
- **AI 摘要**: 本文研究Transformer残差流中的特权基，发现预测方向作为内容定义的锚点，残差流变化在几何和行为上呈现分层结构，为理解模型内部表征提供新视角。
- **原始摘要**: arXiv:2608.12447v3 Announce Type: replace-cross Abstract: Trained transformer models develop privileged bases: coordinate axes whose statistics differ from the rest of the residual stream. But what ki...

### 56. Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19684
- **AI 摘要**: 本文提出一种离线质量-多样性强化学习方法，通过两阶段策略从预收集数据中提取多样化技能作为低级策略，并训练高级策略解决特定任务，以提升策略性能和样本效率。
- **原始摘要**: arXiv:2608.19684v1 Announce Type: new Abstract: Recent studies investigate how to leverage pre-collected datasets to improve the policy performance and sample efficiency of RL. One promising approach...

### 57. TT-net: Quantum Inspired Tensor Network Denoising in Conditional GANs
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19789
- **AI 摘要**: 本文介绍TT-net，一种受量子启发的张量网络去噪方法，应用于条件生成对抗网络。利用张量训练（Tensor Train）结构改进生成模型的去噪能力，展示了量子物理工具在机器学习中的新应用。
- **原始摘要**: arXiv:2608.19789v1 Announce Type: new Abstract: Developed as a workhorse for classical simulations of quantum algorithms and quantum many-body systems, Tensor Network methods have entered the scientif...

### 58. SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19842
- **AI 摘要**: 本文提出SAPO，一种单次rollout的自回归策略优化方法，用于智能体强化学习。它解决了现有critic-free方法的多rollout开销和优势估计问题，在长时程交互任务中表现优异。
- **原始摘要**: arXiv:2608.19842v1 Announce Type: new Abstract: Agentic reinforcement learning (RL) has become a critical stage in the post-training of large language models. Existing critic-free, group-relative meth...

### 59. Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20256
- **AI 摘要**: 本文研究推理语言模型如何自适应分配测试时计算资源，通过选择不同推理模式（如快速回答、短思考、长思考）来平衡计算开销和问题难度，提升推理效率。
- **原始摘要**: arXiv:2608.20256v1 Announce Type: new Abstract: Reasoning language models trained with reinforcement learning typically operate under a fixed token budget rather than an explicitly adaptive one, which...

### 60. MidTool: Mid-training Data Synthesis for Agentic Tool Use
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20314
- **AI 摘要**: 本文提出MidTool，一种用于智能体工具使用的中期训练数据合成方法。研究聚焦于增强大语言模型的通用工具使用能力，构建开放语料库，以提升智能体在软件工程等场景中的表现。
- **原始摘要**: arXiv:2608.20314v1 Announce Type: new Abstract: Mid-training is increasingly recognized as a critical stage for shaping the capabilities of large language models. Recent work has shown that targeted m...

### 61. Fairness-Aware Network Embeddings: Methods, Applications, and Challenges
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19381
- **AI 摘要**: 本文综述了公平感知的网络嵌入方法，探讨其在节点分类、链接预测等下游任务中的应用，分析现实网络中的人口失衡、同质性等结构性不平等问题，并总结了公平感知嵌入的挑战与未来方向。
- **原始摘要**: arXiv:2608.19381v1 Announce Type: cross Abstract: Network embedding methods learn low-dimensional representations of graph-structured data to support downstream tasks such as node classification, link...

### 62. HiRA-CAM: Preserving Fine-Grained Spatial Relevance in Gradient-Based Visual Explanations
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19407
- **AI 摘要**: 本文提出HiRA-CAM，一种改进的基于梯度的视觉解释方法，在LayerCAM基础上保留细粒度空间相关性，增强卷积神经网络的可解释性，适用于关键应用中的AI决策解释。
- **原始摘要**: arXiv:2608.19407v1 Announce Type: cross Abstract: Deep Learning models can include billions of parameters or more, making it difficult to explain their internal transformations and outputs. However, e...

### 63. Open-Vocabulary 3D Object Detection with Co-Distillation Discovery and Dual Guidance Robust Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19973
- **AI 摘要**: 本文提出一种开放词汇3D目标检测方法，采用共蒸馏发现和双引导鲁棒训练，改进两阶段流程中定位不准确和分类不匹配的问题，提升对未见物体的检测能力。
- **原始摘要**: arXiv:2608.19973v1 Announce Type: cross Abstract: Recently, open-vocabulary 3D object detection (3D-OVD) has gained increasing attention for its ability to detect unseen objects in 3D scenes. Existing...

### 64. CharTool: Tool-Integrated Visual Reasoning for Chart Understanding
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.02794
- **AI 摘要**: 本文提出CharTool，一种工具集成的视觉推理方法，用于图表理解。通过DuoChart数据管道生成高质量训练数据，增强多模态大模型的细粒度视觉定位和数值计算能力。
- **原始摘要**: arXiv:2604.02794v2 Announce Type: replace Abstract: Charts are ubiquitous in scientific and financial literature for presenting structured data. However, chart reasoning remains challenging for multim...

### 65. Towards Efficient Pareto Set Approximation via Mixture of Experts Based Model Fusion
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2024年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2406.09770
- **AI 摘要**: 本文提出基于混合专家模型融合的高效帕累托集逼近方法，解决大规模深度神经网络多目标优化问题，降低计算成本并支持多任务学习。
- **原始摘要**: arXiv:2406.09770v2 Announce Type: replace-cross Abstract: Solving multi-objective optimization problems for large deep neural networks is a challenging task due to the complexity of the loss landscape...

### 66. VISD: Enhancing Video Reasoning via Structured Self-Distillation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.06094
- **AI 摘要**: 本文提出VISD方法，通过结构化自蒸馏增强视频推理能力。针对视频大语言模型训练中奖励稀疏和信用分配问题，结合可验证奖励强化学习与密集自蒸馏监督，提升复杂推理效率。
- **原始摘要**: arXiv:2605.06094v5 Announce Type: replace-cross Abstract: Training VideoLLMs for complex reasoning remains challenging due to sparse sequence level rewards and the lack of fine grained credit assignme...

### 67. Anatomy Contextualized Adaptation of CT Foundation Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.27154
- **AI 摘要**: 本文提出解剖学上下文自适应方法，用于CT基础模型的微调。通过结合解剖级视觉特征与全局上下文，解决细粒度预训练中丢失全局信息的问题，提升下游任务性能。
- **原始摘要**: arXiv:2607.27154v2 Announce Type: replace-cross Abstract: CT vision-language foundation models have demonstrated promising performance across downstream tasks, but are typically trained with whole-vol...

### 68. Triangular Fuzzy Rescaling Distance
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19234
- **AI 摘要**: 本文提出三角模糊数重缩放距离度量方法，用于处理复杂系统中模糊集的不精确信息，解决异构属性尺度不同需归一化的问题。
- **原始摘要**: arXiv:2608.19234v1 Announce Type: new Abstract: Decision-making in complex systems often involves dealing with imprecise or uncertain information, frequently represented using fuzzy sets, particularly...

### 69. Empirical Characterization of Learning Geometry in Hybrid Quantum Forecasting Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19497
- **AI 摘要**: 本文通过对比混合量子预测模型与经典基线，利用神经正切核动力学分析学习动态，研究核目标对齐、核漂移等指标，揭示量子模型学习特性。
- **原始摘要**: arXiv:2608.19497v1 Announce Type: new Abstract: We characterize the learning dynamics of a compact hybrid quantum forecasting model through comparison with a structurally aligned classical baseline. U...

### 70. K\"ahler landscapes for complex neural network descents and guarantees including a search and destroy of the Calabi-Yau manifold
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19584
- **AI 摘要**: 本文研究复参数化神经网络的损失景观，从信息论流形视角出发，利用Kähler信息度量与Wirtinger Hessian分析下降路径，提供优化保证。
- **原始摘要**: arXiv:2608.19584v1 Announce Type: new Abstract: We study landscapes for complex-parameterized networks. Our approach is motivated with an information-theoretic manifold perspective of the parameter an...

### 71. Unregularized Convergence of Single-Loop, Entropy-Regularized Natural Actor-Critic
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19587
- **AI 摘要**: 本文分析单循环熵正则化自然演员-评论家算法，在兼容线性函数近似下证明其未正则化目标的收敛性，弥合理论与实践差距。
- **原始摘要**: arXiv:2608.19587v1 Announce Type: new Abstract: While entropy regularization is widely used to stabilize and accelerate Natural Policy Gradient methods, its ability to yield faster convergence rates f...

### 72. Demons on a Budget: Adaptive Measurement Placement at the Entanglement Phase Transition
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19248
- **AI 摘要**: 本文研究监测量子电路中的纠缠相变，固定测量预算并比较随机、手工设计及学习策略的测量放置，探索自适应放置的影响。
- **原始摘要**: arXiv:2608.19248v1 Announce Type: cross Abstract: Monitored quantum circuits exhibit a measurement-induced phase transition between volume-law and area-law entanglement as a function of the measuremen...

### 73. Quantum Gaussian processes for prediction of channel observations
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19306
- **AI 摘要**: 本文扩展量子高斯过程回归至非酉演化，预测未知量子通道输出中泡利可观测量的期望值，证明通道输出收敛性。
- **原始摘要**: arXiv:2608.19306v1 Announce Type: cross Abstract: Given a set of input states, we consider the task of predicting the expectation value of a Pauli observable at the output of an unknown quantum evolut...

### 74. A Layered Simplex Architecture for Large Alphabets
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.19908
- **AI 摘要**: 本文提出了一种用于大字母表概率估计的新型贝叶斯估计器，通过坐标独立均匀采样并归一化构建，结构简单且具有多个优良性质。
- **原始摘要**: arXiv:2608.19908v1 Announce Type: cross Abstract: Probability estimation over large alphabets under log loss is a well-studied problem, with celebrated methods such as the Good-Turing estimator. We in...

### 75. Maximum Likelihood Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.02710
- **AI 摘要**: 本文指出当反馈为终端且二元时，模型隐式诱导正确轨迹的似然，最大似然是自然框架，但强化学习被用作非可微性的变通方法，并证明了相关性质。
- **原始摘要**: arXiv:2602.02710v2 Announce Type: replace Abstract: Reinforcement learning (RL) is the method of choice for training models in setups where the objective function can only be evaluated by sampling fro...

### 76. Higher Resolution, Better Generalization: Unlocking Visual Scaling in Deep Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.10546
- **AI 摘要**: 本文研究表明，像素级深度强化学习智能体的观察分辨率是关键变量，更高分辨率输入可显著提升性能与泛化能力，前提是网络架构能处理。
- **原始摘要**: arXiv:2605.10546v2 Announce Type: replace Abstract: Pixel-based deep reinforcement learning agents are typically trained on heavily downsampled visual observations, a convention inherited from early b...

### 77. The Price of Hidden Curvature: Improved Lower Bounds for Bandit Convex Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.18652
- **AI 摘要**: 本文建立了随机带状凸优化的改进下界，证明其比线性带状问题更难，首次超过d√n依赖，为时间范围n≥d^(10/3)提供Ω(d^(4/3)√n)下界。
- **原始摘要**: arXiv:2607.18652v3 Announce Type: replace-cross Abstract: We establish improved lower bounds on the minimax expected regret of stochastic bandit convex optimization for $1$-Lipschitz functions on the...

### 78. Learning Asymptotics with Convergence-Rate Guarantees using Linear Least Squares
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.23287
- **AI 摘要**: 本文提出渐近学习理论（ALT），将优化与渐近分析结合，统一计算渐近展开中的未知常数/参数，并研究两种强大的数值方法。
- **原始摘要**: arXiv:2607.23287v2 Announce Type: replace-cross Abstract: We introduce a new research area that is called Asymptotics Learning Theory (ALT) and combines optimization with asymptotic analysis. In parti...

### 79. Provably Efficient Self-Calibrating Quantum Fault Tolerance
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.05686
- **AI 摘要**: 量子纠错需要所有物理操作持续低于容错阈值，但模拟控制参数会漂移。本文提出高效的自校准量子容错方法，以应对长时间计算中的环境波动。
- **原始摘要**: arXiv:2608.05686v2 Announce Type: replace-cross Abstract: Quantum error correction protects logical information only when every physical operation remains below the fault-tolerance threshold, a condit...

### 80. Which Negatives Matter? Ask Your Text Encoder: Adaptive Similarity Margins for Dense-Caption Retrieval
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.18521
- **AI 摘要**: 密集字幕检索中，现有方法使用InfoNCE目标易过早饱和。本文提出利用文本编码器自适应相似度边际，以改进对比微调效果。
- **原始摘要**: arXiv:2608.18521v2 Announce Type: replace-cross Abstract: Dense-caption retrieval has recently been improved by introducing segmentation, edge maps, LLM-filtered captions, and cross-modal modules into...

### 81. Route by Kinematics, Act by Observation: Kinematics-Supervised Expert Routing in MoE-Augmented VLA
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.26807
- **AI 摘要**: 观察到操作任务可归结为运动学原型，提出运动学监督的显式路由方法，解决MoE增强VLA中因动作运动学异质性导致的专家路由低效问题。
- **原始摘要**: arXiv:2607.26807v2 Announce Type: replace Abstract: While MoE augments VLA via expert specialization, router suffers from ineffective expert routing owing to the kinematic heterogeneity of actions acr...

### 82. Symmetric Lyapunov Subcenter Manifolds for Periodic Regulation of Mechanical Systems
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2025年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2505.13064
- **AI 摘要**: 本文研究保守机械系统中Lyapunov子中心流形上的非线性振荡特性，用于机器人周期性调节任务，探索能量高效的周期控制目标。
- **原始摘要**: arXiv:2505.13064v4 Announce Type: replace-cross Abstract: Multi-body mechanical systems have rich internal dynamics, whose solutions can be exploited as energy-efficient control targets. Yet, solution...

### 83. Aug 12, 2026Introducing Grok 4.6
- **来源**: xAI Blog (TIER1)
- **发布日期**: Aug 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://x.ai/news/grok-4-6
- **AI 摘要**: 正式推出Grok 4.6模型，介绍了其新特性和性能提升，展示了在语言理解和生成方面的进步。

### 84. Qwen3Guard: Real-time Safety for Your Token Stream
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen3guard/
- **AI 摘要**: Qwen3Guard是Qwen系列首个安全护栏模型，基于Qwen3微调，用于提示和响应的安全检测，提供风险级别和分类，实现精准内容审核，达到先进水平。
- **原始摘要**: Tech Report GitHub Hugging Face ModelScope DISCORD Introduction We are excited to introduce Qwen3Guard, the first safety guardrail model in the Qwen family. Built upon the powerful Qwen3 foundation mo...

### 85. Qwen-Image-Edit: Image Editing with Higher Quality and Efficiency
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image-edit/
- **AI 摘要**: Qwen-Image-Edit是Qwen-Image的图像编辑版本，基于20B参数模型，扩展了文本渲染能力到编辑任务，同时利用Qwen2.5-VL和VAE编码器实现视觉语义和外观控制，提升编辑质量和效率。
- **原始摘要**: QWEN CHAT GITHUB HUGGING FACE MODELSCOPE DISCORD We are excited to introduce Qwen-Image-Edit, the image editing version of Qwen-Image. Built upon our 20B Qwen-Image model, Qwen-Image-Edit successfully...

### 86. Qwen-Image: Crafting with Native Text Rendering
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image/
- **AI 摘要**: Qwen-Image是一个20B参数的MMDiT图像基础模型，在复杂文本渲染和精确图像编辑方面取得显著进展，支持多行布局、段落级语义和细粒度细节，并支持字母语言。
- **原始摘要**: GITHUB HUGGING FACE MODELSCOPE DEMO DISCORD We are thrilled to release Qwen-Image, a 20B MMDiT image foundation model that achieves significant advances in complex text rendering and precise image edi...

### 87. New Kimi K2 Models & Updated Pricing
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/Kimi_API_Newsletter
- **AI 摘要**: 发布了新的Kimi K2模型并更新了定价策略，介绍了新模型的性能和价格调整，为用户提供更优的选择。

### 88. Kimi K2: Open Agentic Intelligence
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/k2-report
- **AI 摘要**: Kimi K2作为开放智能体智能，展示了其强大的自主推理和任务执行能力，适用于多种复杂场景。

### 89. AGIBOT’s WITA-Omni Preview Tops Daily-Om...News and Information | 2026-07-28
- **来源**: Agibot (智元机器人) (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://agibot.com/article/231/detail/86.html
- **AI 摘要**: AGIBOT的WITA-Omni预览版在Daily-Omni基准测试中排名第一，展示了其在多模态AI模型方面的技术优势。

### 90. Machine Learning23
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://tenstorrent.com/newsroom/newsroom/tags/machine-learning
- **AI 摘要**: 汇总了23条机器学习相关新闻，包括新算法、应用案例、研究进展及行业趋势。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
