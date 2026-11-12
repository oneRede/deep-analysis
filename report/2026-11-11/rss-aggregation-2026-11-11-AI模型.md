# RSS 聚合报告 - AI模型

**生成时间**: 2026-11-12 07:46:15
**文章数量**: 231 篇

---

### 1. The Fed’s Other Big Debate: When Should John Williams’ Term End?
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 15:33:03 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/retirement-rules-spark-exit-date-debate-for-ny-fed-s-williams
- **AI 摘要**: 文章讨论了美联储最长任职的政策制定者即将退休引发的内部讨论，讨论的主题是区域美联储领导人的任期限制规则。这与军事技术、AI芯片、编译器、光计算、经济、时政等类别不符。文章主题更接近于AI模型类别，但具体讨论的是美联储内部的政策讨论，而不是AI技术。
- **原始摘要**: The looming retirement of the Federal Reserve’s longest-serving policymaker has set off a debate within the US central bank over the rules governing term limits for regional Fed leaders, according to...

### 2. Token Pooling-Aware Training for Multi-Vector Embedding Models
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Wed, 11 Nov 2026 00:00:00 GMT (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://huggingface.co/blog/token-pooling
- **AI 摘要**: 本文介绍了Token Pooling技术在多向量嵌入模型中的应用，通过合并相似的查询词向量来减少向量数量，同时使用Sentence Transformers进行训练，最终提高了模型的检索效果和存储效率。

### 3. How we made JSON.stringify more than twice as fast
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-08-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://v8.dev/blog/json-stringify
- **AI 摘要**: 本文介绍了V8引擎如何通过优化JSON.stringify函数使其执行速度提升超过一倍，主要通过引入一个无需处理副作用的快速路径来实现。
- **原始摘要**: JSON.stringify is a core JavaScript function for serializing data. Its performance directly affects common operations across the web, from serializing data for a network request to saving data to loca...

### 4. Speculative Optimizations for WebAssembly using Deopts and Inlining
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-06-24T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://v8.dev/blog/wasm-speculative-optimizations
- **AI 摘要**: 本文介绍了V8在Google Chrome M137中实现的两种WebAssembly优化：speculative call_indirect inlining和deoptimization支持。这些优化通过利用运行时反馈来生成更高效的机器码，从而加速WebAssembly执行，特别是在WasmGC程序中。
- **原始摘要**: In this blog post, we explain two optimizations for WebAssembly that we recently implemented in V8 and that shipped with Google Chrome M137, namely speculative call_indirect inlining and deoptimizatio...

### 5. Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-04-29T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://v8.dev/blog/explicit-compile-hints
- **AI 摘要**: 本文介绍了V8如何通过显式编译提示来优化JavaScript的启动性能，从而加快网页加载速度。V8在加载网络中的脚本时，需要为每个函数决定是立即编译还是推迟编译。立即编译可以减少重复的解析工作，提高脚本的启动速度。
- **原始摘要**: Getting JavaScript running fast is key for a responsive web app. Even with V8's advanced optimizations, parsing and compiling critical JavaScript during startup can still create performance bottleneck...

### 6. v1.6.0: Mistrall goes Small 3.1 with vision
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2025-03-20T15:03:08Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.6.0
- **AI 摘要**: 这篇文章提到了Mistrall模型的更新，增加了视觉功能。这属于AI模型的范畴。
- **原始摘要**: What's Changed Missing new line by @theophilegervet in #234 Add support to Mistral Small 3.1 by @juliendenize in #239 Remove file refs by @juliendenize in #240 Release 1.6.0 by @juliendenize in #241 N...

### 7. Turbocharging V8 with mutable heap numbers
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-02-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://v8.dev/blog/mutable-heap-number
- **AI 摘要**: 本文描述了V8 JavaScript引擎中对
async-fs
基准测试优化的实现，该优化提高了
2.5倍。优化灵感来源于基准测试，但也在实际代码中出现。优化涉及使用可变堆内存来改进
Math.random
的实现。
- **原始摘要**: At V8, we're constantly striving to improve JavaScript performance. As part of this effort, we recently revisited the JetStream2 benchmark suite to eliminate performance cliffs. This post details a sp...

### 8. v1.4.0: Pixtral 👀
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-09-13T13:10:17Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.4.0
- **AI 摘要**: 该文章发布了一个新的模型版本，属于AI模型类别。
- **原始摘要**: Pixtral Mistral models can now 👀 ! pip install --upgrade mistral_inference # >= 1.4.0 Download: from huggingface_hub import snapshot_download from pathlib import Path mistral_models_path = Path.home()...

### 9. Bril: An Intermediate Language for Teaching Compilers
- **来源**: Adrian Sampson's blog (TIER2)
- **发布日期**: 2024-07-26T00:00:00+00:00
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://www.cs.cornell.edu/~asampson/blog/bril.html
- **AI 摘要**: 这篇文章介绍了一个名为Bril的中间语言，它是专门为教学编译器课程设计的。文章提到了Bril的特点，如易于开始使用、易于混合组件、简单的语义和严格的语法等。
- **原始摘要**: I created a new intermediate language, called Bril, for teaching my funky open-source, hands-on compilers course. Because it’s for education, Bril prioritizes simplicity and regularity over more typic...

### 10. v1.3.0 Mistral-Nemo
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-18T15:45:30Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.3.0
- **AI 摘要**: 该文章提到的是关于Mistral-Nemo模型的版本更新，属于AI模型类别。
- **原始摘要**: Welcome Mistral-Nemo from Mistral 🤝 NVIDIA Read more about Mistral-Nemo here. Install pip install mistral-inference>=1.3.0 Download export NEMO_MODEL=$HOME/12B_NEMO_MODEL wget https://models.mistralcd...

### 11. v1.2.0 Add Mamba
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-07-16T18:41:37Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.2.0
- **AI 摘要**: 该文章标题为v1.2.0 Add Mamba，内容主要涉及GitHub上mistralai/mistral-inference仓库的模型版本更新。文章内容与AI模型的发布、模型架构、训练方法等技术细节无关。
- **原始摘要**: Welcome 🐍 Codestral-Mamba and 🔢 Mathstral pip install mistral-inference>=1.2.0 Codestral-Mamba pip install packaging mamba-ssm causal-conv1d transformers Download export MAMBA_CODE=$HOME/7B_MAMBA_CODE...

### 12. Introducing the WebAssembly JavaScript Promise Integration API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-07-01T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://v8.dev/blog/jspi
- **AI 摘要**: 本文介绍了WebAssembly与JavaScript Promise集成API（JSPI），该API允许原本假设同步访问外部功能的WebAssembly应用在异步环境中也能正常运行。
- **原始摘要**: The JavaScript Promise Integration (JSPI) API allows WebAssembly applications that were written assuming synchronous access to external functionality to operate smoothly in an environment where the fu...

### 13. WebAssembly JSPI has a new API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-06-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://v8.dev/blog/jspi-newapi
- **AI 摘要**: V8团队宣布WebAssembly JSPI API新增功能，包括取消Suspender对象和改变API风格。新的API允许WebAssembly应用程序在返回Promise时暂停计算，并在Promise解决时恢复。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API has a new API, available in Chrome release M126. We talk about what has changed, how to use it with Emscripten, and what is the roadmap for JSPI...

### 14. v1.0.4 - Mistral-inference
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-05-24T18:32:35Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.0.4
- **AI 摘要**: 该文章标题为v1.0.4 - Mistral-inference，内容为GitHub上Mistral-inference仓库的更新信息。根据内容判断，此文章主题与AI模型的发布和更新有关。
- **原始摘要**: Mistral-inference is the official inference library for all Mistral models: 7B, 8x7B, 8x22B. Install with: pip install mistral-inference Run with: from mistral_inference.model import Transformer from...

### 15. v1.1.0 Add LoRA
- **来源**: Mistral AI Releases (TIER2)
- **发布日期**: 2024-05-24T18:32:10Z
- **类型**: releases
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://github.com/mistralai/mistral-inference/releases/tag/v1.1.0
- **AI 摘要**: 该文章提到的是关于mistralai/mistral-inference库的版本更新，具体是添加了LoRA技术。这与AI模型的更新和改进相关。
- **原始摘要**: mistral-inference==1.1.0 supports running LoRA models that were trained with: https://github.com/mistralai/mistral-finetune Having trained a 7B base LoRA, you can run mistral-inference as follows: fro...

### 16. Static Roots: Objects with Compile-Time Constant Addresses
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-02-05T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://v8.dev/blog/static-roots
- **AI 摘要**: 本文介绍了V8编译器中的静态根（static roots）特性，该特性允许在编译时预分配一些核心对象，如undefined和true，从而提高代码的执行效率。
- **原始摘要**: Did you ever wonder where undefined, true, and other core JavaScript objects come from? These objects are the atoms of any user defined object and need to be there first. V8 calls them immovable immut...

### 17. Variable-Length Prompts on Chimera GPNPU
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Wed, 11 Nov 2026 08:02:29 +0000 (今天)
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://semiengineering.com/variable-length-prompts-on-chimera-gpnpu/
- **AI 摘要**: 本文讨论了如何为边缘产品编译语言模型时处理不同长度提示的问题，提出了在编译过程中灵活选择二进制的方法，以适应最长和最短的提示长度。
- **原始摘要**: How a flexible binary can serve every length up to the capacity you set. The post Variable-Length Prompts on Chimera GPNPU appeared first on Semiconductor Engineering....

### 18. Attribute-Evidence Learning with Multimodal Prompt for Generalized Category Discovery
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12975
- **AI 摘要**: 该文章讨论了一种新的多模态框架AptM-GCD，用于解决从无标签数据中发现新类别的问题，该框架通过属性证据学习和多模态提示推理来利用文本指导。
- **原始摘要**: arXiv:2611.12975v1 Announce Type: new Abstract: Generalized category discovery (GCD) aims to discover novel categories from unlabeled data by leveraging limited labeled samples from old classes. Exist...

### 19. Evidence-Grounded Iterative Reasoning for the Diagnosis of Diffuse Cystic Lung Diseases
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12981
- **AI 摘要**: 该文章讨论了用于诊断弥漫性囊性肺疾病（DCLDs）的证据支持迭代推理框架，旨在解决影像表现重叠导致的鉴别诊断难题。
- **原始摘要**: arXiv:2611.12981v1 Announce Type: new Abstract: Overlapping imaging manifestations complicate the differential diagnosis of Diffuse Cystic Lung Diseases (DCLDs), while limited annotated data constrain...

### 20. TIB: Sample-wise Tempered Information Bottleneck for Multimodal Attribution beyond Alignment Assumption
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12997
- **AI 摘要**: 该文章讨论了信息瓶颈方法在多模态解释中的应用，提出了TIB方法来解决假设下的结构限制问题。
- **原始摘要**: arXiv:2611.12997v1 Announce Type: new Abstract: Multimodal (e.g. vision-language, in this work) attribution aims to interpret the models without access to ground-truth explanatory supervision. Existin...

### 21. How Hyperbolic Are Hyperbolic Vision-Language Models?
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13384
- **AI 摘要**: 文章讨论了超平面视觉语言模型在实践中的曲率情况，发现其在预映射的欧几里得空间中的距离和角度变化不大，且移除映射不会影响评估分数。因此，作者训练了基于CC3M的欧几里得视觉语言模型。
- **原始摘要**: arXiv:2611.13384v1 Announce Type: new Abstract: Hyperbolic vision-language models (VLMs) have emerged as a rapidly growing area of research, reporting strong zero-shot performance alongside an interpr...

### 22. Relaxing Cross-Modal Correspondence for Multimodal Remote Sensing Pretraining
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13807
- **AI 摘要**: 该文章讨论了在多模态遥感预训练中放松跨模态对应关系的方法，提出了一种新的预训练策略SemPair，以类一致的跨实例配对替代精确的实例配对。
- **原始摘要**: arXiv:2611.13807v1 Announce Type: new Abstract: Multimodal remote sensing pretraining commonly relies on exact instance-level correspondence across modalities, implicitly treating strictly paired obse...

### 23. EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video Understanding
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13907
- **AI 摘要**: 该文章讨论了通过证据充分性引导训练来增强视频理解的方法，适用于适应性思考。
- **原始摘要**: arXiv:2611.13907v1 Announce Type: new Abstract: Under a fixed frame budget, video understanding with vision-language models (VLMs) depends on whether the sampled frames provide sufficient evidence for...

### 24. ZoomGain: Mining Global-to-Zoom Perception Gaps for Fine-Grained Visual Supervision
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14076
- **AI 摘要**: 文章讨论了如何利用视觉信息通过放大查看来构建关于完整图像的问题，以解决视觉感知中的细微差异。ZoomGain提出了一种数据构建管道，用于生成关于完整图像的问题，这些问题只能通过放大查看来获得。
- **原始摘要**: arXiv:2611.14076v1 Announce Type: new Abstract: Fine-grained visual perception requires Vision-Language Models (VLMs) to locate and interpret subtle evidence within complex scenes. Constructing superv...

### 25. OnlyAct: Extracting Action Representations from Foundation Models for World Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14420
- **AI 摘要**: 文章讨论了如何从预训练的基础模型中提取动作表示，以用于视频世界模型。文章提出了一个不同的方法，而不是从零开始学习动作，而是从预训练的基础模型（V-JEPA 2）的帧对嵌入中开始。
- **原始摘要**: arXiv:2611.14420v1 Announce Type: new Abstract: Video world models promise general-purpose interactive simulators, but their training is limited by action supervision: action labels are scarce, fragme...

### 26. Structured Kernel Surrogate Models for Multimodal Attribution
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13198
- **AI 摘要**: 文章讨论了跨样本模态 attribution 的问题，提出了一种结构化的核代理模型来捕捉样本和模态之间的交互。
- **原始摘要**: arXiv:2611.13198v1 Announce Type: cross Abstract: We study the problem of cross-sample modality attribution, which involves measuring how one modality in one sample affects the learning outcome in oth...

### 27. GARD: Gradient-Guided Adversarial Representation Defense against Backdoors in Multimodal Contrastive Learning Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14143
- **AI 摘要**: 文章讨论了对抗性表示防御方法GARD，用于对抗多模态对比学习模型中的后门攻击。
- **原始摘要**: arXiv:2611.14143v1 Announce Type: cross Abstract: Multimodal contrastive learning models such as CLIP are vulnerable to backdoor attacks with diverse trigger structures, ranging from localized patches...

### 28. Multimodal Abstention That Preserves Acquired Correct Answers
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14311
- **AI 摘要**: 该文章讨论了如何在多模态模型中添加弃权机制以保留已获得的正确答案，提出了ReFrain方法来修复弃权错误。
- **原始摘要**: arXiv:2611.14311v1 Announce Type: cross Abstract: Adding abstention to a task-adapted multimodal model can discard correct answers, including capabilities acquired during adaptation. We formulate abst...

### 29. RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.14700
- **AI 摘要**: 本文提出了一种RepFusion方法，利用多模态语言模型（MLLM）对噪声表示进行编码，以提高文本到图像转换系统的性能。
- **原始摘要**: arXiv:2606.14700v2 Announce Type: replace Abstract: Large language models (LLMs) are widely used in text-to-image (T2I) systems, but they are typically limited to text encoding, while denoising is han...

### 30. Mixture of Cognitive Experts in Large Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.10796
- **AI 摘要**: 文章讨论了大型视觉语言模型需要结合视觉和文本输入的强大推理能力，以及如何整合多编码专家以提高模型的可信度和减少幻觉。
- **原始摘要**: arXiv:2607.10796v2 Announce Type: replace Abstract: Large Vision Language Models (LVLMs) require strong reasoning over both visual and textual inputs. Recent work suggests that cognitive elements, esp...

### 31. CRIL-U-Net: Compact Ratio-Interaction Learning for Focal Cortical Dysplasia Segmentation from T1w and FLAIR MRI
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.03185
- **AI 摘要**: 本文提出了一种新的U-Net架构CRIL-U-Net，用于T1w和FLAIR MRI图像上的FCD类型II的自动分割。
- **原始摘要**: arXiv:2608.03185v2 Announce Type: replace Abstract: Focal cortical dysplasia (FCD) type II is an important cause of drug-resistant focal epilepsy, but its small size and subtle magnetic resonance imag...

### 32. Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.10864
- **AI 摘要**: 文章讨论了如何通过多视图关系蒸馏（MVRD）来改进视觉语言模型的几何基础，以提高其在空间推理中的表现，特别是在机器人、AI和自动驾驶等领域。
- **原始摘要**: arXiv:2608.10864v3 Announce Type: replace Abstract: Vision-language models (VLMs) have achieved strong image and video understanding, yet their visual-spatial representations remain geometrically frag...

### 33. DORIS: Polarization Aware Multimodal Degradation Perception for Underwater Image Restoration
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.17991
- **AI 摘要**: 文章讨论了DORIS框架，该框架用于从受损的水下观测中恢复高质量图像，利用了极化观察作为补充物理线索来恢复清晰水下的目标亮度。文章提出了一种统一的多模态语言驱动框架DORIS，该框架结合了极化和RGB...
- **原始摘要**: arXiv:2610.17991v2 Announce Type: replace Abstract: Recovering high-quality images from degraded underwater observations is crucial for underwater exploration. Polarization observations show promise a...

### 34. CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.32012
- **AI 摘要**: 文章讨论了如何通过分解不确定性为特定上下文和特定多样性的部分来估计多模态大型语言模型的不确定性，属于AI模型类别。
- **原始摘要**: arXiv:2606.32012v2 Announce Type: replace-cross Abstract: Uncertainty estimation has been a long-standing challenge in AI models; it amounts to "knowing what you don't know," and metacognition is noto...

### 35. STABLE: A Continual Learning Optimizer with Adaptive Drift Control
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.10655
- **AI 摘要**: 文章讨论了STABLE优化器，旨在解决持续学习中的遗忘问题，通过在优化器层面引入自适应漂移控制来实现。
- **原始摘要**: arXiv:2611.10655v2 Announce Type: replace-cross Abstract: Continual learning suffers from catastrophic forgetting, leading to the loss of past knowledge and unstable adaptation across task streams. Ex...

### 36. Accelerating GPT-5.6 Sol UltrafastAugust 13, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ust 13, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai
- **AI 摘要**: 文章摘要：关于加速GPT-5.6的介绍，发布时间为2026年8月13日。

### 37. Debugging Dead MoE Models: A Step-by-Step GuideJuly 28, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: uly 28, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/moe-guide-debug
- **AI 摘要**: 本文提供了一个步骤指南来调试失效的MoE模型。

### 38. Getting the most out of GPT-5.6: Sol, Terra, and LunaJuly 27, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: uly 27, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/getting-the-most-out-of-gpt-5-6-sol-terra-and-luna
- **AI 摘要**: 文章讨论了GPT-5.6的Sol、Terra和Luna模型，属于AI模型类别。

### 39. MoE at Scale: Making Sparse Models Fast on Real HardwareOctober 22, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 22, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/moe-guide-scale
- **AI 摘要**: 本文讨论了在大规模稀疏模型上实现快速运行的方法，针对实际硬件进行优化。

### 40. MoE Math Demystified: What Does 8x7B Actually Mean?October 06, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 06, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/moe-guide-calculator
- **AI 摘要**: 本文探讨了MoE（模型并行化）模型的数学原理，解释了8x7B参数量的具体含义。

### 41. Introducing OpenAI GPT-5.3-Codex-Spark Powered by CerebrasFebruary 12, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 12, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/openai-codexspark
- **AI 摘要**: 文章介绍了OpenAI的GPT-5.3、Codex和Spark，这些技术由Cerebras提供支持。

### 42. This new model is smarter than Sonnet 4.5…and 20X faster?January 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.cerebras.ai/blog/glm-4-7-migration-guide
- **AI 摘要**: 本文介绍了一个新模型，声称其比Sonnet 4.5更聪明，并且速度快20倍。

### 43. AlphaGenome 2: Deciphering how cells read DNA to better understand disease
- **来源**: Google DeepMind Blog (TIER1)
- **发布日期**: Wed, 11 Nov 2026 15:00:15 +0000 (今天)
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/
- **AI 摘要**: 文章讨论了如何预测DNA序列及其变异对特定人类细胞类型和疾病的影响力，属于AI模型类别。
- **原始摘要**: Predicting how DNA sequences and their variations impact specific human cell types and disease.

### 44. Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12901
- **AI 摘要**: 该文章讨论了如何通过改进MDLMs的解码策略来减少解码过程中的幻觉现象。
- **原始摘要**: arXiv:2611.12901v1 Announce Type: new Abstract: Recent advancements in multimodal diffusion language models (MDLMs) have exhibited strong global modeling capabilities through iterative refinement. We...

### 45. TimeOmni-o1: Bidirectionally Coupling Time Series Foundation Models and LLMs for Multimodal Reasoning and Forecasting
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12902
- **AI 摘要**: 该文章讨论了一种新的模型TimeOmni-o1，它通过双向耦合时间序列基础模型和语言模型来实现多模态推理和预测。
- **原始摘要**: arXiv:2611.12902v1 Announce Type: new Abstract: Time series from real-world systems are often accompanied by text, such as a report on an event that affects them. Two common tasks on these series are...

### 46. Actionable Feedback: Improving Model Capabilities from User Edit Data on Clinical Documentation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12904
- **AI 摘要**: 文章讨论了如何利用临床文档编辑数据来改进大型语言模型的能力，但指出并非所有编辑都具有行动价值。文章提出了一种方法来解决这一问题。
- **原始摘要**: arXiv:2611.12904v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly being deployed in clinical documentation workflows, where clinicians review and edit their outputs before...

### 47. Brasilidade: Measuring Brazilian Identity for Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12906
- **AI 摘要**: 该文章讨论了针对巴西葡萄牙语的大规模语言模型评估基准，强调了模型大小并非唯一决定因素，并揭示了不同任务水平下的显著差异。
- **原始摘要**: arXiv:2611.12906v1 Announce Type: new Abstract: This work presents a new benchmark that aims to address the limitations of current methods for evaluating LLMs in Brazilian Portuguese. We introduced Br...

### 48. Capacity Allocation at the Source: Sparse Target Optimization for LLM Knowledge Editing
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12995
- **AI 摘要**: 该文章讨论了在大型语言模型（LLMs）中进行知识编辑的方法，提出了一种使用$l_1$正则化方法来简化目标隐藏状态的技术，以优化模型的容量分配。
- **原始摘要**: arXiv:2611.12995v1 Announce Type: new Abstract: Knowledge editing has emerged as a promising approach for efficiently updating embedded knowledge in large language models (LLMs). It first computes an...

### 49. A Multi-Word Tokenizer for 204 Languages That Needs Fewer Tokens Than GPT-4o's, Including on English
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13059
- **AI 摘要**: 该文章介绍了训练了一种新的多词标记器Havon v4，它在保持与GPT-4o相同词汇量的情况下，减少了对204种语言的token需求，特别是在英语上。
- **原始摘要**: arXiv:2611.13059v1 Announce Type: new Abstract: Languages of India need 1.6 to 14 times as many tokens as English on GPT-4o's tokenizer for the same content, which makes them more expensive and slower...

### 50. Catch It Where It Happens: Real Time Error Correction During LLM Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13107
- **AI 摘要**: 该文章讨论了一种实时错误校正的方法，用于LLM的推理过程中，以提高模型的准确性和效率。
- **原始摘要**: arXiv:2611.13107v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly trusted with mathematical, scientific and engineering work, yet their mistakes are often confidently writt...

### 51. HiCAP: Hierarchical Cultural Adaptation via Personality for Dialogue Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13207
- **AI 摘要**: 文章讨论了HiCAP框架，该框架通过融入个性特质来增强对话生成中的文化适应性。
- **原始摘要**: arXiv:2611.13207v1 Announce Type: new Abstract: Cultural adaptation in dialogue systems refers to the ability to generate responses that conform to linguistic norms and social expectations across diff...

### 52. Deletion Sensitivity Is a Property of the Model: A Three-Condition Measurement across Seven Open Reasoning Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13223
- **AI 摘要**: 该文章讨论了在多轮工具呼叫中的推理历史删除测量，涉及多个模型和条件，发现删除对模型性能的影响较小，模型性能主要由模型本身决定。
- **原始摘要**: arXiv:2611.13223v1 Announce Type: new Abstract: Reasoning models write a reasoning trace at every turn of a multi-turn tool session, and later turns read this history. Across 94k ShareGPT conversation...

### 53. What drives the emergence of symbolic mechanisms in large language models?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13270
- **AI 摘要**: 文章讨论了大型语言模型中出现符号机制的因素，通过训练从零开始的神经网络来探索数据多样性和架构因素对符号机制的影响。
- **原始摘要**: arXiv:2611.13270v1 Announce Type: new Abstract: Recent work has identified a set of emergent symbolic mechanisms that support abstract reasoning in large language models, but it remains unclear what f...

### 54. Measuring Definition Sensitivity in LLM Annotation of Social Science Concepts
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13339
- **AI 摘要**: 文章讨论了使用大型语言模型进行社会科学研究中的概念标注，通过比较两次使用不同定义的标注结果来检测定义敏感性。
- **原始摘要**: arXiv:2611.13339v1 Announce Type: new Abstract: In social science research, text annotation is a fundamental task that is traditionally a costly, hard-to-scale manual process. Researchers have used la...

### 55. BioMem: Agentic Memory for Biomedical LLM Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13426
- **AI 摘要**: 文章讨论了大型语言模型在生物医学领域的应用及其代理记忆系统的有效性。文章分析了五种记忆方法在四种大型语言模型中的表现，重点研究了任务效果、检索质量、信息真实性以及长期稳健性。
- **原始摘要**: arXiv:2611.13426v1 Announce Type: new Abstract: Large language models (LLMs) have demonstrated considerable potential in biomedical applications, while agentic memory systems have emerged as a promisi...

### 56. Inherited Weights: Measuring the Tokenization Premium and the Sovereignty Cost of Language Models for the Global South
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13441
- **AI 摘要**: 该文章讨论了语言模型在不同语言和Tokenizer上的细调带来的词汇、知识、文化对齐等特性继承问题，以及对全球南方语言模型的影响。
- **原始摘要**: arXiv:2611.13441v1 Announce Type: new Abstract: Most language models deployed outside the United States and China are fine-tuned descendants of a small number of pretrained families. We argue that fin...

### 57. Framing-Induced Vulnerability in Large Language Models: Evidence from Chinese News Headlines
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13531
- **AI 摘要**: 该文章讨论了大型语言模型在评估和报道新闻时的偏见问题，通过实验研究了新闻标题的框架变化对模型判断的影响。
- **原始摘要**: arXiv:2611.13531v1 Announce Type: new Abstract: Large language models increasingly evaluate, route, and moderate news, so a model's judgment of a headline has become a gatekeeping decision. We ask whe...

### 58. How Post-Training Influences Verbalized Algorithmic Computation in Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13552
- **AI 摘要**: 该文章讨论了语言模型在多数字加法任务中的推理改进，特别是在使用后训练（post-training）时，语言模型如何利用内部信息和口头推理链（CoT）。
- **原始摘要**: arXiv:2611.13552v1 Announce Type: new Abstract: Post-training improves language-model reasoning, but how it changes the use of internal information and verbalized chain of thought (CoT) remains unclea...

### 59. Are Dense Rewards Worth Their Tokens in GRPO?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13560
- **AI 摘要**: 该文章讨论了在强化学习中使用密集奖励的经济性问题，提出了匹配计算协议来解决这个问题。
- **原始摘要**: arXiv:2611.13560v1 Announce Type: new Abstract: RLVR trains language models to reason by rewarding correct final answers. A widely used algorithm, group-relative policy optimization (GRPO), gives ever...

### 60. An evidence-traceable benchmark of clinical reasoning in large language models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13562
- **AI 摘要**: 本文介绍了一种新的临床推理基准测试Med Evidence Bench，用于评估大型语言模型在临床知识和实际场景中的表现。
- **原始摘要**: arXiv:2611.13562v1 Announce Type: new Abstract: Benchmark scores for medical large language models (LLMs) are difficult to interpret when scoring criteria cannot be traced to clinical evidence. Here w...

### 61. A Concept-Based Interpretable Framework for Clinical Text-based Prediction via Token-Concept Attention without Concept Supervision
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13564
- **AI 摘要**: 该文章讨论了一种无需概念监督的方法，用于在临床文本预测任务中实现概念基础的解释。
- **原始摘要**: arXiv:2611.13564v1 Announce Type: new Abstract: Objective: Concept-based interpretation has emerged as a promising approach for explaining blackbox models using human-understandable, high-level concep...

### 62. IFRS Compliance Verification: An Open Multi-LLM Benchmark and Content-Conditioned Ensemble Classifier
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13595
- **AI 摘要**: 该文章讨论了使用多语言模型（LLM）进行国际财务报告标准（IFRS）合规性验证的基准测试和内容条件化集成分类器。
- **原始摘要**: arXiv:2611.13595v1 Announce Type: new Abstract: Verifying corporate financial disclosures against the International Financial Reporting Standards (IFRS) is a core auditing task in which experts cross-...

### 63. One Byte, One Token: Byteifying a 27B Hybrid-Attention LLM with Self-Generated Data
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13607
- **AI 摘要**: 该文章讨论了如何将一个已经训练好的27B字子模型转换为一个纯字节模型，不使用任何补丁结构或局部编码器。
- **原始摘要**: arXiv:2611.13607v1 Announce Type: new Abstract: Byte-level BPE fragments Chinese text (for Qwen3.8 on Chinese Wikipedia, 3.84 bytes per token on average; 64% of tokens are single characters) and hides...

### 64. An Interpretable Stylometric Framework for Early Chinese Buddhist Translator Styles: A Case Study on the Attribution of Disputed Works of An Shigao
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13636
- **AI 摘要**: 该文章介绍了一种解释性的风格定量框架，用于早期中国佛教翻译家风格的识别，通过比较争议文本与已认证的安世高的文本风格。框架使用了佛教学者定义或审查的功能字符、句子公式、句子末尾字符、句子长度和词性n-gram等特征。
- **原始摘要**: arXiv:2611.13636v1 Announce Type: new Abstract: Attributing early Chinese Buddhist translations requires evidence that scholars can trace back to the texts. We develop an interpretable stylometric fra...

### 65. On the information rate of phones, syllables and words
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13990
- **AI 摘要**: 文章讨论了在有限的建模预算下，使用单词、音节、多词组合等不同语言单位来编码语音内容的信息率。结果表明，当建模能力有限时，介于音节和多词组合之间的单位提供了最有效的信息率表示。
- **原始摘要**: arXiv:2611.13990v1 Announce Type: new Abstract: Which linguistic units minimise the bitrate required to encode speech content: phones, syllables, words, maybe larger units, or something in between? Th...

### 66. One Sequence Is Enough: Fingerprinting Language Models from Fixed-Length Integer Sequences
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14010
- **AI 摘要**: 文章讨论了如何通过固定长度的整数序列来识别语言模型，提出了一种新的基准和模型，以提高模型识别的准确性。
- **原始摘要**: arXiv:2611.14010v1 Announce Type: new Abstract: Users of model APIs and third-party platforms often rely on the declared model name to identify the model responding to their requests. However, the act...

### 67. HandsOnAid: Building and Evaluating an Offline First-Aid Assistant for Emergency Response Scenarios
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14059
- **AI 摘要**: 本文介绍了一种离线急救助手HandsOnAid，通过Fine-tuning模型提高急救建议的安全性和准确性。
- **原始摘要**: arXiv:2611.14059v1 Announce Type: new Abstract: Emergencies can occur where there is no phone signal and no ambulance nearby. A small language model on a phone can be helpful in such situations, but i...

### 68. From Bias to Positionality: A critical grammar for Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14079
- **AI 摘要**: 文章讨论了大型语言模型中的偏见问题，并提出位置性（位置、表达、拥有和争议的位置）是更好的语法规则。
- **原始摘要**: arXiv:2611.14079v1 Announce Type: new Abstract: Bias has become a default lens for understanding what machine learning systems do and how we should relate to them. Bias is at root a deviation from a s...

### 69. Sckwoky at SHROOM-Visions: Character-Level Hallucination-Span Detection in Image-Conditioned VLMs via Dual-Prompted LoRA Decoders
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14100
- **AI 摘要**: 该文章讨论了在图像条件下的视觉语言模型响应中，基于双提示LoRA解码器的字符级幻觉跨度检测系统。
- **原始摘要**: arXiv:2611.14100v1 Announce Type: new Abstract: We present our system for the SHROOM-visions 2026 shared task on character-level hallucination span detection in image-conditioned vision-language model...

### 70. Stagewise and interpretable emergence of inside-outside computation in Transformer-based language models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14221
- **AI 摘要**: 文章讨论了Transformer语言模型在学习自然语言中变异性结构和解析模糊性方面的学习动态，特别关注了在可变句法树结构的合成上下文中Transformer的学习曲线。
- **原始摘要**: arXiv:2611.14221v1 Announce Type: new Abstract: Variability in syntactic structure and parsing ambiguity are fundamental aspects of natural language which modern LLMs have to learn to deal with profic...

### 71. StaRSE: Compact Russian Sentence Embeddings with a Sign-Coded Static Encoder
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14236
- **AI 摘要**: 本文介绍了一种名为StaRSE的紧凑型俄语静态句子编码器，它在不使用Transformer的推理阶段存储了token的方向和范数，并在对比优化阶段直接优化了符号投影的token表。
- **原始摘要**: arXiv:2611.14236v1 Announce Type: new Abstract: Transformer sentence encoders provide strong retrieval quality, but their inference cost becomes a bottleneck when embeddings must be produced on CPUs o...

### 72. Dyship: Leveraging Acoustic Features For Speaker Relationship Classification From Dyadic Conversations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14241
- **AI 摘要**: 该文章讨论了利用声学特征从对话语料中分类说话人熟悉度和亲缘关系的方法，比较了五种不同的语音表示。
- **原始摘要**: arXiv:2611.14241v1 Announce Type: new Abstract: We introduce DyShip, a framework for classifying speaker familiarity and kinship from dyadic conversations in the Seamless Interaction corpus. We compar...

### 73. Point-in-Time Encoders for Earnings Calls
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14325
- **AI 摘要**: 该文章讨论了用于财务电话会议的点时间编码器，通过训练不同的编码器来解决前瞻偏见问题，提高了预测准确性。
- **原始摘要**: arXiv:2611.14325v1 Announce Type: new Abstract: Text encoders turn earnings calls into vectors for search, for language models that answer from retrieved passages, and for forecasting models. A live r...

### 74. Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14387
- **AI 摘要**: 本文提出了一种名为Blurring the Block Boundaries（B3）的方法，用于加速扩散语言模型，通过在共享前向传播中并行优化两个块，从而提高模型的生成速度。
- **原始摘要**: arXiv:2611.14387v1 Announce Type: new Abstract: Diffusion Language Models (DLMs) have emerged as effective alternatives to autoregressive models for latency-critical tasks, enabling faster token gener...

### 75. When does text encoding matter for language modeling?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14459
- **AI 摘要**: 文章讨论了不同编码方式对语言模型性能的影响，特别是UTF-8编码在语言模型中的局限性。
- **原始摘要**: arXiv:2611.14459v1 Announce Type: new Abstract: UTF-8's role as the de facto encoding standard in language models introduces cross-lingual inequities due to its variable-length design. However, the ef...

### 76. Pterodactyl: Pushing the Limits of Efficient Automated Translation Evaluation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14480
- **AI 摘要**: 本文介绍了一种用于自动翻译质量评估的系统Pterodactyl，该系统针对WMT26共享任务中的两个子任务进行了优化。
- **原始摘要**: arXiv:2611.14480v1 Announce Type: new Abstract: In this paper, we present 1020 Group's submission to the WMT26 shared task on automated quality evaluation. Our system, Pterodactyl, was engineered spec...

### 77. Mechanistic Interpretability Needs a Logic of Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14483
- **AI 摘要**: 文章讨论了神经网络的解释性研究进展，提出了五个原则来指导从复杂神经系统中推断机制的过程。
- **原始摘要**: arXiv:2611.14483v1 Announce Type: new Abstract: Neural networks are increasingly studied not merely as predictive systems, but as complex systems whose internal computations are themselves objects of...

### 78. Seeing Is Not Believing: Counterfactual Lesion Erasure Teaches a Small Medical Vision-Language Agent to Report Only What the Image Shows
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13006
- **AI 摘要**: 该文章讨论了一种医疗视觉语言模型MedScope-4B，它能够忽略图像并仅报告图像中实际存在的病变。文章提到了一个名为“Seeing Is Not Believing”的实验，展示了该模型在处理图像时的性能。
- **原始摘要**: arXiv:2611.13006v1 Announce Type: cross Abstract: Medical vision-language models (VLMs) often report a finding because the question names it; standard benchmarks miss this. From public segmentation da...

### 79. One Temperature to Rule Them All?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13077
- **AI 摘要**: 文章讨论了温度控制在大型语言模型中的应用，分析了温度多样性在多样本推断中的作用，并提出了一种评估最优多温度分配方案的方法。
- **原始摘要**: arXiv:2611.13077v1 Announce Type: cross Abstract: Inference-time sampling is a central mechanism for improving large language models, with temperature controlling the tradeoff between reliability and...

### 80. Agreeing on the Answer but Not the Reason: Measurement Limits of LLM Reasoning Failure Taxonomies
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13140
- **AI 摘要**: 该文章讨论了LLM推理失败分类测量的局限性，指出分类结果很大程度上取决于测量方法。
- **原始摘要**: arXiv:2611.13140v1 Announce Type: cross Abstract: Failure taxonomies for LLM reasoning are increasingly reported as measurements: papers state what fraction of a model's errors fall into named categor...

### 81. MicroLens: Read, Trace, and Rewire the Residual Stream with Two Lenses
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13322
- **AI 摘要**: 文章讨论了使用双镜头查看语言模型的残差流，展示了模型在不同编辑方向下的行为。
- **原始摘要**: arXiv:2611.13322v1 Announce Type: cross Abstract: Lenses that decode hidden states into words are a popular way to look inside language models, but a heatmap of decoded words only shows what a vector...

### 82. Free Lunch Uncertainty: Sequence-Level R\'enyi Entropy from Particle Decoding for Adaptive LLM Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13414
- **AI 摘要**: 该文章讨论了通过粒子编码和顺序蒙特卡洛解码来估计语言模型完成分布的序列级瑞利熵，提出了一种零成本的不确定性量化方法。
- **原始摘要**: arXiv:2611.13414v1 Announce Type: cross Abstract: Quantifying uncertainty over an entire LLM completion is critical for selective prediction and adaptive compute. Zero-cost signals such as mean token...

### 83. Leveraging Psychophysical Attentional Distribution for Gaze-Augmented Reward Modeling
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13477
- **AI 摘要**: 文章讨论了利用眼动追踪数据训练奖励模型的方法，模型能够更好地预测人类偏好。
- **原始摘要**: arXiv:2611.13477v1 Announce Type: cross Abstract: Integrating human feedback into language models has gained increasing attention as a means to align model outputs with human preferences, with Reinfor...

### 84. Sanity Checks for Attention Surgery: Null Models and Matched Interventions for Representation-Motivated Design
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13543
- **AI 摘要**: 该文章讨论了Transformer架构修改时需要进行的统计检查，以确保修改的效果，并分析了在不同注意力机制下的效果。
- **原始摘要**: arXiv:2611.13543v1 Announce Type: cross Abstract: Transformer architectural modifications frequently measure a statistic on internal representations, observe that it is large, remove it architecturall...

### 85. Walrus Technical Report
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13689
- **AI 摘要**: 文章介绍了Walrus模型，这是一个统一的8B语音和音频基础模型，能够处理语音识别、语音转文本、语音到语音翻译、文本到语音、情绪识别、音频描述和一般音频理解等多种任务。主要贡献在于数据训练方案。
- **原始摘要**: arXiv:2611.13689v1 Announce Type: cross Abstract: We present Walrus, a unified 8B speech-and-audio foundation model handling speech recognition (including code-switching and multi-talker speech), spee...

### 86. Understanding Mixture-of-Experts Language Models Beyond Expert Boundaries
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13975
- **AI 摘要**: 文章讨论了Mixture-of-Experts语言模型中专家特化的问题，通过RAMP分析方法发现不同领域内的神经元有较高的重叠率，但专家特化的影响较小。文章还追踪了模型在预训练和后训练阶段神经元重要性的变化。
- **原始摘要**: arXiv:2611.13975v1 Announce Type: cross Abstract: In Mixture-of-Experts (MoE) models, the nature of expert specialization remains controversial. Reports of domain-associated expert preferences contras...

### 87. Specify Privacy Yourself: Assessing Inference-Time Personalized Privacy Preservation Ability of Large Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13997
- **AI 摘要**: 该文章讨论了大型视觉语言模型在推理时间实现个性化隐私保护的能力，提出了一个新的评估任务和工具。
- **原始摘要**: arXiv:2611.13997v1 Announce Type: cross Abstract: Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities but raise significant privacy concerns due to their abilities to infer...

### 88. REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14399
- **AI 摘要**: 该文章讨论了在推测解码中优化预期接受长度（EAL）的方法，提出了REAL损失函数以减少偏差。
- **原始摘要**: arXiv:2611.14399v1 Announce Type: cross Abstract: Speculative decoding accelerates LLM inference by having a draft model propose multiple tokens for the target model to verify in one pass. The speedup...

### 89. Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14413
- **AI 摘要**: 研究比较了在小局部语言模型中，存储权重在更少位数上的节省内存和对答案选项顺序平均化减少敏感度之间的成本效益。
- **原始摘要**: arXiv:2611.14413v1 Announce Type: cross Abstract: Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a...

### 90. Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14514
- **AI 摘要**: 文章讨论了LLM代理在数据驱动的科学发现中的应用，提出了Contrastive Discovery方法来解决单一假设测试的问题。
- **原始摘要**: arXiv:2611.14514v1 Announce Type: cross Abstract: LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirica...

### 91. AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14515
- **AI 摘要**: 文章讨论了AutoScaffold框架，该框架利用AI为强化学习中的语言模型生成适应性支架，以提高训练效率。
- **原始摘要**: arXiv:2611.14515v1 Announce Type: cross Abstract: Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number an...

### 92. Linear-time Minimum Bayes Risk Decoding with Reference Aggregation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2024年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2402.04251
- **AI 摘要**: 本文提出了一种新的方法来近似最小贝叶斯风险解码中的实用指标得分，从而将复杂度从O(n^2)降低到O(n)，同时保持了大部分的解码质量提升。
- **原始摘要**: arXiv:2402.04251v3 Announce Type: replace Abstract: Minimum Bayes Risk (MBR) decoding is a text generation technique that has been shown to improve the quality of machine translations, but is expensiv...

### 93. Do Reasoning LLMs Refuse What They Infer in Long Contexts?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.08874
- **AI 摘要**: 文章讨论了大型语言模型在长上下文中的推理能力及其潜在的安全风险，包括有害意图可能被分散并隐藏在上下文中的问题。
- **原始摘要**: arXiv:2602.08874v3 Announce Type: replace Abstract: Long-context LLMs can infer objectives that are not explicitly stated. This capability is useful for reasoning over documents, code, and tool traces...

### 94. Cold-Start Personalization via Bayesian Adaptive Questioning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.15012
- **AI 摘要**: 本文提出了一种新的方法CAPE来解决冷启动个性化问题，通过学习用户偏好之间的结构模型来预测用户偏好。
- **原始摘要**: arXiv:2602.15012v2 Announce Type: replace Abstract: Cold-start personalization requires inferring preferences from minimal interaction when no user-specific historical data is available. The space of...

### 95. STDec: Spatio-Temporal Stability Guided Decoding for dLLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.06330
- **AI 摘要**: 文章讨论了扩散大语言模型（dLLMs）的解码问题，提出了一种基于空间和时间稳定的解码方法STDec。
- **原始摘要**: arXiv:2604.06330v2 Announce Type: replace Abstract: Diffusion Large Language Models (dLLMs) have achieved rapid progress, viewed as a promising alternative to the autoregressive paradigm. However, mos...

### 96. Pruning and Distilling Mixture-of-Experts into Dense Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.28207
- **AI 摘要**: 本文提出了一种将混合专家（MoE）转换为密集语言模型（Dense Language Models）的系统框架，通过选择、分组和连接专家来减少内存需求。
- **原始摘要**: arXiv:2605.28207v3 Announce Type: replace Abstract: Mixture-of-Experts (MoE) is now the dominant architecture for frontier language models, yet it requires all expert parameters to be loaded in memory...

### 97. From Architecture to Output: Testing the Structural Origins of Hallucination and the Amplifying Role of Data
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.07537
- **AI 摘要**: 该文章讨论了模型结构对错误的影响，并通过实验测试了这种观点。文章主题属于模型结构和错误的关系。
- **原始摘要**: arXiv:2606.07537v3 Announce Type: replace Abstract: Surveys of hallucination classify errors by how an output relates to its source, and often explain them by the model's structure: attention retrieve...

### 98. BALTO: Balanced Token-Level Policy Optimization for Hallucination Mitigation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.15893
- **AI 摘要**: 本文提出了一种新的政策优化框架BALTO，用于缓解大型语言模型生成内容中的幻觉问题。
- **原始摘要**: arXiv:2606.15893v3 Announce Type: replace Abstract: Hallucinations remain a major obstacle to deploying large language models (LLMs) in knowledge-intensive settings, where generated responses must be...

### 99. Self-Modeling Interventions can Modulate Emergent Misalignment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.23700
- **AI 摘要**: 文章讨论了通过自我模型干预来缓解模型中的不一致性问题，涉及GPT-4.1、Qwen2.5-32B-Instruct和Seed-OSS-36B-Instruct三个模型和多个EM数据集。
- **原始摘要**: arXiv:2606.23700v2 Announce Type: replace Abstract: Emergent misalignment (EM) has been linked to the activation of misaligned persona vectors and evil character traits, suggesting that EM operates th...

### 100. PrefReward: Learning User Preference Matrix for Personalized Text Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.21067
- **AI 摘要**: 本文提出了一种新的生成框架PrefReward，用于学习用户偏好矩阵，以实现个性化文本生成，相比基于模型参数的隐式表示，该框架通过结构化的偏好矩阵来指导生成过程。
- **原始摘要**: arXiv:2607.21067v2 Announce Type: replace Abstract: Large Language Models (LLMs) have demonstrated remarkable ability in generating personalized content by leveraging user histories and contextual cue...

### 101. Detecting Hallucinations and Recovering Verified Answers in Arabic Islamic Question Answering
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.03720
- **AI 摘要**: 该文章讨论了如何检测大型语言模型生成的阿拉伯语伊斯兰问题回答中的错误，并选择正确的答案。文章介绍了用于检测错误和选择正确答案的系统。
- **原始摘要**: arXiv:2608.03720v2 Announce Type: replace Abstract: Large language models can generate fluent responses to Islamic questions while introducing factual errors that are difficult to identify. This paper...

### 102. Time as Structure: A Temporal Backbone for Extraction and Reasoning over Legal Documents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.15270
- **AI 摘要**: 该文章讨论了语言模型在法律文档中的应用，通过提取日期和依赖关系构建时间依赖图，并使用日历修正引擎计算判决日期。文章展示了模型在UK Employment Appeal Tribunal判决中的表现。
- **原始摘要**: arXiv:2608.15270v3 Announce Type: replace Abstract: Miss a filing deadline by one day and the claim is barred, however strong the case. Computing that deadline is rarely simple: the period runs from a...

### 103. Auditing Cross-Lingual Fairness in Language Model Watermarking
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.20047
- **AI 摘要**: 文章讨论了跨语言模型水印检测阈值的设计选择，并提出了一种包含四个组件的评估框架。
- **原始摘要**: arXiv:2608.20047v2 Announce Type: replace Abstract: Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a...

### 104. Quantifying the Generation Modality Gap in Speech-Text Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.14743
- **AI 摘要**: 文章讨论了语音-文本语言模型之间存在的生成内容不一致的问题，提出了一个统一的生成评估套件来比较不同模态的语言模型。
- **原始摘要**: arXiv:2609.14743v3 Announce Type: replace Abstract: Pure speech language models often lag behind text and speech-text language models in generating coherent content, but this gap is difficult to quant...

### 105. Easy to anticipate, hard to compute: boundary dependence finds the computed outputs that entropy patching misses
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.11790
- **AI 摘要**: 文章讨论了语言模型在处理边界依赖和熵修补时存在的问题，并提出了一种结合边界依赖信号的方法来提高模型性能。
- **原始摘要**: arXiv:2610.11790v2 Announce Type: replace Abstract: Byte-level language models such as the Byte Latent Transformer (BLT) group bytes into patches and run their large global model once per patch. BLT s...

### 106. Text Generation in Low-Resource Languages Using Human-Curated Vocabularies
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.37105
- **AI 摘要**: 该文章讨论了如何利用人类编纂的词汇表和少量的人类编写示例来让大型语言模型在资源稀缺的语言中生成连贯的文本。
- **原始摘要**: arXiv:2610.37105v2 Announce Type: replace Abstract: Synthetic text generation offers a promising approach to alleviating data scarcity in low-resource languages. However, its effectiveness is inherent...

### 107. WarBias: A Bilingual LLM Benchmark of Stereotypes About Internally Displaced People and Veterans
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.11284
- **AI 摘要**: 本文介绍了一个关于退伍军人和内战难民的双语基准测试WarBias，旨在评估语言模型对这两个群体的刻板印象。
- **原始摘要**: arXiv:2611.11284v2 Announce Type: replace Abstract: This paper contains examples of stereotypes about veterans and displaced people that may be offensive or distressing. Social bias benchmarks for lan...

### 108. When Should Diffusion Language Models Reconsider Their Commitments?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.11551
- **AI 摘要**: 本文介绍了一种新的训练框架PURL，用于改进扩散语言模型在并行采样中的早期标记承诺。
- **原始摘要**: arXiv:2611.11551v2 Announce Type: replace Abstract: Masked Diffusion Models (MDMs) are well known for fast text generation via parallel decoding. However, independent parallel sampling can commit to i...

### 109. MNN-Pocket-0.3B Technical Report
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12311
- **AI 摘要**: MNN-Pocket-0.3B是针对边缘设备（如智能手机和智能眼镜）的紧凑型300M参数语言模型，支持长达32K的上下文长度。
- **原始摘要**: arXiv:2611.12311v2 Announce Type: replace Abstract: This technical report presents MNN-Pocket-0.3B, a compact 300M-parameter dense language model designed for efficient on-device deployment and suppor...

### 110. Examining the Impact of Data and Training Methods on Emergent and Subliminal Misalignment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.12798
- **AI 摘要**: 该文章讨论了数据和训练方法对语言模型行为变化的影响，特别是关于涌现性不一致和潜意识学习的现象。
- **原始摘要**: arXiv:2605.12798v2 Announce Type: replace-cross Abstract: Post-training a language model can induce surprising behavioral changes far beyond the intended training target. We study two particularly str...

### 111. Einstein World Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.26969
- **AI 摘要**: 文章讨论了Einstein World Models，这是一种基于语言模型的推理系统，允许模型通过视觉和时间滚动来补充语言，以增强其复杂思维能力。
- **原始摘要**: arXiv:2606.26969v2 Announce Type: replace-cross Abstract: Does intelligence require the ability to reason about phenomena beyond direct experience? It is natural to suspect that some complex thought c...

### 112. Probing the Origins of Reasoning Performance: Representational Quality for Mathematical Problem-Solving in RL vs. SFT Fine-Tuned Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.26119
- **AI 摘要**: 该文章讨论了强化学习训练的语言模型在数学推理任务中的表现优于监督微调模型的机制基础，提出了两方面的证据：层间线性探针在合成数学问题上预测答案正确性的准确性更高，且RL训练模型的准确度下降随层数加深而增加。
- **原始摘要**: arXiv:2607.26119v2 Announce Type: replace-cross Abstract: Large language models trained with reinforcement learning (RL) to reason step by step have been increasingly shown to outperform their supervi...

### 113. Multimodal Model Diffing for Feature Discovery and Control
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.09928
- **AI 摘要**: 本文介绍了一种新的模型差异框架MMDiff，用于发现和控制多模态模型的行为。
- **原始摘要**: arXiv:2608.09928v2 Announce Type: replace-cross Abstract: Multimodal Large Language Models (MLLMs) exhibit strong visual understanding, yet the internal features that cause these behaviors remain diff...

### 114. ST$^2$U: Stateful Test-Time Unlearning via Restricted Knowledge Boundary Control
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2608.23034
- **AI 摘要**: 文章讨论了如何通过控制大型语言模型中的受限知识来避免测试时间回退，提出了ST$^2$U方法。
- **原始摘要**: arXiv:2608.23034v2 Announce Type: replace-cross Abstract: Controlling restricted knowledge in large language models is essential for model alignment and safe deployment. Test-time unlearning avoids co...

### 115. Characterising divergence between heuristic and language-model ratings of mobile user interface quality
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.05423
- **AI 摘要**: 该文章讨论了语言模型与基于规则的启发式评分在移动用户界面质量评估中的不一致性，涉及人工智能和评估技术领域。
- **原始摘要**: arXiv:2609.05423v2 Announce Type: replace-cross Abstract: Automated assessment of mobile user interface quality is attractive because manual review does not scale, and large language models are increa...

### 116. Compute-Optimal Scaling Laws for Spiking Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.15146
- **AI 摘要**: 该文章讨论了稀疏激活的神经网络在大规模语言建模中的计算效率与准确性之间的关系，提出了一个计算最优前沿的指数关系。
- **原始摘要**: arXiv:2610.15146v3 Announce Type: replace-cross Abstract: Spiking neural networks target energy-efficient language modeling through sparse, binary activations, but the efficiency-accuracy tradeoff of...

### 117. Muon Makes the First Mixture-of-Experts Layer Harder to Balance
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.37914
- **AI 摘要**: 文章讨论了Muon优化器在混合专家模型中的应用及其对模型参数分布的影响。
- **原始摘要**: arXiv:2610.37914v2 Announce Type: replace-cross Abstract: Many open mixture-of-experts (MoE) language models train with Muon instead of AdamW. Most balance the load with a bias on each expert's routin...

### 118. Counting Events, Not Seeing Them: Diagnosing and Repairing the Readout Failure in Video LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.09949
- **AI 摘要**: 本文研究了视频语言模型在计数物体在屏幕上的出现次数时出现的读取失败问题，提出了修复方法。
- **原始摘要**: arXiv:2611.09949v2 Announce Type: replace-cross Abstract: Video LLMs fail conspicuously at counting how many times an object crosses the screen, a failure attributed to missing object permanence. Usin...

### 119. LandslideFM: A Foundation Model Towards Unified Landslide Perception and Understanding
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12936
- **AI 摘要**: 该文章讨论了一种统一的基础模型LandslideFM，旨在解决智能滑坡检测中的孤立视觉任务、大量标注数据需求和缺乏深入分析和场景理解能力的问题。
- **原始摘要**: arXiv:2611.12936v1 Announce Type: new Abstract: Intelligent landslide detection is essential for disaster prevention. However, existing models primarily focus on isolated visual tasks, require extensi...

### 120. Reinforcement Learning based control of Cancer Chemotherapy treatments
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12940
- **AI 摘要**: 该研究关注利用强化学习技术优化癌症化疗治疗方案，主要探讨了强化学习在癌症化疗治疗中的应用。
- **原始摘要**: arXiv:2611.12940v1 Announce Type: new Abstract: Reinforcement Learning has achieved tremendous success in recent years. Extending its scope from the traditional complex games such as Atari, Go, Pokema...

### 121. Tabular Foundation Models vs Tuned Gradient Boosting for Telecom Churn: A Profit- and Calibration-Aware Evaluation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12942
- **AI 摘要**: 该文章讨论了Tabular Foundation Models与优化后的梯度提升树在电信客户流失预测中的表现，涉及模型排名、预期最大利润（EMP）和概率驱动阈值政策。
- **原始摘要**: arXiv:2611.12942v1 Announce Type: new Abstract: Tabular foundation models (TFMs) predict from a labelled context in a single forward pass. A recent benchmark reported that they decisively outperform t...

### 122. Physics2Weight: Direct Neural Network Architecture and Weight Generation from Physical Laws Using Large Language Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12954
- **AI 摘要**: 该文章介绍了一种新的框架Physics2Weight，能够直接利用大型语言模型生成物理方程的神经网络权重，无需基于梯度的优化。
- **原始摘要**: arXiv:2611.12954v1 Announce Type: new Abstract: Recent advances in large language models (LLMs) have enabled weight-space programming (WSP), which directly generates neural network weights without gra...

### 123. Living constitutions: Participatory alignment for sovereign foundation models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13402
- **AI 摘要**: 该文章讨论了如何通过参与式方法制定宪法级AI模型的宪法，以确保模型的正确性与民主性。
- **原始摘要**: arXiv:2611.13402v1 Announce Type: new Abstract: In Constitutional AI, a plain-text "constitution" encodes values and gets incorporated into a model via post-training. However, the procedure for creati...

### 124. The WoW: A Large-Scale World Knowledge Corpus for Full-Lifecycle LLM Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13487
- **AI 摘要**: 该文章介绍了一种名为WoW的世界知识语料库，用于大型基础模型的全生命周期训练，该语料库基于教育知识图谱构建，旨在提高模型在各种基准测试中的性能。
- **原始摘要**: arXiv:2611.13487v1 Announce Type: new Abstract: Existing Chinese educational corpora often suffer from fragmented coverage and a lack of systematic organization. In this paper, we propose WoW (\textbf...

### 125. Nepali-English Code-Mixed Speech Recognition: Data Preparation and Adaptation of a Speech Foundation Model
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13512
- **AI 摘要**: 该文章讨论了如何通过数据准备和适应方法改进一个混合的TDT-CTC模型，使其能够识别尼泊尔语和英语混合的语音数据。
- **原始摘要**: arXiv:2611.13512v1 Announce Type: new Abstract: Nepali speakers regularly mix English words into conversation, but multilingual speech recognisers often struggle with language switches and the writing...

### 126. Topological Dynamics Under Non-Stationary Supervision: Persistent Homology of Neural Network Weight Evolution
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13701
- **AI 摘要**: 该文章讨论了神经网络权重点云在稳定和非平稳监督下的拓扑动态变化，涉及Fashion-MNIST数据集的训练。
- **原始摘要**: arXiv:2611.13701v1 Announce Type: new Abstract: We investigate how the persistent topology of neuron- weight point clouds evolves under stable and non-stationary supervision. An identical multilayer p...

### 127. Broad-Persistent Advising in Interactive Reinforcement Learning via Latent State Encoding
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13712
- **AI 摘要**: 该文章讨论了一种名为Encoder BPA的方法，用于增强交互式强化学习中的持续建议。文章提出了一种使用潜在编码器来检索和重用建议的方法。
- **原始摘要**: arXiv:2611.13712v1 Announce Type: new Abstract: Deep Interactive Reinforcement Learning (Deep IntRL) accelerates reinforcement learning training by incorporating external advice. However, conventional...

### 128. Integrating Action Prefix Prediction and Alignment Across Modalities for Multimodal Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13782
- **AI 摘要**: 文章讨论了在强化学习中通过结合动作前缀预测和基于对比多模态学习的对齐方法来改进多模态表示学习。文章提出了改进的预测表示方法。
- **原始摘要**: arXiv:2611.13782v1 Announce Type: new Abstract: Learning representations from multimodal observations is difficult in reinforcement learning with limited interaction data. Multimodal Joint Predictive...

### 129. An Energy-Based Perspective on Machine Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14383
- **AI 摘要**: 文章讨论了基于能量的模型，并展示了它们如何连接机器学习的不同方面，包括采样、变分推理和最大似然学习方法。
- **原始摘要**: arXiv:2611.14383v1 Announce Type: new Abstract: Energy-based models (EBMs) define a distribution through a scalar energy, $p_\theta(x)\propto\exp(-E_\theta(x))$, and are usually presented as one model...

### 130. AFNO: Universal Certifiably-Arbitrage-Free Operator Learning Framework for European Call-Price Surfaces
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12899
- **AI 摘要**: 文章讨论了一种新的神经操作器框架AFNO，用于消除欧洲期权价格表面的无套利性问题。
- **原始摘要**: arXiv:2611.12899v1 Announce Type: cross Abstract: Neural operators (NOs) have been introduced as deep learning-powered solutions to the computational bottleneck of solving families of problems. Once t...

### 131. MADSNet: A Multi-Scale Axial-Attentive Dense Spiking Network for Spike Camera Image Reconstruction
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.12980
- **AI 摘要**: 本文提出了一种用于光相机图像重建的MADSNet多尺度轴向注意密集型神经网络，该网络在PSNR和Spk2ImgNet基准测试中均优于现有方法。
- **原始摘要**: arXiv:2611.12980v1 Announce Type: cross Abstract: Spike cameras encode dynamic scenes into high-temporal-resolution binary spike streams for efficient high-speed vision. Although spiking neural networ...

### 132. Wrong the Same Way: Cross-Prompt Sharing Both Suppresses and Amplifies Reward Hacking in RLVR
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13218
- **AI 摘要**: 文章讨论了RLVR与不完美验证器互动的两种解释，并研究了泄露的普遍性和验证器的静态假阳性率对奖励劫持的影响。
- **原始摘要**: arXiv:2611.13218v1 Announce Type: cross Abstract: Two accounts of how reinforcement learning with verifiable rewards (RLVR) interacts with an imperfect verifier coexist: in one, reward hacking is inhe...

### 133. Off-policy Learning with Excursion Policies
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13275
- **AI 摘要**: 文章讨论了Off-policy学习中的Excursion策略，这是一种新的策略结构，通过多步“探险”阶段来学习目标策略的价值。
- **原始摘要**: arXiv:2611.13275v1 Announce Type: cross Abstract: Off-policy reinforcement learning (RL) tries to learn the value of a target policy while data comes from a different behavior policy. This often requi...

### 134. Stochastic Projections and Rank-Aware Learning Rates for Federated LoRA
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13331
- **AI 摘要**: 本文提出了一种新的方法来优化联邦LoRA模型的训练，通过冻结和周期性重采样适应矩阵，以减少计算和通信开销。
- **原始摘要**: arXiv:2611.13331v1 Announce Type: cross Abstract: Fine-tuning large-scale foundation models across resource-constrained, distributed clients presents significant computational and communication challe...

### 135. Enforcing Axioms for AI Alignment under Loss-Based Rules
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13369
- **AI 摘要**: 该文章讨论了在基于损失的训练方法下，如何通过改进奖励模型或比较数据来恢复帕累托最优性。
- **原始摘要**: arXiv:2611.13369v1 Announce Type: cross Abstract: Many alignment methods, most notably reinforcement learning from human feedback (RLHF), train reward models by minimizing a loss on pairwise compariso...

### 136. Sharp Sample Complexity of KL-Regularized Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13480
- **AI 摘要**: 文章讨论了KL-正则化强化学习的样本复杂度，提出了在折扣MDP中找到最优策略所需的样本数量，该数量与状态动作对数、折扣因子和温度有关。
- **原始摘要**: arXiv:2611.13480v1 Announce Type: cross Abstract: KL-regularized reinforcement learning, the objective behind maximum-entropy RL and RL from human feedback, is variational inference in the graphical m...

### 137. Reasoning-Aware Relational Representation Learning for Open-Vocabulary Scene Graph Generation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13496
- **AI 摘要**: 该文章讨论了一种新的框架RaRe，用于解决开放词汇场景图生成中的关系表示学习问题，旨在改善模型在罕见关系识别和未知谓词上的泛化能力。
- **原始摘要**: arXiv:2611.13496v1 Announce Type: cross Abstract: Open-Vocabulary Scene Graph Generation (OV-SGG) requires models to recognize visual relationships beyond the training vocabulary, yet existing methods...

### 138. Mixed Signals: Weight-Space Programming for EEG and ECG
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13758
- **AI 摘要**: 文章讨论了在脑电图（EEG）和心电图（ECG）数据上训练的语言模型，能够通过推理而不是梯度下降来训练模型，并且能够从头开始编写网络的所有权重。
- **原始摘要**: arXiv:2611.13758v1 Announce Type: cross Abstract: Weight-space programming allows language models to read a trained neural network's weights and edit them. This opens the door to ``training'' by reaso...

### 139. Satellite Pretraining Is Not One Thing: A Matched-Pair Study of Generic and Earth-Observation Foundation Models for Scene Classification
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13849
- **AI 摘要**: 文章讨论了地球观测模型和通用模型在RGB场景分类数据集上的预训练效果，发现地球观测预训练对某些数据集和指标有显著提升，但对其他数据集和指标则有显著损害。
- **原始摘要**: arXiv:2611.13849v1 Announce Type: cross Abstract: Geospatial foundation models are pretrained on satellite and aerial imagery, but whether such an encoder beats a strong generic one for few-label land...

### 140. Mechanistic Interpretability of Deep Neural Networks: Methods, Frameworks, and Perspectives
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13868
- **AI 摘要**: 文章讨论了深度神经网络内部机制的解释方法和框架，属于AI模型类别。
- **原始摘要**: arXiv:2611.13868v1 Announce Type: cross Abstract: Deep neural networks underpin fundamental tasks in a wide range of signal domains, such as image, audio, and language processing. However, their inter...

### 141. Margin-Guided Token Credit for Reinforcement Learning with Verifiable Rewards
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14015
- **AI 摘要**: 本文提出了一种新的方法MCPO，用于强化学习中的可验证奖励，通过在模型犹豫的地方分配奖励，提高了模型的性能。
- **原始摘要**: arXiv:2611.14015v1 Announce Type: cross Abstract: In reinforcement learning with verifiable rewards, a language model is rewarded for a correct final answer, and GRPO passes that reward to every token...

### 142. Representational Atoms in Neural Networks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14168
- **AI 摘要**: 文章讨论了神经网络内部表示的基本单元（FRUs）的概念及其在保持高准确性和稳定性方面的有效性。
- **原始摘要**: arXiv:2611.14168v1 Announce Type: cross Abstract: Understanding the internal representations of neural networks and characterizing their relationship with human conceptual structure are two critical q...

### 143. Quantifying the Sampling Frequency Invariance of Time-Series Foundation Models for Sensor Data Applications
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14425
- **AI 摘要**: 该文章讨论了时间序列基础模型在传感器数据应用中的采样频率不变性测试，涉及四个主要模型。
- **原始摘要**: arXiv:2611.14425v1 Announce Type: cross Abstract: Time-Series Foundation Models (TSFMs) are increasingly used in sensor applications, where sampling frequency (SF) varies across sensors, devices, and...

### 144. Toward Foundation Detection Models via Example-Based Grounding in EM-DETR
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14518
- **AI 摘要**: 该文章讨论了一种新的方法来构建一个多领域的基础模型用于病变检测，该方法结合了多种医疗图像数据集，并且能够处理不同标签空间的数据。
- **原始摘要**: arXiv:2611.14518v1 Announce Type: cross Abstract: DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depen...

### 145. Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14519
- **AI 摘要**: 文章讨论了将预训练的通用模型应用于医学影像分割，与特定任务训练的模型进行比较。文章分析了不同策略下基础模型的适应效果。
- **原始摘要**: arXiv:2611.14519v1 Announce Type: cross Abstract: Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they...

### 146. Robustness Verification in Neural Networks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2024年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2403.13441
- **AI 摘要**: 该文章讨论了神经网络计算的正式验证问题，包括输入输出的线性规划实例和网络功能的相同性等问题。文章提出了一个理论框架来分析这些问题的计算复杂性。
- **原始摘要**: arXiv:2403.13441v2 Announce Type: replace Abstract: In this paper we investigate formal verification problems for Neural Network computations. Of central importance will be various robustness and mini...

### 147. Towards end-to-end LLM-based censoring-aware survival analysis
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.25399
- **AI 摘要**: 本文介绍了一种新的框架LLMSurvival，它能够使用未经修改的大语言模型（LLMs）直接处理临床数据中的生存分析问题，克服了传统方法中因 censoring 导致的困难。
- **原始摘要**: arXiv:2605.25399v2 Announce Type: replace Abstract: Objective: Survival analysis is central to medical prediction, yet large language models (LLMs) are rarely used as end-to-end survival models becaus...

### 148. Purin: A Biology-inspired Mechanism for Artificial Neural Networks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.31235
- **AI 摘要**: 该文章提出了一种基于生物学机制的人工神经网络机制Purin，以解决固定权重和离散时间步长带来的问题。
- **原始摘要**: arXiv:2609.31235v2 Announce Type: replace Abstract: Artificial neural networks (ANNs) usually represent neural transmission with fixed trainable weights during a training batch, which omits short-term...

### 149. IECG: Weakly-Supervised Interpretability-Enhancing Foundation Model for Electrocardiogram
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.28083
- **AI 摘要**: 本文介绍了一种弱监督的ECG基础模型IECG，该模型能够在不依赖手动标注异常区域的情况下进行诊断分类和异常定位，提高ECG分析的可解释性。
- **原始摘要**: arXiv:2610.28083v2 Announce Type: replace Abstract: Electrocardiography (ECG) is a cornerstone of cardiac diagnosis, yet most machine learning methods for ECG analysis lack interpretability, limiting...

### 150. Are Spiking Neural Networks Harder to Steal? The Role of Stochastic Encoding in Model Extraction
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.36298
- **AI 摘要**: 该文章讨论了在边缘设备上部署的机器学习模型容易受到模型窃取攻击的问题，并研究了稀疏编码在防止模型窃取中的作用，特别是针对稀疏神经网络（SNNs）和人工神经网络（ANNs）的比较。
- **原始摘要**: arXiv:2610.36298v2 Announce Type: replace Abstract: Machine learning models deployed on edge devices are vulnerable to model stealing attacks, in which an adversary replicates a model using only its p...

### 151. Learning to Reason from Reference Samples Alone: Reinforced Adversarial Learning for Modern LLM Post-Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.38851
- **AI 摘要**: 文章讨论了一种新的方法Reinforced Adversarial Learning (RAL)，用于在没有显式奖励的情况下训练推理语言模型。
- **原始摘要**: arXiv:2610.38851v3 Announce Type: replace Abstract: In many settings where LLM post-training is desirable, high-quality answers are recognizable but difficult to score with explicit rewards. Reinforce...

### 152. Cross-Modality Investigation on WESAD Stress Classification
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2025年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2502.18733
- **AI 摘要**: 该文章讨论了使用Transformer模型在WESAD数据集上进行跨模态压力分类的研究，涉及心电图、皮肤电活动、肌电图、呼吸率、体温和3轴加速度计信号。
- **原始摘要**: arXiv:2502.18733v2 Announce Type: replace-cross Abstract: Deep learning's growing prevalence has driven its widespread use in healthcare, where AI and sensor advancements enhance diagnosis, treatment,...

### 153. Deep Double Q-learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2025年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2507.00275
- **AI 摘要**: 本文介绍了一种新的深度双Q学习算法DDQL，通过引入双Q学习目标来训练两个Q函数，以解决直接训练单个Q函数导致的估计器相关性问题。
- **原始摘要**: arXiv:2507.00275v3 Announce Type: replace-cross Abstract: Double Q-learning is a classical control algorithm that mitigates the maximization bias of Q-learning. To do so, it explicitly trains two inde...

### 154. FiLoRA: Focus-and-Ignore LoRA for Controllable Feature Reliance
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.02060
- **AI 摘要**: 文章讨论了FiLoRA方法，这是一种用于控制模型内部特征依赖的框架，主要关注的是模型的可控性。
- **原始摘要**: arXiv:2602.02060v3 Announce Type: replace-cross Abstract: Multimodal foundation models integrate heterogeneous signals across modalities, yet it remains unclear whether their predictions can be contro...

### 155. COMO: Closed-Loop Optical Molecule Recognition with Minimum Risk Training
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2604.23546
- **AI 摘要**: 文章讨论了在光学化学结构识别中引入最小风险训练（MRT）的方法，提出了一种新的框架COMO来减少暴露偏差，以提高分子识别的准确性。
- **原始摘要**: arXiv:2604.23546v2 Announce Type: replace-cross Abstract: Optical chemical structure recognition (OCSR) translates molecular images into machine-readable representations such as SMILES strings or mole...

### 156. MC$^2$: Monte Carlo Correction for Fast Elliptic PDE Solving
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.09288
- **AI 摘要**: 该文章讨论了一种新的混合神经网络-蒙特卡洛偏微分方程求解器MC$^2$，它结合了蒙特卡洛方法和神经网络，旨在提高求解偏微分方程的精度和效率。
- **原始摘要**: arXiv:2605.09288v2 Announce Type: replace-cross Abstract: Partial differential equation (PDE) solvers underpin modern computer graphics, geometry processing, and scientific computing. Classical Monte...

### 157. Diff-Instruct with Diffused Reward: Towards Principled One-step Generator RL
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.24001
- **AI 摘要**: 本文提出了一种新的方法Diff-Instruct with Diffused Reward（DIDR），用于解决文本到图像生成中的奖励优化问题。
- **原始摘要**: arXiv:2605.24001v3 Announce Type: replace-cross Abstract: Recent advances in one-step text-to-image generation have enabled real-time synthesis with remarkable efficiency and quality. Previous reinfor...

### 158. Adaptive Reparametrized Time for Score-Based Diffusion Sampling
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.02137
- **AI 摘要**: 该文章讨论了用于分数驱动扩散采样的时间分配方法，提出了一种连续时间控制形式，ART，用于学习采样时钟的速度以适应原扩散时间。
- **原始摘要**: arXiv:2607.02137v4 Announce Type: replace-cross Abstract: We study timestep allocation for score-based diffusion sampling, where a learned reverse-time dynamics is discretized on a finite grid. Unifor...

### 159. Reinforcement Learning over Patient Trajectories for Clinical Reasoning in EHR Foundation Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.12277
- **AI 摘要**: 该文章讨论了使用强化学习对电子健康记录基础模型进行微调的方法，以增强其临床推理能力，特别是在有限和不完整的电子健康记录数据下。
- **原始摘要**: arXiv:2609.12277v2 Announce Type: replace-cross Abstract: Electronic health record (EHR) foundation models trained on longitudinal patient trajectories have demonstrated strong performance across dive...

### 160. Learning Perturbation Robust Policies for LLM Agents with Stable Optimization
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.34064
- **AI 摘要**: 文章讨论了如何通过稳定优化策略提高语言模型代理对各种扰动的鲁棒性，涉及RL和政策优化。
- **原始摘要**: arXiv:2609.34064v2 Announce Type: replace-cross Abstract: Reinforcement learning (RL) has become an effective post-training paradigm for long-horizon large language model (LLM) agents. However, we fin...

### 161. Byzantine-Robust Muon: Resilient Momentum Orthogonalization for Distributed Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13137
- **AI 摘要**: 文章讨论了Muon优化器在分布式和联邦学习中的鲁棒性，特别是在对抗性行为和数据异质性方面的表现。
- **原始摘要**: arXiv:2611.13137v1 Announce Type: new Abstract: Optimization methods, including the Muon optimizer based on the Linear Minimization Oracle (LMO) and momentum orthogonalization, have shown strong empir...

### 162. Domain-Routed Delta Optimization for Multi-Teacher On-Policy Distillation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13249
- **AI 摘要**: 该文章讨论了一种新的多教师在线策略蒸馏方法，通过指定每个样本所属的域教师来优化学生参数。
- **原始摘要**: arXiv:2611.13249v1 Announce Type: new Abstract: Multi-teacher on-policy distillation assigns each sample a domain teacher but typically updates shared student parameters. We introduce Domain-Routed De...

### 163. An Analytical Model of Compute-limited Multistage Training Pipelines
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13276
- **AI 摘要**: 文章讨论了多阶段训练管道中的计算限制模型，涉及预训练、监督微调和强化学习。
- **原始摘要**: arXiv:2611.13276v1 Announce Type: new Abstract: Modern foundation models are trained through multiple stages, yet how these stages interact and how compute should be allocated across them remain poorl...

### 164. Looping Deeper Without Growing the KV Cache: Recurrent Depth for Causal Encoder-Decoders
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13378
- **AI 摘要**: 该文章讨论了一种新的语言模型设计，通过循环深度来减少参数数量，同时保持全上下文的键值存储，解决了模型在处理长上下文时的内存限制问题。
- **原始摘要**: arXiv:2611.13378v1 Announce Type: new Abstract: Looped language models deepen computation without adding parameters, yet caching full-context key-value (KV) states across layers and rounds severely bo...

### 165. SLIC: Reinforcement Fine-Tuning Small LMs for Multi-Turn Analog Circuit Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13452
- **AI 摘要**: 该文章介绍了一种用于模拟电路优化的小型语言模型强化微调框架SLIC，适用于多轮迭代设计。
- **原始摘要**: arXiv:2611.13452v1 Announce Type: new Abstract: Analog integrated circuit (IC) design is a multi-turn, simulator-grounded engineering task that demands iterative reasoning over coupled performance tra...

### 166. Parallel Broyden Methods for Efficiently Evaluating Nonlinear State Space Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13523
- **AI 摘要**: 该文章讨论了用于高效评估非线性状态空间模型的并行Brodyen方法，涉及机器学习中的模型评估和优化。
- **原始摘要**: arXiv:2611.13523v1 Announce Type: new Abstract: Nonlinear state space models are typically evaluated sequentially, limiting their ability to exploit modern parallel hardware. Recent work has shown tha...

### 167. Beyond the Log-Linear Frontier: Pre-Asymptotic Analysis of Finite-Budget Neural Scaling Laws
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13534
- **AI 摘要**: 该文章讨论了神经网络规模和数据规模在有限预算下的非线性规律，分析了谱异质性和域异质性的影响。
- **原始摘要**: arXiv:2611.13534v1 Announce Type: new Abstract: Classical neural scaling laws model excess risk as a separable power law in model capacity $N$ and dataset size $D$. At finite budgets, however, empiric...

### 168. Adaptive catalyst discovery emerges from composable scientific intelligence
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13536
- **AI 摘要**: 文章讨论了Composable Catalytic Intelligence（CatAI）框架，该框架通过学习结构-性质关系来指导催化剂设计，取得了显著的性能提升。
- **原始摘要**: arXiv:2611.13536v1 Announce Type: new Abstract: Catalysis underpins chemical manufacturing, yet knowledge for catalyst design remains dispersed across experimental observations, computational data and...

### 169. Closing the BF16-FP16 Convergence Speed Gap in RL Post-Training with Stochastic Rounding
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13545
- **AI 摘要**: 该文章讨论了在强化学习中使用BF16和FP16训练模型时收敛速度的差异，并提出了一种使用随机舍入的方法来解决这一问题。
- **原始摘要**: arXiv:2611.13545v1 Announce Type: new Abstract: BF16 is widely used to pretrain large language models because it has the same dynamic range as FP32 and converges similarly to FP32 training. However, i...

### 170. Investigating Composite Modeling in Multi-Objective Bayesian Optimization for Scientific Design
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13565
- **AI 摘要**: 文章讨论了在多目标贝叶斯优化中的复合建模方法，以提高单目标优化中的样本效率。但复合建模在多目标贝叶斯优化中的效果尚未得到充分研究。
- **原始摘要**: arXiv:2611.13565v1 Announce Type: new Abstract: Scientific design often requires balancing competing objectives that are expensive to evaluate through experiments or simulations. Multi-objective Bayes...

### 171. Unified Optimization of Traffic Signal and Lane Channelization for an Isolated Intersection Using Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13599
- **AI 摘要**: 文章讨论了使用强化学习解决交通信号控制和车道分隔设计的联合优化问题的方法。
- **原始摘要**: arXiv:2611.13599v1 Announce Type: new Abstract: Optimizing traffic signal control has been a long-lasting critical issue in traffic engineering, and a number of robust methodologies have emerged to so...

### 172. Deterministic, Reproducible Inference in Exact Integer Arithmetic, and Verifiable Distributed Inference as Its Consequence
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13730
- **AI 摘要**: 该文章讨论了使用整数算术执行优化推理以实现跨环境的可重复性和验证分布式推理的方法。
- **原始摘要**: arXiv:2611.13730v1 Announce Type: new Abstract: Optimized floating-point inference is not reproducible across environments: the same model on different hardware, compilers or thread counts can produce...

### 173. Dual-Core Tensor Wheel Decomposition with Structure-Cached Acceleration for Tensor Recovery
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13938
- **AI 摘要**: 文章讨论了改进张量轮分解的方法，以减少计算效率和内存成本。
- **原始摘要**: arXiv:2611.13938v1 Announce Type: new Abstract: Tensor wheel decomposition captures complex correlations in high-dimensional data through interactions between outer-ring factors and a high-order centr...

### 174. ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14035
- **AI 摘要**: 文章讨论了用于脑-计算机接口的电极图谱基础模型，提出了一种新的框架ScaleBrain，以解决现有框架在多尺度表示学习中的问题。
- **原始摘要**: arXiv:2611.14035v1 Announce Type: new Abstract: Foundation models pre-trained on large unlabeled electroencephalography (EEG) corpora have emerged as a transformative paradigm for Brain-Computer Inter...

### 175. Tree-Ising: Repairing Language Models with Bit-Level Ising Edits
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14210
- **AI 摘要**: 本文介绍了一种名为Tree-Ising的方法，用于通过位级Ising编辑修复语言模型，该方法将修复问题转化为模型自身BF16权重的稀疏离散优化问题。
- **原始摘要**: arXiv:2611.14210v1 Announce Type: new Abstract: Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. T...

### 176. A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14397
- **AI 摘要**: 文章讨论了LoRA在多类线性分类中的理论解释，通过统一的margin视角分析了LoRA适配器的最优情况。文章关注的是LoRA的鲁棒性到灾难性遗忘和独立训练的适配器合并。
- **原始摘要**: arXiv:2611.14397v1 Announce Type: new Abstract: Low-rank adaptation (LoRA) is the de facto method for parameter-efficient fine-tuning of large neural networks, achieving strong task adaptation with mi...

### 177. A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14467
- **AI 摘要**: 文章讨论了语言模型后训练中的策略优化，特别是覆盖崩溃和参考重置问题，提出了一些覆盖保持的算法来避免这些问题。
- **原始摘要**: arXiv:2611.14467v1 Announce Type: new Abstract: Policy optimization is central to language model post-training, yet principled guidance remains limited. We revisit its theoretical foundations to ident...

### 178. Emergent Biological Capabilities in a Foundation Model for Molecular Interactions
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14504
- **AI 摘要**: 该文章讨论了在大型无监督语料库上训练的基线模型在多模态生物学中的能力涌现，特别是在分子相互作用方面的功能、残基和键能力。
- **原始摘要**: arXiv:2611.14504v1 Announce Type: new Abstract: Foundation models trained on large unlabeled corpora develop emergent capabilities, tasks that go beyond the training objective. We extend this paradigm...

### 179. Alchemically Transferable Parameters for Variational Quantum Eigensolvers
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.11445
- **AI 摘要**: 该文章讨论了如何使用几何投影技术，将目标分子的局部化学环境映射到小的氢化碎片上，使得现有的氢化求解器可以重复使用，而无需重新训练。
- **原始摘要**: arXiv:2611.11445v1 Announce Type: cross Abstract: Machine-learned circuit parameters could remove one of the main bottlenecks of variational quantum eigensolvers: the classical optimization loop, with...

### 180. Block-Sparse Gauss-Newton Optimization of Finite Basis Physics-Informed Neural Networks: Sparse Automatic Differentiation Approach
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13231
- **AI 摘要**: 本文提出了一种基于块稀疏的高斯-牛顿优化方法，用于有限基础物理信息神经网络（FBPINNs），通过稀疏自动微分技术减少计算成本和内存需求。
- **原始摘要**: arXiv:2611.13231v1 Announce Type: cross Abstract: In this work, we develop an efficient Gauss-Newton optimization approach for finite basis physics-informed neural networks (FBPINNs). The key ingredie...

### 181. Discrete Model-Based Diffusion for Combinatorial Optimization in Multi-Robot Task Allocation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13382
- **AI 摘要**: 该文章讨论了一种新的方法Discrete Model-Based Diffusion，用于解决多机器人任务分配中的组合优化问题，该方法不需要训练。
- **原始摘要**: arXiv:2611.13382v1 Announce Type: cross Abstract: Decision making in multi-agent and multi-robot systems often involves discrete decision variables, leading to NP-hard combinatorial optimization probl...

### 182. Decision-Focused Learning via Neural Optimization Layers for Battery-Assisted Grid-Import Smoothing in AI Data Centers
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13694
- **AI 摘要**: 该文章讨论了一种用于AI数据中心电网集成的电池调度学习方法，通过神经优化层实现风险感知的电池调度。
- **原始摘要**: arXiv:2611.13694v1 Announce Type: cross Abstract: Rapid AI data-center power fluctuations challenge grid integration. Sustained grid-import smoothing requires allocating limited battery power and ener...

### 183. Adaptive Policy-Guided Error Mitigation (APGEM): A Unified Learning-Based Framework for Noise Resilience in Quantum Machine Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13815
- **AI 摘要**: 本文提出了一种新的量子机器学习错误缓解框架APGEM，该框架能够根据训练过程中的噪声变化动态选择最佳缓解策略。
- **原始摘要**: arXiv:2611.13815v1 Announce Type: cross Abstract: Error mitigation stands between variational quantum algorithms and useful results on today's noisy hardware, yet in practice a mitigation method is us...

### 184. Gradient Inversion through Linear and Affine Subspace Constraints
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13976
- **AI 摘要**: 文章讨论了联邦学习中梯度逆向攻击的方法，通过线性和仿射子空间限制来改进梯度重建的准确性。
- **原始摘要**: arXiv:2611.13976v1 Announce Type: cross Abstract: Federated learning enables multiple clients to collaboratively train a machine-learning model without directly sharing their local datasets. However,...

### 185. LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14004
- **AI 摘要**: 文章讨论了LUMIR框架，该框架通过对比学习方法将来自异构数据源的多模态旅游信息统一到一个共享的文本表示空间，并设计了交互感知融合机制来建模跨模态交互，同时将序列信号作为结构约束引导表示学习。
- **原始摘要**: arXiv:2611.14004v1 Announce Type: cross Abstract: As multimodal tourism-related information collected from heterogeneous data sources has become increasingly available, learning effective representati...

### 186. The Star Geometry of Critic-Based Regularizer Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2024年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2408.16852
- **AI 摘要**: 文章讨论了通过批评性损失函数学习星形几何体的正则化器的方法，这是一种新的正则化技术。
- **原始摘要**: arXiv:2408.16852v3 Announce Type: replace Abstract: Variational regularization is a classical technique to solve statistical inference tasks and inverse problems, with modern data-driven approaches pa...

### 187. Iterative Orthogonalization Scaling Laws
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2505.04005
- **AI 摘要**: 本文讨论了在muon优化器中使用迭代正交化过程的超参数缩放行为，指出随着矩阵规模增大，随机矩阵的奇异值会减小，可能影响优化器性能。
- **原始摘要**: arXiv:2505.04005v3 Announce Type: replace Abstract: The muon optimizer has picked up much attention as of late as a possible replacement to the seemingly omnipresent Adam optimizer. Recently, care has...

### 188. OptiMind: Improving Small Language Models for Optimization Modeling through Formulation Guidance and Multi-Turn Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2509.22979
- **AI 摘要**: OptiMind系统通过数据清理和类特定提示结合使用求解器反馈训练小语言模型，以提高小语言模型在优化建模中的性能。
- **原始摘要**: arXiv:2509.22979v3 Announce Type: replace Abstract: Mathematical optimization drives decisions in supply chains, logistics, energy, and scheduling, but translating natural-language problems into solve...

### 189. On the Origin of Algorithmic Progress in AI: Evidence from Language Model Pre-Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2511.21622
- **AI 摘要**: 文章讨论了算法对AI预训练效率的影响，通过实验发现效率提升主要由算法决定，而非其他创新。
- **原始摘要**: arXiv:2511.21622v2 Announce Type: replace Abstract: Algorithms have been estimated to increase AI pretraining FLOP efficiency by a factor of 22,000 between 2012 and 2023 (Ho et al., 2024). Running abl...

### 190. Generative Online Reinforcement Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2512.02581
- **AI 摘要**: 文章讨论了一种名为GoRL的算法框架，旨在解决强化学习中稳定优化与表达性生成之间的矛盾。
- **原始摘要**: arXiv:2512.02581v4 Announce Type: replace Abstract: Reinforcement learning (RL) faces a persistent tension: policies that are stable to optimize (e.g., Gaussians) are often too simple to represent the...

### 191. Beyond local reconstruction: Geometry-preserving output alignment for binary LLM quantization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2512.21651
- **AI 摘要**: 文章讨论了在1比特量化中，输出驱动准则在保持模型输出行为方面的问题，提出了与权重驱动准则不同的输出驱动准则，以解决量化过程中出现的误差积累和异向性失真问题。
- **原始摘要**: arXiv:2512.21651v4 Announce Type: replace Abstract: Recent advances in post-training quantization for large language models (LLMs) have demonstrated that low-bit quantization methods can maintain most...

### 192. Graph Energy Matching: Transport-Aligned Energy-Based Modeling for Graph Generation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.23398
- **AI 摘要**: 文章讨论了用于生成离散数据（如图）的基于能量的模型，特别是针对图生成的应用场景，提出了一种新的方法Graph Energy Matching来解决离散能量模型在高效和高质量采样方面的挑战。
- **原始摘要**: arXiv:2603.23398v4 Announce Type: replace Abstract: Generative modeling of discrete data, such as graphs, underpins many scientific and industrial applications, including molecular discovery and mater...

### 193. Rethinking Black-Box On-Policy Distillation: A Rubric-based Analysis
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.07396
- **AI 摘要**: 本文研究了基于评分表的监督是否能为黑盒上的政策蒸馏提供一种仅通过文本的反馈接口，以及其有效性。
- **原始摘要**: arXiv:2605.07396v2 Announce Type: replace Abstract: On-policy distillation (OPD) is a powerful paradigm for LLM post-training, yet its reliance on teacher logits restricts it to white-box teachers. In...

### 194. Tokens-per-Parameter Coverage Is Critical for Robust LLM Scaling Law Extrapolation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.08541
- **AI 摘要**: 文章讨论了语言模型参数和令牌数量之间的关系，以及如何通过控制tokens-per-parameter比率来改善模型的泛化能力。
- **原始摘要**: arXiv:2605.08541v4 Announce Type: replace Abstract: Neural scaling laws approximate a language model's loss as a power-law function of parameter count $N$ and token count $D$. Following Chinchilla-sty...

### 195. CRAFT: Conflict-Resolved Aggregation for Federated Training
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.21317
- **AI 摘要**: 本文提出了一种新的联邦学习聚合框架CRAFT，用于解决异构数据分布下的客户端更新冲突问题。
- **原始摘要**: arXiv:2605.21317v2 Announce Type: replace Abstract: The aggregation of conflicting client updates remains a fundamental bottleneck in federated learning (FL) under heterogeneous data distributions. Na...

### 196. GAIA: Geometry-Adaptive Operator Learning for Forward and Inverse Problems
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.01128
- **AI 摘要**: GAIA模型通过几何自适应整数自编码器，学习任意几何形状下的正向和反向问题的解决方案算子，实现单次通过即可解决。
- **原始摘要**: arXiv:2607.01128v2 Announce Type: replace Abstract: Operator learning for partial differential equations (PDEs) on arbitrary geometries builds fast neural surrogates for large-scale simulation. While...

### 197. On the Potential of Graph Neural Networks as Metamodels for Supply Chain Optimization: Dataset, Architectures, and Directions
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.16769
- **AI 摘要**: 本文探讨了图神经网络在供应链优化中的潜力，提出了一个公共训练数据集和初步的GNN架构研究。
- **原始摘要**: arXiv:2607.16769v3 Announce Type: replace Abstract: Graph Neural Networks (GNNs) have emerged as a powerful, differentiable class of learning models for graph-structured systems. Their ability to gene...

### 198. Total Variation Distance Estimation in Autoregressive Models
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2607.19510
- **AI 摘要**: 该文章讨论了在自回归模型中计算总变差距离的方法，涉及样本访问、对数访问和噪声对数访问三种访问模型。
- **原始摘要**: arXiv:2607.19510v2 Announce Type: replace Abstract: Modern LLM deployments use a number of implementation choices and inference optimizations (e.g., batching, custom kernels, and quantization) on top...

### 199. Scalable Bayesian Optimization of Composite Functions for Image-Based Inverse Problems in Materials Characterization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.02126
- **AI 摘要**: 该文章讨论了用于材料表征的图像反问题的可扩展贝叶斯优化方法，主要关注电子显微镜中的参数估计问题。
- **原始摘要**: arXiv:2609.02126v2 Announce Type: replace Abstract: Estimating physical parameters from scientific images is a common inverse problem in materials characterization that often relies on expensive physi...

### 200. Acceptance-Aware Draft Model Training for Speculative Decoding
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.24150
- **AI 摘要**: 该文章讨论了用于加速大型语言模型推理的推测解码技术，提出了直接优化接受长度的损失函数，适用于贪婪验证和采样解码。
- **原始摘要**: arXiv:2609.24150v2 Announce Type: replace Abstract: Speculative decoding accelerates large language model (LLM) inference by using a lightweight draft model to generate multiple candidate tokens that...

### 201. Derivative-Informed Training of Neural Operators On-the-Fly via Sketched Tangent Consistency
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2609.32797
- **AI 摘要**: 该文章讨论了一种新的训练方法sTCL，用于神经操作器的在线衍生信息训练，以提高其对输入输出敏感性的监督，适用于解决反问题、偏微分方程约束优化、设计和控制等场景。
- **原始摘要**: arXiv:2609.32797v2 Announce Type: replace Abstract: Derivative-informed training improves neural operators by directly supervising their input-output sensitivities, which is crucial when neural operat...

### 202. Data Density Scaling Laws for Image Self-Distillation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.19013
- **AI 摘要**: 该文章讨论了图像自我蒸馏模型中样本数量与模型性能的关系，提出了一种结合独特样本数量和重复次数的度量互动缩放法则。
- **原始摘要**: arXiv:2610.19013v2 Announce Type: replace Abstract: Current scaling law formulations suggest that increasing the number of unique samples in a dataset consistently improves model performance, while re...

### 203. Aligning Forest and Trees in Images & Long Captions for Visually Grounded Understanding
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2602.02977
- **AI 摘要**: 该文章讨论了如何改进视觉语言模型（如CLIP）理解长且详细描述的图像和长段落的能力，提出了一种新的模型CAFT，该模型能够更好地结合局部文本区域和全局图像文本表示。
- **原始摘要**: arXiv:2602.02977v3 Announce Type: replace-cross Abstract: Vision-language models such as CLIP often struggle to faithfully understand long, detail-rich captions, relying on dominant scene cues while o...

### 204. RECAP: Local Hebbian Prototype Learning as a Self-Organizing Readout for Reservoir Dynamics
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2603.06639
- **AI 摘要**: 该文章介绍了一种名为RECAP的学习策略，用于稳健的图像分类，结合了未训练的流体动态和一种自我组织的Hebbian原型读出机制。
- **原始摘要**: arXiv:2603.06639v2 Announce Type: replace-cross Abstract: Robust perception in brains is often attributed to high-dimensional population activity together with local plasticity mechanisms that reinfor...

### 205. Gaussian mixture models in Hilbert spaces via kernel methods
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.05996
- **AI 摘要**: 文章讨论了在希尔伯特空间中使用核方法的高斯混合模型，适用于包含时间演变的无限维随机对象的现代数据集。文章提出了基于核均值嵌入的高斯混合框架，并开发了优化算法进行估计。文章还证明了所提出算法的理论保证，并展示了在不同数据几何结构上的实验结果。
- **原始摘要**: arXiv:2605.05996v2 Announce Type: replace-cross Abstract: Modern datasets across many disciplines increasingly consist of time-evolving, potentially infinite-dimensional random objects, such as dynami...

### 206. Factor Augmented High-Dimensional SGD
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2605.19291
- **AI 摘要**: 本文提出了一种新的优化方法Factor-Augmented SGD（FSGD），它利用高维学习任务中的潜在因素表示，能够在流数据上进行操作，适用于大规模和高维问题。同时，文章建立了第一个理论框架，将潜在因素估计误差纳入SGD分析中。
- **原始摘要**: arXiv:2605.19291v2 Announce Type: replace-cross Abstract: Stochastic gradient descent (SGD) is a fundamental optimization algorithm widely used in modern machine learning. In this paper, we propose Fa...

### 207. From AGI to ASI
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2606.12683
- **AI 摘要**: 文章讨论了从AGI到ASI的发展，包括AGI和ASI的概念，以及从AGI到ASI的四种潜在路径。
- **原始摘要**: arXiv:2606.12683v3 Announce Type: replace-cross Abstract: Over the last decade, building human-level artificial general intelligence has moved from far-fetched speculation to being a concrete next-dec...

### 208. MSCR: Jointly Balancing Utilization Across Modalities and Discovering Synergistic Information
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.24395
- **AI 摘要**: 本文提出了一种新的融合方法MSCR，旨在平衡跨模态利用和发现协同信息。
- **原始摘要**: arXiv:2610.24395v2 Announce Type: replace-cross Abstract: In multimodal learning, modality imbalance often lets one modality dominate optimization and keeps the model from fully exploiting cross-modal...

### 209. Variance Reduction for Decentralized Stochastic Optimization with Multiple Local Updates
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.41927
- **AI 摘要**: 本文提出了一种结合多本地更新和方差减少的新型原-对偶式分布式优化算法，该算法的步长与网络大小无关，且与本地更新次数成反比。
- **原始摘要**: arXiv:2610.41927v2 Announce Type: replace-cross Abstract: Multiple local updates are widely used in decentralized optimization to enhance communication efficiency, often in conjunction with stochastic...

### 210. Seeing Isn't Enough: Unlocking Visual Reasoning by Bridging the Reasoning-Access Gap with TIGER
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.10552
- **AI 摘要**: 文章讨论了视觉推理模型在处理图像时的表现不如处理文本的问题，并提出了TIGER方法来解决这一问题。
- **原始摘要**: arXiv:2611.10552v2 Announce Type: replace-cross Abstract: Multimodal Large Language Models (MLLMs) inherit strong textual reasoning capabilities from their language backbones and text pretraining, but...

### 211. Few-Shot Residual Adaptation of Pretrained Latent World Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13592
- **AI 摘要**: 文章讨论了一种从少量交互中学习预训练潜世界模型的自监督修正方法，该方法用于在物理动态变化时进行适应。
- **原始摘要**: arXiv:2611.13592v1 Announce Type: new Abstract: Pretrained latent world models can support visual planning and control, but their predictions may fail when physical dynamics change at deployment. We s...

### 212. LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14048
- **AI 摘要**: 文章讨论了一种新的世界动作模型LaST0.5，该模型引入了交互为中心的物理表示，以解决现有世界动作模型在处理局部机器人-环境交互时存在的问题。
- **原始摘要**: arXiv:2611.14048v1 Announce Type: new Abstract: World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation, endowing policies with strong capabilities for modeli...

### 213. Koopman Model-Based Reinforcement Learning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.14186
- **AI 摘要**: 本文提出了一种基于Koopman模型的强化学习算法，用于控制未知动态的非线性机器人系统。
- **原始摘要**: arXiv:2611.14186v1 Announce Type: new Abstract: We propose a Koopman model-based reinforcement learning (K-MBRL) algorithm for controlling nonlinear robotic systems with unknown dynamics. The K-MBRL l...

### 214. PhysMoE: Fast Spatial Grounding with Single-Token Coordinate Representation in Modality-Decoupled VLMs
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13000
- **AI 摘要**: 本文提出了一种新的PhysMoE架构，用于解决多模态视觉语言模型在坐标预测中的瓶颈问题。
- **原始摘要**: arXiv:2611.13000v1 Announce Type: cross Abstract: Embodied Vision-Language Models (VLMs) are backbones for robotic planning and manipulation. However, for coordinate prediction in grounding tasks, exi...

### 215. CACHEFORGE: LLM-Guided End-to-End Generative Cache Replacement Policy for Performance and Hardware Efficiency
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2610.07668
- **AI 摘要**: 文章讨论了CACHEFORGE框架，它通过嵌入大型语言模型在受硬件影响的循环中，实现端到端的缓存替换策略，以提高性能和硬件效率。
- **原始摘要**: arXiv:2610.07668v2 Announce Type: replace Abstract: Modern cache replacement designs saturate because they operate within fixed representational structures, hand-crafted and heuristic based feature-en...

### 216. Curriculum proof repair with learned counterexamples
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2611.13627
- **AI 摘要**: 本文提出了一种基于语言模型的框架TopoVerus，用于Verus证明修复，通过训练生成有用的反例来改进证明过程。
- **原始摘要**: arXiv:2611.13627v1 Announce Type: new Abstract: Language models (LMs) have substantially lowered the barrier to applying formal verification for building reliable and secure software. Existing approac...

### 217. For Generalised Algebraic Theories, Two Sorts Are Enough
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI模型
- **链接**: https://arxiv.org/abs/2601.19426
- **AI 摘要**: 文章讨论了广义代数理论中涉及的多类型问题，提出了一种简化理论的方法，涉及两种类型。
- **原始摘要**: arXiv:2601.19426v3 Announce Type: replace Abstract: Generalised algebraic theories (GATs) allow multiple sorts indexed over each other. Categories have two sorts, objects and morphisms, and the latter...

### 218. GLM-5.3 Now Running on SambaCloud
- **来源**: SambaNova (TIER1)
- **发布日期**: November 11, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://sambanova.ai/blog/glm-5.3-now-running-on-sambacloud
- **AI 摘要**: 文章提到GLM-5.3模型现在运行在SambaCloud上，属于AI模型类别

### 219. Qwen-Image: Crafting with Native Text Rendering
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-image/
- **AI 摘要**: 本文介绍了一种新的图像基础模型Qwen-Image，其在复杂文本渲染和精确图像编辑方面取得了显著进展。
- **原始摘要**: GITHUB HUGGING FACE MODELSCOPE DEMO DISCORD We are thrilled to release Qwen-Image, a 20B MMDiT image foundation model that achieves significant advances in complex text rendering and precise image edi...

### 220. GSPO: Towards Scalable Reinforcement Learning for Language Models
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/gspo/
- **AI 摘要**: 本文提出了一种新的RL算法GSPO，旨在解决现有RL算法在长训练过程中出现的稳定性问题，以提升语言模型的性能。
- **原始摘要**: PAPER DISCORD Introduction Reinforcement Learning (RL) has emerged as a pivotal paradigm for scaling language models and enhancing their deep reasoning and problem-solving capabilities. To scale RL, t...

### 221. Qwen-MT: Where Speed Meets Smart Translation
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://qwenlm.github.io/blog/qwen-mt/
- **AI 摘要**: Qwen-MT是Qwen3的最新更新，支持92种语言的翻译，通过强化学习提高翻译准确性和流畅度。
- **原始摘要**: DEMO API DISCORD Introduction Here we introduce the latest update of Qwen-MT (qwen-mt-turbo) via Qwen API. This update builds upon the powerful Qwen3, leveraging trillions multilingual and translation...

### 222. 京ICP备20011824号-24
- **来源**: Zhipu AI Research (TIER1)
- **发布日期**: 2026-11-12
- **类型**: research
- **优先级**: high
- **分类**: AI模型
- **链接**: https://beian.miit.gov.cn/#/Integrated/index
- **AI 摘要**: 文章内容与AI模型、Harness工程、具身智能、AI芯片、编译器、光计算、军事技术、经济或时政等类别无关，无法判断其具体主题。

### 223. New Kimi K2 Models & Updated Pricing
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://platform.kimi.ai/blog/posts/Kimi_API_Newsletter
- **AI 摘要**: 文章摘要为新Kimim2模型及更新价格，与AI模型相关。

### 224. Progress on provable inference for large language models
- **来源**: Anthropic Research (TIER1)
- **发布日期**: 2026-11-12
- **类型**: research
- **优先级**: high
- **分类**: AI模型
- **链接**: https://www.anthropic.com/research/provable-inference
- **AI 摘要**: 文章讨论了大型语言模型的可证明推理进展，属于AI模型类别。

### 225. Introducing Gpt 5 5
- **来源**: OpenAI News (TIER1)
- **发布日期**: 2026-11-12
- **类型**: news
- **优先级**: high
- **分类**: AI模型
- **链接**: https://openai.com/index/introducing-gpt-5-5/
- **AI 摘要**: 文章标题为Introducing Gpt 5 5，摘要未提供具体信息。根据标题判断，这似乎是在介绍一个新的GPT模型，因此最可能的类别是AI模型。

### 226. Machine Learning23
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://tenstorrent.com/newsroom/newsroom/tags/machine-learning
- **AI 摘要**: 文章标题为《Machine Learning23》，但摘要未提供具体信息，无法判断其主题类别。

### 227. TT in the News1
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://tenstorrent.com/newsroom/newsroom/tags/tt-in-the-news
- **AI 摘要**: 文章标题为TT in the News1，但摘要信息不足进行详细总结。根据现有信息，无法判断文章主题。

### 228. System Engineering1
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://tenstorrent.com/newsroom/newsroom/tags/system-engineering
- **AI 摘要**: 文章标题为《System Engineering1》，但未提供足够的信息来判断其主题类别。

### 229. DeepSeek-V4.1-Flash Is Generally Available: 552B MoE, Native Vision, New Peak/Off-Peak Pricing
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-09-18
- **类型**: research
- **优先级**: high
- **分类**: AI模型
- **链接**: https://deepseek.ai/blog/deepseek-v41-flash-generally-available
- **AI 摘要**: DeepSeek发布V4.1-Flash版本，包含552B MoE模型，支持原生图像理解，原版V4-Flash和视觉变体已退役，新增高峰时段定价。
- **原始摘要**: The two-day beta became an official release: V4.1-Flash ships as deepseek-flash with native image understanding, V4-Flash and the vision variant retired, V4-Pro routed away from September 14 — and the...

### 230. DeepSeek V4.1 Flash Enters a Two-Day API Beta: Native Multimodal, 20 Concurrent Requests
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-09-08
- **类型**: blog
- **优先级**: high
- **分类**: AI模型
- **链接**: https://deepseek.ai/blog/deepseek-v41-flash-beta-native-multimodal
- **AI 摘要**: DeepSeek V4.1模型进入为期两天的API预览期，新架构、图像和文本集成于单一模型中，支持20个并发请求。
- **原始摘要**: The model ID deepseek-v4.1-flash-expires-on-0910 is live for limited testing: new architecture, images and text in one model, V4-Flash billing — and an expiry date written into the name.

### 231. DeepSeek V4.1 Flash Enters a Two-Day API Beta: Native Multimodal, 20 Concurrent Requests
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-09-08
- **类型**: research
- **优先级**: high
- **分类**: AI模型
- **链接**: https://deepseek.ai/blog/deepseek-v41-flash-beta-native-multimodal
- **AI 摘要**: DeepSeek V4.1模型进入为期两天的API预览期，支持多模态和20个并发请求。
- **原始摘要**: The model ID deepseek-v4.1-flash-expires-on-0910 is live for limited testing: new architecture, images and text in one model, V4-Flash billing — and an expiry date written into the name.

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
