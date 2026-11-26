> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `CONTRACT`
> - **Role:** Current bounded scientific-communication transfer contract
> - **Authority:** Current repository-native authority for the scientific-communication semantics explicitly owned by this file; current renderer/runtime and machine contracts remain the executable-behavior boundary
> - **Current meaning:** Read this subject inside the `declared recipe/data → communication audit → render → figure evidence → bounded transfer` chain. It preserves what a figure declares and how that declaration was recorded without silently upgrading communication into scientific proof
> - **Evidence / implementation boundary:** Render success is not scientific truth; a `supports` binding is not entailment; communication coverage is not evidence sufficiency or probability; uncertainty metadata is not statistical validation; accessibility support is not WCAG certification; publisher profile alignment is not acceptance; downstream transfer does not inherit validity
> - **Cross-document relation:** Architecture integrates the full figure pipeline; specialized contracts own binding/coverage/transfer semantics; current code and machine contracts bound implementation; `DOCUMENT_STATUS.md` separates current contracts from historical snapshots
> - **Update trigger:** Update when owned figure/evidence/transfer semantics or implemented mechanics materially change, or when a confirmed current-authority conflict appears
> - **Preservation rule:** Existing technical content and dated stage calibration remain intact. Historical stage-close or research-language passages retain their own evidence boundary

# Scientific Communication Transfer Contract — sci-render-kit

## 中文专业正文对照 / Chinese technical counterpart

**具体研究对象 / Concrete subject:** 视觉传播只传递来源声明和有限上下文，不继承上游 Claim 的真值、同行评审或 R3 复现

**English owning title:** Scientific Communication Transfer Contract — sci-render-kit

**图像证据判别 / Figure evidence reading:** 应分别取得源数据版本、recipe/profile、实际后端输出、manifest、声明绑定、上游 sidecar 与可访问性实测结果，不能将图像 bytes、示例文档或测试定义视为实际同行评审 / Keep source, recipe, backend, manifest and claim identities separate, verify the exact execution evidence before asserting quality or reproducibility

| English original section / 英文原章 | 中文对应定位 / Chinese section meaning |
| --- | --- |
| Purpose | 目标 |
| Stable profile | 该图像合同的局部机制与证据限制 |
| Source semantics | 来源语义 |
| Reproducibility-context preservation | 该图像合同的局部机制与证据限制 |
| Transfer constraints | 传递条件 |
| Transfer coverage | 该图像合同的局部机制与证据限制 |
| Assertion basis | 该图像合同的局部机制与证据限制 |
| CLI | 该图像合同的局部机制与证据限制 |
| Relationship to figure evidence | 该图像合同的局部机制与证据限制 |
| Machine-readable contract | 该图像合同的局部机制与证据限制 |
| Cross-repository context | 该图像合同的局部机制与证据限制 |
| Current maintenance authority | 该图像合同的局部机制与证据限制 |
| Global calibration | 该图像合同的局部机制与证据限制 |

**限界 / Limits:** 原有配置、图形行为与未知执行状态保持不变，本节不新增科学审定、出版接纳、WCAG 认证或真实浏览器通过声明 / Original behaviors and unknown states are unchanged, no scientific or publisher certification is implied


**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-09-01  
**Implementation:** `core/communication_transfer.py`

## Purpose

`sci-render-kit/communication-transfer` summarizes an existing `sci-render-kit/figure-evidence` sidecar for downstream publication, archival, review or agent workflows.

The transfer exists so a figure does not travel downstream as only an image path or claim ID. It keeps communication context that is easy to lose:

```text
claim refs
visual-to-claim bindings
upstream evidence / claim-audit / provenance refs
uncertainty semantics
process disclosure
communication-audit summary
runtime-validation summary
reproducibility context
```

## Stable profile

```text
sci-render-kit/communication-transfer
```

Project-owned identifiers remain unversioned. Real external/runtime versions remain explicit only when genuinely observed or specified.

## Source semantics

The source figure-evidence file is locally byte-identified with SHA-256. Destination and purpose are caller-declared when supplied.

No relationship is inferred from filenames, image pixels, captions, legends or prose.

The optional `claim_communication.bindings` collection must be an array of JSON objects when supplied. Malformed collections fail explicitly rather than silently dropping declared bindings or reporting a misleading zero binding count.

The optional `claim_communication.claim_refs` collection accepts omission or null; a supplied non-null value must be an array of nonempty strings. Existing trimming and deduplication remain unchanged. If supplied, `claim_communication.inferred_bindings` must be a JSON boolean; omission retains the previous false default. Explicit null and non-boolean flags fail instead of being converted. These checks precede transfer and coverage calculation; they do not infer bindings, resolve references, or establish entailment.

```text
source hash != semantic equivalence
caller-declared destination != publication acceptance
```

## Reproducibility-context preservation

As of 2026-09-01, the transfer copies the figure-evidence `reproducibility` object rather than dropping it at the communication boundary.

Current figure evidence uses local project semantics such as:

```text
R1 = replay-addressable render inputs/artifact identity
R3 = requires an actual separate rerun and declared comparison criterion
```

The transfer preserves that context but explicitly refuses stronger inheritance:

```text
independent_reproduction_inherited: false
independent_reproduction_claim: false
```

