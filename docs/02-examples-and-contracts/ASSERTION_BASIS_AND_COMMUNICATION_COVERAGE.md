> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `METHOD / EVIDENCE CONTRACT`
> - **Role:** Current contract for assertion basis and dimensional communication coverage
> - **Authority:** Current repository-native authority for the scientific-communication semantics explicitly owned by this file; current renderer/runtime and machine contracts remain the executable-behavior boundary
> - **Current meaning:** Read this subject inside the `declared recipe/data → communication audit → render → figure evidence → bounded transfer` chain. It preserves what a figure declares and how that declaration was recorded without silently upgrading communication into scientific proof
> - **Evidence / implementation boundary:** Render success is not scientific truth; a `supports` binding is not entailment; communication coverage is not evidence sufficiency or probability; uncertainty metadata is not statistical validation; accessibility support is not WCAG certification; publisher profile alignment is not acceptance; downstream transfer does not inherit validity
> - **Cross-document relation:** Architecture integrates the full figure pipeline; specialized contracts own binding/coverage/transfer semantics; current code and machine contracts bound implementation; `DOCUMENT_STATUS.md` separates current contracts from historical snapshots
> - **Update trigger:** Update when owned figure/evidence/transfer semantics or implemented mechanics materially change, or when a confirmed current-authority conflict appears
> - **Preservation rule:** Existing technical content and dated stage calibration remain intact. Historical stage-close or research-language passages retain their own evidence boundary

# Assertion Basis & Communication Coverage — sci-render-kit

## 中文专业正文对照 / Chinese technical counterpart

**具体研究对象 / Concrete subject:** 展示覆盖度应按 claim、visual binding 与可访问性维度分别记录，不构造未经论证的总体质量评分

**English owning title:** Assertion Basis & Communication Coverage — sci-render-kit

**图像证据判别 / Figure evidence reading:** 应分别取得源数据版本、recipe/profile、实际后端输出、manifest、声明绑定、上游 sidecar 与可访问性实测结果，不能将图像 bytes、示例文档或测试定义视为实际同行评审 / Keep source, recipe, backend, manifest and claim identities separate, verify the exact execution evidence before asserting quality or reproducibility

| English original section / 英文原章 | 中文对应定位 / Chinese section meaning |
| --- | --- |
| Purpose | 目标 |
| Assertion bases | 该图像合同的局部机制与证据限制 |
| No automatic AI detection | 该图像合同的局部机制与证据限制 |
| Communication coverage | 该图像合同的局部机制与证据限制 |
| No aggregate communication-quality score | 不得汇总未经核验的质量分数 |
| Transfer coverage stays separate | 该图像合同的局部机制与证据限制 |
| Runtime validation remains separate | 该图像合同的局部机制与证据限制 |
| Relation to current research-agent work | 该图像合同的局部机制与证据限制 |
| Current document and maintenance authority | 该图像合同的局部机制与证据限制 |
| Hard boundaries | 该图像合同的局部机制与证据限制 |
| The denominator of coverage is not a denominator of truth | 该图像合同的局部机制与证据限制 |

**限界 / Limits:** 原有配置、图形行为与未知执行状态保持不变，本节不新增科学审定、出版接纳、WCAG 认证或真实浏览器通过声明 / Original behaviors and unknown states are unchanged, no scientific or publisher certification is implied


**Calibration:** 2026-08-31  
**Status:** implemented companion contract for `sci-render-kit/figure-claim-audit`, `sci-render-kit/figure-evidence`, and downstream communication handoff

## Purpose

Scientific communication metadata should expose both

1. **what the recipe declares** about claims, evidence context, uncertainty and process
2. **where that declaration or identity came from**

The repository therefore keeps

```text
assertion basis
communication coverage
runtime validation
scientific validity
```

as separate concepts

## Assertion bases

Current figure-side bases include

| Surface | Basis |
|---|---|
| figure bytes | `runtime-observed-local-bytes` |
| recipe/profile file identity | runtime-observed local bytes + canonical serialization |
| claim refs | `recipe-declared` |
| visual-to-claim bindings | `recipe-declared` |
| process disclosure | `recipe-declared` |
| uncertainty semantics | `recipe-declared` |
| upstream research refs | recipe-declared with optional local resolution |
| local reference resolution | `runtime-observed-local-filesystem` |
| transferred context | copied from local figure-evidence sidecar |
| transfer destination/purpose | caller-declared or `not_declared` |

A declared relation such as `supports` remains a communication assertion
Its basis being explicit does not make it scientific entailment

```text
assertion basis != correctness
copied-from-sidecar != independently reverified
recipe-declared support != verified support
```

## No automatic AI detection

Figure evidence emits

```json
{
  "automatic_ai_detection_used": false
}
```

