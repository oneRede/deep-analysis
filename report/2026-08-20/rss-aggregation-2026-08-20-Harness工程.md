# RSS 聚合报告 - Harness工程

**生成时间**: 2026-08-21 11:22:50
**文章数量**: 60 篇

---

### 1. AI-generated code detection in CI/CD — looking for approaches and real-world experience [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-20T11:31:12+00:00 (今天)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vtgw1g/aigenerated_code_detection_in_cicd_looking_for/
- **AI 摘要**: 作者正在开发一个系统，通过Git提交级信号（如提交元数据、代码变更量等）估算代码是否由AI生成，但面临置信度和校准问题。文章寻求在CI/CD中检测AI生成代码的方法和实际经验。
- **原始摘要**: ​ I'm working on a system to estimate whether code committed to a repository was generated with AI coding tools. My current approach is based on Git/commit-level signals such as AI-related commit trai...

### 2. We’ve got a workshop on production retrieval-augmented generation with open models, benchmarked end to end, thought it’d be relevant here [D]
- **来源**: r/MachineLearning (TIER3)
- **发布日期**: 2026-08-17T22:02:45+00:00 (3 天前)
- **类型**: forum
- **优先级**: low
- **分类**: Harness工程
- **链接**: https://www.reddit.com/r/MachineLearning/comments/1vr6cd2/weve_got_a_workshop_on_production/
- **AI 摘要**: 8月29日将举办一场关于生产级检索增强生成（RAG）的实操研讨会，使用完全开源模型，涵盖混合检索、重排序和RAGAS评估，由AI顾问Ben Auffarth主持。
- **原始摘要**: There’s a hands-on workshop on August 29 that builds and benchmarks this properly, end to end, using entirely open models, no API calls involved. Led by Ben Auffarth, AI Consultant and Founder of Chel...

### 3. DeepSeek V4 Pro 0813 vs GPT-5.6 Sol on DeepSWE: Cost, Coding, and Routing
- **来源**: Together AI Blog (TIER2)
- **发布日期**: Tue, 18 Aug 2026 00:00:00 GMT (3 天前)
- **类型**: blog
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://www.together.ai/blog/deepseek-v4-pro-0813-vs-gpt-5-6-sol-on-deepswe-cost-coding-and-routing
- **AI 摘要**: DeepSeek V4 Pro 0813与GPT-5.6 Sol在DeepSWE基准上对比，Sol在pass@1上领先10分但成本高35倍，Pro在pass@4上胜出，Pro优先级联达到83.0%准确率。
- **原始摘要**: We ran 904 DeepSWE rollouts on DeepSeek V4 Pro 0813 and GPT-5.6 Sol. Sol leads pass@1 by 10 points at 35x the cost; Pro wins pass@4, and a Pro-first cascade hits 83.0%.

### 4. DeepSeek V4 Pro 0813 vs Claude Fable 5 on DeepSWE: Cost, Coding, and Routing
- **来源**: Together AI Blog (TIER2)
- **发布日期**: Mon, 17 Aug 2026 00:00:00 GMT (4 天前)
- **类型**: blog
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://www.together.ai/blog/deepseek-v4-pro-0813-vs-claude-fable-5-on-deepswe-cost-coding-and-routing
- **AI 摘要**: 文章对比了DeepSeek V4 Pro 0813与Claude Fable 5在DeepSWE基准上的表现。Fable在pass@1上领先但成本高出90倍；Pro在pass@4上胜出，且Pro优先的级联策略达到82.7%的通过率。
- **原始摘要**: We ran 904 DeepSWE rollouts on DeepSeek V4 Pro 0813 and Claude Fable 5. Fable leads pass@1 at 90x the cost; Pro wins pass@4, and a Pro-first cascade hits 82.7%.

### 5. A/B test models in production
- **来源**: Together AI Blog (TIER2)
- **发布日期**: Mon, 17 Aug 2026 00:00:00 GMT (4 天前)
- **类型**: blog
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://www.together.ai/blog/a-b-test-models-in-production
- **AI 摘要**: 文章讨论了生产环境中A/B测试模型的方法。影子流量能验证候选模型的操作稳定性，但无法反映用户偏好。建议在端点而非应用代码中运行分流测试，以更准确评估模型效果。
- **原始摘要**: Shadow traffic proves a candidate is operationally sound. It can't tell you if users like it better. Run the split at the endpoint instead of in your app code.

