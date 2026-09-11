# RSS 聚合报告 - Harness工程

**生成时间**: 2026-09-12 07:11:35
**文章数量**: 71 篇

---

### 1. How to handle cofound variables? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-09-11T18:57:40+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1wdpat4/how_to_handle_cofound_variables_d/
- **AI 摘要**: 该讨论帖询问在机器学习实验或统计分析中如何处理混杂变量（文中写为cofound variables，应为confounding variables）。参与者建议了多种方法，包括在实验设计中随机化、使用分层分析、引入协变量进行回归调整、倾向得分匹配等，并讨论了不同场景下各方法的适用性和局限性，旨在帮助研究者避免因混杂因素导致的错误因果推断。
- **原始摘要**: edit: confound Hello all, I am working on a object classification with a automotive radar point clouds. I compared many models and feature vectors. Once i used range as feature, all models scored high...

### 2. Any tools to turn a codebase into a fine tuning dataset? [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-09-11T04:27:12+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1wd5zkk/any_tools_to_turn_a_codebase_into_a_fine_tuning/
- **AI 摘要**: 该讨论帖询问有哪些工具可以将现有代码库自动转换为微调数据集。参与者推荐了多种方案，包括利用静态分析提取函数和文档字符串、使用LLM生成指令-响应对、基于代码变更历史构建训练样本等。讨论还涉及数据质量过滤、格式转换和隐私保护等实际问题，为希望利用自有代码微调模型的开发者提供了实用工具和实践建议。
- **原始摘要**: I have a few web projects with pretty good UI/UX and I’m wondering if there’s any tool or workflow that can turn an existing codebase into a dataset for fine tuning. For example, given a React/Next.js...

### 3. Why is TMLR so slow in recent times [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-09-11T04:09:09+00:00 (昨天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1wd5mki/why_is_tmlr_so_slow_in_recent_times_d/
- **AI 摘要**: 该讨论帖探讨了TMLR（Transactions on Machine Learning Research）期刊近期审稿和处理速度明显变慢的原因。参与者分析了可能因素，包括投稿量激增、审稿人短缺、编辑流程效率下降等，并分享了各自的投稿等待经历。讨论反映了机器学习领域学术出版面临的普遍压力，以及社区对审稿周期延长的担忧。
- **原始摘要**: A final-year PhD student here. A few months back, I submitted a solo-authored paper to TMLR. The reviewers were on time and extremely positive, with some minor revisions. After submitting the revised...

### 4. Microsoft's Data Center Plans Face Big Costs
- **来源**: Bloomberg Technology (TIER3)
- **发布日期**: Fri, 11 Sep 2026 18:21:40 GMT (今天)
- **类型**: news
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.bloomberg.com/news/videos/2026-09-11/microsoft-s-data-center-plans-face-big-costs-video
- **AI 摘要**: 微软计划将数据中心容量扩大三倍以上，以解决计算短缺问题。此前因算力不足，微软不得不拒绝部分AI和云业务，此举旨在满足日益增长的AI服务需求。
- **原始摘要**: Microsoft plans to more than triple its data center capacity to help overcome a computing shortage that has forced it to turn away some AI and cloud business. Bloomberg's Brody Ford joins Ed Ludlow on...

