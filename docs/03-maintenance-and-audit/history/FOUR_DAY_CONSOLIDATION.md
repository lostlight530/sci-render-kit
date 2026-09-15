# Four-Day Consolidation — sci-render-kit

**Window:** 2026-08-24 → 2026-08-27  
**Repository role:** evidence-aware scientific communication plane

## Consolidated outcome

The repository moved from a renderer-centric shape toward a bounded scientific-communication artifact pipeline:

```text
recipe + declared research context
  -> runtime checks
  -> backend-bounded render
  -> manifest / provenance / accessibility
  -> claim communication audit
  -> figure evidence
```

## What became concrete

- explicit research-context and claim-to-visual binding semantics;
- separate runtime-quality and claim-communication audit planes;
- process disclosure for declared AI assistance and human review;
- typed uncertainty semantics;
- stable figure evidence handoff;
- replay-addressable render identity and backend/runtime provenance;
- tighter WCAG 2.2 scope language;
- publisher presets explicitly bounded away from acceptance claims;
- experimental modules described by actual mechanics rather than metaphor.

## Identifier cleanup

Project-owned profile names were normalized to stable identifiers without decorative `@1/@2` or `/v1` suffixes:

```text
sci-render-kit/runtime-quality
sci-render-kit/render-manifest
sci-render-kit/provenance
sci-render-kit/a11y
sci-render-kit/figure-claim-binding
sci-render-kit/figure-claim-audit
sci-render-kit/process-disclosure
sci-render-kit/figure-evidence
```

This cleanup deliberately does **not** erase real external/runtime versions. Actual Matplotlib/NumPy/Python/ggplot2 versions, the pinned Observable Plot dependency, WCAG 2.2, RO-Crate 1.3 and CFF 1.2.0 remain legitimate evidence when applicable.

## Non-hallucination rule

Unknown metadata remains unknown. The repository must not invent provider/model/version/source/review/validation state simply to make an evidence object look complete.

## Scientific boundary

```text
render success != scientific truth
claim binding != verified entailment
runtime validation != scientific validity
human review != peer review
publisher alignment != acceptance
provenance != truth
checksum != reproduction
```

## Maintenance boundary

No GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge-gate architecture were added as part of this consolidation. Local checks remain optional maintenance aids rather than scientific evidence.
