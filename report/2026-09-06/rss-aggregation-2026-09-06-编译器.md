# RSS 聚合报告 - 编译器

**生成时间**: 2026-09-07 07:06:29
**文章数量**: 10 篇

---

### 1. How we made JSON.stringify more than twice as fast
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-08-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/json-stringify
- **AI 摘要**: V8引擎团队通过引入无副作用快速路径，将JSON.stringify的性能提升了两倍以上。该优化基于一个前提：如果序列化对象不会触发任何副作用（如用户自定义代码或垃圾回收），则可以使用更快的专用实现。新的快速路径采用迭代而非递归方式，避免了栈溢出检查，支持更深层嵌套对象。此外，字符串序列化器根据字符类型（单字节或双字节）进行了模板化，生成两个专用版本，避免运行时分支检查，从而提升性能。
- **原始摘要**: JSON.stringify is a core JavaScript function for serializing data. Its performance directly affects common operations across the web, from serializing data for a network request to saving data to loca...

### 2. Speculative Optimizations for WebAssembly using Deopts and Inlining
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-06-24T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/wasm-speculative-optimizations
- **AI 摘要**: V8在WebAssembly中实现了推测性优化，包括call_indirect内联和反优化支持，随Chrome M137发布。这些优化基于运行时反馈生成更好的机器码，特别加速了WasmGC程序。在Dart微基准测试中平均提速超过50%，在大型应用中提速1%-8%。文章解释了背景：JavaScript依赖推测优化，而WebAssembly因静态类型信息通常不需要，但WasmGC引入后需要此类优化以支持Java、Kotlin、Dart等托管语言。
- **原始摘要**: In this blog post, we explain two optimizations for WebAssembly that we recently implemented in V8 and that shipped with Google Chrome M137, namely speculative call_indirect inlining and deoptimizatio...

### 3. Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-04-29T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/explicit-compile-hints
- **AI 摘要**: V8开发了显式编译提示功能，允许Web开发者控制哪些JavaScript文件和函数被急切编译，以加速网页启动。在脚本加载时，V8需决定每个函数是立即编译还是延迟编译。若函数在页面加载期间被调用，急切编译更有利，因为可在后台线程并行处理。实验显示20个热门网页中17个有改进，平均减少前台解析和编译时间630毫秒。Chrome 136支持通过文件顶部的魔法注释选择整个文件进行急切编译，但需谨慎使用以免消耗过多资源。
- **原始摘要**: Getting JavaScript running fast is key for a responsive web app. Even with V8's advanced optimizations, parsing and compiling critical JavaScript during startup can still create performance bottleneck...

### 4. Land ahoy: leaving the Sea of Nodes
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-03-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/leaving-the-sea-of-nodes
- **AI 摘要**: V8的优化编译器Turbofan正逐步放弃Sea of Nodes（SoN）中间表示，转向更传统的控制流图（CFG）IR，命名为Turboshaft。目前JavaScript后端和WebAssembly已全面使用Turboshaft。文章回顾了Turbofan采用SoN的历史原因，以及Crankshaft编译器存在的问题：手写汇编过多、难以优化asm.js、无法在lowering中引入控制流、不支持try-catch、性能悬崖和去优化循环等。这些缺陷促使团队设计新的CFG-based IR。
- **原始摘要**: V8’s end-tier optimizing compiler, Turbofan, is famously one of the few large-scale production compilers to use Sea of Nodes (SoN). However, since almost 3 years ago, we’ve started to get rid of Sea o...

### 5. Turbocharging V8 with mutable heap numbers
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-02-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/mutable-heap-number
- **AI 摘要**: V8团队通过引入可变堆数字优化了JetStream2基准测试中的async-fs性能，获得2.5倍提升。性能瓶颈在于自定义Math.random实现，其种子变量存储在ScriptContext中。默认配置下，ScriptContext槽位存储31位小整数或指向不可变HeapNumber的压缩指针。每次调用Math.random更新种子时，若数值超出SMI范围则需分配新的HeapNumber，造成性能问题。通过允许堆数字可变，避免了频繁分配，显著提升了性能。
- **原始摘要**: At V8, we're constantly striving to improve JavaScript performance. As part of this effort, we recently revisited the JetStream2 benchmark suite to eliminate performance cliffs. This post details a sp...

