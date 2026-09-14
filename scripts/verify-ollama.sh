#!/bin/bash
# Ollama 安装验证脚本

echo "================================================"
echo "🔍 Ollama 安装验证"
echo "================================================"
echo ""

# 检查 Ollama 是否安装
echo "1. 检查 Ollama 安装..."
if command -v ollama &> /dev/null; then
    echo "   ✅ Ollama 已安装: $(ollama --version)"
else
    echo "   ❌ Ollama 未安装"
    echo ""
    echo "请运行以下命令安装:"
    echo "   curl -fsSL https://ollama.com/install.sh | sh"
    echo ""
    echo "或访问: https://ollama.com/download"
    exit 1
fi

echo ""

# 检查 Ollama 服务
echo "2. 检查 Ollama 服务..."
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "   ✅ Ollama 服务正在运行"
else
    echo "   ⚠️  Ollama 服务未运行"
    echo ""
    echo "请运行以下命令启动服务:"
    echo "   ollama serve"
    echo ""
    echo "或后台运行:"
    echo "   nohup ollama serve > /dev/null 2>&1 &"
    exit 1
fi

echo ""

# 列出已安装的模型
echo "3. 检查已安装模型..."
models=$(ollama list 2>&1)
echo "$models"

echo ""

# 检查推荐模型
if echo "$models" | grep -q "qwen2.5:3b"; then
    echo "   ✅ 推荐模型 qwen2.5:3b 已安装"
elif echo "$models" | grep -q "qwen2.5"; then
    echo "   ✅ Qwen2.5 模型已安装"
elif echo "$models" | grep -q "llama3.2"; then
    echo "   ✅ Llama3.2 模型已安装"
elif echo "$models" | grep -q "gemma2"; then
    echo "   ✅ Gemma2 模型已安装"
else
    echo "   ⚠️  未找到推荐模型"
    echo ""
    echo "建议安装以下模型之一:"
    echo "   ollama pull qwen2.5:3b     # 推荐：中文最佳"
    echo "   ollama pull llama3.2:3b    # 备选：通用模型"
    echo "   ollama pull gemma2:2b      # 备选：最轻量"
    exit 1
fi

echo ""
echo "================================================"
echo "✅ Ollama 配置完成！"
echo "================================================"
echo ""
echo "下一步:"
echo "  cd scripts"
echo "  python3 test-local-classifier.py  # 测试分类器"
echo "  ./run-rss.sh                      # 运行 RSS 聚合器"
echo ""
