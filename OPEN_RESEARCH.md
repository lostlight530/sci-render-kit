# Open Research / 开放科研

Status: durable open-research production guide
Scope: repository-level research positioning, independent research-production method, scholarly-metadata boundaries, and semantic-drift governance

## Language policy / 语言政策

English is the canonical and default language for this open-research contract. Chinese text is provided as an accessibility and interpretation aid. If wording diverges, the English normative text governs; repository evidence and current owning contracts remain authoritative over both.

英文是本开放科研契约的默认与规范语言；中文用于辅助理解与可访问性。若中英文表述有差异，以英文规范文本为准；仓库事实与当前 owning contract 的权威仍高于任何翻译。

## Authority

This guide complements implementation, `MANIFEST.yaml`, architecture, figure/communication contracts, maintenance contracts, release policy, and historical evidence. It does not replace them.

```text
current repository truth
→ implementation / MANIFEST / figure-evidence contracts
→ OPEN_RESEARCH.md
→ RESEARCH_TEMPLATE.md
→ prospective research records
→ scholarly metadata / downstream indexes
```

A stricter repository-native contract wins.

## Canonical positioning

**Canonical Type:** Scientific-figure compilation and evidence-aware communication research software

**One-line positioning:** Research software for declarative scientific-figure compilation with backend-bounded rendering, provenance, figure-evidence records, uncertainty semantics, accessibility checks, and publisher-target boundaries

**Primary domains:** scientific visualization; data visualization; figure provenance; uncertainty communication; accessibility; reproducibility

**Non-goals:** scientific truth engine; statistical validator; publisher acceptance service; accessibility certification authority; generic image editor

```text
External Classification != Repository Identity
Inferred Topic != Canonical Research Domain
Keyword Match != Project Purpose
Scholarly Graph Representation != Repository Self-Definition
```

## Independent research-production layer

Engineering and maintenance evidence do not automatically constitute an independent research result. New research units should explicitly preserve question, falsifiability, data/source identity, figure/recipe/backend identity, procedure actually executed, raw observation, counterexample or misleading-interpretation check, bounded conclusion, research increment, and retest condition.

A successful render or target-profile check establishes only the implemented predicate actually observed.

## Repository-specific method

Record when relevant
- scientific claim or communication objective
- input data and uncertainty identity
- figure recipe identity
- rendering backend and version
- visual encoding
- claim-to-figure binding
- provenance or figure-evidence sidecar
- accessibility checks
- publisher-target constraints
- misleading-interpretation counterexample

`render success != scientific truth`
`claim binding != entailment`
`uncertainty metadata != statistical validation`
`accessibility check != certification`
`publisher profile != acceptance`

Research records should preserve scientific claim or communication objective, input data and uncertainty identity, rendering backend/version, visual encoding, claim-to-figure binding, provenance/evidence sidecars, accessibility checks, publisher-target constraints, and misleading-interpretation counterexamples where relevant.

## Evidence and execution discipline

```text
render success != scientific truth
claim binding != entailment
uncertainty metadata != statistical validation
accessibility check != certification
publisher profile != acceptance
```

Unknown or unexecuted states stay explicit.

## Open-science file responsibilities

- `README.md` — public orientation.
- `OPEN_RESEARCH.md` — durable open-research method and positioning.
- `RESEARCH_TEMPLATE.md` — prospective bounded research-record template.
- `AUTHORS`, `LICENSE`, `CITATION.cff`, `codemeta.json` — authorship, reuse, citation/software metadata.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` — contribution/community/security governance.
- `RELEASE_POLICY.md` — release/archive semantics.
- `.github/ISSUE_TEMPLATE/**` and pull-request template — reviewable intake.

These support open research; they do not establish scientific validity.

## Scholarly metadata discipline

Preserve Canonical Type, One-line Positioning, Primary Domains, Non-goals, accurate structured subjects where supported, and 5–7 defining keywords before future metadata publication. Do not rewrite precise scientific-software descriptions for classifier optimization or keyword stuffing.

## Shadow classification

Candidate title + abstract/description may be checked against downstream topic/keyword inference.

```text
ALIGNED
PARTIALLY_ALIGNED
MISCLASSIFIED
CLASSIFIER_NOISE
```

Execution state is separately `RUN` or `NOT_RUN`. Repair owning metadata only for genuine upstream ambiguity; otherwise record downstream classifier noise.

## Semantic drift audit

Compare canonical positioning with `CITATION.cff`, CodeMeta, archive/DOI metadata, OpenAIRE, and OpenAlex.

- **CANONICAL_DRIFT**
- **TRANSPORT_DRIFT**
- **DERIVATION_DRIFT**
- **VERSION_SKEW**

`DERIVATION_DRIFT != REPOSITORY_DEFECT`.

## History and correction

```text
CURRENT_STATE != TASK_TIME_STATE
LATER_SUCCESS != EARLIER_SUCCESS
PUBLICATION_IDENTITY != CURRENT_MAIN
RESEARCH_PRODUCTION != MAINTENANCE != PERIODIC_AUDIT
```

Preserve historical Stage/maintenance records. Correct current interpretation forward through correction, reconciliation, or a new timepoint record.

## Contribution and review

Use `OPEN_RESEARCH.md` for research-method/positioning changes and `RESEARCH_TEMPLATE.md` for new research records. State data/figure/recipe/backend identities, procedures and checks actually executed, raw observations, unresolved interpretation risk, and historical impact.

## Permanent boundary

```text
research record != capability claim
publication != validation
usage != adoption
citation != reproduction
metadata consistency != scientific correctness
external indexing != repository self-definition
```

## 中文摘要

本文件定义 Sci Render Kit 的长期开放科研方法，并与工程实现、figure/communication contract、maintenance 和历史记录分层。共同科研骨架要求研究问题、可证伪假设、数据/来源身份、固定 figure/recipe/backend 身份、实际执行程序、原始观测、反例或误导性解释检查、有界结论、研究增量与复验条件。

render success、claim binding、uncertainty metadata、accessibility check、publisher profile 都只能支持其实际检查到的属性，不能自动升级为科学真值、统计验证、认证或期刊接收。

未来 scholarly metadata 以准确定位、少量高质量 subjects 与 5–7 个定义性 keywords 为主；外部分类漂移只有在 upstream metadata 确有歧义时才修 owning layer，否则记录 classifier noise。
