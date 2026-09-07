# RSS 聚合报告 - 编译器

**生成时间**: 2026-09-07 10:07:13
**文章数量**: 10 篇

---

### 1. How we made JSON.stringify more than twice as fast
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-08-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/json-stringify
- **AI 摘要**: V8引擎团队通过引入无副作用快速路径、迭代式序列化器、以及针对单字节和双字节字符串的模板化实现，使JSON.stringify的性能提升超过两倍。该优化基于对序列化过程无副作用的保证，绕过了通用序列化器的昂贵检查，同时支持更深层嵌套对象的序列化，显著提升了Web应用中数据序列化的效率。
- **原始摘要**: JSON.stringify is a core JavaScript function for serializing data. Its performance directly affects common operations across the web, from serializing data for a network request to saving data to loca...

### 2. Speculative Optimizations for WebAssembly using Deopts and Inlining
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-06-24T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/wasm-speculative-optimizations
- **AI 摘要**: V8引擎为WebAssembly实现了推测性call_indirect内联和反优化支持，基于运行时反馈生成更优的机器码。该组合优化在Dart微基准测试中平均提速超过50%，在大型应用和基准测试中提速1%-8%。这些优化尤其有利于WasmGC程序，并为未来进一步优化奠定基础。
- **原始摘要**: In this blog post, we explain two optimizations for WebAssembly that we recently implemented in V8 and that shipped with Google Chrome M137, namely speculative call_indirect inlining and deoptimizatio...

### 3. Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-04-29T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/explicit-compile-hints
- **AI 摘要**: V8引入显式编译提示功能，允许Web开发者通过魔法注释选择需要立即编译的JavaScript文件，以加快页面启动速度。实验显示20个热门网页中有17个获得改进，平均前台解析和编译时间减少630毫秒。该功能在Chrome 136中支持按文件选择，但需谨慎使用以避免过度编译消耗资源。
- **原始摘要**: Getting JavaScript running fast is key for a responsive web app. Even with V8's advanced optimizations, parsing and compiling critical JavaScript during startup can still create performance bottleneck...

### 4. Land ahoy: leaving the Sea of Nodes
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-03-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/leaving-the-sea-of-nodes
- **AI 摘要**: V8的Turbofan编译器正逐步放弃Sea of Nodes中间表示，转向更传统的基于控制流图的Turboshaft IR。文章回顾了Crankshaft的局限性，包括大量手写汇编、难以优化asm.js、无法在lowering中引入控制流、不支持try-catch以及性能悬崖等问题，解释了转向Turboshaft的动机。
- **原始摘要**: V8’s end-tier optimizing compiler, Turbofan, is famously one of the few large-scale production compilers to use Sea of Nodes (SoN). However, since almost 3 years ago, we’ve started to get rid of Sea o...

### 5. Turbocharging V8 with mutable heap numbers
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-02-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/mutable-heap-number
- **AI 摘要**: V8团队通过引入可变堆数字优化，解决了JetStream2基准测试中async-fs的性能瓶颈。该基准测试的自定义Math.random实现因每次调用都分配不可变HeapNumber对象而导致性能下降。通过允许堆数字原地修改，消除了分配开销，使async-fs基准性能提升2.5倍，该模式也存在于真实世界代码中。
- **原始摘要**: At V8, we're constantly striving to improve JavaScript performance. As part of this effort, we recently revisited the JetStream2 benchmark suite to eliminate performance cliffs. This post details a sp...

### 6. Bril: An Intermediate Language for Teaching Compilers
- **来源**: Adrian Sampson's blog (TIER2)
- **发布日期**: 2024-07-26T00:00:00+00:00
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://www.cs.cornell.edu/~asampson/blog/bril.html
- **AI 摘要**: 本文介绍了Bril，一个专为编译器教学设计的中间语言（IL）。作者Adrian Sampson在康奈尔大学开设博士级编译器课程时，为了让学生快速上手并避免工业级编译器的复杂API，创建了Bril。Bril的设计优先考虑教学需求：快速上手、易于混搭组件（包括学生编写的部分）、语义简单、语法规整。它采用基于指令的汇编风格，具有类型系统，并以JSON格式表示程序，方便学生使用任何编程语言（如Python）处理。与LLVM等工业级IL不同，Bril不追求代码大小、编译速度和生成代码性能，而是专注于教育场景。文章通过阶乘程序示例展示了Bril的语法，并强调其作为教学工具的独特价值。
- **原始摘要**: I created a new intermediate language, called Bril, for teaching my funky open-source, hands-on compilers course. Because it’s for education, Bril prioritizes simplicity and regularity over more typic...

### 7. Introducing the WebAssembly JavaScript Promise Integration API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-07-01T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi
- **AI 摘要**: WebAssembly JavaScript Promise Integration (JSPI) API允许假设同步访问外部功能的WebAssembly应用在异步环境中运行。它通过拦截异步Web API返回的Promise对象，挂起WebAssembly应用，待异步操作完成后恢复执行，使应用能用直线代码处理异步操作，且对现有应用改动极小。
- **原始摘要**: The JavaScript Promise Integration (JSPI) API allows WebAssembly applications that were written assuming synchronous access to external functionality to operate smoothly in an environment where the fu...

### 8. WebAssembly JSPI has a new API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-06-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-newapi
- **AI 摘要**: WebAssembly JSPI API在Chrome M126中推出新版本，主要变化包括：取消显式Suspender对象，改用JavaScript/WebAssembly边界作为挂起分隔点；不再使用WebAssembly.Function构造器，提供专用函数；仅当JavaScript函数实际返回Promise时才挂起。这些改变简化了API使用并减少不必要的挂起。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API has a new API, available in Chrome release M126. We talk about what has changed, how to use it with Emscripten, and what is the roadmap for JSPI...

### 9. WebAssembly JSPI is going to origin trial
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-03-06T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-ot
- **AI 摘要**: WebAssembly JSPI API在Chrome M123进入origin trial阶段。该API允许顺序代码访问异步Web API。开发者需注册origin trial token并使用Emscripten 3.1.47以上版本。已知问题包括：频繁创建包装调用时性能可能下降，以及为每个包装调用分配固定大小栈可能导致内存压力。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API is entering an origin trial, with Chrome release M123. What that means is that you can test whether you and your users can benefit from this new...

### 10. Static Roots: Objects with Compile-Time Constant Addresses
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-02-05T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/static-roots
- **AI 摘要**: V8的static roots特性使undefined、true等核心对象具有编译时常量地址。通过将只读堆放置在指针压缩cage的起始位置，V8可以在编译时预测对象地址，例如通过检查指针低32位是否为0x61来判断是否为undefined。该特性在Chrome 111中落地，提升了整个VM的性能，特别是C++代码和内置函数。
- **原始摘要**: Did you ever wonder where undefined, true, and other core JavaScript objects come from? These objects are the atoms of any user defined object and need to be there first. V8 calls them immovable immut...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
