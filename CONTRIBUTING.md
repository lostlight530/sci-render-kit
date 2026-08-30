# Contributing

Contributions should strengthen explicit scientific-figure semantics rather than only increase renderer/module count

## Repository boundaries

Keep changes scoped to the owning layer: recipe schema, runtime rules, backend adapter, accessibility, publisher preset, claim communication, assertion basis, communication coverage, figure evidence, communication transfer, maintenance or documentation

Do not introduce GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge-gate architecture as ordinary maintenance

## Current document authority

Before changing repository semantics, read [DOCUMENT_STATUS.md](DOCUMENT_STATUS.md)

Current contracts are authoritative for present behavior
Historical `*_DAY_CONSOLIDATION.md` files are snapshots of earlier stages and must not be silently rewritten into current truth

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

## Stable internal identifiers

Project-owned profiles use stable unversioned names
Real external standards and observed runtime/library versions remain legitimate provenance when known

Do not add decorative internal `@1/@2` or `/v1` counters unless a real compatibility regime is deliberately introduced

## Scientific integrity

Do not present schema success, render success, runtime findings, claim bindings, checksums/provenance, human-review declarations, communication coverage, communication transfer, publisher-preset alignment, accessibility sidecars or visual similarity as scientific validation

Unknown metadata stays unknown
Never invent provider, model, version, source, review or validation status

## Assertion-basis rule

New evidence fields should state how their values were obtained when this repository can know that honestly

Examples

```text
recipe-declared
runtime-observed-local-bytes
runtime-observed-local-filesystem
recipe-declared-with-optional-local-resolution
copied-from-local-figure-evidence-sidecar
caller-declared
```

```text
assertion basis != correctness
```

Do not add AI-text/pixel inference to process disclosure unless a separate explicit detector architecture is designed
The current canonical path records `automatic_ai_detection_used: false`

## Communication-coverage rule

Coverage stays dimensional and transparent

```text
binding counts
claim-index/binding coverage
evidence-context coverage
supports evidence-context coverage
process-disclosure field coverage
```

Do not manufacture a composite research-quality score

```text
communication coverage != entailment
coverage ratio != probability
coverage != provenance soundness
reference context != evidence sufficiency
```

`aggregate_score` remains `null` under the current contract

## Communication-transfer rule

When changing `core/communication_transfer.py`, preserve

```text
scientific_validity_inherited: false
entailment_inherited: false
evidence_sufficiency_inherited: false
statistical_validity_inherited: false
peer_review_inherited: false
publisher_acceptance_inherited: false
accessibility_conformance_inherited: false
```

A transfer must not infer destination, publication status, review authority or claim meaning from filenames, captions, pixels or prose

Synchronize

```text
COMMUNICATION_TRANSFER_CONTRACT.md
metadata/communication_transfer.contract.yaml
RESEARCH_CONTRACT.md
MANIFEST.yaml
examples/README.md
FRONTIER_ALIGNMENT.md
```

## Compatibility

When changing a public field or semantic, update code, machine-readable contracts, Figure Claim Contract, Assertion Basis contract, Manifest, examples and public documentation together
Prefer explicit additive changes over silent reinterpretation

## Cross-repository semantics

Do not strengthen upstream references silently

```text
artifact/claim ref -> trusted evidence       # prohibited
claim audit coverage -> scientific validity # prohibited
human review -> peer review                 # prohibited
supports relation -> proof                  # prohibited
claim transfer -> accepted claim            # prohibited
```

Current handoff vocabulary includes

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

## Daily / weekly / monthly maintenance

The active cadence contract is [MAINTENANCE_CADENCE.md](MAINTENANCE_CADENCE.md)

```text
daily
  local demonstrated drift only

weekly
  current implementation / machine contract / documentation reconciliation

monthly or explicit phase-close
  calendar baseline + history inventory + manual deprecation review
```

On 2026-08-31 the August calendar month and the 2026-08 research-maintenance phase are explicitly closed

```text
maintenance clean != scientific validity
weekly consistency != entailment
calendar-month close != reproduction
```

The local maintenance scanner is evidence about configured repository structure only
It is not a test suite, publisher validator or scientific-review engine

## Local maintenance

Local checks may be run manually when useful, but they are not repository governance and are not scientific evidence

## License

Contributions are licensed under the repository license
