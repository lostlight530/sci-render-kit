# sci-render-kit

**学术渲染工具包 — 配方驱动的多后端科学可视化**
*Academic Render Toolkit — Recipe-driven multi-backend scientific visualization*

---

## 核心差异 / Key Differences (vs `college-draw`)

| 维度 / Dimension | `college-draw` | `sci-render-kit` |
| :--- | :--- | :--- |
| **驱动模式 / Driver** | Python 工厂类 | **YAML 配方声明** |
| **渲染后端 / Backend** | 仅 Matplotlib | **Python + R + JS** |
| **代码量 / Code Volume** | ~800 行 Python | **极简适配器 + YAML** |
| **配置方式 / Config** | 硬编码期刊色板 | **声明式 profiles** |
| **质量门禁 / Quality Gate** | 运行时检查 | **配方静态验证** |
| **元数据 / Metadata** | 无 | **渲染溯源清单** |
| **输出格式 / Output** | PDF/EPS/SVG | **PNG + SVG + HTML** |

## 快速开始 / Quick Start

```bash
# 1. 编写配方 / Write a recipe
# See recipes/line-chart.yaml

# 2. 渲染 / Render
python3 sci_render.py recipes/line-chart.yaml --profile nature --backend matplotlib

# 3. 切换后端 / Switch backend
python3 sci_render.py recipes/line-chart.yaml --profile science --backend ggplot2

# 4. 交互式 / Interactive
python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend observable
```

## 核心概念 / Core Concepts

- **配方 (Recipe)**: 声明式图表定义（YAML）
- **统一调度器 (CLI)**: `sci_render.py` — 加载配方、应用 profile、执行校验、分发引擎
- **Profile**: 期刊规范声明（字体、色板、尺寸）

## 实现状态 / Implementation Status

| Module | Status |
|--------|--------|
| `sci_render.py` CLI | **Implemented** |
| Matplotlib backend | **Implemented** |
| R ggplot2 backend | **Implemented** |
| JS Observable backend | **Implemented** |
| Profile static validation | **Implemented** |
| `collapse_view.py` → `core/projection.py` | **Experimental** |
| `cognitive_color.py` → `core/color_encoding.py` | **Experimental** |
| `time_crystal.py` → `core/time_crystal.py` | **Experimental** |
| `uncertainty_legend.py` → `core/uncertainty_legend.py` | **Experimental** |
| `observer_dashboard.py` → `core/observer_dashboard.py` | **Experimental** |
| `quantum_layer.py` → `core/superposition.py` | **Experimental** |

## 配方示例 / Recipe Example

See `recipes/` directory for sample recipes.

## 文档 / Documentation

- [Architecture](ARCHITECTURE.md)
- [Profile Guide](profiles/README.md)

## 许可 / License

MIT License
