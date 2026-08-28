# Contributing

Contributions should strengthen explicit scientific-figure semantics rather than only increase renderer/module count.

## Repository boundaries

Keep changes scoped to the owning layer: recipe schema, runtime rules, backend adapter, accessibility, publisher preset, claim communication, assertion basis, communication coverage, evidence sidecar or documentation.

Do not introduce GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge-gate architecture as ordinary maintenance.

## Stable internal identifiers

Project-owned profiles use stable unversioned names. Real external standards and observed runtime/library versions remain legitimate provenance when known.

## Scientific integrity

Do not present schema success, render success, runtime findings, claim bindings, checksums/provenance, human-review declarations, communication coverage, publisher-preset alignment, accessibility sidecars or visual similarity as scientific validation.

Unknown metadata stays unknown. Never invent provider, model, version, source, review or validation status.

## Assertion-basis rule

New evidence fields should state how their values were obtained when this repository can know that honestly.

Examples:

```text
recipe-declared
runtime-observed-local-bytes
runtime-observed-local-filesystem
recipe-declared-with-optional-local-resolution
```

```text
assertion basis != correctness
```

Do not add AI-text/pixel inference to process disclosure unless a separate explicit detector architecture is designed; the current canonical path records `automatic_ai_detection_used: false`.

## Communication-coverage rule

Coverage stays dimensional and transparent:

```text
binding counts
claim-index/binding coverage
evidence-context coverage
supports evidence-context coverage
process-disclosure field coverage
```

Do not manufacture a composite research-quality score.

```text
communication coverage != entailment
coverage ratio != probability
coverage != provenance soundness
reference context != evidence sufficiency
```

`aggregate_score` remains `null` under the current contract.

## Compatibility

When changing a public field or semantic, update code, machine-readable contracts, Figure Claim Contract, Assertion Basis contract, Manifest, examples and public documentation together. Prefer explicit additive changes over silent reinterpretation.

## Cross-repository semantics

Do not strengthen upstream references silently:

```text
artifact/claim ref -> trusted evidence       # prohibited
claim audit coverage -> scientific validity # prohibited
human review -> peer review                 # prohibited
supports relation -> proof                  # prohibited
```

## Local maintenance

Local checks may be run manually when useful, but they are not repository governance and are not scientific evidence.
