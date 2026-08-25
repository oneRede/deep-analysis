# RSS 聚合报告 - 编译器

**生成时间**: 2026-08-25 14:20:38
**文章数量**: 5 篇

---

### 1. Nova: An End-to-End MLIR Compiler for Deep Learning
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.00029
- **AI 摘要**: 本文介绍Nova，一个端到端MLIR编译器，用于深度学习。它通过从计算结构直接合成细粒度内核，实现对硬件映射的绝对控制，并扩展支持完整Transformer架构，实现全图优化。
- **原始摘要**: arXiv:2608.00029v2 Announce Type: replace Abstract: The performance of deep learning models at scale relies heavily on how effectively high-level mathematical operations are mapped to underlying physi...

### 2. SYNTLOG: FSM Benchmarks Evaluation for FPGA
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.23288
- **AI 摘要**: SYNTLOG是一个FPGA综合工具，在101个FSM基准上对比Xilinx Vivado，面积模式下LUT减少45%-66%，延迟更浅，运行速度快1-2个数量级，并包含功能验证。
- **原始摘要**: arXiv:2608.23288v1 Announce Type: new Abstract: We introduce a curated benchmark collection of \num{101} FSM descriptions organized into five size classes (\emph{small}, \emph{medium}, \emph{large}, \...

### 3. Tensor Seeks Layout: Formalizing Layout Selection for ML Compilers
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.21555
- **AI 摘要**: 本文首次对机器学习编译器中的张量内存布局选择进行形式化研究，将其建模为数据流图上的组合优化问题，证明最优布局选择是计算上困难的，并为特定数据流图设计了最优多项式时间算法。
- **原始摘要**: arXiv:2608.21555v1 Announce Type: new Abstract: Modern machine learning compilers select tensor memory layouts to minimize execution cost under hardware constraints. Layout selection is global: an ope...

### 4. Yarrow: Reconciling Effect Handlers and Region-Based Memory Management
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2607.15876
- **AI 摘要**: 本文介绍Yarrow语言，融合代数效应和基于区域的内存管理，提出Yarrow逻辑支持对单次和多次效应处理器下区域的安全模块化推理，并通过检查点、异步计算等案例验证其正确性。
- **原始摘要**: arXiv:2607.15876v2 Announce Type: replace Abstract: We present a new ML-like programming language Yarrow with algebraic effects and region-based memory management. Reconciling these programming langua...

### 5. All for one and none forall: Compiling polymorphic relations without monomorphization
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年07月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2607.24678
- **AI 摘要**: 本文提出一种新的多态关系编译方法，避免单态化。基于semiringKanren语言，通过等式模式和大到足以覆盖多态关系的实例，将多态程序编译为非多态程序，并证明其正确性。
- **原始摘要**: arXiv:2607.24678v2 Announce Type: replace Abstract: We present a new approach for implementing polymorphism for bottom-up relational languages that avoids monomorphization. We begin by introducing sem...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