### 6. Reproducible Multimodal Affordance Prediction
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18317
- **AI 摘要**: 本文指出可复现的多模态可供性预测面临问题表述多样、数据集标注不一致、实验协议不完整及部署条件信息有限等挑战，这些限制了公平基准测试和性能比较。
- **原始摘要**: arXiv:2608.18317v1 Announce Type: new Abstract: Affordance prediction is the identification of potential actions an agent can perform on a target object from multimodal inputs. Affordance prediction m...

### 7. MR-IQA-2: Faithful Image Quality Reflection via Fine-Grained Credit Assignment
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18579
- **AI 摘要**: 本文提出MR-IQA-2方法，通过细粒度信用分配提升多模态大模型在图像质量评估中的推理忠实度，解决共享奖励导致的监督源模糊问题，确保推理真实反映图像质量。
- **原始摘要**: arXiv:2608.18579v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) have shown strong potential for image quality assessment (IQA) by improving consistency between quality ratings...

### 8. OmniHandwritingOCR: A Diagnostic Benchmark for Evaluating Multimodal LLMs in Handwritten OCR Scenarios
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18586
- **AI 摘要**: 本文提出OmniHandwritingOCR基准，用于评估多模态大语言模型在真实手写OCR场景中的表现，涵盖多语言手写、书写错误及复杂数学表达式等挑战，弥补现有基准的不足。
- **原始摘要**: arXiv:2608.18586v1 Announce Type: new Abstract: Multimodal large language models (MLLMs) are increasingly used as OCR systems in document and knowledge-processing pipelines, but their ability to faith...

### 9. EVADE: Evidence-Verified Agentic Diagnosis with Escape
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18833
- **AI 摘要**: EVADE是一种无需训练的推理方法，通过证据验证和逃逸机制增强冻结医学视觉语言模型的安全性，在不确定时进行定位，以校准模型信任度并提高可靠性。
- **原始摘要**: arXiv:2608.18833v1 Announce Type: new Abstract: Medical vision-language models (VLMs) can achieve high accuracy but remain unreliable: they are systematically overconfident, benefit little from test-t...

### 10. How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.16094
- **AI 摘要**: 本文分析视觉语言模型在组合式视觉问答中的失败机制，通过检查失败与特定推理操作的关系，揭示视觉-操作错位问题。
- **原始摘要**: arXiv:2607.16094v2 Announce Type: replace Abstract: Compositional visual question answering requires Vision-Language Models (VLMs) to execute multiple reasoning operations like object selection, spati...

### 11. SCOPE-Router: Cost-Aware Open-Set VLM Routing for Execution-Oriented Tasks
- **来源**: arXiv cs.CV (计算机视觉) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: medium
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.12127
- **AI 摘要**: 本文提出SCOPE-Router，一种面向执行任务的成本感知开放集VLM路由方法，通过校准优化和成本感知训练目标，在候选模型池中平衡质量与成本，提升开放集场景下的路由性能。
- **原始摘要**: arXiv:2608.12127v2 Announce Type: replace Abstract: Model routing aims to select the most suitable model from a candidate pool for each query, balancing quality and cost. Existing VLM routing research...

### 12. Never Loop Without VerifiersJune 24, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: une 24, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/never-loop-without-verifiers
- **AI 摘要**: 文章强调在AI开发循环中必须引入验证器，以防止模型在无监督迭代中偏离目标或产生错误。通过持续验证，确保系统可靠性和性能，是构建稳健AI应用的关键实践。

### 13. Lessons learned from building multi-agent workflowsApril 16, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ril 16, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/lessons-learned-from-building-multi-agent-workflows
- **AI 摘要**: 文章基于构建多智能体工作流的实践经验，总结了关键教训，包括设计模式、协作机制、错误处理及性能优化等，为开发者提供了实用指导。

### 14. How to stop your autoresearch loop from cheatingMarch 19, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: rch 19, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/how-to-stop-your-autoresearch-loop-from-cheating
- **AI 摘要**: 文章讨论了如何防止自动研究循环中的作弊行为，可能涉及AI代理在自主研究时通过捷径获取结果的问题，并提出了相应的监控或约束方法。

