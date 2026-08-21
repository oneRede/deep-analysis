# RSS 聚合报告 - 编译器

**生成时间**: 2026-08-21 15:54:49
**文章数量**: 20 篇

---

### 1. Supply chain attack on arrayref
- **来源**: Rust Blog (TIER2)
- **发布日期**: 2026-08-20T00:00:00+00:00 (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/
- **AI 摘要**: 2026年8月20日，Rust安全响应团队确认proc-macro1等crate存在供应链攻击，其构建脚本会下载恶意载荷。
- **原始摘要**: What happened On 2026-08-20 at 7:15 UTC we got a report that the proc-macro1 crate was malicious. The Rust Security Response Team verified this to be the case: the crate had a build script that was do...

### 2. Announcing Rust 1.98.0
- **来源**: Rust Blog (TIER2)
- **发布日期**: 2026-08-20T00:00:00+00:00 (昨天)
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://blog.rust-lang.org/2026/08/20/Rust-1.98.0/
- **AI 摘要**: Rust团队宣布发布1.98.0版本，该版本是Rust编程语言的一次更新，用户可通过rustup升级。
- **原始摘要**: The Rust team is happy to announce a new version of Rust, 1.98.0. Rust is a programming language empowering everyone to build reliable and efficient software. If you have a previous version of Rust in...

### 3. How we made JSON.stringify more than twice as fast
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-08-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/json-stringify
- **AI 摘要**: V8引擎团队通过工程优化，使JSON.stringify函数性能提升超过两倍，从而加快网页交互和响应速度，提升用户体验。
- **原始摘要**: JSON.stringify is a core JavaScript function for serializing data. Its performance directly affects common operations across the web, from serializing data for a network request to saving data to loca...

### 4. Speculative Optimizations for WebAssembly using Deopts and Inlining
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-06-24T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/wasm-speculative-optimizations
- **AI 摘要**: V8在WebAssembly中实现了推测性call_indirect内联和反优化支持，基于运行时反馈生成更优机器码，显著提升WasmGC程序执行速度。
- **原始摘要**: In this blog post, we explain two optimizations for WebAssembly that we recently implemented in V8 and that shipped with Google Chrome M137, namely speculative call_indirect inlining and deoptimizatio...

### 5. Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-04-29T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/explicit-compile-hints
- **AI 摘要**: V8通过显式编译提示，在启动时优先编译关键JavaScript函数，减少解析和编译瓶颈，加快网页加载速度。
- **原始摘要**: Getting JavaScript running fast is key for a responsive web app. Even with V8's advanced optimizations, parsing and compiling critical JavaScript during startup can still create performance bottleneck...

### 6. Land ahoy: leaving the Sea of Nodes
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-03-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/leaving-the-sea-of-nodes
- **AI 摘要**: V8的Turbofan编译器正从Sea of Nodes转向传统控制流图中间表示，以简化优化流程并提升编译效率。
- **原始摘要**: V8’s end-tier optimizing compiler, Turbofan, is famously one of the few large-scale production compilers to use Sea of Nodes (SoN). However, since almost 3 years ago, we’ve started to get rid of Sea o...

### 7. Turbocharging V8 with mutable heap numbers
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-02-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/mutable-heap-number
- **AI 摘要**: V8通过引入可变堆数字优化，消除了JetStream2基准中的性能悬崖，使async-fs基准提升2.5倍，整体得分显著提高。
- **原始摘要**: At V8, we're constantly striving to improve JavaScript performance. As part of this effort, we recently revisited the JetStream2 benchmark suite to eliminate performance cliffs. This post details a sp...

### 8. Bril: An Intermediate Language for Teaching Compilers
- **来源**: Adrian Sampson's blog (TIER2)
- **发布日期**: 2024-07-26T00:00:00+00:00
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://www.cs.cornell.edu/~asampson/blog/bril.html
- **AI 摘要**: 作者为编译器课程创建了名为Bril的中间语言，它优先考虑简单性和规范性，而非性能和简洁性。文章概述了Bril的设计、特点及其自2019年以来的生态系统发展。
- **原始摘要**: I created a new intermediate language, called Bril, for teaching my funky open-source, hands-on compilers course. Because it’s for education, Bril prioritizes simplicity and regularity over more typic...

### 9. Introducing the WebAssembly JavaScript Promise Integration API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-07-01T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi
- **AI 摘要**: WebAssembly的JavaScript Promise集成API允许同步编写的Wasm应用无缝调用异步Web API，本文介绍其核心能力、访问方式及开发示例。
- **原始摘要**: The JavaScript Promise Integration (JSPI) API allows WebAssembly applications that were written assuming synchronous access to external functionality to operate smoothly in an environment where the fu...

### 10. WebAssembly JSPI has a new API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-06-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-newapi
- **AI 摘要**: WebAssembly JSPI API在Chrome M126中更新，本文介绍新API变化、Emscripten使用方式及未来路线图。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API has a new API, available in Chrome release M126. We talk about what has changed, how to use it with Emscripten, and what is the roadmap for JSPI...

### 11. WebAssembly JSPI is going to origin trial
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-03-06T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-ot
- **AI 摘要**: WebAssembly的JSPI API进入Chrome M123的源试用阶段，允许开发者测试该API，使同步Wasm代码访问异步Web API。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API is entering an origin trial, with Chrome release M123. What that means is that you can test whether you and your users can benefit from this new...

### 12. Static Roots: Objects with Compile-Time Constant Addresses
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-02-05T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/static-roots
- **AI 摘要**: V8通过静态根技术，在编译时确定核心JavaScript对象（如undefined、true）的内存地址，实现快速访问，提升性能。
- **原始摘要**: Did you ever wonder where undefined, true, and other core JavaScript objects come from? These objects are the atoms of any user defined object and need to be there first. V8 calls them immovable immut...

### 13. PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX
- **来源**: arXiv cs.CL (计算与语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.17379
- **AI 摘要**: 本文介绍PTXBench基准，用于评估和适配LLM使用架构特定的PTX指令进行GPU内核优化。该基准在H100和B200上测量功能正确性、运行时执行和加速比，发现架构特定PTX能力发展不均。
- **原始摘要**: arXiv:2608.17379v2 Announce Type: replace Abstract: We introduce PTXBench, a benchmark for evaluating and adapting large language models (LLMs) to use architecture-specific PTX for GPU kernel optimiza...

### 14. A Thread-Register Decoupled GPU Execution Model for Efficient Tensor Computation
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.19628
- **AI 摘要**: 本文提出线程-寄存器解耦的GPU执行模型，以高效编排张量计算流水线，解决现代AI工作负载中固定并行度和粗粒度调度带来的瓶颈，提升Tensor Core利用率。
- **原始摘要**: arXiv:2608.19628v1 Announce Type: new Abstract: Modern GPUs increasingly integrate Tensor Cores into the execution pipeline. Although aggregate tensor throughput continues to grow, aided by an operand...

### 15. Architecture and Compilation Co-Design for High-Rate Quantum Product Codes on Neutral Atom Arrays
- **来源**: arXiv cs.AR (硬件架构) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.20164
- **AI 摘要**: 本文针对中性原子阵列上的高码率量子乘积码，提出架构与编译协同设计方法，解决量子纠错码物理执行计划合成的困难组合问题，提升容错量子计算的可扩展性。
- **原始摘要**: arXiv:2608.20164v1 Announce Type: cross Abstract: Achieving fault-tolerant quantum computing at a practical scale demands quantum error correction (QEC) codes with high encoding rates. Quantum low-den...

### 16. Hippogriff: a semantic approach to uniting core and modules
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.19728
- **AI 摘要**: 介绍Hippogriff语言，其模块系统统一了核心层和模块层的语法，基于依赖类型理论，支持通用递归且保证类型检查终止，并讨论实现与语义。
- **原始摘要**: arXiv:2608.19728v1 Announce Type: new Abstract: In this paper we introduce Hippogriff, a language with a module system that unifies syntax between the core level and the module level. Hippogriff's typ...

### 17. Formal Performance and Compile Time Guarantees for Compiler Optimization Heuristics
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.20137
- **AI 摘要**: 提出验证编译器优化启发式的性能和编译时间属性，以内联展开为例，用成本模型形式化，确保优化不仅语义正确，还满足性能与编译时间保证。
- **原始摘要**: arXiv:2608.20137v1 Announce Type: new Abstract: Modern optimizing compilers rely on heuristic search algorithms for NP-hard optimization problems, which can result in poor generated-code performance a...

### 18. DSLHyPE-a DSL kernel language for the Exascale Hyperbolic PDE Engine ExaHyPE
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.19273
- **AI 摘要**: 介绍DSLHyPE，一种双语领域特定语言，用于ExaHyPE求解器中的计算内核建模，用户用C/C++表达物理，数值方案用Python DSL，编译器将Python描述降至MLIR并集成。
- **原始摘要**: arXiv:2608.19273v1 Announce Type: cross Abstract: We introduce a bilingual domain-specific language (DSL) for modelling compute kernels within a generic solver for hyperbolic partial differential equa...

### 19. Write Once, Run Everywhere: The Axon DSL for Shape-Safe and Framework-Agnostic LLM Architectures
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年08月 (约 6 天前)
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2608.19889
- **AI 摘要**: 提出Axon，一种强类型领域特定语言，用于定义形状安全且框架无关的LLM架构，实现一次编写处处运行，提高模型可移植性和效率，降低维护成本。
- **原始摘要**: arXiv:2608.19889v1 Announce Type: cross Abstract: The entire ecosystem of open-source language models effectively relies on a single platform. What if this platform was forced to shut down tomorrow? I...

### 20. Sound State Encodings in Translational Separation Logic Verifiers (Extended Version)
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年03月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2603.20001
- **AI 摘要**: 扩展版论文，研究分离逻辑翻译验证器中状态编码的正确性，确保前端编码到中间验证语言及后端验证的健全性，形式化验证翻译验证器的可靠性。
- **原始摘要**: arXiv:2603.20001v2 Announce Type: replace Abstract: Automated program verifiers are often organized into a front-end, which encodes an input program into an intermediate verification language (IVL), a...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
