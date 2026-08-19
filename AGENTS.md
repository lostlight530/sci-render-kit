# Agent 快速上手指引 / Agent Guide

面向被指派来扩展、修改或定制 `sci-render-kit` 的 Agent/Bot。读完本文即可正确动手。本文只写**操作约定与边界**；设计原理见 `ARCHITECTURE.md`，人类贡献者流程见 `CONTRIBUTING.md`。

## 0. 铁律（先读这个）

1. **声明优先**：用户写 YAML 配方（`recipes/*.yaml`），不写绘图代码。
2. **唯一入口**：一切渲染必须走 `python3 sci_render.py`。**直接调用后端适配器已废弃**——会绕过全部质量门。
3. **校验集中在 CLI**：适配器是 dumb 的代码生成器，不做校验；所有校验在 `sci_render.py`。
4. **每次渲染必须产出** `manifest.json`；matplotlib 后端另产出 `.prov.json` 溯源旁车（P2 门禁强制）。
5. **收尾前必须** `python3 tests/test_all.py` 全绿（当前 26/26；依赖 node/R 的用例在缺环境时自动 SKIP，不算失败）。

## 1. 目录导览

```
sci_render.py            统一 CLI：读配方 → 校验 → 分发 → 渲染后检查
core/
  color_encoding.py      [已实现] 语义色彩编码 + WCAG 对比度计算
  palettes.py            [已实现] 命名色板注册表（okabe-ito/petroff10/viridis/cividis/Crameri 系）
  cvd_simulation.py      [已实现] 色盲模拟（供 P1 cvd-contrast 门禁使用）
  projection.py / time_crystal.py / superposition.py /
  uncertainty_legend.py / observer_dashboard.py   [EXPERIMENTAL] 未接入主流程，勿当已实现引用
backends/
  matplotlib_adapter.py  Python 后端（png/svg/pdf；含溯源内嵌 + .prov.json）
  ggplot2_adapter.R      R 后端（png/svg/pdf）
  observable_adapter.js  JS 后端（仅 html）
profiles/                期刊配置：nature / science / cell / ieee / presentation
quality/gates.yaml       质量门规则声明（P0–P3）
metadata/                recipe.schema.yaml（配方 Schema）、reproducibility.schema.yaml（manifest Schema）
recipes/                 示例配方（每种图表类型至少一个）
tests/test_all.py        全量测试套件
examples/README.md       示例命令集
```

## 2. 怎么渲染

```bash
# 环境：pip install pyyaml jsonschema matplotlib numpy
# （observable 后端另需 node + npm install；ggplot2 后端另需本机 R 及 yaml/jsonlite/digest/ggplot2 包）

python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend matplotlib
python3 sci_render.py recipes/semantic-line-chart.yaml --profile presentation --backend matplotlib   # 语义色板演示
python3 sci_render.py recipes/line-chart-interactive.yaml --profile presentation --backend observable # 交互式 HTML
```

- CLI 参数：`sci_render.py <recipe.yaml> [--profile nature|science|cell|ieee|presentation] [--backend matplotlib|ggplot2|observable]`（默认 `--profile nature --backend matplotlib`）。
- 产物在配方 `output.dir` 声明的目录下：图件 + 同名 `.manifest.json`；matplotlib 后端另有同名 `.prov.json`（溯源旁车：配方/输入数据/输出文件 SHA-256、后端版本、时间戳）。
- 后端能力边界（dispatch 前强制校验，声明于 `sci_render.py.BACKEND_CAPABILITIES`，与 `MANIFEST.yaml` 一致）：matplotlib/ggplot2 → `png/svg/pdf`，observable → `html` 仅。越界即 `BACKEND_CAPABILITY_MISMATCH`，exit 1。
- **边界**：ggplot2 (R) 路径未在本仓库自动化测试中做运行时验证；observable E2E 依赖 node 环境，缺失时测试自动 SKIP。宣称能力时不得超出上述边界。

## 3. 配方字段速查

Schema 以 `metadata/recipe.schema.yaml` 为准。必需顶层字段：`id, type, data, aesthetics, output`。

