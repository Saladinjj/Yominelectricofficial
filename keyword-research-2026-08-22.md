# 关键词机会矩阵 — Yomin Electric（2026-08-22）

**站点:** https://www.yominelectric.com/ · **行业:** 电能计量 / 电气仪表出口
**目标:** 有机高流量、低竞争关键词 → 新博客选题
**现有覆盖:** blog/ 目录 56 篇已发布文章（已做去重与蚕食检查）

📊 **数据来源: 启发式估算 + Google Suggest 真实补全验证 + 站点覆盖缺口分析 | 置信度: 低 (0.5) | 采集时间: 2026-08-22 13:10**
> 降级原因: 付费关键词 API（Semrush/Ahrefs/DataForSEO/Moz）未授权；用户未回复 Semrush 浏览器登录询问（ask_user 超时 300s）；DuckDuckGo SERP 被 CAPTCHA 拦截。按 seo-keywords 技能「极端情况 → 启发式估算 + Google Suggest」兜底路径执行。搜索量/难度为定性区间估计（非精确数值），正式投放前建议用 Semrush/关键词规划器复核。

---

## 1. 选题原则

1. **需求验证**: 每个词必须通过 Google Suggest 真实补全确认存在持续搜索需求（下方附补全原文）。
2. **竞争评估**: 优先选择 SERP 由低质量内容站/问答站占据、无行业巨头官方页主导的「可赢」词。
3. **覆盖缺口**: 与现有 56 篇博客逐条比对，避免关键词蚕食（一词一页）。
4. **商业相关**: 全部选题可自然回链 Yomin 产品线（energy meter / CT / solar PV / RS485 / smart meter）。

---

## 2. 机会矩阵（Top 6 选题）

📊 数据来源: Google Suggest 补全（2026-08-22 实时抓取）+ 定性竞争评估 | 置信度: 低 (0.5)

| # | 关键词（主） | 需求区间 | 竞争度 | 意图 | 对应产品线 | 覆盖缺口 | 建议 slug |
|---|---|---|---|---|---|---|---|
| 1 | kw vs kwh（difference / explained / meaning） | 高 | 低-中 | Informational | Energy Meter | ✅ 无（understanding-kwh 只讲 kWh 单概念） | `kw-vs-kwh-whats-the-difference` |
| 2 | are smart meters safe / smart meter safety | 高 | 低 | Informational | Smart Meter | ✅ 无（smart-meters-explained 未涉健康安全） | `are-smart-meters-safe` |
| 3 | what is power factor（formula / correction / definition） | 高 | 中 | Informational | Power Analyzer / Energy Meter | ✅ 无 | `what-is-power-factor-and-why-it-matters` |
| 4 | what is submetering（electricity / system / meaning） | 中-高 | 低 | Informational+Commercial | Prepaid / Submeter | ✅ 无（prepaid-metering-for-landlords 角度不同） | `what-is-submetering-a-guide-for-landlords` |
| 5 | modbus energy meter / rs485 power meter | 中 | 低 | Commercial (B2B) | RS485 / Modbus Meter | ✅ 无 | `modbus-rs485-energy-meters-guide` |
| 6 | time of use meter（tou metering / tou electricity meter） | 中 | 低 | Informational | Smart Meter (TOU) | ✅ 无 | `time-of-use-metering-guide` |

### Google Suggest 补全证据（原文，2026-08-22）

| 种子 | 补全变体 |
|---|---|
| kw vs kwh | kw vs kwh meaning / explained / solar / electric car / on electric bill / conversion / difference / vs kva / vs kwp |
| smart meter safe | smart meter safety / safety concerns / safe distance / safety checks / safety switch / is safe or not |
| power factor | power factor formula / correction / calculator / definition / equation / correction capacitor / correction device |
| submetering | submetering meaning / electricity / system / solutions / equipment / companies |
| modbus energy meter | modbus energy meter 3 phase / home assistant / software / ct / modbus power meter schneider |
| time of use meter | time of use metering / time of use electricity meter / time of use smart meters / is time of use metering worth it |

