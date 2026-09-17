# 01 — Source and Explanation

This class answers three durable questions:

1. **What does sci-render-kit actually implement?**
2. **Where are renderer/backend and scientific-communication boundaries explained?**
3. **Which successful outputs are engineering/render evidence rather than scientific validation?**

## Implementation map

| Surface | Repository role | Boundary |
|---|---|---|
| root `sci_render.py` | public/CLI rendering entry surface | successful invocation does not certify the scientific meaning of a figure |
| `core/` | recipe interpretation, communication/evidence logic, repository-owned rendering rules | implemented predicates remain narrower than scientific validity |
| `backends/` | backend adapters and backend-specific behavior | backend source presence != backend runtime availability in every environment |
| `tests/` | revision-scoped engineering/regression evidence | passing tests do not prove entailment, publisher acceptance, or accessibility conformance |
| root `Makefile` | supported engineering command entry points | command presence != command execution |
| root `package.json` | declared JavaScript/tooling metadata where applicable | declaration/installability != successful execution |

The maintenance scanner remains implementation source even when it supports class 03 materials. Scanner source is not scanner execution.

## Architecture and explanation

- root [`README.md`](../../README.md) — public repository entry point and capability overview.
- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — detailed renderer/backend architecture, schema/profile/quality relationships, communication integrity boundaries, and cross-repository handoff context.

Implementation and revision-matched execution own actual renderer behavior. README and Architecture explain that behavior; they do not upgrade it.

## Scientific-communication boundaries

Keep these distinctions explicit:

```text
render success != scientific validity
claim binding != entailment
uncertainty metadata != statistical validation
publisher profile/alignment != publisher acceptance
accessibility metadata/support != WCAG certification
backend adapter present != backend available
```

A generated figure can be structurally correct for a declared recipe while the underlying scientific claim, data provenance, uncertainty interpretation, or publication status remains unverified.

## Cross-layer reading

Machine/configuration surfaces such as `metadata/`, `profiles/`, `quality/`, and `recipes/` are routed with the active contracts in class 02 because they constrain supported communication behavior. Their presence does not by itself prove a runtime backend, publication acceptance, or scientific correctness.

The documents under [`../02-examples-and-contracts/`](../02-examples-and-contracts/) define figure-claim, communication-transfer, assertion-basis, and research-contract semantics.

Current document taxonomy is routed from [`../README.md`](../README.md). Class 03 maintenance/audit material is operational/historical context and does not own figure validity.
