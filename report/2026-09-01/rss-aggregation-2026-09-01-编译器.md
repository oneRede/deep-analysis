# RSS 聚合报告 - 编译器

**生成时间**: 2026-09-02 10:22:59
**文章数量**: 5 篇

---

### 1. Announcing rustup 1.29.1
- **来源**: Rust Blog (TIER2)
- **发布日期**: 2026-09-01T00:00:00+00:00 (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://blog.rust-lang.org/2026/09/01/Rustup-1.29.1/
- **AI 摘要**: rustup 1.29.1版本发布，主要改进包括：并发更新检查和多组件并发安装，提升操作效率；弃用隐式安装活动工具链并产生警告；新增rustup doc --serve标志支持本地HTTP服务文档；64位Windows安装i686主机工具链需强制非主机标志；修复取消安装残留文件和Windows安装失败问题；将“target triple”更名为“target tuple”以反映新术语；新增aarch64-pc-windows-gnullvm主机平台支持。用户可通过rustup self update或rustup update更新。
- **原始摘要**: The rustup team is happy to announce the release of rustup version 1.29.1. Rustup is the recommended tool to install Rust, a programming language that empowers everyone to build reliable and efficient...

### 2. Separating Parsing Expression Grammars using Cell-Probe Lower Bounds
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 18 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.29592
- **AI 摘要**: 本文解决了解析表达式文法（PEG）的三个开放问题，构造了一个线性上下文无关语言C，证明PEG语言在反转和拼接下不封闭，并利用细胞探针下界技术将脚手架自动机转化为动态数据结构。
- **原始摘要**: arXiv:2608.29592v1 Announce Type: new Abstract: We resolve three open problems concerning parsing expression grammars (PEGs). We construct a single language $C$ satisfying $C\in\mathsf{LIN}\cap\mathsf...

### 3. Rust's Type Checker Implementation Is Unsound: An Empirical Study on Soundness Bugs in rustc
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 18 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.28713
- **AI 摘要**: 本文对Rust官方编译器rustc中的30个健全性缺陷进行了实证研究，分析了这些缺陷的特征、症状、后果、触发因素及生命周期，并探讨了现有工具如AddressSanitizer、Miri等的作用。
- **原始摘要**: arXiv:2608.28713v1 Announce Type: cross Abstract: Rust is claimed to be a type-sound language capable of preventing various undesirable behaviors, including memory bugs. However, rustc, the official R...

### 4. Outrunning Big KATs: Efficient Decision Procedures for Variants of GKAT
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年01月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2601.09986
- **AI 摘要**: 本文提出了几种高效的GKAT自动机迹等价决策程序，利用SAT求解器进行符号技术，并在Rust中实现，性能提升一个数量级，还发现了Ghidra反编译器中的bug。
- **原始摘要**: arXiv:2601.09986v3 Announce Type: replace Abstract: This paper presents several efficient decision procedures for trace equivalence of GKAT automata, which make use of on-the-fly symbolic techniques v...

### 5. From C to Idiomatic Rust: A Ship-of-Theseus Agentic Translation
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2607.28835
- **AI 摘要**: 本文提出一种从C到惯用Rust的迁移方法，首先生成语义保持的非惯用Rust代码，再逐步重构为惯用Rust，以解决C代码中的内存安全问题。
- **原始摘要**: arXiv:2607.28835v2 Announce Type: replace-cross Abstract: C underpins operating systems, embedded platforms, and network infrastructure as its abstractions map directly to machine behaviour. Its expli...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
