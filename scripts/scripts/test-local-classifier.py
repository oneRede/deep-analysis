#!/usr/bin/env python3
"""
快速测试脚本 - 验证本地分类器配置
"""

import sys
import requests

def main():
    print("=" * 60)
    print("🔍 本地分类器快速诊断")
    print("=" * 60)
    print()

    # 1. 检查 Ollama 连接
    print("1️⃣  检查 Ollama 服务...")
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("   ✅ Ollama 服务正常")
            models = response.json().get('models', [])
            if models:
                print(f"   📦 已安装 {len(models)} 个模型:")
                for model in models:
                    print(f"      - {model['name']}")
            else:
                print("   ⚠️  未安装任何模型")
                print("   💡 运行: ollama pull qwen2.5:3b")
                return False
        else:
            print(f"   ❌ Ollama API 错误: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ 无法连接 Ollama: {str(e)}")
        print("   💡 请确保 Ollama 已启动: ollama serve")
        return False

    print()

    # 2. 检查推荐模型
    print("2️⃣  检查推荐模型...")
    recommended = ['qwen2.5:3b', 'qwen2.5:1.5b', 'llama3.2:3b', 'gemma2:2b']
    model_names = [m['name'] for m in models]
    found = None

    for model in recommended:
        if model in model_names:
            found = model
            print(f"   ✅ 找到推荐模型: {model}")
            break

    if not found:
        print("   ⚠️  未找到推荐模型")
        print("   💡 建议安装: ollama pull qwen2.5:3b")
        return False

    print()

    # 3. 测试分类功能
    print("3️⃣  测试分类功能...")
    try:
        from local_classifier import LocalClassifier

        classifier = LocalClassifier(model=found)

        test_article = {
            'title': 'OpenAI 发布新一代大语言模型',
            'summary': '该模型在推理和编程能力上有显著提升',
        }

        test_categories = [
            {'key': 'ai_model', 'name': 'AI模型', 'description': '关于新模型、模型架构'},
            {'key': 'ai_application', 'name': 'AI应用', 'description': '关于AI应用场景'},
        ]

        print(f"   🤖 使用模型: {found}")
        print("   ⏳ 处理测试文章...")

        summary, category = classifier.classify_and_summarize_single(
            test_article,
            test_categories,
            'ai_application',
            max_length=100
        )

        if summary and category:
            print("   ✅ 分类成功!")
            print(f"   📝 摘要: {summary[:50]}...")
            print(f"   🏷️  分类: {category}")
        else:
            print("   ⚠️  分类返回空结果")
            return False

    except Exception as e:
        print(f"   ❌ 分类测试失败: {str(e)}")
        return False

    print()

    # 4. 检查配置文件
    print("4️⃣  检查配置文件...")
    try:
        import yaml
        with open('../config/feeds.yml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            ai_summary = config.get('ai_summary', {})

            enabled = ai_summary.get('enabled', False)
            classifier_type = ai_summary.get('classifier', 'unknown')
            local_model = ai_summary.get('local_model', 'not set')

            print(f"   📄 AI 摘要: {'启用' if enabled else '禁用'}")
            print(f"   🔧 分类器类型: {classifier_type}")
            print(f"   🤖 配置的模型: {local_model}")

            if classifier_type != 'local':
                print("   ⚠️  分类器未设置为 'local'")
                print("   💡 在 config/feeds.yml 中设置: classifier: 'local'")
            else:
                print("   ✅ 配置正确")

    except Exception as e:
        print(f"   ⚠️  无法读取配置: {str(e)}")

    print()
    print("=" * 60)
    print("✅ 诊断完成 - 本地分类器已就绪!")
    print("=" * 60)
    print()
    print("下一步:")
    print("  • 运行 RSS 聚合器: ./run-rss.sh")
    print("  • 查看完整文档: LOCAL_CLASSIFIER_GUIDE.md")
    print()
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
