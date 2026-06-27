# sci-render-kit

**学术渲染工具包 — 配方驱动的多后端科学可视化**
*Academic Render Toolkit — Recipe-driven multi-backend scientific visualization*

---

## 🌟 核心差异 / Key Differences (vs `college-draw`)

| 维度 / Dimension | `college-draw` | `sci-render-kit` (本项目) |
| :--- | :--- | :--- |
| **驱动模式 / Driver** | Python 工厂类 / Factory class | **YAML 配方声明 / Declarative YAML recipes** |
| **渲染后端 / Backend** | 仅 / Only Matplotlib | **Python (Matplotlib) + R (ggplot2) + JS (Observable)** |
| **代码量 / Code Volume** | ~800 行 Python / lines of Python | **极简适配器 / Minimal adapters + YAML recipes** |
| **配置方式 / Config** | 硬编码期刊色板 / Hardcoded palettes | **声明式、可扩展的 profiles / Declarative, extensible profiles** |
| **质量门禁 / Quality Gate**| 运行时检查 / Runtime check | **配方静态验证 + 美学规范检查 / Static + Aesthetic validation before rendering** |
| **元数据 / Metadata** | 无 / None | **强制生成渲染溯源清单 / Mandatory reproducibility manifest** |
| **输出格式 / Output** | PDF/EPS/SVG | **PNG + SVG + HTML (交互式 / Interactive)** |

---

## 🚀 快速开始 / Quick Start

**sci-render-kit** 提供了一个统一的命令行入口，让你可以用同一套 YAML 配方，在不同的绘图语言间无缝切换。
*sci-render-kit provides a unified CLI, allowing you to seamlessly switch between plotting languages using the exact same YAML recipe.*

```bash
# 1. 编写一个配方 (Write a chart recipe)
# 查看 recipes/line-chart.yaml (See recipes/line-chart.yaml)

# 2. 渲染：使用 Python Matplotlib 后端，并应用 Nature 期刊规范
# Render using Python Matplotlib backend with Nature journal profile
python3 sci_render.py recipes/line-chart.yaml --profile nature --backend matplotlib

# 3. 切换渲染引擎：使用 R ggplot2 后端，应用 Science 期刊规范
# Switch engine: Render using R ggplot2 backend with Science journal profile
python3 sci_render.py recipes/line-chart.yaml --profile science --backend ggplot2

# 4. 生成交互式网页：使用 Observable Plot 后端
# Generate interactive web plots: Render using Observable Plot backend
python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend observable
```

---

## 🧠 核心概念 / Core Concepts

- **配方 (Recipe)**: 声明式图表定义（YAML）。只描述数据和图表结构，不写绘图代码。 / *Declarative chart definition (YAML). Describes data and structure without writing plotting code.*
- **统一调度器 (Unified CLI)**: `sci_render.py`。负责加载配方、读取规范、执行强校验，最后分发给底层引擎。 / *The main entry point that loads recipes, applies profiles, enforces validation, and dispatches to engines.*
- **后端 (Backend)**: 将配方转换为对应语言（Python/R/JS）代码的适配器。 / *Adapters that translate recipes into language-specific execution code (Python/R/JS).*
- **配置 (Profile)**: 针对特定学术期刊（如 Nature, Science）或场景（如 PPT 演示）的美学预设。 / *Aesthetic presets for specific academic journals (e.g., Nature, Science) or scenarios.*
- **质量门 (Quality Gate)**: 在渲染前强制执行的 Schema 校验与业务逻辑验证（如：色彩数量超标拦截）。 / *Pre-render validation checks ensuring schema compliance and aesthetic rules (e.g., color count limits).*
- **元数据 (Metadata)**: 每次渲染必然伴随生成的 `.manifest.json` 溯源文件，确保 100% 实验可复现。 / *A `.manifest.json` provenance file automatically generated with every render to guarantee 100% reproducibility.*

---

## 🏗️ 目录结构 / Directory Structure

```text
sci-render-kit/
├── sci_render.py          ← 统一命令行入口 (Unified CLI Entrypoint)
├── ARCHITECTURE.md        ← 详细系统架构设计 (Detailed Architecture Design)
├── MANIFEST.yaml          ← 工具包能力声明 (Toolkit capability manifest)
├── recipes/               ← 图表配方示例 (Chart recipes in YAML)
│   ├── line-chart.yaml
│   ├── bar-chart.yaml
│   ├── scatter-plot.yaml
│   ├── heatmap.yaml
│   ├── boxplot.yaml
│   └── histogram.yaml
├── backends/              ← 后端适配器 (Backend adapters / Code generators)
│   ├── matplotlib_adapter.py
│   ├── ggplot2_adapter.R
│   └── observable_adapter.js
├── profiles/              ← 期刊/场景配置预设 (Journal aesthetic profiles)
│   ├── nature.yaml
│   ├── science.yaml
│   ├── ieee.yaml
│   └── presentation.yaml
├── metadata/              ← 元数据规范 (Metadata validation schemas)
│   ├── recipe.schema.yaml
│   └── reproducibility.schema.yaml
├── quality/               ← 质量门定义 (Quality gate rule definitions)
│   └── gates.yaml
└── tests/                 ← 测试套件 (Test suite)
    └── test_all.py
```

---

## ⚖️ 协议 / License

MIT License

---

## 🛑 严格错误控制体系 (Strict Error Control System)
为了保证 100% 稳定的学术渲染流程，本工具禁止任何静默失败，定义了以下强制中断信号：
* `YAML_PARSE_FAILURE`: 当解析到损坏的 YAML 配方或配置时触发。
* `MISSING_PROFILE`: 强制声明特定的期刊配置，若未找到对应的 `.yaml` 文件则直接报错，拒绝执行。
* `P0_SCHEMA_FAILURE`: 当用户提供的配方字段类型或必需项校验失败时触发。
* `BACKEND_EXECUTION_FAILURE`: 底层渲染适配器发生异常或失败时触发。
* `MANIFEST_MISSING`: 溯源元数据文件未能成功生成时触发。
