# Sci Render Kit Scientific Closure Design — Historical Record

Date: 2026-08-05  
Status: **SUPERSEDED on 2026-08-24**  
Historical base: `main@a193ddc0013dda2524f8ff10910eee86633708d5`

## Why this file remains

This document records an earlier design direction. It is retained for historical context only and must not be treated as the current maintenance contract.

The active architecture is now defined by:

- `README.md`
- `ARCHITECTURE.md`
- `RESEARCH_CONTRACT.md`
- `MANIFEST.yaml`
- `AGENTS.md`
- `quality/rules.yaml`

## Historical objective

The 2026-08-05 design aimed to make the declarative scientific-rendering toolkit more truthful, backend-aware and reproducible while preserving the public CLI and existing recipe/profile paths.

Useful ideas from that design remain part of the current repository:

- validate declared structures before rendering;
- fail explicitly on unsupported backend capabilities;
- bind artifacts to stable content identities;
- keep scientific claims narrower than implementation evidence;
- separate optional ecosystems from verified runtime evidence;
- prevent experimental modules from masquerading as production capabilities.

## Superseded decisions

The earlier design also proposed repository-specific GitHub governance, cloud verification, CodeQL, dependency-maintenance workflows, and merge acceptance tied to cloud checks.

Those proposals are **retired** for the current architecture.

Current maintenance policy intentionally does not require:

```text
GitHub Actions
CI
CodeQL
dependency bots
branch-protection assumptions
merge gates
cloud-check acceptance
```

P0–P3 now mean **runtime figure-validation phases**, not repository-hosting gates.

## 2026-08-24 replacement architecture

The active data flow is:

```text
recipe + research context + uncertainty semantics
  -> P0 schema
  -> P1 runtime findings (error/warning/info)
  -> backend capability resolution
  -> backend render
  -> render-manifest@2 / provenance@2 / a11y@1
  -> P2 artifact integrity
  -> P3 publisher-target alignment
  -> figure-evidence@1
```

Key differences from the historical design:

- one boolean quality-gate model has been replaced by structured runtime findings;
- publisher profile checks are target-alignment evidence, not compliance certification;
- uncertainty semantics are explicit and cannot be inferred from bounds alone;
- figure-level evidence has a versioned handoff profile;
- experimental physics metaphors are bounded to actual deterministic utilities;
- fake t-SNE/constant projection metrics are not acceptable placeholders;
- Matplotlib accessibility behavior uses explicit function injection rather than global monkeypatching;
- Observable HTML records its pinned CDN/network dependency;
- no completion claim depends on running GitHub/cloud tests.

## Historical security/failure notes retained where applicable

The earlier preference for explicit failure, bounded execution, path hygiene and no arbitrary dynamic execution remains good engineering guidance when those concerns apply to current code.

However, a security or reliability guideline should be implemented in the relevant runtime code rather than converted into a generic repository-hosting gate by default.

## Scientific integrity

Current hard boundaries:

```text
Render success ≠ scientific truth
Runtime validation ≠ scientific validity
Publisher alignment ≠ journal acceptance
Provenance ≠ truth
Checksum ≠ reproduction
Accessibility sidecar ≠ whole-publication WCAG conformance
```

## Historical status

No further implementation should be planned from this file without first reconciling it against the active 2026-08-24 architecture documents.