### 6. Bril: An Intermediate Language for Teaching Compilers
- **来源**: Adrian Sampson's blog (TIER2)
- **发布日期**: 2024-07-26T00:00:00+00:00
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://www.cs.cornell.edu/~asampson/blog/bril.html
- **AI 摘要**: 本文介绍了Bril，一个专为编译器教学设计的中间语言（IL）。作者Adrian Sampson在康奈尔大学开设博士级编译器课程时，为了让学生快速上手并避免工业级编译器的复杂API，创建了Bril。Bril的设计优先考虑教学需求：快速上手、易于混用组件（包括学生编写的组件）、语义简单、语法规则统一。它采用JSON格式作为语法，使学生可以用任何编程语言处理，无需学习特定实现语言。Bril是面向指令的、类似汇编的、带类型的ANF语言，虽然不追求代码大小、编译速度和生成代码性能，但与现代编译器IL相似。作者用比喻说明，若LLVM是完整循环系统，Bril则是一个血细胞。
- **原始摘要**: I created a new intermediate language, called Bril, for teaching my funky open-source, hands-on compilers course. Because it’s for education, Bril prioritizes simplicity and regularity over more typic...

### 7. Introducing the WebAssembly JavaScript Promise Integration API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-07-01T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi
- **AI 摘要**: WebAssembly JavaScript Promise Integration (JSPI) API允许假设同步访问外部功能的WebAssembly应用在异步环境中运行。异步API通过Promise分离操作启动与完成，而C/C++等语言通常使用阻塞式同步API。JSPI通过拦截异步Web API返回的Promise对象，挂起WebAssembly应用，待异步操作完成后恢复执行，使应用能用直线代码处理异步操作。该API对现有应用改动极小，弥合了同步应用与异步Web API之间的鸿沟。
- **原始摘要**: The JavaScript Promise Integration (JSPI) API allows WebAssembly applications that were written assuming synchronous access to external functionality to operate smoothly in an environment where the fu...

### 8. WebAssembly JSPI has a new API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-06-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-newapi
- **AI 摘要**: WebAssembly JSPI API在Chrome M126中推出了新版本。主要变更包括：取消显式Suspender对象，改用JavaScript/WebAssembly边界作为挂起计算的切分点；不再使用WebAssembly.Function构造函数，提供专用函数和构造函数，简化工具链；仅当JavaScript函数实际返回Promise时才挂起，避免不必要的挂起。这些变化使API更易用，部分应用可避免不必要的浏览器事件循环往返。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API has a new API, available in Chrome release M126. We talk about what has changed, how to use it with Emscripten, and what is the roadmap for JSPI...

### 9. WebAssembly JSPI is going to origin trial
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-03-06T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-ot
- **AI 摘要**: WebAssembly的JavaScript Promise Integration (JSPI) API在Chrome M123中进入源试用阶段。JSPI允许编译为WebAssembly的顺序代码访问异步Web API。开发者需注册源试用并生成相应的WebAssembly和JavaScript，使用Emscripten至少3.1.47版本。已知问题包括：频繁创建派生计算的应用性能可能受影响，因为包装调用资源未缓存；每个包装调用分配固定大小栈，大量简单调用可能造成内存压力。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API is entering an origin trial, with Chrome release M123. What that means is that you can test whether you and your users can benefit from this new...

### 10. Static Roots: Objects with Compile-Time Constant Addresses
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-02-05T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/static-roots
- **AI 摘要**: V8实现了静态根特性，使undefined、true等核心JavaScript对象具有编译时常量地址。通过将只读堆放置在指针压缩笼的起始位置，这些对象获得可预测的压缩地址。例如undefined的压缩地址始终为0x61，因此可通过检查指针低32位是否为0x61来判断对象是否为undefined。该特性在Chrome 111中落地，提升了整个VM的性能，特别是加速了C++代码和内置函数。
- **原始摘要**: Did you ever wonder where undefined, true, and other core JavaScript objects come from? These objects are the atoms of any user defined object and need to be there first. V8 calls them immovable immut...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
