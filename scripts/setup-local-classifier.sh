#!/bin/bash
# 本地分类器快速设置脚本

set -e

echo "=============================================="
echo "🚀 本地分类器快速设置"
echo "=============================================="
echo ""

# 检查 Ollama 是否安装
echo "📦 检查 Ollama 安装状态..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama 已安装: $(ollama --version)"
else
    echo "❌ Ollama 未安装"
    echo ""
    echo "请访问以下链接安装 Ollama:"
    echo "  - macOS/Linux: curl -fsSL https://ollama.com/install.sh | sh"
    echo "  - Windows: https://ollama.com/download"
    echo ""
    exit 1
fi

echo ""

# 检查 Ollama 服务是否运行
echo "🔍 检查 Ollama 服务状态..."
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "✅ Ollama 服务正在运行"
else
    echo "⚠️  Ollama 服务未运行"
    echo "启动服务: ollama serve"
    echo ""

    # 尝试启动服务
    echo "尝试启动 Ollama 服务..."
    if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
        nohup ollama serve > /dev/null 2>&1 &
        sleep 2

        if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
            echo "✅ Ollama 服务已启动"
        else
            echo "❌ 无法启动 Ollama 服务，请手动运行: ollama serve"
            exit 1
        fi
    else
        echo "请手动运行: ollama serve"
        exit 1
    fi
fi

echo ""

# 列出已安装的模型
echo "📋 已安装的模型:"
ollama list

echo ""

# 推荐模型列表
RECOMMENDED_MODELS=("qwen2.5:3b" "qwen2.5:1.5b" "llama3.2:3b" "gemma2:2b")
INSTALLED_RECOMMENDED=false

for model in "${RECOMMENDED_MODELS[@]}"; do
    if ollama list | grep -q "$model"; then
        INSTALLED_RECOMMENDED=true
        echo "✅ 推荐模型 $model 已安装"
        break
    fi
done

echo ""

if [ "$INSTALLED_RECOMMENDED" = false ]; then
    echo "💡 推荐安装以下模型之一:"
    echo ""
    echo "  1. qwen2.5:3b (推荐) - 中文最佳，3GB 显存"
    echo "  2. llama3.2:3b - 英文强，中文可用，3GB 显存"
    echo "  3. gemma2:2b - 最轻量，速度快，2GB 显存"
    echo ""

    read -p "是否现在下载 qwen2.5:3b? (y/n) " -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📥 下载 qwen2.5:3b (这可能需要几分钟)..."
        ollama pull qwen2.5:3b
        echo "✅ 模型下载完成"
    else
        echo "跳过下载。稍后可以运行: ollama pull qwen2.5:3b"
    fi
fi

echo ""

# 测试分类器
echo "🧪 测试本地分类器..."
cd "$(dirname "$0")"

if [ -f "local_classifier.py" ]; then
    python3 local_classifier.py

    if [ $? -eq 0 ]; then
        echo ""
        echo "=============================================="
        echo "✅ 设置完成！"
        echo "=============================================="
        echo ""
        echo "下一步:"
        echo "  1. 确认 config/feeds.yml 中 classifier 设置为 'local'"
        echo "  2. 运行: ./run-rss.sh"
        echo ""
        echo "详细文档: scripts/LOCAL_CLASSIFIER_GUIDE.md"
    else
        echo ""
        echo "❌ 分类器测试失败"
        echo "请检查上述错误信息"
    fi
else
    echo "❌ 找不到 local_classifier.py"
fi
