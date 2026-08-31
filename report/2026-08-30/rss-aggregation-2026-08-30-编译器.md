# RSS 聚合报告 - 编译器

**生成时间**: 2026-08-31 09:39:19
**文章数量**: 11 篇

---

### 1. Donkey Kong 64 finally gets a fully native PC port written in C — DK64 ReKONGpiled brings ultrawide support, uncapped framerates, and zero AI code
- **来源**: Tom's Hardware (TIER3)
- **发布日期**: Sun, 30 Aug 2026 14:26:14 +0000 (今天)
- **类型**: news
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://www.tomshardware.com/video-games/retro-gaming/donkey-kong-64-finally-gets-a-fully-native-pc-port-written-in-c-dk64-rekongpiled-brings-ultrawide-support-uncapped-framerates-and-zero-ai-code
- **AI 摘要**: 《大金刚64》终于获得用C语言编写的完全原生PC移植版——DK64 ReKONGpiled，支持超宽屏、无上限帧率，且不含任何AI代码。文章主要介绍该移植版的技术特点和功能。
- **原始摘要**: A team of veteran developers has recompiled Donkey Kong 64 in C, so it runs natively on Windows, Linux, and Mac. The entire project is free, uses no generative AI, but still includes more features tha...

### 2. How we made JSON.stringify more than twice as fast
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-08-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/json-stringify
- **AI 摘要**: V8引擎团队通过引入无副作用快速路径，使JSON.stringify性能提升超过两倍。该优化基于序列化对象不会触发副作用（如用户代码执行或垃圾回收）的保证，采用迭代而非递归实现，避免栈溢出检查并支持更深的嵌套对象。同时，针对字符串的一字节和两字节表示，将序列化器模板化为两个专门版本，减少类型检查分支，提升处理混合编码的效率。这些优化显著加快了网页交互和响应速度。
- **原始摘要**: JSON.stringify is a core JavaScript function for serializing data. Its performance directly affects common operations across the web, from serializing data for a network request to saving data to loca...

### 3. Speculative Optimizations for WebAssembly using Deopts and Inlining
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-06-24T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/wasm-speculative-optimizations
- **AI 摘要**: V8在Chrome M137中为WebAssembly实现了推测性优化，包括call_indirect内联和反优化支持。这些优化基于运行时反馈生成更好的机器码，尤其加速WasmGC程序，在Dart微基准测试中平均提速超50%，大型应用提速1%-8%。文章解释了背景：JavaScript依赖推测优化，而WebAssembly因静态类型和AOT编译传统上不需要，但随着WasmGC引入托管语言，需要此类优化以提升性能。反优化也是未来进一步优化的基础。
- **原始摘要**: In this blog post, we explain two optimizations for WebAssembly that we recently implemented in V8 and that shipped with Google Chrome M137, namely speculative call_indirect inlining and deoptimizatio...

### 4. Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-04-29T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/explicit-compile-hints
- **AI 摘要**: V8推出显式编译提示功能，允许Web开发者控制哪些JavaScript文件或函数在初始编译时被急切编译，以加快页面启动速度。通过在文件顶部添加注释//# allFunctionsCalledOnLoad，可触发整个文件的急切编译。实验显示，20个热门网页中17个获得改进，平均前台解析和编译时间减少630毫秒。该功能在Chrome 136中可用，但需谨慎使用，避免过度编译消耗时间和内存。
- **原始摘要**: Getting JavaScript running fast is key for a responsive web app. Even with V8's advanced optimizations, parsing and compiling critical JavaScript during startup can still create performance bottleneck...

### 5. Land ahoy: leaving the Sea of Nodes
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-03-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/leaving-the-sea-of-nodes
- **AI 摘要**: V8的优化编译器Turbofan正在逐步放弃Sea of Nodes（SoN）中间表示，转向更传统的控制流图（CFG）IR，命名为Turboshaft。目前JavaScript后端和WebAssembly已全面使用Turboshaft。文章回顾了Crankshaft的局限性：手写汇编代码多、难以优化asm.js、无法在lowering中引入控制流、不支持try-catch、存在性能悬崖和反优化循环。这些原因促使团队设计新的CFG-based IR，以改善可维护性和性能。
- **原始摘要**: V8’s end-tier optimizing compiler, Turbofan, is famously one of the few large-scale production compilers to use Sea of Nodes (SoN). However, since almost 3 years ago, we’ve started to get rid of Sea o...

