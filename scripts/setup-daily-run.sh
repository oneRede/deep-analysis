#!/bin/bash
# AI技术追踪 - 快速设置脚本

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   AI技术追踪系统 - 每日自动运行设置"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 检查Python
echo "🔍 检查依赖..."
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 python3"
    echo "请先安装 Python 3"
    exit 1
fi
echo "✅ Python3: $(python3 --version)"

# 检查必要的Python包
echo ""
echo "🔍 检查 Python 依赖包..."
MISSING_PACKAGES=""

for package in requests beautifulsoup4 feedparser pyyaml cloudscraper; do
    if ! python3 -c "import ${package//-/_}" 2>/dev/null; then
        MISSING_PACKAGES="$MISSING_PACKAGES $package"
    fi
done

if [ -n "$MISSING_PACKAGES" ]; then
    echo "⚠️  缺少以下包:$MISSING_PACKAGES"
    echo ""
    read -p "是否安装缺少的包？ (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📦 正在安装依赖包..."
        pip3 install $MISSING_PACKAGES --user
        if [ $? -ne 0 ]; then
            echo "❌ 安装失败"
            exit 1
        fi
        echo "✅ 依赖包安装完成"
    else
        echo "❌ 请手动安装: pip3 install$MISSING_PACKAGES --user"
        exit 1
    fi
else
    echo "✅ 所有依赖包已安装"
fi

# 创建必要的目录
echo ""
echo "📁 创建目录结构..."
mkdir -p /Users/rede/Git/deep_analysis/logs
mkdir -p /Users/rede/Git/deep_analysis/report
echo "✅ 目录创建完成"

# 测试运行
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🧪 测试运行"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
read -p "是否进行测试运行？这将获取昨天的文章 (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "▶️  开始测试运行..."
    echo ""
    /Users/rede/Git/deep_analysis/scripts/daily-run.sh

    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ 测试运行成功！"
        echo ""
        echo "📊 生成的报告目录:"
        ls -lt /Users/rede/Git/deep_analysis/report/ 2>/dev/null | grep "^d" | head -1 | awk '{print "   📁", $9}'

        # 显示最新目录中的文件
        LATEST_DIR=$(ls -t /Users/rede/Git/deep_analysis/report/ 2>/dev/null | grep -E "^[0-9]{4}-[0-9]{2}-[0-9]{2}$" | head -1)
        if [ -n "$LATEST_DIR" ]; then
            echo "   包含文件:"
            ls /Users/rede/Git/deep_analysis/report/$LATEST_DIR/*.md 2>/dev/null | awk '{print "     📄", $0}'
        fi
    else
        echo ""
        echo "❌ 测试运行失败"
        echo "请查看日志: cat logs/daily-run-$(date +%Y-%m-%d).log"
        exit 1
    fi
fi

# 安装自动运行
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📅 安装每日自动运行"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "系统将配置为每天早上 8:00 自动运行"
echo ""
read -p "是否安装自动运行任务？ (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    /Users/rede/Git/deep_analysis/scripts/manage-daily-task.sh install

    if [ $? -eq 0 ]; then
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "✅ 设置完成！"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        echo "📅 任务: 每天早上 8:00 自动运行"
        echo "📊 报告: /Users/rede/Git/deep_analysis/report/"
        echo "📝 日志: /Users/rede/Git/deep_analysis/logs/"
        echo ""
        echo "常用命令:"
        echo "  查看状态: ./scripts/manage-daily-task.sh status"
        echo "  查看日志: ./scripts/manage-daily-task.sh logs"
        echo "  立即运行: ./scripts/manage-daily-task.sh start"
        echo "  卸载任务: ./scripts/manage-daily-task.sh uninstall"
        echo ""
        echo "📖 完整文档: DAILY_SCHEDULE_GUIDE.md"
        echo ""
    else
        echo "❌ 安装失败"
        exit 1
    fi
else
    echo ""
    echo "⏭️  跳过自动运行安装"
    echo ""
    echo "如需稍后安装，运行:"
    echo "  ./scripts/manage-daily-task.sh install"
    echo ""
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 所有设置已完成！"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
