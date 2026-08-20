#!/bin/bash
# AI技术追踪 - 每日自动运行脚本
# 此脚本由 launchd 调用，每天运行一次

# 设置工作目录
cd /Users/rede/Git/deep_analysis

# 设置日志目录
LOG_DIR="/Users/rede/Git/deep_analysis/logs"
mkdir -p "$LOG_DIR"

# 日志文件（按日期命名）
LOG_FILE="$LOG_DIR/daily-run-$(date +%Y-%m-%d).log"

# 记录开始时间
echo "========================================" >> "$LOG_FILE"
echo "开始时间: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"

# 激活Python环境（如果使用虚拟环境）
# source venv/bin/activate

# 运行爬虫
echo "正在运行 RSS 聚合器..." >> "$LOG_FILE"
python3 /Users/rede/Git/deep_analysis/scripts/rss-aggregator.py >> "$LOG_FILE" 2>&1

# 记录退出状态
EXIT_CODE=$?
echo "" >> "$LOG_FILE"
echo "退出代码: $EXIT_CODE" >> "$LOG_FILE"
echo "结束时间: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# 清理30天前的日志
find "$LOG_DIR" -name "daily-run-*.log" -mtime +30 -delete

exit $EXIT_CODE
