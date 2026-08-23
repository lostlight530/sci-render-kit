# sci-render-kit

**声明式学术可视化：把配方、出版规范、可复现性与可访问性放进同一条可审计渲染链**  
*Declarative scientific visualization with publishing profiles, provenance, and auditable accessibility contracts.*

## 当前定位

`sci-render-kit` 不是“自动把图画漂亮”的包装器。它把科研图件看成一个需要同时满足四类运行时约束的研究产物：

```text
Recipe Schema (P0)
    ↓
Aesthetics + Accessibility (P1)
    ↓
Backend capability + render
    ↓
Output integrity / metadata / provenance (P2)
    ↓
Journal profile (P3)
```

核心思想是：**图的颜色、线型、marker、文本替代、尺寸、DPI、输出格式和溯源都应成为可声明、可检查、可复查的事实，而不是散落在脚本里的隐含习惯。**

## 快速开始

普通配方：

```bash
python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend matplotlib
```

带可访问性契约的配方：

```bash
python3 sci_render.py recipes/accessible-line-chart.yaml --profile presentation --backend matplotlib
```

该示例会生成图件，并在既有 `.manifest.json` / `.prov.json` 之外生成同名 `.a11y.json`。

## 四层运行时质量规则

### P0 — Recipe schema

`metadata/recipe.schema.yaml` 校验图表类型、数据、美学、输出以及新的 `accessibility` 对象。

### P1 — 美学与可访问性

已接入的主要规则：

- `palette-contrast`：需要被辨认的色板颜色与背景保持项目要求的 ≥ 3.0 对比度
- `text-contrast`：声明 `text_color` 时对背景 ≥ 4.5（WCAG 2.2 SC 1.4.3）
- `text-alternative`：`require_alt_text: true` 时必须提供 `alt_text`，用于支撑 SC 1.1.1 的文本替代设计
- `non-color-cue`：`redundant_encoding: required` 时，多系列 line / scatter / bar 必须有可区分 marker / line style / hatch，支撑 SC 1.4.1“颜色不能是唯一信息通道”的设计原则
- `declared-adjacency`：只对 `accessibility.adjacent_pairs` 声明的实际相邻且需要辨认的系列边界做 ≥ 3.0 检查，贴近 SC 1.4.11 / G209 的真实作用域
- `palette-adjacency`：旧的 `aesthetics.adjacency_check: true` 仍保留为**项目更严格的全色对策略**；它不是 WCAG 要求所有分类色两两 3:1
- `cvd-contrast`：Machado 2009 三类 CVD 模拟下的额外项目防护，不包装成 WCAG 条文本身
- `palette-name`：命名色板必须命中注册表，系列图必须使用 categorical 类型

### P2 — 输出完整性

统一检查：

- 图件存在且非空
- 扩展名与声明格式一致
- `.manifest.json` 存在
- Matplotlib `.prov.json` 存在
- 配方声明 `accessibility` 时 `.a11y.json` 存在

### P3 — 期刊 profile

Nature / Science / Cell / IEEE / presentation profile 保持出版约束。P3 负责矢量格式、DPI、宽高上限等明确规则，而不是把“期刊名”当成一个模糊 style preset。

## Accessibility contract

Recipe 新增：

```yaml
accessibility:
  require_alt_text: true
  alt_text: "Two series diverge over four observations."
  long_description: "Optional longer interpretation or data-table pointer."
  redundant_encoding: required
  adjacent_pairs:
    - [control, treatment]
```

还可以按系列覆盖非颜色线索：

```yaml
accessibility:
  redundant_encoding: required
  series_styles:
    control:
      marker: o
      line_style: "-"
    treatment:
      marker: s
      line_style: "--"
```

Matplotlib 当前真正消费这些 series style；如果 R/Observable 配方要求 `auto` / `required` 冗余编码，统一 CLI 会返回 `BACKEND_ACCESSIBILITY_MISMATCH`，直到对应后端完成真实接线。**能力矩阵不再把“schema 支持”误写成“后端已实现”。**

## `.a11y.json`

当 recipe 声明 accessibility 时，统一 CLI 写出：

```text
<figure>.a11y.json
```

内容包括：

- `sci-render-kit/a11y@1` profile
- `alt_text` / `long_description`
- redundant-encoding 模式
- 每个系列的颜色与非颜色 cue
- 声明的 adjacent pairs
- 明确的 `conformance_claim: false`

这是可访问性设计与审计旁车，不等于一张 PNG、一个 PDF 或整篇论文自动获得 WCAG 合规认证。

## Matplotlib adapter architecture

为避免把成熟渲染逻辑和政策规则揉成一个巨型文件：

```text
backends/matplotlib_base.py
    └─ 原有渲染 / manifest / provenance 基础实现

backends/matplotlib_adapter.py
    └─ 公共兼容层
       + marker / line-style / hatch 冗余编码
       + alt-text metadata（格式支持时）
       + accessibility manifest linkage
```

公共 adapter 保留直接脚本执行的 repo-root import bootstrap，因此 `python3 backends/matplotlib_adapter.py ...` 与模块导入两种方式都继续可用。原有 `generate_python_code`、`resolve_palette` 等公共接口继续由 adapter 重导出，降低架构升级对既有调用者的破坏。

## Provenance 与 reproducibility

Matplotlib 仍生成：

- `.manifest.json`：运行参数与输出 checksum
- `.prov.json`：recipe / input / output SHA-256、运行环境与生成时间
- 图件内嵌 provenance metadata（格式支持范围内）

这些能力提高可追溯性与复现证据质量，但 README 不再使用“100% 可复现”这种无法由单一 manifest 保证的绝对表述。

## 实现状态

| 能力 | 状态 |
|---|---|
| Unified `sci_render.py` dispatcher | **Implemented** |
| Matplotlib base renderer | **Implemented** |
| Matplotlib accessibility policy adapter | **Implemented** |
| R ggplot2 renderer | **Implemented / runtime environment optional** |
| Observable renderer | **Implemented / node environment optional** |
| Recipe / profile / P0–P3 runtime checks | **Implemented** |
| semantic palette / named palettes / CVD simulation | **Implemented** |
| text alternative contract + `.a11y.json` | **Implemented** |
| redundant marker/line-style/hatch rendering | **Implemented (Matplotlib)** |
| redundant series style on R/Observable | **Not Integrated** |
| Matplotlib provenance sidecar + embedded metadata | **Implemented** |
| R/Observable provenance parity | **Optional follow-up** |
| projection / time_crystal / uncertainty_legend / observer_dashboard / superposition | **Experimental** |

## 本地检查

需要时可以手动运行：

```bash
python -m pip install pyyaml jsonschema matplotlib numpy pillow
make test
```

这些检查覆盖既有渲染、运行时质量规则、色板、期刊 profile、provenance 与 accessibility 行为，只是本地维护工具，**不是 GitHub 合并门禁**。

Node/R 端到端环境仍保持可选；没有对应 runtime 时不能把“未运行”包装成已验证。

## 科研软件引用

仓库提供 `CITATION.cff`（Citation File Format 1.2.0）。

## 文档

- [Architecture](ARCHITECTURE.md)
- [Profile Guide](profiles/README.md)
- [Examples](examples/README.md)
- [Agent Guide](AGENTS.md)
- [Manifest](MANIFEST.yaml)

## License

MIT License