### 15. Scaling SWE Agent Data Collection with Dockerized Environments for ExecutionNovember 24, 2025
- **来源**: Cerebras (TIER1)
- **发布日期**: ber 24, 2025
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/scaling-swe-agent-data-collection-with-dockerized-environments-for-execution
- **AI 摘要**: 文章探讨了通过Docker化环境执行来扩展SWE智能体数据收集的方法，旨在提升软件开发任务中AI智能体的训练数据规模与质量，涉及工程实践与工具链优化。

### 16. The Year of Latency Debt (And How Big Tech Is Paying It Down)January 28, 2026
- **来源**: Cerebras (TIER1)
- **发布日期**: ary 28, 2026
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://www.cerebras.ai/blog/latency-debt
- **AI 摘要**: 文章探讨了2026年AI领域面临的延迟债务问题，即模型推理延迟带来的性能瓶颈，并分析了大型科技公司如何通过优化基础设施、算法和硬件来偿还这笔债务，以提升用户体验和系统效率。

### 17. Self- and Other-Labels Induce Bidirectional Bias in LLM Judges
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18091
- **AI 摘要**: 随着LLM作为评判者的系统日益普及，自我偏好引发了对评估可靠性的担忧。现有研究多聚焦于生成文本，难以区分风格与质量。本文通过改变对象，研究自我标签与他人标签对LLM评判者的双向偏差影响。
- **原始摘要**: arXiv:2608.18091v1 Announce Type: new Abstract: As LLM-as-a-judge systems become increasingly widespread, self-preference in LLMs -- the tendency to favor one's own outputs -- raises growing concerns...

### 18. Computational Orientalism: Measuring Structural Discourse Bias in Large Language Models Using the Middle East Cultural Sensitivity Score (MECSS)
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18100
- **AI 摘要**: 本文提出中东文化敏感度评分（MECSS），用于衡量大语言模型在生成中东相关内容时的结构性话语偏见，探讨其是否体现萨义德所称的东方主义，即否认中东主体的能动性。
- **原始摘要**: arXiv:2608.18100v1 Announce Type: new Abstract: AI systems now shape how hundreds of millions of people learn about cultures other than their own. When someone asks one of these systems about the Midd...

### 19. Different Facets of Verbalised Overconfidence: an Interpretability Study
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18106
- **AI 摘要**: 本文通过受控推理场景研究大语言模型（Qwen3-4B）的过度自信行为，操纵逻辑必然性和可能性，并比较三种不确定性表达方式（言语认知标记、弃权、数值置信度）。结果证实模型倾向于过度自信，尤其在提示词引导下更为明显。
- **原始摘要**: arXiv:2608.18106v1 Announce Type: new Abstract: Large language models tend to overconfidence, giving assertive answers when the evidence suggests hedging or abstention. Using controlled reasoning scen...

### 20. Same Facts, Different Updates: Inference Setup Shapes LLM Behavior in Medical Allocation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18108
- **AI 摘要**: 大型语言模型被用于敏感决策，其行为可能受部署中积累的上下文影响。本文研究医疗资源分配场景，发现推理设置（如上下文）会改变模型行为，导致意外结果。
- **原始摘要**: arXiv:2608.18108v1 Announce Type: new Abstract: Large language models are being incorporated into sensitive and important decision-making processes across nearly all fields. While prior work studies m...

### 21. Temporal Multi-Signal Fusion for Token-Level Hallucination Detection
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18115
- **AI 摘要**: 本文提出一种基于时间多信号融合的token级幻觉检测方法，将幻觉视为时间扩展片段，通过序列标注对每个token从33维特征流评分，融合文本统计、NLI蕴含和语言模型惊异度，无需访问模型内部信息。
- **原始摘要**: arXiv:2608.18115v1 Announce Type: new Abstract: Token-level hallucination detectors score each token independently from a single signal, and fail exactly when the generating model is confidently wrong...