### 5. Together AI expands fine-tuning service with more models, live metrics, and finer controls
- **来源**: Together AI Blog (TIER2)
- **发布日期**: Fri, 11 Sep 2026 00:00:00 GMT (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://www.together.ai/blog/together-ai-expands-fine-tuning-service-with-more-models-live-metrics-and-finer-controls
- **AI 摘要**: Together AI 扩展其微调服务，新增更多可微调模型、实时训练指标以及更精细的控制选项。平台提供无服务器推理、批量推理、专用吞吐量、GPU 集群（GB300、B200、H200 等）及自定义训练与评估能力，并支持 MiniMax M3、Gemma 4、DeepSeek V4 Pro、GLM-5.2、kimi K2.7 Code、gpt-oss-120B 等开源模型，面向开发者提供从微调、评估到部署的一站式 AI 工程工具链。
- **原始摘要**: Together Fine-Tuning adds the latest open-weight models, live experiment tracking, Expert LoRA, early stopping, tokenized dataset previews, pre-flight validation, and lower training prices on selected...

### 6. HW Information-Flow Tracking for Pre-Silicon Security Testing (Princeton, MIT, EPFL)
- **来源**: SemiEngineering (TIER2)
- **发布日期**: Fri, 11 Sep 2026 20:15:35 +0000 (今天)
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://semiengineering.com/hw-information-flow-tracking-for-pre-silicon-security-testing-princeton-mit-epfl/
- **AI 摘要**: 普林斯顿、MIT CSAIL与EPFL发表论文，提出CEGAR-T框架，用于硅前安全测试的高效硬件信息流跟踪。针对CellIFT等污点逻辑导致仿真开销过大的问题，CEGAR-T自动合成污点逻辑，在保证无假阳性前提下最小化插桩开销。在RISC-V核时序侧信道安全评估中，插桩和仿真开销几何平均分别从5.64倍降至1.42倍、34.65倍降至1.79倍。
- **原始摘要**: Researchers at Princeton University, MIT CSAIL, and EPFL published a technical paper titled “Efficient Hardware Information-Flow Tracking for Pre-Silicon Security Testing.” Abstract “Register-Transfer...

### 7. Beyond Benchmarks: Using VLMs to Reveal Systematic Classification Failures Under Real World Conditions
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11126
- **AI 摘要**: 探索利用视觉语言模型加速分类模型验证与确认，提出基于VLM的错误切片检测方法，在国防场景下自动发现系统性分类失败模式，缓解人工检查负担并应对领域数据不足挑战。
- **原始摘要**: arXiv:2609.11126v1 Announce Type: new Abstract: Verification and validation (V&V) of classification models is crucial to enable a wide range of sensor processing applications. Currently, the V&V proce...

### 8. HALDETECT at ImageEval 2026 Shared Tasks: Answer-First Contrastive Grounding with QLoRA
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11236
- **AI 摘要**: HALDETECT系统参加ImageEval 2026幻觉检测任务，采用答案优先的对比式定位与QLoRA微调Qwen2.5-VL-7B，冻结视觉编码器，在千项测试集上取得CI 0.035，位列八队第三。
- **原始摘要**: arXiv:2609.11236v1 Announce Type: new Abstract: Large multimodal models tend to hallucinate visual detail fluently, which limits their deployment for fine-grained interpretation. We present HALDETECT,...

### 9. From Evaluation to Enhancement: Benchmarking and Improving Think-with-Video Reasoning for Video Generative Models
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11242
- **AI 摘要**: 提出VWG-Bench基准，覆盖9个推理维度和38项任务，用三级VLM-as-Judge协议评估视频生成模型的规则遵循与目标实现能力，并推出Vid-PRE提示推理增强器以改进逻辑约束任务表现。
- **原始摘要**: arXiv:2609.11242v1 Announce Type: new Abstract: Video generation has advanced to produce visually compelling and temporally coherent results. Yet, whether these models can genuinely think with video--...

### 10. MedGEN-Bench: A Contextually Entangled Benchmark for Open-ended Multimodal Medical Generation
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2511.13135
- **AI 摘要**: 针对医学视觉语言模型评测中查询-图像错位、封闭式格式与文本中心输出三大局限，提出开放式多模态医学生成基准MedGEN-Bench，含6422个专家审核图文对，覆盖6种影像模态、15项临床任务与27个子任务。
- **原始摘要**: arXiv:2511.13135v3 Announce Type: replace Abstract: Medical vision-language models (VLMs) are increasingly expected to support clinical workflows through diagnostic text and relevant medical images. H...

### 11. Larger Context Window, Fewer Overcorrections: Optimizing Prompts and Batching for Minimal-Edit Grammatical Error Correction
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10810
- **AI 摘要**: 针对最小编辑语法纠错中大模型过度纠正问题，提出基于分类指令、批量输入和更大上下文窗口的提示方法，在无需微调情况下缩小与微调模型的差距并降低编辑率。
- **原始摘要**: arXiv:2609.10810v1 Announce Type: new Abstract: Minimal-edit Grammatical Error Correction (GEC) is a challenging task for zero- and few-shot prompted Large Language Models (LLMs), which systematically...

### 12. Detectable Only Where It Is Confounded: What Verified Duplication Counts Say About Membership Evidence in Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10830
- **AI 摘要**: 利用OLMo-2和Pythia公开预训练语料及重复计数索引，直接检验模型对训练句子的预测便宜度与成员关系，发现普通文本重复水平下1B至13B模型仅留下微弱痕迹，秩相关约-0.08。
- **原始摘要**: arXiv:2609.10830v1 Announce Type: new Abstract: When a language model finds a sentence unusually cheap to predict, it is tempting to conclude that the sentence was in its training data. Almost every p...

### 13. SearchAtlas: Analyzing Agentic Search Strategies via Evidential Query Graphs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10901
- **AI 摘要**: 提出SearchAtlas框架，将LLM搜索智能体的搜索轨迹转化为结构化证据查询图，自动解析边F1达86%，并在三个基准上分析五个搜索智能体的搜索规模与证据聚合差异。
- **原始摘要**: arXiv:2609.10901v1 Announce Type: new Abstract: LLM search agents are often evaluated on final-answer accuracy, overlooking the process. Analyzing a search strategy requires understanding how credible...

### 14. Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10922
- **AI 摘要**: 提出Auto-RecSys自主研究系统，通过分布式异步执行和跨服务器集中记忆等harness设计，解决工业级推荐模型实验中反馈周期长、系统复杂的问题，实现长周期自动化实验。
- **原始摘要**: arXiv:2609.10922v1 Announce Type: new Abstract: Auto-research agents have shown the potential to automate hypothesis generation, experiment execution, and iterative refinement. However, scaling this p...

### 15. Rethinking Verbalized Confidence for LLM-as-a-Judge: A Compatibility Shift on Post-2025 Proprietary Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10996
- **AI 摘要**: 发现2025年后顶级专有模型上，言语化置信度比对数概率更适合作为LLM评判的软评分机制，并提出过度自信提示与自我辩论两种方法改善校准与鲁棒性。
- **原始摘要**: arXiv:2609.10996v1 Announce Type: new Abstract: Verbalized confidence, long dismissed as overconfident, coarse, and prone to round-number clustering, is now the more robust soft-scoring mechanism for...

### 16. When Noise Fabricates Bias: The Fragility of LLM-as-a-Judge Bias Measurement under Noisy Text
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11067
- **AI 摘要**: 研究文本表面噪声对LLM评判社会偏见测量的影响，发现噪声会不对称地将中性判断转为有偏判断，最高达120倍，且不同评判模型表现差异明显。
- **原始摘要**: arXiv:2609.11067v1 Announce Type: new Abstract: Large language models are increasingly used as judges to measure social bias in text, yet the passages they judge are often noisy, containing typos, inf...

### 17. Overview of the NLPCC 2026 Shared Task 11: Agent-Based Experiment Reproduction from Scientific Papers
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11117
- **AI 摘要**: 介绍NLPCC 2026共享任务11，提出AgentActionBench过程导向基准，用MCP动作记录器捕获智能体复现科学论文实验的行为，涵盖150篇ML与AI4Science论文。
- **原始摘要**: arXiv:2609.11117v1 Announce Type: new Abstract: Reproducibility is essential to scientific progress, yet the growing volume and complexity of scientific publications make exhaustive manual verificatio...

### 18. Can LLMs Normalize Databases? A Benchmark and Multi-Agent Framework for Schema Normalization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11141
- **AI 摘要**: 研究LLM进行数据库范式化的可靠性，提出包含3275个样本的DNBENCH基准，从语义等价、结构准确和逻辑有效三方面评估，并提出多智能体框架MARS改进范式化。
- **原始摘要**: arXiv:2609.11141v1 Announce Type: new Abstract: Large Language Models (LLMs) are increasingly used to generate structured outputs, but their reliability remains unclear when those outputs must satisfy...

### 19. OmniHallu: Unified Hallucination Detection for Cross-Modal Comprehension and Generation in Multimodal Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11244
- **AI 摘要**: 提出OmniHallu统一幻觉检测框架，覆盖图像、视频、音频的理解与生成任务，构建万级样本基准OmniHallu-Bench，采用多智能体分解原子断言并跨模态验证。
- **原始摘要**: arXiv:2609.11244v1 Announce Type: new Abstract: While Multimodal Large Language Models (MLLMs) have achieved remarkable progress across diverse tasks, they suffer from hallucinations where generated o...

### 20. On the Impact of Anonymization on the Performance of Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11335
- **AI 摘要**: 系统研究匿名化对大语言模型性能的影响，评测5个模型11个基准，发现匿名化总体降低性能，能力越强模型下降越大，且影响因任务而异，如TruthfulQA提升而检索任务骤降。
- **原始摘要**: arXiv:2609.11335v1 Announce Type: new Abstract: As large language models are increasingly deployed in sensitive domains, anonymizing input data to protect personally identifiable information has becom...

### 21. TransClean: A Benchmark for Detecting and Extracting Clean Translations from Large Language Model Outputs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11399
- **AI 摘要**: 构建TransClean基准，用于检测和提取大模型翻译输出中的翻译噪声，分析79万余条输出归纳12类噪声模式，含9900对噪声-干净样本，并评测两种提取方法。
- **原始摘要**: arXiv:2609.11399v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used for machine translation, yet their outputs often contain additional text beyond the translation itsel...

### 22. RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11758
- **AI 摘要**: 提出RAG-Safety-Bench基准，通过分离检索质量影响并划分四种条件，系统评估检索增强生成对LLM安全性的影响，帮助理解RAG引入的安全副作用机制。
- **原始摘要**: arXiv:2609.11758v1 Announce Type: new Abstract: Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However...

### 23. The widening evaluation gap in medical large language model research 2023 to 2026
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11770
- **AI 摘要**: 分析2023至2026年医学大语言模型研究，发现评估滞后从1.33个季度扩大到6.08个季度，随机试验评估的模型更旧，严谨性与时效性存在张力。
- **原始摘要**: arXiv:2609.11770v1 Announce Type: new Abstract: Large language models are superseded every few quarters; clinical evidence takes years. We asked whether medical research is keeping pace with the syste...

### 24. Beyond Word Error Rate: A Switch Aware Evaluation of ASR and Audio Language Models on English Yoruba Code-Switched Speech
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11786
- **AI 摘要**: 对11个ASR和音频语言模型在英语-约鲁巴语码切换语音上进行切换感知评估，发现总体WER掩盖了码切换行为，音频LM在切换局部指标上显著优于最佳ASR模型。
- **原始摘要**: arXiv:2609.11786v1 Announce Type: new Abstract: Automatic speech recognition (ASR) systems and audio language models (audio LMs) now report low error rates on monolingual benchmarks, but their behavio...

### 25. Domain-Specific Hallucination Detection in Large Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11878
- **AI 摘要**: 提出多信号幻觉检测流水线，结合DeBERTa-v3分类、MC Dropout不确定性量化和温度校准，在HaluEval上达F1=0.915、AUROC=0.977，并用DPO优化Qwen模型。
- **原始摘要**: arXiv:2609.11878v1 Announce Type: new Abstract: Large language models generate fluent text that can contain unfaithful claims -- a phenomenon known as hallucination. We present a multi-signal detectio...

### 26. Studying Without a Syllabus: Task-Agnostic Environment Preprocessing
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10824
- **AI 摘要**: 研究任务无关的环境预处理：智能体在不知下游任务分布时，能否在预算内探索新环境并构建索引、脚本等可复用资源，比较不同元智能体的准备策略。
- **原始摘要**: arXiv:2609.10824v1 Announce Type: cross Abstract: Before an LLM agent tackles tasks in a new environment, it can inspect available corpora and tools and construct reusable resources such as indices, s...

### 27. Empirical Evaluation of Membership Inference Attacks on NLP Text Classifiers: A Baseline Study on SST-2
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10935
- **AI 摘要**: 在SST-2情感分类上对TF-IDF+逻辑回归与微调DistilBERT进行成员推断攻击基准测试，两模型均泄露成员信号，强正则化与减少训练轮次可降低泄露但影响效用。
- **原始摘要**: arXiv:2609.10935v1 Announce Type: cross Abstract: Membership inference attacks (MIAs) try to determine whether a specific record was used to train a model, a privacy risk that matters in natural langu...

### 28. Beyond Solver Verdicts: Generative Reward Models for Autoformalization
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11085
- **AI 摘要**: 针对神经符号系统中形式化翻译可能保持判定结果却不忠实的问题（VPU），提出生成式验证GenV，将Z3等价预言机蒸馏为无参考的连续等价评分，可精确提取空间错误。
- **原始摘要**: arXiv:2609.11085v1 Announce Type: cross Abstract: Neurosymbolic systems rely on mathematical solvers to guarantee reasoning correctness, yet solvers are fundamentally blind to whether a formal transla...

### 29. REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11209
- **AI 摘要**: 针对RAG长上下文带来的延迟、KV缓存与token成本问题，提出REVA框架。它从历史查询-文档-模型交互中挖掘生成器注意力轨迹，构建可复用的证据视图评分库，实现与预算无关的压缩，避免逐查询独立压缩的在线开销。
- **原始摘要**: arXiv:2609.11209v1 Announce Type: cross Abstract: Retrieval-augmented generation (RAG) improves knowledge-intensive large language model (LLM) applications by conditioning generation on retrieved docu...

### 30. SpecGuard: Inference-Time Backdoor Detection For Free
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11799
- **AI 摘要**: 提出SpecGuard，一种零额外模型计算成本的推理时后门检测器。它复用推测解码机制，利用小草稿模型提议token、目标模型验证的过程来识别后门触发，无需输入扰动或额外生成，适合延迟敏感的LLM服务。
- **原始摘要**: arXiv:2609.11799v1 Announce Type: cross Abstract: Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves nor...

### 31. MindTopo: Can Foundation Models Reason in Topological Space?
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11900
- **AI 摘要**: 提出MindTopo基准，从连续性、分离性、顺序、包围、纽结五个拓扑属性评估基础模型的拓扑直觉，涵盖推理与规划两个认知层次，含11030个实例并测试14个多模态大模型。
- **原始摘要**: arXiv:2609.11900v1 Announce Type: cross Abstract: Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant un...

### 32. The PIMMUR Principles: Ensuring Validity in Collective Behavior of LLM Societies
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2509.18052
- **AI 摘要**: 系统审计576项LLM社会模拟研究，提出PIMMUR六项方法学标准，发现Profile、Interaction、Memory达标率高于Minimal-Control、Unawareness、Realism，且提示词常预设结果。
- **原始摘要**: arXiv:2509.18052v4 Announce Type: replace Abstract: Large language models (LLMs) are increasingly used to simulate human collective behavior, yet claims that such simulations are human-like remain lar...

### 33. Do Vision-Language Models Understand Visual Persuasiveness? A Diagnosis via Visual Persuasive Factors
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年11月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2511.17036
- **AI 摘要**: 诊断视觉语言模型是否理解视觉说服力，发现其存在召回偏向、过度预测图像有说服力，并提出视觉说服因素分类法，揭示模型与人类判断的差异。
- **原始摘要**: arXiv:2511.17036v2 Announce Type: replace Abstract: Visual persuasion uses images to shape cognition, emotion, and behavior, with its effects depending on both visual attributes and semantic context....

### 34. DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Reports
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2601.08536
- **AI 摘要**: 提出DeepResearch Bench II基准，含22个领域132项研究任务和9430条细粒度二元评分标准，覆盖信息召回、分析与呈现，由专家文章经LLM加人工流程构建。
- **原始摘要**: arXiv:2601.08536v3 Announce Type: replace Abstract: Deep Research Agents (DRA) aim to help users search the web, synthesize information, and deliver comprehensive investigative reports. Prior benchmar...

### 35. Towards Reliable Medical LLMs: Benchmarking and Enhancing Confidence Estimation of Large Language Models in Medical Consultation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2601.15645
- **AI 摘要**: 提出首个面向真实医疗问诊多轮交互的置信度评估基准，引入信息充分度梯度刻画置信度与正确性的动态关系，并对比27种方法，揭示医疗数据会放大token级与一致性级置信度方法的固有缺陷。
- **原始摘要**: arXiv:2601.15645v2 Announce Type: replace Abstract: Large-scale language models (LLMs) often offer clinical judgments based on incomplete information, increasing the risk of misdiagnosis. Existing stu...

### 36. Evaluating LLM-Simulated Conversations in Modeling Inconsistent and Uncollaborative Behaviors in Human Social Interaction
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.17094
- **AI 摘要**: 重新审视LLM模拟对话的评估，指出人类对话本身包含误解、打断等不一致与不合作行为。提出CoCoEval框架，基于轮级检测10类行为，并提供专业场景基准，用于对比模拟对话与真实人类对话。
- **原始摘要**: arXiv:2603.17094v2 Announce Type: replace Abstract: Simulating human conversations using large language models (LLMs) has emerged as a scalable methodology for modeling human social interaction. This...

### 37. Alignment Reduces Expressed but Not Encoded Gender Bias: A Unified Framework and Study
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.24125
- **AI 摘要**: 提出统一框架，用相同中性提示联合分析LLM内在与外在性别偏见，直接比较内部表征编码的性别信息与生成输出表达的偏见。发现二者在统一协议下存在一致关联，并考察对齐对偏见的影响。
- **原始摘要**: arXiv:2603.24125v3 Announce Type: replace Abstract: During training, Large Language Models (LLMs) learn social regularities that can lead to gender bias in downstream applications. Most mitigation eff...

### 38. Inverse Turing Bench: Evaluating Language Models as Judges of Human vs. AI Dialogue
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.21844
- **AI 摘要**: 提出Inverse Turing Bench基准，用配对对话记录评估LLM区分纯人类对话与人机对话的能力。GPTZero、Claude Opus-4.6和GPT-5.5准确率最高，分别达89.41%、77.92%、75.94%。结果表明统计方法有语义盲点，语义方法易受角色提示影响。
- **原始摘要**: arXiv:2606.21844v2 Announce Type: replace Abstract: As AI systems integrate into online spaces, differentiating them from humans in conversations is increasingly important. We present Inverse Turing B...

### 39. Sympathetic Framing: Evaluating AI Alignment across Sociodemographic Groups
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.27232
- **AI 摘要**: 评估LLM与人类情感感知的对齐程度。以政治地缘冲突新闻标题为材料，3011名英国代表样本与七个LLM判断标题是否引发对某方同情。模型与人类相关性从0.789到0.4不等，领先模型在各人口统计子群体中均与人类判断广泛一致。
- **原始摘要**: arXiv:2607.27232v2 Announce Type: replace Abstract: Large Language Models (LLMs) are increasingly shaping how we consume information and form our worldview. This raises concerns beyond bias in AI: do...

### 40. Causal Episodic Memory for Feedback-Driven Agent Repair
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.05906
- **AI 摘要**: 提出MERIT，一种免训练智能体，维护经预言机验证的修正与失败方向的在线双极记忆，用于Text-to-SQL修复。确定性分类器分配粗粒度失败类型，条件化混合检索器。在Spider上执行准确率从66.34%提升至69.79%，BIRD上从47.35%提升至48.44%。
- **原始摘要**: arXiv:2608.05906v2 Announce Type: replace Abstract: LLM agents that repair failures often discard successful corrections, forcing later episodes to rediscover similar solutions. We study whether final...

### 41. Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 28 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.22230
- **AI 摘要**: 研究LLM仇恨言论审核中标注者风格反驳攻击的脆弱性，涵盖洗白仇恨内容与抹黑正常内容两个方向。提出重判协议，扩展直接矛盾并加入决策边界扰动与对抗性理由。实验显示反驳显著降低审核性能，多轮设置下更强，且存在稳定的模型特定不对称性。
- **原始摘要**: arXiv:2608.22230v3 Announce Type: replace Abstract: Large language models (LLMs) are increasingly used for hate speech moderation, often within human--AI workflows in which reviewers provide feedback...

### 42. OUTLETS: Output-Length Prediction from Speculative Decoding Backbones
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01068
- **AI 摘要**: 提出OUTLETS方法，利用投机解码骨干网络的草稿表示预测LLM输出长度，无需额外代理模型，提升资源调度效率。
- **原始摘要**: arXiv:2609.01068v2 Announce Type: replace Abstract: The heavy-tailed distribution of output lengths in Large Language Model (LLM) serving poses major challenges for resource provisioning and cluster s...

### 43. Limitations of Automated Simulatability: LLM Simulators Can Bypass Explanations
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.08585
- **AI 摘要**: 研究自动化可模拟性评估的局限，发现LLM模拟器可绕过解释直接解题或利用类别匿名化泄漏标签映射，存在捷径问题。
- **原始摘要**: arXiv:2609.08585v2 Announce Type: replace Abstract: Simulatability is an evaluation protocol for explanations that quantifies their usefulness by how well they help a user predict a task model's outpu...

### 44. Evaluating Memory Structure in LLM Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年02月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2602.11243
- **AI 摘要**: 提出StructMemEval基准，测试LLM智能体组织长期记忆结构的能力，而非简单事实召回，弥补现有记忆评估的不足。
- **原始摘要**: arXiv:2602.11243v3 Announce Type: replace-cross Abstract: Modern LLM-based agents and chat assistants rely on long-term memory frameworks to store reusable knowledge, recall user preferences, and augm...

### 45. Proof-Carrying Cognition: Closing the Verification Gap with Reality-Settled Reward
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.09776
- **AI 摘要**: 指出语言模型推理的瓶颈是验证缺口，即形式领域外缺乏可扩展且不可腐蚀的奖励。理论证明验证者与金标准相关性决定测试时计算与能力的兑换率，并在程序合成中验证不健全验证者随优化增长而失效。
- **原始摘要**: arXiv:2609.09776v1 Announce Type: new Abstract: Frontier gains in language-model reasoning come from reinforcement learning on reasoning traces and are concentrated in domains with a cheap, sound veri...

### 46. Why Sample What You Can Enumerate? Exact Policy Optimization for Genomic Tool Selection
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10221
- **AI 摘要**: 指出在工具子集可枚举的专业科学场景中，GRPO从少量采样估计动作期望存在结构性错配，训练成功后优势信号消失。提出FGPO对全部工具子集评分，在基因组推理中解决奖励信号缺失问题。
- **原始摘要**: arXiv:2609.10221v2 Announce Type: new Abstract: Reinforcement learning over a frozen reasoner has become a common recipe for teaching a policy which external tools to invoke. We show that this recipe...

### 47. Smart Adaptive Computing Across the Continuum: LLMs in IoT-Edge-Cloud Resource Management
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.09348
- **AI 摘要**: 扩展DRL持续编排系统分类法，新增AI增强范式与反馈通道两个维度，分析六个近期系统架构，发现共同缺口：云持续环境中无一同时实现完整LLM编排与完整智能体层反馈闭环。
- **原始摘要**: arXiv:2609.09348v1 Announce Type: cross Abstract: Managing resources across IoT, edge, and cloud layers calls for continuous, context-aware decisions under constraints that rarely stay fixed. Deep rei...

### 48. An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.09404
- **AI 摘要**: 提出MMPIBench基准，通过六种视觉载体对智能体AI框架实施多模态提示注入攻击，覆盖720次运行，发现攻击成功率约1%，但尝试率达12.8%，主要受阻于规划环节，模型选择影响显著。
- **原始摘要**: arXiv:2609.09404v1 Announce Type: cross Abstract: Agentic AI frameworks let a language model plan, keep memory, and call tools that reach real files, mail, and services. Most of these agents also read...

### 49. Kernel-Complexity Edge Sanitization for Training-Free Defense against Structural Graph Attacks
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.09698
- **AI 摘要**: 提出KCES无训练模型无关的图结构攻击防御框架，基于图Gram矩阵导出图核复杂度度量，定义边级KC分数并剪除高KC边，可有效识别并移除对抗性扰动边。
- **原始摘要**: arXiv:2609.09698v1 Announce Type: cross Abstract: Graph Neural Networks (GNNs) have achieved remarkable success across diverse applications, yet they remain highly vulnerable to adversarial attacks th...

### 50. Non-Stationarity Breaks Permutation Surrogates in Multi-Agent Reinforcement Learning: Diagnosis and Remedies
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.23716
- **AI 摘要**: 发现多智能体强化学习中非平稳性会破坏置换代理方法，导致假阳性率近100%，建议改变零模型而非简单剔除训练暂态。
- **原始摘要**: arXiv:2604.23716v4 Announce Type: replace Abstract: Reporting guidance for information-theoretic measures is rarely tested against ground truth. We test one guardrail in two multi-agent reinforcement...

### 51. A Composable Evaluation System for Reproducible Omni-Modal Foundation Model Evaluation
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.01315
- **AI 摘要**: 提出OmniEvaluator可组合评估系统，统一连接多种推理引擎与评估框架，支持全模态基础模型可复现评估与跨模型比较。
- **原始摘要**: arXiv:2609.01315v2 Announce Type: replace Abstract: Building an omni-modal foundation model means evaluating it across text, image, video, and audio. Excellent evaluation toolkits exist for each modal...

### 52. A Taxonomy of Architecture Options for Foundation Model-based Agents: Analysis and Decision Model
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2024年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2408.02920
- **AI 摘要**: 提出基于基础模型智能体的架构分类法，涵盖功能与非功能属性及设计运行时操作，并建立指导关键决策的决策模型。
- **原始摘要**: arXiv:2408.02920v2 Announce Type: replace-cross Abstract: The rapid advancement of AI technology has led to widespread applications of agent systems across various domains. However, the need for detai...

### 53. MOSAIC: A Universal Agent-Level Interface for Cross-Paradigm Agent Mixing and Human-AI Collaboration
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2603.01260
- **AI 摘要**: 提出MOSAIC开源平台，通过IPC工作协议和算子抽象，使RL策略、LLM、VLM与人类操作者能在同一强化学习环境中混合协作，实现跨范式公平对比与可复现的人机协作。
- **原始摘要**: arXiv:2603.01260v3 Announce Type: replace-cross Abstract: Existing infrastructure cannot deploy agents from different decision-making paradigms within the same environment, making fair cross-paradigm...

### 54. The Truth Was Never Gone: Perfect Aliasing in Compliant-Context Truth Probes
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10739
- **AI 摘要**: 揭示合规语境下真值探针与规定动作探针存在完美混叠，二者AUROC互补为1；通过随机码本与混合语境拟合可分离真值与规定动作，使奖励训练策略的探针AUROC从0.006提升至1.000。
- **原始摘要**: arXiv:2609.10739v1 Announce Type: new Abstract: A truth probe fitted where truthful reporting and a task's prescribed action coincide cannot distinguish those targets from its fitting labels alone. We...

### 55. Certifying Lower Bounds for Risk-Sensitive Reinforcement Learning under Adversarial State Perturbations
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10866
- **AI 摘要**: 针对对抗状态扰动下的风险敏感强化学习，通过φ散度松弛将认证问题转化为凸优化并求对偶，给出累积奖励指数效用下界，提出提升认证下界的经验方法。
- **原始摘要**: arXiv:2609.10866v1 Announce Type: new Abstract: Reinforcement learning (RL) agents deployed in real-world environments are often vulnerable to adversarial perturbations in state observations, creating...

### 56. Phase-Decoupled, Model-Calibrated Power Control for Disaggregated LLM Serving
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11133
- **AI 摘要**: 针对预填充/解码分离的LLM服务，发现Max-Q推理配置增益有限且增加延迟，提出相位解耦、模型校准的功耗控制器，为预填充与解码分别配置SM时钟窗口并在SLO保护下将余量转化为能效。
- **原始摘要**: arXiv:2609.11133v1 Announce Type: new Abstract: Datacenter GPU power is the binding constraint on LLM serving capacity, and production serving has shifted to prefill/decode (PD) disaggregation. Deploy...

### 57. MUC-FL: Block-Wise Marginal Utility Contribution for Communication-Efficient Federated Learning
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10545
- **AI 摘要**: 提出MUC-FL联邦学习框架，按块对模型性能的边际效用贡献选择性传输数据块。在MIMIC多模态数据上仅1.76%的块携带有效信号，可减少45-50%通信量并提升F1分数。
- **原始摘要**: arXiv:2609.10545v1 Announce Type: cross Abstract: Federated Learning (FL) enables distributed model training without centralizing data but suffers from high communication overhead. To address this, we...

### 58. SynCo: Synthetic Community-Aware Attributed Graph Generator for Graph Neural Network Benchmarking
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.10742
- **AI 摘要**: 提出SynCo，一种面向图神经网络基准测试的合成社区感知属性图生成器，针对现有生成器过度依赖幂律度分布、缺乏高质量社区检测数据集的问题，生成更贴近真实社交网络的图。
- **原始摘要**: arXiv:2609.10742v1 Announce Type: cross Abstract: Graph Neural Networks (GNNs) are powerful models for handling attributed graphs in tasks such as classification, link prediction, and community detect...

### 59. Risk-Averse Decision Making with Multi-Level Reliability Guarantees
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11524
- **AI 摘要**: 研究多级可靠性保证下的风险规避决策，将加权平均证书最大化等价为嵌套预测集优化，连接保形预测并给出对偶形式，在无线传输系统中刻画多可靠性级别的Pareto权衡。
- **原始摘要**: arXiv:2609.11524v1 Announce Type: cross Abstract: Many applications in engineering, including wireless broadcasting, require designs that provide performance certificates at different target outage le...

### 60. FluxMoE: Decoupling Expert Residency for High-Performance MoE Serving
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.02715
- **AI 摘要**: 提出FluxMoE，通过专家分页抽象将专家与GPU物理驻留解耦，结合PagedTensor、压缩GPU内存与主机DRAM的带宽均衡层级及预算感知驻留规划器，按需流式加载权重，在vLLM上实现最高7.2倍吞吐提升。
- **原始摘要**: arXiv:2604.02715v3 Announce Type: replace Abstract: Mixture-of-Experts (MoE) models have become mainstream for scaling language models to hundreds of billions of expert parameters. Despite sparse expe...

### 61. Statistically Valid Post-Training Hyperparameter Selection: From Tuning to Guarantees
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.25601
- **AI 摘要**: 面向现代AI系统部署后的超参数选择，提出以learn-then-test为核心的统一统计框架，将超参选择建模为多重假设检验，从而为可靠性提供形式化统计保证。
- **原始摘要**: arXiv:2606.25601v2 Announce Type: replace-cross Abstract: Post-training hyperparameter selection is a critical step in the deployment of modern artificial intelligence systems, given the need to tune...

### 62. EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2606.18239
- **AI 摘要**: EBench是诊断通用移动操作策略的仿真基准，含26个任务，按5个能力维度和4个泛化维度标注。评测π0、π0.5、XVLA、InternVLA-A1等模型，揭示其能力画像差异，并从4个视角分析分布偏移下的泛化能力。
- **原始摘要**: arXiv:2606.18239v3 Announce Type: replace Abstract: We present EBench, a simulation benchmark that diagnoses generalist mobile manipulation policies beyond a single success-rate scalar. EBench compris...

### 63. Design and Implementation of a Kalman Filter-Infused Algorithm for Tilt Estimation
- **来源**: arXiv cs.RO (机器人) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.00730
- **AI 摘要**: 基于MPU6050与RP2040平台设计单轴倾角估计系统，利用卡尔曼滤波融合加速度计与陀螺仪数据，兼顾长期稳定与短期平滑，并完成仿真与硬件实验。
- **原始摘要**: arXiv:2609.00730v2 Announce Type: replace-cross Abstract: Accurate tilt angle estimation is important in many engineering applications, such as robotics, motion tracking, and embedded control systems....

### 64. ShellVis: Sandboxed Live Programming for Shell Scripts
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年09月 (约 -3 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2609.11000
- **AI 摘要**: ShellVis通过沙箱化实现Shell脚本的实时编程，将文件操作限制在安全文件系统覆盖层中，逐行反馈运行时行为。用户评估显示其有帮助，能替代繁琐实践并增强信心。
- **原始摘要**: arXiv:2609.11000v1 Announce Type: cross Abstract: Live programming provides visibility to programmers by running and tracing programs as they are edited. However, for programs with potentially harmful...

### 65. AlignmentAutomated researchers can reliably mitigate alignment failures
- **来源**: Anthropic Research (TIER1)
- **发布日期**: Aug 28, 2026
- **类型**: research
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures
- **AI 摘要**: 探讨自动化研究者如何可靠地缓解对齐失败问题，提升AI系统的安全性与可控性。

### 66. Frontier Red TeamPatterns and problems in emerging multiagent systems
- **来源**: Anthropic Research (TIER1)
- **发布日期**: Aug 13, 2026
- **类型**: research
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.anthropic.com/research/multiagent-systems
- **AI 摘要**: 前沿红队分析新兴多智能体系统中的模式与问题，探讨多智能体协作带来的安全挑战。

### 67. Rapidly scaling online storage to serve over 1 billion ChatGPT usersEngineeringSep 11, 2026
- **来源**: OpenAI News (TIER1)
- **发布日期**: 2026-09-11T10:00
- **类型**: news
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://openai.com/index/scaling-storage-one-billion-users-part-one/
- **AI 摘要**: 介绍如何快速扩展在线存储系统，以支撑超过10亿ChatGPT用户的使用需求，属于大规模AI基础设施工程实践。

### 68. DeepSeek V4-Pro GA: Agent Frameworks & New Surge Pricing Guide
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-08-16
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://deepseek.ai/blog/deepseek-v4-pro-ga-harness-surge-pricing-guide-2026
- **AI 摘要**: DeepSeek发布V4-Pro GA、Harness智能体框架及行业首创高峰定价。介绍如何优化思考投入并利用非高峰AI费率。
- **原始摘要**: DeepSeek launches V4-Pro GA, the DeepSeek Harness agent framework, and industry-first surge pricing. Learn how to optimize 'Thinking Effort' and leverage off-peak AI rates.

### 69. DeepSeek Harness Explained: The Open-Source, Plugin-First Alternative to Claude Code
- **来源**: DeepSeek Blog (TIER1)
- **发布日期**: 2026-08-16
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://deepseek.ai/blog/deepseek-harness-open-source-claude-code-alternative
- **AI 摘要**: DeepSeek Harness是基于Cordis的MIT开源编码智能体运行时，模型、工具、会话和UI均可热插拔，文章介绍安装、架构及与Claude Code对比。
- **原始摘要**: A free, MIT-licensed coding agent runtime built on Cordis, where every capability — models, tools, sessions, even the UI — is a hot-swappable plugin. Install steps, architecture, Claude Code compariso...

### 70. DeepSeek V4-Pro GA: Agent Frameworks & New Surge Pricing Guide
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-08-16
- **类型**: research
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://deepseek.ai/blog/deepseek-v4-pro-ga-harness-surge-pricing-guide-2026
- **AI 摘要**: DeepSeek发布V4-Pro GA、Harness智能体框架及行业首创高峰定价。介绍如何优化思考投入并利用非高峰AI费率。
- **原始摘要**: DeepSeek launches V4-Pro GA, the DeepSeek Harness agent framework, and industry-first surge pricing. Learn how to optimize 'Thinking Effort' and leverage off-peak AI rates.

### 71. DeepSeek Harness Explained: The Open-Source, Plugin-First Alternative to Claude Code
- **来源**: DeepSeek Research (TIER1)
- **发布日期**: 2026-08-16
- **类型**: research
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://deepseek.ai/blog/deepseek-harness-open-source-claude-code-alternative
- **AI 摘要**: 介绍DeepSeek Harness，一个基于Cordis构建的开源MIT许可编码代理运行时，所有能力均可热插拔，并附安装步骤、架构说明及与Claude Code的对比。
- **原始摘要**: A free, MIT-licensed coding agent runtime built on Cordis, where every capability — models, tools, sessions, even the UI — is a hot-swappable plugin. Install steps, architecture, Claude Code compariso...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
