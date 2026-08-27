# Contributing

Contributions should strengthen explicit scientific-figure semantics rather than only increase renderer or module count.

## Repository boundaries

Keep changes scoped to the layer that owns them: recipe schema, runtime rules, backend adapter, accessibility, publisher preset, claim communication, evidence sidecar or documentation.

Do not introduce GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge-gate architecture as part of ordinary maintenance.

## Stable internal identifiers

Project-owned profiles use stable names such as:

```text
sci-render-kit/render-manifest
sci-render-kit/provenance
sci-render-kit/a11y
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

Do not append decorative `@1/@2` or `/v1` suffixes. Real external standards and observed runtime/library versions remain legitimate provenance and should be recorded when known.

## Scientific integrity

Do not present any of the following as scientific validation:

- schema success;
- render success;
- runtime findings passing;
- claim bindings;
- checksums or provenance;
- human-review declarations;
- publisher-preset alignment;
- accessibility sidecars;
- numerical or visual similarity.

Unknown metadata stays unknown. Never invent provider, model, version, source, review or validation status.

## Compatibility

When changing a public field or profile semantic, update code, machine-readable contracts and public documentation together. Prefer additive/explicit changes over silent reinterpretation.

## Local maintenance

Local checks may be run manually when useful, but they are not repository governance and are not scientific evidence.
