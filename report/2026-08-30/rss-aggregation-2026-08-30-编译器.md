# RSS 聚合报告 - 编译器

**生成时间**: 2026-08-31 10:19:47
**文章数量**: 11 篇

---

### 1. Donkey Kong 64 finally gets a fully native PC port written in C — DK64 ReKONGpiled brings ultrawide support, uncapped framerates, and zero AI code
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Sun, 30 Aug 2026 14:26:14 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://www.tomshardware.com/video-games/retro-gaming/donkey-kong-64-finally-gets-a-fully-native-pc-port-written-in-c-dk64-rekongpiled-brings-ultrawide-support-uncapped-framerates-and-zero-ai-code
- **AI 摘要**: 《Donkey Kong 64》终于获得完全原生的PC移植版，由C语言编写，名为DK64 ReKONGpiled，支持超宽屏、无上限帧率，且不包含任何AI代码。文章介绍了该移植版的特点，并附带Tom's Hardware网站的会员服务及硬件评测相关内容。
- **原始摘要**: A team of veteran developers has recompiled Donkey Kong 64 in C, so it runs natively on Windows, Linux, and Mac. The entire project is free, uses no generative AI, but still includes more features tha...

### 2. How we made JSON.stringify more than twice as fast
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-08-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/json-stringify
- **AI 摘要**: V8引擎团队通过引入无副作用快速路径和针对字符串表示类型（单字节/双字节）的模板化优化，使JSON.stringify性能提升超过两倍。快速路径基于序列化过程无副作用（如用户代码执行或垃圾回收触发）的保证，采用迭代而非递归方式，避免栈溢出检查并支持更深层嵌套对象。该优化显著提升了Web应用中数据序列化相关操作的响应速度。
- **原始摘要**: JSON.stringify is a core JavaScript function for serializing data. Its performance directly affects common operations across the web, from serializing data for a network request to saving data to loca...

### 3. Speculative Optimizations for WebAssembly using Deopts and Inlining
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-06-24T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/wasm-speculative-optimizations
- **AI 摘要**: V8团队为WebAssembly实现了推测性优化，包括call_indirect内联和反优化（deopt）支持，已随Chrome M137发布。这些优化基于运行时反馈生成更好的机器码，尤其加速WasmGC程序，在Dart微基准上平均提速超50%，大型应用提速1%-8%。反优化也是未来进一步优化的基础。
- **原始摘要**: In this blog post, we explain two optimizations for WebAssembly that we recently implemented in V8 and that shipped with Google Chrome M137, namely speculative call_indirect inlining and deoptimizatio...

### 4. Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-04-29T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/explicit-compile-hints
- **AI 摘要**: V8推出显式编译提示（Explicit Compile Hints）功能，允许Web开发者控制哪些JavaScript文件或函数在启动时被急切编译，以提升页面加载性能。通过在文件顶部添加魔法注释//# allFunctionsCalledOnLoad可触发整个文件的急切编译。实验显示20个热门网页中17个获得改进，平均前台解析和编译时间减少630毫秒。
- **原始摘要**: Getting JavaScript running fast is key for a responsive web app. Even with V8's advanced optimizations, parsing and compiling critical JavaScript during startup can still create performance bottleneck...

### 5. Land ahoy: leaving the Sea of Nodes
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-03-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/leaving-the-sea-of-nodes
- **AI 摘要**: V8的Turbofan优化编译器正逐步放弃Sea of Nodes（SoN）中间表示，转向更传统的基于控制流图（CFG）的Turboshaft IR。文章回顾了Crankshaft的局限性（手写汇编多、无法引入控制流、不支持try-catch、性能悬崖等），解释了转向CFG的原因。目前JavaScript后端和WebAssembly已全面使用Turboshaft，剩余部分正逐步替换。
- **原始摘要**: V8’s end-tier optimizing compiler, Turbofan, is famously one of the few large-scale production compilers to use Sea of Nodes (SoN). However, since almost 3 years ago, we’ve started to get rid of Sea o...

