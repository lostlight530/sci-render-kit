# sci-render-kit

> 学术渲染工具包 — 配方驱动的多后端科学可视化 | Recipe-driven multi-backend scientific visualization

## 核心差异 / Key Differences（vs `college-draw`）

| 维度 / Dimension | college-draw | sci-render-kit |
|------|--------------|----------------|
| 驱动模式 / Driver | Python 工厂类 / Factory class | YAML 配方声明 / Declarative recipes |
| 渲染后端 / Backend | 仅 Matplotlib | Python + R + Observable Plot |
| 代码量 / Code | ~800 行 Python | ~200 行适配器 + YAML 配方 |
| 配置方式 / Config | 硬编码期刊/色板 / Hardcoded | 声明式 profiles + 可扩展 / Declarative, extensible |
| 质量门 / QA Gate | 运行时检查 / Runtime check | 配方静态验证 + 运行时检查 / Static + runtime |
| 元数据 / Metadata | 无 / None | 强制渲染溯源 / Mandatory reproducibility manifest |
| 输出格式 / Output | PDF/EPS/SVG | PNG + SVG + HTML（交互式 / interactive） |

## 快速开始 / Quick Start

```bash
# 1. 写一个配方 / Write a recipe
# recipes/line-chart.yaml

# 2. 渲染 / Render
python backends/matplotlib_adapter.py render recipes/line-chart.yaml
# 或 / or
Rscript backends/ggplot2_adapter.R render recipes/line-chart.yaml
```

## 核心概念 / Core Concepts

```
配方 / Recipe       → 声明式图表定义（YAML）/ Declarative chart definition
后端 / Backend      → 配方 → 代码转换器（适配器模式）/ Adapter pattern converter
配置 / Profile      → 期刊/场景美学预设 / Journal/scene aesthetic presets
元数据 / Metadata   → 每次渲染自动记录的完整溯源 / Full render provenance
质量门 / Gate       → 配方静态验证 + 渲染后检查 / Pre-validation + post-render check
```

## 设计理念 / Design Philosophy

1. **声明优先 / Declaration First**：图表定义用 YAML，不用写代码 / Define charts in YAML, not code
2. **后端无关 / Backend Agnostic**：同一配方在 matplotlib/ggplot2/Observable 间切换 / Same recipe, any backend
3. **元数据强制 / Mandatory Metadata**：每次渲染必须输出 reproducibility manifest / Every render carries provenance
4. **质量前置 / Quality Ahead**：配方在渲染前通过静态验证 / Validate before rendering

## 目录结构 / Directory Structure

```
sci-render-kit/
├── README.md
├── MANIFEST.yaml          ← 能力声明 / Capability manifest
├── recipes/               ← 图表配方 / Chart recipes (YAML)
│   ├── line-chart.yaml
│   ├── bar-chart.yaml
│   ├── scatter-plot.yaml
│   └── heatmap.yaml
├── backends/              ← 后端适配器 / Backend adapters
│   ├── matplotlib_adapter.py
│   ├── ggplot2_adapter.R
│   └── observable_adapter.js
├── profiles/              ← 期刊/场景配置 / Journal profiles
│   ├── nature.yaml
│   ├── science.yaml
│   ├── ieee.yaml
│   └── presentation.yaml
├── metadata/              ← 元数据规范 / Metadata schemas
│   ├── recipe.schema.yaml
│   └── reproducibility.schema.yaml
├── quality/               ← 质量门定义 / Quality gate definitions
│   └── gates.yaml
└── tests/                 ← 测试 / Tests
    └── test_all.py
```

## 协议 / License

MIT
