# Agent Guide — sci-render-kit

This is the operational contract for agents modifying the repository. Keep runtime code, schemas, profiles, evidence sidecars and public documentation semantically aligned.

## Canonical architecture

```text
recipe
  -> P0 schema
  -> P1 runtime + claim communication audit
  -> backend capability resolution
  -> render
  -> render-manifest / provenance / a11y
  -> P2 artifact integrity
  -> P3 publisher-target alignment
  -> figure-evidence
```

## Stable project identifiers

Use these names exactly:

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

Do not invent `@1`, `@2`, `/v1` or similar internal counters. If compatibility ever needs explicit versioning, define a real compatibility policy first.

Real external/runtime versions are different: keep WCAG 2.2, RO-Crate 1.3, CFF 1.2.0 and actual backend/library/runtime versions when they are genuinely observed.

## Hard rules

1. **Schema ≠ backend support.** Do not advertise behavior until a backend actually implements it.
2. **No hidden overrides.** Do not silently change DPI, format, uncertainty semantics or declared data.
3. **Claim bindings are explicit only.** Never infer visual-to-claim relations from titles, legends, pixels, labels, prose or data values.
4. **Claim relation ≠ entailment.** `supports`, `illustrates` and related labels are communication declarations, not verified scientific inference.
5. **Process disclosure is bounded.** Tool/model/provider identifiers and human review do not adjudicate authorship, peer review, truth or publisher compliance.
6. **Unknown stays unknown.** Missing provider/model/version/review/source metadata remains `null`, absent or `not_declared`; never guess.
7. **Uncertainty must be typed.** Bounds alone are not a confidence interval or probability model.
8. **WCAG scope must stay exact.** SC 1.4.11 is not a universal all-palette-pairs rule; project all-pairs checks are extra safeguards.
9. **CVD simulation is extra.** Do not describe it as a normative WCAG test.
10. **Publisher presets are snapshots.** They are not acceptance validators.
11. **Matplotlib extension model stays explicit.** Use function injection rather than hidden global monkeypatching.
12. **Optional ecosystems stay optional.** R/Node adapter source does not prove runtime availability.
13. **Figure evidence is handoff, not truth.** Upstream references are not independently scientifically validated by the renderer.
14. **No fake algorithms.** Unsupported experimental methods must fail explicitly rather than fabricate output.
15. **Experimental stays Experimental.** Importability does not promote a module into canonical capability.
16. **No GitHub governance creep.** Do not add Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge-gate architecture.

## Change ownership

| Goal | Primary files | Synchronize |
|---|---|---|
| recipe field | `metadata/recipe.schema.yaml` | runtime + docs + evidence semantics |
| claim binding/audit | `core/claim_binding_audit.py`, `core/figure_evidence.py` | Figure Claim Contract + Manifest |
| process disclosure | recipe schema + figure evidence | public contracts |
| runtime rule | `quality/rules.yaml`, `sci_render.py` | severity + docs |
| accessibility | `core/accessibility.py`, `sci_render.py` | a11y profile + backend truth |
| Matplotlib | `backends/matplotlib_base.py`, adapter | manifest/provenance semantics |
| ggplot2 | `backends/ggplot2_adapter.R` | manifest/runtime boundary |
| Observable | `backends/observable_adapter.js` | pinned real dependency + network boundary |
| publisher profile | `profiles/*.yaml` | source status + acceptance false |
| public capability | README / Architecture / Contracts / Manifest | update together |

## Cross-repository references

Preferred stable names:

```text
auto-doc-engine/artifact-record
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
```

These are optional handoff references, not direct runtime coupling.

## Experimental semantics

- `projection`: PCA/projection metrics; t-SNE not implemented here;
- `uncertainty_legend`: typed uncertainty metadata;
- `superposition`: deterministic variant layering;
- `time_crystal`: periodic waveform utility;
- `observer_dashboard`: caller-fed telemetry.

Never use metaphorical filenames as evidence of scientific capability.

## Local maintenance

Local commands may be used manually when useful. Their success is not evidence of scientific validity, real-provider behavior, publisher acceptance or independent reproduction.