- `type`：`line-chart | bar-chart | scatter-plot | heatmap | boxplot | histogram`（`3d-*` 被 P1 禁止）。
- `aesthetics`（均可被 profile 默认值合并，配方优先）：
  - 基础：`title, x_label, y_label, palette(hex 数组, ≤8), font_size(≥5), figsize([w,h] 英寸), dpi(≥72), line_width, cmap(热力图色阶), bins(直方图)`
  - 色彩增强（触发对应 P1 门禁，未声明则不启用，向后兼容）：
    - `semantic_palette: true` — 系列名命中语义标签（positive/negative/stable 等）时自动分配语义色；仅系列图（line/bar/scatter/boxplot/histogram）生效
    - `background` — 画布背景色 hex；声明后启用 palette-contrast 与 cvd-contrast 门禁
    - `text_color` — 文字颜色 hex；声明后启用 text-contrast 门禁
    - `adjacency_check: true` — 启用分类色板两两对比度门禁
    - `palette_name` — 引用 `core/palettes.py` 注册色板（如 `okabe-ito`、`petroff10`）；系列图仅接受 categorical 色板，顺序/发散色阶请用 `cmap`
- `output`：`dir, filename` 必需；`format: png|svg|pdf|eps|html`（默认 png）。注意 `nature/science/cell` profile 在 P3 强制 pdf/eps。

## 4. 质量门体系（P0–P3）

规则声明在 `quality/gates.yaml`，执行在 `sci_render.py`。任一失败 → 打印规则冲突并 exit 1。

| 级别 | 时机 | 检查 id | 触发条件与规则 |
|---|---|---|---|
| P0 | 渲染前 | schema-compliance / required-fields / data-type / output-config | 配方符合 `recipe.schema.yaml`；含 `id,type,data,aesthetics,output`；output 含 `dir,filename` |
| P1 | 渲染前 | color-count | 有效色板颜色数 ≤ 8 |
| P1 | 渲染前 | font-size | nature ≥ 5pt；science ≥ 6pt |
| P1 | 渲染前 | forbidden-pairs | 显式 palette 不得红绿（#ff0000/#00ff00）并置 |
| P1 | 渲染前 | palette-contrast | 声明 `background` 或启用 `semantic_palette` 时：各色板色 vs 背景 WCAG 对比度 ≥ 3.0（未声明 background 按 #FFFFFF） |
| P1 | 渲染前 | text-contrast | 声明 `text_color` 时：文字 vs 背景 ≥ 4.5（WCAG SC 1.4.3） |
| P1 | 渲染前 | palette-adjacency | 声明 `adjacency_check: true` 时：分类色板两两 ≥ 3.0（SC 1.4.11），报告失败色对 |
| P1 | 渲染前 | cvd-contrast | 同 palette-contrast 触发条件：三种色盲模拟（protanopia/deuteranopia/tritanopia）下各色 vs 背景保持 ≥ 3.0 |
| P1 | 渲染前 | palette-name | 声明 `palette_name` 时必须命中 `core/palettes.py` 注册表；系列图仅接受 categorical |
| P1 | 渲染前 | no-3d | `type` 不得以 `3d-` 开头 |
| — | 分发前 | backend capability | `output.format` 必须在所选后端能力集内（见 §2），否则 `BACKEND_CAPABILITY_MISMATCH` |
| P2 | 渲染后 | file-exists / non-empty / format-match | 输出文件存在、非空、扩展名与 `output.format` 一致 |
| P2 | 渲染后 | manifest-exists | 同名 `.manifest.json` 必须存在 |
| P2 | 渲染后 | prov-exists | matplotlib 后端必须产出同名 `.prov.json`（R/JS 侧为可选跟进，不强制） |
| P3 | 渲染后 | vector-format | profile 为 nature/science/cell 时输出须为 .pdf/.eps |
| P3 | 渲染后 | dpi-check | 合并后 dpi 不得低于 profile 声明的 `aesthetics.dpi` |
| P3 | 渲染后 | size-check | figsize 为正值二元组；不得超过 profile 的 `max_width_in`/`max_height_in` |

