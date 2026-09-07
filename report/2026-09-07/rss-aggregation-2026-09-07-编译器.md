# RSS 聚合报告 - 编译器

**生成时间**: 2026-09-08 07:11:32
**文章数量**: 8 篇

---

### 1. Rust debugging survey 2026 results
- **来源**: Rust Blog (TIER2)
- **发布日期**: 2026-09-07T00:00:00+00:00 (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://blog.rust-lang.org/2026/09/07/rust-debugging-survey-2026-results/
- **AI 摘要**: Rust官方博客发布了2026年调试调查结果。调查收到2300多份回复，旨在了解开发者使用调试器的情况和问题。结果显示，超过80%的受访者为中级或高级用户，但超过一半的受访者目前不使用Rust调试器。高级用户中近半数使用调试器，而初学者中约半数从未使用过。约3%的前用户因调试支持问题停止使用Rust，另有24%认为调试问题部分相关。在调试方式上，打印调试和dbg!宏最常用，其次是IDE中的lldb和命令行gdb。文章还按操作系统分析了调试工具的使用分布，Linux上命令行gdb使用较多。该调查由编译器团队发起，旨在改善Rust调试体验。
- **原始摘要**: One of the biggest challenges Rust developers report in our annual surveys is a subpar debugging experience. So, back in February, we ran our first Rust Debugging Survey, in the hopes of identifying h...

### 2. Compiler-Guided Adaptive Proof Search with Cross-Model Synergy on Context-Dependent Theorem Proving
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 24 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.18084
- **AI 摘要**: 提出编译器引导的自适应证明搜索框架，结合双模型生成和停滞触发重采样以探索多样起点，利用编译器反馈进行当前最优精化，在真实Lean 4项目上提升了定理证明的效率与效果。
- **原始摘要**: arXiv:2608.18084v2 Announce Type: replace Abstract: Theorem proving in real-world Lean 4 projects is challenging because proofs often depend on project-specific context. While iterative refinement can...

### 3. HLS-Seek: QoR-Aware Code Generation for High-Level Synthesis via Proxy Comparative Reward Reinforcement Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2605.13536
- **AI 摘要**: 本文提出HLS-Seek框架，通过代理比较奖励强化学习实现质量感知的自然语言到HLS代码生成，避免全合成循环，并采用不确定性感知的MC dropout切换防止奖励黑客。
- **原始摘要**: arXiv:2605.13536v2 Announce Type: replace-cross Abstract: High-Level Synthesis (HLS) compiles algorithmic C/C++ descriptions into hardware, with Quality of Results (QoR)---latency and resource utiliza...

### 4. GraphMend: Code Transformations for Fixing Graph Breaks in PyTorch 2
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2025年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2509.16248
- **AI 摘要**: 本文提出GraphMend，一种编译器技术，通过源码级分析和转换自动修复PyTorch 2中的FX图断裂，消除CPU-GPU同步，提升优化机会，无需手动重构。
- **原始摘要**: arXiv:2509.16248v5 Announce Type: replace-cross Abstract: This paper presents GraphMend, a compiler technique that automatically fixes FX graph breaks in PyTorch 2 programs. Although PyTorch 2 introdu...

### 5. CuLifter: Lifting GPU Binaries to Typed IR
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年04月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2604.27486
- **AI 摘要**: 本文提出CuLifter，一种将GPU二进制（SASS）提升为LLVM IR的框架。通过约束传播和冲突检测恢复寄存器类型，重构显式控制流，并聚合多指令模式。在11977个内核上实现90%以上执行正确性，验证了类型恢复的关键作用。
- **原始摘要**: arXiv:2604.27486v2 Announce Type: replace Abstract: GPU compilers merge all data types into a single unified register file, erasing the type information that binary-analysis tools rely on. We show tha...

### 6. JLIR: A Julia-Native MLIR-Inspired Intermediate Representation with Automatic JACC Kernel Extraction
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2609.04585
- **AI 摘要**: JLIR是一个Julia原生的、受MLIR启发的中间表示框架，自动提取JACC内核。它解决了MLIR对动态语言类型系统和抽象级别的不足，使科学计算用户能自然地引入新抽象并优化算法实现。
- **原始摘要**: arXiv:2609.04585v1 Announce Type: new Abstract: The Multi-Level Intermediate Representation (MLIR) has made reusable compiler infrastructure practical for domain-specific computation. However, MLIR's...

### 7. CPL: A Compact C-like Systems Language with Explicit Low-Level Control
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年09月 (约 -7 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2609.04904
- **AI 摘要**: CPL是一种紧凑的类C系统语言，保留C的直接内存访问和机器接口，同时采用更小的语法和现代语言特性。文章描述其设计、编译器流水线、后端、静态分析架构，并通过微基准测试评估原型后端。
- **原始摘要**: arXiv:2609.04904v1 Announce Type: new Abstract: This paper presents Cordell Programming Language (CPL), a compact C-like systems language that retains C's direct access to memory, layout, and machine...

### 8. A Compilation Framework for Quantum Simulation of Non-unitary Dynamics
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年05月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2605.23358
- **AI 摘要**: 本文提出通道优先的量子编译框架，将量子通道作为一等编译对象，核心IR ChannelIR以Kraus形式显式表示通道。通过LindFront前端和结构感知后端，优化后门数减少高达99%。
- **原始摘要**: arXiv:2605.23358v2 Announce Type: replace-cross Abstract: Most quantum compilers assume programs are reversible unitary circuits. This fits closed-system algorithms, but not open-system simulation, wh...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
