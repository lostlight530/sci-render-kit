# sci-render-kit

**声明式科研图件编译：把数据语义、claim 绑定、可访问性、出版目标、后端边界与证据旁车放进同一条可检查链**  
*Declarative scientific-figure compilation with bounded claim bindings, publisher profiles, provenance, accessibility and figure evidence.*

## 当前定位

`sci-render-kit` 不判断科研结论是否正确，也不把“画出一张图”包装成“完成复现”。它负责把一个声明式 recipe 转换成后端可实现的图件，并留下足够清楚的运行与沟通证据。

```text
Recipe + research context + claim bindings + uncertainty + process disclosure
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
Figure Evidence Envelope @2
```

### 科研边界

```text
A rendered figure ≠ a true scientific conclusion
A runtime rule pass ≠ scientific validity
A publisher profile match ≠ journal acceptance
A visual-to-claim binding ≠ verified entailment
An interval ≠ a confidence interval unless its semantics say so
A checksum ≠ independent reproduction
Human review ≠ peer review
AI/tool disclosure ≠ authorship adjudication
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
- `research_context.claim_bindings`：显式 `visual_ref -> claim_refs[]` 沟通关系
- `process_disclosure`：AI assistance / tool identifiers / human-review state
- `uncertainty.kind` / `uncertainty.semantics` / `uncertainty.source_ref`
- `accessibility`：text alternative、redundant encoding、adjacent pairs

Schema 通过只说明 recipe 结构符合当前声明，不证明 claim、统计分析、AI disclosure 或 publisher compliance 正确。

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

## Research context、claim binding 与 uncertainty

Recipe 可以把上游研究证据和 claim 关系带到图件 handoff：

```yaml
research_context:
  artifact_id: analysis-042
  evidence_envelope_ref: evidence/run-042.evidence.json
  provenance_ref: provenance/run-042.prov.json
  claim_refs: [claim_1, claim_2]
  claim_bindings:
    - visual_ref: series:treated
      claim_refs: [claim_2]
      relation: illustrates
      evidence_ref: evidence/run-042.evidence.json

uncertainty:
  kind: bootstrap-interval
  level: 0.95
  semantics: "95% percentile bootstrap interval over declared resamples"
  source_ref: analysis-042
```

允许的 claim binding relation：

```text
supports
illustrates
contextualizes
compares
derived-from
```

这些只是 recipe **显式声明的沟通关系**。renderer 不分析标题、图例或像素来猜测缺失绑定，也不验证逻辑蕴含、因果支持或 evidence sufficiency。

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

## Process disclosure

Recipe 可以可选声明图件生成/准备过程：

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools:
    - provider/model or tool identifier declared by the author
  human_review: reviewed
  disclosure_ref: methods/figure-disclosure.md
```

字段语义是**过程披露**，不是作者资格或科学审查：

```text
ai_assistance: none|used|not_declared
human_review: reviewed|partial|not_reviewed|not_declared
```

缺失字段不会被解释成 `none` 或 `reviewed`。`ai_tools` 是人工/上游系统声明的标识，仓库不会向厂商 registry 自动验真。

## Figure Evidence Envelope

`core/figure_evidence.py` 输出：

```text
sci-render-kit/figure-evidence@2
```

它汇总：

- figure / recipe / profile / manifest / provenance / accessibility sidecar 的 SHA-256 引用
- backend 与 output identity
- 上游 `research_context`
- `sci-render-kit/figure-claim-binding@1`：figure-level claim refs + visual-to-claim bindings
- `sci-render-kit/process-disclosure@1`：AI assistance / tools / human-review disclosure
- `uncertainty`
- runtime validation findings
- local reproducibility level
- `scientific_validity_claim: false`
- `statistical_validity_claim: false`
- `causal_validity_claim: false`
- `authorship_claim: false`
- `peer_review_claim: false`
- `publisher_acceptance_claim: false`

`claim_communication.inferred_bindings` 固定为 `false`：只有 recipe 显式声明的绑定会进入证据包。

这是与 `epistemic-pipeline/evidence-envelope@2` 等上游对象衔接的项目 handoff contract，不是外部标准。

详细语义见 [Figure Claim & Process Disclosure Contract](FIGURE_CLAIM_CONTRACT.md)。

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
- [Figure Claim & Process Disclosure Contract](FIGURE_CLAIM_CONTRACT.md)
- [Frontier Alignment](FRONTIER_ALIGNMENT.md)
- [Architecture](ARCHITECTURE.md)
- [Profile Guide](profiles/README.md)
- [Examples](examples/README.md)
- [Agent Guide](AGENTS.md)
- [Manifest](MANIFEST.yaml)

## Research software citation

仓库提供 Citation File Format 1.2.0 `CITATION.cff`。

## License

MIT License
