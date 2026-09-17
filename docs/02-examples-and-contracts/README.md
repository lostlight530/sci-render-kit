# 02 — Examples and Contracts

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
