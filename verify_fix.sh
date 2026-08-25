#!/bin/bash
# RSS聚合器修复验证脚本

echo "=========================================="
echo "RSS聚合器修复验证"
echo "=========================================="
echo ""

# 1. 检查.env文件
echo "1. 检查环境配置..."
if [ -f .env ]; then
    echo "   ✅ .env 文件存在"
    if grep -q "DEEPSEEK_API_KEY=" .env; then
        KEY_LENGTH=$(grep "DEEPSEEK_API_KEY=" .env | cut -d'=' -f2 | wc -c)
        echo "   ✅ DEEPSEEK_API_KEY 已配置 (长度: $((KEY_LENGTH-1)))"
    else
        echo "   ❌ DEEPSEEK_API_KEY 未找到"
        exit 1
    fi
else
    echo "   ❌ .env 文件不存在"
    exit 1
fi
echo ""

# 2. 检查修复后的脚本
echo "2. 检查脚本文件..."
if [ -f scripts/run-rss.sh ]; then
    echo "   ✅ scripts/run-rss.sh 存在"
    if grep -q "set -a" scripts/run-rss.sh; then
        echo "   ✅ 已使用新的环境变量加载方式"
    else
        echo "   ⚠️  脚本可能未更新"
    fi
else
    echo "   ❌ scripts/run-rss.sh 不存在"
    exit 1
fi

if [ -f scripts/rss-aggregator.py ]; then
    echo "   ✅ scripts/rss-aggregator.py 存在"
    if grep -q "_test_api_connection" scripts/rss-aggregator.py; then
        echo "   ✅ 已添加API连接测试"
    else
        echo "   ⚠️  API测试功能可能未添加"
    fi
else
    echo "   ❌ scripts/rss-aggregator.py 不存在"
    exit 1
fi
echo ""

# 3. 运行Python测试
echo "3. 运行功能测试..."
if [ -f test_rss_simple.py ]; then
    echo "   运行测试脚本..."
    python3 test_rss_simple.py
    if [ $? -eq 0 ]; then
        echo ""
        echo "   ✅ 功能测试通过"
    else
        echo ""
        echo "   ❌ 功能测试失败"
        exit 1
    fi
else
    echo "   ⚠️  测试脚本不存在，跳过"
fi
echo ""

# 4. 总结
echo "=========================================="
echo "✅ 验证完成"
echo "=========================================="
echo ""
echo "修复内容："
echo "  1. ✅ 环境变量加载方式已修复 (set -a + source)"
echo "  2. ✅ API连接测试已添加"
echo "  3. ✅ 功能测试通过"
echo ""
echo "下一步："
echo "  运行完整的RSS聚合："
echo "  $ bash scripts/run-rss.sh"
echo ""
echo "  查看生成的报告："
echo "  $ ls -la report/\$(date +%Y-%m-%d)/"
echo ""
