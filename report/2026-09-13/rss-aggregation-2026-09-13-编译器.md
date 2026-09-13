# RSS 聚合报告 - 编译器

**生成时间**: 2026-09-14 07:06:53
**文章数量**: 10 篇

---

### 1. How we made JSON.stringify more than twice as fast
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-08-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/json-stringify
- **AI 摘要**: V8团队通过引入无副作用的快速路径、迭代式序列化以及按字符类型模板化等优化，使JSON.stringify性能提升超过两倍。快速路径避免了通用序列化器的昂贵检查和防御逻辑，迭代实现消除了栈溢出检查并支持更深嵌套对象。字符串处理针对单字节和双字节字符分别编译专用版本，减少分支和类型检查。该优化显著加快了网页数据序列化、网络请求和localStorage操作等常见场景的响应速度。
- **原始摘要**: JSON.stringify is a core JavaScript function for serializing data. Its performance directly affects common operations across the web, from serializing data for a network request to saving data to loca...

### 2. Speculative Optimizations for WebAssembly using Deopts and Inlining
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-06-24T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/wasm-speculative-optimizations
- **AI 摘要**: V8在Chrome M137中为WebAssembly引入推测性call_indirect内联和去优化支持，通过运行时反馈生成更优机器码。该优化对WasmGC程序效果显著，Dart微基准测试平均提速超50%，实际应用提升1%至8%。文章回顾了JavaScript依赖推测优化和去优化的背景，指出WebAssembly因静态类型和AOT优化此前无需此类技术，但WasmGC的引入使推测优化变得必要，去优化也为未来优化奠定基础。
- **原始摘要**: In this blog post, we explain two optimizations for WebAssembly that we recently implemented in V8 and that shipped with Google Chrome M137, namely speculative call_indirect inlining and deoptimizatio...

### 3. Giving V8 a Heads-Up: Faster JavaScript Startup with Explicit Compile Hints
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-04-29T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/explicit-compile-hints
- **AI 摘要**: V8推出显式编译提示功能，允许开发者通过魔术注释控制哪些JavaScript文件在启动时被急切编译，从而加快网页加载。V8处理脚本时需决定每个函数是立即编译还是延迟编译，急切编译可在后台线程与网络加载并行，避免主线程阻塞。实验显示20个热门网页中17个有改进，平均前台解析编译时间减少630毫秒。Chrome 136已支持按文件选择急切编译，但需谨慎使用以免消耗过多时间和内存。
- **原始摘要**: Getting JavaScript running fast is key for a responsive web app. Even with V8's advanced optimizations, parsing and compiling critical JavaScript during startup can still create performance bottleneck...

### 4. Land ahoy: leaving the Sea of Nodes
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-03-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/leaving-the-sea-of-nodes
- **AI 摘要**: V8的Turbofan编译器正逐步弃用Sea of Nodes中间表示，转向更传统的控制流图IR Turboshaft。文章回顾了2013年Crankshaft编译器因手写汇编过多、难以优化asm.js、不支持lowering中引入控制流、不支持try-catch及性能悬崖等问题，促使Turbofan采用Sea of Nodes。但Sea of Nodes在实践中也暴露出问题，因此V8决定回归CFG。目前JavaScript后端和WebAssembly全流程已使用Turboshaft，仅builtin管线和JS前端仍部分使用Sea of Nodes。
- **原始摘要**: V8’s end-tier optimizing compiler, Turbofan, is famously one of the few large-scale production compilers to use Sea of Nodes (SoN). However, since almost 3 years ago, we’ve started to get rid of Sea o...

### 5. Turbocharging V8 with mutable heap numbers
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2025-02-25T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/mutable-heap-number
- **AI 摘要**: V8通过引入可变堆数字优化，使JetStream2的async-fs基准测试性能提升2.5倍。该基准使用自定义Math.random实现，其种子变量存储在ScriptContext中。由于种子值超出SMI范围，每次更新都需分配新的不可变HeapNumber对象，造成大量堆分配开销。V8的优化允许在ScriptContext中直接存储可变的双精度浮点值，避免重复分配HeapNumber，从而消除性能瓶颈。该模式在真实代码中也有出现，优化具有实际意义。
- **原始摘要**: At V8, we're constantly striving to improve JavaScript performance. As part of this effort, we recently revisited the JetStream2 benchmark suite to eliminate performance cliffs. This post details a sp...

