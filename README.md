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

# 2. 渲染 / Render (matplotlib 后端)
python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend matplotlib

# 3. 语义色彩编码 / Semantic color encoding
python3 sci_render.py recipes/semantic-line-chart.yaml --profile presentation --backend matplotlib

# 4. 交互式 / Interactive (需先 npm install，且本机有 node)
python3 sci_render.py recipes/line-chart-interactive.yaml --profile presentation --backend observable
```

门禁演示 / Gate demo（预期被拦截，展示质量门在工作）：

```bash
# Nature/Science profile 在 P3 门禁强制矢量输出；PNG 配方会被拒绝（exit 1）
python3 sci_render.py recipes/line-chart.yaml --profile nature --backend matplotlib
# → [期刊规范对齐] 矢量格式: nature 期望矢量格式 (.pdf/.eps)，但得到 .png
```

后端依赖说明 / Backend requirements：

- **matplotlib**：`pip install pyyaml jsonschema matplotlib numpy`
- **ggplot2**（可选）：本机 R + `yaml`/`jsonlite`/`digest`/`ggplot2` 包；该路径未在本仓库自动化测试中做运行时验证
- **observable**：本机 node + `npm install`（声明于 `package.json`，仅 `yaml` 一个依赖）；输出能力为 HTML

## 核心概念 / Core Concepts

- **配方 (Recipe)**: 声明式图表定义（YAML）
- **统一调度器 (CLI)**: `sci_render.py` — 加载配方、应用 profile、执行校验、分发引擎
- **Profile**: 期刊规范声明（字体、色板、尺寸）
- **语义色彩编码 (Semantic Color Encoding)**: 配方声明 `semantic_palette: true` 后，系列名命中语义标签（`positive`/`negative`/`stable` 等）即由 `core/color_encoding.py` 自动分配语义色（三后端一致）；声明 `background` 或启用语义色板时，P1 质量门 `palette-contrast` 强制校验色板与背景的 WCAG 对比度 ≥ 3.0。示例：`recipes/semantic-line-chart.yaml`

## 实现状态 / Implementation Status

| Module | Status |
|--------|--------|
| `sci_render.py` CLI | **Implemented** |
| Matplotlib backend | **Implemented** |
| R ggplot2 backend | **Implemented** |
| JS Observable backend | **Implemented** |
| Profile static validation | **Implemented** |
| `core/color_encoding.py` 语义色彩编码（semantic_palette + `palette-contrast` 质量门，三后端） | **Implemented** |
| `collapse_view.py` → `core/projection.py` | **Experimental** |
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