```text
reproducibility metadata copied != rerun executed
R1 context preserved != R3 achieved
source reproducibility label != downstream independent reproduction
```

## Transfer constraints

The handoff explicitly carries:

```text
scientific_validity_inherited: false
entailment_inherited: false
evidence_sufficiency_inherited: false
statistical_validity_inherited: false
peer_review_inherited: false
publisher_acceptance_inherited: false
accessibility_conformance_inherited: false
independent_reproduction_inherited: false
```

A downstream publication/review system receives communication metadata without silently inheriting authority the renderer never established.

## Transfer coverage

The record reports counts/presence for claim refs, bindings, upstream research context, process disclosure, uncertainty semantics, communication audit, runtime validation, and reproducibility context.

```text
reproducibility_context_present: true | false
aggregate_score: null
```

Presence is descriptive only. It does not mean independent reproduction occurred.

## Assertion basis

```text
source figure-evidence identity
  -> runtime-observed-local-bytes

transferred figure context
  -> copied-from-local-figure-evidence-sidecar

reproducibility context
  -> copied-from-local-figure-evidence-sidecar

destination / purpose
  -> caller-declared | not_declared

basis_inferred
  -> false
```

```text
copied-from-sidecar != independently reverified
assertion basis != correctness
```

## CLI

```bash
python core/communication_transfer.py \
  output/figure.evidence.json \
  --destination manuscript-main-text \
  --purpose publication-handoff \
  --output output/figure.communication-transfer.json
```

## Relationship to figure evidence

```text
figure-evidence
        ↓ bounded copy / transfer constraints
communication-transfer
        ↓
publication / review / archive / agent workflow
```

The transfer does not replace the full figure evidence sidecar. It is a portable handoff view.

## Machine-readable contract

The machine companion is:

```text
metadata/communication_transfer.contract.yaml
```

The machine contract and this document must stay semantically aligned.

## Cross-repository context

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
        ↓
sci-render-kit/communication-transfer
```

The chain is a handoff path, not a chain of inherited scientific authority.

## Current maintenance authority

Current document authority is indexed in `DOCUMENT_STATUS.md`. The August scientific-communication phase closed on 2026-08-31; the 2026-09-01 repair hardens current handoff fidelity without reopening that stage.

## Global calibration

Current long-horizon and scientific-agent work reinforces keeping constraints and intermediate state visible across handoffs. The 2026-09-01 repair applies that principle narrowly to reproducibility semantics: a downstream consumer should not lose the difference between replay-addressable evidence and an actually reproduced result.

These works are design calibration only. They do not certify this repository or make declared visual relations scientifically valid.

## Hard boundaries

```text
Communication transfer != Entailment
Claim binding != Claim truth
Upstream reference != Inherited validity
Uncertainty metadata != Statistical validation
Reproducibility context != Independent reproduction
Accessibility metadata != WCAG certification
Publisher target != Acceptance
Human review != Peer review
Provenance != Truth
Calendar-month close != Reproduction
```


## Input-shape validation — 2026-10-23

The implementation added by merged PR [#163](https://github.com/lostlight530/sci-render-kit/pull/163) validates copied optional context before reading nested fields or calculating transfer-coverage metrics:

- The sidecar root must be a JSON object and its `profile` must equal `sci-render-kit/figure-evidence`
- Each supplied non-null context field — `claim_communication`, `upstream_research`, `uncertainty`, `process_disclosure`, `communication_audit`, `runtime_validation`, and `reproducibility` — must itself be a JSON object
- Omitted or explicit `null` fields retain the existing not-declared semantics
- Arrays, strings, numbers, booleans, and other non-object non-null values are rejected with an explicit `ValueError`; the tool adapter reports `EXECUTION_FAILED` rather than producing a partial transfer
- Validation runs before transfer-coverage calculation, and the input sidecar is not mutated

This is structural input validation only. It does not validate the scientific meaning or sufficiency of copied content, and does not upgrade source authority, entailment, statistical validity, peer review, publisher acceptance, accessibility conformance, or independent reproduction. The implementation's existing PR #163 `local-tool-contract` workflow passed; this dated contract reconciliation does not claim a new local test execution.

## Fail-closed shape validation versus inherited scientific status

`core/communication_transfer.py::_load_json` requires source profile `sci-render-kit/figure-evidence`. It rejects supplied non-object nested sections for claim communication, upstream research, uncertainty, process disclosure, communication audit, runtime validation and reproducibility; if `claim_communication.bindings` is supplied it must be an array of objects. Missing/null sections preserve unreported state.

A valid transfer copies claim references/bindings and structured upstream, uncertainty, disclosure, audit and validation fields. `source_figure_evidence.file_sha256` hashes the local figure-evidence sidecar bytes; it is not a signature of the original data, source proposition, publisher or human reviewer. `destination` and `purpose` are caller-supplied, not evidence that a downstream organization accepted the object.

**Counterexample:** a source sidecar declares `uncertainty.kind` and supplies reproducibility metadata, but contains no raw measurement validation or independent reproduction. The transfer may truthfully report both fields as present. It must not inherit statistical validity, R3 reproduction, accessibility conformance, peer review or publisher acceptance.