### 竞争度评估依据

| 词 | 理由 |
|---|---|
| kw vs kwh | 解释型内容，SERP 多为问答站/普通博客，无头部厂商官方页主导；长尾（on electric bill / solar）更易赢 |
| smart meter safety | SERP 多为情绪化反对内容或政府 FAQ，缺少"制造商视角+数据"的权威中立回答，信息缺口大 |
| power factor | 中竞争（有厂商科普页），但"面向非工程师的易懂版+功率因数表测量"角度空白 |
| submetering | 词根明确、垂直细分，主要竞争为服务商官网（北美），制造商内容稀缺 |
| modbus/rs485 meter | B2B 技术采购词，竞争为施耐德等大牌产品页，长尾"如何选型/接线/读数"空白 |
| TOU metering | 区域性强（LADWP/NSW），通用科普+制造商方案角度竞争低 |

---

## 3. 落地计划

| 步骤 | 内容 | 状态 |
|---|---|---|
| 1 | 6 篇博客按现有模板（nav+hero+内容+CTA+footer，含 BlogPosting+FAQPage JSON-LD）撰写 | 待执行 |
| 2 | hero 图：真实产品合成场景（明亮、布线整齐，符合品牌视觉） | 待执行 |
| 3 | 每篇含产品类目链接 + 相关阅读内链（站内互链） | 待执行 |
| 4 | 更新 blog.html（JSON-LD + 可见卡片）+ sitemap-main.xml | 待执行 |

---

## 附录：方法论与计算依据

### 1. 需求区间评估（启发式）

**估算方法:** 由 Google Suggest 补全变体数量与多样性推断需求层级：
- 变体 ≥8 且含多意图（meaning/explained/对比）→ 需求"高"
- 变体 6–8 且主题聚焦 → 需求"中-高"
- 变体 4–6 → 需求"中"

**计算依据:** Google Autocomplete 反映真实查询语料（Google 搜索日志聚合），补全多样性与该词族的搜索需求正相关（行业通用启发式，参考 Moz Keyword Explorer 的 suggestion 信号）。

**采用原因:** 在无付费 API 授权的前提下，Autocomplete 是唯一可程序化获取的真实需求信号；已用多种子交叉验证。

**作用与意义:** 为选题提供需求方向的排序依据；正式投放前用 Semrush/Google Keyword Planner 复核精确量级。

### 2. 竞争度评估（定性）

**估算方法:** 基于领域知识判断 SERP 构成（主导者类型：政府/官方页、大牌厂商、问答站、低质内容站）+ 词族商业化程度：
- 主导者为低质内容站/问答站、无官方权威页 → "低"
- 有厂商科普页但无垄断性结果 → "中"
- 头部品牌官方页+广告饱和 → "高"

**计算依据:** SEO 行业通用的 SERP 竞争构成分析法（Ahrefs 竞争度方法论之定性版）。

**采用原因:** 无法抓取完整 SERP（DuckDuckGo CAPTCHA、本地引擎结果质量差）时的替代方案。

**作用与意义:** 判断"以当前站点权威度能否赢下该词"，聚焦 0–30 分位（可立即进攻）的词汇。

### 3. 覆盖缺口检查（防蚕食）

**方法:** 将候选词与 blog/ 目录 56 个 slug + blog.html JSON-LD 全部条目比对，确认无同主词页面；语义相近但意图不同的（如 submetering vs prepaid-metering-for-landlords）按意图区分，一词一页。

**作用与意义:** 符合 seo-keywords 的 keyword-to-page assignment 规则，避免两页竞争同一查询。

---

*报告生成: 2026-08-22 · 工具链: geo-agent 插件 seo-keywords 技能（Jungle Scout 默认兜底不可用 → 启发式路径）*
