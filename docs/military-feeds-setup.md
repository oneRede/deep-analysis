# 军事新闻源配置说明

## 📊 配置概览

已将世界范围内著名的军事新闻媒体添加到 `~/git/deep_analysis/config/feeds.yml` 的 `military` 分类中。

## ✅ 可用的RSS源（4个）

以下媒体提供RSS订阅，可自动获取文章：

1. **Breaking Defense** - `https://breakingdefense.com/full-rss-feed/?v=2`
   - 状态: ✅ 正常 (30篇文章)
   - 优先级: high
   - 内容: 国防政策、武器系统报道

2. **TASS** - `http://tass.com/rss/v2.xml`
   - 状态: ✅ 正常 (100篇文章)
   - 优先级: medium
   - 内容: 俄罗斯官方通讯社军事报道

3. **Military.com** - `https://www.military.com/feed/`
   - 状态: ✅ 正常 (10篇文章)
   - 优先级: medium
   - 内容: 面向军人和军事爱好者的综合平台

4. **The War Zone** - `https://www.twz.com/feed`
   - 状态: ✅ 正常 (39篇文章)
   - 优先级: high
   - 内容: 深度军事分析和报道

## ⚠️  RSS不可用或需要检查（3个）

以下媒体的RSS源返回0篇文章，可能需要进一步调查：

1. **Defense News** - `https://www.defensenews.com/m/rss/`
   - 可能需要尝试其他RSS URL

2. **Military Times** - `https://www.militarytimes.com/m/rss/`
   - 可能需要尝试其他RSS URL

3. **Stars and Stripes** - `https://subscribe.stripes.com/rss`
   - 可能需要认证或不同的RSS端点

## 🕷️  网页爬虫支持（1个可用）

创建了 `scripts/military_scraper.py` 来爬取没有RSS的网站：

### 可用：

1. **Jane's Defence** - `https://www.janes.com`
   - 状态: ✅ 正常 (9篇文章)
   - 方法: 网页爬虫
   - 内容: 权威的防务情报和分析

### 暂时不可用：

2. **Army Technology** - `https://www.army-technology.com`
   - 状态: ❌ 403 Forbidden
   - 原因: 反爬虫保护
   - 建议: 需要使用代理或Selenium

3. **环球网军事** - `https://mil.huanqiu.com`
   - 状态: ⚠️  0篇文章
   - 原因: 页面结构识别问题
   - 建议: 需要改进爬虫逻辑

4. **中国军网** - `http://www.81.cn`
   - 状态: ❌ 重定向循环
   - 原因: HTTP/HTTPS重定向问题
   - 建议: 需要特殊处理

5. **Global Security** - `https://www.globalsecurity.org`
   - 状态: ❌ 403 Forbidden
   - 原因: 访问限制
   - 建议: 需要代理或特殊headers

## 🚀 使用方法

### 1. 运行完整的RSS聚合器

```bash
cd ~/git/deep_analysis/scripts
python3 rss-aggregator.py
```

这会：
- 抓取所有配置的RSS源（包括AI和军事类别）
- 运行网页爬虫获取无RSS的源
- 生成分类报告到 `report/` 目录

### 2. 仅测试军事新闻源

```bash
cd ~/git/deep_analysis/scripts
python3 test_military_feeds.py
```

这会测试所有军事RSS源和爬虫的可用性。

### 3. 仅运行军事爬虫

```bash
cd ~/git/deep_analysis/scripts
python3 military_scraper.py
```

## 📝 配置文件结构

### feeds.yml

```yaml
military:
  - name: "Breaking Defense"
    url: "https://breakingdefense.com/full-rss-feed/?v=2"
    type: "news"
    priority: "high"
    keywords:
      - "defense"
      - "weapons systems"
      - "military technology"
  
  # ... 其他源
```

### rss-aggregator.py 集成

军事新闻源已集成到主聚合器中：
- RSS源通过通用的 `fetch_feed()` 方法处理
- 爬虫文章通过 `scrape_military_sources()` 获取
- 所有文章统一去重和过滤
- 按 tier 分组输出

## 📈 当前统计

- **RSS源**: 4个可用，3个需要检查
- **爬虫源**: 1个可用，4个暂不可用
- **总可用**: 5个军事新闻源
- **每次抓取**: 约180-200篇文章（RSS）+ 9篇（爬虫）

## 🔧 改进建议

### 短期改进：

1. **修复Defense News和Military Times的RSS**
   - 尝试完整的RSS feeds列表页面
   - 检查是否需要特定的User-Agent

2. **改进环球网爬虫**
   - 分析实际页面结构
   - 使用浏览器开发者工具查找正确的选择器

### 长期改进：

1. **添加Selenium支持**
   - 处理需要JavaScript渲染的页面
   - 绕过Cloudflare等反爬虫保护

2. **添加代理支持**
   - 处理403错误
   - 轮换IP避免封禁

3. **添加更多军事媒体**
   - Naval News
   - Air Force Magazine
   - Defense One
   - 解放军报

## 💡 最佳实践

1. **优先使用RSS源** - 数据质量更好，包含日期和摘要
2. **定期测试** - 网站结构可能变化，需要更新爬虫
3. **尊重robots.txt** - 检查网站爬取政策
4. **适当延迟** - 爬虫之间添加延迟，避免被封禁
5. **错误处理** - 单个源失败不应影响整体流程

## 🔗 相关文件

- 配置: `~/git/deep_analysis/config/feeds.yml`
- 主脚本: `~/git/deep_analysis/scripts/rss-aggregator.py`
- 军事爬虫: `~/git/deep_analysis/scripts/military_scraper.py`
- 测试脚本: `~/git/deep_analysis/scripts/test_military_feeds.py`
- 报告目录: `~/git/deep_analysis/report/`
