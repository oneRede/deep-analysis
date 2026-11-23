# RSS 聚合报告 - 编译器

**生成时间**: 2026-11-24 07:38:17
**文章数量**: 2 篇

---

### 1. Seeing the machine code of your Java program, with a few lines of Java
- **来源**: Daniel Lemire's blog (TIER2)
- **发布日期**: Mon, 23 Nov 2026 13:00:38 +0000 (今天)
- **类型**: blog
- **优先级**: high
- **分类**: 编译器
- **链接**: https://lemire.me/blog/2026/11/23/seeing-the-machine-code-of-your-java-program/
- **AI 摘要**: 本文作者通过使用JMH工具来分析Java程序的性能问题，并进一步通过查看JIT编译器生成的机器码来找出性能瓶颈所在。
- **原始摘要**: When I want to know why some Java code is slow, I usually reach for JMH. JMH is great to time a function. But a timing tells you how slow the code is, not why. For that, you need to see the machine co...

### 2. Exposing Call-Shared Stacks to a Meta-Tracing JIT Compiler
- **来源**: arXiv cs.PL (编程语言) (TIER1)
- **提交时间**: 2026年09月
- **类型**: arxiv
- **优先级**: high
- **分类**: 编译器
- **链接**: https://arxiv.org/abs/2609.23759
- **AI 摘要**: 本文提出了一种新的共享数据栈布局方法，该方法将共享数据栈分为固定宽度的顶部片段和共享溢出数组，以供元追踪JIT编译器访问。
- **原始摘要**: arXiv:2609.23759v2 Announce Type: replace Abstract: Meta-tracing JIT compilers such as RPython's can optimize accesses to interpreter state when the state is represented in a form that the optimizer c...

---

## 📋 下一步行动

1. **人工审查**: 阅读上述文章，标记高价值候选
2. **深度分析**: 将候选 URL 喂给 Claude，运行 `prompts/deep-research-tracker.md` 的 Prompt B
3. **启动流水线**: 对确认收录的内容，使用 `/curate-research` skill

**提示**: 可以将本报告内容复制到 Claude，让 AI 帮助初步筛选。
