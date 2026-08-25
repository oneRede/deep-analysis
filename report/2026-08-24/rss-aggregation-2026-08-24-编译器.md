# RSS 聚合报告 - 编译器

**生成时间**: 2026-08-25 10:30:41
**文章数量**: 11 篇

---

### 1. AsmEvo: Agentic Assembly-Level Optimization of AMD GPU Kernels with Functional Equivalence Verification
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.20711
- **AI 摘要**: 提出AsmEvo，一种针对AMD GPU内核的智能体汇编级优化器。它重建可重汇编表示，通过长时程智能体提出低级编辑，重建保持ABI的优化对象，并在与原始代码对象进行差分验证后接受候选。结合代码对象恢复、元数据感知重建、性能分析引导的热窗口编辑和正确性门控。
- **原始摘要**: arXiv:2608.20711v1 Announce Type: new Abstract: High-performance ML systems increasingly rely on GPU kernels whose editable source is unavailable, generated, or too distant from final machine code to...

### 2. HIERA: Workload-Aware Planning Across Implementation Spaces for GPU Kernel Optimization
- **来源**: arXiv cs.AI (人工智能) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.21157
- **AI 摘要**: 本文提出HIERA，一种分层搜索空间规划框架，用于GPU内核优化。它构建契约增强任务规范，在PyTorch算子、CUDA库和自定义内核间选择实现空间，并利用性能反馈和专家知识指导迭代优化，在KernelBench上取得更好效果。
- **原始摘要**: arXiv:2608.21157v1 Announce Type: cross Abstract: High-performance GPU kernels underpin modern deep learning and scientific computing. As workloads become increasingly diverse and GPU hardware evolves...

### 3. CubicSplat: Differentiable Vector Graphics via Error-Bounded Forward Relaxation
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.20803
- **AI 摘要**: CubicSplat是一种可微矢量光栅化器，用均匀折线替代贝塞尔最近点求解器，将几何误差限制在O(S^-2)，通过静态计算图获得良好条件的梯度，并利用合成可见性机制剪枝退化图元，解决了可微优化中前向精确性与梯度信号之间的权衡问题。
- **原始摘要**: arXiv:2608.20803v1 Announce Type: cross Abstract: Vector graphics are prized for their resolution independence, compact storage, and direct editability, making differentiable optimization of their par...

### 4. Primal Acceleration of Newton's Method
- **来源**: arXiv cs.LG (机器学习) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.21359
- **AI 摘要**: 本文提出一种新的直接加速牛顿法，仅使用原始变量，每次迭代只需一次线性求解，以O(1/k^3)的全局收敛率最小化具有Lipschitz连续Hessian的凸函数。该方法无需辅助非线性子问题，可无Hessian实现，并扩展到Bregman几何和复合优化问题。
- **原始摘要**: arXiv:2608.21359v1 Announce Type: cross Abstract: We develop a new direct accelerated Newton method for minimizing convex functions with Lipschitz continuous Hessian. The algorithm uses only primal va...

### 5. Bern2Edge: A Neurosymbolic Compiler for Edge Deployment via Bernstein Polynomial Networks
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.20497
- **AI 摘要**: Bern2Edge是一个神经符号编译器，通过Bernstein多项式网络将预训练教师网络转换为硬件高效的LUT或符号规则表示，实现边缘设备上的高保真、可解释推理，并提升压缩下的准确率。
- **原始摘要**: arXiv:2608.20497v1 Announce Type: cross Abstract: Deploying high-accuracy neural networks on resource-constrained edge devices remains challenging, as existing approaches treat training, compression,...

### 6. AgRefactor: Self-Evolving Agentic Workflow for HLS Compatibility and Performance
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2606.30949
- **AI 摘要**: AgRefactor是一个基于LLM的多智能体工作流，用于将软件重构为HLS兼容代码，具备自进化记忆系统和自动化重构工具，平衡LLM重写与工具转换，提升效率和可扩展性。
- **原始摘要**: arXiv:2606.30949v2 Announce Type: replace-cross Abstract: High-Level Synthesis (HLS) provides a fast path from concepts to silicon, but converting real-world software into synthesizable HLS code remai...

### 7. Portability of Fortran's 'do concurrent' on GPUs II
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.20586
- **AI 摘要**: 本文探讨了Fortran的'do concurrent'语言特性在NVIDIA、AMD和Intel三大GPU厂商上的可移植性，使用生产级应用测试其GPU加速能力，并评估了纯标准语言与OpenMP指令增强的适用场景，发现三大厂商现已支持纯Fortran GPU加速。
- **原始摘要**: arXiv:2608.20586v1 Announce Type: new Abstract: There continues to be growing interest in using standard language constructs for parallel and accelerated HPC computing, avoiding the need for (sometime...

### 8. Symbolic Basic Block Profiling for Machine Learning Kernels
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.20605
- **AI 摘要**: 本文提出符号化基本块剖析技术，为机器学习内核生成基本块执行次数的符号公式，避免动态插桩的开销。在LLVM中实现，并在TVM生成的78个ML算子中验证，73个结果与动态插桩一致，中位加速15093倍。
- **原始摘要**: arXiv:2608.20605v1 Announce Type: new Abstract: Current basic block profiling techniques obtain the count of executions of each basic block in a program using dynamic instrumentation. These profiling...

### 9. Granthi: Higher-Order Quantum Programming via Unitary Wiring
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.20443
- **AI 摘要**: 本文介绍Granthi，一种纯幺正高阶量子编程语言，支持量子程序作为一等公民、标签保留路由和有限标签类型。编译器将程序布线为量子电路，已在OCaml DSL中端到端实现。
- **原始摘要**: arXiv:2608.20443v1 Announce Type: cross Abstract: Existing quantum programming languages confine higher order structure to a classical host while restricting the quantum layer to first order operation...

### 10. When Do Staging Annotations Preserve Semantics? Mechanizing Typed Semantics-Preserving Multi-stage Programming with Let-Insertion (Extended Version)
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年06月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2606.30854
- **AI 摘要**: 本文研究多阶段编程的语义保持问题，探讨带引号的多阶段语言中代码片段操作可能改变求值顺序，导致阶段化程序与非阶段化参考实现语义不一致。通过机械化方式设计具有语义保持保证的多阶段语言。
- **原始摘要**: arXiv:2606.30854v2 Announce Type: replace Abstract: Multi-stage programming with quotations has long provided a powerful way to generate and manipulate code. By treating code as data, programmers can...

### 11. Compiling WebAssembly Concolic Execution with Staging, Continuations, and Snapshots (Extended Version)
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 10 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.18327
- **AI 摘要**: 本文提出一种编译WebAssembly混合执行的新方法，结合解释器和插桩策略的优点，通过定义性混合解释器并阶段化编译消除解释开销，同时保留解释实现的简洁性，利用延续和快照技术实现高效路径探索。
- **原始摘要**: arXiv:2608.18327v2 Announce Type: replace Abstract: Concolic execution is a variant of symbolic execution that runs a program simultaneously with concrete and symbolic inputs. It records the symbolic...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
