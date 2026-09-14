#!/bin/bash
# macOS 本地模型完整安装指南

echo "================================================"
echo "🚀 本地模型分类器 - macOS 安装指南"
echo "================================================"
echo ""

echo "📋 安装步骤："
echo ""

echo "【步骤 1】安装 Ollama"
echo "----------------------------------------"
echo "运行以下命令："
echo ""
echo "  curl -fsSL https://ollama.com/install.sh | sh"
echo ""
echo "或者访问 https://ollama.com/download 下载安装包"
echo ""
read -p "已安装 Ollama? (按回车继续，或按 Ctrl+C 退出) "

echo ""
echo "【步骤 2】启动 Ollama 服务"
echo "----------------------------------------"
echo "Ollama 通常会自动启动。如果没有，运行："
echo ""
echo "  ollama serve"
echo ""
echo "或后台运行："
echo ""
echo "  nohup ollama serve > /dev/null 2>&1 &"
echo ""

# 等待用户启动服务
echo "正在检测 Ollama 服务..."
for i in {1..10}; do
    if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
        echo "✅ Ollama 服务已启动"
        break
    fi
    if [ $i -eq 10 ]; then
        echo "⚠️  未检测到 Ollama 服务，请手动启动"
        exit 1
    fi
    sleep 1
done

echo ""
echo "【步骤 3】下载推荐模型"
echo "----------------------------------------"
echo "推荐使用 Qwen2.5-3B (中文最佳，约 1.9GB)："
echo ""
echo "  ollama pull qwen2.5:3b"
echo ""

read -p "是否现在下载 qwen2.5:3b? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📥 下载中 (需要几分钟，取决于网速)..."
    ollama pull qwen2.5:3b

    if [ $? -eq 0 ]; then
        echo "✅ 模型下载完成"
    else
        echo "❌ 模型下载失败"
        exit 1
    fi
else
    echo "跳过下载。稍后可以运行："
    echo "  ollama pull qwen2.5:3b"
    exit 0
fi

echo ""
echo "【步骤 4】验证配置"
echo "----------------------------------------"
echo "运行验证脚本..."
echo ""

if [ -f "scripts/verify-ollama.sh" ]; then
    ./scripts/verify-ollama.sh
else
    echo "⚠️  找不到验证脚本，手动验证："
    echo "  ollama list"
fi

echo ""
echo "【步骤 5】测试分类器"
echo "----------------------------------------"
echo "运行测试："
echo ""
echo "  cd scripts"
echo "  python3 test-local-classifier.py"
echo ""

read -p "是否现在运行测试? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    cd scripts
    python3 test-local-classifier.py
    cd ..
fi

echo ""
echo "================================================"
echo "✅ 安装完成！"
echo "================================================"
echo ""
echo "现在可以运行 RSS 聚合器："
echo ""
echo "  cd scripts"
echo "  ./run-rss.sh"
echo ""
echo "或者运行快速诊断："
echo ""
echo "  python3 scripts/test-local-classifier.py"
echo ""
echo "文档："
echo "  • 快速参考: scripts/QUICK_REFERENCE.md"
echo "  • 完整指南: scripts/LOCAL_CLASSIFIER_GUIDE.md"
echo ""