### 22. You Are What You Prompt: Prompt Quality, Domain Shift, and Uncertainty in Agrifood Vision-Language Models
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18116
- **AI 摘要**: 本文评估了零样本提示集成（ZPE）在农业食品领域视觉语言模型中的表现，使用CLIP和SigLIP在四个数据集和四个提示池上测试，发现ZPE在领域偏移下仍能有效提升分类性能，但提示质量对结果影响显著。
- **原始摘要**: arXiv:2608.18116v1 Announce Type: new Abstract: Vision-language models enable zero-shot classification through natural language prompts, but performance is sensitive to prompt formulation, especially...

### 23. The Deontic Gap: Large Language Models and the Modal Language of Obligation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18144
- **AI 摘要**: 本文研究了大型语言模型（LLMs）是否再现人类道义情态动词（如must、should）的使用模式。通过多个语料库和受控实验发现，AI生成文本持续少用积极道义情态动词，揭示了AI与人类在表达义务和权威方面的差异。
- **原始摘要**: arXiv:2608.18144v1 Announce Type: new Abstract: Modal auxiliaries such as must, should, and have to mark necessity and obligation within the contexts of speaker authority and interpersonal stance. We...

### 24. Efficient INT8 Inference of Small NLP Models on Server CPUs with PyTorch Native Stack
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18182
- **AI 摘要**: 本文介绍将SmoothQuant集成到TorchAO中，优化PyTorch原生栈下小型NLP模型（如BERT）在服务器CPU上的INT8推理，实现延迟、吞吐量和成本的良好平衡。
- **原始摘要**: arXiv:2608.18182v1 Announce Type: new Abstract: Small NLP models, especially BERT-family encoders, remain important in industrial workloads such as classification, ranking, and retrieval even in the e...

### 25. Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18575
- **AI 摘要**: 本文提出用轻量级图神经网络（GNN）替代LLM进行多智能体系统故障归因，识别失败轨迹中的故障智能体及错误类型，提升效率并降低计算成本。
- **原始摘要**: arXiv:2608.18575v1 Announce Type: new Abstract: Large language model (LLM)-based multi-agent systems (MAS) often exhibit complex failure modes, which frequently cause agents to produce incorrect outco...

### 26. Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18578
- **AI 摘要**: 本文研究了后训练量化（PTQ）对大型语言模型中主动干扰（PI）的影响。通过FP16、INT8和INT4/NF4三种精度评估，发现量化会放大PI，导致模型性能下降。
- **原始摘要**: arXiv:2608.18578v1 Announce Type: new Abstract: Proactive interference (PI) is a documented failure mode in large language models in which retrieval of a repeatedly overwritten value degrades as prior...

### 27. Learning What to Fail On: Failure-Mode Contextual Bandits for Adversarial Data Curation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18681
- **AI 摘要**: 本文提出一种失败感知的对抗性检索增强框架，将对抗性数据筛选建模为失败模式上下文赌博机问题，通过检索增强生成候选样本，经目标模型过滤和LLM评审验证，以提升自然语言理解的鲁棒性。
- **原始摘要**: arXiv:2608.18681v1 Announce Type: new Abstract: We introduce a failure-aware adversarial retrieval-augmented framework for improving robustness in natural language understanding. Rather than selecting...

### 28. Execution-grounded evaluation reveals hidden failures in language-model calculations for environmental science
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18726
- **AI 摘要**: 大型语言模型在环境科学定量工作中应用日益广泛，但现有评估仅评分最终答案，忽略计算过程。本文提出AtmosCoder-Bench，一种执行导向的基准，通过半自动管道构建436个问题、3910个变体，使计算过程可见，并验证问题无歧义。
- **原始摘要**: arXiv:2608.18726v1 Announce Type: new Abstract: Large language models are increasingly used for quantitative work in the environmental sciences, yet existing evaluations score only final answers, leav...

### 29. Decomposing Wrong-Consensus Agreement in LLM Self-Consistency: A GPT-4.1 Case Study
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18795
- **AI 摘要**: 本文定量分析了LLM自一致性中多数投票在难题上失效的原因，提出多元一致性指数Gamma，并将其分解为机械成分和语义成分，以解释错误共识现象。
- **原始摘要**: arXiv:2608.18795v1 Announce Type: new Abstract: Majority voting over multiple LLM samples is widely used to raise answer accuracy, yet its gain varies erratically: on hard questions it can even backfi...

