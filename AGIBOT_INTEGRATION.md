# Agibot Research 信源集成说明

## 概述

已成功将 Agibot Research (https://agibot.com/research/) 集成到 RSS 聚合系统中。

## 实施详情

### 1. 技术挑战

Agibot Research 页面是一个 JavaScript 渲染的单页应用（SPA），研究内容存储在独立的 JavaScript 数据文件中，无法通过传统的 HTML 解析获取。

**数据源位置**: `https://agibot.com/research/content/featured.js`

### 2. 解决方案

在 `scripts/web_scraper.py` 中添加了专门的爬虫函数 `scrape_agibot_research()`，该函数：

1. 直接获取 `featured.js` JavaScript 文件
2. 使用正则表达式提取 `window.FEATURED` 数组
3. 将 JavaScript 数组解析为 JSON 格式
4. 提取每篇研究的元数据：
   - title: 研究标题
   - venue: 发表会议/期刊 (如 "CVPR 2026", "arXiv 2026")
   - date: 发布日期 (格式: "YYYY-MM")
   - desc: 一句话描述
   - project: 项目主页链接
   - github: GitHub 代码仓库链接

### 3. 代码修改

#### 新增函数 (`scripts/web_scraper.py:712-791`)

```python
def scrape_agibot_research(self, days_lookback: int = 7) -> List[Dict]:
    """
    爬取 Agibot Research 页面的研究项目
    URL: https://agibot.com/research/
    注意：内容存储在 JavaScript 文件中
    """
```

**核心特性**:
- 解析 JavaScript 数组数据
- 支持时间窗口过滤（`days_lookback` 参数）
- 优先使用项目主页链接，其次使用 GitHub 链接
- 自动构建摘要（包含发表信息和描述）
- 将研究类型标记为 `research`，优先级为 `high`

#### 集成到主流程 (`scripts/web_scraper.py:1228-1230`)

在 `scrape_all_custom_sources()` 函数中添加了对 Agibot Research 的调用：

```python
# 爬取 Agibot Research (JavaScript-based, 需要特殊处理)
all_articles.extend(scraper.scrape_agibot_research(days_lookback))
time.sleep(1)
```

#### 更新配置 (`scripts/web_scraper.py:850-856`)

从通用的 `scrape_embodied_ai_companies()` 函数中移除了 Agibot Research URL，因为它现在由专门的函数处理：

```python
{
    'name': 'Agibot (智元机器人)',
    'urls': [
        ('https://agibot.com/news', ['/news', '/article']),
        # Research page handled by scrape_agibot_research() - JavaScript-based
    ]
}
```

### 4. 测试结果

运行 `python3 test_agibot.py` 测试成功，找到 **4 篇研究论文**：

1. **GE-Sim 2.0** (2026-05)
   - 发表于 arXiv 2026
   - 闭环视频世界模拟器用于机器人操作
   - 链接: https://ge-sim-v2.github.io/

2. **RoboClaw** (2026-03)
   - 发表于 ECCV 2026
   - 可扩展长时程机器人任务的智能体框架
   - 链接: https://roboclaw-agibot.github.io/

3. **ACoT-VLA** (2026-02)
   - 发表于 CVPR 2026
   - 视觉-语言-动作模型的动作链思维方法
   - 链接: https://github.com/AgibotTech/ACoT-VLA

4. **Act2Goal** (2026-01)
   - 发表于 RSS 2026
   - 从世界模型到通用目标条件策略
   - 链接: https://act2goal.github.io/

### 5. 信源分类

Agibot Research 属于 **具身智能（Embodied Intelligence）** 领域，研究内容涵盖：
- 世界模型（World Model）
- 机器人学习（Robot Learning）
- 视觉-语言-动作模型（Vision-Language-Action Models）
- 机器人操作（Robotic Manipulation）

在 RSS 聚合系统中，这些文章会被自动分类到相应的技术类别中。

### 6. 维护说明

- **自动更新**: 每次运行 `scripts/rss-aggregator.py` 时会自动爬取最新研究
- **时间窗口**: 默认获取最近 7 天内的研究（可通过 `days_lookback` 参数调整）
- **去重机制**: 系统会自动对 URL 去重，避免重复收录
- **数据源稳定性**: Agibot 的数据格式相对稳定，但如果未来修改了 JavaScript 文件结构，需要相应更新解析逻辑

## 相关文件

- `scripts/web_scraper.py` - 主要爬虫实现
- `config/feeds.yml` - RSS 信源配置（Agibot 不需要在此配置）
- `test_agibot.py` - 独立测试脚本

## 后续优化建议

1. **错误处理增强**: 添加更详细的异常处理和日志记录
2. **数据验证**: 对解析的 JSON 数据进行更严格的验证
3. **缓存机制**: 考虑缓存 JavaScript 文件以减少网络请求
4. **监控告警**: 如果数据源格式变化，及时告警

## 总结

✅ Agibot Research 已成功集成到 RSS 聚合系统中
✅ 支持自动爬取和分类
✅ 测试通过，可正常工作
✅ 文档完整，便于后续维护
