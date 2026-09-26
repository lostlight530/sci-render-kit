# Frontier Research Annotations — Stage A-G 合并批注 (sci-render-kit)

**Reviewer:** 淇（Qi）· 2026-09-26 · Independence: 独立（SPEC §12 声明式） · Rewrite: NONE

## 0. 仓定位批注

sci-render 仓的轴=**科学图表的通信身份**：一张图被正确解读需要记录什么（编码/无障碍/运行时/交互语义）。与 auto-doc 轴的交叉点=derivation target（同一手稿多格式渲染）——A2/sci-A 是天然三角对。

## 1. 逐 Stage 批注

### Stage A / 2024-Q1
- [事实核验] Q1 渲染生态：Matplotlib 3.8.x 线稳定（3.8.0 于 2023-09，Q1 处补丁期）；**Altair 5.x/Vega-Lite 5.x 主线**；无障碍侧：图表 alt-text 自动化研究活跃（plot2csv 类反推工具）
- [决定] NO_FOLLOW_UP + 锚 1

### Stage B / 2024-Q2
- [事实核验] Q2：Pandoc 3.2（05-17）的 figure 处理改进与 Quarto 1.5 的 figure-crossref——**文档侧渲染事件的直接对象域命中**；NumPy 2.0（06-16）对渲染栈的 ABI 冲击（matplotlib 兼容矩阵）——"version-dependent"命题的现实压力事件
- [决定] APPEND_RELATION：双锚

### Stage C / 2024-Q3
- [事实核验] Q3：Matplotlib 3.9.0 基线实际在 2024-05-15（Q2）；Q3 对应的是 3.9.1（07-04）与 3.9.2（08-12）补丁线。colormap/色觉无障碍议题持续；SVG 可访问性标准无单一 Q3 发布事件
- [决定] NO_FOLLOW_UP + UNKNOWN 1

### Stage D / 2024-Q4
- [事实核验] **Matplotlib 3.10.0 于 2024-12-14 发布**（后续 3.10.x 补丁线的起点版本——时间轴锚点）；Q4 渲染侧的 environment 敏感性议题（headless 渲染/font 缓存）为"runtime identity"命题的前哨
- [决定] APPEND_RELATION：3.10.0 锚

### Stage E / 2025-Q1
- [事实核验] Q1：Plotly.py 6.0.0 官方 changelog 日期为 **2025-01-28**，明确属于 Q1；因此“若 E 文件按 Q1 记录 6.0 则越界”的原判断撤销。Vega-Lite 5.x→6.0 线与 Matplotlib 3.10.x 补丁线仍作为同期背景
- [决定] Plotly.py 6.0 时间边界已校正；其余对象按现有证据继续 NO_FOLLOW_UP / VERIFY_IN_PLACE

### Stage F / 2025-Q2
- [事实核验] Plotly.py 6.0.0 实际为 **2025-01-28（Q1）**，因此不再作为 Q2 边界事件；Matplotlib 3.10.5 实际为 **2025-07-31（Q3）**，也不属于 Stage F。Stage F 的叙事应避免用这两个版本节点支撑 Q2 时间线；科学出版侧 figure 溯源与 reproducibility 要求可继续作为背景议题
- [决定] 删除 Plotly 6.0 / Matplotlib 3.10.5 作为 Q2 时间锚的建议；Stage F 若扩展应重新选择 Q2 内真实版本节点

### Stage G / 2025-Q3
- [事实核验] **G 的 Matplotlib 3.10.5（2025-07-31）与 Plotly.py 6.3.0（2025-08-12）均落在 Q3**；Vega-Lite 6.3/6.4 的精确发布日期仍需单独核验。G 的对象选择与 runtime/browser/interaction version-sensitivity 主题保持一致；"renderer update != scientific validity"边界句成立
- [决定] CONFIRMED（对象-版本对齐成立）

## 2. 治理件横切批注

- BRIEF RQ：仅 A 显式——同系治理注记
- REVIEW 独立性：七 Stage 未声明——GAP 汇总（本文件补位）
- REGISTER：A→G 衰减同型（F/G 最薄）——E/F correction 优先
- 厚度曲线同型——系统性衰减三仓确认

## 3. 跨仓三角

- 三轴平行链提案：渲染轴=encoding→accessibility→version-sensitivity→backend→browser→interaction（同 auto-doc 批注的纵向 correction 提案）
- MCP 事件：本仓无涉（NO_RELATION 声明）

## 4. Search log
本轮补核：Matplotlib 3.9.0=2024-05-15、3.9.1=2024-07-04、3.9.2=2024-08-12；Matplotlib 3.10.0=2024-12-14、3.10.5=2025-07-31；Plotly.py 6.0.0=2025-01-28、6.3.0=2025-08-12。Vega-Lite 6.3/6.4 精确日仍未在本批注中建立，继续 UNKNOWN / VERIFY_IN_PLACE。2026-09-26。
---
*Annotation ends. 历史文件零改动。*
