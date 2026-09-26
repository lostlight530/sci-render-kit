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
- [事实核验] Q3：Matplotlib 3.9 发布线（2024 下半年，UNKNOWN 精确日）；colormap/色觉无障碍（viridis 系之后 perceptually-uniform 线）持续；SVG 可访问性标准（W3C SVG a11y）无单点事件
- [决定] NO_FOLLOW_UP + UNKNOWN 1

### Stage D / 2024-Q4
- [事实核验] **Matplotlib 3.10.0 于 2024-12-13 前后发布**（G 阶段 3.10.5 的起点版本——时间轴锚点）；Q4 渲染侧的 environment 敏感性议题（headless 渲染/font 缓存）为"runtime identity"命题的前哨
- [决定] APPEND_RELATION：3.10.0 锚

### Stage E / 2025-Q1
- [事实核验] Q1：Plotly.py 5.x 末期与 6.0 预热（**6.0 实际 2025-03-06 发布——若 E 文件按 Q1 窗口记 6.0 即越界一个半月，VERIFY_IN_PLACE**）；Vega-Lite 5.x→6.0 预热；Matplotlib 3.10.x 补丁线
- [决定] VERIFY_IN_PLACE 一处 + NO_FOLLOW_UP

### Stage F / 2025-Q2
- [事实核验] **Plotly.py 6.0（2025-03-06，Q1 末/Q2 初边界）**——大版本（Plotly.js 3.0 底座）；**Matplotlib 3.10.5 于 2025-06 前后（G 阶段对象的先行补丁线）**；科学出版侧 figure 溯源议题（journal 的 reproducibility figure 要求）持续
- [决定] APPEND_RELATION：两锚（日期 UNKNOWN 项标注）

### Stage G / 2025-Q3
- [事实核验] **G 三对象与版本线精确对齐：Matplotlib 3.10.5（wheel/运行时平台目标变化）、Plotly.py 6.3（browser acquisition+Plotly.js 版本成为显式导出依赖）、Vega-Lite 6.3/6.4（interaction/tooltip 语义版本敏感）**——G 选题是本仓七阶段最准切片；"renderer update != scientific validity"边界句为仓哲学代表句
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
Pandoc 3.2/NumPy 2.0/Plotly 6.0/Vega-Lite 6.0 查询部分命中（噪音滤除后 3.2/2.0 确认）；Matplotlib 3.10.0/3.10.5、Plotly 6.3、Vega-Lite 6.3/6.4 精确日未验证——UNKNOWN 标注。2026-09-26。
---
*Annotation ends. 历史文件零改动。*
