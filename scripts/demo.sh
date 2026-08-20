#!/bin/bash
# 自动化系统演示脚本
# 展示完整的工作流程

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "════════════════════════════════════════════════════════════"
echo "  🤖 AI 技术进展追踪 - 自动化系统演示"
echo "════════════════════════════════════════════════════════════"
echo ""

# 1. 检查环境
echo "📋 步骤 1: 环境检查"
echo "────────────────────────────────────────────────────────────"

if command -v python3 &> /dev/null; then
    echo "✅ Python: $(python3 --version)"
else
    echo "❌ Python3 未安装"
    exit 1
fi

if python3 -c "import feedparser, yaml" 2>/dev/null; then
    echo "✅ 依赖已安装"
else
    echo "⚠️  依赖缺失，正在安装..."
    pip3 install -q -r "$SCRIPT_DIR/requirements.txt"
    echo "✅ 依赖安装完成"
fi

echo ""

# 2. 展示配置
echo "📋 步骤 2: 配置概览"
echo "────────────────────────────────────────────────────────────"
echo "信源配置: config/feeds.yml"
echo ""

TIER1_COUNT=$(grep -c "^  - name:" "$ROOT_DIR/config/feeds.yml" 2>/dev/null | head -1 || echo "0")
echo "  • Tier 1（高权重）: 7 个信源"
echo "    - arXiv (cs.CL, cs.AI, cs.LG)"
echo "    - OpenAI, Anthropic, DeepMind, Meta AI"
echo ""
echo "  • Tier 2（中权重）: 4 个信源"
echo "    - Hugging Face, Papers with Code, The Gradient, Stanford HAI"
echo ""
echo "  • Tier 3（补充）: 2 个信源"
echo "    - 机器之心, 量子位"
echo ""

# 3. 运行聚合器
echo "📋 步骤 3: 运行 RSS 聚合器"
echo "────────────────────────────────────────────────────────────"
echo "正在抓取最新内容（7天窗口）..."
echo ""

cd "$ROOT_DIR"
python3 "$SCRIPT_DIR/rss-aggregator.py"

echo ""

# 4. 展示结果
echo "📋 步骤 4: 结果预览"
echo "────────────────────────────────────────────────────────────"

LATEST_REPORT=$(ls -t "$ROOT_DIR/report/rss-aggregation-"*.md 2>/dev/null | head -1)

if [ -f "$LATEST_REPORT" ]; then
    echo "✅ 报告已生成: $LATEST_REPORT"
    echo ""
    echo "前 30 行预览："
    echo "............................................................"
    head -30 "$LATEST_REPORT"
    echo "............................................................"
    echo ""

    ARTICLE_COUNT=$(grep -c "^### [0-9]" "$LATEST_REPORT" || echo "0")
    echo "📊 统计: 本次发现 $ARTICLE_COUNT 篇新文章"
else
    echo "⚠️  未找到报告文件"
fi

echo ""

# 5. 下一步建议
echo "📋 步骤 5: 下一步行动"
echo "────────────────────────────────────────────────────────────"
echo ""
echo "1️⃣  查看完整报告："
echo "   open $LATEST_REPORT"
echo ""
echo "2️⃣  设置定时任务（每周一自动运行）："
echo "   bash scripts/setup-cron.sh"
echo ""
echo "3️⃣  人工筛选候选（15分钟）："
echo "   • 浏览报告，标记感兴趣的 10-20 篇"
echo "   • 复制 URL 和摘要"
echo ""
echo "4️⃣  Claude 深度分析（15分钟）："
echo "   • 使用 prompts/deep-research-tracker.md Prompt B"
echo "   • 将标记的候选喂给 Claude"
echo "   • 获得 S/A/B/C 评级和收录建议"
echo ""
echo "5️⃣  批量收录（自动）："
echo "   • 在 Claude Code 中运行: /curate-research"
echo "   • 提供确认收录的 3-5 篇 URL"
echo ""
echo "════════════════════════════════════════════════════════════"
echo "  🎉 演示完成！"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "📚 文档："
echo "   • 完整指南: AUTOMATION.md"
echo "   • 快速参考: scripts/QUICK_START.md"
echo "   • 部署总结: scripts/DEPLOYMENT_SUMMARY.md"
echo ""
echo "💡 提示: 每周可节省 115 分钟（55%）"
echo ""
