# RSS 聚合报告 - 2026-11-11

**生成时间**: 2026-11-12 07:46:15
**报告日期**: 2026-11-11 (昨天)
**新发现文章**: 743 篇

## 📊 分类统计

- **AI模型**: 231 篇
- **Harness工程**: 100 篇
- **具身智能**: 78 篇
- **AI芯片**: 48 篇
- **编译器**: 2 篇
- **光计算**: 1 篇
- **军事技术**: 30 篇
- **经济**: 59 篇
- **时政**: 121 篇
- **AI应用**: 72 篇
- **未分类**: 1 篇

---

## 🏷️  AI模型

**231 篇文章**

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

## 🏷️  Harness工程

**100 篇文章**

### 1. Cyanogen co-founder unveils Kora, a Linux OS that splits AI models across the CPU, GPU, and NPU
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 13:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://www.tomshardware.com/software/linux/cyanogen-co-founder-unveils-kora-a-linux-os-that-splits-ai-models-across-the-cpu-gpu-and-npu-snapdragon-x2-elite-and-hexagon-npu-get-full-support-first
- **AI 摘要**: 文章主要介绍了Cyanogen的联合创始人推出了一款名为Kora的Linux操作系统，该系统能够将AI工作负载分布在CPU、GPU和NPU上，并且还支持连接到同一本地网络的其他机器。这属于AI工程实践和AI芯片领域。
- **原始摘要**: Kora, a Linux desktop OS with built-in AI models and agents for local agentic work, is coming to PCs in 2027, including Snapdragon X2 Elite machines.

### 2. CSTO calls for regular operations to counter drug trafficking, terrorism
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 20:18:13 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://tass.com/world/2216553
- **AI 摘要**: 文章内容主要涉及集体安全条约组织（CSTO）呼吁增加内部行动以应对毒品走私、非法移民、信息科技犯罪和恐怖主义。文章未涉及AI模型、芯片、编译器、光计算、军事技术、经济或时政等具体领域。
- **原始摘要**: The states highlighted the successful joint fighting of the competent authorities against trafficking of narcotics, psychotropic substances and their precursors

### 3. Land ahoy: leaving the Sea of Nodes
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-03-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://v8.dev/blog/leaving-the-sea-of-nodes
- **AI 摘要**: 本文介绍了V8 JavaScript引擎从使用Sea of Nodes转向使用TurboShaft的过程，解释了TurboShaft取代Sea of Nodes的原因，包括TurboShaft在生成更快代码和优化asm.js方面的能力。
- **原始摘要**: V8’s end-tier optimizing compiler, Turbofan, is famously one of the few large-scale production compilers to use Sea of Nodes (SoN). However, since almost 3 years ago, we’ve started to get rid of Sea o...

### 4. Blog Review: Nov. 11
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Wed, 11 Nov 2026 08:01:21 +0000 (今天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/blog-review-nov-11-3/
- **AI 摘要**: 文章主要讨论了AI基础设施中的互连组件的重要性，以及如何通过Adaptive Traffic Profiles来确保互连能够满足实际的带宽需求。此外，还提到了如何通过设计安全功能来缓解控制流攻击。
- **原始摘要**: Interconnects key in AI infrastructure; floating nets; mitigating Control Flow attacks; PNT trends; SEMI Market Symposium. The post Blog Review: Nov. 11 appeared first on Semiconductor Engineering....

### 5. MICRO: A Surgery-Phase Retinal Image Rigid Registration Benchmark and One-Step Frequency-Structure Similarity Registration Learning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13045
- **AI 摘要**: 该文章讨论了用于眼科手术的多模态视网膜图像精确注册数据集MICRO的介绍，MICRO包含跨模态视网膜图像配准数据，涵盖了手术的不同阶段。文章还讨论了现有的深度注册方法通过两步分割-检测框架实现的MRIRG结果。
- **原始摘要**: arXiv:2611.13045v1 Announce Type: new Abstract: Precise multimodal retinal image rigid registration (MRIRG) is essential for aligning cross-modal vessel structures, offering critical guidance for opht...

### 6. VIGOR: Benchmarking Visual Rationale Correctness in Multimodal Large Language Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13150
- **AI 摘要**: 文章讨论了如何评估多模态大型语言模型的视觉推理正确性，提出了VIGOR基准来衡量视觉推理的质量。
- **原始摘要**: arXiv:2611.13150v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) are typically evaluated by whether they produce correct answers, but correctness alone does not reveal whether...

### 7. Multimodal Judges Flag, Humans Decide: A Review-and-Edit Framework for AI-Generated Product Video Ads
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13178
- **AI 摘要**: 该文章描述了一种用于审核和编辑AI生成的电商产品视频广告的方法，包括人类评审员和AI模型的协作。
- **原始摘要**: arXiv:2611.13178v1 Announce Type: new Abstract: Generative pipelines can now turn every product page of an e-commerce catalog into a short video ad, but deciding whether such an ad is usable is not on...

### 8. Multimodal Road Closure Mapping via Cross-Modal Graph Attention
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13192
- **AI 摘要**: 文章讨论了一种统一的多模态多任务框架，用于准确识别道路关闭情况，该框架结合了地图数据、卫星图像和街景图像，通过跨模态图注意力机制进行学习。
- **原始摘要**: arXiv:2611.13192v1 Announce Type: new Abstract: Accurate and timely identification of road closures is critical for large-scale navigation and logistics systems, yet remains challenging due to the nee...

### 9. Before Words, Beyond Speech: Evaluating Nonverbal Social Reasoning in Early Childhood
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13213
- **AI 摘要**: 该文章讨论了一个针对儿童非言语社交推理的基准测试，旨在解决现有基准侧重于成人对话互动的问题。
- **原始摘要**: arXiv:2611.13213v1 Announce Type: new Abstract: Children's earliest years are a period of intense social learning, during which meaning is built through gaze, gesture, and physical contact. Yet, this...

### 10. UniWeaver: Harnessing Unified Multimodal Models for Interleaved Text-Image Generation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13530
- **AI 摘要**: 本文提出了一种名为UniWeaver的框架，用于训练统一的多模态模型，以生成混合文本和图像的内容。UniWeaver结合了多模态规划、生成和视觉反馈，以产生连贯的混合输出。
- **原始摘要**: arXiv:2611.13530v1 Announce Type: new Abstract: Unified multimodal models (UMMs) have opened up new possibilities for generating rich interleaved text-image content. However, they generally lack nativ...

### 11. CASCADE: Constraint-Aware SCAffolded DEcomposition for Logical Anomaly Detection
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13820
- **AI 摘要**: 这篇文章讨论了逻辑异常检测中的问题，提出了一种新的方法CASCADE来解决文本和图像之间的不匹配问题。
- **原始摘要**: arXiv:2611.13820v1 Announce Type: new Abstract: Logical Anomaly Detection (LAD) requires verifying whether all category-specific constraints, such as object counts, pairing relations, and measurement...

### 12. Towards Text-Only Remote Sensing Scene Classification via Semantic Proxy
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13851
- **AI 摘要**: 该文章讨论了一种仅使用文本语义表示进行遥感场景分类的新方法，涉及文本生成和文本嵌入模型。
- **原始摘要**: arXiv:2611.13851v1 Announce Type: new Abstract: Remote sensing scene classification (RSSC) is traditionally formulated as a vision-centric problem, where inference relies on rich visual representation...

### 13. Interleaving anatomical inspection and diagnostic reasoning for explainable radiology report generation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14018
- **AI 摘要**: 本文介绍了一种名为ARIVE的框架，用于生成解释性放射学报告，该框架结合了解剖学检查和诊断推理。
- **原始摘要**: arXiv:2611.14018v1 Announce Type: new Abstract: Automated radiology report generation can draft clinically plausible reports, yet the pathway from visual evidence to reported findings remains opaque,...

### 14. Looking One Step Ahead: An Anticipation-guided Agent for Object State Readout in Videos
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14113
- **AI 摘要**: 该文章讨论了一种名为LASER的引导式对象状态读取代理，它利用可能的下一步变化来确定当前需要检查的属性。文章提出了一种新的方法来提高视觉描述的详细程度。
- **原始摘要**: arXiv:2611.14113v1 Announce Type: new Abstract: Understanding the progress of an activity requires tracking how the objects involved change over time. Object state readout provides this information by...

### 15. C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language Inference
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14469
- **AI 摘要**: 文章讨论了C$^2$-Routing方法，该方法通过结合裁剪和压缩来减少视觉语言模型的计算负担，以提高VQA的效率。
- **原始摘要**: arXiv:2611.14469v1 Announce Type: new Abstract: Visual Question Answering (VQA) imposes substantial computational overhead on vision-language models (VLMs), motivating model-agnostic input reduction m...

### 16. EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.12934
- **AI 摘要**: 该文章介绍了一种新的基准测试EarthRecord，用于评估多模态代理在处理四十年的卫星图像数据以进行可靠的土地变化分析方面的能力。
- **原始摘要**: arXiv:2611.12934v1 Announce Type: cross Abstract: While multimodal agents now carry out complex data analysis with tools, their ability to turn decades of satellite imagery into reliable land-change a...

### 17. Action-Guided Reachability for Deterministic World Models of Vision-Based Systems
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2512.08991
- **AI 摘要**: 该文章讨论了用于视觉系统的确定性世界模型和基于动作引导的分区验证技术，以解决闭环行为验证的挑战。
- **原始摘要**: arXiv:2512.08991v4 Announce Type: replace Abstract: End-to-end vision-based controllers map raw camera images directly to control actions, yet verifying their closed-loop behavior remains challenging:...

### 18. With Tools or Because of Tools? Tracing Capability Gains in Multimodal Agents
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.02357
- **AI 摘要**: 文章讨论了工具辅助的多模态代理在理解和推理任务上的表现，指出仅凭工具调用记录不足以证明代理学会了使用工具，工具辅助并未带来显著的性能提升。
- **原始摘要**: arXiv:2606.02357v3 Announce Type: replace Abstract: Tool-augmented multimodal agents show strong benchmark gains, often taken as evidence that agents have learned to use tools. We argue that this inte...

### 19. How Many Demonstrations Does a VLA Need? On the Sample Efficiency of VLA Finetuning
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.09964
- **AI 摘要**: 该文章讨论了预训练的视觉语言行动模型在不同演示数据量下的适应效率，涉及多个模型和四个LIBERO套件。
- **原始摘要**: arXiv:2611.09964v2 Announce Type: replace Abstract: Pretrained vision language action (VLA) models show strong zero-shot performance but they are rarely deployed directly and are often first post-trai...

### 20. Learning Where to Trust: Reliability-Guided Expert Routing and Velocity Gating for 3D Deformable Registration
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2610.36672
- **AI 摘要**: 本文提出了一种新的3D变形注册方法ReliMorph，通过结合局部匹配可靠性与空间上下文选择和变形更新强度，以解决学习驱动的变形注册中局部匹配可靠性不足的问题。
- **原始摘要**: arXiv:2610.36672v2 Announce Type: replace-cross Abstract: Deformable image registration relies on accurate anatomical correspondences. However, explicitly coupling local matching reliability with spat...

### 21. How Faster Inference Gives Cybersecurity Companies an EdgeJuly 22, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: uly 22, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/ai-inference-cybersecurity
- **AI 摘要**: 文章讨论了更快的推理如何为网络安全公司带来竞争优势。

### 22. How We Built Our Knowledge BaseJuly 15, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: uly 15, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/how-we-built-our-knowledge-base
- **AI 摘要**: 文章摘要：文章讨论了如何构建知识库，未涉及AI模型、芯片、编译器等技术，也未涉及具体行业落地的产品或解决方案。

### 23. Figma - MultiAgentsApril 16, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ril 16, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/figma-multiagents
- **AI 摘要**: 文章摘要未提供，无法生成总结。

### 24. Lessons learned from building multi-agent workflowsApril 16, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ril 16, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/lessons-learned-from-building-multi-agent-workflows
- **AI 摘要**: 文章讨论了构建多代理工作流的经验教训，关键词包括multi-agent workflows。这与Harness工程相关。

### 25. How AlphaSense Uses Fast Inference to Make Agentic Research InteractiveSeptember 30, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 30, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/how-alphasense-uses-fast-inference-to-make-agentic-research-interactive
- **AI 摘要**: 文章讨论了AlphaSense如何使用快速推理来使交互式研究更加便捷。

### 26. Why Cyber Defense Needs Faster InferenceSeptember 24, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 24, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/why-cyber-defense-needs-faster-inference
- **AI 摘要**: 文章讨论了网络安全领域需要更快的推理速度，但并未提及具体技术或应用。

### 27. Disaggregated Inference From The Ground UpOctober 01, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 01, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/disaggregated-inference-from-the-ground-up
- **AI 摘要**: 本文讨论了从基础层面实现的分布式推理技术。

### 28. ExomeBench: A Benchmark for Clinical Variant Interpretation in Exome RegionsFebruary 23, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 23, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/exomebench
- **AI 摘要**: 本文介绍了一个用于外显子区域临床变异解释的基准ExomeBench。

### 29. SELD: Detecting Silent Evidence Loss in Context Compression beyond the Answer
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.12903
- **AI 摘要**: 文章讨论了语言模型在处理长输入时，压缩上下文可能导致关键证据被删除的问题，并提出了一种无需训练和标签的方法来检测这种沉默证据损失。
- **原始摘要**: arXiv:2611.12903v1 Announce Type: new Abstract: Context compression is now routine for language models with long inputs, but a compressed context is useful only if it keeps the evidence for the answer...

### 30. Mapping Instructors' Attitudes Towards Cheating with AI: An Exploratory Analysis Using Forum Analysis
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13366
- **AI 摘要**: 该文章讨论了大学教授关于使用大型语言模型进行学术作弊的态度，通过分析Reddit论坛上的201万条帖子来理解教授们对学术诚信的看法。
- **原始摘要**: arXiv:2611.13366v1 Announce Type: new Abstract: In teaching and learning environments, cheating and the violation of academic integrity have always been one of the challenges, involving different leve...

### 31. Synapse-Control: Making Agent Experience Actionable with Lightweight Runtime Control
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13615
- **AI 摘要**: 本文介绍了一种名为Synapse-Control的系统，它通过轻量级控制平面来选择并决定何时将建议发送给执行任务的大模型，以提高复杂任务的可靠性。
- **原始摘要**: arXiv:2611.13615v1 Announce Type: new Abstract: Large language model agents reuse execution experience to improve reliability on complex tool-based tasks. Systems such as Sentry call large models to g...

### 32. OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13675
- **AI 摘要**: 文章讨论了OpticalRAG框架，该框架通过视觉编码器将文档转换为图像，然后使用冻结的视觉编码器进行编码，并将检索到的视觉标记转换为最少的16个注入标记，以提高文本生成的效率。该框架解决了大型语言模型在文本预算上的瓶颈问题。
- **原始摘要**: arXiv:2611.13675v1 Announce Type: new Abstract: Retrieval-augmented generation (RAG) is bottlenecked by the token budget of large language models: feeding long documents into the context window is exp...

### 33. LLM Validation Makes Minimal-Pair Benchmarks Easier for Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13788
- **AI 摘要**: 文章讨论了使用LLM验证最小对基准，发现LLM验证的效果不如单个人类评判员。
- **原始摘要**: arXiv:2611.13788v1 Announce Type: new Abstract: Minimal-pair benchmarks are only as good as their labels, and LLMs are an obvious substitute for costly human validation. We test it on BLiMP (English)...

### 34. PolyRoute: A Twelve-Language and Code-Mixed Benchmark for Typed-Decision Routing, with Baselines and a Leaderboard
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13843
- **AI 摘要**: 本文发布了一种名为PolyRoute的多语言和代码混合基准测试，包含12种语言和9种书写系统的消息，以及独立模型和TF-IDF与逻辑回归的性能评估。
- **原始摘要**: arXiv:2611.13843v1 Announce Type: new Abstract: Typed-decision encoders answer a question about a text in one forward pass, but their behaviour outside English is rarely measured on a fixed yardstick....

### 35. Program-Aided Patchable Skill Evolution
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14019
- **AI 摘要**: 本文提出了一种新的技能进化方法PASE，通过将技能与可执行程序关联，使其更容易维护和进化。
- **原始摘要**: arXiv:2611.14019v1 Announce Type: new Abstract: Agent skills have emerged as an effective means of enabling LLM agents to solve complex, interactive tasks by encoding reusable knowledge without modify...

### 36. Using LLM Agents to Evaluate Prosocial Interventions on Social Media Platforms
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.12922
- **AI 摘要**: 该文章讨论了使用大型语言模型（LLM）代理来评估社交媒体平台上的善行干预措施，通过模拟实验来减少人类实验的成本。
- **原始摘要**: arXiv:2611.12922v1 Announce Type: cross Abstract: Social media platforms are a primary source of information for many users. Although research explores various interventions to promote prosocial conte...

### 37. Repository-Context-Guided Image Understanding for Agentic Software Development
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13026
- **AI 摘要**: 该文章讨论了如何通过增强编码代理来改进使用UI截图的场景，这些截图通常包含在错误报告中。文章提出了一种方法，即在代理需要修改的代码库中生成清晰的截图，以提供清晰的用户界面视觉证据。
- **原始摘要**: arXiv:2611.13026v1 Announce Type: cross Abstract: Coding agents increasingly receive UI screenshots as part of bug reports, yet degraded image quality - caused by low resolution, compression artifacts...

### 38. GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13028
- **AI 摘要**: 文章介绍了GTAGym环境和框架，用于评估和强化学习在GTA V任务上的应用。文章提到了一个包含103个在线任务和47个基于图像的射击任务的评估基准。
- **原始摘要**: arXiv:2611.13028v1 Announce Type: cross Abstract: AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA g...

### 39. ASPIRE: An Agentic System-Identification Platform for Iterative Reasoning and Exploration
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13114
- **AI 摘要**: 本文介绍了一种名为ASPIRE的系统识别平台，它使用大型语言模型来选择和执行非线性系统识别方法。ASPIRE能够从测量数据中构建封闭形式的静态或动态模型，并且可以验证形式化的物理要求。
- **原始摘要**: arXiv:2611.13114v1 Announce Type: cross Abstract: System identification requires expert decisions on the identification method, incorporation of prior physical knowledge, and model validation. We prop...

### 40. Activation-Guided Graph Retrieval for Cognitive Memory Reconstruction in Language Model Systems
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13127
- **AI 摘要**: 文章讨论了一种新的语言模型系统架构，该架构通过激活条件下的记忆可用性来增强检索增强语言模型。
- **原始摘要**: arXiv:2611.13127v1 Announce Type: cross Abstract: Retrieval-augmented language model systems generally select context by query-conditioned relevance. We argue that long-lived AI systems require a seco...

### 41. Towards Reliable VLM Judges: State-Conditional Invariance and Presentation-Aware Diagnostics
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13596
- **AI 摘要**: 该文章讨论了视觉语言模型在多模态和具身任务中的可靠性问题，并提出了一种新的可靠性原则State-Conditional Invariance（SCI），用于评估模型在不同呈现条件下的稳定性。
- **原始摘要**: arXiv:2611.13596v1 Announce Type: cross Abstract: Vision-language models (VLMs) are increasingly used as automated judges for multimodal and embodied tasks, yet aggregate accuracy or consistency alone...

### 42. AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14333
- **AI 摘要**: 该文章讨论了在公共平台上，用户对两个固定版本的大语言模型进行盲选时，对两个模型都评价为“不好”的投票比例在增加，这表明用户在选择时变得更加挑剔。
- **原始摘要**: arXiv:2611.14333v1 Announce Type: cross Abstract: Users often complain that AI assistants such as ChatGPT are getting worse. Some versions do change, but human evaluation leaves a second possibility u...

### 43. EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14356
- **AI 摘要**: 文章讨论了如何通过EngineAgent系统自动化在移动设备上的大型语言模型（LLM）模型启用，通过分离可重用的引擎和硬件知识与模型特定实现，解决了模型在不同层面上的依赖关系和硬件后端的问题。
- **原始摘要**: arXiv:2611.14356v1 Announce Type: cross Abstract: Rapidly evolving LLM architectures and heterogeneous mobile hardware make supporting new models in on-device inference engines a recurring and costly...

### 44. FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14477
- **AI 摘要**: 该文章讨论了一种名为FERN的方法，用于改进文本到SQL的系统。FERN使用冻结的检索器和学习的排名器来提高表召回率。
- **原始摘要**: arXiv:2611.14477v1 Announce Type: cross Abstract: Text-to-SQL systems over large pooled catalogs must first retrieve the tables a question needs. We compare against the published table recall of RASL,...

### 45. Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14493
- **AI 摘要**: 该文章讨论了三种评估框架在企业数据分析代理中的稳定性、风险检测和未知风险发现方面的比较分析。
- **原始摘要**: arXiv:2611.14493v1 Announce Type: cross Abstract: Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-too...

### 46. StakeBench: Evaluating Language Understanding Grounded in Market Commitment
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.26074
- **AI 摘要**: 该文章介绍了一种新的金融NLP基准测试框架StakeBench，它基于市场承诺来评估语言理解能力。
- **原始摘要**: arXiv:2605.26074v2 Announce Type: replace Abstract: Existing financial NLP benchmarks often rely on labels supplied by outside observers, measuring how language is perceived rather than what speakers...

### 47. Hearsay or Fact? How Framing and Elicitation Shape LLM Probability Updates
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2610.27745
- **AI 摘要**: 该文章讨论了语言模型概率更新在不同框架下的测试情况，涉及多种模型和配置。
- **原始摘要**: arXiv:2610.27745v3 Announce Type: replace Abstract: We measure LLM probability updates on $\delta$-SNLI premise-hypothesis pairs across the Multi-Candidate Verbalization (MCV) family. Separate calls e...

### 48. CulturalCrosswords: A Multilingual Benchmark of Answer Constraints and Grid Completion
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.10044
- **AI 摘要**: 文章讨论了CulturalCrosswords项目，这是一个多语言文化谜题基准测试，用于评估大型语言模型在解决特定社区知识相关的文化谜题时的表现。文章提到了不同版本的谜题设置对模型性能的影响。
- **原始摘要**: arXiv:2611.10044v2 Announce Type: replace Abstract: When several answers fit a riddle, exact-match scoring can penalise a valid response. CulturalCrosswords tests how answer constraints affect large l...

### 49. AnyMo: Geometry-Aware Setup-Agnostic Modeling of Human Motion in the Wild
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.22715
- **AI 摘要**: 文章介绍了一种名为AnyMo的框架，用于在不受设备设置影响的情况下建模人类在野外的运动。该框架使用物理基础的IMU模拟来生成多样且合理的合成信号。
- **原始摘要**: arXiv:2605.22715v3 Announce Type: replace-cross Abstract: As wearable and mobile devices become increasingly embedded in daily life, they offer a practical way to continuously sense human motion in th...

### 50. Beyond Third-Person Audits: Situated Interaction Auditing for User-Centered LLM Bias Research
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.12247
- **AI 摘要**: 该文章讨论了大型语言模型偏见研究中的第三方审计方法存在的问题，并提出了一种新的第一人称审计方法。
- **原始摘要**: arXiv:2606.12247v2 Announce Type: replace-cross Abstract: Research on bias in large language models (LLMs) has predominantly focused on third-person audits, which study how models represent or evaluat...

### 51. A Factorial Ablation of a Speech-to-SFT Pipeline: Differential Effects on Data Quality and Downstream Transfer
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.20394
- **AI 摘要**: 该文章讨论了在生产级的语音到监督微调数据管道中，不同阶段的改进对下游多选择问答质量的影响。文章使用韩国医疗和金融会议录音生成QA形式的微调数据，并进行了多模型评估。
- **原始摘要**: arXiv:2608.20394v2 Announce Type: replace-cross Abstract: Industry pipelines that turn speech into supervised fine-tuning (SFT) data via multi-stage refinement are increasingly adopted but, to our kno...

### 52. SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2610.36991
- **AI 摘要**: 文章讨论了SpectRAG框架，该框架通过结合混合候选种子、加权块图构建、基于图的扩展、谱相关性传播和基于令牌的上下文选择来改进检索增强生成（RAG）系统。
- **原始摘要**: arXiv:2610.36991v4 Announce Type: replace-cross Abstract: Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation o...

### 53. Machine Hearing: Can Audio LLMs Generalize Beyond Human Auditory Perception?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.10693
- **AI 摘要**: 文章讨论了多模态语言模型在感知物理世界方面的进展，特别是如何扩展人类听觉范围以感知人类听不到的声音。文章引入了机器听觉基准（MHB），涵盖13个任务和7个领域，涉及从10^-5到10^6 Hz的采样率，从10^1到10^6样本长度的序列长度，以及单通道和多通道输入。
- **原始摘要**: arXiv:2611.10693v2 Announce Type: replace-cross Abstract: Multimodal LLMs have made remarkable progress in perceiving the physical world, while their perceptual scope remains largely human-centric, fo...

### 54. FinCutBench: A Continually Updated Benchmark for Measuring the Temporal Boundaries of LLM Financial Knowledge
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.11588
- **AI 摘要**: 文章讨论了FinCutBench基准测试，用于评估模型在金融市场知识上的时间边界。涉及金融知识的测试问题覆盖了中文和美国市场的多个信息类别。
- **原始摘要**: arXiv:2611.11588v2 Announce Type: replace-cross Abstract: In financial backtesting and other point-in-time tasks, external inputs can be restricted by date, but model parameters may retain financial f...

### 55. Building World Models from Intrinsic Motivation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13113
- **AI 摘要**: 文章讨论了如何通过内在动机构建世界模型，涉及了多种内在动机的整合，旨在理解哪些内在收集的经验能够构建出可重用的模型。
- **原始摘要**: arXiv:2611.13113v1 Announce Type: new Abstract: In the absence of extrinsic rewards or task supervision, human behavior is guided by intrinsic motivation---neural signals that drive curiosity, creativ...

### 56. Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13161
- **AI 摘要**: 该文章讨论了一种基于语言引导的多智能体强化学习框架，用于协作机器人中的搜索与救援任务。
- **原始摘要**: arXiv:2611.13161v1 Announce Type: new Abstract: Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazar...

### 57. Darmok: Championship Cryptic Crossword Solving via Constraint Tightening and Resilient Orchestration
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13557
- **AI 摘要**: 文章介绍了名为Darmok的系统，该系统在英国密特克（cryptic crossword）比赛中达到了超人类的表现，能够快速且准确地解决所有比赛谜题。
- **原始摘要**: arXiv:2611.13557v1 Announce Type: new Abstract: We present Darmok, the first automated system to reach superhuman performance on British cryptic crosswords. Unlike American-style crosswords, cryptic c...

### 58. Obscured Wildfire Flame Detection by Spatio-temporal Analysis of Smoke Patterns Using Frame-wise Transformers
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14074
- **AI 摘要**: 本文提出了一种使用帧级变换器进行烟雾模式时空分析的新方法，用于检测可见和被遮挡的火。
- **原始摘要**: arXiv:2611.14074v1 Announce Type: cross Abstract: In this paper, we propose a new paradigm in wildfire management for detecting both visible and obscured fire using Deep Learning (DL). The essence of...

### 59. Model-Free Runtime Measurement of Task-Relevant Information
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14111
- **AI 摘要**: 该文章讨论了一种新的模型自由架构，用于评估信息获取过程是否符合任务需求。
- **原始摘要**: arXiv:2611.14111v1 Announce Type: cross Abstract: Autonomous systems increasingly monitor physical kinematics, environmental states and task completion outcomes. While existing work provides methods t...

### 60. Achieving Robust Channel Estimation Neural Networks on Doppler effects by Designed Training Data
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14267
- **AI 摘要**: 本文研究了在快速通道变化和高德拉夫偏移的无线通信系统中，神经网络进行信道估计的能力。提出了生成合成训练数据的设计标准。
- **原始摘要**: arXiv:2611.14267v1 Announce Type: cross Abstract: Channel estimation is crucial in wireless communication systems. Many existing works train and test their models using the same or similar channel. Ho...

### 61. Differentiable Learning of Lifted Action Schemas for Classical Planning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.13282
- **AI 摘要**: 文章讨论了使用神经网络架构学习从完全观测状态到未观测动作参数的行动模式，这是学习规划领域从序列图像和动作标签中学习的一个简化步骤。
- **原始摘要**: arXiv:2605.13282v4 Announce Type: replace Abstract: Classical planners can effectively solve very large deterministic MDPs represented in STRIPS or PDDL where states are sets of atoms over objects and...