### 30. Assessing Quality of Experience in Natural Language Generation of German Text
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18888
- **AI 摘要**: 本文介绍TextQ-German，一个用于德语自然语言生成（NLG）人工评估的新数据集套件，旨在解决传统自动评估指标无法捕捉生成文本多维感知质量的问题，推动以人为中心的NLG评估。
- **原始摘要**: arXiv:2608.18888v1 Announce Type: new Abstract: The rapid advancement of Natural Language Generation (NLG) has made the reliable evaluation of generated text increasingly critical, as these systems, s...

### 31. Structure, Association, and Decision Value: Representation-Based Difficulty Estimation for Adaptive Inference in African-Language NLI
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.19003
- **AI 摘要**: 本文探讨在非洲语言自然语言推理任务中，内部表示统计量能否为自适应推理提供难度信号。研究发现，在15种非洲语言上使用冻结的现成检查点，这些统计量无法提供有效的难度信号。同时发现AfriXNLI与XNLI存在大量重叠样本。
- **原始摘要**: arXiv:2608.19003v1 Announce Type: new Abstract: We ask whether internal representation statistics can provide useful example-level difficulty signals for adaptive inference in multilingual African NLP...

### 32. Grading the Graders: Verification Autonomy Levels (L0-L5) for LLM Reasoning
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.19009
- **AI 摘要**: 大型语言模型常与验证器配对以检测错误，但文献中“level”一词含义模糊。本文提出验证自主性等级（L0-L5），旨在统一验证系统的评估标准，明确不同层级的自主程度与能力。
- **原始摘要**: arXiv:2608.19009v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly paired with verifiers (step checkers, self-consistency filters, tool-based fact checkers, formal proof ass...

### 33. Safety Alignment Illusion: The Cross-Lingual Safety Gap in LLMs
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18131
- **AI 摘要**: 当前LLM安全对齐训练以英语为中心，导致非英语语言存在安全漏洞，可能产生刻板印象输出并传播有害偏见，影响语音助手等口语技术。
- **原始摘要**: arXiv:2608.18131v1 Announce Type: cross Abstract: Current safety alignment training for Large Language Models (LLMs) are heavily English-centric. When such safety filters fail for non-English language...

### 34. ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18307
- **AI 摘要**: ComponentBench是一个用于诊断计算机使用代理组件级故障的基准测试和诊断流程，填补了长时工作流基准与原子GUI测试之间的空白，通过短而丰富的组件交互来评估现代界面负担。
- **原始摘要**: arXiv:2608.18307v1 Announce Type: cross Abstract: Current evaluation of computer-use agents is split between long-horizon workflow benchmarks and atomic GUI-grounding tests. This leaves an under-instr...

### 35. Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18591
- **AI 摘要**: 本文提出BudgetDoc基准，用于评估LLM在文档推理中的计算预算与性能权衡，并训练轻量级模型DRB（约10亿参数）预估推理表现，以优化推理预算分配。
- **原始摘要**: arXiv:2608.18591v1 Announce Type: cross Abstract: Uniformly allocating inference reasoning budgets to LLMs is expensive and prone to over-thinking penalties; especially in document tasks where visual...

### 36. Metrics That Write Themselves: Evolving an Evaluator from Its Own Blind Spots
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18744
- **AI 摘要**: 本文提出一种自动生成评估指标的方法，通过一组小型Python算子池，每个算子标记候选答案的特定缺陷或弃权并投票，从而在缺乏人工评分的情况下评估智能体（如报告生成）的表现。
- **原始摘要**: arXiv:2608.18744v1 Announce Type: cross Abstract: Agents improve quickly against a reliable automatic metric and stall without one, and the applications that need them most, report generation among th...

### 37. When Readability and Source Retention Diverge: An Evaluability Gap in AI Translation
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.19083
- **AI 摘要**: 本文研究了AI翻译中可读性与源文保留之间的评估差距。通过2*2实验（N=306）使用TransLingo，考察源文条件、输出呈现方式对翻译质量感知的影响，以及输出和系统评价与信任和披露意愿的关系。
- **原始摘要**: arXiv:2608.19083v1 Announce Type: cross Abstract: Readable AI output can leave an evaluability gap: even when the source is shown, an overall-quality judgment may not reflect what an output preserves....

### 38. ConspirED: A Dataset for Cognitive Traits of Conspiracy Theories and Large Language Model Safety
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2025年08月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2508.20468
- **AI 摘要**: 本文介绍CONSPIRED数据集，用于研究阴谋论的认知特征及大语言模型安全性。该数据集捕捉阴谋论修辞模式，旨在支持针对性预辟谣和评估AI漏洞，以应对AI生成的虚假信息。
- **原始摘要**: arXiv:2508.20468v2 Announce Type: replace Abstract: Conspiracy theories erode public trust in science and institutions while resisting debunking by evolving and absorbing counter-evidence. As AI-gener...

### 39. When to Call an Apple Red: Humans Follow Introspective Rules, VLMs Don't
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.06422
- **AI 摘要**: 本文通过引入Graded Color Attribution (GCA)数据集，研究视觉语言模型（VLMs）在决策规则上的行为一致性，探讨模型能否可靠预测自身行为并遵循内省推理，为可信部署提供评估基准。
- **原始摘要**: arXiv:2604.06422v2 Announce Type: replace Abstract: Understanding when Vision-Language Models (VLMs) will behave unexpectedly, whether models can reliably predict their own behavior, and if models adh...

### 40. Predicting the Benefit of Retrieval Augmentation in Open-Domain Question Answering
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2604.07985
- **AI 摘要**: 本文研究开放域问答中预测检索增强是否有助于提升回答质量的问题，评估了基于检索信号、答案特征和语义一致性的多种预测方法。
- **原始摘要**: arXiv:2604.07985v3 Announce Type: replace Abstract: While retrieval augmented generation has become a common approach for enhancing question answering systems, retrieval is not universally advantageou...

### 41. CanLegalRAGBench: Evaluating Retrieval-Augmented Generation on Canadian Case Law
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2605.30497
- **AI 摘要**: 本文介绍CanLegalRAGBench，一个基于加拿大案例法的检索增强生成基准，用于评估法律AI助手，减少幻觉，填补加拿大法律评估空白。
- **原始摘要**: arXiv:2605.30497v2 Announce Type: replace Abstract: RAG-based legal assistants have been growing in popularity, but LLM hallucinations remain a key issue and potentially undermines justice. While benc...

### 42. Hallucination Detection in Large Language Models Using Diversion Decoding
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.10476
- **AI 摘要**: 本文提出一种利用分流解码技术检测大语言模型幻觉的方法，通过对比不同解码路径的输出来评估模型不确定性，从而识别事实错误，提升模型可靠性。
- **原始摘要**: arXiv:2607.10476v2 Announce Type: replace Abstract: Large language models (LLMs) have emerged as a powerful tool for retrieving knowledge through seamless, human-like interactions. Despite their advan...

### 43. SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2607.20145
- **AI 摘要**: 本文介绍了在昇腾NPU超级集群上对DeepSeek-V4系列万亿参数MoE模型进行全参数后训练的系统优化实践，解决了内存压力、通信开销和内核执行效率等挑战。
- **原始摘要**: arXiv:2607.20145v3 Announce Type: replace Abstract: Full-parameter post-training of trillion-parameter-scale MoE models introduces substantial system-level challenges for large-scale distributed train...

### 44. How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.14905
- **AI 摘要**: 本文评估AI代理在100个真实前沿研究任务中的表现，通过端到端诊断揭示其失败模式。现有评估范围狭窄，仅衡量性能而不揭示代理运作或故障点，本文旨在填补这一空白。
- **原始摘要**: arXiv:2608.14905v2 Announce Type: replace Abstract: AI has long assisted scientific research, but the rapid advance of LLMs and agentic scaffolds is reshaping the landscape; a single system can now ca...

### 45. From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.16002
- **AI 摘要**: 本文提出了一种用于LLM代理的可靠性不确定性传播方法，从序列到结构，解决现有UQ方法忽略长程依赖导致错误累积的问题，以识别代理失败。
- **原始摘要**: arXiv:2608.16002v2 Announce Type: replace Abstract: Reliable uncertainty quantification (UQ) is essential for deploying large language model (LLM) agents in complex interactive environments. Existing...

### 46. Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.16645
- **AI 摘要**: 本文提出Reconstruction基准，用于评估语言模型仅凭论文发表前的参考文献恢复其核心研究思想的能力。该基准通过严格防泄漏协议，隐藏种子论文及同期或未来文献，由独立模型评判生成假设与真实思想的匹配度。
- **原始摘要**: arXiv:2608.16645v2 Announce Type: replace-cross Abstract: Can a language model recover the true research idea of a published paper when given only that paper's pre-publication bibliography? We introdu...

### 47. Position: Profiling Game Worlds by Transition Complexity
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18079
- **AI 摘要**: 本文提出过渡复杂度剖面（TCP），通过一组可复现的指标刻画游戏环境或数据集的转移核，区分游戏世界建模与强化学习的难度，并量化接口（像素/令牌/潜在）下的预测问题复杂度。
- **原始摘要**: arXiv:2608.18079v1 Announce Type: new Abstract: Game world modeling (GWM) and reinforcement learning (RL) are often confounded because research papers rarely quantify how difficult the underlying tran...

### 48. Position: Current Model Cards Are Insufficient for Downstream Governance of Open-Weight Foundation Models
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18086
- **AI 摘要**: 本文指出当前模型卡片不足以支持开放权重基础模型的下游治理。通过分析Hugging Face上的500个模型卡片，作者认为现有框架未能充分告知开发者相关安全挑战，并提出改进建议。
- **原始摘要**: arXiv:2608.18086v1 Announce Type: new Abstract: The growth of open-weight foundation models (OWFMs) has prompted the AI community to re-evaluate strategies for effective downstream governance. Althoug...

### 49. Solving Is Not Drawing: A Benchmark for Diagrammatic Reasoning in Olympiad Geometry
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18111
- **AI 摘要**: 本文提出一个用于奥林匹克几何图形推理的基准，强调解题与绘图是不同技能，模型需具备构建准确图形和辅助构造的能力。
- **原始摘要**: arXiv:2608.18111v1 Announce Type: new Abstract: Foundation models such as GPT and Claude now solve olympiad-level mathematics with remarkable proficiency, so much so that geometry problem solving has...

### 50. Candidate-Fate Accounting for Transparent Sensor Diagnostic Pipeline Search
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18665
- **AI 摘要**: 工业传感器诊断依赖预处理、表示和分类流水线，自动流水线搜索可降低人工设计成本。现有AutoML/AutoDL报告仅保留拟合试验、分数和获胜者，忽略无效、剪枝、跳过、缓存或未拟合的候选，限制了审查者检查信号一致性的能力。
- **原始摘要**: arXiv:2608.18665v1 Announce Type: new Abstract: Industrial sensor diagnostics relies on preprocessing, representation, and classification pipelines, making automated pipeline search useful for reducin...

### 51. \textsc{TestifAI}: Tomography-Based Testing for Deep Learning Systems
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18900
- **AI 摘要**: 本文提出TestifAI，一种基于断层扫描的深度学习系统测试方法。针对现有鲁棒性测试计算开销大的问题，该方法通过高效生成测试用例，验证模型在输入扰动下的输出稳定性，旨在提升AI系统在安全关键领域（如自动驾驶）中的可靠性。
- **原始摘要**: arXiv:2608.18900v1 Announce Type: new Abstract: As AI systems are increasingly deployed in safety-critical application domains (e.g., autonomous driving), associated risks increase too. Deep learning...

### 52. Harness Continual Learning: Continual Adaptation Beyond Model Parameters
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.19013
- **AI 摘要**: 本文提出持续学习不仅限于模型参数，还可通过提示、记忆、工具、技能和路由规则等“harness”进行适应。文章探讨了在模型冻结时，如何通过更新harness来持续改进智能体行为，同时避免破坏已有可靠性。
- **原始摘要**: arXiv:2608.19013v1 Announce Type: cross Abstract: Continual learning has largely been model-centric, treating model parameters as the state that changes with sequential experience. Modern agents can a...

### 53. MAVEN: A Macro-Societal Value Evaluation Framework of Multimodal Content with Compact Aligned Evaluators
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18096
- **AI 摘要**: MAVEN是一个基于国际人权文书的多模态内容宏观社会价值评估框架，采用层级结构，通过紧凑对齐的评估器来评估内容是否符合和平、正义、自由等价值观，弥补了现有框架在安全导向分类和文本心理测量上的不足。
- **原始摘要**: arXiv:2608.18096v1 Announce Type: cross Abstract: Assessing whether multimodal content aligns with macro-societal values, such as peace, justice, and freedom, has become an increasingly urgent challen...

### 54. Automated Computational Energy Minimization of ML Algorithms using Constrained Bayesian Optimization
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2024年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2407.05788
- **AI 摘要**: 本文提出使用约束贝叶斯优化自动最小化机器学习算法的计算能耗，在优化预测性能的同时兼顾能源效率，展示了在超参数优化中平衡性能与能耗的可行性。
- **原始摘要**: arXiv:2407.05788v2 Announce Type: replace Abstract: Bayesian optimization (BO) is an efficient framework for optimization of black-box objectives when function evaluations are costly and gradient info...

### 55. On the Robustness of Vision-Language Models in Zero-shot Privacy Classification
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2510.09253
- **AI 摘要**: 本文系统分析了视觉语言模型（VLMs）在零样本图像隐私分类中的鲁棒性，考察图像退化对模型性能的影响，评估其在不同场景下的可靠性。
- **原始摘要**: arXiv:2510.09253v2 Announce Type: replace-cross Abstract: Automatic systems for document understanding require multimodal models that accurately identify sensitive visual content, even in the presence...

### 56. A Configuration-First Framework for Reproducible, Low-Code Machine Learning: a Localization Use Case
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年10月
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2510.25692
- **AI 摘要**: 本文提出一种配置优先的机器学习框架，旨在提高结果的可复现性，并支持低代码开发。通过将配置、执行、版本化和评估统一管理，减少重复工作，并以定位用例展示其应用。
- **原始摘要**: arXiv:2510.25692v5 Announce Type: replace-cross Abstract: As machine learning underpins more critical applications, the value of a reported result depends on whether it can be compared and repeated. I...

### 57. TokenPowerSandbox: Evidence-Gated CPU-First Screening for Energy-Aware LLM Serving
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18149
- **AI 摘要**: TokenPowerSandbox提出一种证据门控的CPU优先筛选工作流，用于节能LLM服务。它结合可解释的CPU投影器、短目标GPU探针、全工作负载验证及防篡改的测量前冻结溯源，以低成本比较配置并避免超出范围的预测。
- **原始摘要**: arXiv:2608.18149v1 Announce Type: new Abstract: Energy-aware LLM serving requires comparing configurations under realistic request shapes, yet exhaustive target-GPU profiling is costly and a cheap pre...

### 58. FPGA Lifecycle Management for RISC-V Systems
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://arxiv.org/abs/2608.18156
- **AI 摘要**: 本文提出一种主机无关的控制平面架构，将FPGA生命周期管理移至操作系统层，利用标准Linux功能解耦部署与特定ISA及供应商栈，使支持Linux的RISC-V处理器能实现可扩展的比特流部署。
- **原始摘要**: arXiv:2608.18156v1 Announce Type: new Abstract: FPGA lifecycle management remains tied to proprietary toolchains and host architectures, leaving RISC-V without a vendor-neutral model for scalable bits...

### 59. ICYMI: The Kimi Playground: Your faster way to iterate and test
- **来源**: Kimi Blog (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://platform.kimi.ai/blog/posts/ICYMI_The_Kimi_Playground
- **AI 摘要**: 文章介绍Kimi Playground，一个用于加速AI迭代和测试的平台，旨在帮助开发者更高效地实验和优化AI模型。

### 60. System Engineering1
- **来源**: Tenstorrent (TIER1)
- **发布日期**: 2026-08-21
- **类型**: blog
- **优先级**: high
- **分类**: Harness工程
- **链接**: https://tenstorrent.com/newsroom/newsroom/tags/system-engineering
- **AI 摘要**: 文章标题为System Engineering1，但摘要内容为空，无法生成具体摘要。建议补充文章内容后再进行分析。

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
