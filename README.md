# sci-render-kit

**声明式科研图件编译：把数据语义、可访问性、出版目标、后端边界与证据旁车放进同一条可检查链**  
*Declarative scientific-figure compilation with bounded publisher profiles, provenance, accessibility and figure evidence.*

## 当前定位

`sci-render-kit` 不判断科研结论是否正确，也不把“画出一张图”包装成“完成复现”。它负责把一个声明式 recipe 转换成后端可实现的图件，并留下足够清楚的运行证据。

```text
Recipe + research context + uncertainty semantics
        ↓ P0 schema
Runtime visual/accessibility rules
        ↓ P1 findings (error / warning / info)
Backend capability resolution
        ↓
Render
        ↓
Render manifest + provenance + accessibility sidecar
        ↓ P2 artifact integrity
Publisher-target alignment
        ↓ P3 findings
Figure Evidence Envelope
```

### 科研边界

```text
A rendered figure ≠ a true scientific conclusion
A runtime rule pass ≠ scientific validity
A publisher profile match ≠ journal acceptance
An interval ≠ a confidence interval unless its semantics say so
A checksum ≠ independent reproduction
An accessibility sidecar ≠ WCAG conformance of a whole publication
```

## 快速开始

```bash
python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend matplotlib
python3 sci_render.py recipes/accessible-line-chart.yaml --profile presentation --backend matplotlib
```

成功路径根据实际能力生成：

```text
<figure>
<figure>.manifest.json
<figure>.prov.json       # Matplotlib path
<figure>.a11y.json       # recipe declares accessibility
<figure>.evidence.json   # unified CLI figure handoff
```

## Runtime rules，不是 GitHub 门禁

当前 active catalog 是：

```text
quality/rules.yaml
profile: sci-render-kit/runtime-quality@1
```

规则输出结构化 finding：

- `error`：当前声明无法可靠实现或产物契约失败，停止本次 render
- `warning`：项目 safeguard / publisher-target mismatch，保留为证据但不冒充失败
- `info`：解释性记录

P0/P1/P2/P3 是**运行阶段**，不是 GitHub Actions、CI、branch protection 或 merge gate。

### P0 — Recipe structure

`metadata/recipe.schema.yaml` 约束 chart type、data、aesthetics、output，并支持：

- `research_context`：上游 artifact / evidence / provenance / claim 引用
- `uncertainty.kind` / `uncertainty.semantics` / `uncertainty.source_ref`
- `accessibility`：text alternative、redundant encoding、adjacent pairs

### P1 — Visual / accessibility semantics

主要规则包括：

- `text-alternative`：`require_alt_text: true` 时必须提供短文本替代
- `non-color-cue`：需要 redundant encoding 时，颜色不能是唯一系列区分方式
- `declared-adjacency`：只对声明为实际相邻且理解所需的图形边界检查 3:1
- `text-contrast`：声明文字颜色时检查文字/背景对比度
- `palette-adjacency`：可选的全色对项目严格策略，**不是 WCAG 的普遍要求**
- `cvd-contrast`：Machado 2009 模拟的项目额外 safeguard，**不是 WCAG 强制测试**
- `palette-name`：注册色板必须与图表语义类型匹配

### P2 — Artifact integrity

检查输出文件、扩展名、render manifest、Matplotlib provenance sidecar、可访问性 sidecar 等当前实现的 artifact contract。

### P3 — Publisher-target alignment

Publisher profile 是带来源状态的机器可读 preset，不是官方 submission validator。

- `nature`：2026-08-24 已重新核对当前 Nature figure guidance 的主图尺寸/字体/编辑性与初稿 raster guidance
- `science` / `cell` / `ieee`：保留 2026-08-19 snapshot，并明确标记 `snapshot_not_reverified_2026_08_24`
- `presentation`：内部 preset，无外部 publisher authority

P3 mismatch 默认是 warning；profile 内明确 `acceptance_claim: false`。

## Research context 与 uncertainty

Recipe 可以把上游研究证据带到图件 handoff：

```yaml
research_context:
  artifact_id: analysis-042
  evidence_envelope_ref: evidence/run-042.evidence.json
  provenance_ref: provenance/run-042.prov.json
  claim_refs: [claim_1, claim_2]

uncertainty:
  kind: bootstrap-interval
  level: 0.95
  semantics: "95% percentile bootstrap interval over declared resamples"
  source_ref: analysis-042
```