### 6. Turbocharging V8 with mutable heap numbers
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-02-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/mutable-heap-number
- **AI 摘要**: V8团队针对JetStream2基准中的async-fs测试，通过引入可变堆数字（mutable heap numbers）优化，实现了2.5倍的性能提升。该基准中的Math.random实现将seed存储在ScriptContext中，每次更新需要分配不可变HeapNumber，造成性能瓶颈。通过允许原地更新堆数字，避免了频繁分配，显著提升了整体得分。
- **原始摘要**: At V8, we're constantly striving to improve JavaScript performance. As part of this effort, we recently revisited the JetStream2 benchmark suite to eliminate performance cliffs. This post details a sp...

### 7. Bril: An Intermediate Language for Teaching Compilers
- **来源**: Adrian Sampson's blog (TIER2)
- **发布日期**: 2024-07-26T00:00:00+00:00
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://www.cs.cornell.edu/~asampson/blog/bril.html
- **AI 摘要**: 本文介绍了康奈尔大学Adrian Sampson为编译器课程设计的教学用中间语言Bril。Bril是一种基于指令、类似汇编、带类型的ANF语言，其设计目标并非追求代码体积、编译速度或生成代码性能，而是优先考虑快速上手、易于混用组件和语义简单。Bril程序以JSON格式表示，允许学生使用任何编程语言处理，无需学习工业级编译器的复杂API。作者将Bril比作LLVM这个庞大循环系统中的单个血细胞，强调其简洁性和教学适用性，旨在帮助学生通过实践理解编译器算法，同时避免工业级工具的繁琐。
- **原始摘要**: I created a new intermediate language, called Bril, for teaching my funky open-source, hands-on compilers course. Because it’s for education, Bril prioritizes simplicity and regularity over more typic...

### 8. Introducing the WebAssembly JavaScript Promise Integration API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-07-01T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi
- **AI 摘要**: WebAssembly JavaScript Promise Integration (JSPI) API允许以同步方式编写的WebAssembly应用在异步环境中运行。它通过拦截异步Web API返回的Promise对象，挂起WebAssembly应用，待异步操作完成后再恢复执行。该API使C/C++等同步代码无需大量修改即可使用异步Web API，弥合了同步应用与异步生态之间的鸿沟。
- **原始摘要**: The JavaScript Promise Integration (JSPI) API allows WebAssembly applications that were written assuming synchronous access to external functionality to operate smoothly in an environment where the fu...

### 9. WebAssembly JSPI has a new API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-06-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-newapi
- **AI 摘要**: WebAssembly JSPI API在Chrome M126中发布了新版本，主要变更包括：取消显式Suspender对象，改用JavaScript/WebAssembly边界作为挂起计算的分隔点；不再使用WebAssembly.Function构造函数，提供专用函数和构造器；仅当JavaScript函数实际返回Promise时才挂起。这些变化简化了API使用，并带来性能优化。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API has a new API, available in Chrome release M126. We talk about what has changed, how to use it with Emscripten, and what is the roadmap for JSPI...

### 10. WebAssembly JSPI is going to origin trial
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-03-06T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-ot
- **AI 摘要**: WebAssembly JSPI API在Chrome M123中进入origin trial阶段，允许开发者注册试用。JSPI允许顺序代码访问异步Web API。文章介绍了注册要求（使用Emscripten 3.1.47+）、潜在注意事项（如频繁创建包装调用可能影响性能、固定大小栈可能造成内存压力），并指出API仍在标准化过程中，现有API将保留至origin trial结束。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API is entering an origin trial, with Chrome release M123. What that means is that you can test whether you and your users can benefit from this new...

### 11. Static Roots: Objects with Compile-Time Constant Addresses
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-02-05T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/static-roots
- **AI 摘要**: V8实现了静态根（Static Roots）特性，使undefined、true等核心JavaScript对象拥有编译期常量地址。通过将只读堆放置在指针压缩笼的起始位置，并利用指针压缩技术，V8可以在编译时预测对象地址，例如通过检查低32位是否为0x61来判断是否为undefined。该特性在Chrome 111中落地，提升了整个VM的性能，特别是C++代码和内置函数。
- **原始摘要**: Did you ever wonder where undefined, true, and other core JavaScript objects come from? These objects are the atoms of any user defined object and need to be there first. V8 calls them immovable immut...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
