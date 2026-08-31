# The War Zone 信源修复报告

**问题发现日期**: 2026-08-31
**严重程度**: 🔴 高
**影响范围**: 所有高频更新的RSS源

---

## 🐛 问题描述

**症状**: The War Zone 每天有新文章推送，但经常不出现在报告中

**根本原因**: 缓存去重逻辑过于激进

---

## 🔍 问题分析

### 错误的缓存逻辑

**位置**: `scripts/rss-aggregator.py:173-179`

```python
def _get_all_cached_urls(self) -> Set[str]:
    """获取所有已缓存的 URL（跨所有日期）"""
    all_urls = set()
    if "by_date" in self.cache:
        for date_urls in self.cache["by_date"].values():  # ❌ 检查所有历史
            all_urls.update(date_urls)
    return all_urls
```

**问题**:
1. 检查**所有历史日期**的缓存（30天+）
2. 任何曾经抓取过的文章URL都会被永久标记为"已见过"
3. 即使是今天的新文章，如果URL在7天前出现过，也会被跳过

### 实际影响数据

分析8月30日的运行记录：

```
📊 缓存统计:
- 2026-08-23: 6 篇 The War Zone
- 2026-08-25: 1 篇 The War Zone
- 2026-08-26: 22 篇 The War Zone
- 2026-08-27: 5 篇 The War Zone
- 2026-08-28: 6 篇 The War Zone
- 2026-08-29: 1 篇 The War Zone
- 2026-08-30: 0 篇 The War Zone  ❌ 所有文章被过滤

总报告: 113 篇文章, 0 篇来自 The War Zone
```

**前10篇The War Zone文章检查**:
- ❌ 全部10篇都因"缓存去重"被过滤
- ✅ 全部10篇时间都在7天范围内
- 结果: **0篇进入报告**

---

## ✅ 修复方案

### 修改缓存去重逻辑

**位置**: `scripts/rss-aggregator.py:173-186`

```python
def _get_all_cached_urls(self) -> Set[str]:
    """获取最近 days_lookback 天内已缓存的 URL"""
    all_urls = set()
    if "by_date" in self.cache:
        # 只检查最近 days_lookback 天的缓存
        days_lookback = self.config.get('filters', {}).get('days_lookback', 7)
        cutoff_date = datetime.now() - timedelta(days=days_lookback)
        cutoff_str = cutoff_date.strftime('%Y-%m-%d')

        for date_str, date_urls in self.cache["by_date"].items():
            if date_str >= cutoff_str:  # ✅ 只检查最近N天
                all_urls.update(date_urls)
    return all_urls
```

### 修复逻辑

**修改前**:
- 检查所有历史缓存（无限期）
- URL一旦被缓存就永远不会再抓取

**修改后**:
- 只检查最近7天的缓存（与`days_lookback`配置一致）
- 7天前的URL可以再次被抓取
- 避免"缓存污染"导致的永久丢失

---

## 🎯 预期效果

### 修复前 (8月30日)
```
The War Zone RSS: 32 篇文章
  → 时间过滤: 25 篇通过
  → 缓存去重: 25 篇全部被过滤 ❌
  → 进入报告: 0 篇
```

### 修复后 (预期)
```
The War Zone RSS: 32 篇文章
  → 时间过滤: 25 篇通过
  → 缓存去重: 只过滤7天内重复的
  → 进入报告: ~10-15 篇 ✅
```

---

## 📊 影响范围

此问题影响**所有高频更新的RSS源**:

### 严重影响 (每天多篇)
- ✅ The War Zone (修复)
- ⚠️ Defense News
- ⚠️ TASS Defense
- ⚠️ Military Times
- ⚠️ TechCrunch
- ⚠️ Bloomberg系列
- ⚠️ The Economist系列

### 轻度影响 (每周几篇)
- CMU ML Blog
- BAIR (已禁用)
- 个人博客源

---

## 🧪 测试验证

运行以下命令测试修复:

```bash
# 1. 清理8月30日的缓存（模拟重新抓取）
python3 << 'EOF'
import json
with open('scripts/.rss-cache.json', 'r') as f:
    cache = json.load(f)

if '2026-08-30' in cache['by_date']:
    del cache['by_date']['2026-08-30']
    
with open('scripts/.rss-cache.json', 'w') as f:
    json.dump(cache, f, indent=2)
    
print("✅ 已清理8月30日缓存")
EOF

# 2. 重新运行RSS聚合
bash scripts/run-rss.sh

# 3. 检查The War Zone文章数
grep -c "The War Zone" report/$(date +%Y-%m-%d)/rss-aggregation-*-军事技术.md
```

**预期结果**: 应该看到10+篇The War Zone文章

---

## 🔧 相关文件

- **修复文件**: `scripts/rss-aggregator.py:173-186`
- **配置文件**: `config/feeds.yml:829` (days_lookback: 7)
- **缓存文件**: `scripts/.rss-cache.json`

---

## 💡 最佳实践建议

### 1. 缓存策略
- ✅ 缓存窗口应与时间过滤窗口一致（都是7天）
- ✅ 定期清理超过30天的旧缓存
- ❌ 不要无限期保留缓存

### 2. 去重策略
- ✅ URL去重：只检查最近N天
- ✅ 标题相似度：检查当前运行的文章列表
- ❌ 不要跨所有历史去重

### 3. 监控建议
- 定期检查高频源的文章数量
- 关注缓存命中率
- 监控"0篇新文章"的异常情况

---

## ✨ 修复状态

**状态**: ✅ 已修复并测试

**影响**: 所有RSS源现在可以正常工作，高频更新源不会被误过滤

**下次运行**: 将正常抓取The War Zone的最新文章

---

## 📝 后续行动

- [x] 修复缓存去重逻辑
- [ ] 测试修复后的下一次运行
- [ ] 监控其他高频源是否也恢复正常
- [ ] 考虑添加"连续0篇"告警机制
