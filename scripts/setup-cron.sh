#!/bin/bash
# 设置定时任务 - RSS 聚合器
# 用途：配置 macOS launchd 或 cron，每周一自动运行 RSS 聚合

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
PYTHON_PATH="/usr/bin/python3"

echo "🔧 RSS 聚合器定时任务设置"
echo "================================"
echo "脚本目录: $SCRIPT_DIR"
echo "根目录: $ROOT_DIR"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

echo "✅ Python: $(python3 --version)"

# 检查依赖
echo ""
echo "📦 检查依赖..."
if ! python3 -c "import feedparser" 2>/dev/null; then
    echo "⚠️  feedparser 未安装，正在安装..."
    pip3 install -r "$SCRIPT_DIR/requirements.txt"
else
    echo "✅ 依赖已安装"
fi

# 检测操作系统
OS="$(uname -s)"

if [ "$OS" = "Darwin" ]; then
    echo ""
    echo "📱 检测到 macOS，配置 launchd..."

    PLIST_FILE="$HOME/Library/LaunchAgents/com.deepanalysis.rss-aggregator.plist"

    cat > "$PLIST_FILE" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.deepanalysis.rss-aggregator</string>

    <key>ProgramArguments</key>
    <array>
        <string>$PYTHON_PATH</string>
        <string>$SCRIPT_DIR/rss-aggregator.py</string>
    </array>

    <key>WorkingDirectory</key>
    <string>$ROOT_DIR</string>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>1</integer>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>$ROOT_DIR/scripts/.rss-aggregator.log</string>

    <key>StandardErrorPath</key>
    <string>$ROOT_DIR/scripts/.rss-aggregator.error.log</string>

    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
EOF

    echo "✅ 创建 launchd plist: $PLIST_FILE"

    # 加载任务
    if launchctl list | grep -q "com.deepanalysis.rss-aggregator"; then
        echo "🔄 重新加载现有任务..."
        launchctl unload "$PLIST_FILE" 2>/dev/null || true
    fi

    launchctl load "$PLIST_FILE"
    echo "✅ launchd 任务已加载"

    echo ""
    echo "📋 任务详情:"
    echo "   • 执行时间: 每周一 09:00"
    echo "   • 日志文件: $ROOT_DIR/scripts/.rss-aggregator.log"
    echo "   • 错误日志: $ROOT_DIR/scripts/.rss-aggregator.error.log"
    echo ""
    echo "🛠️  管理命令:"
    echo "   • 查看状态: launchctl list | grep rss-aggregator"
    echo "   • 手动运行: launchctl start com.deepanalysis.rss-aggregator"
    echo "   • 停止任务: launchctl unload $PLIST_FILE"
    echo "   • 查看日志: tail -f $ROOT_DIR/scripts/.rss-aggregator.log"

elif [ "$OS" = "Linux" ]; then
    echo ""
    echo "🐧 检测到 Linux，配置 crontab..."

    CRON_ENTRY="0 9 * * 1 cd $ROOT_DIR && $PYTHON_PATH $SCRIPT_DIR/rss-aggregator.py >> $SCRIPT_DIR/.rss-aggregator.log 2>&1"

    # 检查是否已存在
    if crontab -l 2>/dev/null | grep -q "rss-aggregator.py"; then
        echo "⚠️  crontab 中已存在相关任务，请手动检查"
        crontab -l | grep "rss-aggregator.py"
    else
        # 添加到 crontab
        (crontab -l 2>/dev/null; echo "$CRON_ENTRY") | crontab -
        echo "✅ crontab 任务已添加"

        echo ""
        echo "📋 任务详情:"
        echo "   • 执行时间: 每周一 09:00"
        echo "   • 日志文件: $SCRIPT_DIR/.rss-aggregator.log"
        echo ""
        echo "🛠️  管理命令:"
        echo "   • 查看任务: crontab -l | grep rss-aggregator"
        echo "   • 编辑任务: crontab -e"
        echo "   • 查看日志: tail -f $SCRIPT_DIR/.rss-aggregator.log"
    fi
else
    echo "❌ 不支持的操作系统: $OS"
    exit 1
fi

echo ""
echo "🎉 设置完成！"
echo ""
echo "💡 提示："
echo "   1. 首次运行可以手动测试: python3 $SCRIPT_DIR/rss-aggregator.py"
echo "   2. 报告文件将保存到: $ROOT_DIR/report/rss-aggregation-*.md"
echo "   3. 可以随时修改 config/feeds.yml 调整信源和过滤规则"
