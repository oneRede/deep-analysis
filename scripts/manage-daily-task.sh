#!/bin/bash
# AI技术追踪 - 自动运行管理脚本

PLIST_FILE="com.user.ai-tech-tracker.daily.plist"
PLIST_SOURCE="/Users/rede/Git/deep_analysis/scripts/$PLIST_FILE"
PLIST_DEST="$HOME/Library/LaunchAgents/$PLIST_FILE"

show_usage() {
    echo "AI技术追踪 - 自动运行管理"
    echo ""
    echo "用法: $0 {install|uninstall|start|stop|status|logs}"
    echo ""
    echo "命令:"
    echo "  install    - 安装每日自动运行任务（每天早上8点）"
    echo "  uninstall  - 卸载自动运行任务"
    echo "  start      - 启动任务（立即运行一次）"
    echo "  stop       - 停止任务"
    echo "  status     - 查看任务状态"
    echo "  logs       - 查看最近的运行日志"
    echo "  test       - 测试运行（不安装定时任务）"
}

install_task() {
    echo "📦 正在安装每日自动运行任务..."

    # 检查源文件
    if [ ! -f "$PLIST_SOURCE" ]; then
        echo "❌ 错误: 找不到配置文件 $PLIST_SOURCE"
        exit 1
    fi

    # 创建目标目录
    mkdir -p "$HOME/Library/LaunchAgents"

    # 复制配置文件
    cp "$PLIST_SOURCE" "$PLIST_DEST"
    echo "✅ 已复制配置文件到 $PLIST_DEST"

    # 加载任务
    launchctl load "$PLIST_DEST"

    if [ $? -eq 0 ]; then
        echo "✅ 任务安装成功！"
        echo ""
        echo "📅 任务将在每天早上 8:00 自动运行"
        echo "📊 报告保存在: /Users/rede/Git/deep_analysis/report/"
        echo "📝 日志保存在: /Users/rede/Git/deep_analysis/logs/"
        echo ""
        echo "使用 '$0 status' 查看任务状态"
        echo "使用 '$0 logs' 查看运行日志"
    else
        echo "❌ 任务安装失败"
        exit 1
    fi
}

uninstall_task() {
    echo "🗑️  正在卸载自动运行任务..."

    if [ ! -f "$PLIST_DEST" ]; then
        echo "⚠️  任务未安装"
        exit 0
    fi

    # 卸载任务
    launchctl unload "$PLIST_DEST"
    rm "$PLIST_DEST"

    echo "✅ 任务已卸载"
}

start_task() {
    echo "▶️  正在启动任务（立即运行一次）..."

    if [ ! -f "$PLIST_DEST" ]; then
        echo "❌ 任务未安装，请先运行: $0 install"
        exit 1
    fi

    launchctl start com.user.ai-tech-tracker.daily
    echo "✅ 任务已启动"
    echo "💡 使用 '$0 logs' 查看运行日志"
}

stop_task() {
    echo "⏹️  正在停止任务..."
    launchctl stop com.user.ai-tech-tracker.daily
    echo "✅ 任务已停止"
}

show_status() {
    echo "📊 任务状态"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if [ ! -f "$PLIST_DEST" ]; then
        echo "状态: ❌ 未安装"
        echo ""
        echo "使用 '$0 install' 安装任务"
        return
    fi

    echo "配置文件: ✅ $PLIST_DEST"
    echo ""

    # 检查任务是否加载
    if launchctl list | grep -q "com.user.ai-tech-tracker.daily"; then
        echo "运行状态: ✅ 已加载"
        echo ""
        launchctl list com.user.ai-tech-tracker.daily
    else
        echo "运行状态: ⚠️  未加载"
        echo ""
        echo "使用 '$0 start' 启动任务"
    fi

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "最近的报告目录:"
    ls -lt /Users/rede/Git/deep_analysis/report/ 2>/dev/null | grep "^d" | head -5 | awk '{print "  📁", $9, "(" $6, $7, $8 ")"}'

    echo ""
    echo "最近的日志文件:"
    ls -lt /Users/rede/Git/deep_analysis/logs/daily-run-*.log 2>/dev/null | head -3 | awk '{print "  📝", $9, "(" $6, $7, $8 ")"}'
}

show_logs() {
    LOG_DIR="/Users/rede/Git/deep_analysis/logs"

    echo "📝 查看运行日志"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    # 查找最新的日志文件
    LATEST_LOG=$(ls -t "$LOG_DIR"/daily-run-*.log 2>/dev/null | head -1)

    if [ -z "$LATEST_LOG" ]; then
        echo "⚠️  没有找到日志文件"
        echo ""
        echo "日志文件位置: $LOG_DIR/daily-run-YYYY-MM-DD.log"
        return
    fi

    echo "最新日志: $(basename $LATEST_LOG)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    tail -50 "$LATEST_LOG"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "完整日志: $LATEST_LOG"
}

test_run() {
    echo "🧪 测试运行（不安装定时任务）"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    /Users/rede/Git/deep_analysis/scripts/daily-run.sh

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ 测试完成"
    echo ""
    echo "如果测试成功，使用 '$0 install' 安装定时任务"
}

# 主逻辑
case "$1" in
    install)
        install_task
        ;;
    uninstall)
        uninstall_task
        ;;
    start)
        start_task
        ;;
    stop)
        stop_task
        ;;
    status)
        show_status
        ;;
    logs)
        show_logs
        ;;
    test)
        test_run
        ;;
    *)
        show_usage
        exit 1
        ;;
esac

exit 0