### 6. Bril: An Intermediate Language for Teaching Compilers
- **来源**: Adrian Sampson's blog (TIER2)
- **发布日期**: 2024-07-26T00:00:00+00:00
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://www.cs.cornell.edu/~asampson/blog/bril.html
- **AI 摘要**: 康奈尔大学Adrian Sampson为编译器课程设计了教学用中间语言Bril。Bril以JSON为语法，采用指令式、类汇编、带类型、ANF形式，语义简单、语法规整，便于学生快速上手并用任意语言实现。其设计优先考虑易用性和组件可组合性，而非代码大小、编译速度或生成代码性能。Bril用于课程实践项目，帮助学生通过实现算法理解编译器，避免学习复杂工业级API。
- **原始摘要**: I created a new intermediate language, called Bril, for teaching my funky open-source, hands-on compilers course. Because it’s for education, Bril prioritizes simplicity and regularity over more typic...

### 7. Introducing the WebAssembly JavaScript Promise Integration API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-07-01T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi
- **AI 摘要**: V8介绍WebAssembly JavaScript Promise Integration（JSPI）API，旨在让假设同步访问外部功能的WebAssembly应用在异步环境中顺畅运行。JSPI通过拦截异步Web API返回的Promise对象，暂停WebAssembly应用，待异步操作完成后恢复执行，使应用可用直线代码处理异步操作。该API对WebAssembly应用本身改动极小，解决了C/C++等同步API应用与浏览器异步生态之间的不匹配问题，尤其有利于难以移植的遗留应用。
- **原始摘要**: The JavaScript Promise Integration (JSPI) API allows WebAssembly applications that were written assuming synchronous access to external functionality to operate smoothly in an environment where the fu...

### 8. WebAssembly JSPI has a new API
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-06-04T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-newapi
- **AI 摘要**: WebAssembly JSPI API在Chrome M126中推出新版本。主要变化包括：取消显式Suspender对象，改以JavaScript/WebAssembly边界作为暂停计算的分界点；不再使用WebAssembly.Function构造函数，改为提供特定函数和构造器，简化工具链并移除对类型反射提案的依赖；仅在JavaScript函数实际返回Promise时才暂停，避免不必要的浏览器事件循环往返。新API更易用，对多数应用影响小，部分应用将显著受益。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API has a new API, available in Chrome release M126. We talk about what has changed, how to use it with Emscripten, and what is the roadmap for JSPI...

### 9. WebAssembly JSPI is going to origin trial
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-03-06T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/jspi-ot
- **AI 摘要**: WebAssembly JSPI API在Chrome M123进入Origin Trial阶段，开发者可测试其效果。JSPI允许编译为WebAssembly的顺序代码访问异步Web API，通过拦截Promise实现应用的暂停与恢复。使用需Emscripten 3.1.47以上版本并注册Origin Trial令牌。已知问题包括：密集创建派生计算时包装序列性能可能下降，因资源不缓存依赖垃圾回收；每次包装调用分配固定大小栈，大量简单调用在途时可能造成内存压力。API仍在标准化过程中。
- **原始摘要**: WebAssembly’s JavaScript Promise Integration (JSPI) API is entering an origin trial, with Chrome release M123. What that means is that you can test whether you and your users can benefit from this new...

### 10. Static Roots: Objects with Compile-Time Constant Addresses
- **来源**: V8 Blog (TIER2)
- **发布日期**: 2024-02-05T00:00:00Z
- **类型**: blog
- **优先级**: medium
- **分类**: 编译器
- **链接**: https://v8.dev/blog/static-roots
- **AI 摘要**: V8引入静态根特性，使undefined、true等不可变不可移动根对象拥有编译期常量地址。这些对象存放在只读堆中，通过指针压缩将只读堆置于每个压缩笼起始位置，使undefined的压缩地址固定为0x61。JIT代码可直接通过地址比较判断对象类型，无需查找。该特性在Chrome 111落地，显著加速C++代码和内置函数。文章还介绍了通过mksnapshot在编译期创建只读对象并写入快照的引导过程。
- **原始摘要**: Did you ever wonder where undefined, true, and other core JavaScript objects come from? These objects are the atoms of any user defined object and need to be there first. V8 calls them immovable immut...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