### 62. GraphToolbox: A Configurable Framework for Controlled Benchmarking of Graph Neural Network Forecasting
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.24609
- **AI 摘要**: 本文介绍了一种名为GraphToolbox的框架，用于统一控制下的图神经网络（GNN）预测实验的各个阶段，包括数据驱动的图构建、PyTorch Geometric中大多数图卷积操作和递归图细胞的单一接口、在线专家聚合、预测解释和预测显著性测试。
- **原始摘要**: arXiv:2609.24609v2 Announce Type: replace-cross Abstract: Electricity forecasting often involves spatially related signals observed over regions, substations, and feeders, and Graph Neural Networks (G...

### 63. Which Successes Make Good References? Action-Sequence Alignment for Multi-Turn On-Policy Distillation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13135
- **AI 摘要**: 文章讨论了在多轮策略使用代理中的成功参考选择问题，提出了使用最长公共子序列进行行动序列对齐的方法来解决兼容性问题。
- **原始摘要**: arXiv:2611.13135v1 Announce Type: new Abstract: On-policy distillation (OPD) reduces train-inference distribution mismatch by supervising a student on its own trajectories. For multi-turn tool-use age...

### 64. Audited Gradients, Anchored Policies: Model-Based Reinforcement Learning for Efficient Flow Control
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13203
- **AI 摘要**: 该文章讨论了基于模型的强化学习在高效流控制中的应用，重点介绍了反馈控制器的设计成本以及使用可微分代理和中央有限差分估计进行审计的方法。
- **原始摘要**: arXiv:2611.13203v1 Announce Type: new Abstract: Feedback controllers for flows are expensive to design, since each candidate must be evaluated with a high-fidelity solver. Differentiable surrogates re...

### 65. Multifidelity Operator Inference for Non-intrusive Model Reduction under Data Scarcity
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13624
- **AI 摘要**: 文章讨论了在数据稀缺的情况下，如何使用Operator Inference方法进行非侵入式模型简化，以应对高精度数值模型的高昂成本问题。
- **原始摘要**: arXiv:2611.13624v1 Announce Type: new Abstract: Many-query analyses, in which a computational model is repeatedly evaluated, play an important role in uncertainty quantification and optimization for e...

### 66. Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14511
- **AI 摘要**: 本文介绍了一种用于蛋白质-配体结合预测的基准测试工具Pyrite及其两个基于LLM的排名代理PyriteReasoner和PyriteFeaturizer。
- **原始摘要**: arXiv:2611.14511v1 Announce Type: new Abstract: Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, b...

### 67. One-Sided Expert-Parallel All-to-All for Mixture-of-Experts Inference over NVLink
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13188
- **AI 摘要**: 该文章讨论了一种新的One-Sided EP All-to-All通信方法，用于NVLink域内的GPU之间，以加速Mixture-of-Experts的推理过程。
- **原始摘要**: arXiv:2611.13188v1 Announce Type: cross Abstract: Expert parallelism (EP) shards the experts of a Mixture-of-Experts (MoE) layer across GPUs, so every MoE layer requires two all-to-all communications,...

### 68. Simultaneous Near-Optimal Region Identification in Continuous Simulation Optimization: Minimax Complexity and Adaptive Sampling
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13489
- **AI 摘要**: 该文章讨论了连续模拟优化中近似最优区域的识别问题，涉及复杂度和适应性采样。
- **原始摘要**: arXiv:2611.13489v1 Announce Type: cross Abstract: Simulation optimization typically returns a single estimated optimal point. When decisions also depend on criteria evaluated independently of simulati...

### 69. Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13539
- **AI 摘要**: 文章讨论了如何利用推荐系统模型的特征不变量缩放法则来高效地进行A/B实验，以减少计算资源的消耗。
- **原始摘要**: arXiv:2611.13539v1 Announce Type: cross Abstract: Researchers and engineers improve recommendation systems by performing A/B experiments with new model architectures, optimization methods, and data fe...

### 70. Stylization as Geodesic Navigation on Diffusion Manifolds
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14097
- **AI 摘要**: 文章讨论了一种新的方法Stylus，用于面部风格转移，该方法将风格转移视为预训练扩散模型曲面流形上的导航。
- **原始摘要**: arXiv:2611.14097v1 Announce Type: cross Abstract: Facial stylization asks for a delicate transformation: the image should look unmistakably artistic, yet the person should remain unmistakably the same...

### 71. Safe Approximate Nonlinear Model Predictive Control Without Expert Demonstrations
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.24503
- **AI 摘要**: 该文章讨论了一种无需专家演示的近似非线性模型预测控制方法，通过神经网络进行参数共享，减少计算成本。
- **原始摘要**: arXiv:2603.24503v2 Announce Type: replace Abstract: Repeated online optimization makes nonlinear model predictive control (NMPC) computationally demanding for real-time applications. Neural approximat...

### 72. Is Online Linear Optimization Sufficient for Strategic Robustness?
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2602.12253
- **AI 摘要**: 文章讨论了在线线性优化算法是否足以满足投标算法的稳健性需求，主要结果表明，线性化子线性后悔是满足稳健性的充分条件。
- **原始摘要**: arXiv:2602.12253v2 Announce Type: replace-cross Abstract: We consider bidding in repeated Bayesian first-price auctions. Bidding algorithms that achieve optimal regret have been extensively studied, b...

### 73. How Much of Your VLA Is kNN
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13160
- **AI 摘要**: 文章讨论了VLA模型在LIBERO模拟基准测试中的表现，以及通过检索附近的演示来提高成功率的方法。
- **原始摘要**: arXiv:2611.13160v1 Announce Type: new Abstract: Vision-language-action (VLA) models now exceed 95% success on the LIBERO simulation benchmark, yet it remains unclear how much of this performance requi...

### 74. ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13482
- **AI 摘要**: 该文章讨论了一种新的方法ExRL，用于在线适应长动作片段的机器人政策，通过控制每个预测动作片段的执行长度来实现。
- **原始摘要**: arXiv:2611.13482v1 Announce Type: new Abstract: Predicting long action chunks, often spanning dozens of timesteps, has become a key ingredient in increasingly capable robot policies. In this paper, we...

### 75. Camera equalisation of an 11.5x drop in environmental illuminance: four imitation-learning policies on an SO-101 arm
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13810
- **AI 摘要**: 研究对比了四种模仿学习策略在环境光照降低11.5倍时对任务成功率的影响，光照条件对策略的敏感性无显著影响。
- **原始摘要**: arXiv:2611.13810v1 Announce Type: new Abstract: Real-robot benchmarks of learned visuomotor policies often record room illuminance as the lighting condition. We show that, on a typical low-cost rig, r...

### 76. LEASH: Stay Safe in Agentic Robotics
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14115
- **AI 摘要**: 文章讨论了使用大型语言模型控制机器人带来的安全风险，并提出了一种综合性的评估机器人安全性的基准测试RoboRisk。
- **原始摘要**: arXiv:2611.14115v1 Announce Type: new Abstract: Foundation models such as GPT and Claude have shown strong capabilities in spatial understanding and embodied intelligence. These advances make agentic...

### 77. One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14432
- **AI 摘要**: 该文章描述了在OmniGibson模拟器中解决2026年BEHAVIOR挑战赛100个长期任务的方法，使用了一个单一的视觉语言行动（VLA）模型，该模型在2025年的解决方案基础上进行了训练，提高了模型的性能。
- **原始摘要**: arXiv:2611.14432v1 Announce Type: new Abstract: We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leade...

### 78. Taxonomy-Agnostic Neurosymbolic Grounding of Robot Kinematics
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13850
- **AI 摘要**: 该文章讨论了如何使用神经符号框架将统一机器人描述格式（URDF）文件转换为具有语义上下文的OWL本体，以支持机器人任务分配的符号推理。
- **原始摘要**: arXiv:2611.13850v1 Announce Type: cross Abstract: While symbolic reasoning for task allocation requires grounding a robot's physical capabilities, standard Unified Robot Description Format (URDF) file...

### 79. From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14365
- **AI 摘要**: 文章讨论了预训练的视频扩散模型（VDMs）在世界行动模型（WAMs）中的应用，提出了一种新的信号注入方法，通过频率域编码来改善模型性能。
- **原始摘要**: arXiv:2611.14365v1 Announce Type: cross Abstract: Pretrained video diffusion models (VDMs) offer a powerful foundation for World Action Models (WAMs), which jointly predict robot actions and future ob...

### 80. Mass Scaling Laws for Energy-Optimal Horizontal Multirotor Flight
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.04748
- **AI 摘要**: 该文章讨论了多旋翼飞行器在质量变化时能量最优水平飞行行为与质量之间的关系，通过数值模拟和理论推导进行了验证。
- **原始摘要**: arXiv:2611.04748v2 Announce Type: replace Abstract: Multicopters are a type of aerial robot seeing extensive real-world applications but with range and endurance as critical bottlenecks. Optimization...

### 81. Effect of Temporal Resolution on Zero-Shot Semantic Understanding of Rapid Human Actions
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.00496
- **AI 摘要**: 该文章讨论了零样本理解快速人类动作的时序分辨率影响，使用空手道作为案例研究，提出了一种无需训练的管道。
- **原始摘要**: arXiv:2605.00496v3 Announce Type: replace-cross Abstract: Understanding human actions from visual observations is essential for human-robot interaction, particularly when semantic interpretation of un...

### 82. Agentic AI Meets Formal Verification in the Era of Agentic Hardware Development
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13705
- **AI 摘要**: 文章讨论了AI在硬件验证中的应用，包括在规格、证明构造和推理引擎三个层面的进展，以及AI驱动硬件开发中的RTL生成、调试和保真优化。
- **原始摘要**: arXiv:2611.13705v1 Announce Type: cross Abstract: As AI agents become increasingly capable of generating and optimizing hardware circuits, ensuring the correctness of AI-generated designs becomes more...

### 83. Toward Autonomous RTL and Synthesis Optimization: Benchmarking and Self-Improving Agents
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13713
- **AI 摘要**: 该文章讨论了在硬件设计优化中的自主RTL和合成优化方向，包括基于参考和开放式的RTL优化基准测试，以及通过多agent框架实现的RTL优化自动化。
- **原始摘要**: arXiv:2611.13713v1 Announce Type: cross Abstract: Recent advances in large language models (LLMs) and autonomous agents are creating new opportunities for hardware design optimization. This paper exam...

### 84. Scaling Shapley Energy Attribution to Large LLM Batches
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13802
- **AI 摘要**: 本文提出了一种名为StepSplit的方法，用于解决大型LLM批次请求中能量分配的问题，该方法通过观察每个推理步骤的能量消耗来计算公平的能量分配。
- **原始摘要**: arXiv:2611.13802v1 Announce Type: cross Abstract: LLM services have become essential infrastructure for applications such as chat assistants and coding agents. Service providers need to attribute reso...

### 85. Two-Sided Amortized Resource Analysis: Verifying Resource Lower Bounds via Ill-Typing
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.12925
- **AI 摘要**: 该文章讨论了一种结合自动摊余资源分析和Ramsay和Walpole的两面型系统的方法，用于验证函数程序的资源下界。
- **原始摘要**: arXiv:2611.12925v1 Announce Type: new Abstract: We present a two-sided type system with potential for verifying resource lower bounds of functional programs. Automatic amortized resource analysis (AAR...

### 86. Context Types: Bunched Modalities for Unifying Safety and Reachability
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.13471
- **AI 摘要**: 该文章讨论了一种新的类型系统，用于高阶函数程序，能够同时支持安全性和可达性属性，通过资源代数和捆绑模态来实现。
- **原始摘要**: arXiv:2611.13471v1 Announce Type: new Abstract: Most type systems are designed to verify safety properties: the judgement $e : \tau$ holds if $e$ may evaluate to any value contained in the denotation...

### 87. CFGKAT: A Complete Calculus for Non-Local Control Flow
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14201
- **AI 摘要**: 文章讨论了CFGKAT的扩展，这是一种改进的控制流图代数，添加了非局部控制流，并保持了高效的决策程序。文章解决了CFGKAT中非局部控制流和goto语句的语义带来的问题，提出了一个完整的等价性公理化。
- **原始摘要**: arXiv:2611.14201v1 Announce Type: new Abstract: CFGKAT is an extension of guarded Kleene Algebra with Tests (GKAT) that adds non-local control flow (e.g., break, goto) while maintaining an efficient d...

### 88. Efficient Conversion of Algorithms to Linear Programs
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.12896
- **AI 摘要**: 文章讨论了LP编译器优化方法，旨在生成可由现有求解器处理的紧凑LP模型。
- **原始摘要**: arXiv:2611.12896v1 Announce Type: cross Abstract: The expressiveness of Linear Programming (LP) has motivated research on an LP compiler that generates polynomial-size LPs for polynomial-time solvable...

### 89. Secure Information Flow in Quantum Programs
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14147
- **AI 摘要**: 该文章讨论了量子程序中的信息流安全问题，提出了两种信息流安全的定义，并证明了它们等价。文章还开发了一种基于量子Hoare逻辑的证明框架来验证量子程序的信息流安全。
- **原始摘要**: arXiv:2611.14147v1 Announce Type: cross Abstract: Information-flow security aims to prevent the leakage of confidential information through program execution. This problem becomes fundamentally subtle...

### 90. Performance Portability Explained: Insights from accelerating ICON microphysics
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2611.14204
- **AI 摘要**: 该文章讨论了不同高性能计算（HPC）系统对微物理核（来自ICON气候模型）的优化需求，提出了衡量框架表达性的方法以评估不同框架的性能。
- **原始摘要**: arXiv:2611.14204v1 Announce Type: cross Abstract: Scientific computing is under increasing pressure to adapt to HPC hardware that is shaped by AI workloads. In these modern ecosystems, extracting reas...

### 91. ICYMI: The Kimi Playground: Your faster way to iterate and test
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://platform.kimi.ai/blog/posts/ICYMI_The_Kimi_Playground
- **AI 摘要**: 摘要介绍了一款名为Kimi的工具，声称可以加快迭代和测试的速度。

### 92. Welcoming Tom Sanocki as VP of EngineeringTom joins the 1X team with a remarkable track record of building and scaling software organizations that have reached millions of people.JUN 25 '261X
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.1x.tech/discover/tom-sanocki-vp-engineering
- **AI 摘要**: Tom Sanocki加入1X团队担任工程副总裁，拥有丰富的软件组织建设与扩展经验。

### 93. Vayavya Labs and Tenstorrent Partner to Accelerate RISC-V Hardware and Software Development Through Virtual Platform ModelingVayavya Labs and Tenstorrent are delivering SystemC virtual platforms for Tenstorrent’s security and system management IP using the TvastaaVP platform.Read more
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://tenstorrent.com/newsroom/newsroom/vayavya-labs-and-tenstorrent-partner-to-accelerate-hardware-and-software-development
- **AI 摘要**: Vayavya Labs与Tenstorrent合作通过虚拟平台建模加速RISC-V硬件和软件开发。

### 94. 2024-08-20燧原科技万卡集群点亮，助力庆阳打造“东数西算”标杆示范案例2024年8月20日，甘肃省庆阳市——昨日在2024“数盾”生态大会上举办了“燧原科技国产万卡集群点亮仪式”，甘肃省委常委、常务副省长程晓波、庆阳市委副书记、市长周继军等领导出席了大会。周继军在发言中表示，两年多来，庆阳紧抓“东数西算”国家战略机遇，持续在平台搭建、产业协同、服务保障等方面加力突破，推动数字企业生态实现从无到有、从有到优的转变，被国家发改委和数据局评价为在八大枢纽节点中起点最高、增了解更多
- **来源**: Enflame (燧原科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.enflame-tech.com/news/news/2024-08-20
- **AI 摘要**: 甘肃省庆阳市举办燧原科技国产万卡集群点亮仪式，庆祝‘东数西算’国家战略实施，庆阳市在数字企业生态建设方面取得显著进展。

### 95. Validating GPU Platforms with Runtime AI Inventory via the NVIDIA DSX AI Factory
- **来源**: NVIDIA Technical Blog (TIER1)
- **发布日期**: 2026-11-11T17:00:00Z (今天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://developer.nvidia.com/blog/validating-gpu-platforms-with-runtime-ai-inventory-via-the-nvidia-dsx-ai-factory/
- **AI 摘要**: 本文讨论了使用NVIDIA Dynamo、Kubeflow或Slurm部署和扩展AI工作负载时，需要超越平台的可见性。
- **原始摘要**: As teams deploy and scale AI workloads using NVIDIA Dynamo, Kubeflow, or Slurm, tracking what actually runs requires visibility beyond the platform......

### 96. DeepSeek V4.1 Flash vs GPT-6 Astra: Four Real Builds, Full Cost and Time Breakdown
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-09-16
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://deepseek.ai/blog/deepseek-v41-flash-vs-gpt6-astra-four-builds
- **AI 摘要**: 该文章对比了两个模型在不同应用场景下的成本和时间消耗，属于AI工程实践和评估的范畴。
- **原始摘要**: An independent creator gave both models the same four builds — an RTS replica, a 3D scroll website, a booking app and a Blender animation. DeepSeek came in ~6x cheaper on API spend; Astra was ~3x fast...

### 97. DeepSeek Opens ~150 Engineering Roles — and Not One AI Research Role
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-09-08
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://deepseek.ai/blog/deepseek-hiring-150-engineers-systems-shift
- **AI 摘要**: 该文章提到DeepSeek在招聘中不设置AI研究职位，而是专注于服务器端开发和弹性计算，暗示AI研究正逐渐从实验室转移到生产环境。
- **原始摘要**: Server-side development and agent elastic computing, zero research positions. Why the moat is moving from the lab to the serving stack, and what it means if you build on the API.

### 98. DeepSeek Opens ~150 Engineering Roles — and Not One AI Research Role
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-09-08
- **类型**: research
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://deepseek.ai/blog/deepseek-hiring-150-engineers-systems-shift
- **AI 摘要**: 文章提到DeepSeek在招聘中不设置AI研究职位，强调将研究重点转移到生产堆栈，暗示研究与生产之间的转变。
- **原始摘要**: Server-side development and agent elastic computing, zero research positions. Why the moat is moving from the lab to the serving stack, and what it means if you build on the API.

### 99. DeepSeek V4 Complete: Flash-Vision, Pro GA, and the New API Economics
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-08-23
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://deepseek.ai/blog/deepseek-v4-rollout-flash-vision-pricing-harness-2026-guide
- **AI 摘要**: DeepSeek发布V4版本，包含Flash-Vision和Pro GA功能，并推出新的高峰时段API定价策略。
- **原始摘要**: DeepSeek completes the V4 rollout with the release of V4-Flash-Vision-Exp and V4-Pro GA, alongside a new peak-hour API pricing strategy and viral open-source infrastructure tools.

### 100. DeepSeek V4 Complete: Flash-Vision, Pro GA, and the New API Economics
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-08-23
- **类型**: research
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://deepseek.ai/blog/deepseek-v4-rollout-flash-vision-pricing-harness-2026-guide
- **AI 摘要**: DeepSeek发布V4版本，包括Flash-Vision、Pro GA和新的API定价策略，同时提供开源基础设施工具。
- **原始摘要**: DeepSeek completes the V4 rollout with the release of V4-Flash-Vision-Exp and V4-Pro GA, alongside a new peak-hour API pricing strategy and viral open-source infrastructure tools.

## 🏷️  具身智能

**78 篇文章**

### 1. Plurai wants to help AI agents work better using the same approach that helped get self-driving cars to roads
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 14:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://techcrunch.com/2026/11/11/plurai-wants-to-help-ai-agents-work-better-using-the-same-approach-that-helped-get-self-driving-cars-to-roads/
- **AI 摘要**: Plurai公司希望通过模拟数据和自驾车技术的模拟评估方法来提高AI代理的性能。该公司希望利用合成数据来准备模型处理困难的边缘情况。
- **原始摘要**: Like the end-to-end models trained to drive cars, AI agents are probabilistic systems operating in unpredictable environments.

### 2. Israel’s Rafael unveils new, larger cruise missile dubbed Super Ice
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 08:00:00 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://breakingdefense.com/2026/11/israels-rafael-unveils-new-larger-cruise-missile-dubbed-super-ice/
- **AI 摘要**: 以色列国防军公司Rafael展示了名为Super Ice的新型大型巡航导弹，该导弹的重量可达1000磅，可以用于空、陆、海三地发射。Super Ice导弹具有打击坚固目标的能力，包括地堡、弹道导弹发射站和大型军舰。Rafael公司称其为世界上最好的巡航导弹之一，适用于远程打击高价值目标，如防空系统。
- **原始摘要**: Super Ice is comparable in size to the US-made Tomahawk missile....

### 3. DroneSegEdit: Adapting Pretrained Generative Editors for UAV Segmentation with Language-Grounded Verification
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13890
- **AI 摘要**: 本文介绍了一种新的方法DroneSegEdit，用于解决无人机图像分割中的掩码渲染与目标选择之间的差距问题。
- **原始摘要**: arXiv:2611.13890v1 Announce Type: new Abstract: Recent work has shown that pretrained image generators can support diverse visual tasks. Yet directly applying them to language-guided unmanned aerial v...

### 4. 3A-VLA: Abstraction-Aligned Action Learning for Vision-Language Agents in 3D Game Worlds
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: medium
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2602.02212
- **AI 摘要**: 文章讨论了如何通过引入3A-VLA框架来解决视觉语言行动模型在3D游戏世界中的局限性，该框架通过意图和环境抽象来指导行动学习，而不是简单的模式匹配。
- **原始摘要**: arXiv:2602.02212v2 Announce Type: replace Abstract: Despite advances in vision-language-action (VLA) models, they remain limited in highly dynamic game settings such as 3D open worlds and competitive...

### 5. Embodied Science Agents: Making Embodied Experimental Design Learnable
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.12958
- **AI 摘要**: 文章讨论了如何使自驾车实验室成为实现自主科学发现的关键，但现有实验室在结合计算推理和物理实验时存在矛盾。文章提出了解决这一矛盾的方法，即在认知学习、实验学习和具身学习三个方面嵌入学习能力。
- **原始摘要**: arXiv:2611.12958v1 Announce Type: new Abstract: Recent advances in large models have accelerated AI for Science toward agentic science, where AI agents autonomously conduct scientific discovery. Reali...

### 6. Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14262
- **AI 摘要**: 本文介绍了一种新的SNN架构——Community Recurrent SNNs（CoRe SNNs），用于强化学习。这种架构将网络划分为固定角色的社区，以实现模块化和递归。
- **原始摘要**: arXiv:2611.14262v1 Announce Type: new Abstract: Biological neural circuits are both modular and recurrent, with dense communities sparsely linked to one another. Spiking neural networks (SNNs) for rei...

### 7. Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2607.00033
- **AI 摘要**: 该文章讨论了使用人类演示来指导机器人的精细操作，通过接触力矩空间来实现这一目标。文章提出了一种名为CHORD的框架，用于通过强化学习进行复杂的物体操作。
- **原始摘要**: arXiv:2607.00033v3 Announce Type: replace-cross Abstract: Dexterous robot manipulation can benefit from the abundance of human demonstrations, but transferring such demonstrations to robot policies re...

### 8. Maze Runner: Autonomous Maze Navigation with Line-Based Localization and Control Barrier Functions
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.12949
- **AI 摘要**: 本文介绍了一种用于自主迷宫导航的系统Maze Runner，它结合了线性定位和控制边界函数，适用于模拟环境中的Husarion ROSbot XL机器人。
- **原始摘要**: arXiv:2611.12949v1 Announce Type: new Abstract: Maze navigation requires localization from sparse, repetitive geometry, planning through narrow corridors, and control that stays safe when the estimate...

### 9. CAFE: Closed-Loop Autonomous Task Formulation and Execution without Instance-Specific Instructions
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.12983
- **AI 摘要**: 文章讨论了一种名为CAFE的方法，用于在没有特定实例目标或动作序列的情况下，通过规则引导的触发器语言模型（Trigger-LLM）、草稿、完成和审计来制定和执行任务。文章在12个AI2-THOR场景中进行了评估。
- **原始摘要**: arXiv:2611.12983v1 Announce Type: new Abstract: Scene-driven robot autonomy requires selecting tasks from observations as well as executing them. We study scene-driven task formulation and execution u...

### 10. RoboACE: Adversarial Co-Evolution for Robot Self-Improvement
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13034
- **AI 摘要**: 该文章讨论了RoboACE框架，通过联合进化课程和执行框架来改进机器人技能，以适应不断变化的能力需求。
- **原始摘要**: arXiv:2611.13034v1 Announce Type: new Abstract: Robot agents can improve reusable skills, planning procedures, and recovery strategies from execution feedback, yet a fixed practice source leaves the s...

### 11. Robo-MLT: Dual-System Robotic Manipulation for Long-Horizon Medical Laboratory Tasks
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13039
- **AI 摘要**: 文章讨论了Robo-MLT框架，该框架结合了明确的工作流监控和学习生成的动作，用于医疗实验室自动化中的复杂任务。
- **原始摘要**: arXiv:2611.13039v1 Announce Type: new Abstract: Reliable medical laboratory automation requires robots to complete entire workflows in protocol order while handling changes during execution. A robot m...

### 12. Ground Reaction Force-Aware Model Predictive Control for Underactuated Upright Physical Assistance
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13204
- **AI 摘要**: 本文提出了一种基于地面反作用力和中心压力的模型预测控制（GRF-MPC）框架，用于下肢康复机器人提供支撑力。
- **原始摘要**: arXiv:2611.13204v1 Announce Type: new Abstract: Many rehabilitation robots execute prescribed motions using reactive tracking controllers that do not explicitly incorporate the user's instantaneous hu...

### 13. Latent Barrier Steering: Hierarchical Safety for Generative Planning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13227
- **AI 摘要**: 本文介绍了一种名为Latent Barrier Steering（LBS）的框架，用于解决基于流匹配的生成规划中的安全问题。LBS通过协调干预将行为选择与路径认证分离，提高了路径校正器的裕量。
- **原始摘要**: arXiv:2611.13227v1 Announce Type: new Abstract: We introduce Latent Barrier Steering (LBS), a hierarchical semantic-to-path framework for safe flow-matching-based generative planning. Existing control...

### 14. Incorporating World Models in Decision Making for Next Best View Selection in Active Sensing
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13229
- **AI 摘要**: 该文章讨论了如何使用预训练的世界模型来指导机器人在主动感知中的最佳视图选择，通过学习传感器返回适配器来适应部署条件。
- **原始摘要**: arXiv:2611.13229v1 Announce Type: new Abstract: Efficient robotic 3D reconstruction requires selecting views that contribute new surface measurements with few physical captures. Pretrained world model...

### 15. Curie's Jarvis: Autonomous Robotic Chemistry Experiments from Printed Protocols
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13251
- **AI 摘要**: 本文介绍了一种名为Curie's Jarvis的系统，它能够让机器人手臂在没有固定位置和标记的普通实验台上执行化学实验，该系统通过读取打印指令的图片、通过多个摄像头识别容器标签来完成实验。
- **原始摘要**: arXiv:2611.13251v1 Announce Type: new Abstract: A person running a bench experiment works from a printed instruction sheet, tells identical containers apart by the labels written on them, and looks at...

### 16. Force-Closure Condition for Cooperative Multi-robot Pushing of Rectangular Objects
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13268
- **AI 摘要**: 该文章讨论了四面摩擦力为零的推力下，矩形物体的力闭合条件，该条件与物体的中心位置无关，用于验证接触配置并确定需要调整的接触对。
- **原始摘要**: arXiv:2611.13268v1 Announce Type: new Abstract: In cooperative object manipulation, the placement of pushing contacts determines whether force closure can be achieved and agents can generate arbitrary...

### 17. Does Haptic Connection to a Healthy Partner Improve Motor Learning in Chronic Stroke? A Pilot Study of Robot-Based Dyadic Training
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13307
- **AI 摘要**: 本文探讨了机器人触觉双人合作对慢性中风患者学习复杂追踪任务的影响，包括认知、运动和感觉评估。
- **原始摘要**: arXiv:2611.13307v1 Announce Type: new Abstract: Purpose: Robot-based haptic dyads, where two users exchange forces through robots, have been proposed for robot-assisted neurorehabilitation. This inter...

### 18. PneuGen: Task-Driven Agentic Co-Design of Soft Pneumatic Robots
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13344
- **AI 摘要**: 本文介绍了一种名为PneuGen的软体机器人设计框架，通过使用大型语言模型（LLM）代理来高效搜索软体机器人设计空间，以实现任务目标。
- **原始摘要**: arXiv:2611.13344v1 Announce Type: new Abstract: Task-driven design of soft robots requires the consideration of factors such as geometry, morphology, material properties, and actuation, resulting in a...

### 19. AHEADance: Anticipatory Humanoid Dance from Streaming Audio
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13370
- **AI 摘要**: 本文介绍了一种名为AHEADance的人形机器人舞蹈生成系统，该系统能够根据实时流音乐进行舞蹈动作生成。
- **原始摘要**: arXiv:2611.13370v1 Announce Type: new Abstract: A humanoid that dances to streamed music must commit each motion chunk before it has heard the music that chunk accompanies, and must continue from moti...

### 20. Rhythmic-Semantic Co-Speech Gestures for Emotional Dialogue in Robots
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13472
- **AI 摘要**: 该文章讨论了一种情感感知的节奏-语义同步手势系统，能够实时生成与文本和机器人内部情绪状态相关的语义手势和节奏手势。文章提出了一种基于情绪的节奏-语义手势生成任务，并训练了一个轻量级模型来预测手势的强度。
- **原始摘要**: arXiv:2611.13472v1 Announce Type: new Abstract: Co-speech gestures can increase engagement and improve speech understanding. Yet, most data-driven robot systems generate either rhythmic beat-like moti...

### 21. DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13499
- **AI 摘要**: 本文提出了一种新的深度表示学习方法DeRep，用于在杂乱环境中端到端的导航。该方法结合了局部鸟瞰视图可达性监督和深度重建。
- **原始摘要**: arXiv:2611.13499v1 Announce Type: new Abstract: End-to-end navigation in cluttered environments relies on compact visual representations to support collision avoidance and goal-directed motion. Existi...

### 22. GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13528
- **AI 摘要**: 文章讨论了GEMOR-GS算法，用于改进3D Gaussian Splatting SLAM中的地图，使其几何准确、全局优化并可重新进入，以提高机器人感知和决策的效果。
- **原始摘要**: arXiv:2611.13528v1 Announce Type: new Abstract: Photorealistic and metrically consistent world representations are a primary requirement for LiDAR--inertial--visual SLAM systems that serve robots over...

### 23. From Egocentric Human Video to Robot Manipulation in the Era of Embodied Intelligence
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13610
- **AI 摘要**: 文章讨论了从自传视频到机器人操作的学习方法，涉及四种学习范式：明确的本体转移、明确的动作和任务监督、自传视频表示预训练以及动作和动力学的隐式建模。
- **原始摘要**: arXiv:2611.13610v1 Announce Type: new Abstract: Egocentric human video (EHV) records close-range hand-object interaction (HOI) and the temporal structure of everyday activities, offering a potentially...

### 24. Ego Guidance: Enhancing Robot Policy Learning with Action-Free Human Egocentric Videos
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13685
- **AI 摘要**: 该文章讨论了如何利用人类自体视频来增强机器人政策学习，而无需动作监督。文章提出了一个名为Shared Prediction on Action and Representation (SPAR)的模型架构。
- **原始摘要**: arXiv:2611.13685v1 Announce Type: new Abstract: In this paper, we investigate how human egocentric videos can benefit robot policy learning without action supervision. Building on a pretrained VLM, we...

### 25. CIALLO: Learning Shared Intent Representations for Cross-Embodiment Manipulation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13732
- **AI 摘要**: 文章讨论了一种名为CIALLO的模型，该模型用于跨机器人控制接口的学习共享意图表示，以实现不同机器人之间的行为意图共享。
- **原始摘要**: arXiv:2611.13732v1 Announce Type: new Abstract: Robot demonstrations contain reusable manipulation knowledge, but transferring this knowledge across embodiments requires representations that bridge di...

### 26. From Depth to Safe Depth: Uncertainty-Aware Monocular Perception for Mobile Robot Navigation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13769
- **AI 摘要**: 该文章讨论了使用单目深度模型替代移动机器人上的深度传感器，提出了一种轻量级插件模块来生成安全深度，以提高导航性能。
- **原始摘要**: arXiv:2611.13769v1 Announce Type: new Abstract: Monocular depth foundation models make it tempting to replace depth sensors on mobile robots with a single RGB camera. We show that, used off the shelf,...

### 27. Softness is something you also need! Why compliance helps control: information metrics of a passive walker with compliant ankle
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13779
- **AI 摘要**: 文章讨论了智能机器人与自然界的动物和植物在适应性、灵活性和灵巧性方面的差距，以及如何通过采用生物观察的原则来设计人工代理，文章涉及信息度量和动态学之间的联系。
- **原始摘要**: arXiv:2611.13779v1 Announce Type: new Abstract: A great gap in adaptivity, flexibility, and dexterity still exists between intelligent robots, whether they are made of rigid or (partially) compliant c...

### 28. WAM is capable in BEHAVIOR-1K: the 2nd-place solution to the 2026 BEHAVIOR Challenge
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13818
- **AI 摘要**: 该文章介绍了在2026年行为挑战赛中获得第二名的解决方案，使用了增强的世界行动模型（WAM）和特定任务组和技能的LoRA适配器。
- **原始摘要**: arXiv:2611.13818v1 Announce Type: new Abstract: This work presents the 2nd-place solution (Team IF1001) to the 2026 BEHAVIOR Challenge, which evaluates mobile manipulation across 100 household tasks....

### 29. Game-Enhanced Embodied Learning with Event and Foresight Pretraining
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13819
- **AI 摘要**: 该文章讨论了通过游戏增强的 embodied 学习，结合了事件和预见性预训练，提高了机器人在多个游戏环境中的表现。
- **原始摘要**: arXiv:2611.13819v1 Announce Type: new Abstract: Human gameplay supplies paired observations, actions, and visual consequences that can supplement robot-policy training. We study event-and-foresight pr...

### 30. Learn-To-Propagate: Distributionally Robust Motion Planning for Nonlinear Uncertain Systems
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13863
- **AI 摘要**: 该文章讨论了一种新的学习到传播的分布鲁棒森林算法，用于解决未知初始状态和过程噪声分布的非线性不确定系统的运动规划问题。
- **原始摘要**: arXiv:2611.13863v1 Announce Type: new Abstract: Motion planning for stochastic systems aims to find a sequence of control inputs that drives a system to a goal set while avoiding unsafe states with hi...

### 31. ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric Loads
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13929
- **AI 摘要**: 本文提出了一种名为ReACT的方法，用于在不对称上半身负载下实现准确的运动跟踪。
- **原始摘要**: arXiv:2611.13929v1 Announce Type: new Abstract: In recent years, humanoid loco-manipulation has progressed to whole-body grasping, lifting, and transport. A basic requirement underlying these tasks is...

### 32. Optimization-Based Path Planning for Industrial Manipulators: Experimental Validation in Additive Manufacturing
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13983
- **AI 摘要**: 该文章讨论了基于优化的路径规划方法，用于工业机械臂在增材制造中的应用，并通过实验验证了其有效性。
- **原始摘要**: arXiv:2611.13983v1 Announce Type: new Abstract: Robotic additive manufacturing requires joint paths that reconcile robot feasibility with process-specific geometry. We develop an offline optimization-...

### 33. RedirectMimic: Local Motion Content Redaction for Humanoid Whole-Body Control
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14049
- **AI 摘要**: 本文介绍了一种名为RedirectMimic的方法，用于在人形机器人动作控制中移除特定动作，该方法通过分离观察者和训练目标来实现。
- **原始摘要**: arXiv:2611.14049v1 Announce Type: new Abstract: Humanoid motion interfaces should accommodate application-specific movement constraints while retaining useful reference behavior. Local content redacti...

### 34. A human-in-the-loop Control Paradigm for Construction Robotics: From VR-Guided Teleoperation to Semi-Autonomous Dual-Arm Operation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14062
- **AI 摘要**: 该文章讨论了一种结合虚拟现实指导的远程操作、半自主共享控制和基于规则的自主执行的人工智能控制框架，用于结构化施工任务。
- **原始摘要**: arXiv:2611.14062v1 Announce Type: new Abstract: Construction tasks in hazardous and unstructured environments require both human adaptability and robotic precision, yet existing approaches often treat...

### 35. DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14092
- **AI 摘要**: 该文章讨论了如何生成低成本的机器人演示数据，以便用于手眼协调的视觉语言动作学习。
- **原始摘要**: arXiv:2611.14092v1 Announce Type: new Abstract: We study how to generate diverse, physically executable robot demonstrations for dexterous vision-language-action (VLA) learning. Existing demonstration...

### 36. Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14257
- **AI 摘要**: 本文提出了一种名为Elastic-WAM的方法，用于优化机器人控制中的世界动作模型，该模型通过自适应地分配时空细化计算来减少视频去噪的计算开销。
- **原始摘要**: arXiv:2611.14257v1 Announce Type: new Abstract: World-Action Models improve robot control by predicting future visual dynamics, but iterative video denoising incurs substantial inference overhead. Rec...

### 37. From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14274
- **AI 摘要**: 文章讨论了在变形线性对象的抓取控制中，预测与决策实用性的区别，并介绍了Geometry-Pointer-Flow（GPF）政策。文章比较了真实参数、估计参数和学习交互历史表示在预测和执行控制中的表现。
- **原始摘要**: arXiv:2611.14274v1 Announce Type: new Abstract: A representation that accurately predicts a deformable object's response is not necessarily the one most useful for choosing manipulation actions. We st...

### 38. SIGMO: Sigmoid Gated Interaction-Aware Motion Planning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14414
- **AI 摘要**: 本文提出了一种新的运动规划方法SIGMO，用于解决复杂环境中的自动驾驶车辆导航问题。
- **原始摘要**: arXiv:2611.14414v1 Announce Type: new Abstract: Despite the widespread adoption of autonomous vehicle technologies, reliable navigation within cluttered environments remains arduous due to the necessi...

### 39. TanCRAFT: Context-Reasoned Anticipatory Feedback for Assembly Tasks
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14470
- **AI 摘要**: 本文介绍了一种名为TanCRAFT的系统，用于物理组装任务中的预测性辅助，通过场景状态跟踪、当前部分组装的推理、预测未来操作的移动以及在预测放置与目标不兼容时进行干预。
- **原始摘要**: arXiv:2611.14470v1 Announce Type: new Abstract: Preventing human error in physical assembly tasks requires assistance systems that can intervene before mistakes are made. This is especially challengin...

### 40. Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14488
- **AI 摘要**: 该文章讨论了记忆增强的视觉语言行动政策在计数任务中的问题，发现它们会将空闲时间误认为工作时间，影响了任务的成功率。
- **原始摘要**: arXiv:2611.14488v1 Announce Type: new Abstract: Memory-augmented vision-language-action (VLA) policies are meant to remember what happened. Many of them, however, fill memory by time: they sample fram...

### 41. One Trajectory, Two Requirements: Accuracy and Local Stability in Euler Sampling for Flow Matching Policies
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13311
- **AI 摘要**: 文章讨论了在Euler采样用于流匹配政策时，步长选择对精度和局部稳定性的影响。文章分析了在保持学习传输不变的情况下，即使步长选择不同，精度和局部稳定性要求也会不同。
- **原始摘要**: arXiv:2611.13311v1 Announce Type: cross Abstract: Flow matching robot policies commonly use a fixed Euler step count selected from offline accuracy sweeps. At inference time, however, each policy inpu...

### 42. A computational framework for understanding embodied plans
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13669
- **AI 摘要**: 该文章讨论了一种新的代理表示GenEA，能够理解和推理多步骤、长期的生物力学和物体交互的计划。
- **原始摘要**: arXiv:2611.13669v1 Announce Type: cross Abstract: Reasoning about people's plans and goals based on their actions is fundamental to human social interaction and essential for cooperative, embodied art...

### 43. Persistent Metric-Semantic Maritime Scene Memory from Open-Vocabulary 3D Scene Graphs
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.13903
- **AI 摘要**: 该文章讨论了如何将适用于室内外环境的3D场景图方法应用于海洋环境，但需要进行一些适应。
- **原始摘要**: arXiv:2611.13903v1 Announce Type: cross Abstract: Three-dimensional scene graphs (3DSGs) can provide robots with persistent metric-semantic representations for spatial reasoning, but the existing meth...

### 44. HiPFuse: Real-Time LiDAR Semantic Segmentation for Robotic Perception on Edge Devices
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14025
- **AI 摘要**: 该文章介绍了HiPFuse框架，用于边缘设备上的实时激光雷达语义分割，提高了性能和效率。
- **原始摘要**: arXiv:2611.14025v1 Announce Type: cross Abstract: Real-time robotic perception requires accurate LiDAR semantics under limited resources. Bird's-eye-view (BEV) aggregation is efficient but can mix dif...

### 45. Personalized Affective Perception via Continual Learning in Human-Agent Negotiation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.14247
- **AI 摘要**: 该文章讨论了通过持续学习和想象来适应面部表情识别的方法，以使智能代理能够个性化地理解和适应人类的非言语表达。
- **原始摘要**: arXiv:2611.14247v1 Announce Type: cross Abstract: Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their behavior accordingly. However, ge...

### 46. Learning Beyond Rigid Manipulation with Hybrid Soft-Rigid Robots
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2024年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2410.07787
- **AI 摘要**: 该文章讨论了结合刚性和柔性的机器人系统的学习能力，展示了其在传统任务中的表现。
- **原始摘要**: arXiv:2410.07787v4 Announce Type: replace Abstract: Rigid-soft robot hybrids promise to unite the precision and repeatability of rigid manipulators with the compliance and adaptability of soft structu...

### 47. Chasing Stability: Humanoid Running via Control Lyapunov Function Guided Reinforcement Learning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2509.19573
- **AI 摘要**: 该文章讨论了通过控制Lyapunov函数和强化学习相结合的方法来实现人形机器人跑步的稳定性控制，属于具身智能领域。
- **原始摘要**: arXiv:2509.19573v2 Announce Type: replace Abstract: Achieving highly dynamic behaviors on humanoid robots, such as running, requires controllers that are both robust and precise, and hence difficult t...

### 48. Self-supervised Physics-Informed Manipulation of Deformable Linear Objects with Non-negligible Dynamics
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2602.03623
- **AI 摘要**: 本文提出了一种结合精确变形物体模型的物理信息自监督学习框架SPiD，用于动态操纵可变形线性物体。
- **原始摘要**: arXiv:2602.03623v2 Announce Type: replace Abstract: We address dynamic manipulation of deformable linear objects by presenting SPiD, a physics-informed self-supervised learning framework that couples...

### 49. Pose Distance Fields for Humanoid Robots
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2602.04851
- **AI 摘要**: 该文章讨论了用于人形机器人的姿态距离场（PDF-HR），这是一种轻量级的先验知识，用于表示机器人的姿态分布。
- **原始摘要**: arXiv:2602.04851v2 Announce Type: replace Abstract: Pose and motion priors play a crucial role in humanoid robotics. Although such priors have been widely studied in human motion recovery (HMR) domain...

### 50. Quadruped Agile Locomotion: Sparsely Gated Mixture of Experts with Visual Input
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2604.19344
- **AI 摘要**: 该文章讨论了将稀疏门控混合专家架构应用于基于视觉的机器人运动控制，以提高敏捷性。
- **原始摘要**: arXiv:2604.19344v2 Announce Type: replace Abstract: Agile locomotion is important for quadruped robots in the real world. Recent approaches have demonstrated impressive capabilities including dynamic...

### 51. SSR: Scaling Surefooted and Symmetric Humanoid Traversal Toward the Open World
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2605.30770
- **AI 摘要**: 文章讨论了SSR框架，用于高效地基于自体视觉的人形机器人行走，该框架能够学习安全可靠的足部放置和自然的全身行为。
- **原始摘要**: arXiv:2605.30770v2 Announce Type: replace Abstract: Advancing humanoid traversal toward the open world is key to practical deployment in human environments, but remains challenging. The robot must use...

### 52. HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2606.31682
- **AI 摘要**: 本文介绍了一种名为HABIT的数据集，用于训练机器人在有人在场的环境中执行任务，该数据集包含超过10000个演示任务，涵盖了协作、共事和监督三种角色。
- **原始摘要**: arXiv:2606.31682v2 Announce Type: replace Abstract: Large-scale demonstration datasets have been central to recent progress in general-purpose robot policies. However, existing datasets are collected...

### 53. XS-VLA: Teaching Tiny Vision-Language-Action Models with Spatial Supervision and Demonstration Conditioning
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2607.04171
- **AI 摘要**: 本文介绍了一种名为XS-VLA的训练框架，用于训练紧凑的视觉语言行动模型，该框架结合了教师生成的空间标签和示范条件化动作学习。
- **原始摘要**: arXiv:2607.04171v5 Announce Type: replace Abstract: How can richer training supervision improve robot control while keeping the deployed policy compact? We present XS-VLA, a staged training framework...

### 54. Autonomous robotic bridging using distributed swarm control without inter-agent communication
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2609.01394
- **AI 摘要**: 该文章描述了一种无需GPS或RF通信的分布式群控技术，用于自主机器人在水下桥跨越，适用于军队的不规则河流穿越，提高乘员生存能力和减少后勤足迹。
- **原始摘要**: arXiv:2609.01394v2 Announce Type: replace Abstract: We describe SCARAB--Swarm-Capable Autonomous Robotic Aquatic Bridging. Using distributed swarm control and multi-model sensing of agents and docking...

### 55. OpenDexGrasp: Open-vocabulary Task-Oriented Dexterous Grasping
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2609.18117
- **AI 摘要**: 本文提出了一种新的框架OpenDexGrasp，用于生成能够执行任务的开放词汇 Dexterous 抓取，该框架结合了自动抓取合成和视觉语言注释的大规模语义和几何覆盖，以及通过人类远程操作和类别级转移获得的高质量的体外对齐。
- **原始摘要**: arXiv:2609.18117v4 Announce Type: replace Abstract: Dexterous grasp synthesis has advanced rapidly in generating stable and physically plausible hand poses, but real-world manipulation requires grasps...

### 56. Awomo-SimDataEngine: Agentic Simulation-ReadyWorld Generation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2610.02274
- **AI 摘要**: 本文介绍了一种名为Awomo-SimDataEngine的系统，该系统连接了资产和场景生成服务，用于机器人演示合成。
- **原始摘要**: arXiv:2610.02274v2 Announce Type: replace Abstract: Generating useful robot-training data requires more than visually plausiblescenes: objects must support interaction, placements must remain physical...

### 57. Evaluating Long-Horizon Robot Planning under Uncertainty
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2610.17326
- **AI 摘要**: 该文章讨论了家用机器人在不确定环境下的长期规划任务，涉及多个任务环境和初始记忆配置。文章评估了ReAct、VLM-TAMP和Tru-POMDP等规划器的表现。
- **原始摘要**: arXiv:2610.17326v2 Announce Type: replace Abstract: Household robots must successfully navigate im-perfect circumstances, both in their internal models and the external world. We introduce a benchmark...

### 58. SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年10月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2610.28480
- **AI 摘要**: 文章讨论了一种新的方法SuperMimic，它通过一个可微的世界模型来学习大规模人类动作数据，从而实现高效的人形机器人全身控制。
- **原始摘要**: arXiv:2610.28480v2 Announce Type: replace Abstract: Tracking large human-motion datasets has become the dominant route to general, expressive humanoid whole-body control, but scaling across many motio...

### 59. An Integrated Open-Source Stack for Vision-Based Autonomous Navigation of Wheeled Rovers
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.08100
- **AI 摘要**: 该文章介绍了一种基于视觉的自主导航堆栈，适用于轮式漫游者，包括目标箭头跟随、到达终端锥体和自主返回起点。
- **原始摘要**: arXiv:2611.08100v2 Announce Type: replace Abstract: Vision-based rover autonomy requires integrating perception, localization, planning and platform-specific control under limited sensing and computin...

### 60. Control-Aware Command Generation for Asynchronous Control and Action Inference with Vision-Based Policies towards Fast Execution
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.11089
- **AI 摘要**: 该文章讨论了基于视觉的控制策略在执行复杂任务时的执行速度问题，并提出了一种新的异步推理和控制框架来解决这一问题。
- **原始摘要**: arXiv:2611.11089v2 Announce Type: replace Abstract: Vision-based control policies, including vision-language-action models, have enabled robots to perform increasingly complex tasks. However, their ex...

### 61. DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.11166
- **AI 摘要**: 本文提出了一种新的框架DexForesight，用于学习机器人手的隐式空间预见，该框架通过将具有动力学感知的世界表示注入到精细操作策略的隐空间中来实现。
- **原始摘要**: arXiv:2611.11166v2 Announce Type: replace Abstract: Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand. Existing world-action models often acquir...

### 62. PA-SaR: Perception-Aware Learning, Control, and Coordination for Multi-Robot Search and Rescue
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.11648
- **AI 摘要**: 文章讨论了PA-SaR框架，用于协调多机器人搜索与救援任务，涉及感知、学习、控制和协调。
- **原始摘要**: arXiv:2611.11648v2 Announce Type: replace Abstract: Autonomous SaR requires robots to explore unknown or partially known environments, avoid hazards, coordinate team activities, and guide discovered v...

### 63. Fade to... Red? Scheduling Coloured Noise Exploration Supports Efficient Robot Learning with Reduced Movement Jerk
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.11868
- **AI 摘要**: 该文章讨论了在机器人学习中使用不同颜色噪声的效果，特别是红色噪声，发现其能减少动作的抖动。
- **原始摘要**: arXiv:2611.11868v2 Announce Type: replace Abstract: Exploration in deep reinforcement learning (RL) for continuous control is commonly driven by temporally uncorrelated Gaussian (white) action noise,...

### 64. OASIS: Optimization-Aware Subgoal Inference with Safety Constraints for Autonomous Mobile Robot Navigation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2611.11996
- **AI 摘要**: 该文章讨论了用于自主移动机器人导航的OASIS框架，该框架结合了优化结果来生成强化学习下的局部子目标，并在运动限制和几何碰撞避免约束下跟踪这些子目标。
- **原始摘要**: arXiv:2611.11996v2 Announce Type: replace Abstract: Navigation in dynamic environments requires mobile robots to make progress toward their goals while respecting motion limits and avoiding surroundin...

### 65. DiffeoMorph: Learning Distributed 3D Morphogenesis with Rotation-Invariant Spectral Shape Matching
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2512.17129
- **AI 摘要**: 文章讨论了一种新的框架DiffeoMorph，用于学习引导群体代理形成目标3D形状的形态发生协议。该框架使用SE(3)-不变的图神经网络进行代理的更新。
- **原始摘要**: arXiv:2512.17129v3 Announce Type: replace-cross Abstract: Biological systems can form complex three-dimensional structures through the collective behavior of agents that share a common update rule and...

### 66. Show, Don't Tell: Detecting Novel Objects by Watching Human Videos
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://arxiv.org/abs/2603.12751
- **AI 摘要**: 该文章讨论了一种无需复杂语言描述和昂贵的人工干预，仅通过人类演示自动创建的数据集训练专用物体检测器的方法，以识别新对象。
- **原始摘要**: arXiv:2603.12751v2 Announce Type: replace-cross Abstract: How can a robot quickly identify and recognize new objects shown to it during a human demonstration? Existing closed-set object detectors freq...

### 67. OpenClaw and OpenClaw API: The Complete Guide
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://platform.kimi.ai/blog/posts/what-is-openclaw
- **AI 摘要**: 本文为OpenClaw和OpenClaw API提供了全面指南。

### 68. Clawdbot in 2026: From Concept to OpenClaw Implementation
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://platform.kimi.ai/blog/posts/clawdbot-moltbot-openclaw-tutorial
- **AI 摘要**: 文章讨论了Clawdbot的概念从概念到OpenClaw实现的过程，涉及机器人和机械臂技术。

### 69. Kimi K2: Open Agentic Intelligence
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://platform.kimi.ai/blog/posts/k2-report
- **AI 摘要**: 文章标题为Kimi K2: Open Agentic Intelligence，摘要未提供具体信息，但标题暗示可能涉及开放的实体智能。

### 70. NEO’s Hands | An API to the Physical WorldWe’re excited to announce our breakthrough 25 Degree of Freedom (DOF), tendon-driven hands for the NEO humanoid platform– achieving near human-level dexterity, strength, safety, and reliability.JUL 09 '261X
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.1x.tech/discover/neos-hands
- **AI 摘要**: NEO发布25自由度的软体手，具有接近人类的灵活性、力量、安全性和可靠性。

### 71. 1X & NVIDIA Research CollaborationThe 1X AI Team and NVIDIA GEAR Lab collaborate on advancing AI in robotics, spending a week in employees homes teaching NEO Gamma to do the dishes.MAR 18 '251X
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.1x.tech/discover/1X-NVIDIA-Research-Collaboration
- **AI 摘要**: 1X与NVIDIA研究团队合作，一周内让NEO Gamma机器人在员工家中学习洗碗。

### 72. 1X Acquires Kind Humanoid1X and Kind Humanoid is Joining Forces to Build Humanoids Alongside HumansJAN 27 '251X
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.1x.tech/discover/1x-acquires-kind-humanoid
- **AI 摘要**: 1X公司收购Kind Humanoid，并与之合作开发人形机器人，与人类共同工作。

### 73. Podcast: 1X CEO, Bernt Børnich on the Venture Europe PodcastIn the latest episode of the Venture Europe Podcast, Bernt Børnich, CEO of 1X, sits down with host Calin Fabri to explore the evolving world of humanoid robotics.MAY 02 '241X
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.1x.tech/discover/1x-ceo-bernt-bornich-on-the-venture-europe-podcast
- **AI 摘要**: 1X CEO Bernt Børnich在Venture Europe Podcast中讨论了人形机器人领域的演变。

### 74. NEO Factory | Building Your NEOThe NEO Factory in Hayward, California is America’s first true vertically integrated high-volume humanoid robot factory.APR 30 '261X
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.1x.tech/discover/neo-factory
- **AI 摘要**: NEO工厂是美国首个真正的垂直整合高产量人形机器人工厂，位于加利福尼亚州海沃德。

### 75. The 1X World Model Lab | Est. 20261X Launches World Model Lab to Scale Humanoid Intelligence, Appoints Sam Sinha as Head of World Models and Founding ResearcherJUN 04 '261X
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.1x.tech/discover/1x-world-model-lab
- **AI 摘要**: 1X World Model Lab宣布成立，Sam Sinha担任世界模型负责人。

### 76. 2023-12-15UBTECH Robotics Collaborates with the University of Hong Kong for Joint Research on Human-like Visual Perception
- **来源**: UBTECH (优必选) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.ubtrobot.com/en/about/news/493495795167301
- **AI 摘要**: UBTECH Robotics与香港大学合作进行人类视觉感知的联合研究。

### 77. Kung Fu Meets SpringUnitree Spring Festival Gala Robots Present "Cyber Real Kung Fu" in the Year of the HorseLearn More >
- **来源**: Unitree (宇树科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://www.unitree.com/news/38
- **AI 摘要**: 文章内容与机器人表演有关，涉及Kung Fu和SpringUnitree机器人，但未提及具体技术细节或应用。

### 78. The First Disaggregated Inference Demo for AI Agents Is Live
- **来源**: SambaNova (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 具身智能
- **链接**: https://sambanova.ai/blog/first-disaggregated-inference-demo-for-ai-agents-live
- **AI 摘要**: 文章提到了首个解耦推理演示，这与AI代理相关。

## 🏷️  AI芯片

**48 篇文章**

### 1. With $720M round, Britain’s Fractile gets a leg up in the race for AI chips
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 19:34:55 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://techcrunch.com/2026/11/11/with-720m-round-britains-fractile-gets-a-leg-up-in-the-race-for-ai-chips/
- **AI 摘要**: 英国初创公司Fractile在人工智能芯片领域获得7.2亿美元融资，希望确保英国在这一关键领域拥有更大份额。Fractile将利用这笔资金开发更高效的AI芯片，并与Axelera、Etched和OLIX等公司竞争。
- **原始摘要**: Fractile has now become one of the top-funded players in the race for purpose-built AI chips.

### 2. SpaceX develops its own ‘Kessel’ rack-scale system featuring 72 Nvidia Rubin GPUs for data centers in space, report claims
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 15:03:08 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-develops-its-own-kessel-rack-scale-system-featuring-72-nvidia-rubin-gpus-for-data-centers-in-space-report-claims-replaces-conventional-nvlink-cable-assemblies-with-a-massive-84-layer-printed-circuit-board
- **AI 摘要**: SpaceX正在开发一种新的‘Kessel’系统，该系统使用72个Nvidia Rubicon GPU来替代传统的NVLink电缆连接器，采用了一块84层的印刷电路板。这表明SpaceX在太空数据中心领域取得了进展。
- **原始摘要**: SpaceX is reportedly developing a 'Kessel' rack-scale system design with 72 Nvidia Rubin GPUs that relies on a massive 84-layer PCB midplane.

### 3. Cognichip reveals how its new AI-assisted program can slash chip design times from months to days — automating labor-intensive tasks cuts design time down, Chief Product Officer explains
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 13:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://www.tomshardware.com/tech-industry/semiconductors/cognichip-reveals-how-its-new-ai-assisted-program-can-slash-chip-design-times-from-months-to-days-automating-labor-intensive-tasks-cuts-design-time-down-chief-product-officer-explains
- **AI 摘要**: Cognichip发布了一款新的AI辅助程序，能够将芯片设计时间从数月缩短到数天。首席产品官解释称，自动化繁重任务缩短了设计时间。
- **原始摘要**: Cognichip claims its AI can slash chip design time from months to days, only that that design must be very simplistic.

### 4. AMD shares how it can retain 95% of server performance with just half the DRAM, sidestepping memory shortages with MEXT
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 12:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI芯片
- **链接**: https://www.tomshardware.com/pc-components/cpus/amd-shares-how-it-can-retain-95-percent-of-server-performance-with-just-half-the-dram-sidestepping-memory-shortages-with-mext-tech-powers-over-100-servers-already-running-with-plans-to-expand-to-2-000-servers-in-2027
- **AI 摘要**: AMD分享了如何仅使用一半的DRAM就能保留95%的服务器性能，并通过MEXT技术避免内存短缺。目前已有100多台服务器运行，计划在2027年扩展到2000台服务器。
- **原始摘要**: Following AMD’s acquisition of MEXT earlier this year, the company has revealed its own IT infrastructure is using the technology to run servers at 50% DRAM capacity while achieving 95% of the perform...

### 5. Optimized E-Beam Evaporation Reduces Metal-Semiconductor Contact Degradation (RWTH Aachen)
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Wed, 11 Nov 2026 23:00:41 +0000 (今天)
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://semiengineering.com/optimized-e-beam-evaporation-reduces-metal-semiconductor-contact-degradation-rwth-aachen/
- **AI 摘要**: 该文章讨论了RWTH Aachen大学的研究成果，通过优化电子束蒸发技术来减少金属-半导体接触的降解。研究结果表明，优化后的电子束蒸发技术可以减少费米能级的钉扎，从而提高n型硅的肖特基二极管的势垒。
- **原始摘要**: Researchers at RWTH Aachen University published “Mitigating the degradation of metal–semiconductor contacts with optimized electron beam evaporation.” Abstract “An optimized electron beam evaporation...

### 6. UCIe Connectivity for 2.5D and 3D Multi-Die Designs
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Wed, 11 Nov 2026 08:01:52 +0000 (今天)
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://semiengineering.com/ucie-connectivity-for-2-5d-and-3d-multi-die-designs/
- **AI 摘要**: 本文探讨了UCIe标准在2.5D和3D多芯片设计中的应用差异及工程考量。2.5D设计中UCIe链路通过封装通道传输，影响PHY和封装设计；而3D设计中，由于短垂直连接和精细键合，数据带宽可通过连接密度提升，减少高速序列化、均衡化和通道训练的需求。
- **原始摘要**: The differences and engineering considerations behind choosing and implementing UCIe connectivity for advanced multi-die designs. The post UCIe Connectivity for 2.5D and 3D Multi-Die Designs appeared...

### 7. Ultrafast Frontier Inference: Cerebras Deep Dive at Hot Chips 2026August 25, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ust 25, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026
- **AI 摘要**: 文章摘要：关于Cerebras在Hot Chips 2026上的Ultrafast Frontier Inference技术的深入探讨。

### 8. August 18, 2026Introducing Cerebras CS-4:  The Fastest AI Just Got FasterRead blog post
- **来源**: Cerebras (TIER1)
- **发布日期**: ust 18, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/introducing-cerebras-cs-4
- **AI 摘要**: 文章介绍了Cerebras CS-4，这是目前最快的AI芯片。

### 9. NewsJune 30, 2026Frontier Inference ClustersWe co-design chips, racks, software, and manufacturing methods so frontier models can run with best-in-class throughput, latency, cost, and power efficiency for both prefill and decode workloads.

Earlier this year our A0 silicon came back from TSMC N4P, and today we are busy validating our first rack-scale product with customers to fulfill $1B in demand.

We’re a team of 400+ engineers from NVIDIA, Google TPUs, Broadcom, SK Hynix, TSMC, and more. We’ve raised $800M across four unannounced financings, including a strategic investment from VentureTech Alliance. We’re excited to deepen our partnership with the world’s leading semiconductor manufacturer.
- **来源**: Etched (TIER1)
- **发布日期**: une 30, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://etched.com/progress/progress/frontier-inference-clusters
- **AI 摘要**: 本文介绍了团队在Frontier Inference Clusters方面的进展，包括芯片设计、软件和制造方法的协同设计，以及与客户合作验证首个大规模产品，以满足高达10亿美元的市场需求。团队成员来自NVIDIA、Google TPUs、Broadcom等公司。

### 10. Which is faster: Kimi K2.6 on Cerebras or Gemini Flash?June 05, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 05, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/which-is-faster-gemini-3-5-flash-or-kimi-k2-6-on-cerebras
- **AI 摘要**: 对比Kimi K2.6和Gemini Flash的性能，文章讨论了在Cerebras上的运行速度。

### 11. Cerebras and Upstage Bring Ultra-Fast AI to South KoreaJuly 10, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: uly 10, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/cerebras-and-upstage-bring-ultra-fast-ai-to-korea
- **AI 摘要**: 文章提到了Cerebras和Upstage在韩国推出超快AI技术。

### 12. Fast inference is going mainstream — the Cerebras ecosystem is scaling accessApril 28, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ril 28, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/ecosystem
- **AI 摘要**: 文章讨论了Cerebras生态系统如何扩大其主流快速推理访问。

### 13. Partner Spotlight: Armis + Cerebras Enable Teams Build and Secure Software FasterMarch 27, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: rch 27, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/partner-spotlight-armis
- **AI 摘要**: 文章讨论了Armis与Cerebras的合作，旨在帮助团队更快地构建和保护软件。

### 14. The GPU Is Being Split in HalfMarch 26, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: rch 26, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/disaggregated-inference
- **AI 摘要**: 文章摘要：2026年3月26日，一篇关于GPU分割的文章摘要。

### 15. Cerebras is coming to AWSMarch 13, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: rch 13, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/cerebras-is-coming-to-aws
- **AI 摘要**: 文章摘要：Cerebras将入驻AWS，讨论其在AWS中的应用。

### 16. StackAI × Cerebras: enabling the fastest inference for enterprise AI agentsJanuary 28, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 28, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/stackai-cerebras-enabling-the-fastest-inference-for-enterprise-ai-agents
- **AI 摘要**: StackAI与Cerebras合作，加速企业AI代理的推理速度。

### 17. OpenAI Partners with Cerebras to Bring High-Speed Inference to the MainstreamJanuary 14, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 14, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.cerebras.ai/blog/openai-partners-with-cerebras-to-bring-high-speed-inference-to-the-mainstream
- **AI 摘要**: OpenAI与Cerebras合作将高速推理带入主流市场

### 18. ‘Safeguarding against system failures and cyber threats’: SK hynix builds trust in physical AI memory
- **来源**: SK hynix Newsroom (TIER1)
- **发布日期**: Wed, 11 Nov 2026 01:36:17 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://news.skhynix.com/en/iec-61508-certification-2026-5/
- **AI 摘要**: 三星电子忆存发布ISO/SAE 21434网络安全流程证书，提升物理AI内存的安全性。
- **原始摘要**: ▲ SK hynix ISO/SAE 21434 Cybersecurity Process Certificate

### 19. ‘Safeguarding against system failures and cyber threats’: SK hynix builds trust in physical AI memory
- **来源**: SK hynix Newsroom (TIER1)
- **发布日期**: Wed, 11 Nov 2026 01:34:45 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://news.skhynix.com/en/iec-61508-certification-2026-4/
- **AI 摘要**: 三星Hynix通过ISO/SAE 21434网络安全流程证书，加强物理AI内存系统的信任。
- **原始摘要**: ▲ SK hynix ISO/SAE 21434 Cybersecurity Process Certificate

### 20. ‘Safeguarding against system failures and cyber threats’: SK hynix builds trust in physical AI memory
- **来源**: SK hynix Newsroom (TIER1)
- **发布日期**: Wed, 11 Nov 2026 01:29:07 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://news.skhynix.com/en/iec-61508-certification-2026-3/
- **AI 摘要**: 三星电子忆阻器公司(SK hynix)开发了物理AI内存，以提高系统的安全性和可靠性。
- **原始摘要**: ▲ IEC 61508 Safety Integrity Levels (SIL) and operating modes. LPDDR5X supports SIL 3 and continuous mode.

### 21. ‘Safeguarding against system failures and cyber threats’: SK hynix builds trust in physical AI memory
- **来源**: SK hynix Newsroom (TIER1)
- **发布日期**: Wed, 11 Nov 2026 01:28:04 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://news.skhynix.com/en/iec-61508-certification-2026-2/
- **AI 摘要**: 三星电子忆朕公司获得了IEC 61508产品和过程证书，以确保物理AI内存的安全和可靠性。
- **原始摘要**: ▲ SK hynix IEC 61508 Product and Process Certificates

### 22. ‘Safeguarding against system failures and cyber threats’: SK hynix builds trust in physical AI memory
- **来源**: SK hynix Newsroom (TIER1)
- **发布日期**: Wed, 11 Nov 2026 01:25:43 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://news.skhynix.com/en/iec-61508-certification-2026-1/
- **AI 摘要**: 三星电子忆亿公司（SK hynix）致力于构建物理AI内存的信任，通过防范系统故障和网络安全威胁。

### 23. FAME-QP: A GPU-Accelerated Quadratic-Programming Solver for Real-Time Model Predictive Control
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.13766
- **AI 摘要**: 本文介绍了一种新的GPU加速的QP求解器FAME-QP，用于线性模型预测控制中的稠密二次规划问题，通过设备校准和问题特定的定时选择执行配置，同时保持解决方案精度和控制性能。
- **原始摘要**: arXiv:2611.13766v1 Announce Type: new Abstract: We present FAME-QP, a GPU-accelerated solver for dense quadratic programs arising in linear model predictive control. FAME-QP combines constraint-depend...

### 24. Priority-Aware Deficit Round Robin for AXI4 Bandwidth Fairness in ASAP-7nm Process
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.12979
- **AI 摘要**: 该文章讨论了在AXI4架构中实现带宽公平性的QoS-aware deficit round robin架构，对比了round robin和QoS优先级带宽分配策略。
- **原始摘要**: arXiv:2611.12979v1 Announce Type: new Abstract: Modern systems-on-chip place real-time clients, processor cores and bulk data engines on the same AXI4 interconnect, where they contend for shared slave...

### 25. An Open Implementation Flow for the Xilinx Spartan-3E and Spartan-6 that Runs in the Browser, Checked Byte for Byte Against ISE
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.13008
- **AI 摘要**: 作者描述了一种开放的实现流程，用于Xilinx Spartan-3E和Spartan-6设备，这些设备仅支持已停售的ISE 14.7。流程可以在浏览器或Node.js中运行。
- **原始摘要**: arXiv:2611.13008v1 Announce Type: new Abstract: The author describes an open implementation flow, from HDL to a programmable bitstream, for the Xilinx Spartan-3E (XC3S100E to XC3S1200E) and Spartan-6...

### 26. Tri-Stack-PIM: A Heterogeneous Multi-Die 3D-Integrated Processing-in-Memory Architecture for Efficient LLM Inference
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.13644
- **AI 摘要**: 本文提出了一种新的三重堆叠处理在内存（PIM）架构，用于高效的语言模型推理。
- **原始摘要**: arXiv:2611.13644v1 Announce Type: new Abstract: Large language model (LLM) inference during autoregressive decoding is fundamentally memory-bandwidth-bound. Existing three-dimensional (3D) stacked pro...

### 27. Exploiting What NVIDIA Profilers Hide: Fast and Accurate Analytical GPU Performance Modeling
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.13762
- **AI 摘要**: 该文章讨论了如何改进GPU性能分析模型，以更快地预测不同硬件配置下的性能表现。
- **原始摘要**: arXiv:2611.13762v1 Announce Type: new Abstract: GPUs have become essential to many fields, including AI and scientific computing. As GPUs grow more complex, the design space of their hardware configur...

### 28. Uncovering the Memory Hierarchy of Modern NVIDIA GPUs for Accurate Simulation
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.13860
- **AI 摘要**: 本文介绍了一种新的方法来重构现代NVIDIA GPU的内存层次结构，以提高其准确性的方法。
- **原始摘要**: arXiv:2611.13860v1 Announce Type: new Abstract: Emerging artificial intelligence workloads, particularly Large Language Models (LLMs), place unprecedented demands on GPU memory systems. Consequently,...

### 29. SFU-Sim: Bit-Exact Reverse Engineering of NVIDIA MUFU and Validation of PTX Paths
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.13879
- **AI 摘要**: 本文介绍了一种通过反向工程构建NVIDIA MUFU指令的精确模型的方法，并展示了如何分析PTX到SASS的编译路径，以恢复段结构、等效系数表和有限宽度算术。
- **原始摘要**: arXiv:2611.13879v1 Announce Type: new Abstract: Reproducing the numerical behavior of a GPU requires predicting the exact output of special function instructions. Vendor documents give only the functi...

### 30. SkipLane: Write-Once, Conflict-Free Accumulation for Zero-Skipping CNN Engines on FPGAs
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.14495
- **AI 摘要**: 该文章讨论了在FPGA上用于CNN加速器的SkipLane技术，通过写一次的方式解决零激活的跳跃问题和合并问题，显著提高性能。
- **原始摘要**: arXiv:2611.14495v1 Announce Type: new Abstract: Skipping zero activations saves multiplications in CNN accelerators, but it complicates accumulation: the products in a compressed input window belong t...

### 31. SPMW: A Grid-Based Programming Model for Scalable Accelerator Design
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.12944
- **AI 摘要**: 本文介绍了一种新的编程模型SPMW，用于设计可扩展的加速器，该模型保持了网格的规则性，并结合了行为硬件描述语言（HLS）和结构实时逻辑（RTL）生成。
- **原始摘要**: arXiv:2611.12944v1 Announce Type: cross Abstract: Modern accelerators specialize recurring computation and replicate it across regular hardware structures to achieve high performance. Sustaining this...

### 32. Machine-learning decoders for fusion-based quantum computing in real time
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.13630
- **AI 摘要**: 该文章讨论了用于融合量子计算的机器学习解码器，旨在提高错误率和吞吐量。
- **原始摘要**: arXiv:2611.13630v1 Announce Type: cross Abstract: Fault-tolerant quantum computation requires decoders that combine accuracy, throughput, low latency, and scalability to large numbers of physical qubi...

### 33. fRAC: Remote Accelerator Calls on Hostless FPGAs
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2025年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2504.04404
- **AI 摘要**: 文章讨论了远程加速器调用（RAC）的概念，该概念旨在通过硬件在FPGA上实现网络到加速器的接口，从而减少分布式应用中网络调用的延迟。
- **原始摘要**: arXiv:2504.04404v3 Announce Type: replace-cross Abstract: Hardware accelerators are essential for meeting microsecond-scale demands in distributed applications, but invoking them over the network rema...

### 34. Parametric Proof-Carrying Compilation for Quantum Error-Correction
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://arxiv.org/abs/2611.12985
- **AI 摘要**: 本文提出了一种名为PC-QEC的量子纠错编译框架，该框架能够证明四种量子纠错编码（标准、标志、Shor和Knill）在指定错误和读出合同下的所有合法编码距离。
- **原始摘要**: arXiv:2611.12985v1 Announce Type: new Abstract: We present PC-QEC, a proof-carrying compilation framework for quantum error correction parameterized by both code distance and syndrome-extraction schem...

### 35. ‘Safeguarding against system failures and cyber threats’: SK hynix builds trust in physical AI memory
- **来源**: SK hynix Newsroom (TIER1)
- **发布日期**: Tue, 10 Nov 2026 23:59:29 +0000 (昨天)
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://news.skhynix.com/en/iec-61508-certification-2026/
- **AI 摘要**: 三星Hynix获得IEC 61508 SIL 3工业功能安全认证和ISO/SAE 21434网络安全管理系统认证，扩展其国际认证。
- **原始摘要**: ▪ SK hynix secures IEC 61508 SIL 3 industrial functional safety certification for LPDDR5X and ISO/SAE 21434-based Cybersecurity Management System (CSMS) certification product lifecycle process. ▪ Buil...

### 36. Physical Design2
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://tenstorrent.com/newsroom/newsroom/tags/physical-design
- **AI 摘要**: 文章标题为Physical Design2，但摘要中未提供足够的信息来判断其主题类别。根据标题，可能与硬件设计相关，但无法确定。

### 37. AI chip startup d-Matrix shifts into high gear as business expands
- **来源**: D-Matrix (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.d-matrix.ai/announcements/ai-chip-startup-d-matrix-shifts-into-high-gear-as-business-expands/
- **AI 摘要**: 文章摘要：AI芯片初创公司d-Matrix业务扩展，文章主要讨论其在AI芯片领域的进展。

### 38. d-Matrix Adopts NVIDIA NVLink Fusion Rackscale Infrastructure for Ultra-Low Latency AI Inference
- **来源**: D-Matrix (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.d-matrix.ai/announcements/d-matrix-rackscale-nvidia/
- **AI 摘要**: d-Matrix采用NVIDIA NVLink Fusion大规模基础设施，实现超低延迟AI推理。

### 39. Chip startup d-Matrix to use Nvidia chip-linking tech in AI servers
- **来源**: D-Matrix (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.d-matrix.ai/announcements/chip-startup-d-matrix-to-use-nvidia-chip-linking-tech-in-ai-servers/
- **AI 摘要**: d-Matrix公司将使用Nvidia的芯片互联技术在AI服务器中应用

### 40. 2026-09-11越过山丘，天地俊秀——燧原科技（688801.SH）正式登陆科创板​2026年9月11日，中国上海——上海燧原科技股份有限公司（股票简称：燧原科技；股票代码：688801）正式在上海证券交易所科创板鸣锣上市。从2018年3月开启创业征程，到2026年9月叩开资本市场大门，燧原科技用八年半时间，成长为国产算力崛起浪潮中的标杆企业之一，完成了企业资本化规模化发展的关键蜕变。燧原科技董事长赵立东：在产业发展机遇与国家政策导向的双重驱动下，国产AI芯片赛道正迎来黄金发展期了解更多
- **来源**: Enflame (燧原科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.enflame-tech.com/news/news/2026-09-11
- **AI 摘要**: 燧原科技在2026年9月11日成功登陆科创板，成为国产算力崛起浪潮中的标杆企业之一。

### 41. 2026-09-10壁仞科技与上海大学共建“集成电路智能芯片联合实验室”
- **来源**: Biren (壁仞科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.birentech.com/news//news/ushlilpreh47xrx99u9oljkh/
- **AI 摘要**: 壁仞科技与上海大学共建‘集成电路智能芯片联合实验室’，推动智能芯片领域研究。

### 42. 2026-09-07一图读懂壁仞科技2026年半年度报告
- **来源**: Biren (壁仞科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.birentech.com/news//news/gix30jnrvumo1yi3qi24qhkk/
- **AI 摘要**: 摘要内容为：2026-09-07一图读懂壁仞科技2026年半年度报告。

### 43. 2026-09-07壁仞科技斩获中国专利银奖，自研GPU技术再获国家级认可
- **来源**: Biren (壁仞科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.birentech.com/news//news/nc9aodl93m390l96hsdcxolr/
- **AI 摘要**: 壁仞科技自研GPU技术在2026年获得中国专利银奖，这是国家级的认可。

### 44. 2026-09-07共探训推融通新路径！壁仞科技 x 龙蜥社区 x PyTorch生态共建MeetUp圆满收官
- **来源**: Biren (壁仞科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://www.birentech.com/news//news/z7mnt0q87wmvhpfshy0fumoi/
- **AI 摘要**: 壁仞科技、龙蜥社区与PyTorch生态在MeetUp上圆满收官，共探训推融通新路径。

### 45. DeepSeek's Reported 160,000-Chip Huawei Cluster in Inner Mongolia
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-09-08
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://deepseek.ai/blog/deepseek-huawei-ascend-160000-chip-cluster
- **AI 摘要**: 文章提到华为在内蒙古的一个约1GW的站点中部署了至少160,000个Ascend 950DT加速器，用于推理而非训练。这与AI芯片相关。
- **原始摘要**: At least 160,000 Ascend 950DT accelerators at a ~1 GW site in Ulanqab — earmarked for inference, not training. What is reported, what is confirmed, and what it means for API capacity.

### 46. DeepSeek's Reported 160,000-Chip Huawei Cluster in Inner Mongolia
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-09-08
- **类型**: research
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://deepseek.ai/blog/deepseek-huawei-ascend-160000-chip-cluster
- **AI 摘要**: 文章提到华为在内蒙古的一个约1GW的站点中部署了至少160,000个Ascend 950DT加速器，用于推理而非训练。这与AI芯片相关。
- **原始摘要**: At least 160,000 Ascend 950DT accelerators at a ~1 GW site in Ulanqab — earmarked for inference, not training. What is reported, what is confirmed, and what it means for API capacity.

### 47. DeepSeek’s $74B Pivot: 160k Huawei Chips & V4-Vision Open Weights
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-09-06
- **类型**: blog
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://deepseek.ai/blog/deepseek-huawei-cluster-v4-vision-open-weights-2026-update
- **AI 摘要**: DeepSeek发布16万片华为芯片集群，并开放V4-Vision-Exp权重，表明向硬件独立和多模态AI的重大转变。
- **原始摘要**: DeepSeek unveils a 160,000-chip Huawei cluster and releases DeepSeek-V4-Flash-Vision-Exp open weights, signaling a major move toward hardware independence and multimodal AI.

### 48. DeepSeek’s $74B Pivot: 160k Huawei Chips & V4-Vision Open Weights
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-09-06
- **类型**: research
- **优先级**: high
- **分类**: AI芯片
- **链接**: https://deepseek.ai/blog/deepseek-huawei-cluster-v4-vision-open-weights-2026-update
- **AI 摘要**: DeepSeek发布160,000片华为芯片集群，并开放V4-Vision-Exp权重，表明向硬件独立性和多模态AI的重大转变。
- **原始摘要**: DeepSeek unveils a 160,000-chip Huawei cluster and releases DeepSeek-V4-Flash-Vision-Exp open weights, signaling a major move toward hardware independence and multimodal AI.

## 🏷️  编译器

**2 篇文章**

### 1. Retargetable Compilation for Tensor Kernels via a Unified Layout Abstraction
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2611.13741
- **AI 摘要**: 本文介绍了一种名为Arknife的编译器，它将指令可见布局视为第一类指令语义，以统一的方式处理后端布局要求。
- **原始摘要**: arXiv:2611.13741v1 Announce Type: new Abstract: Modern hardware accelerators achieve high performance through specialized instructions coupled with tightly managed memory hierarchies. These instructio...

### 2. RECURSUM: Automated Code Generation for Recurrence Relations Exceeds Expert Optimization via LayeredCodegen
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2604.18585
- **AI 摘要**: 文章讨论了RECURSUM项目，它通过三层代码生成技术超越了专家手动优化，用于生成优化后的C++代码以处理复杂数学关系。
- **原始摘要**: arXiv:2604.18585v2 Announce Type: replace Abstract: Automated code generation can systematically exceed expert hand-optimization for recurrence relations--computational primitives ubiquitous in orthog...

## 🏷️  光计算

**1 篇文章**

### 1. Millisecond optical coherence and strong collective coupling in an integrated telecom rare-earth photonic platform
- **来源**: arXiv physics.optics (光学/光计算) (TIER1)
- **提交时间**: 2026年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: 光计算
- **链接**: https://arxiv.org/abs/2608.08221
- **AI 摘要**: 文章讨论了在电信号集成光子平台上使用Er³⁺:CaWO₄晶体，通过消除粘合层直接与高Q电光可调薄膜铌酸锂微环共振器结合，实现了在电信波长下强光物质耦合和长相干时间。
- **原始摘要**: arXiv:2608.08221v2 Announce Type: replace-cross Abstract: Long-range quantum network nodes require the combination of strong light-matter coupling, long coherence times and in-situ spectral control at...

## 🏷️  军事技术

**30 篇文章**

### 1. Nvidia’s Board Is Meeting to Discuss Jensen Huang’s Future
- **来源**: The New York Times Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 23:32:14 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.nytimes.com/2026/11/11/technology/nvidia-jensen-huang.html
- **AI 摘要**: 文章内容与Nvidia董事会讨论Jensen Huang的未来相关，涉及个人关系问题，因此与军事技术相关。
- **原始摘要**: Mr. Huang has been under scrutiny for an affair with a woman said to be a Chinese spy, as well as a relationship with an executive at his A.I. chip company.

### 2. Trump Officials Clashed Over Megaspeed, Firm at Heart of Nvidia Affair
- **来源**: The New York Times Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 17:11:59 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.nytimes.com/2026/11/11/business/economy/nvidia-affair-spy-bessent-lutnick.html
- **AI 摘要**: 文章讨论了美国财政部和商务部对Megaspeed的芯片销售限制问题的分歧，Megaspeed是一家与Nvidia有关联的公司。文章主题与军事技术相关。
- **原始摘要**: Treasury Secretary Scott Bessent confronted Commerce Secretary Howard Lutnick last week about why the administration had not put restrictions on advanced chip sales to Megaspeed.

### 3. Nintendo unleashes DMCA takedown wave against open-source Switch modchip firmware, 144 tools disabled
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 13:42:37 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.tomshardware.com/video-games/nintendo/nintendo-unleashes-dmca-takedown-wave-against-open-source-switch-modchip-firmware-144-tools-disabled-picofly-sx-core-and-hwfly-among-casualties-following-criminal-trial-victory
- **AI 摘要**: 任天堂对开源的Switch模块芯片固件发起DMCA撤回行动，导致144种工具被禁用，其中包括Picofly、SX Core和HWFLY等工具。这起事件与军事技术无关。
- **原始摘要**: Nintendo is going after the open-source firmware behind hardware modchips on Nintendo Switch

### 4. 3,500 laser-armed AI submarine drones patrol Norwegian salmon farms, killing sea lice and protecting 112 million fish
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 10:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths
- **AI 摘要**: 文章描述了挪威使用3500个激光武装的AI潜艇机器人在鲑鱼养殖场巡逻，消灭海虱并保护11200万条鱼。这属于军事技术领域。
- **原始摘要**: 3,500 Stingray AI laser robots deployed around salmon pens along the Norwegian coast 24/7 protect over 112 million fish from sea lice.

### 5. Nato should take the ‘offensive’ against Russia, says Sedwill
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 17:28:09 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://www.ft.com/content/83dba705-b3cd-426b-92d2-096ac895c702?syn-25a6b1a6=1
- **AI 摘要**: 文章讨论了北约应采取主动对抗俄罗斯的战略，涉及陆地、海洋、空中、网络和太空等多个领域。这与军事技术相关。
- **原始摘要**: Former UK national security adviser makes reference to all domains, including land, sea, air, cyber and space

### 6. Russia will be satisfied only after win achieved, peace accords are signed — Medinsky
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 19:11:57 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/politics/2216523
- **AI 摘要**: 俄罗斯总统顾问Vladimir Medinsky表示，俄罗斯只有在赢得胜利并签署符合自身条件的和平协议后才会感到满意。这则新闻与军事技术相关。
- **原始摘要**: Russia, the United States and Ukraine held talks in Abu Dhabi on November 10-11

### 7. Kalashnikov showcases latest small arms, UAVs at CSTO forum
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:15:08 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/defense/2216475
- **AI 摘要**: Kalashnikov集团在国际集体安全论坛上首次展示了其最新的小武器和无人机。展品包括AK-12K和AK-12SK突击步枪、2023年型号的AK-12和7.62毫米的AK-15K和AK-15SK紧凑型版本。
- **原始摘要**: The exhibits include the Kalashnikov AK-12K and the compact AK-12SK assault rifles, the 2023-model Kalashnikov AK-12, as well as compact versions of the 7.62-mm AK-15K and AK-15SK

### 8. Ukrainian drone strikes destroy 115 buses in DPR since beginning of year
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:25:08 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/politics/2216377
- **AI 摘要**: TASS新闻报道了乌克兰无人机袭击导致顿涅茨克人民共和国115辆公交车被毁的情况。该报道属于军事技术类别。
- **原始摘要**: Ukrainian forces also targeted commuter buses

### 9. Russia’s Kub-2-2E UAV can be deployed in swarms — Rosoboronexport
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:33:46 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/defense/2216307
- **AI 摘要**: 俄罗斯的Kub-2-2E无人机可以部署成群，Rosoboronexport表示该无人机可以在40公里范围内摧毁目标，飞行速度为100-150公里/小时，续航时间为25分钟。
- **原始摘要**: The Kub has a flight speed of 100-150 km/h and can stay in the air for about 25 minutes

### 10. Expert names Russian air defense systems capable of shooting down Rusty Dagger missiles
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:25:49 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/defense/2216253
- **AI 摘要**: 文章内容主要关于俄罗斯的防空导弹系统可以拦截挪威制造的美国Rusty Dagger巡航导弹。文章提到了多种俄罗斯防空导弹系统，如S-300、S-400等，可以与美国的Storm Shadow和SCALP导弹相抗衡。
- **原始摘要**: According to retired Colonel Yury Knutov, these missiles can be countered in the same way as the Storm Shadow and SCALP missiles

### 11. The Famous World War I Poet Who Died Days Before the Armistice
- **来源**: Military.com (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:14:29 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.military.com/the-famous-world-war-one-poet-who-died-days-before-the-armistice
- **AI 摘要**: 本文讲述了在第一次世界大战结束前去世的英国军官和军功获得者威尔弗里德·奥威尔的故事。他在1918年11月11日去世，当时他的家人正在庆祝停战的消息。
- **原始摘要**: Wilfred Owen, a British infantry officer and Military Cross recipient, wrote World War I's best-known poems before dying at a French canal in 1918.

### 12. Ukrainian forces lose over 50 Baba-Yaga drones in battles for Voskresenka
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 14:40:08 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/politics/2216155
- **AI 摘要**: 俄罗斯军队在乌克兰的Voskresenka地区成功夺回阵地，并报告称乌克兰军队损失了超过50架Baba-Yaga重型六轴无人机。
- **原始摘要**: During prolonged fighting, units of Russia's Battlegroup East established control over a large area of Ukrainian defenses

### 13. Supercam to form new agricultural drone squadrons in 2027
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 14:38:53 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/economy/2216135
- **AI 摘要**: Supercam公司计划在2027年组建新的农业无人机中队，用于空中化学作业。该公司在2026年已开始使用无人机进行农作物保护产品的喷洒，覆盖了50个农场的90,000公顷土地。
- **原始摘要**: Field treatment using agricultural drones and their maintenance is a new line of business for Supercam launched by the company in 2026, the spokesperson said

### 14. Doomsday drone technology being adopted by Russian security agencies — expert
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 14:25:27 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://tass.com/defense/2216125
- **AI 摘要**: 俄罗斯安全机构正在采用一种名为‘Doomsday’的核打击后果缓解无人机技术。该技术由Dmitry Kuzyakin，一位无人驾驶航空专家和集成无人解决方案中心的首席设计师提供。
- **原始摘要**: According to Dmitry Kuzyakin, Russia’s security agencies currently have the largest supply of drones in the world

### 15. US midterms: Trump class, F-47, Golden Dome, and budgets
- **来源**: Army Technology (MILITARY)
- **发布日期**: 2026-11-12
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.army-technology.com/features/us-midterms-trump-class-f-47-golden-dome-and-budgets/
- **AI 摘要**: 文章内容主要讨论了美国中期选举的相关信息，包括特朗普、F-47战斗机、Golden Dome等军事项目和预算，与AI模型、Harness工程、具身智能、AI芯片、光计算、军事技术等主题无关。

### 16. Aselsan reports strong revenue, growth and record contracts
- **来源**: Army Technology (MILITARY)
- **发布日期**: 2026-11-12
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.army-technology.com/news/turkiyes-aselsan-2024-filing/
- **AI 摘要**: 文章主要报道了Aselsan公司在营收、增长和合同方面的良好表现，未涉及AI技术相关内容。

### 17. Saab reports increased order bookings in Q4 2024
- **来源**: Army Technology (MILITARY)
- **发布日期**: 2026-11-12
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.army-technology.com/news/saab-q4-2024-filing/
- **AI 摘要**: 文章主要报道了Saab公司在2024年第四季度订单增加的情况，与AI技术无关。

### 18. MilDef sees 89% jump in Q4 order intake and strong backlog
- **来源**: Army Technology (MILITARY)
- **发布日期**: 2026-11-12
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.army-technology.com/news/mildef-q4-2024-filing/
- **AI 摘要**: 文章主要讨论了MilDef在第四季度订单收入增长89%和强大的客户订单积压情况，未涉及AI技术相关内容。

### 19. Saab wins Danish order for CV90 drone and laser training equipment
- **来源**: Army Technology (MILITARY)
- **发布日期**: 2026-11-12
- **类型**: news
- **优先级**: medium
- **分类**: 军事技术
- **链接**: https://www.army-technology.com/news/saab-denmark-cv90-training-equipment/
- **AI 摘要**: 这篇文章报道了Saab公司获得了一份来自丹麦的订单，用于CV90无人机和激光训练设备。这与军事装备、武器系统和国防技术相关。

### 20. DoD pushes out 3 loans totaling $450M to bolster US space companies
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 20:15:00 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://breakingdefense.com/2026/11/dod-pushes-out-3-loans-totally-450m-to-bolster-us-space-companies/
- **AI 摘要**: 美国国防部宣布向三家美国太空公司发放总额4.5亿美元的贷款，以增强其发射和太空监测能力。最近的一笔贷款是1.5亿美元给火箭实验室，以帮助其增加其可重复使用的Neutron火箭的飞行率，以满足日益增长的商业和国家安全对太空访问的需求。
- **原始摘要**: One industry source told Breaking Defense that the reason for the spate of new loan announcements is that the Pentagon “needed to finalize loans by the end of the fiscal year.”...

### 21. The Army’s coming C2 challenge is fighting across thousands of miles
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:05:00 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://breakingdefense.com/2026/11/the-armys-coming-c2-challenge-is-fighting-across-thousands-of-miles/
- **AI 摘要**: 文章讨论了美国陆军的NGC2计划，该计划旨在建立一个能够加速数据收集、管理和分析，并支持多域作战的统一数据基础设施。文章提到了NGC2将如何帮助应对战场上的不断变化的威胁。
- **原始摘要**: Breaking down stovepipes, managing data and enabling better decision making are key components of the Army’s NGC2 plan....

### 22. Australian Army’s littoral transformation is the right move, experts say
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:31:41 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://breakingdefense.com/2026/11/australian-armys-littoral-transformation-is-the-right-move-experts-say/
- **AI 摘要**: 文章讨论了澳大利亚军队将地面部队转型为专注于沿海机动的部队的决定，以及专家对此的评价。文章提到了2024年澳大利亚国防战略中提出的计划，并指出该决定是为了应对印度-太平洋地区的紧张局势。文章还提到了预算削减可能影响到一些项目，从而影响到该单位的资源分配。
- **原始摘要**: The introduction of two new classes of landing craft would introduce capabilities that the Australian Army has not operated in recent times, an expert told Breaking Defense....

### 23. NATO taps Ukraine as red-team in drills to ‘trigger an adaptation cycle’
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:17:05 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://breakingdefense.com/2026/11/nato-taps-ukraine-as-red-team-in-drills-to-trigger-an-adaptation-cycle/
- **AI 摘要**: 北约利用乌克兰作为‘红队’在演习中‘触发适应循环’。北约高级官员表示，这是为了提升其战场战术。乌克兰在2025年葡萄牙的REPMUS演习中击败了北约成员国。
- **原始摘要**: “What we’ve done so far, we took some experience from Ukraine, for example, where we hid some Ukrainian forces and Ukrainian-made USVs, and made them the red team against the blue force of NATO,” Adm....

### 24. Plans To Fly Talon Blue CCA Drone From British Carrier Confirmed By Northrop Grumman
- **来源**: The War Zone (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:30:40 -0500 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://www.twz.com/news-features/plans-to-fly-talon-blue-cca-drone-from-british-carrier-confirmed-by-northrop-grumman
- **AI 摘要**: 文章提到北诺斯罗普·格鲁曼确认了英国皇家海军计划在航空母舰上飞行Talon Blue CCA无人机。这架无人机将比之前任何在航空母舰上飞行的无人机更先进。
- **原始摘要**: The Royal Navy wants to infuse drone capabilities into its air wings and Talon Blue would be far more advanced than anything that has flown off the carriers yet. The post Plans To Fly Talon Blue CCA D...

### 25. Inside Warhound’s plan to engineer a better military working dog
- **来源**: Defense News (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:00:00 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://www.defensenews.com/industry/techwatch/2026/11/11/inside-warhounds-plan-to-engineer-a-better-military-working-dog/
- **AI 摘要**: 文章报道了一家名为Warhound的创业公司获得了2000万美元的融资，计划通过基因工程来提升军犬的能力。这与军事技术相关。
- **原始摘要**: The company plans to clone top-performing dogs, edit genes associated with health problems and introduce standardized training to puppies as young as two weeks old.

### 26. When networks are contested, paring down the data may mean better logistics at the edge
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 13:42:00 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://breakingdefense.com/2026/11/when-networks-are-contested-paring-down-the-data-may-mean-better-logistics-at-the-edge/
- **AI 摘要**: 本文讨论了在网络被敌对势力攻击的情况下，如何通过减少数据量来提高边缘战场的物流能力。文章提到了软件定义系统、智能仓储和远程更新等技术在提高军事后勤能力中的应用。
- **原始摘要**: AI and software can improve logistics, but only if they work with limited bandwidth....

### 27. F-35s Train In India For “Red Flag Of The East”
- **来源**: The War Zone (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 13:31:47 -0500 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://www.twz.com/air/f-35s-train-in-india-for-red-flag-of-the-east
- **AI 摘要**: F-35战斗机在印度进行了训练演习，与印度空军及其他七国外空军队一同参与。
- **原始摘要**: Seven foreign air forces trained alongside the Indian Air Force, as American F-35s took part in their first exercise in India. The post F-35s Train In India For “Red Flag Of The East” appeared first o...

### 28. Autonomous Cessna Caravan Air Ambulance To Be Tested By U.S. Military
- **来源**: The War Zone (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 12:46:17 -0500 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://www.twz.com/news-features/autonomous-cessna-caravan-air-ambulance-to-be-tested-by-u-s-military
- **AI 摘要**: 文章提到美国军方将测试一款自主的Cessna Caravan空中救护车，该测试将在摩洛哥进行。这表明无人选项在其他遥远地区也可能有价值。
- **原始摘要**: The demonstration will take place in Morocco, but uncrewed options for rescuing casualties could be valuable in other far-flung locales globally. The post Autonomous Cessna Caravan Air Ambulance To Be...

### 29. Romanian servers targeted by Russian hackers to scoop up emails about NATO, EU
- **来源**: Defense News (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 12:08:33 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://www.defensenews.com/global/europe/2026/11/11/romanian-servers-targeted-by-russian-hackers-to-scoop-up-emails-about-nato-eu/
- **AI 摘要**: 文章提到的是关于俄罗斯黑客利用罗马尼亚服务器窃取与北约和欧盟相关的电子邮件。这与军事技术相关，但文章内容更偏向于网络安全和情报收集，因此更贴切的分类是军事技术。
- **原始摘要**: Hackers linked to Russia's FSB quietly compromised a Romanian government organization’s servers to collect emails related to NATO and the EU in December 2025, a Slovak cybersecurity firm has revealed.

### 30. Army Wants New Palletized Short-Range Air Defenses In Service By The End Of 2029
- **来源**: The War Zone (MILITARY)
- **发布日期**: Tue, 10 Nov 2026 18:43:49 -0500 (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 军事技术
- **链接**: https://www.twz.com/land/army-wants-new-palletized-short-range-air-defenses-in-service-by-the-end-of-2029
- **AI 摘要**: 美国陆军希望在2029年底之前部署新的短程防空系统，这些系统被称为‘雪橇’，旨在提供新的灵活性和容量，特别是针对无人机群。
- **原始摘要**: Army sees new short-range air defense 'sleds' providing critical new flexibility and capacity, especially against drone swarms. The post Army Wants New Palletized Short-Range Air Defenses In Service B...

## 🏷️  经济

**59 篇文章**

### 1. Softbank loses $3.7 billion on canceled AI data center gas turbine orders days after denying Elon Musk’s claim it was defaulting
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 14:29:43 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://www.tomshardware.com/tech-industry/data-centers/softbank-loses-usd3-7-billion-on-canceled-ai-data-center-gas-turbine-orders-days-after-denying-elon-musks-claim-it-was-defaulting-company-kills-reserved-13-gigawatts-of-power-more-than-six-hoover-dams-worth-of-capacity
- **AI 摘要**: 软银因取消了价值37亿美元的AI数据中心燃气涡轮订单而亏损，这发生在该公司否认埃隆·马斯克称其违约后不到一天。软银取消了13吉瓦的电力储备，相当于超过6座大坝的容量。
- **原始摘要**: SoftBank might not have defaulted on a raft of gas turbine orders, but it has pulled out of deals for unwanted power units after overestimating how many it could use amid the AI data center buildout b...

### 2. We Are Probably Overbuilding Data Centers: Gary Marcus
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 23:05:40 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/we-are-probably-overbuilding-data-centers-gary-marcus-video
- **AI 摘要**: 文章讨论了Gary Marcus对Anthropic IPO的批评，认为其财务前景依赖于快速且持续的增长。文章来源为Bloomberg。
- **原始摘要**: Gary Marcus argues that investors should avoid Anthropic’s IPO because its financial outlook depends on rapid, sustained growth. He speaks with Romaine Bostick and Vonnie Quinn on The Close. (Source:...

### 3. Hosin, Amicro Set to Trade in Hong Kong as IPOs Gather Pace
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 23:00:00 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/hosin-amicro-set-to-trade-in-hong-kong-as-ipos-gather-pace
- **AI 摘要**: 中国内存产品制造商Hosin Electronics Co.和机器人技术平台Amicro Technology Co.计划在周四开始在香港进行交易，这是投资者对地区科技股兴趣的测试，此前Anthropic PBC的大型美国上市即将来临。
- **原始摘要**: Chinese memory product maker Hosin Electronics Co. and robotics technology platform Amicro Technology Co. are set to begin trading on Thursday in Hong Kong in a test of investor appetite for technolog...

### 4. CoreWeave Plans to Raise at Least $4 Billion in High-Grade Loan
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:42:47 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/coreweave-plans-to-raise-at-least-4-billion-in-high-grade-loan
- **AI 摘要**: CoreWeave公司计划通过投资级贷款筹集至少40亿美元，因为这家AI计算供应商上调了年度销售预期，缓解了投资者对其负债累累的业务的担忧。
- **原始摘要**: CoreWeave Inc. plans to raise at least $4 billion through an investment-grade loan offering after the AI computing supplier boosted its annual sales forecast, easing investor concerns about its debt-l...

### 5. Nissan's Ivan Espinosa on China, US, Japan Markets and Company Outlook
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:29:28 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/nissan-s-ivan-espinosa-on-china-us-japan-markets-video
- **AI 摘要**: 本文标题为Nissan的Ivan Espinosa对中国、美国和日本市场的展望。内容主要涉及市场分析和公司前景。这与AI技术无关。
- **原始摘要**: Nissan CEO Ivan Espinosa spoke to Bloomberg News' Nicholas Takahashi about the company's outlook following its earnings, including growth prospects in major markets such as China, the US and Japan. (S...

### 6. US Stock Futures Fall as Nvidia Turmoil Deepens: Markets Wrap
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:08:05 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/stock-market-today-dow-s-p-live-updates
- **AI 摘要**: 本文内容与股市和金融市场相关，未提及任何AI技术或具体应用。
- **原始摘要**: US stock futures fell as turmoil at Nvidia Corp. sent a jolt through the artificial intelligence industry, tempering a rally in technology shares after the chipmaker was reported to be considering the...

### 7. BC Partners to Buy Investcorp BDC Amid Private Credit Shakeout
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:03:25 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/bc-partners-to-buy-investcorp-bdc-amid-private-credit-shakeout
- **AI 摘要**: 本文内容与AI技术无关，属于经济新闻，涉及私募信贷市场的变动。
- **原始摘要**: Buyout firm BC Partners has agreed to purchase a struggling business development company from Investcorp, as turbulence in the $1.8 trillion private credit market continues to fuel consolidation.

### 8. Stocks Slide as AI Trade Roars Back | Closing Bell
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 21:58:37 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/stocks-slide-as-ai-trade-roars-back-closing-bell-video
- **AI 摘要**: 文章主要报道了美国市场的收盘情况，涉及Bloomberg Television、Bloomberg Radio和YouTube的综合跨平台覆盖，由Romaine Bostick、Vonnie Quinn、Carol Massar和Tim Owens主持。文章主题为金融市场和股市。
- **原始摘要**: Comprehensive cross-platform coverage of the U.S. market close on Bloomberg Television, Bloomberg Radio, and YouTube with Romaine Bostick, Vonnie Quinn, Carol Massar and Tim Stenovec. (Source: Bloombe...

### 9. Paraguay on Watch for Downgrade at Fitch After Bank Collapse
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Wed, 11 Nov 2026 21:43:21 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/paraguay-on-watch-for-downgrade-at-fitch-after-bank-collapse
- **AI 摘要**: 本文讨论了Paraguay可能因银行危机面临Fitch评级下调的风险。
- **原始摘要**: Fitch Ratings placed Paraguay’s credit rating on watch for a potential downgrade on Wednesday, citing risks to the nation’s finances and economy from a banking crisis that toppled President Santiago P...

### 10. OpenAI, Anthropic Valuations Fuel VC Fears of Startup Correction
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 21:39:14 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/openai-anthropic-valuations-fuel-vc-fears-of-startup-correction
- **AI 摘要**: 文章讨论了OpenAI和Anthropic的估值对初创企业融资的影响，暗示了可能的市场回调。
- **原始摘要**: In late September, OpenAI entered discussions for its latest funding round with confidence. After having early discussions with prospective backers who had expressed interest, the company presented it...

### 11. Lula Unveils Plan to Curb Spending Growth in Bid to Calm Fiscal Worries
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Wed, 11 Nov 2026 21:34:24 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/lula-unveils-plan-to-curb-spending-growth-in-bid-to-calm-fiscal-worries
- **AI 摘要**: 巴西总统卢拉(Luiz Inácio Lula da Silva)公布了旨在加强公共财政和缓解投资者对公共债务上升的担忧的措施，以平息自其选举胜利以来市场上的财政担忧。
- **原始摘要**: Brazil’s government unveiled a package of measures meant to shore up public finances and ease investor concerns about rising public debt, as President Luiz Inácio Lula da Silva aims to alleviate fisca...

### 12. Nvidia shares rebound as Jensen Huang faces scrutiny ahead of earnings
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 21:04:36 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/11/nvidia-stock-jensen-huang-affair-china.html
- **AI 摘要**: Nvidia股票在CEO Huang面临调查前反弹。投资者正在评估其个人事务是否会对Nvidia的业务产生影响。
- **原始摘要**: Investors are assessing whether CEO Jensen Huang's affair will have spillover effects on Nvidia's business.

### 13. US tech stocks rally as AI trade revives
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 21:04:17 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/639de881-6017-454f-abfa-cfb191d1e7cd?syn-25a6b1a6=1
- **AI 摘要**: 纳斯达克市场在上周亏损后收复失地，CoreWeave的结果和更高Anthropic IPO估值的前景提振了市场情绪。
- **原始摘要**: Nasdaq erases last week’s losses as CoreWeave results and prospect of higher Anthropic IPO valuation boost sentiment

### 14. Microsoft Vows to Pay Its Own Way to Power Data Centers
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 20:33:16 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/microsoft-vows-to-pay-its-own-way-to-power-data-centers
- **AI 摘要**: 微软表示将寻找方式自行支付其数据中心的电力，不再依赖政府补贴或增加其他电力消费者的成本。
- **原始摘要**: Microsoft Corp. aims to find ways to power its data centers without relying on government subsidies or driving up costs for other electricity consumers.

### 15. Prediction markets tied to clinical trials and drug approvals draw lawmakers' ire
- **来源**: CNBC Top News (TIER3)
- **发布日期**: Wed, 11 Nov 2026 19:16:23 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/11/kalsi-polymarket-prediction-market-senators-hhs-drug-approval.html
- **AI 摘要**: 民主党参议员Angela Alsobrooks和Ron Wyden敦促卫生与人类服务部减轻与临床试验和食品和药物管理局批准相关的预测市场的风险。他们通过一封CNBC首先获得的信函表达了对这些市场可能影响患者的影响的担忧。
- **原始摘要**: Sens. Angela Alsobrooks and Ron Wyden are asking what steps the Department of Health and Human Services has taken to mitigate risks from the markets.

### 16. Healey says Treasury discussing ‘worst-case’ energy support for UK households
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 18:47:25 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/22798c90-e999-4564-924a-4f04343cac3d?syn-25a6b1a6=1
- **AI 摘要**: 哈丽叶表示财政部正在讨论为英国家庭提供‘最坏情况’的能源支持，并称结束伊朗战争将是英国经济的最大提振。
- **原始摘要**: Chancellor prepares for deepening energy crisis and says end to Iran war would be biggest boost to Britain’s economy

### 17. CFTC investigates if Kalshi improperly self-certified event contracts
- **来源**: CNBC Top News (TIER3)
- **发布日期**: Wed, 11 Nov 2026 17:22:34 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/11/cftc-investigates-if-kalshi-improperly-self-certified-event-contracts.html
- **AI 摘要**: 美国商品期货交易委员会(CFTC)正在调查Kalshi是否违规自行认证了某些事件合同。Kalshi表示正在与CFTC合作解决该问题。允许预测市场平台在不获得联邦机构批准的情况下自行认证事件合同，只要它们符合《商品交易法》。
- **原始摘要**: News of the probe comes after the CFTC ordered Kalshi to take down a sports-related "mention markets" back in August.

### 18. What’s really going on in the UK labour market?
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 17:00:07 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/c3f6a7b9-5a15-4651-a855-18d2ea29f8f5
- **AI 摘要**: 本文讨论了英国劳动力市场的实际情况，以确定货币政策应如何紧缩。
- **原始摘要**: Getting clear about how much slack there is will tell us how tight monetary policy should be

### 19. Single-stock perps look like pointiest horn of a bull market
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 15:57:13 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/0ecbc732-4d5a-4a3e-97aa-86d19285bcf8?syn-25a6b1a6=1
- **AI 摘要**: 文章主要讨论了单股票权市场面临的监管不确定性问题，认为这是阻碍更广泛采用的主要障碍。
- **原始摘要**: Regulatory uncertainty is the biggest hurdle to wider adoption, says one survey

### 20. Britain should ‘exploit’ NHS data to power AI, says minister
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 14:37:32 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/f95d9298-d27e-4c1b-87e5-ea75f67a1e0c?syn-25a6b1a6=1
- **AI 摘要**: 英国大臣Chris McDonald表示，国家在整合生命科学和人工智能产业方面具有‘战略竞争优势’，应充分利用NHS数据推动AI发展。
- **原始摘要**: Chris McDonald says country has ‘strategic competitive advantage’ in uniting its life sciences and AI industries

### 21. How GLP-1 Drugs and a Revamp Revived Ro’s Business
- **来源**: The New York Times Business (TIER3)
- **发布日期**: Wed, 11 Nov 2026 14:06:50 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.nytimes.com/2026/11/11/business/dealbook/ro-revenue-glp1.html
- **AI 摘要**: 文章主要讲述了远程医疗服务公司通过重新调整业务并拥抱减肥治疗，其年度化收入增长了近十倍。这与AI技术并无直接关联。
- **原始摘要**: The telehealth company said that its annualized revenue had grown nearly tenfold since it revamped its business and embraced weight-loss treatments.

### 22. Anthropic’s I.P.O. and the Clubby Business of A.I.
- **来源**: The New York Times Business (TIER3)
- **发布日期**: Wed, 11 Nov 2026 13:40:36 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.nytimes.com/2026/11/11/business/dealbook/anthropic-ipo-nvidia.html
- **AI 摘要**: 文章讨论了Anthropic即将上市的AI巨头背后的投资者及其重要业务伙伴关系。这与AI模型和Harness工程无关，但与经济领域中的资本市场和企业关系相关。
- **原始摘要**: Some of the biggest investors in the artificial intelligence giant’s upcoming listing are also some of its most important business partners.

### 23. German Economic Advisers More Than Double 2026 Growth Forecast
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 13:30:00 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/german-economic-advisers-more-than-double-2026-growth-forecast
- **AI 摘要**: 德国经济顾问将今年的增长预期提高了两倍以上，得益于大规模政府支出和出口表现超出预期。
- **原始摘要**: Germany’s economy will expand this year at more than twice the pace envisaged in the spring thanks to vast government spending and surprisingly robust exports, according to the country’s independent e...

### 24. Nasdaq 100 Rallies as CoreWeave Quells AI Fears, Draws Buyers In
- **来源**: Bloomberg Markets (TIER3)
- **发布日期**: Wed, 11 Nov 2026 13:28:45 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/us-equity-futures-rise-as-ai-enthusiasm-counters-hot-inflation
- **AI 摘要**: 本文讨论了Nasdaq 100指数因CoreWeave公司缓解了对AI的担忧而上涨的情况，涉及金融和股市相关内容。
- **原始摘要**: US technology stocks rallied Wednesday, with the technology-heavy Nasdaq 100 index nearly erasing losses since the US midterm election, as renewed excitement over the artificial intelligence trade lur...

### 25. The wonderful shallowness of Andy Burnham
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 12:38:42 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/978493a9-7c1c-4ec6-9310-9d17b92acb12?syn-25a6b1a6=1
- **AI 摘要**: 文章讨论了Andy Burnham左翼姿态的表面功夫，暗示英国应该感谢这一点。这与AI技术无关。
- **原始摘要**: He makes leftwing gestures to avoid taking leftwing action. Britain should thank its stars

### 26. US and China trade ties
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 12:00:01 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/newsletters/2026-11-11/us-and-china-trade-ties
- **AI 摘要**: 本文标题为《US and China trade ties》，内容主要涉及美国和中国的贸易关系，未提及任何AI技术或相关话题。因此，文章主题与AI技术无关。
- **原始摘要**: Bessent hailed bilateral relations and Trump’s close engagement with Xi

### 27. Chile Finance Minister Jorge Quiroz Says Recession Is Short-Term Blip
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 11:00:10 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/chile-finance-minister-jorge-quiroz-says-recession-is-short-term-blip
- **AI 摘要**: 本文讨论了智利财政部长Jorge Quiroz的观点，认为经济衰退只是短期的波动。这与AI技术无关。
- **原始摘要**: Chile Finance Minister Jorge Quiroz conceded for the first time that the economy is in a recession, while stressing activity will rebound quickly.

### 28. ‘Fear factor’ hits the AI power boom
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 11:00:06 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.ft.com/content/1bf39007-d0c1-441c-8a87-906c5284bd1a?syn-25a6b1a6=1
- **AI 摘要**: 文章提到AI相关公司的股价持续下滑，同时希望为数据中心提供动力的公司花费大量资金。这暗示了AI热潮可能受到抑制。
- **原始摘要**: Shares continue to slide while companies hoping to power data centres spend heavily

### 29. German Economy on the Mend Though Reforms Needed, Nagel Says
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 08:20:00 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/german-economy-on-the-mend-though-reforms-needed-nagel-says
- **AI 摘要**: 德国经济正在比几个月前预期的更快复苏，但政府必须继续推进结构性改革以确保长期增长。Bundesbank行长Joachim Nagel表示。
- **原始摘要**: Germany’s economy is rebounding faster than expected a few months ago, but the government must press ahead with structural reforms to secure long-term growth, Bundesbank President Joachim Nagel said.

### 30. Investors pivot to defensive stocks as markets enter a ‘state of alert’
- **来源**: CNBC Top News (TIER3)
- **发布日期**: Wed, 11 Nov 2026 06:00:01 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/11/tech-selloff-defensive-pivot.html
- **AI 摘要**: 文章提到投资者转向防御性行业，如医疗保健、消费必需品和公用事业，以应对科技股的波动。文章提到了科技行业面临的AI支出、融资和经济前景的担忧。文章建议防御性轮动可能已经过度，科技估值大幅下跌，尽管基本面并未受到影响。
- **原始摘要**: Technology stocks have lost momentum while defensive sectors gain ground, as investors reassess risks.

### 31. Anthropic opens Australian retail IPO offering as AI scrutiny intensifies
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 01:52:56 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/11/anthopic-australian-retail-ipo-offering-.html
- **AI 摘要**: Anthropic在澳大利亚启动了零售IPO，同时加强了对AI公司的监管。IPO预计于11月17日结束。
- **原始摘要**: Anthropic opened its Australia retail IPO offering on Wednesday, allowing individual investors to apply for shares ahead of its planned IPO.

### 32. Fed’s Goolsbee Says October CPI Report ‘Borderline Disturbing’
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 00:51:18 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/fed-s-goolsbee-says-october-cpi-report-borderline-disturbing-mwbel9qz
- **AI 摘要**: 芝加哥联储主席Austan Goolsbee表示，官员们需要应对通胀问题，十月消费者价格指数报告令人不安。
- **原始摘要**: Federal Reserve Bank of Chicago President Austan Goolsbee said officials have to address elevated inflation, calling the October report on consumer prices disturbing.

### 33. Australia’s Home Loans Fall by Record After Rapid RBA Rate Hikes
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 00:49:42 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/australia-s-home-loans-fall-by-record-after-rapid-rba-rate-hikes
- **AI 摘要**: 澳大利亚第三季度住房贷款创下纪录下滑，反映了利率激增以控制通胀导致的借款需求下降。
- **原始摘要**: Australian home loans posted a record drop in the third quarter, underscoring the erosion of borrowing demand in response to the Reserve Bank’s aggressive interest-rate increases to control inflation.

### 34. Officials From Major Central Banks Signal More Rate Increases
- **来源**: Bloomberg Economics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 00:01:00 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/officials-from-major-central-banks-signal-more-rate-increases
- **AI 摘要**: 主要央行官员在伦敦举行的会议上暗示将进一步提高利率，英国央行可能需要将借款成本提高到5%。
- **原始摘要**: Policymakers from the UK, US and eurozone gathered in London laid the groundwork for further interest-rate hikes, as a leading think tank warned the Bank of England may have to raise borrowing costs t...

### 35. Jim Cramer: Wall Street is focusing too much on what could go wrong instead of right
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Tue, 10 Nov 2026 23:41:43 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cnbc.com/2026/11/10/cramer-stocks-inflation-nvidia-anthropic.html
- **AI 摘要**: 文章主要讨论了投资者不应过分关注市场风险，而应关注可能推动股市反弹的因素。Cramer提到了油价下跌、Nvidia领导层不确定性解决以及Anthropic即将上市等发展。
- **原始摘要**: Investors shouldn't let mounting market risks overshadow the potential for a rebound, CNBC's Jim Cramer said Tuesday.

### 36. Alrosa unveils rare pink diamond worth $1.5 mln
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 21:49:30 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216597
- **AI 摘要**: 俄罗斯钻石公司Alrosa在新年展示会上展示了一颗价值150万美元的罕见粉色钻石。这颗钻石重3.07克拉，形成于3亿年前，是投资级钻石类别中的稀有品种。
- **原始摘要**: The gemstone with an estimated age of 300 mln years was unearthed in Yakutia in 2025

### 37. India's oil imports up to record level in September with over third supplied by Russia
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:57:02 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216519
- **AI 摘要**: 印度9月份的石油进口量创历史新高，其中超过三分之一的石油来自俄罗斯。俄罗斯在9月份对印度的石油供应占比从8月份的45%降至35%。印度的石油进口量在9月份达到了创纪录的水平，主要原因是炼油能力的增强。
- **原始摘要**: Imports rose by 20% on average compared to August to 5.4 mln barrels per day

### 38. Steelmaking in Russia down 1.9% in October 2026 — statistics
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:45:26 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216515
- **AI 摘要**: 2026年10月俄罗斯钢铁产量下降1.9%，至520万吨。前10个月的钢铁产量下降3%，至5440万吨。
- **原始摘要**: Over the first ten months of 2026, steel output declined by 3% to 54.4 mln tons

### 39. Russian Agriculture Ministry expects higher duties on wines from unfriendly countries
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:17:01 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216479
- **AI 摘要**: 俄罗斯农业部表示，2026年将对来自敌对国家的葡萄酒征收更高的关税。此前已两次提高关税。
- **原始摘要**: There have already been two increases in 2026, Oksana Lut noted

### 40. Gazprom updates record daily gas supplies to China for fifth time in November
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:00:27 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216445
- **AI 摘要**: Gazprom更新了其对中国的天然气供应记录，这是11月第五次更新。俄罗斯天然气供应通过西伯利亚力量管道进行，该管道的长期购买和销售协议由Gazprom和CNPC之间签订。俄罗斯副总理亚历山大·诺瓦克表示，今年将通过西伯利亚力量管道向中国供应390亿立方米的天然气。
- **原始摘要**: The new record was set on November 10

### 41. German authorities decided to create strategic gas reserves
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:56:35 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216437
- **AI 摘要**: 德国政府决定建立国家战略天然气储备，以应对严重中断、破坏或其他紧急情况。该储备的目标容量为24太瓦时（TWh），约占德国天然气存储容量的10%。储备容量预计足以补偿30天的国家天然气进口基础设施停运。
- **原始摘要**: Ministers approved the relevant draft regulatory act proposed by Economy Minister Katherina Reiche at a cabinet meeting

### 42. Russia’s 2026 grain harvest reaches around 140 mln tons, wheat exceeds 95 mln tons
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:51:57 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216431
- **AI 摘要**: 俄罗斯2026年粮食总产量约为1.4亿吨，其中小麦产量超过9500万吨。
- **原始摘要**: The harvest of oilseeds has grown by 13% since the start of the year, reaching 34.8 million tons, with the final annual figure projected to exceed 35 million tons in net weight

### 43. Hungary faces difficulty in moving away from Russian gas due to LNG market crisis — expert
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:44:58 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216417
- **AI 摘要**: 匈牙利因液化天然气市场危机难以摆脱对俄罗斯天然气的依赖，俄罗斯天然气工业研究所的Alexey Belogoryev表示，匈牙利和其他欧盟国家都面临液化天然气进口短缺的问题，主要是因为来自卡塔尔的大宗量天然气供应不足。
- **原始摘要**: "At present, not only Hungary but other EU nations as well are facing a shortage of LNG imports, as supply is severely constrained by the absence of major volumes of Qatari gas from the market," Alexe...

### 44. Bank of Russia raises dollar exchange rate to 82.66 rubles for November 12
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:28:24 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216387
- **AI 摘要**: 本文报道了俄罗斯央行将美元汇率定为82.66卢布，同时提到了欧元和人民币的汇率变动。文章内容与AI技术无关，属于经济领域。
- **原始摘要**: The official euro exchange rate has been raised by 30.02 kopecks to 92.6968 rubles

### 45. OPEC+ countries increase oil production by 1.94 mln bpd in October
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:27:54 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216383
- **AI 摘要**: OPEC+成员国在2026年10月提高了石油产量，达到32.817万桶/日，比9月增加了1.94万桶/日。
- **原始摘要**: The alliance’s oil production totaled 32.817 mln bpd

### 46. Seven OPEC+ countries boost oil production by 1.976 mln bpd in October
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:24:04 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216371
- **AI 摘要**: 七家OPEC+成员国在10月将石油产量提高了197.6万桶/日，总产量达到2818.1万桶/日。沙特阿拉伯的产量增加了118.2万桶/日，达到9194万桶/日。
- **原始摘要**: Among the seven countries, Saudi Arabia saw the largest increase in oil production in October, raising its output by 1.182 million bpd to 9.194 million bpd

### 47. Russia increases oil production by 41,000 bpd in October — OPEC
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:10:25 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216353
- **AI 摘要**: 俄罗斯在2026年10月的石油产量增加了41000桶/天，达到866.8万桶/天。根据OPEC的报告，俄罗斯的石油产量配额为994.9万桶/天，其中包括自愿限制。这使得俄罗斯在该月的产量低于配额128.1万桶/天。
- **原始摘要**: The figure increased to 8.668 million bpd

### 48. Russian foreign trade surplus down to $12.1 bln in September 2026 — Central Bank
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:59:15 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216335
- **AI 摘要**: 俄罗斯2026年9月的对外贸易顺差降至121亿美元，较8月减少323亿美元，较去年同期减少150亿美元。
- **原始摘要**: The figure increased by $323 mln against August 2026

### 49. Cost of Russian gas, rising demand, situation in Europe: what we know
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:58:03 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216331
- **AI 摘要**: 文章主要讨论了俄罗斯天然气价格、需求增加以及欧洲的情况，涉及政治和经济领域。
- **原始摘要**: Hungary’s Prime Minister Peter Magyar said that his government does not consider Russian gas to be cheap and continues to look for alternative sources to import fuel at the most favorable prices

### 50. US refinery utilization falls to 92.93% in October — OPEC report
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:48:22 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216323
- **AI 摘要**: 美国炼油厂利用率在10月降至92.93%，低于9月的94.4%。OPEC报告显示，美国炼油厂10月日均产量为167.7万桶，比上月减少24.7万桶。全球炼油厂10月日均产量为786.1万桶，比上月减少123万桶。
- **原始摘要**: US refinery throughput totaled 16.77 mln barrels per day in October

### 51. OPEC keeps non-OPEC+ supply growth forecast for 2026
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:47:36 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216321
- **AI 摘要**: OPEC维持2026年非OPEC+国家石油产量增长预期为每天60万桶，主要增长动力来自巴西、美国、加拿大和阿根廷。
- **原始摘要**: Brazil, the United States, Canada and Argentina are expected to be the main growth drivers

### 52. Russian e-commerce market reaching $133 bln over 9M 2026
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:44:17 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216317
- **AI 摘要**: 俄罗斯电子商务市场在2026年前9个月的交易额约为11万亿卢布（约132.9亿美元），尽管用户数量基本没有增加，但得益于新技术的引入，市场仍在发展。
- **原始摘要**: Despite the fact that the number of e-commerce users is practically not increasing, the market continues to develop due to the introduction of new technologies, Artyom Sokolov noted

### 53. Russia’s groundwater reserves to increase by 40,000 cubic meters per day in 2026
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:33:52 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 经济
- **链接**: https://tass.com/economy/2216305
- **AI 摘要**: 俄罗斯计划在2026年通过联邦预算支持的地质勘探，使地下水储备增加40,000立方米/天。
- **原始摘要**: Geological exploration at four new sites is planned for 2027, with groundwater reserves expected to increase by 60,600 cubic meters per day

### 54. The Economics of AI ReasoningJune 17, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 17, 2026
- **类型**: blog
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cerebras.ai/blog/the-economics-of-ai-reasoning
- **AI 摘要**: 文章讨论了AI推理的经济性，涉及AI模型的成本效益分析。

### 55. The Year of Latency Debt (And How Big Tech Is Paying It Down)January 28, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 28, 2026
- **类型**: blog
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.cerebras.ai/blog/latency-debt
- **AI 摘要**: 文章讨论了2026年延迟债务的问题，以及大型科技公司如何解决这一问题。

### 56. Investor Relations
- **来源**: Zhipu AI Research (TIER1)
- **发布日期**: 2026-11-12
- **类型**: research
- **优先级**: high
- **分类**: 经济
- **链接**: https://zhipuai.cn/investor_relations
- **AI 摘要**: 文章标题为Investor Relations，内容与投资关系相关，明显不属于上述任何类别关键词范围。

### 57. Business License
- **来源**: Zhipu AI Research (TIER1)
- **发布日期**: 2026-11-12
- **类型**: research
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.zhipuai.cn/en/certificates/1
- **AI 摘要**: 摘要内容为空，无法生成总结。

### 58. Welcoming Bill Nash as CFOBill brings extensive financial leadership experience from some of the most technically ambitious and fast-moving companies in autonomy, aerospace, and life sciences.JUL 02 '261X
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 经济
- **链接**: https://www.1x.tech/discover/bill-nash-cfo
- **AI 摘要**: Bill Nash 将担任 CFO 职位，拥有在自动驾驶、航空航天和生命科学领域技术最先进且发展迅速的公司中的丰富财务领导经验。

### 59. We've raised $700M at a $21B valuation led by Jane StreetLearn more
- **来源**: Etched (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 经济
- **链接**: https://etched.com/progress/progress/from-zero-to-one
- **AI 摘要**: 文章提到We've raised $700M at a $21B valuation led by Jane Street，与AI技术无关。

## 🏷️  时政

**121 篇文章**

### 1. Jensen Huang accused of having another affair — with an Nvidia exec
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 23:17:05 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://techcrunch.com/2026/11/11/jensen-huang-accused-of-having-another-affair-with-a-nvidia-exec/
- **AI 摘要**: TechCrunch报道称Nvidia CEO Jensen Huang涉嫌与公司员工Kimberly Powell有婚外情。Nvidia已启动对Huang公开承认的婚外情的调查。
- **原始摘要**: Jensen Huang, who has come under fire for admitting to an affair with a woman accused of being a Chinese intelligence agent, has been accused of having a separate affair with an Nvidia subordinate.

### 2. Court Rules That Sexual Harassment Case Against SpaceX Can Proceed
- **来源**: The New York Times Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 20:51:49 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.nytimes.com/2026/11/11/business/sexual-harassment-spacex-elon-musk.html
- **AI 摘要**: SpaceX公司因性骚扰案件需在仲裁员面前解决的主张被法院驳回。法院认为该案件可以继续进行。
- **原始摘要**: The company had argued that the case, involving eight former workers, must be resolved before an arbitrator.

### 3. How backlash and red tape continue to slow data centers post-Blue Wave
- **来源**: TechCrunch AI (TIER3)
- **发布日期**: Wed, 11 Nov 2026 20:02:14 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://techcrunch.com/podcast/how-backlash-and-red-tape-continue-to-slow-data-centers-post-blue-wave/
- **AI 摘要**: 本文讨论了数据中心建设面临的反对意见和审批延迟问题，以及在AI基础设施投资巨大的背景下，区分实际可行项目与空想项目的必要性。
- **原始摘要**: The data center boom is running into serious real-world obstacles, from widespread local opposition and permitting delays to a scramble for electricity. Before those challenges even come into play, th...

### 4. Congress to call Jensen Huang in to answer for alleged Chinese spy affair
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 19:22:22 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://techcrunch.com/2026/11/11/congress-to-call-jensen-huang-in-to-answer-for-alleged-chinese-spy-affair/
- **AI 摘要**: 美国国会计划传唤Nvidia首席执行官Jensen Huang，调查他与涉嫌中国间谍的Megaspeed执行长Alice Huang的关系。此次调查源于上周国会共和党人向Huang发送的传票。
- **原始摘要**: Nvidia CEO Jensen Huang has until the end of the day Wednesday to answer a call from House Republicans for a closed-door briefing on his affair with alleged Chinese spy.

### 5. Silicon Valley Tech Allies Support Jensen Huang
- **来源**: The New York Times Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 17:29:52 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.nytimes.com/2026/11/11/technology/jensen-huang-affair-nvidia-support.html
- **AI 摘要**: 文章讨论了Elon Musk等人对Nvidia首席执行官与一名被怀疑是中国间谍的女人关系的看法，认为这是个人失误而非安全问题。
- **原始摘要**: Elon Musk and other Silicon Valley figures cast the Nvidia chief’s relationship with a woman believed to be a Chinese spy as a personal lapse, not a security failure.

### 6. OpenAI and Georgia county leaders hit with Mafia-style RICO racketeering lawsuit over $30 billion AI data center
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 16:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.tomshardware.com/tech-industry/data-centers/georgia-politicians-openai-slapped-with-racketeering-lawsuit-over-3-2-gigawatt-ai-data-centers-plaintiffs-allege-multiple-violations-were-part-of-a-coordinated-scheme-to-get-project-camellia-approved
- **AI 摘要**: 文章内容涉及OpenAI和佐治亚县领导被指控与30亿美元的AI数据中心有关的黑手党式RICO反组织犯罪诉讼。文章讨论了居民的闭门密谈和保密协议被用于推动‘Project Camellia’计划。
- **原始摘要**: The plaintiffs alleged that the parties committed fraud and concealment through NDAs and misleading public statements.

### 7. Congress could issue subpoena to Nvidia CEO Jensen Huang if he doesn’t respond by today to request for a ‘joint, closed-door briefing’
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 13:04:44 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.tomshardware.com/tech-industry/policy/congress-could-issue-subpoena-to-nvidia-ceo-jensen-huang-if-he-doesnt-respond-by-today-to-request-for-a-joint-closed-door-briefing-us-representatives-want-to-discuss-companys-security-protocols-against-foreign-adversary-espionage
- **AI 摘要**: 本文报道了美国国会议员要求Nvidia CEO进行闭门会议讨论公司安全协议，否则将发出传票。这与军事技术相关。
- **原始摘要**: Three committee chairpersons want to grill Jensen Huang about his company's 'security protocols against foreign adversary espionage,' as a former CIA agent says that he had a target on his back as the...

### 8. Elon Musk wants to build a s $24 billion gas-powered AI supercomputer in Texas company town
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 11:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.tomshardware.com/tech-industry/data-centers/elon-musk-wants-to-build-a-new-gas-powered-data-center-in-starbase-texas-usd24-billion-site-goes-up-for-approval-in-december-but-could-face-headwinds-from-new-governor
- **AI 摘要**: 文章主要描述了Elon Musk计划在德克萨斯公司镇建造一个价值240亿美元的使用天然气的AI超级计算机。该计划在12月获得批准，但可能受到新上任的州长的反对。文章属于时政类别。
- **原始摘要**: The city of Starbase, Texas, is set to vote on a proposed $24 billion data center to be built within its limits, but the SpaceX company town may not provide the friendly regulatory environment that ow...

### 9. Ukrainian drone operations squeezed by fiber optic cable shortage triggered by AI data center buildouts
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 11:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.tomshardware.com/tech-industry/drones/data-center-demand-for-fiber-optics-squeezes-ukrainian-drone-operations-supply-crunch-has-incurred-6x-10x-cost-increase-for-critical-cabling
- **AI 摘要**: 本文提到乌克兰无人机操作因光纤电缆短缺而受到挤压，该短缺由AI数据中心建设引起。Tom's Hardware网站对此进行了报道。文章涉及军事和科技领域。
- **原始摘要**: Ukrainian drone manufacturer BlueBird Tech says that limited fiber optic supplies are making it harder to build jam-proof fiber optic drones.

### 10. United Airlines Blocks AI Agents Like Muse and Instinct From Booking Flights
- **来源**: The Information (TIER3)
- **发布日期**: 2026-11-11T23:28:57Z (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.theinformation.com/briefings/united-airlines-blocks-ai-agents-like-muse-instinct-booking-flights
- **AI 摘要**: 联合航空公司宣布禁止AI助手和代理预订其航班，这是继银行和零售商之后采取的类似措施，原因是隐私问题。
- **原始摘要**: United Airlines said Wednesday it will ban AI agents and assistants from booking its flights, following similar bans by banks and retailers that cited privacy concerns. The ban covers bookings made di...

### 11. Nvidia Board Reportedly Preparing To Oust Nvidia CEO
- **来源**: The Information (TIER3)
- **发布日期**: 2026-11-11T22:47:48Z (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.theinformation.com/briefings/report-nvidia-board-reportedly-preparing-oust-nvidia-ceo
- **AI 摘要**: NVIDIA董事会正在准备将CEO詹森·黄（Jensen Huang）扫地出门，据《华尔街日报》周三报道。董事会一直在调查黄与一位与一家中国公司有恋爱关系的女性的关系，该公司获得了被美国禁止的NVIDIA芯片，并且美国怀疑该公司可能向美国提供信息。
- **原始摘要**: Nvidia’s board is preparing to oust Nvidia CEO Jensen Huang, the Wall Street Journal reported Wednesday. The board has been investigating Huang’s romantic relationship with a woman whose Chinese firm...

### 12. Nvidia prepares to oust Jensen Huang, WSJ reports — stock sinks
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 23:28:11 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-affair-employee.html
- **AI 摘要**: Nvidia CEO Jensen Huang被指控与公司员工Kimberly Powell有婚外情，导致股价下跌。该报道发布在Nvidia承认与一名被怀疑是间谍的女性有婚外情之后。
- **原始摘要**: The report comes days after Huang admitted to an affair with a woman who is believed by U.S. intelligence of being a Chinese spy.

### 13. Brady Says Democrats Control Lame-Duck Funding Timing
- **来源**: Bloomberg Politics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 23:25:19 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/brady-says-democrats-control-lame-duck-funding-timing-video
- **AI 摘要**: 凯文·布拉德表示，民主党在即将到来的跛脚鸭会期中政府资金立法的时机和内容上具有控制权。他预计立法者将延长政府资金，而不是导致政府关闭。布拉德还提到，分裂的政府可能为两党税收政策提供机会，包括恢复可再生能源、儿童和医疗保健税抵免，以及提高对企业和个人的税收。
- **原始摘要**: Kevin Brady, former Republican Congressman from Texas, says Democrats are effectively in control of the timing and content of government funding legislation during the lame-duck session as control of...

### 14. Nvidia board set to meet after revelations Huang had affair with top company executive
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:56:26 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ft.com/content/d3838274-a055-4d5d-a1ff-48f2979a08f0?syn-25a6b1a6=1
- **AI 摘要**: 美国芯片巨头Nvidia的CEO因涉嫌与高级公司执行人员有染而面临巨大压力，即将召开董事会会议。
- **原始摘要**: Head of US chip giant comes under mounting pressure days after claims he had affair with alleged Chinese spy

### 15. Jensen Huang affair in D.C.: Resignation calls and moves to tighten Nvidia China exports
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:46:29 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-congress-resign-ai-chips.html
- **AI 摘要**: 美国总统科技顾问Jensen Huang因涉嫌不当行为引发争议，部分国会议员呼吁他辞职。这一事件可能促使国会推进一系列法案，以加强对中国出口的监管。
- **原始摘要**: Huang was notably opposed to strict export controls on AI chips to China, which ruffled feathers with congressional China hawks.

### 16. Huang Said to Have Had Affair With Nvidia Executive: NYT
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:35:57 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/huang-said-to-have-had-affair-with-nvidia-executive-nyt-video
- **AI 摘要**: Nvidia CEO Jensen Huang与公司健康护理副总裁Kimberly Powell有婚外情的报道被纽约时报披露。
- **原始摘要**: Nvidia CEO Jensen Huang had a relationship with Kimberly Powell, Nvidia’s vice president of health care, according to the New York Times. Michael Shepard has more on "Balance of Power: Evening Edition...

### 17. Big Take: Huang's Scandal Will Push Democrats on US-China Policy
- **来源**: Bloomberg Politics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:31:58 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/huang-s-scandal-will-push-dems-on-us-china-policy-video
- **AI 摘要**: 本文讨论了Huang的丑闻将如何推动民主党在中美政策上的立场变化。这与军事技术、经济和时政等主题无关，应归类为时政。
- **原始摘要**: Today’s Big Take podcast digs into the geopolitical legacy President Trump is trying to cement in his final two years in office, even as a new majority Democratic Congress aims to rein him in on trade...

### 18. Jensen Huang Said to Have Had Relationship With Nvidia Executive Who Reports to Him
- **来源**: The New York Times HomePage (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:27:54 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.nytimes.com/2026/11/11/technology/jensen-huang-nvidia-affair.html
- **AI 摘要**: Nvidia首席执行官黄仁勋因与一名中国商界女性的关系而受到美国情报机构认定为中共间谍的调查。
- **原始摘要**: Mr. Huang, Nvidia’s chief executive, is already facing scrutiny over an affair with a Chinese businesswoman who U.S. intelligence determined was a Chinese spy.

### 19. Ukraine peace talks end with prisoner swap but no breakthrough
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 21:09:30 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ft.com/content/39254048-0d84-47b8-bb97-4b9d9e1f2b92?syn-25a6b1a6=1
- **AI 摘要**: 乌克兰和平谈判结束，焦点在于战后安全保障协议，未取得突破。
- **原始摘要**: Discussions involving Kyiv as well as Russia and the US focus on postwar security guarantees

### 20. Huang's Ties to Trump Under Scrutiny After Spy Claim
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 20:12:39 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/huang-s-ties-to-trump-under-scrutiny-after-spy-claim-video
- **AI 摘要**: 特朗普政府和英伟达CEO黄仁勋的行为在国会的调查中受到了更多关注，因为有报道称黄仁勋与一名被指为中国的间谍女性有关系。特朗普曾否认他了解黄仁勋与这名女性的关系可能带来的国家安全风险，但最近的《纽约时报》报道显示，特朗普在早些时候的中国之行前曾被告知过这种风险。
- **原始摘要**: Bloomberg's Mike Shepard said that actions taken by the Trump administration and by Nvidia CEO Jensen Huang are coming under sharper scrutiny by Congress amid investigations into the affair Huang had...

### 21. Rubenstein on the Anthropic IPO, Nvidia CEO Scandal
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 19:53:18 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/rubenstein-on-the-anthropic-ipo-nvidia-ceo-scandal-video
- **AI 摘要**: 大卫·鲁宾斯坦讨论了Anthropic的IPO以及英伟达CEO詹森·黄的丑闻。他预计Anthropic的估值将达到1.3万亿美元，并认为黄将继续担任英伟达的领导。他还谈到了即将推出的《侠盗猎车手》VI。
- **原始摘要**: Carlyle Group co-Chairman and Bloomberg Host David Rubenstein talks about the anticipated initial public offering of Anthropic and the scandal involving Nvidia CEO Jensen Huang. He expects the Anthrop...

### 22. Expect ‘Dislocations’ in AI Investment Cycle: Waxman
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 19:36:20 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/expect-dislocations-in-ai-investment-cycle-waxman-video
- **AI 摘要**: 文章讨论了Alan Waxman对AI市场的看法，他提到了市场中的不稳定性。
- **原始摘要**: Alan Waxman, CEO and co-founder of Sixth Street, joins Dani Burger on “Bloomberg Deals.” They discuss dislocations he is seeing in the AI market. (Source: Bloomberg)

### 23. Inside Ken Griffin's Miami
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 15:57:11 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ft.com/video/d3756827-8b64-48af-a8fb-727788b8d8fb?syn-25a6b1a6=1
- **AI 摘要**: 文章主要介绍了FT记者对肯·格里芬在迈阿密如何利用财富影响城市发展的访问。文章主题偏向于时政领域，涉及富豪如何影响城市政策和规划。
- **原始摘要**: The FT's Jill Shah visits Miami to see what happens when a billionaire uses his fortune to shape a city

### 24. Thousands of schools in Italy, Scotland and Ireland receive bomb threats
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 15:39:44 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ft.com/content/7bbc0a5e-b7e2-4a3f-874f-a63de94e922d?syn-25a6b1a6=1
- **AI 摘要**: 意大利、苏格兰和爱尔兰的数千所学校遭遇爆炸威胁，这似乎是旨在扰乱欧洲生活的最新协调攻击。
- **原始摘要**: Incidents appear to be latest co-ordinated attack aimed at disrupting life in Europe

### 25. RAF Fairford incident partly directed from New York jail, US claims
- **来源**: Financial Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 14:14:04 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ft.com/content/687acbbb-6296-4030-a1a0-c07936a6c9db?syn-25a6b1a6=1
- **AI 摘要**: 美国指控称，一架英国空军基地可能遭攻击的阴谋与针对欧洲犹太人场所的更大运动有关。美国指控称，部分阴谋策划可能来自纽约监狱。
- **原始摘要**: US indictment links alleged plot to attack British air base to wider campaign across Europe targeting Jewish sites

### 26. Nvidia's Huang tries to project 'business as usual' in return to office after affair revelation
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 13:46:59 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.cnbc.com/2026/11/10/nvidia-jensen-huang-affair-office.html
- **AI 摘要**: 英伟达CEO Jensen Huang在承认婚外情后返回办公室，公司内部表示情绪低落。英伟达董事会正在调查此事。
- **原始摘要**: Nvidia employees described the mood as "sad" as CEO Jensen Huang returned to the office after disclosing an affair.

### 27. Nissan cuts sales forecast again on China woes as CEO outlines plan to fight back
- **来源**: CNBC World News (TIER3)
- **发布日期**: Wed, 11 Nov 2026 13:18:48 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.cnbc.com/2026/11/11/nissan-sales-forecast-earnings-china.html
- **AI 摘要**: 日产汽车在华销量预期下调，日产汽车CEO表示正在开发专为中国消费者设计的车辆，并计划通过改进电动车和加大美国、日本市场的结构调整来应对竞争。
- **原始摘要**: Intensifying competition in the world's largest auto market forced Nissan to cut its annual sales forecast for a second time in months.

### 28. A Museum’s ‘Wanted’ Poster Campaign Brings Looted Painting Back to France
- **来源**: The New York Times World (TIER3)
- **发布日期**: Wed, 11 Nov 2026 10:03:50 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.nytimes.com/2026/11/11/world/europe/france-art-wanted-poster.html
- **AI 摘要**: 奥尔良艺术博物馆正在发起一项寻回二战期间被盗艺术品的活动，并希望公众协助。
- **原始摘要**: The Orléans Fine Arts Museum is on a quest to recover hundreds of works stolen during World War II — and the director wants your help.

### 29. U.S., China should ‘harbor no illusions’ as they cooperate, compete on AI, Bessent says
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 05:15:50 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.cnbc.com/2026/11/11/trump-xi-summit-ai-nvidia-.html
- **AI 摘要**: 美国和中国在人工智能领域需要在竞争和领导责任之间找到平衡，但目前尚未做出限制AI发展的承诺。
- **原始摘要**: During Xi's September visit, Washington and Beijing agreed to launch an AI dialogue with a communications channel to help defuse serious incidents.

### 30. European sanctions office, EU mistakes, visa rules in Moldova: Russian MFA briefing
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 23:52:31 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216613
- **AI 摘要**: 文章内容主要涉及俄罗斯外长就欧盟制裁办公室、签证规则等问题的表态，与机器人、机械臂、人形机器人、运动控制、操作/抓取、导航、自动驾驶、具身智能、AI芯片、编译器、光计算、军事技术、经济、时政等主题均无直接关联。
- **原始摘要**: Spokeswoman Maria Zakharova said that the OSCE is becoming complicit in the Kiev regime’s information campaign to conceal the true nature and scale of crimes against individuals, including by remainin...

### 31. Houthis carry out strikes on Riyadh Airport, deny attack on Mecca — spokesman
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 23:27:29 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216611
- **AI 摘要**: 塔斯社消息，也门胡塞武装否认在麦加空域拦截无人机，称在沙特首都麦加附近机场和Yanbu附近油库附近发动了袭击。胡塞武装发言人表示，武装部队（胡塞武装）使用了三枚巡航导弹袭击了沙特首都麦加的国王卡利卜国际机场，并在Yanbu地区对第11号泵站发动了无人机袭击。
- **原始摘要**: Yahya Saree confirmed an attack on oil infrastructure near the city of Yanbu

### 32. Putin-Trump meeting, European officials’ presence in Abu Dhabi: Kremlin aide’s statements
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 23:03:33 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216609
- **AI 摘要**: 俄罗斯政治与外交消息。俄罗斯总统普京和美国前总统特朗普的会面计划在APEC峰会上进行。俄罗斯克里姆林宫顾问尤里·乌沙科夫表示，欧洲官员在阿布扎比与乌克兰和美国方面进行了幕后工作。
- **原始摘要**: Yury Ushakov has said that a bilateral meeting between the Russian and US presidents at the APEC summit is being planned

### 33. NATO 2027 summit in Albania unlikely to be held as planned — defense minister
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 22:30:55 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216605
- **AI 摘要**: 阿尔巴尼亚国防部长表示，2027年北约峰会可能被取消或以不同的形式举行，如虚拟会议。原计划在2027年7月在阿尔巴尼亚举行峰会，但由于该国是北约最低国防开支的国家，北约总部对此表示担忧。
- **原始摘要**: Instead, NATO could hold "a flexible meeting," with leaders free to decide whether to attend, or "even a virtual summit," Ermal Nufi said

### 34. Canada against Russian presence at 2026 IIHF Junior World Championship
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 22:23:55 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/sports/2216603
- **AI 摘要**: 加拿大政府表示，将不会为2026年IIHF青年世界锦标赛中的俄罗斯球员发放签证。加拿大政府已经通知了国家冰球协会和国际冰球联合会，他们不会为俄罗斯球员发放签证。
- **原始摘要**: The Canadian authorities informed the country’s hockey association and the International Ice Hockey Federation that they will not issue visas to Russian players

### 35. CSTO leaders adopt Counterterrorism Strategy through 2030
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 22:14:13 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216599
- **AI 摘要**: 俄罗斯集体安全条约组织(CSTO)领导人通过了2030年前的反恐战略。该战略由俄罗斯倡议起草，并在集体安全理事会的最终声明和关于反恐合作的声明中得到了体现。
- **原始摘要**: In addition, the common approaches of the organization’s member states were set forth in the final Declaration of the Collective Security Council, as well as in statements on cooperation in the field...

### 36. EU leaders to consider assigning Russia negotiator at Dublin summit — media
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 21:43:19 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216595
- **AI 摘要**: 欧盟领导人将在11月13日的都柏林紧急峰会上讨论任命一名代表欧盟参与乌克兰和平进程的人员。目前，欧盟领导人正在讨论该角色的结构和职责。
- **原始摘要**: According to the source, this would be an initial debate about the structure and mandate of the role

### 37. No technical difficulties preventing ISS operation after 2030 — NASA
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 21:33:27 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/science/2216591
- **AI 摘要**: 文章主要讨论了国际空间站（ISS）的未来运营问题，NASA表示目前没有技术障碍阻止ISS在2030年后继续运行。文章内容与军事技术无关。
- **原始摘要**: In late October, Roscosmos head Dmitry Bakanov told reporters that the ISS could be decommissioned in 2031 or 2032

### 38. Armenian president signs Trump Route agreement
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 21:31:27 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216589
- **AI 摘要**: 亚美尼亚总统Vahagn Khachaturyan签署了与美国关于特朗普路线项目的战略合作协议。该项目旨在促进国际和平与繁荣。
- **原始摘要**: Vahagn Khachaturyan signed the law on November 10

### 39. Iran could mediate between Saudi Arabia, Houthis — parliament speaker
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 21:20:01 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216585
- **AI 摘要**: 伊朗议会议长表示，如果被要求，伊朗愿意帮助沙特和也门叛军胡塞组织解决冲突。议会议长强调，不应干涉也门内部事务，也门人应该自己解决分歧。
- **原始摘要**: Mohammad Bagher Ghalibaf stressed that "no one should interfere in Yemen’s internal affairs, and Yemenis must resolve their differences themselves"

### 40. Situation in special op zone significantly changed since Anchorage meeting — Shoigu
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 21:16:38 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216581
- **AI 摘要**: 俄罗斯安全委员会秘书绍伊古表示，自8月在安克雷奇与美国总统唐纳德·特朗普会面以来，特别军事行动区的情况发生了显著变化。绍伊古称，前线观察者可以轻松地将任何地图（美国、乌克兰或其他地图）与会面后的状况进行比较，以看到情况的变化。他强调，自那以来，情况发生了显著变化，并且每天都在变化。
- **原始摘要**: The Russian Security Council Secretary added that Russian forces are advancing every day

### 41. House Passes Sweeping TCAVA Veterans Benefits Bill Despite Disability Pay Concerns
- **来源**: Military.com (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 21:09:09 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.military.com/house-passes-sweeping-veterans-benefits-bill-despite-disability-pay-concerns
- **AI 摘要**: 美国众议院在11月11日的退伍军人节上通过了一项涵盖广泛退伍军人福利法案，尽管有关未来残疾支付的担忧存在。
- **原始摘要**: The House passed a sweeping veterans benefits bill on Veterans Day, advancing expanded benefits despite concerns over future disability payments.

### 42. Iran to hit US bases in Europe if attacks come from there — Security Council secretary
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 20:46:44 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216573
- **AI 摘要**: 伊朗表示，如果美国飞机从欧洲的未被攻击的军事基地起飞对伊朗发动攻击，伊朗将对这些基地进行打击。伊朗国家安全委员会秘书长Mohsen Rezaei警告美国政府不要犯错。
- **原始摘要**: Mohsen Rezaei mentioned American military bases located in remote regions that have not yet been attacked

### 43. Armenia loses voting rights in CSTO over debt obligations: what we know
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 20:44:02 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216569
- **AI 摘要**: 俄罗斯媒体TASS报道，阿塞拜疆和哈萨克斯坦等国在莫斯科举行的CSTO峰会上决定剥夺亚美尼亚的投票权，亚美尼亚也将失去在该组织中提名代表的能力。亚美尼亚总理诺尼·帕西尼扬此前表示亚美尼亚对参与CSTO失去兴趣。
- **原始摘要**: According to Russian Presidential Spokesman Dmitry Peskov, Armenian Prime Minister Nikol Pashinyan has previously "repeatedly stated that Armenia has lost interest in participating in the CSTO"

### 44. Lavrov comments on US envoys’ upcoming Moscow visit following Abu Dhabi talks
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 20:37:36 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216563
- **AI 摘要**: 俄罗斯外长在阿布扎比与俄美乌三方会谈后表示，美国代表团将前往莫斯科向普京汇报会谈情况，以决定下一步行动。
- **原始摘要**: The Russian foreign minister said the trilateral format of negotiations on Ukraine is the most justified under the current conditions

### 45. Iran, Oman reach understanding on Hormuz shipping routes — Iranian parliament speaker
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 20:30:37 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216559
- **AI 摘要**: 伊朗和阿曼就霍尔木兹海峡的航运路线和交通分离方案达成共识，伊朗议会议长表示，霍尔木兹海峡的现状不会恢复到战争前的状态。
- **原始摘要**: Mohammad Bagher Ghalibaf added that the status of the Strait of Hormuz "will not return to what it was before the war"

### 46. Putin, Japarov discuss investment cooperation
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 20:25:38 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/economy/2216557
- **AI 摘要**: 俄罗斯总统普京与吉尔吉斯斯坦总统萨德尔·贾帕罗夫讨论了两国之间的投资合作。俄罗斯是吉尔吉斯斯坦的主要贸易和经济伙伴，两国的贸易额在过去一年中增长了超过25%。
- **原始摘要**: The Russian leader noted that the trade turnover is on the rise

### 47. Gazprom, Srbijagas discussed gas supplies continuation
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 19:50:49 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/economy/2216545
- **AI 摘要**: 这篇文章讨论了Gazprom和Srbijagas公司关于天然气供应的讨论，属于国际政治和外交领域。
- **原始摘要**: The parties discussed cooperation in the gas sphere

### 48. CSTO Collective Forces combat training, fight against epidemics: Putin’ statements
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 19:45:14 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216535
- **AI 摘要**: 俄罗斯总统普京在CSTO集体安全理事会会议上表示，2027年将对CSTO具有重要意义，因为该组织将在同年庆祝成立两周年。普京强调了在俄罗斯担任主席期间对CSTO集体力量的战斗训练发展给予的关注，并指出需要缔结关于联合快速应对流行病威胁的协议。
- **原始摘要**: The year 2027 will be significant for the CSTO, as the association will celebrate two anniversaries at once, the Russian president noted

### 49. Zimbabwe seeks after full-fledged membership in BRICS — Foreign Minister
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 19:36:45 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216531
- **AI 摘要**: 津巴布韦希望成为BRICS的正式成员，并已获得BRICS新开发银行的借款成员资格。津巴布韦外长表示，成为全球金融架构的一部分对融入全球经济非常重要。
- **原始摘要**: Zimbabwe has already secured its admission to the BRICS New Development Bank as a borrowing member

### 50. Russian ambassador to US Alexander Darchiev dies — Foreign Ministry
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 19:25:24 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216529
- **AI 摘要**: 俄罗斯驻美国大使亚历山大·达契夫去世，享年66岁。俄罗斯外交部表示，达契夫大使在11月11日突然去世。
- **原始摘要**: Alexander Darchiev was 66 years old

### 51. Tehran grateful for historic stance taken by Russia, China at UN Security Council
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:42:47 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216511
- **AI 摘要**: 伊朗感谢俄罗斯和中国的联合国安全理事会立场，认为这是对美国单方面行动的国际法背景下具有历史意义的立场。伊朗感谢俄罗斯的支持。
- **原始摘要**: Minister-Counselor at the Iranian Embassy in Russia Afshin Parchizadeh said that "even European countries did not support military aggression against Iran"

### 52. Proposal to transport enriched uranium from Iran to Russia remains on table — diplomat
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:29:17 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216499
- **AI 摘要**: 俄罗斯外长发言人表示，俄罗斯提议将伊朗浓缩铀转移到俄罗斯领土进行稀释，这一提议仍然在讨论之中。俄罗斯方面表示，他们有必要的技术和经验。
- **原始摘要**: Russia proposed transferring Iranian enriched uranium to Russian territory for 'dilution,' Maria Zakharova reminded

### 53. Honor the Fallen Service Members of the Iran War
- **来源**: Military.com (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:25:57 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.military.com/deployment/honor-fallen-of-operation-epic-fury.html
- **AI 摘要**: 本文列出了在伊朗战争期间因Operation Epic Fury和后续海外行动中死亡的美国军事人员名单。
- **原始摘要**: Here is a list of the confirmed deaths of U.S. military service members who have died in the Iran war.

### 54. CSTO concerned over foreign military infrastructure expansion to its borders — declaration
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:23:44 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216493
- **AI 摘要**: 俄罗斯安全组织联盟（CSTO）表示担忧，一些国家在其他军事联盟和联盟中的军事基础设施扩张可能威胁到联盟的安全。
- **原始摘要**: The CSTO member states highlighted that creating threats to collective security is unacceptable

### 55. Putin to meet with US presidential envoys tomorrow morning — Kremlin aide
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:14:59 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216487
- **AI 摘要**: 俄罗斯总统普京将于11月12日早与美国特使会面，会议将遵循常规程序。
- **原始摘要**: Yury Ushakov stressed that, in terms of protocol, the meeting will proceed "as usual"

### 56. Armenia deprived of voting rights in CSTO over unpaid debts
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:13:39 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216471
- **AI 摘要**: 亚美尼亚因未支付债务被集体安全条约组织剥夺了投票权。集体安全理事会通过了针对亚美尼亚的‘关于应用集体安全条约组织宪章第25条的决定’。
- **原始摘要**: The Collective Security Council adopted the "decision on the application of Article 25 of the Charter of the Collective Security Treaty Organization with respect to the Republic of Armenia"

### 57. 60 Plus Veterans Bills Could Expand Benefits for Millions as Congress Weighs Benefits Package
- **来源**: Military.com (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:07:46 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.military.com/60-plus-veterans-bills-could-expand-benefits-for-millions-as-congress-weighs-benefits-package
- **AI 摘要**: 美国国会正在考虑一项新的法案，旨在扩大60岁以上退伍军人的福利范围，包括伤残退伍军人、金星家庭和丧偶配偶。这项法案被称为‘爱永存法案’，旨在消除丧偶军人配偶的‘再婚惩罚’。
- **原始摘要**: More than 60 veterans bills could expand benefits for combat-injured veterans, Gold Star families and surviving spouses.

### 58. Putin points to importance of CSTO Collective Forces’ combat training
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:07:00 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216467
- **AI 摘要**: 俄罗斯总统普京在CSTO集体安全理事会会议上强调了2026年俄罗斯主席国期间对CSTO集体安全系统作战训练的重视。
- **原始摘要**: The Russian president emphasized that a series of large-scale joint exercises had recently been conducted in Belarus, Kazakhstan, Tajikistan, and Russia

### 59. Senior US Soldier Based at NATO Headquarters Arrested on Suspicion of Helping Russia
- **来源**: Military.com (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:05:19 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.military.com/senior-us-soldier-based-at-a-nato-headquarters-is-arrested-on-suspicion-of-helping-russia
- **AI 摘要**: 一名被派往英国北约总部的美国陆军高级士兵在周二被逮捕，警方和FBI正在调查他与俄罗斯的联系。这名士兵被英国的国家安全法拘留。
- **原始摘要**: A U.S. Army soldier at Imjin Barracks in England is held under Britain's National Security Act as police and the FBI probe alleged Russia ties.

### 60. Lukashenko calls for boosting CSTO military potential
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:03:19 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216461
- **AI 摘要**: 白俄罗斯总统卢卡申科在 CSTO 集体安全理事会会议上表示，应加强 CSTO 的军事能力，以确保集体安全。他支持今天将要采取的决定，包括加强移动防空单位以支持 CSTO 部队以及改善集体空军。
- **原始摘要**: The Belarusian president said that CSTO members must continually adapt the military mechanisms the organization has developed to ensure collective security, taking into account present-day realities a...

### 61. CSTO summit makes decision to deprive Armenia of voting right
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:00:52 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216451
- **AI 摘要**: 俄罗斯 CSTO 峰会决定剥夺亚美尼亚的投票权，因为亚美尼亚多年未履行承诺。
- **原始摘要**: Russian Presidential Spokesman Dmitry Peskov recalled that Armenia had not been honoring its commitments for several years now

### 62. Putin describes global epidemiological situation as tough
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:48:06 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216419
- **AI 摘要**: 文章内容与俄罗斯总统普京关于全球公共卫生状况的描述相关，未涉及AI模型、芯片、编译器、光计算、军事技术、经济、时政等具体类别，因此应归类为时政。
- **原始摘要**: In some regions of the world there are seemingly prosperous countries, but problems still arise there, the Russian leader said

### 63. US Charges 3 Men With Plotting Terror Attacks, Including Planned Assault on UK Air Base
- **来源**: Military.com (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:45:29 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.military.com/us-charges-3-men-with-plotting-terror-attacks-including-planned-assault-on-uk-air-base
- **AI 摘要**: 美国指控3名男子策划恐怖袭击，其中包括计划袭击英国空军基地的行动。被定罪的男子曾试图将秘密信息传递给伊朗策划者。
- **原始摘要**: A man jailed on terrorism charges was able to pass secret messages to Iranian operatives planning an attack on a British air base.

### 64. Lukashenko believes CSTO could become military-political foundation of Eurasian charter
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:40:21 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216403
- **AI 摘要**: 白俄罗斯总统卢卡申科认为，集体安全条约组织（CSTO）可以成为21世纪欧亚宪章的军事政治基础。卢卡申科表示，该组织在确保安全和稳定方面具有巨大的、未被充分利用的潜力。
- **原始摘要**: According to the Belarusian president, the organization possesses enormous potential in the field of ensuring security and stability

### 65. Parties move closer to peace following talks in Abu Dhabi — Russian delegation head
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:30:19 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216381
- **AI 摘要**: 俄罗斯和乌克兰在阿布扎比的会谈使双方更接近和平。俄罗斯总统顾问Vladimir Medinsky表示，所有目标都将实现，但取决于乌克兰、美国和欧洲的态度。
- **原始摘要**: Vladimir Medinsky said that all the objectives will be achieved

### 66. All parties positively assess UAE meetings — Lavrov
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:22:51 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216365
- **AI 摘要**: 俄罗斯外长表示，俄罗斯、美国和乌克兰在阿布扎比的会谈中，各方都相对积极地评价了这次会谈。俄罗斯外长指出，只有乌克兰总统泽连斯基在‘玩自己的游戏’。尽管如此，泽连斯基的代表团在会谈中表现得更专注于实质内容。
- **原始摘要**: The Russian foreign minister said that only Vladimir Zelensky is "playing his own games"

### 67. Large-scale prisoner swap, security: chief Russian negotiator speaks after Abu Dhabi
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:21:11 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216361
- **AI 摘要**: 俄罗斯总统顾问在阿布扎比举行的会谈中表示，俄罗斯和乌克兰就大规模囚犯交换达成一致，交换细节将在不久后公布。俄罗斯总统顾问还提到，欧洲安全系统是会谈中的一个关键议题，各方在某些条款上达成了一致。
- **原始摘要**: As a rule, Russia doesn't discuss the details of negotiations until an agreement is reached, Vladimir Medinsky said

### 68. IN BRIEF: What to know about Witkoff and Kushner coming to Moscow
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:14:43 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216359
- **AI 摘要**: 这篇文章讨论了美国特使Jared Kushner和美国特别特使Steve Witkoff计划访问莫斯科的消息，以及俄罗斯总统发言人和俄罗斯总统助理的回应。这与军事装备、武器系统、国防、军队或军事行动无关，也不涉及AI技术。因此，最合适的类别是时政。
- **原始摘要**: The US envoy said he will travel to Moscow together with the US special envoy on November 12

### 69. Putin to determine next steps after US envoys brief him on Abu Dhabi talks — Lavrov
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:08:50 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216351
- **AI 摘要**: 俄罗斯外长拉夫罗夫表示，美国总统特使将在11月12日访问莫斯科，向俄罗斯总统普京通报阿布扎比会谈的情况。普京将根据特使通报的内容决定俄罗斯的下一步行动。
- **原始摘要**: US envoy Jared Kushner said earlier that he and US Special Presidential Envoy Steve Witkoff planned to travel to Moscow on November 12

### 70. Kremlin spokesman addresses potential for Russia-EU talks on Ukraine, Eurasian security
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:05:57 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216343
- **AI 摘要**: 俄罗斯总统尚未收到俄罗斯代表团在阿布扎比三边谈判结果的全面报告，克里姆林宫发言人表示，俄罗斯与欧洲讨论乌克兰冲突的格式尚不清楚。同时，俄罗斯总统普京强调，欧亚安全在集体安全条约组织（CSTO）峰会上一直是讨论的主题。
- **原始摘要**: Russian President Vladimir Putin has not yet received a comprehensive report from the Russian delegation on the outcomes of the trilateral negotiations on the Ukrainian settlement in Abu Dhabi, Dmitry...

### 71. Ukrainian conflict settlement to feature on agenda of 2026 APEC Summit in China — Kremlin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 17:02:15 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216341
- **AI 摘要**: 俄罗斯表示，2026年APEC峰会期间，乌克兰冲突的解决将被纳入议程。俄罗斯总统发言人表示，俄罗斯、美国和乌克兰在阿布扎比举行的三方会谈的结果不会影响俄总统普京与美国总统之间的双边会谈。
- **原始摘要**: Russia, the United States and Ukraine held talks in Abu Dhabi on November 10-11

### 72. Post-Soviet security bloc’ summit to address global security — Putin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:52:17 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216327
- **AI 摘要**: 俄罗斯总统普京表示，俄罗斯作为当前的CSTO主席，与所有成员国协商后为CSTO会议准备了议程，重点讨论了全球和区域安全问题。
- **原始摘要**: As the current CSTO chair, Russia has prepared an agenda for the meeting in consultation with all member states, the Russian president said

### 73. Thailand backs Russia’s bid for APEC chairmanship — MFA
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:50:03 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216325
- **AI 摘要**: 泰国支持俄罗斯担任APEC主席国的消息。俄罗斯外交部长助理表示，泰国加入支持俄罗斯的国家行列，包括中国、越南和印度尼西亚。泰国的支持有助于加强俄罗斯的候选地位。
- **原始摘要**: Marat Berdiyev said that he welcome this news

### 74. Russia works successfully with CSTO to counter international terrorism — official
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:45:18 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216319
- **AI 摘要**: 俄罗斯与 CSTO 成员国成功合作，对抗国际恐怖主义。俄罗斯外长助理指出，国际恐怖主义仍然是国家安全的主要威胁。俄罗斯与 CSTO 成员国的合作有助于协调各自立场，防止恐怖袭击。
- **原始摘要**: Pyotr Ilyichev noted that international terrorism "remains the main threat to state security"

### 75. Foundation laid for further work after trilateral talks on Ukraine in Abu Dhabi — diplomat
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:41:27 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216315
- **AI 摘要**: 俄罗斯、美国和乌克兰在阿布扎比举行的三方会谈上达成了一些共识，俄罗斯副外长表示，这为未来的工作奠定了基础。
- **原始摘要**: Russia, the United States and Ukraine held talks in Abu Dhabi on November 10-11

### 76. Kushner says EU should choose one person to speak for it at Ukraine table
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:28:00 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216303
- **AI 摘要**: 美国总统顾问Jared Kushner认为，欧洲应该选择一个代表来在乌克兰谈判桌上发言，以减少欧洲内部的复杂性。他指出，欧洲是一个多样化的群体，具有不同的性格、观点和利益。
- **原始摘要**: The complexity of the situation lies in the fact that "Europe is a very diverse mix of a lot of different personalities and perspectives and interests," Jared Kushner explained

### 77. Raymond Weeks: The Birmingham Veteran Who Pushed for a Day for All Veterans
- **来源**: Military.com (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:22:34 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.military.com/the-birmingham-veteran-who-pushed-for-a-day-for-all-veterans
- **AI 摘要**: 文章讲述了Raymond Weeks，一位二战老兵，他在1946年向艾森豪威尔将军提出设立“全国退伍军人纪念日”的计划，并在1947年，伯明翰市举办了第一届。最终，11月11日被定为全国退伍军人纪念日，即今天的退伍军人节。文章没有涉及AI技术相关内容。
- **原始摘要**: Raymond Weeks, a World War II veteran, took a plan for “National Veterans Day” to Gen. Eisenhower in 1946.

### 78. United Nations' War Crimes Findings Could Test US Military Aid to Israel
- **来源**: Military.com (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:58:27 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.military.com/united-nations-war-crimes-findings-could-test-us-military-aid-to-israel
- **AI 摘要**: 联合国对以色列军队在加沙战争中犯有战争罪的调查结果可能加强美国向以色列提供武器的挑战，并可能在国际法庭上受到质疑。
- **原始摘要**: A UN commission's Gaza war crimes findings could bolster challenges to US military aid to Israel under Leahy laws and in international courts.

### 79. Russian Foreign Minister to visit Abu Dhabi on November 12-14 to attend forum
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:54:14 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216271
- **AI 摘要**: 俄罗斯外长将于11月12日至14日访问阿联酋首都阿布扎比，参加和平与安全国际论坛。
- **原始摘要**: According to Maria Zakharova, Sergey Lavrov is expected to hold meetings with UAE officials on the sidelines of the event

### 80. Three challenges identified for digital trade development by 2036 — X5 Vice President
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:47:59 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/economy/2216267
- **AI 摘要**: 文章讨论了2036年数字贸易发展的三个关键挑战，包括在互联网中断期间确保数字平台的稳健运行、规范人工智能的使用以及确定机器人的责任。这与军事技术无关。
- **原始摘要**: Boris Ogarkov noted that the industry needs to jointly seek solutions that will avoid stifling the development of new technologies while preventing their uncontrolled deployment

### 81. Veterans' Groups Seek Hegseth Impeachment Even if He Resigns
- **来源**: Military.com (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:45:11 GMT (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://www.military.com/veterans-groups-seek-hegseth-impeachment-even-if-he-resigns
- **AI 摘要**: 退役军人团体要求国防部长彼得·赫格斯（Pete Hegseth）即使辞职或被解雇也应被弹劾，指控他在伊朗战争和海上打击行动中的行为。
- **原始摘要**: Veterans' groups want Defense Secretary Pete Hegseth impeached over the Iran war and strikes at sea. Here are the laws and precedent involved.

### 82. US envoys to visit Moscow on November 12
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:45:00 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216265
- **AI 摘要**: 美国特使Jared Kushner和Steve Witkoff计划于11月12日访问莫斯科，与俄罗斯总统普京会面讨论乌克兰问题。
- **原始摘要**: Jared Kushner and Steve Witkoff intend to hold meeting with Russian President Vladimir Putin

### 83. Russian troops liberate two communities in Ukraine operation over past day — top brass
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:36:51 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216261
- **AI 摘要**: 俄罗斯军队在乌克兰特别军事行动中解放了两个社区，分别是顿涅茨克人民共和国的希洛夫卡镇和扎波罗热地区的复活节镇。
- **原始摘要**: Units of Russia's Battlegroup Center liberated the settlement of Shilovka in the DPR and servicemen of the Battlegroup East liberated the settlement of Voskresenka in the Zaporozhye Region through dec...

### 84. Armenia is not participating in CSTO’s work, response to follow — Kremlin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:35:37 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216263
- **AI 摘要**: 俄罗斯克里姆林宫发言人表示，亚美尼亚尚未参与CSTO活动，该组织将对此作出相应回应。发言人指出，亚美尼亚总理尼古拉·帕希扬曾表示亚美尼亚已失去参与CSTO的兴趣，且亚美尼亚尚未提出退出请求。
- **原始摘要**: Dmitry Peskov added that Yerevan hasn't initiated the withdrawal process

### 85. Ban on Russian grain transit shouldn't cancel existing deals — Latvian PM
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:32:05 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216259
- **AI 摘要**: 拉脱维亚总理安德里斯·库尔克尔斯表示，如果禁止俄粮食过境，不应影响已经达成的合同。他指出，这些合同涉及的粮食属于国际贸易商，包括美国、瑞士、丹麦和阿联酋的企业。库尔斯基表示，如果禁止过境，将导致拉脱维亚在法律诉讼中败诉，并需支付赔偿。
- **原始摘要**: According to Andris Kulbergs, halting the fulfillment of active contracts would lead to legal proceedings that Latvia would lose, forcing it to pay compensation

### 86. Russia-Ukraine prisoner exchange to be one of largest POW swaps — general Zorin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:22:55 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216245
- **AI 摘要**: 俄罗斯国防官员称，与乌克兰的囚犯交换将是一次大型的战俘交换，但具体数字尚未确定。此次交换可能成为战俘交换中最大的一次。
- **原始摘要**: Lieutenant General Alexander Zorin added that the sides had not come to any specific figure yet, because the procedure requires approval

### 87. Putin open to contacts with Europeans including Merz — Kremlin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:21:16 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216239
- **AI 摘要**: 俄罗斯总统普京对与欧洲代表，特别是德国总理默茨的接触持开放态度。此前，默茨表示，他不会回避在G20峰会上与普京的对话。
- **原始摘要**: Earlier, the German chancellor said that he would not shy away from a conversation with Putin on the sidelines of the G20 summit in Miami

### 88. North-South Corridor called to drive trade, investments in Eurasia — Lavrov
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:19:36 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216237
- **AI 摘要**: 俄罗斯外长拉夫罗夫表示，需要新的路线来促进俄罗斯与外国国家之间的货运运输，他提到了北南国际运输走廊的发展，该走廊可以加强外国贸易关系，并释放欧亚国家的经济潜力。
- **原始摘要**: Amid ongoing changes to the global logistics map, there is a growing need for new routes to carry out freight transportation between Russia and foreign states, the top Russian diplomat noted

### 89. No request from Oslo for another phone call with Putin — Kremlin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:17:58 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216243
- **AI 摘要**: 挪威首相Jonas Gahr Store表示可能与俄罗斯总统普京进行电话交谈，但俄罗斯方面表示并未收到挪威方面的请求。
- **原始摘要**: Earlier, the Norwegian PM did not rule out another conversation with the Russian leader

### 90. Putin to hold talks with US envoys Witkoff, Kushner soon — Kremlin aide
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:15:03 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216231
- **AI 摘要**: 俄罗斯总统普京将与美国特使Steve Witkoff和Jared Kushner很快会面，俄罗斯总统助理尤里·乌沙科夫表示，他们可能会访问莫斯科。
- **原始摘要**: Commenting on Jared Kushner’s remark about plans to travel to Moscow following trilateral talks with Russia and Ukraine in Abu Dhabi, Yury Ushakov said that he did not rule out that they will visit Mo...

### 91. Russia, Ukraine may exchange POWs in next two-three weeks — general Zorin
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:06:52 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216219
- **AI 摘要**: 俄罗斯和乌克兰可能在接下来的两周内交换战俘，俄罗斯副参谋长阿列克谢·佐林表示，这取决于交换程序的所有相关问题达成一致。
- **原始摘要**: Lieutenant General Alexander Zorin believes that it will happen after all the issues related to the swap procedure are agreed upon

### 92. Russia thanks US envoys for helping facilitate talks on Ukraine settlement in Abu Dhabi
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 14:57:20 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216205
- **AI 摘要**: 俄罗斯感谢美国特使在阿布扎比推动乌克兰和解会议中的积极作用。俄罗斯总统助理表示，俄罗斯对美国特使Steve Witkoff和Jared Kushner在调解乌克兰冲突中的角色表示积极评价。
- **原始摘要**: Russian Presidential Aide Vladimir Medinsky said that Moscow positively evaluates the role of Steve Witkoff and Jared Kushner

### 93. Moscow, Chengdu Technology Zone to form partnership — minister
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 14:56:45 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/economy/2216181
- **AI 摘要**: 俄罗斯莫斯科政府与成都高新区达成合作意向，莫斯科政府表示愿意为这一合作提供支持。双方已达成原则协议，将在莫斯科的托里斯基区和新莫斯科区与成都高新区建立合作伙伴关系。
- **原始摘要**: The Moscow government is ready to provide required support to this initiative, Minister of the Moscow Government Sergey Cheremin stressed

### 94. IN BRIEF: Second day of talks between Russia, US, Ukraine ends in Abu Dhabi: what we know
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 14:28:12 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216129
- **AI 摘要**: TASS报道了俄罗斯、美国和乌克兰在阿布扎比进行的第二次会谈情况。会议在上午结束，双方同意在未来进行一次囚犯交换。
- **原始摘要**: The meeting lasted just under two hours

### 95. Russia, Ukraine agree on large-scale prisoner exchange — chief negotiator
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 14:24:37 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216133
- **AI 摘要**: 俄罗斯和乌克兰在阿布扎比的会谈中达成了一项大规模的囚犯交换协议。俄罗斯总统顾问维克多·梅德韦斯基表示，人道主义问题在谈判中得到了讨论。
- **原始摘要**: Vladimir Medinsky emphasized that humanitarian issues had been discussed during the negotiations

### 96. EU representatives approve sanctions against Russian companies, individuals
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 14:11:29 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216087
- **AI 摘要**: 欧盟代表批准了对俄罗斯公司的制裁，这些制裁与正在进行的阿布扎比会谈无关。这是计划中的制裁，与正在准备的第22批反俄制裁无关。
- **原始摘要**: These were planned sanctions unrelated to talks underway in Abu Dhabi, the source noted

### 97. US ultimatums to Iran will not yield results for Washington — Iranian diplomat
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 14:11:22 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216081
- **AI 摘要**: 伊朗外交官表示，对伊朗的强硬措辞不会对美国产生预期效果，反而会进一步复杂化地区局势。
- **原始摘要**: According to the statement, such rhetoric will also further complicate the situation in the region

### 98. Russian negotiators at Abu Dhabi talks to address the press soon — source
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 13:55:45 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216077
- **AI 摘要**: 俄罗斯在阿布扎比的谈判即将结束，俄罗斯代表团将在接下来的一小时内向媒体通报谈判情况。这是俄罗斯、美国和乌克兰三方会谈的第二天。
- **原始摘要**: The Russian delegation will address the media in the coming hour

### 99. Kremlin spokesman addresses Abu Dhabi talks and relations with Europe
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 13:48:32 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216071
- **AI 摘要**: 俄罗斯总统助理在阿布扎比会谈期间向普京汇报了与乌克兰和美国的双边会谈情况，以及与欧洲的关系和波兰公民涉嫌间谍活动的拘留情况。
- **原始摘要**: According to Dmitry Peskov, Russia’s delegation to the Abu Dhabi talks is keeping the President informed about the course of trilateral talks with Ukraine and the United States

### 100. What we know about Day 2 of Abu Dhabi talks between Russia, US and Ukraine
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 13:47:48 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216061
- **AI 摘要**: 本文报道了俄罗斯、美国和乌克兰在阿布扎比举行的第三轮会谈的最新进展。文章提到了会谈的背景信息和主要议题。

### 101. Putin, Lukashenko discussed Abu Dhabi talks at yesterday’s meeting, Kremlin says
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 13:47:29 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216073
- **AI 摘要**: 俄罗斯总统普京和白俄罗斯总统卢卡申科在11月10日的会议上讨论了在阿布扎比进行的俄罗斯、美国和乌克兰之间的三方会谈。
- **原始摘要**: The presidents of Russia and Belarus met in Novo-Ogaryovo on November 10

### 102. G7 foreign ministers discuss air defense, long-range weapons supplies to Ukraine
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 12 Nov 2026 01:46:11 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216629
- **AI 摘要**: G7外长在巴黎讨论向乌克兰提供防空系统和远程武器的进展，并宣布将增加对乌克兰的军事援助。
- **原始摘要**: The officials also announced their intention to step up efforts to provide military assistance to Ukraine

### 103. Cairo International Film Festival opens for 47th edition
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 12 Nov 2026 01:17:03 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/society/2216627
- **AI 摘要**: 文章内容关于埃及开罗国际电影节的开幕，提到了今年电影节的第47届，以及来自64个国家的145部电影参赛。文章主题与电影节相关，不属于上述任何类别。
- **原始摘要**: This year, 145 films from 64 countries will compete for the top award, the Golden Pyramid

### 104. Putin to chair Council on Sports meeting today
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 12 Nov 2026 00:56:06 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216625
- **AI 摘要**: 俄罗斯总统普京将主持体育发展理事会会议，讨论体育活动和体育赛事的发展。该理事会自上周修订法规并设立特别委员会以来首次召开会议。
- **原始摘要**: Last week, the Russian president revised its regulations and established special commissions

### 105. Putin to meet with US envoys Witkoff, Kushner today
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 12 Nov 2026 00:45:26 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216623
- **AI 摘要**: 俄罗斯总统普京将于今日与美国特使Steve Witkoff和Jared Kushner会面。此次会面是继俄罗斯、美国和乌克兰在阿布扎比举行的三方会谈之后。
- **原始摘要**: Kremlin Spokesman Dmitry Peskov said that the Russian president is expected to meet with the US envoys in the first half of the day

### 106. CSTO leaders approve nearly 20 documents at Moscow summit
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 12 Nov 2026 00:05:42 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/politics/2216619
- **AI 摘要**: 俄罗斯政治与外交新闻，CSTO领导人批准了莫斯科峰会上的近20份文件。
- **原始摘要**: The summit participants also approved a declaration

### 107. Israeli attacks kill six Palestinians in Gaza Strip over past day — Health Ministry
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Thu, 12 Nov 2026 00:01:22 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 时政
- **链接**: https://tass.com/world/2216617
- **AI 摘要**: 以色列对加沙地带的空袭导致过去一天内至少6人死亡，包括在阿什法医院发现的3名平民和在加沙城历史中心阿尔达贾区被炮击中死亡的1名平民。还有2人在加沙难民营阿布雷伊杰区丧生。另有20多人受伤，被送往医院。
- **原始摘要**: The ministry reported that over 20 injured people were taken to hospitals throughout the day

### 108. Poland says Pentagon supports permanent US base, with decision expected in December
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 19:09:00 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://breakingdefense.com/2026/11/poland-says-pentagon-supports-permanent-us-base-with-decision-expected-in-december/
- **AI 摘要**: 波兰国防部长表示，美国国防部支持在波兰建立永久军事基地，预计最终决定将在12月初做出。美国国防部长皮特·赫奇特表示一切都在良好方向上发展。
- **原始摘要**: Warsaw has identified four potential locations for a base that could accommodate 5,000 US troops and their families, and is offering to spend up to $4.4 billion on supporting infrastructure....

### 109. EU sets out $3.4B defense budget for 2027, boosts Ukraine spending
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 18:22:56 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://breakingdefense.com/2026/11/eu-sets-out-3-4b-defense-budget-for-2027-boosts-ukraine-spending/
- **AI 摘要**: 欧盟宣布2027年国防和安全预算为340亿美元，重点支持乌克兰。文章主要讨论了欧盟在国防预算上的增加，尤其是对乌克兰的支持。
- **原始摘要**: The new fiscal uplift comes in the wake of Ukraine President Volodymyr Zelenskyy telling European leaders last month that “we need at least €70 billion more from you.”...

### 110. Ukraine Regretting White House-Brokered Temporary Ceasefire In Strategic Riverside Town Of Oleshky
- **来源**: The War Zone (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 16:23:00 -0500 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.twz.com/news-features/ukraine-regretting-white-house-brokered-temporary-ceasefire-in-strategic-riverside-town-of-oleshky
- **AI 摘要**: 乌克兰官员表示，白 House 辅助的临时停火协议重新引发了俄罗斯在 Oleshky 的军事存在，可能导致新的 Dnipro 河攻势。
- **原始摘要**: Ukrainian officials are expressing concern that a renewed Russian military presence in Oleshky will result in new waves of attacks across the Dnipro River. The post Ukraine Regretting White House-Brok...

### 111. Turkey prepares to withdraw from base in Iraq in shift for Ankara-Baghdad relations: Analysts
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:39:45 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://breakingdefense.com/2026/11/turkey-prepares-to-withdraw-from-base-in-iraq-in-shift-for-ankara-baghdad-relations-analysts/
- **AI 摘要**: 土耳其政府预计本月将从伊拉克北部的一个军事基地撤出军队，分析师认为这将有助于改善两国关系。土耳其军队于2015年部署在巴沙贾军事基地，该基地位于土耳其南部边境50英里处，曾引发安卡拉与巴格达之间的摩擦。土耳其军队的撤出被视为恢复伊拉克主权和改善双边安全关系的一步。
- **原始摘要**: The move “comes amid broader efforts to stabilize the region and potentially establish a new regional security architecture based on greater regional ownership and responsibility,” according to defens...

### 112. House Republicans sidestep effort to impeach Hegseth
- **来源**: Defense News (MILITARY)
- **发布日期**: Tue, 10 Nov 2026 23:31:53 +0000 (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.defensenews.com/congress/2026/11/10/house-republicans-sidestep-effort-to-impeach-hegseth/
- **AI 摘要**: 美国国会众议院投票决定将国防部长彼得·赫格瑟的弹劾提案送至司法委员会，从而否决了罢免他的努力。
- **原始摘要**: In a 211 to 204 vote, House Republicans sent proposed impeachment articles against Hegseth to the Judiciary Committee, quashing the effort.

### 113. House opts to stall Hegseth impeachment vote, sending resolution to Judiciary Committee
- **来源**: Breaking Defense (MILITARY)
- **发布日期**: Tue, 10 Nov 2026 23:18:14 +0000 (昨天)
- **类型**: news
- **优先级**: high
- **分类**: 时政
- **链接**: https://breakingdefense.com/2026/11/house-opts-to-stall-hegseth-impeachment-vote-sending-resolution-to-judiciary-committee/
- **AI 摘要**: 美国国会将对国防部长彼得·赫格斯的弹劾议案提交给司法委员会，以阻止其弹劾投票。此举将推迟对国防部长的弹劾投票，并且任何重启该进程的努力将需要下届国会。
- **原始摘要**: A 211-204 House vote sent Rep. Thomas Massie’s impeachment resolution to the Judiciary Committee, effectively killing the effort for now and leaving any attempt to revive it to the next Congress....

### 114. The Debate of MCP vs. CLI Centers on SpeedApril 06, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ril 06, 2026
- **类型**: blog
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.cerebras.ai/blog/MCPvsCLI
- **AI 摘要**: 本文讨论了MCP与CLI中心之间的速度辩论。

### 115. You Are What You Read: Indian Political News Media Bias Dataset for Hindi Language
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 时政
- **链接**: https://arxiv.org/abs/2611.13686
- **AI 摘要**: 该文章讨论了印度语（Hindi）政治新闻媒体偏见数据集，涉及多个新闻机构的448篇文章，分为四种偏见类别。
- **原始摘要**: arXiv:2611.13686v1 Announce Type: new Abstract: Media bias understanding and detection remains an under-researched problem for Indian context, specifically for Indic languages, such as, Hindi, which i...

### 116. 北京公安备 11010802041394 号
- **来源**: Zhipu AI Research (TIER1)
- **发布日期**: 2026-11-12
- **类型**: research
- **优先级**: high
- **分类**: 时政
- **链接**: https://beian.mps.gov.cn/#/query/webSearch
- **AI 摘要**: 文章标题为北京公安备 11010802041394 号，内容与AI技术无关。

### 117. NEO Featured in NVIDIA GTC KeynoteMAR 18 '241X
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.1x.tech/discover/1x-humanoid-robot-neo-featured-in-nvidia-gtc-keynote
- **AI 摘要**: 摘要未提供具体信息，无法生成摘要。

### 118. 2023-12-30As Walker S Strikes the Gong, UBTECH Robotics Becomes the First Humanoid Robot  Company Listed on the Main Board of the HKEX
- **来源**: UBTECH (优必选) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ubtrobot.com/en/about/news/498758766067781
- **AI 摘要**: UBTECH Robotics成为首家在港交所主板上市的人形机器人公司。

### 119. 2023-09-01UBTECH Robotics to Play a Key Role in Hosting the IEEE RO-MAN 2024
- **来源**: UBTECH (优必选) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.ubtrobot.com/en/about/news/473378826465349
- **AI 摘要**: UBTECH Robotics将在IEEE RO-MAN 2024中扮演关键角色。

### 120. 2024-12-20燧原科技万卡集群建成，助推庆阳建设中国算力高地2024年12月20日，甘肃省庆阳市——“2024中国算谷数字产业发展大会”今日召开，甘肃省委常委、常务副省长程晓波、国家数据局副局长夏冰、国家发改委高技术司二级巡视员阮高峰、国家信息中心主任徐强、庆阳市委书记黄泽元、庆阳市委副书记、市长周继军等领导出席了大会。本次大会以“‘中国算谷 智慧庆阳’AI赋能产业变革城市转型”为主题，旨在加快推进全国一体化算力网络国家枢纽节点（甘肃）庆阳数据中心集群建设了解更多
- **来源**: Enflame (燧原科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.enflame-tech.com/news/news/2024-12-20
- **AI 摘要**: 甘肃省庆阳市召开2024中国算谷数字产业发展大会，推进全国一体化算力网络国家枢纽节点（甘肃）庆阳数据中心集群建设。

### 121. 2024-07-04专注为通用人工智能算力底座筑基 燧原科技连续五年参加世界人工智能大会2024年7月4日，中国上海——由外交部、国家发展和改革委员会、教育部、科学技术部、工业和信息化部、国家互联网信息办公室、中国科学院、中国科学技术协会和上海市人民政府共同主办的2024世界人工智能大会（WAIC 2024）正式开幕。致力于为通用人工智能打造算力底座的燧原科技以 “芯火燎原”为主题，连续第五年参会。大会期间，燧原科技不仅在展台现场（H2馆C109）展示了智算中心落地案例和里程碑系列产了解更多
- **来源**: Enflame (燧原科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: 时政
- **链接**: https://www.enflame-tech.com/news/news/2024-07-04
- **AI 摘要**: 燧原科技连续五年参加2024世界人工智能大会，展示智算中心落地案例和里程碑系列产品。

## 🏷️  AI应用

**72 篇文章**

### 1. 卷起来了！11月11日，大模型厂商在天猫打5折
- **来源**: 量子位 (TIER3)
- **发布日期**: Wed, 11 Nov 2026 06:18:09 +0000 (昨天)
- **类型**: news
- **优先级**: low
- **分类**: AI应用
- **链接**: https://www.qbitai.com/2026/11/509085.html
- **AI 摘要**: 文章主要介绍了大模型厂商在天猫进行打折促销活动的情况，包括智谱、MiniMax、千问办公、阿里云、Qoder等大模型厂商在天猫打5折。文章还提到了天猫双11 Token的火爆情况，标志着大模型开始走进大众消费。
- **原始摘要**: 大模型厂商智谱、MiniMax、千问办公、阿里云、Qoder都在天猫打5折。

### 2. AMD’s Venice-X maxes out family at 5.3 GHz, returning 3D V-Cache to data center after four years
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 21:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.tomshardware.com/pc-components/cpus/amds-venice-x-maxes-out-family-at-5-3-ghz-returning-3d-v-cache-to-data-center-after-four-years-chips-target-hpc-workloads-with-pcie-6-0-and-1-6-tb-s-memory-bandwidth
- **AI 摘要**: AMD的Venice-X处理器在5.3GHz下运行，重新引入了3D V-Cache到数据中心，这是在四年后。这篇文章主要讨论了AMD处理器的性能提升和数据中心技术的发展。
- **原始摘要**: AMD's Venice-X CPUs launch in the second half of 2027, bringing 3D V-Cache back to the data center after four years on the sidelines.

### 3. Why the data center you dread might never even be built
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 20:15:15 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://techcrunch.com/video/why-the-data-center-you-dread-might-never-even-be-built/
- **AI 摘要**: 文章讨论了AI基础设施投资项目的可行性问题，指出许多项目可能无法实际建设。文章提到了反对意见、许可延迟和电力供应等问题。TechCrunch Equity播客主持人讨论了如何区分可行和不可行的数据中心项目。
- **原始摘要**: The data center boom is running into serious real-world obstacles, from widespread local opposition and permitting delays to a scramble for electricity. Before those challenges even come into play, th...

### 4. CoreWeave turns to customer prepayments, shorter contracts to fund AI growth
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 19:54:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://techcrunch.com/2026/11/11/coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth/
- **AI 摘要**: CoreWeave公司通过要求客户预付费用和签订短期合同来筹集资金以支持其AI增长。公司表示，这些策略有助于更高效地融资，并从现有的基础设施中榨取更多现金。但这些策略的成功取决于当前的需求和定价能力。
- **原始摘要**: CoreWeave is increasingly asking customers to pay upfront, borrowing against specific contracts, and even looking to short-term deals that could lead to higher prices, according to the company’s third...

### 5. Is Jensen Huang’s bad behavior more commonplace than it seems?
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 16:16:07 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://techcrunch.com/2026/11/11/is-jensen-huangs-bad-behavior-more-commonplace-than-it-seems/
- **AI 摘要**: 文章讨论了Nvidia CEO Jensen Huang的丑闻事件，以及中国在半导体行业中的经济间谍活动。文章提到了Nvidia的CEO在公司内部存在不良行为，这引发了行业内的担忧。文章指出，中国在经济间谍活动方面有着长期的历史，并且随着人工智能行业的兴起，这种行为变得更加普遍。
- **原始摘要**: “There are a lot of senior people in the industry that know this is happening, and are effectively condoning it,” an investment intel consultant said.

### 6. OpenAI’s quarterly revenue reportedly crosses $10B for the first time
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 16:14:44 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://techcrunch.com/2026/11/11/openais-quarterly-revenue-reportedly-crosses-10b-for-the-first-time/
- **AI 摘要**: OpenAI的季度营收首次突破10亿美元，较第二季度的67亿美元增长了43%。这反映了其在最近推出的AI模型上的强劲需求。
- **原始摘要**: Sales of $10 billion represents an almost 50% jump from revenue of $6.7 billion the company recorded in the second quarter.

### 7. Siri co-founder backs Helix for its voice ID tech
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 15:02:47 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://techcrunch.com/2026/11/11/siri-co-founder-backs-helix-for-its-voice-id-tech/
- **AI 摘要**: Siri联合创始人Dag Kittlaus投资语音身份验证公司Helix，该公司利用直接运行在用户设备上的语音技术来验证用户身份，无需用户提供敏感个人信息。
- **原始摘要**: With the rise of AI agents like Instinct and Muse, the industry needs to rethink human identity on the internet and rely on biometric signals like voice, which is where Helix comes in.

### 8. Databricks’ new AI agent tells CEO Ali Ghodsi the unvarnished truth
- **来源**: TechCrunch (TIER3)
- **发布日期**: Wed, 11 Nov 2026 15:00:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://techcrunch.com/2026/11/11/databricks-new-ai-agent-tells-ceo-ali-ghodsi-the-unvarnished-truth/
- **AI 摘要**: Databricks发布的新AI助手Genie能够完成复杂的任务，通过Databricks平台上存储的信息提供上下文。CEO Ali Ghodsi展示了Genie如何分析员工满意度调查并提出改进意见，以及如何准备一次失败的销售演示。
- **原始摘要**: With Databricks at 12,000 employees, AI Ghodsi is the first to admit that he can't know everyone and that they are unlikely to confess the things that go wrong to him. But he doesn't need them to. He...

### 9. ASRock quietly rolls out new firmware after disastrous previous update killed Radeon RX 7900-series GPUs
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 14:20:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.tomshardware.com/pc-components/gpus/asrock-attempts-to-correct-botched-radeon-rx-7000-firmware-release-with-new-version-revised-release-should-work-ok-but-company-provides-no-explanation-for-bricked-cards
- **AI 摘要**: 文章内容主要涉及ASRock公司为Radeon RX 7900系列显卡发布的更新固件，但因之前的更新导致显卡损坏，ASRock未提供保修覆盖信息。这与AI技术无关。
- **原始摘要**: Asrock's VBIOS 1.0.6 update follows reports of Radeon RX 7900 XT and XTX graphics cards failing to boot after installing the previous firmware.

### 10. Linux kernel reviewer steps down from memory management duties due to influx of AI slop patches
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 12:30:00 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back
- **AI 摘要**: Tom's Hardware报道了一名Linux内核审查员因AI相关提交过多而暂停了内存管理职责。文章讨论了AI在技术领域的影响。
- **原始摘要**: Linux kernel memory-management code reviewer steps down due to influx of AI slop patches — volume of submissions coupled with low manpower forces the step back

### 11. Grab 32GB DDR5 for $351 with this Newegg bundle with the 9800X3D, $87 less than the next cheapest memory
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Wed, 11 Nov 2026 10:54:55 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.tomshardware.com/pc-components/ddr5/grab-32gb-ddr5-for-usd351-with-this-newegg-bundle-with-the-9800x3d-usd87-less-than-the-next-cheapest-memory-gaming-pc-build-kit-includes-enthusiast-asus-x870e-motherboard-and-free-aio-liquid-cooler-with-usd128-99-in-total-savings
- **AI 摘要**: 本文介绍了Newegg的一个内存捆绑包，包括9800X3D处理器和32GB DDR5内存，价格为351美元，比最接近的内存便宜87美元。
- **原始摘要**: Another brilliant Newegg combo deal has combined the eight-core AMD Ryzen 7 9850X3D with 32GB of V-Color DDR5-6400 RAM, all for just $650, saving you a whopping $348.99 in the process.

### 12. Sequoia Capital to Invest in AI Holding Co. Sequence
- **来源**: The Information (TIER3)
- **发布日期**: 2026-11-11T21:27:56Z (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.theinformation.com/articles/sequoia-capital-invest-ai-holding-co-sequence
- **AI 摘要**: Sequoia Capital计划投资77亿美元的Sequence Holding，该公司专注于收购会计、保险和业主协会管理等行业的公司，并用人工智能替换或补充人类工作。这是Sequoia Capital在新类别控股公司上的第二次投资。
- **原始摘要**: Sequoia Capital is investing hundreds of millions of dollars into Sequence Holding, a one-year-old business that just announced a $7.7 billion insurance acquisition co-led by Michael Dell’s family off...

### 13. Anthropic, Others Warn of AI Acceleration
- **来源**: The Information (TIER3)
- **发布日期**: 2026-11-11T15:01:35Z (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.theinformation.com/articles/anthropic-others-warn-ai-acceleration
- **AI 摘要**: 文章主要讨论了The Information发布的年度50家最有可能的初创企业名单，提到了一些AI相关的公司如OpenRouter、Cursor和Perplexity，并提到了它们的估值和被收购的情况。文章并未涉及具体的技术实现或应用。
- **原始摘要**: In recent weeks, my colleagues and I have been trying our hand at being venture capitalists: today, the end result of that process is our annual list of the 50 most promising startups of this year, pu...

### 14. Introducing The Information’s 50 Most Promising Startups of 2026
- **来源**: The Information (TIER3)
- **发布日期**: 2026-11-11T14:00:55Z (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.theinformation.com/articles/introducing-informations-50-promising-startups-2026
- **AI 摘要**: 文章主要讨论了2026年《The Information》50家最热门初创公司名单，特别强调了安全领域的崛起。其中包括两家估值超过10亿美元的安全初创公司，且多数安全初创公司来自以色列。文章并未提及AI技术的应用或模型，因此不属于AI模型、Harness工程、具身智能、AI芯片、编译器、光计算、军事技术或经济类别。文章主题与AI在具体行业落地的产品/解决方案无关。
- **原始摘要**: As artificial intelligence changes how companies get hacked, investors are paying up for startups that promise to keep defenders ahead. That dynamic shaped this year’s The Information 50, our annual l...

### 15. The Anthropic-OpenAI Valuation Gap
- **来源**: The Information (TIER3)
- **发布日期**: 2026-11-11T00:11:28Z (昨天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://www.theinformation.com/articles/anthropic-openai-valuation-gap
- **AI 摘要**: 本文对比了Anthropic和OpenAI在IPO前的估值情况，Anthropic计划的估值范围为1.26至1.4万亿美元，而OpenAI的估值为1.25万亿美元。尽管Anthropic在第三季度的收入是OpenAI的70%，且增长速度更快，但其IPO前估值仅比OpenAI高12%。
- **原始摘要**: If you want proof of the widening gap in sentiment between public and private investors, take a look at the valuations of Anthropic and OpenAI.On Tuesday, Anthropic disclosed it was targeting a valuat...

### 16. Zocdoc Brings AI to Healthcare
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:54:40 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/zocdoc-brings-ai-to-healthcare-video
- **AI 摘要**: 文章提到Zocdoc公司通过AI技术改进其医疗服务，包括寻找网络内医生和安排患者时间表等任务。文章讨论了AI在医疗健康领域的应用以及Zocdoc如何保持患者隐私。
- **原始摘要**: AI agents are moving into health care, taking on tasks from finding an in-network doctor to booking appointments around a patient's schedule. Zocdoc CEO Oliver Kharraz says traffic to the platform fro...

### 17. Bloomberg Businessweek Daily Podcast: CoreWeave Triggers Rally
- **来源**: Bloomberg Politics (TIER3)
- **发布日期**: Wed, 11 Nov 2026 22:18:03 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/businessweek-daily-podcast-coreweave-triggers-rally-video
- **AI 摘要**: 文章主要讨论了CoreWeave公司股票的上涨以及对AI投资乐观情绪的影响，提到了芯片制造商和Anthropic公司的IPO计划。文章没有涉及AI模型、芯片、编译器、光计算、军事技术、经济或时政等方面的内容。
- **原始摘要**: The people, companies and trends shaping the global economy. Watch Carol and Tim LIVE every day on YouTube: http://bit.ly/3vTiACF A gauge for emerging-market stocks rose for a third day, led by Asian...

### 18. CoreWeave soars more than 24% for best day since April 2025 after strong Q3 report
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 21:11:26 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cnbc.com/2026/11/11/coreweave-crwv-outlook-earnings-ai.html
- **AI 摘要**: CoreWeave公司发布第三季度财报后股价大涨超过24%，创自2025年4月以来的最佳表现。该公司表示，其业绩超出预期，并提高了全年指导。Neoclouds公司如CoreWeave、Nebius和IREN等因AI交易的可持续性受到投资者的审查。Zacks首席股票策略师John Blank表示，CoreWeave通过减少无担保债券融资来缓解了投资者的担忧。
- **原始摘要**: Neoclouds such as CoreWeave, Nebius and IREN have come under scrutiny this month as investors assessed the sustainability of the AI trade.

### 19. Oura to Buy AI Doctor Startup
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 19:23:00 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.bloomberg.com/news/videos/2026-11-11/oura-to-buy-ai-doctor-startup-video
- **AI 摘要**: Oura公司收购了AI医生服务公司Counsel Health，交易金额为625000000美元，这是该公司在上市计划失败后扩大业务的一部分。Bloomberg Deals节目对此进行了讨论。
- **原始摘要**: Oura agreed to acquire AI and on-demand doctor service Counsel Health for $625 million, expanding its business following a scrapped attempt to go public. Scarlet Fu and Dani Burger discuss the acquisi...

### 20. Google Adds Gemini Voice AI Assistant to Apple CarPlay
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Wed, 11 Nov 2026 18:57:04 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.bloomberg.com/news/articles/2026-11-11/google-adds-gemini-voice-ai-assistant-to-apple-carplay
- **AI 摘要**: 谷歌将 Gemini 语音AI助手添加到苹果CarPlay系统中，为使用该助手的苹果设备用户提供了更多选项。
- **原始摘要**: Alphabet Inc.’s Google is adding its Gemini artificial intelligence app to Apple Inc.’s CarPlay system, expanding options for drivers who may already be using the assistant on their Apple devices.

### 21. I Visited Big Bear Lake’s Famous Bald Eagles and Found Very Human Shenanigans
- **来源**: The New York Times HomePage (TIER3)
- **发布日期**: Wed, 11 Nov 2026 18:50:57 +0000 (今天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.nytimes.com/2026/11/11/magazine/eagle-cam-big-bear-lake.html
- **AI 摘要**: 文章主要描述了作者在观看直播鹰巢的真人冒险经历，属于AI应用类别中的具体行业落地的产品或解决方案。
- **原始摘要**: My I.R.L. adventures in the strange human world behind the enormously popular livestreaming eagle cam.

### 22. Jim Cramer says Anthropic's explosive growth could justify a record-breaking IPO
- **来源**: CNBC Technology (TIER3)
- **发布日期**: Tue, 10 Nov 2026 23:46:35 GMT (昨天)
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cnbc.com/2026/11/10/anthropic-ipo-revenue-growth-cramer.html
- **AI 摘要**: 文章提到Jim Cramer认为Anthropic的快速增长使其估值可以达到历史最高水平，Cramer认为其季度收入增长率为47%仍然令人印象深刻。这与AI应用类别相关。
- **原始摘要**: "The fact that this deal is on is bullish for tech and the AI trade," CNBC's Jim Cramer said Tuesday.

### 23. Europeans would do well to learn realism, desire for peace from US envoys
- **来源**: TASS Defense (MILITARY)
- **发布日期**: Wed, 11 Nov 2026 15:17:07 +0300 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://tass.com/politics/2216233
- **AI 摘要**: 这篇文章讨论了俄罗斯和美国在乌克兰问题上的谈判，以及俄罗斯方面的评论。它不属于任何预设的类别，因为它没有涉及AI模型、芯片、编译器、光计算、军事技术、经济、时政或AI应用等主题。
- **原始摘要**: No Europeans were present at the negotiating table

### 24. BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model
- **来源**: Hugging Face Blog (TIER2)
- **发布日期**: Wed, 11 Nov 2026 05:01:16 GMT (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://huggingface.co/blog/qvac/botpsy
- **AI 摘要**: 本文介绍了一种名为BotPsy的设备上个人助手，它使用了一个参数规模在数亿以下的代理语言模型。该模型在设备上实现了高效且安全的对话功能。

### 25. WebAssembly JSPI is going to origin trial
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-03-06T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://v8.dev/blog/jspi-ot
- **AI 摘要**: V8浏览器引擎中的WebAssembly JSPI API进入试运行阶段，允许WebAssembly应用在异步操作返回时暂停。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API is entering an origin trial, with Chrome release M123. What that means is that you can test whether you and your users can benefit from this new...

### 26. TAMEing the Open-World Personalization: Towards Open-Set Personalized MLLM Assistant
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.14118
- **AI 摘要**: 文章讨论了如何使多模态大型语言模型（MLLM）作为智能助手时，能够更好地适应动态世界中的新概念。提出了TAME-O，一种无需训练的开放集个性化MLLM助手。
- **原始摘要**: arXiv:2611.14118v1 Announce Type: new Abstract: Personalizing Multimodal Large Language Models (MLLMs) as intelligent assistants has recently emerged as an active research topic, where an MLLM is expe...

### 27. What Factors Matter for Collection-Level Counting with Human-AI Collaboration?
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.14380
- **AI 摘要**: 文章讨论了人类与AI合作进行大规模图像集合计数时的选择和策略，涉及多个领域如生物医学显微镜、地面和空中野生动物调查以及城市结构的高空影像。
- **原始摘要**: arXiv:2611.14380v1 Announce Type: new Abstract: Many scientific and policy decisions require estimating the total number of target objects across a large image collection. Exhaustive human labeling is...

### 28. BigEarthNet.txt: A Large-Scale Multi-Sensor Image-Text Dataset and Benchmark for Earth Observation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: medium
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2603.29630
- **AI 摘要**: 文章介绍了BigEarthNet.txt，这是一个大规模多传感器影像-文本数据集，用于提升地球观测中的指令驱动影像-文本学习。
- **原始摘要**: arXiv:2603.29630v3 Announce Type: replace Abstract: Vision-langugage models (VLMs) have shown strong performance in computer vision (CV), yet their performance on remote sensing (RS) data remains limi...

### 29. How Cerebras serves GPT-5.6 Sol at up to 750 tokens per secondAugust 27, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ust 27, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/how-cerebras-serves-gpt-5-6-sol-at-up-to-750-tokens-per-second
- **AI 摘要**: 文章讨论了Cerebras如何为GPT-5.6提供服务，使其每秒处理750个token的速度提升。

### 30. Gemma 4 on Cerebras—The Fastest Inference is Now MultimodalJune 29, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 29, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/gemma-4-on-cerebras-the-fastest-inference-is-now-multimodal
- **AI 摘要**: 文章讨论了Gemma 4在Cerebras上的应用，强调其在多模态推理方面的快速性能。

### 31. Never Loop Without VerifiersJune 24, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 24, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/never-loop-without-verifiers
- **AI 摘要**: 文章摘要未提供具体信息，无法生成100字以内的中文总结

### 32. NewsJuly 23, 2026Accelerating InferenceWe’ve raised $300M at a $10.3B valuation, led by Sequoia Capital alongside Andreessen Horowitz, Jane Street, Diffusion, Argo, and SK Hynix. We’re grateful for their support on our journey to Gigawatt-scale.

Our mission is to run the world’s inference. We believe the world’s most powerful models require an entirely new form of computing. Frontier models deserve frontier inference clusters: co-designed chips, packages, PCBs, cold plates, interconnects, and more that push the entire pareto curve on the most demanding workloads.

Today, under 1% of the global population has access to the most advanced AI models. Distributing access will require better technology to deliver more tokens / watt and many Gigawatts worth of compute. Our mission has never been more urgent.
- **来源**: Etched (TIER1)
- **发布日期**: uly 23, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://etched.com/progress/progress/accelerating-inference
- **AI 摘要**: 本文介绍了近期完成3亿美元融资的公司，旨在推动全球大规模推理技术的发展。公司计划开发专为强大模型设计的新型计算集群。

### 33. First Look @ Gemma 4 on Cerebras: 3 Fast Multimodal Apps We BuiltJuly 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: uly 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/first-look-gemma-4-on-cerebras-3-fast-multimodal-apps-we-built
- **AI 摘要**: 文章讨论了在Cerebras系统上使用Gemma 4开发的3个快速多模态应用。

### 34. Why the AI Race Shifted to SpeedMarch 20, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: rch 20, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/why-the-ai-race-shifted-to-speed
- **AI 摘要**: 文章讨论了AI竞赛从速度上的竞争转向，摘要信息主要集中在AI竞赛的转变上。

### 35. How to stop your autoresearch loop from cheatingMarch 19, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: rch 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/how-to-stop-your-autoresearch-loop-from-cheating
- **AI 摘要**: 文章讨论了如何防止自动研究循环作弊，与机器人、机械臂、人形机器人、运动控制、操作/抓取、导航、自动驾驶等技术无关。

### 36. Stop Shipping AI Slop: How Codex Spark Changes The Way You CodeMarch 04, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: rch 04, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/codex-spark-best-practices
- **AI 摘要**: 文章讨论了Codex Codex如何改变编程方式，属于AI应用类别

### 37. The rise of slow personal assistantsSeptember 24, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 24, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/the-rise-of-slow-personal-assistants
- **AI 摘要**: 文章讨论了个人助理领域的发展，特别是那些响应速度较慢的个人助理。

### 38. We Taught an AI Agent to QA Our Cloud Console — in Plain EnglishSeptember 08, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 08, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/we-taught-an-ai-agent-to-qa-our-cloud-console-in-plain-english
- **AI 摘要**: 文章讲述了如何训练AI代理理解并用简单语言回答云控制台的问题。

### 39. Why speed wins: faster inference is about more than just quicker answers–it’s the new path to accuracyFebruary 19, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.cerebras.ai/blog/speedandaccuracyblog
- **AI 摘要**: 文章讨论了更快的推理速度对准确性的贡献，不属于任何已分类的类别。

### 40. khammoon: From a Linguistic Guideline to a Thai Morpheme Segmenter
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.13012
- **AI 摘要**: 文章讨论了泰语分词问题，提出在词形学层面操作，以khammoon为最小单位进行分词，解决了泰语中词的不统一问题，提高了下游任务的性能。
- **原始摘要**: arXiv:2611.13012v1 Announce Type: new Abstract: Thai is written without spaces between words, making segmentation a foundational step in most Thai NLP pipelines. Existing tools primarily reproduce the...

### 41. The Indic Token Tax in 2026: Measuring Tokenizer. Disparity and Its Cost for the Languages of India
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.13058
- **AI 摘要**: 文章讨论了不同语言在GPT-4o等语言模型中的token差异，以及这种差异对印度25种语言的影响。
- **原始摘要**: arXiv:2611.13058v1 Announce Type: new Abstract: Commercial language model APIs bill per token, so a tokenizer that needs more tokens for the same content in one language makes that language more expen...

### 42. Mobile AI Factory: Building Specialized Language Models for Your Mobile Device
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.13509
- **AI 摘要**: 该文章介绍了Mobile AI Factory系统，该系统用于为特定任务和目标手机构建微调后的量化小语言模型，以保持用户数据隐私并减少对网络连接的依赖。
- **原始摘要**: arXiv:2611.13509v1 Announce Type: new Abstract: Small language models (SLMs) running on mobile devices can keep user data private and work without connectivity. But they perform well only when fine-tu...

### 43. Beyond Fluent Responses: Finding User Dissatisfaction in Human-AI Interactions
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.13894
- **AI 摘要**: 文章讨论了大型语言模型在对话中的表现，以及如何通过分析用户的不满意反馈来检测用户的满意度。
- **原始摘要**: arXiv:2611.13894v1 Announce Type: new Abstract: As large language models generate increasingly high-quality responses, recent work on response evaluation has moved beyond response-centered criteria, s...

### 44. MISO-BR: An Open Corpus for Misogyny Detection in Brazilian Portuguese
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.14036
- **AI 摘要**: 本文介绍了一个用于巴西葡萄牙语中二元性别歧视检测的开放语料库MISO-BR，该语料库包含896篇平衡的社交媒体文本，并提供了构建协议和可复现的基础线模型。
- **原始摘要**: arXiv:2611.14036v1 Announce Type: new Abstract: Misogyny is among the most prevalent forms of online hate speech directed at Brazilian users, yet open and auditable resources dedicated to it in Brazil...

### 45. An AI Assistant for Automating Anti-Corruption Expertise of Draft Legislation Based on the TRACE Framework
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.14244
- **AI 摘要**: 该文章介绍了一种基于TRACE架构的AI助手，用于自动化审查法案中的腐败风险。文章提到，该系统使用模型引导的单条款评估、规则基础的因子分配以及外部人类监督来工作。文章还提供了一个开放基准，用于评估该AI助手的有效性。
- **原始摘要**: arXiv:2611.14244v1 Announce Type: new Abstract: We present an AI assistant for automating anti-corruption expertise of draft legislation based on the TRACE architecture, designed to screen bills for c...

### 46. DermaVQA-DAS: Dermatology Assessment Schema (DAS) & Datasets for Closed-Ended Question Answering & Segmentation in Patient-Generated Dermatology Images
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年12月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2512.24340
- **AI 摘要**: 文章介绍了一种新的数据集DermaVQA-DAS，用于皮肤病评估和分割任务，该数据集结合了皮肤病评估框架DAS和患者生成的皮肤病图像。
- **原始摘要**: arXiv:2512.24340v2 Announce Type: replace-cross Abstract: Recent advances in dermatological image analysis have been driven by large-scale annotated datasets; however, most existing benchmarks focus o...

### 47. AI-Mediated Communication Can Steer Collective Opinion
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2605.16245
- **AI 摘要**: 文章讨论了大型语言模型在人类交流中的影响，特别是在引导集体意见形成方面。
- **原始摘要**: arXiv:2605.16245v2 Announce Type: replace-cross Abstract: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language mo...

### 48. Firefly: Illuminating Large-Scale Verified Tool-Call Data Generation from Real APIs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2605.17558
- **AI 摘要**: 本文介绍了一种名为FireFly的管道，用于从真实世界MCP服务器生成验证的工具调用数据，通过让强大的LLM探索真实API并从观察到的结果中逆向生成任务，以确保标签的正确性。
- **原始摘要**: arXiv:2605.17558v3 Announce Type: replace-cross Abstract: Training tool-calling agents requires large-scale trajectory data with verifiable labels, yet existing approaches either synthesize environmen...

### 49. Market-Conditioned JEPA: Learning from Unpredictable Market Shocks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年11月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: AI应用
- **链接**: https://arxiv.org/abs/2611.13572
- **AI 摘要**: 本文提出了一种新的金融时间序列预测架构MC-JEPA，通过条件化预测市场因素来提高预测性能。
- **原始摘要**: arXiv:2611.13572v1 Announce Type: cross Abstract: Much of the variation in financial time series is driven by market-wide shocks that cannot be predicted from an asset's own history. Per-asset self-su...

### 50. Qwen3Guard: Real-time Safety for Your Token Stream
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://qwenlm.github.io/blog/qwen3guard/
- **AI 摘要**: Qwen3Guard是Qwen家族的第一个安全防护模型，基于强大的Qwen3基础模型进行专门的细调，以确保负责任的AI交互，提供精确的安全检测，涵盖风险级别和分类。
- **原始摘要**: Tech Report GitHub Hugging Face ModelScope DISCORD Introduction We are excited to introduce Qwen3Guard, the first safety guardrail model in the Qwen family. Built upon the powerful Qwen3 foundation mo...

### 51. Qwen-Image-Edit: Image Editing with Higher Quality and Efficiency
- **来源**: Qwen Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://qwenlm.github.io/blog/qwen-image-edit/
- **AI 摘要**: Qwen-Image-Edit是基于20B Qwen-Image模型的图像编辑版本，能够实现精确的文字编辑，并同时使用Qwen2.5-VL和VAE Encoder进行语义和外观编辑。
- **原始摘要**: QWEN CHAT GITHUB HUGGING FACE MODELSCOPE DISCORD We are excited to introduce Qwen-Image-Edit, the image editing version of Qwen-Image. Built upon our 20B Qwen-Image model, Qwen-Image-Edit successfully...

### 52. Security Response Center
- **来源**: Zhipu AI Research (TIER1)
- **发布日期**: 2026-11-12
- **类型**: research
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.zhipuai.cn/en/zsrc
- **AI 摘要**: 摘要内容为：Security Response Center。该摘要内容与所有给定类别均不匹配。

### 53. Kimi Open Platform: New Feature Release Log
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://platform.kimi.ai/blog/posts/changelog
- **AI 摘要**: 摘要未提供足够的信息来确定文章主题，但根据标题《Kimi Open Platform: New Feature Release Log》可以推测可能是关于Kimi Open Platform的新功能发布日志。

### 54. Coding with Kimi K2: Top 6 Agents & Setup Guides
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://platform.kimi.ai/blog/posts/coding_with_kimi_agents_setup
- **AI 摘要**: 文章讨论了Kimi K2的6个代理和设置指南，属于AI应用类别

### 55. K2-Vendor-Verifier Now Includes "Kimi K2 Thinking"
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://platform.kimi.ai/blog/posts/K2_Vendor_Verifier_Newsletter
- **AI 摘要**: 文章提到K2-Vendor-Verifier新增了Kimi K2 Thinking功能，但未提供更多具体信息。

### 56. Intelligence Age
- **来源**: OpenAI News (TIER1)
- **发布日期**: 2026-11-12
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://openai.com/news/intelligence-age/
- **AI 摘要**: 文章摘要未提供足够的信息来确定其主题类别。

### 57. Cooking With NEO Beta and Nick DiGiovanniA behind the scenes look into the production of Nick DiGiovanni and NEO Beta's cooking challenge including BTS content and technical details.NOV 08 '24Dar Sleeper
- **来源**: 1X Technologies (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.1x.tech/discover/cooking-with-neo-beta-and-nick-digiovanni
- **AI 摘要**: 文章内容涉及Nick DiGiovanni和NEO Beta的烹饪挑战制作过程，包括幕后花絮和技术细节。与AI模型、AI芯片、编译器、光计算、军事技术、经济、时政等类别无关。

### 58. Announcements46
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://tenstorrent.com/newsroom/newsroom/tags/announcements
- **AI 摘要**: 文章摘要内容

### 59. Tenstorrent and Smallest.ai Partner to Bring Production-Grade Voice AI On-PremTenstorrent and Smallest.ai have partnered to deliver a production-grade, on-prem voice AI stack.Read more
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://tenstorrent.com/newsroom/newsroom/tenstorrent-and-smallestai-partner-to-bring-production-grade-voice-ai-on-prem
- **AI 摘要**: Tenstorrent和Smallest.ai合作推出生产级的语音AI堆栈。

### 60. ai& and Tenstorrent Launch JapanFold, Bringing Open-Source, Sovereign Drug Discovery to Japanai& and Tenstorrent launched JapanFold, a drug discovery platform running on ai&'s sovereign infrastructure, powered by Tenstorrent Galaxy™ superclusters.Read more
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://tenstorrent.com/newsroom/newsroom/aiand-and-tenstorrent-launch-japanfold
- **AI 摘要**: ai&和Tenstorrent在日本推出了JapanFold平台，该平台基于ai&的主权基础设施，由Tenstorrent Galaxy™超级集群提供支持，用于开源和自主药物发现。

### 61. d-Matrix Recognized on Fast Company’s Next Big Things in Tech List
- **来源**: D-Matrix (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.d-matrix.ai/announcements/d-matrix-recognized-on-fast-companys-next-big-things-in-tech/
- **AI 摘要**: d-Matrix 被 Fast Company 列为科技领域十大创新之一。

### 62. 2026-07-17七年WAIC同行，燧原科技持续展示国产AI算力规模化落地成果，共筑Token经济时代算力底座2026年7月17日，中国上海——2026世界人工智能大会暨人工智能全球治理高级别会议（WAIC 2026）在沪开幕。燧原科技以“芯火燎原”为主题参展WAIC 2026（世博展览馆H2馆C117、张江科学会堂海科厅Z1A-601），集中展示其在人工智能算力基础设施建设和产业应用等方面的最新成果，呈现国产AI算力从技术突破迈向规模化应用的发展图景。燧原科技展台伴随“十五五”规划纲要明确部署全面实施“了解更多
- **来源**: Enflame (燧原科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.enflame-tech.com/news/news/2026-07-17
- **AI 摘要**: 燧原科技在2026世界人工智能大会展示国产AI算力规模化落地成果，包括算力基础设施建设和产业应用。

### 63. 2025-07-27燧原科技亮相WAIC，以国产算力使能互联网创新应用2025世界人工智能大会暨人工智能全球治理高级别会议（WAIC 2025）在上海隆重开幕。作为国产人工智能算力创新的关键推动者，燧原科技以“芯火燎原”为主题连续第六年参展，全面展示算力基础设施建设、AI商业化落地和研发探索的最新成果。展现多元智算进阶落地实践当前，国家正大力推进“人工智能+”行动，强化算力基础设施建设，促进国产AI算力系统在重点行业落地应用。在大模型驱动的智能产业变革中，AI算力已了解更多
- **来源**: Enflame (燧原科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.enflame-tech.com/news/news/2025-07-27
- **AI 摘要**: 燧原科技亮相WAIC大会，展示国产算力在互联网创新中的应用和最新成果。

### 64. 2025-02-25燧原S60上线近万卡为美图AI推理业务保驾护航2025蛇年元宵后，美图公司旗下美颜相机凭借“AI换装”功能爆火，获得了国内外用户的极大青睐，App下载量和使用量迅速激增的同时，也面临了海量推理算力即时支持的挑战。作为美图的战略合作伙伴，燧原科技立即做出响应，仅用4天就在2024年底建成并正式投入使用的庆阳智算中心完成了近万张推理卡上线部署，并且确保推理算力性能优异，为美图公司提供强劲的“隐形引擎”。美颜相机的AI换装效果庆阳智算中心搭载了新一了解更多
- **来源**: Enflame (燧原科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.enflame-tech.com/news/news/2025-02-25
- **AI 摘要**: 美图公司通过燧原科技的庆阳智算中心在2024年底上线近万张推理卡，以支持美颜相机的AI换装功能，确保了算力的高效运行。

### 65. 2025-02-06燧原科技实现全国各地智算中心DeepSeek的全量推理服务部署以DeepSeek-R1和V3为代表的开源模型系列在多语言理解和复杂推理任务中表现出色，极大优化了算力成本，并进一步改变了训练和部署的算法结构，这一技术创新将快速提升对于推理算力的需求，从而加速推动AI应用场景的落地。作为国产算力领军企业，燧原科技完成了对DeepSeek全量模型的高效适配，包括DeepSeek-R1/V3 671B原生模型、DeepSeek-R1-Distill-Qwen-1.5了解更多
- **来源**: Enflame (燧原科技) (TIER1)
- **发布日期**: 2026-11-12
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://www.enflame-tech.com/news/news/2025-02-06
- **AI 摘要**: 燧原科技完成对DeepSeek全量模型的高效适配，包括DeepSeek-R1/V3 671B原生模型和DeepSeek-R1-Distill-Qwen-1.5，提升了算力成本并优化了算法结构。

### 66. ChatGPT Plus for veterans and servicemembersCompanyNov 11, 2026
- **来源**: OpenAI News (TIER1)
- **发布日期**: 2026-11-11T08:00:00Z
- **类型**: news
- **优先级**: high
- **分类**: AI应用
- **链接**: https://openai.com/index/chatgpt-plus-for-veterans/
- **AI 摘要**: 文章讨论了ChatGPT Plus在退役军人和军人群体中的应用。

### 67. DeepSeek-V4.1-Flash Is Generally Available: 552B MoE, Native Vision, New Peak/Off-Peak Pricing
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-09-18
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://deepseek.ai/blog/deepseek-v41-flash-generally-available
- **AI 摘要**: DeepSeek发布V4.1-Flash版本，包含552B MoE和原生图像理解能力，V4-Flash和视觉变体已退役，V4-Pro将于9月14日迁移，同时推出了长期宣布的高峰时段收费。
- **原始摘要**: The two-day beta became an official release: V4.1-Flash ships as deepseek-flash with native image understanding, V4-Flash and the vision variant retired, V4-Pro routed away from September 14 — and the...

### 68. DeepSeek V4.1 Flash vs GPT-6 Astra: Four Real Builds, Full Cost and Time Breakdown
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-09-16
- **类型**: research
- **优先级**: high
- **分类**: AI应用
- **链接**: https://deepseek.ai/blog/deepseek-v41-flash-vs-gpt6-astra-four-builds
- **AI 摘要**: 文章讨论了两个模型DeepSeek和Astra在四个不同构建项目上的API支出和构建时间，DeepSeek在API支出上比Astra便宜约6倍，在构建时间上比Astra快约3倍。
- **原始摘要**: An independent creator gave both models the same four builds — an RTS replica, a 3D scroll website, a booking app and a Blender animation. DeepSeek came in ~6x cheaper on API spend; Astra was ~3x fast...

### 69. DeepSeek Vision API: Sending Images to deepseek-v4-flash-vision-exp
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-08-23
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://deepseek.ai/blog/deepseek-vision-api-guide
- **AI 摘要**: DeepSeek现在接受图像输入，提供了三种输入方法（base64、外部URL、Files API），并详细说明了文档限制。
- **原始摘要**: DeepSeek now accepts images. The three input methods (base64, external URL, Files API), detail levels, the 384-token-per-image ceiling, all documented limits and the Anthropic-compatible variant.

### 70. DeepSeek Vision API: Sending Images to deepseek-v4-flash-vision-exp
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-08-23
- **类型**: research
- **优先级**: high
- **分类**: AI应用
- **链接**: https://deepseek.ai/blog/deepseek-vision-api-guide
- **AI 摘要**: DeepSeek现在接受图像输入。支持三种输入方式（base64、外部URL、Files API），详细级别，每张图像384个token的限制，所有文档限制以及Anthropic兼容的变体都已文档化。
- **原始摘要**: DeepSeek now accepts images. The three input methods (base64, external URL, Files API), detail levels, the 384-token-per-image ceiling, all documented limits and the Anthropic-compatible variant.

### 71. DeepSeek V5: Release Date Rumors vs. Confirmed Facts
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-08-20
- **类型**: blog
- **优先级**: high
- **分类**: AI应用
- **链接**: https://deepseek.ai/blog/deepseek-v5-release-date-rumors
- **AI 摘要**: 文章讨论了DeepSeek V5的发布日期传闻与证实事实，未涉及AI模型、芯片、编译器等具体技术领域。
- **原始摘要**: No changelog entry, no model string, no paper — DeepSeek V5 is unconfirmed. What the September 2026 leak claims, the real V4 timeline, and the three signals that would prove V5 exists.

### 72. DeepSeek V5: Release Date Rumors vs. Confirmed Facts
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-08-20
- **类型**: research
- **优先级**: high
- **分类**: AI应用
- **链接**: https://deepseek.ai/blog/deepseek-v5-release-date-rumors
- **AI 摘要**: 文章讨论了DeepSeek V5的发布日期传闻与已证实的事实，未涉及AI模型、芯片、编译器等具体技术领域。
- **原始摘要**: No changelog entry, no model string, no paper — DeepSeek V5 is unconfirmed. What the September 2026 leak claims, the real V4 timeline, and the three signals that would prove V5 exists.

## 🏷️  未分类

**1 篇文章**

### 1. Prague Dependency Treebank -- Consolidated 2.0: Enriching a Complex Annotation Scheme
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **链接**: https://arxiv.org/abs/2606.24324
- **原始摘要**: arXiv:2606.24324v2 Announce Type: replace Abstract: The Prague Dependency Treebank framework is unique in its attempt to systematically include and link different layers of language, including a meani...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