失败标志（stdout 可 grep）：`P0_SCHEMA_FAILURE`、`YAML_PARSE_FAILURE`、`MISSING_PROFILE`、`BACKEND_CAPABILITY_MISMATCH`、`MANIFEST_MISSING`。

## 5. 怎么扩展

### A. 新增图表类型
1. `metadata/recipe.schema.yaml` 的 `type` enum 加新类型。
2. `recipes/` 加一个演示配方。
3. **三个后端全部实现**：`backends/matplotlib_adapter.py`、`backends/ggplot2_adapter.R`、`backends/observable_adapter.js`；某后端确实无法支持时，显式失败并留 TODO，不得静默跳过。
4. 若涉及系列离散着色，把类型加入 `sci_render.py.SERIES_CHART_TYPES` 与适配器内同名集合。
5. `tests/test_all.py` 加覆盖（存在性 + 端到端渲染 + 至少一个门禁拦截用例）。

### B. 新增质量门
1. `quality/gates.yaml` 声明规则（id/level/rule）。
2. 渲染前规则加进 `run_quality_gates()`；渲染后规则加进 `main()` 的 P2/P3 段。
3. 规则必须有明确的触发条件声明（如「声明 X 时启用」），保持向后兼容：旧配方不声明即不启用。
4. 测试：一个拦截用例 + 一个通过用例。

### C. 新增命名色板
1. 只改 `core/palettes.py` 的 `PALETTE_REGISTRY`：必填 `kind`（categorical/sequential/diverging）、`cvd_safety`（high/medium/unverified）、`source`、`availability`。
2. **诚实声明**：非后端内置的色板在 `availability` 中标注「不可用」，`mpl_name: None`；未独立验证 CVD 安全性的标 `unverified`。测试强制此约定。

### D. 新增 Profile
1. 建 `profiles/<name>.yaml`（结构见 `profiles/README.md`），必须含顶层 `source_url` + `verified_date`（YYYY-MM-DD；内部默认配置 `source_url: null`）。
2. `aesthetics` 中的 `dpi`、`max_width_in/max_height_in`、`font_size` 会被 P1/P3 门禁机器校验；`constraints` 只是人类可读摘要，必须与门禁规则一致。
3. 用 `--profile <name>` 引用；文件缺失即 `MISSING_PROFILE`。

### E. 新增后端适配器
1. 建 `backends/<name>_adapter.<ext>`：吃配方数据 + 合并 aesthetics → 生成目标语言代码 → 执行 → 写图件 + `.manifest.json`。
2. 在 `sci_render.py` 的 `backend_script_map` 与 `BACKEND_CAPABILITIES` 注册，并同步 `MANIFEST.yaml` 的 `backends[].capabilities`。
3. 适配器保持 dumb：不做校验，不覆盖 profile 样式。

## 6. 编码约定（不许做清单）

- 禁止绕过 `sci_render.py` 直连适配器。
- 禁止在适配器里加校验逻辑；禁止在 CLI 里加绘图逻辑。
- 禁止 `shell=True`：分发一律列表式 `subprocess.run`。
- 临时生成的渲染脚本（`_generated_render.*`）执行后必须清理，不留脏文件。
- **依赖政策**：Python 侧只用 `pyyaml / jsonschema / matplotlib / numpy`；JS 侧仅 `package.json` 声明的 `yaml`；R 侧仅 `yaml/jsonlite/digest/ggplot2`。不得引入新依赖。CDN 链接不做版本锁定（用 `@observablehq/plot` 而非 `@observablehq/plot@0.6`），除非严格必要。
- **能力诚实**：未实现/未验证的能力如实标注（注册表 availability、README 边界说明、R 路径未运行时验证等），不得伪装。
- **测试纪律**：改动后跑 `python3 tests/test_all.py`（或 `make test`），26/26 方可收尾；node/R 相关用例缺环境自动 SKIP 属正常。R/JS 适配器内嵌的语义色常量必须与 `core/color_encoding.py` 保持一致（有静态一致性测试）。
- 未接入主流程的新模块必须标 `[EXPERIMENTAL]`。
- 提交信息用 Conventional Commits（`feat:` / `fix:` / `docs:` / `test:` / `chore:`）。
