# 架构设计与理念文档 / Architecture & Philosophy

---

## 1. 核心痛点与“遥遥领先”理念 (Core Pain Points & The "Ahead of the Curve" Philosophy)

### 🔴 传统学术绘图的痛点 (Pain Points of Traditional Academic Plotting)
- **难复现 (Hard to Reproduce)**：绘图代码充斥着硬编码，数据与样式深度耦合。几个月后，原作者往往都无法复现完全一致的图表。 / *Plotting scripts are often filled with hardcoded values, coupling data with styling. Months later, reproducing the exact same chart becomes nearly impossible.*
- **难修改 (Hard to Modify)**：当需要切换目标期刊（如从 IEEE 换投 Nature）时，研究者不得不逐行手动修改字体、颜色、线宽和 DPI 等绘图代码。 / *Switching target journals (e.g., from IEEE to Nature) requires manually editing fonts, colors, line widths, and DPI across hundreds of lines of code.*
- **易踩雷 (Prone to Errors)**：往往在投稿的最后一步，才发现色彩使用了红绿组合（对色盲不友好）、颜色数量过多或分辨率未达标。 / *Researchers often discover formatting issues (e.g., red-green color combinations, incorrect DPI) right before submission.*

### 🟢 “遥遥领先”的解决方案 (The "Ahead of the Curve" Solution)
**sci-render-kit** 提出了一套革命性的理念，彻底重塑学术图表的工作流：
**sci-render-kit** *introduces a revolutionary philosophy to reshape the academic plotting workflow:*

1. **声明优先 (Declaration First)**：画图不需要写代码，而是编写结构化的 YAML 配置（配方 Recipe）。“画什么”（数据）与“怎么画”（代码）彻底解耦。 / *No coding required. Users write structured YAML configurations (Recipes). "What to plot" is strictly decoupled from "how to plot it".*
2. **后端无关 (Backend Agnostic)**：同一套 YAML 配方，可以通过统一接口无缝下发给 Python (Matplotlib)、R (ggplot2) 或 JavaScript (Observable Plot) 进行渲染。 / *The exact same YAML recipe can be seamlessly dispatched to Python, R, or JavaScript for rendering.*
3. **质量前置 (Quality Ahead)**：引入 CI/CD 中的质量门 (Quality Gates) 概念。在调用任何绘图语言之前，系统通过 Schema 和规则库进行强制静态校验，提前拦截不合规的图表。 / *Adopts the "Quality Gates" concept from CI/CD. Schemas and rules are enforced before rendering even begins, blocking non-compliant charts early.*
4. **强制溯源 (Mandatory Metadata)**：生成图表的同时，强制生成 `manifest.json`。该文件包含了完整的生成环境、配方版本和生成时间指纹，保证 100% 实验可溯源。 / *Generating a chart mandatory generates a `manifest.json` file containing the environment, recipe version, and timestamp, ensuring 100% reproducibility.*

---

## 2. 系统架构 (System Architecture)

系统基于**适配器模式 (Adapter Pattern)** 设计，并通过统一的 CLI 调度器 (`sci_render.py`) 实现工作流控制。
*The system is designed based on the **Adapter Pattern** and controlled by a unified CLI dispatcher (`sci_render.py`).*

```text
                                [质量门 / Quality Gates]
                                          |
[YAML 配方 / Recipe] ---> (CLI 解析器 / sci_render.py) ---> [配置注入 / Profiles]
                                          |
              +---------------------------+---------------------------+
              |                           |                           |
              V                           V                           V
 [Python 适配器 / Matplotlib]     [R 适配器 / ggplot2]     [JS 适配器 / Observable]
              |                           |                           |
              V                           V                           V
      [Python 渲染脚本]               [R 渲染脚本]                [HTML/JS 脚本]
              |                           |                           |
              +---------------------------+---------------------------+
                                          |
                                          V
                              [最终输出图表 (PNG/SVG/HTML)]
                                          +
                              [溯源元数据 (manifest.json)]
```

### 2.1 统一入口 CLI (Unified CLI: `sci_render.py`)
整个系统的大脑。它负责：
*The brain of the system. It is responsible for:*
1. **读取配方和配置 (Read & Merge)**：解析目标 YAML，并注入对应的期刊 Profile 约束。
2. **严格验证 (Strict Validation)**：利用 `jsonschema` 对配方进行底层类型检查 (P0 Gate)，并执行 `quality/gates.yaml` 中定义的业务逻辑校验（如色彩数量拦截、字体大小拦截，P1 Gate）。
3. **任务分发 (Dispatching)**：调用相应的后端适配器，传递通过验证的干净数据载荷。

### 2.2 配方与配置 (Recipes & Profiles)
- **Recipe**：纯粹的业务载体。只包含业务数据（如坐标点）和基础美学声明（如 X 轴名称）。 / *Pure business payload. Contains only data and basic aesthetic intentions.*
- **Profile**：学术期刊的硬性约束。例如 `nature.yaml` 会强制覆盖字体族、最小字号和配色规范。这两者在运行时被 CLI 智能融合。 / *Hard constraints for academic journals. Merged dynamically at runtime.*

### 2.3 后端适配器 (Backend Adapters)
被定义为被动（Dumb）的代码生成器。它们不关心质量校验，只负责一件事：将 JSON/YAML 格式的数据对象，使用模板或 AST 转换为目标语言的真实绘图代码，并触发执行。
*Defined as "dumb" code generators. They don't care about validation; they strictly translate YAML data into target language plotting scripts and execute them.*

---

## 3. 标准工作流 (Standard Workflow)

1. **准备配方 (Prepare)**：作者只需编写 `recipes/my-experiment.yaml`。
2. **执行渲染 (Render)**：运行 `python3 sci_render.py recipes/my-experiment.yaml --profile nature --backend ggplot2`。
3. **门禁拦截 (Gate Check)**：如果配方中的配色方案使用了超过 8 种颜色，CLI 会直接拒绝渲染并抛出规则冲突异常。
4. **代码生成与执行 (Generate & Exec)**：校验通过后，自动在 `output/` 目录下生成 `_generated_render.R` 并由系统自动运行 `Rscript`。
5. **获取高品质产物 (Output)**：用户在 `output/` 目录下得到完全符合 Nature 规范的 `my-experiment.png` 以及用于证明可复现性的 `my-experiment.manifest.json`。
