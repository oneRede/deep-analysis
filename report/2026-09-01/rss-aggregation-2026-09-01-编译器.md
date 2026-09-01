# RSS 聚合报告 - 编译器

**生成时间**: 2026-09-02 07:21:23
**文章数量**: 6 篇

---

### 1. Announcing rustup 1.29.1
- **来源**: Rust Blog (TIER2)
- **发布日期**: 2026-09-01T00:00:00+00:00 (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://blog.rust-lang.org/2026/09/01/Rustup-1.29.1/
- **AI 摘要**: 本文是Rust官方博客发布的rustup 1.29.1版本更新公告。该版本主要改进包括：提升并发性能（并行检查更新、并发安装组件）、弃用隐式安装活动工具链并给出警告、新增rustup doc --serve本地HTTP服务支持、64位Windows安装i686工具链需强制参数、修复安装取消残留文件和Windows安装失败等问题，并将术语"target triple"更名为"target tuple"。此外，新增aarch64-pc-windows-gnullvm主机平台支持。文章还提供了更新方法、注意事项及对贡献者的感谢。
- **原始摘要**: The rustup team is happy to announce the release of rustup version 1.29.1. Rustup is the recommended tool to install Rust, a programming language that empowers everyone to build reliable and efficient...

### 2. Spectral Analysis for Sparse Matrix Computation: Insights and Potential
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 18 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.29362
- **AI 摘要**: 本文首次探索稀疏矩阵计算与频谱分析之间的联系，将稀疏矩阵视为二维信号进行FFT分析，发现频谱特征能捕捉全局结构特性，并用于机器学习驱动的SpMV格式选择，提升了性能。
- **原始摘要**: arXiv:2608.29362v1 Announce Type: cross Abstract: Sparse computations are fundamental to scientific computing, graph analytics, and machine learning, yet their performance is highly sensitive to the d...

### 3. Separating Parsing Expression Grammars using Cell-Probe Lower Bounds
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 18 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.29592
- **AI 摘要**: 本文解决了解析表达式文法（PEG）的三个开放问题，构造了一个线性上下文无关语言，证明其反转不属于PEG，从而证实了相关猜想，并否定了PEG对连接、Kleene星号等运算的封闭性。主要技术是将脚手架自动机转化为单元探针模型中的动态数据结构。
- **原始摘要**: arXiv:2608.29592v1 Announce Type: new Abstract: We resolve three open problems concerning parsing expression grammars (PEGs). We construct a single language $C$ satisfying $C\in\mathsf{LIN}\cap\mathsf...

### 4. Rust's Type Checker Implementation Is Unsound: An Empirical Study on Soundness Bugs in rustc
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 18 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.28713
- **AI 摘要**: 本文对Rust官方编译器rustc中的30个健全性缺陷问题进行了实证研究，分析了受影响特性、症状、后果、触发特性、社区共识及生命周期，并考察了相关工具和文档，揭示了Rust类型检查器实现的不健全性。
- **原始摘要**: arXiv:2608.28713v1 Announce Type: cross Abstract: Rust is claimed to be a type-sound language capable of preventing various undesirable behaviors, including memory bugs. However, rustc, the official R...

### 5. Outrunning Big KATs: Efficient Decision Procedures for Variants of GKAT
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2601.09986
- **AI 摘要**: 本文提出几种高效的GKAT自动机迹等价判定过程，利用SAT求解器进行符号化技术。在Rust中实现，并在随机基准和真实控制流变换上评估，性能提升一个数量级，并发现Ghidra反编译器中的错误。
- **原始摘要**: arXiv:2601.09986v3 Announce Type: replace Abstract: This paper presents several efficient decision procedures for trace equivalence of GKAT automata, which make use of on-the-fly symbolic techniques v...

### 6. From C to Idiomatic Rust: A Ship-of-Theseus Agentic Translation
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2607.28835
- **AI 摘要**: 本文提出一种从C到惯用Rust的迁移方法，首先生成语义保持的非惯用Rust，然后逐步重构为惯用代码。该方法处理隐式布局假设、别名模式和未定义行为，以生成安全的Rust代码。
- **原始摘要**: arXiv:2607.28835v2 Announce Type: replace-cross Abstract: C underpins operating systems, embedded platforms, and network infrastructure as its abstractions map directly to machine behaviour. Its expli...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