### 6. Turbocharging V8 with mutable heap numbers
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-02-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/mutable-heap-number
- **AI 摘要**: V8团队通过引入可变堆数字（mutable heap numbers）优化，使JetStream2基准测试中的async-fs性能提升2.5倍。该基准的瓶颈在于自定义Math.random实现，其种子变量存储在ScriptContext中，每次调用需要分配不可变HeapNumber，导致性能下降。优化允许在ScriptContext中直接存储可变堆数字，避免重复分配，从而显著提升性能。这种模式也出现在真实代码中。
- **原始摘要**: At V8, we're constantly striving to improve JavaScript performance. As part of this effort, we recently revisited the JetStream2 benchmark suite to eliminate performance cliffs. This post details a sp...

### 7. Bril: An Intermediate Language for Teaching Compilers
- **来源**: Adrian Sampson's blog (TIER2)
- **发布日期**: 2024-07-26T00:00:00+00:00
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://www.cs.cornell.edu/~asampson/blog/bril.html
- **AI 摘要**: 本文介绍了Bril，一个专为编译器教学设计的中间语言（IL），由康奈尔大学Adrian Sampson创建。Bril旨在让学生快速上手，支持使用任意编程语言，并易于混合搭配组件。它采用JSON作为语法，简化了语义和语法规则，优先考虑教学便利性而非代码大小、编译速度等传统IL目标。文章展示了阶乘程序示例，并强调Bril与LLVM等工业级编译器IL的区别，定位为教学场景中的轻量级工具。
- **原始摘要**: I created a new intermediate language, called Bril, for teaching my funky open-source, hands-on compilers course. Because it’s for education, Bril prioritizes simplicity and regularity over more typic...

### 8. Introducing the WebAssembly JavaScript Promise Integration API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-07-01T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi
- **AI 摘要**: WebAssembly JavaScript Promise Integration (JSPI) API允许假设同步访问外部功能的WebAssembly应用在异步环境中运行。它通过拦截异步Web API返回的Promise对象，挂起WebAssembly应用，待异步操作完成后再恢复执行，使应用能用直线代码处理异步操作。JSPI对现有应用改动极小，桥接了同步应用与异步Web API之间的鸿沟，特别适合难以移植的遗留应用。
- **原始摘要**: The JavaScript Promise Integration (JSPI) API allows WebAssembly applications that were written assuming synchronous access to external functionality to operate smoothly in an environment where the fu...

### 9. WebAssembly JSPI has a new API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-06-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-newapi
- **AI 摘要**: WebAssembly JSPI API在Chrome M126中推出新版本，主要变化包括：取消显式Suspender对象，改用JavaScript/WebAssembly边界作为挂起计算的分隔点；不再使用WebAssembly.Function构造函数，提供专用函数和构造器，简化工具链；仅当JavaScript函数实际返回Promise时才挂起，避免不必要的挂起。这些改动使API更易用，并带来性能优化。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API has a new API, available in Chrome release M126. We talk about what has changed, how to use it with Emscripten, and what is the roadmap for JSPI...

### 10. WebAssembly JSPI is going to origin trial
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-03-06T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-ot
- **AI 摘要**: WebAssembly JSPI API在Chrome M123中进入origin trial阶段，允许开发者测试该API。JSPI使顺序代码编译的WebAssembly应用能访问异步Web API。使用需注册origin trial并生成相应WebAssembly和JavaScript，Emscripten用户需3.1.47以上版本。已知问题包括：频繁创建包装调用时性能可能下降，以及每个包装调用分配固定大小栈可能导致内存压力。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API is entering an origin trial, with Chrome release M123. What that means is that you can test whether you and your users can benefit from this new...

### 11. Static Roots: Objects with Compile-Time Constant Addresses
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-02-05T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/static-roots
- **AI 摘要**: V8实现静态根（Static Roots）特性，使undefined、true等核心JavaScript对象具有编译期常量地址。通过将只读堆放置在指针压缩笼的起始位置，并利用指针压缩，V8能预测对象地址，例如检查指针低32位是否为0x61即可判断是否为undefined。该特性在Chrome 111中落地，加速了C++代码和内置函数的执行，提升整个VM的性能。
- **原始摘要**: Did you ever wonder where undefined, true, and other core JavaScript objects come from? These objects are the atoms of any user defined object and need to be there first. V8 calls them immovable immut...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
