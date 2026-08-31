# 光计算信源配置总结

本文档记录了添加到RSS聚合系统中的光计算（Optical/Photonic Computing）相关信源。

## 📅 更新日期
2026-08-31

## ✅ 已添加的信源

### 1️⃣ arXiv学术源（Tier 1 - 高权重）

#### arXiv physics.optics (光学/光计算)
- **URL**: https://export.arxiv.org/rss/physics.optics
- **类型**: arxiv
- **优先级**: high
- **关键词**:
  - optical computing
  - photonic computing
  - optical neural network
  - photonic chip
  - silicon photonics
  - optical interconnect
  - neuromorphic photonics
  - all-optical

#### arXiv cs.ET (新兴技术)
- **URL**: https://export.arxiv.org/rss/cs.ET
- **类型**: arxiv
- **优先级**: high
- **关键词**:
  - optical computing
  - photonic computing
  - quantum computing
  - neuromorphic
  - emerging technology

---

### 2️⃣ 国际光计算公司（通过网页爬取）

#### Lightmatter
- **URL**: https://lightmatter.co/news
- **描述**: 光子AI芯片公司，已获多轮融资
- **关注点**: 光子互连、光子AI加速器

#### Luminous Computing
- **URL**: https://www.luminous.co/news
- **描述**: 光子超级计算机公司
- **关注点**: 大规模光子计算系统

#### Lightintelligence
- **URL**: https://www.lightintelligence.ai/news
- **描述**: 光子AI加速器公司
- **关注点**: 光学神经网络加速

---

### 3️⃣ 中国光计算公司（通过网页爬取）

#### 曦智科技 (Xizhi Tech)
- **URL**: http://www.xizhi-tech.com/news
- **描述**: 国内光芯片先驱企业
- **关注点**: 光子AI芯片、国产光计算

#### 鲲游光电 (Kunyu Photonics)
- **URL**: https://www.kunyutech.com/
- **描述**: 硅光芯片公司
- **关注点**: 硅光技术、光电集成

#### 量子位 - 光计算专题
- **描述**: 中文科技媒体对光计算的报道
- **关注点**: 国内光计算产业动态、研究进展

---

### 4️⃣ 学术期刊和学会（Tier 2 - 中权重）

#### Nature Photonics
- **URL**: https://www.nature.com/nphoton.rss
- **类型**: journal
- **优先级**: high
- **关键词**:
  - optical computing
  - photonic computing
  - silicon photonics
  - optical neural network
  - photonic chip
  - optical interconnect

#### OSA Optica (Optical Society)
- **URL**: https://opg.optica.org/rss/optica.xml
- **类型**: journal
- **优先级**: high
- **关键词**:
  - optical computing
  - photonics
  - optical processing
  - integrated photonics

#### IEEE Photonics Society News
- **URL**: https://www.photonicssociety.org/news-center.rss
- **类型**: news
- **优先级**: medium
- **关键词**:
  - photonics
  - optical computing
  - silicon photonics
  - optoelectronics

---

## 📊 信源统计

- **arXiv学术源**: 2个
- **国际公司**: 3家
- **中国公司**: 3家
- **学术期刊/学会**: 3个
- **总计**: 11个信源

---

## 🏷️ 新增分类

在 `config/categories.yml` 中添加了新的分类：

```yaml
- key: optical_computing
  name: 光计算
  description: 关于光子计算、光芯片、硅光技术、光神经网络、光互连、光学处理器
```

---

## 🔍 关注的技术主题

1. **光子芯片** (Photonic Chip)
2. **硅光技术** (Silicon Photonics)
3. **光神经网络** (Optical Neural Network)
4. **光互连** (Optical Interconnect)
5. **光学处理器** (Optical Processor)
6. **神经形态光子学** (Neuromorphic Photonics)
7. **全光计算** (All-Optical Computing)
8. **光电集成** (Optoelectronic Integration)

---

## 📝 使用说明

1. **RSS源**会自动通过 `scripts/rss-aggregator.py` 抓取
2. **网页爬取源**需要在爬虫脚本中实现（目前标记为待实现）
3. 所有光计算相关文章会被自动分类到 `optical_computing` 类别
4. 运行方式：`bash scripts/run-rss.sh`

---

## 🚀 下一步计划

- [ ] 在 `scripts/web_scraper.py` 中添加光计算公司的爬虫逻辑
- [ ] 验证所有RSS源的可用性
- [ ] 测试文章分类准确性
- [ ] 考虑添加更多中国光计算研究机构（如中科院光电所）
