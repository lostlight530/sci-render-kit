# sci-render-kit 仓库纪念｜2026-10-28｜CS：科学可视化、可访问性交互与图件证据
# Repository Commemoration · 2026-10-28 · Computer Science: Scientific Visualization, Accessibility, and Figure Evidence

> **Identity / 记录身份：** Independent bilingual commemorative disciplinary study · 独立新增的中英双语学科研究纪念；static inspection of repository-native scripts and research documents / 基于原生脚本与研究文档的静态核查；not a historical rewrite, runtime execution report, or certification / 不改写历史、不声称执行或认证。
>
> **CS2023 alignment / 学科坐标：** GIT (Visualization/Rendering); HCI; SE; DM. These are scholarly comparisons, not endorsements or exact implementation equivalences / 研究分类而非外部机构背书或实现等价。

## 1. 专业归属：这是 CS 的哪一类？ / Disciplinary Position

**中文** — 本仓不是简单“画图服务”，而是**科学可视化、数据编码、图形可访问性与科研沟通证据工程**的结合。CS2023 把 Graphics and Interactive Techniques（GIT）与 Human-Computer Interaction（HCI）独立列为知识领域；视觉编码既关系到可读性，也关系到误导风险。这里研究一个科学结论如何被有限度地表达成图，以及这一转换过程能留下什么证据。

**English** — Sci Render Kit is not merely a chart generator. It connects **scientific visualization, visual encoding, accessibility, and evidence-aware research communication**. CS2023 identifies Graphics and Interactive Techniques (GIT) and Human–Computer Interaction (HCI) as distinct knowledge areas. Choices in color, non-color cues, uncertainty, profiles, and backends affect what a viewer can perceive and what the artifact can honestly claim.

## 2. 仓库自身如何体现？ / Repository-native Architecture and Evidence

**中文** — `sci_render.py` 解析 recipe、检查 P0/P1 约束、分配 Matplotlib、ggplot2 或 Observable 后端、生成渲染与 sidecar；`metadata/recipe.schema.yaml` 描述输入数据、图形、可访问性和研究上下文；`quality/rules.yaml` 定义项目规则。`core/accessibility.py`、`color_encoding.py`、`cvd_simulation.py` 处理视觉可及性相关的具体指标；`claim_binding_audit.py` 检查声明的 visual-to-claim 关联；`figure_evidence.py`、`communication_transfer.py` 记录渲染文件、来源与不继承边界；`recipes/**` 是具名示例。原生架构语义见 `docs/01-source-and-explanation/ARCHITECTURE.md`。

**English** — `sci_render.py` coordinates recipe loading, P0/P1 checks, backend dispatch to Matplotlib/ggplot2/Observable where supported, and rendered artifacts with sidecars. `metadata/recipe.schema.yaml` declares data, chart, accessibility, and research context; `quality/rules.yaml` enumerates project checks. `core/accessibility.py`, `color_encoding.py`, and `cvd_simulation.py` contribute explicit perceptual/accessibility predicates. `claim_binding_audit.py` checks declared visual–claim relations; `figure_evidence.py` and `communication_transfer.py` preserve outputs, references, and non-inheritance boundaries. `recipes/**` supplies concrete examples; the native architecture document owns the technical explanation.

## 3. 人话解释 / In Plain Language

**中文** — 同一组实验数据，画得漂亮不一定画得诚实。**这仓像科学论文的图像工程师兼质检员**：先确认数据和绘图配方，再问颜色是否是唯一线索、误差有没有交代、读者能否追溯图怎样产生。它不替科学家宣告假设成立。

**English** — The same data can make a beautiful but misleading figure. Think of this repository as a **scientific figure engineer and inspection desk**: it records the recipe, checks whether color is the only cue, retains uncertainty declarations, and explains how output files were produced. It does not replace scientific judgment.

## 4. 如何读懂而不夸大？ / Verification and Non-claim Boundaries

**中文** — WCAG 2.2 是精确条款的参照，不是本仓整体可访问性认证。声明 `supports` 只是作者所给的关系，并不推导统计支持或因果关系；render success 不证明出版商接收、科研真实性或跨 backend 功能等价。对图形后端功能支持应逐项按脚本检查，不根据 schema 字段自动假定。

**English** — WCAG 2.2 references specific accessibility principles, not repository-wide conformance certification. A declared `supports` relation is not statistical entailment or causal proof. A successful render does not establish publisher acceptance, scientific validity, or backend parity. A schema field does not create the corresponding implemented renderer feature.

## 5. 十仓中的独特贡献 / Place in the Ten-repository Research System

**中文** — 三仓科研工程体系中，它专职**让研究论点可视化且保留其表达证据**。Auto Doc Engine 管文档与 artifact；Epistemic Pipeline 管研究声明、证据与冲突；Sci Render Kit 管图件输出与沟通边界。三者相互参照但不能互相授予真实性。

**English** — Within the research-engineering trio, it owns **figures and the evidence of scientific communication**. Auto Doc Engine handles documents and artifacts, Epistemic Pipeline handles claims and evidence, and Sci Render Kit handles visual representation. None can grant the others' claims scientific truth.

## 6. 纪念与升华 / Commemoration and Wider Meaning

**中文** — **当复杂 AI 系统开始替人写论文、绘制图表时，审美不能代替诚实。好的可视化不只是让结论被看见，也让限制与误差同样被看见。**

**English** — **As AI systems increasingly draft research and figures, aesthetics cannot replace honesty.** Good visualization makes both a finding and its uncertainty visible.

## 外部学科对照 / External Disciplinary Anchors

- [CS2023: Graphics and Interactive Techniques](https://csed.acm.org/knowledge-areas/)
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)

> **Provenance / 证据说明：** GitHub repository-native artifacts were read at the 2026-10-28 review cutoff. External sources establish disciplinary context only; independent reproduction, external certification and newly executed tests are **NOT_CLAIMED**. / 原生文件按本次时间点核读；外部来源只用于学科对照；**不声称本轮重新执行测试、独立复现或第三方认证**。