允许的 uncertainty kinds 包括：

```text
standard-error
standard-deviation
confidence-interval
credible-interval
min-max-range
quantile-interval
bootstrap-interval
heuristic-bound
```

只有明确声明统计语义时，区间才应被描述成 confidence / credible interval。

## Figure Evidence Envelope

`core/figure_evidence.py` 输出：

```text
sci-render-kit/figure-evidence@1
```

它汇总：

- figure / recipe / profile / manifest / provenance / accessibility sidecar 的 SHA-256 引用
- backend 与 output identity
- `research_context`
- `uncertainty`
- runtime validation findings
- local reproducibility level
- `scientific_validity_claim: false`

这是与 `epistemic-pipeline/evidence-envelope@1` 等上游对象衔接的项目 handoff contract，不是外部标准。

## Backend truth

| Backend | Outputs | 当前证据边界 |
|---|---|---|
| Matplotlib | PNG / SVG / PDF | `render-manifest@2` + `provenance@2`; non-color series styling implemented |
| ggplot2 | PNG / SVG / PDF | `render-manifest@2`; R environment recorded when run |
| Observable Plot | HTML | `render-manifest@2`; generated HTML pins Plot 0.6.17 ESM CDN and records browser network dependency |

Matplotlib 不再偷偷把声明 DPI 强制抬到 300；最终 DPI 来自 profile/recipe 的实际声明。

Matplotlib accessibility adapter 通过显式 `render_logic_fn` / `metadata_fn` 注入扩展 base renderer，不再在 render 期间修改全局 base 函数。

## Accessibility

`core/accessibility.py` 生成 `sci-render-kit/a11y@1` sidecar，并明确：

```text
conformance_claim: false
```

当前设计支持映射到 WCAG 2.2：

- SC 1.1.1 — text alternative support
- SC 1.4.1 — color is not the only required information channel
- SC 1.4.11 — required graphical object/boundary contrast where applicable

完整 PDF / HTML / 论文的 accessibility 仍取决于发布层如何关联文本、图件与交互内容。

## Color semantics

`CognitiveColorEncoder` 类名为兼容保留。当前实现语义是：

> project color convention + sRGB color utilities

`positive -> green`、`stable -> blue` 等是项目映射，不是普世认知心理规律。WCAG contrast 使用当前 sRGB relative-luminance 计算；CVD simulation 是额外 robustness signal。

## Experimental modules

Experimental 不等于 canonical capability：

- `projection.py`：真实 centered-SVD PCA + rank-based trustworthiness / continuity；t-SNE 未实现时明确 `NotImplementedError`
- `uncertainty_legend.py`：typed interval/heuristic-bound visual metadata，不再借海森堡不确定性解释普通区间
- `superposition.py`：deterministic variant layering；量子干涉未实现
- `time_crystal.py`：periodic waveform utility；不是物理 time-crystal simulator
- `observer_dashboard.py`：caller-supplied interaction telemetry accumulator；不自动推断 comprehension 或因果

## Reproducibility semantics

本仓使用局部 R0–R3 术语：

- **R0 Traceable** — figure 与声明来源可关联
- **R1 Replay-addressable** — recipe/data/profile/output identity 与 hash 可定位
- **R2 Environment-bounded** — 运行环境与关键依赖边界也被记录
- **R3 Reproduced** — 实际执行了独立 rerun，并按声明 criterion 比较

生成 `.manifest.json` / `.prov.json` / `.evidence.json` 本身不等于 R3。

## 本地维护

```bash
python -m pip install pyyaml jsonschema matplotlib numpy pillow
make test
```

这些命令只是可选的本地维护工具。**仓库不需要 GitHub Actions / CI / CodeQL / merge gate 来定义科研架构。** 本轮维护不以运行测试为目标。

## 文档

- [Research Contract](RESEARCH_CONTRACT.md)
- [Architecture](ARCHITECTURE.md)
- [Profile Guide](profiles/README.md)
- [Examples](examples/README.md)
- [Agent Guide](AGENTS.md)
- [Manifest](MANIFEST.yaml)

## Research software citation

仓库提供 Citation File Format 1.2.0 `CITATION.cff`。

## License

MIT License
