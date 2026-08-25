#!/bin/bash
# RSS 聚合器 - 快速启动脚本
# 用途：一键运行 RSS 聚合，无需记住路径

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$ROOT_DIR"

# 加载环境变量 - 修复版
if [ -f "$ROOT_DIR/.env" ]; then
    # 使用 set -a 来自动导出所有变量
    set -a
    source "$ROOT_DIR/.env"
    set +a
    echo "✅ 已加载环境变量"

    # 验证关键环境变量
    if [ -z "$DEEPSEEK_API_KEY" ]; then
        echo "⚠️  警告: DEEPSEEK_API_KEY 未设置"
    else
        echo "✅ DEEPSEEK_API_KEY 已设置 (长度: ${#DEEPSEEK_API_KEY})"
    fi
fi

echo "🚀 运行 RSS 聚合器..."
echo ""

python3 "$SCRIPT_DIR/rss-aggregator.py"

echo ""
echo "📄 查看报告："
echo "   open report/rss-aggregation-$(date +%Y-%m-%d).md"
echo ""
echo "💡 下一步："
echo "   1. 浏览报告，标记感兴趣的文章"
echo "   2. 将候选 URL 喂给 Claude，运行深度分析"
echo "   3. 对确认收录的内容使用 /curate-research skill"