The renderer does not inspect labels, captions, prose, pixels or metadata to infer AI authorship/use
It preserves explicit process disclosure supplied in the recipe

```text
AI disclosure != AI detection
AI detection != authorship adjudication
human review != peer review
```

## Communication coverage

`figure-claim-audit` exposes dimensional coverage including

- figure-level claim count
- valid visual binding count
- distinct visual references
- distinct bound claim IDs
- figure-index claims that have at least one binding
- bindings with direct `evidence_ref`
- bindings with any evidence/audit/provenance context
- `supports` bindings and the subset with evidence context
- process-disclosure fields actually declared

Derived ratios include

```text
indexed_claim_binding_ratio
binding_evidence_context_ratio
supports_evidence_context_ratio
```

These ratios describe **metadata coverage only**

For example

```text
supports_evidence_context_ratio = 1.0
```

means every declared `supports` binding has some declared evidence/audit/provenance reference context

It does **not** mean

- all support relations are correct
- evidence is sufficient
- the figure proves the claim
- the statistical analysis is valid
- the figure is publication-ready
- claim truth probability is 1.0

## No aggregate communication-quality score

The coverage record intentionally emits

```json
{
  "aggregate_score": null
}
```

Binding coverage, evidence-reference presence, accessibility, publisher presets, uncertainty semantics and scientific validity are different dimensions
This repository has no validated basis for combining them into one research-quality number

## Transfer coverage stays separate

`communication-transfer` may report counts or presence for the subset of figure context carried downstream
That transfer coverage is a different descriptive surface from figure claim coverage

```text
transfer coverage != entailment
transfer coverage != publisher readiness
transfer coverage != evidence sufficiency
```

The handoff must retain explicit non-inheritance constraints rather than treating coverage as inherited authority

## Runtime validation remains separate

```text
runtime_validation
  visual/accessibility/artifact/publisher predicates

communication_audit
  claim/process/reference consistency + dimensional coverage

communication_transfer
  bounded downstream copy + non-inheritance constraints
```

These objects are related but not interchangeable proof objects

## Relation to current research-agent work

External research motivates the inspectability goal without defining this repository

- claim-level auditability work treats provenance coverage and contradiction transparency as first-class evaluation concerns
- artifact-centered claim-aware observability argues for portable claim/artifact/verification relations
- trajectory-to-evidence work distinguishes completed execution from qualified evidence
- Brain Researcher emphasizes claims bounded by evidence and methodological alternatives
- EarthVerse demonstrates end-to-end consistency failures even when local steps succeed
- scientific-publishing guidance emphasizes transparency, accountability and human oversight
- long-horizon research work motivates re-validating assumptions and constraints across changing phases

The Sci Render response remains communication-layer specific

> preserve declared claim-to-visual relations, their basis, their coverage, and their downstream constraints without pretending to verify the science

## Current document and maintenance authority

See [DOCUMENT_STATUS.md](../03-maintenance-and-audit/DOCUMENT_STATUS.md) for CURRENT versus HISTORICAL documentation
See [MAINTENANCE_CADENCE.md](../03-maintenance-and-audit/MAINTENANCE_CADENCE.md) for daily / weekly / monthly maintenance semantics
The August stage is closed in [STAGE_2026_08_MAINTENANCE.md](../03-maintenance-and-audit/history/STAGE_2026_08_MAINTENANCE.md)

## Hard boundaries

```text
Assertion basis != correctness
Communication coverage != entailment
Binding coverage != evidence sufficiency
Supports label != proof
Runtime validation != scientific validity
Transfer coverage != inherited validity
Accessibility support != whole-publication WCAG conformance
Publisher profile alignment != acceptance
AI disclosure != authorship adjudication
Human review != peer review
Figure evidence != scientific verification
Calendar-month close != reproduction
```

## The denominator of coverage is not a denominator of truth

`claim_communication_coverage` counts figure-level claim IDs, valid declared bindings, distinct visual references, bound claims, evidence-ref-bearing bindings, and support bindings with any upstream-context string. Those fields are a **coverage inventory**. An upstream-context string may be an opaque, unverified URL or unresolved local pointer; `supports_with_evidence_context_count` is not the count of scientifically demonstrated support relationships.

A useful audit report retains `(declared visual_ref, claim_ref, relation, reference_resolution, upstream claim/audit identity, rendering output, independent source assessment)` as separate fields. Increasing `valid_binding_count` without checking the underlying source can raise metadata coverage while leaving evidence quality unchanged.

Example: if every declared figure claim has a binding but all evidence references are unresolvable, the structural binding ratio may be complete while source sufficiency remains unknown. No aggregate probability or scientific-quality score is computed by the code, and the ratio must not be interpreted as a confidence percentage.
