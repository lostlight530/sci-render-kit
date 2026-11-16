# 02 — Examples and Contracts

## 中文专业正文对照 / Chinese technical counterpart

**具体研究对象 / Concrete subject:** 本索引划清 Figure Claim、Communication Transfer 与 Runtime/Schema 验证的拥有关系

**English owning title:** 02 — Examples and Contracts

**图像证据判别 / Figure evidence reading:** 应分别取得源数据版本、recipe/profile、实际后端输出、manifest、声明绑定、上游 sidecar 与可访问性实测结果，不能将图像 bytes、示例文档或测试定义视为实际同行评审 / Keep source, recipe, backend, manifest and claim identities separate, verify the exact execution evidence before asserting quality or reproducibility

| English original section / 英文原章 | 中文对应定位 / Chinese section meaning |
| --- | --- |
| Machine and configuration surfaces | 该图像合同的局部机制与证据限制 |
| Active contracts | 该图像合同的局部机制与证据限制 |
| Publisher, accessibility, uncertainty, and backend boundaries | 该图像合同的局部机制与证据限制 |
| Cross-repository role | 该图像合同的局部机制与证据限制 |
| Operator and contributor surfaces | 该图像合同的局部机制与证据限制 |
| Scholarly metadata | 该图像合同的局部机制与证据限制 |
| Reading path | 该图像合同的局部机制与证据限制 |
| Tool CLI / Offline Evidence Console | 该图像合同的局部机制与证据限制 |

**限界 / Limits:** 原有配置、图形行为与未知执行状态保持不变，本节不新增科学审定、出版接纳、WCAG 认证或真实浏览器通过声明 / Original behaviors and unknown states are unchanged, no scientific or publisher certification is implied


This class answers: **how are recipes, figure claims, communication evidence, profiles, coverage, and downstream transfer constrained and interpreted?**

## Machine and configuration surfaces

- root `MANIFEST.yaml` — machine-readable capability map.
- `metadata/` — declared metadata structures and supporting configuration.
- `profiles/` — publisher/output target profiles and constraints.
- `quality/` — repository-owned quality/checking rules.
- `recipes/` — declarative rendering inputs and supported communication structure.
- `examples/` — worked supported-use examples.

A machine-readable profile or successful structural check does not establish publisher acceptance, scientific validity, statistical validity, or accessibility certification.

## Active contracts

### [`RESEARCH_CONTRACT.md`](./RESEARCH_CONTRACT.md)

Repository-wide scientific-communication semantics and reproduction/evidence boundaries. Start here when interpreting what a render, audit, or communication artifact can actually support.

### [`FIGURE_CLAIM_CONTRACT.md`](./FIGURE_CLAIM_CONTRACT.md)

Defines explicit figure-to-claim relationships and bounded claim auditing.

```text
claim bound to figure != claim entailed by figure
supports relation != proof
coverage != scientific validity
```

A figure can reference or communicate a claim without proving it.

### [`COMMUNICATION_TRANSFER_CONTRACT.md`](./COMMUNICATION_TRANSFER_CONTRACT.md)

Defines bounded transfer of communication/evidence metadata across repository or publication contexts.

Transfer must not silently inherit scientific validity, entailment, evidence sufficiency, statistical validity, peer review, publisher acceptance, or accessibility conformance.

### [`ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md`](./ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md)

Separates field assertion/observation basis from correctness and separates communication coverage from quality, entailment, probability, or evidence sufficiency.

```text
assertion basis != correctness
communication coverage != entailment
coverage ratio != probability
```

## Publisher, accessibility, uncertainty, and backend boundaries

Keep these properties independent:

```text
publisher profile satisfied != publisher accepted
accessibility metadata/support != WCAG certified
uncertainty field present != statistically validated uncertainty
backend adapter source != backend runtime available
render completed != scientific claim valid
```

Unknown publisher/review/backend/accessibility/validation state remains unknown unless directly observed at the relevant surface.

### [FIGURE_CLAIM_NEGATIVE_CASES.md](./FIGURE_CLAIM_NEGATIVE_CASES.md)

A source-derived suite of bounded negative cases for this repository's **own** evidence objects, with exact implementation owners, falsification inputs, excluded claims, and `NOT_EXECUTED` status, it does not change runtime behavior or inherit scientific validity

## Cross-repository role

In the research-infrastructure chain:

```text
auto-doc-engine artifact identity/lineage
        ↓
epistemic-pipeline claim/evidence semantics
        ↓
sci-render-kit communication and figure evidence
```

sci-render-kit is a communication layer. It must not upgrade upstream claim strength merely because evidence is rendered clearly or packaged into a publication-oriented figure.

## Operator and contributor surfaces

- root `AGENTS.md` — repository-owned operational guidance.
- root `CONTRIBUTING.md` — public contribution guidance.
- `examples/`, `profiles/`, and `recipes/` — supported representation/configuration surfaces.

These are constrained by current implementation, `MANIFEST.yaml`, and active contracts.


### [INTEROPERABILITY_VERIFICATION.md](./INTEROPERABILITY_VERIFICATION.md)

Current producer/consumer fixture scope, Python environment pins, CodeMeta 4 migration boundaries, and (where applicable) failure injection or offline renderer verification — evidence of a test is separate from its execution

## Scholarly metadata

- root `CITATION.cff`
- root `codemeta.json`
- root `RELEASE_POLICY.md`
- root `LICENSE`

The repository DOI identifies an archived software publication. It is not evidence that any produced figure is scientifically valid, accepted by a publisher, WCAG conformant, or independently reproduced.

## Reading path

For a new figure/communication integration:

1. identify the owning renderer/backend/configuration and `MANIFEST.yaml` capability;
2. read `RESEARCH_CONTRACT.md` for repository-wide meaning;
3. read the figure/transfer/assertion contract relevant to the object;
4. inspect the exact profile/recipe/example being used;
5. retain revision-matched execution evidence when reporting render/audit success;
6. keep scientific claim support and publication/accessibility status separately sourced.

Architecture and implementation explanation live under [`../01-source-and-explanation/`](../01-source-and-explanation/). Maintenance/audit material in class 03 is operational/historical context, not scientific validity.

## Tool CLI / Offline Evidence Console

- [TOOL_CLI_AGENT.md](TOOL_CLI_AGENT.md) — current allowlisted Tool/CLI/Agent plan semantics, approval, and execution evidence boundaries
- [TOOL_UI_STYLE.md](TOOL_UI_STYLE.md) — offline multi-repository receipt viewer, responsive UI tokens and validation limits
