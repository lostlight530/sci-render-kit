# Agent Guide — sci-render-kit

This is the operational contract for agents modifying the repository
Keep runtime code, schemas, profiles, evidence sidecars, maintenance records, and public documentation semantically aligned

## Canonical architecture

```text
recipe
  -> P0 schema
  -> P1 runtime + claim communication audit
       ├─ assertion basis
       └─ dimensional communication coverage
  -> backend capability resolution
  -> render
  -> render-manifest / provenance / a11y
  -> P2 artifact integrity
  -> P3 publisher-target alignment
  -> figure-evidence
  -> optional communication-transfer
       └─ explicit non-inheritance constraints
```

## Stable project identifiers

```text
sci-render-kit/runtime-quality
sci-render-kit/render-manifest
sci-render-kit/provenance
sci-render-kit/a11y
sci-render-kit/figure-claim-binding
sci-render-kit/figure-claim-audit
sci-render-kit/process-disclosure
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
sci-render-kit/maintenance-cadence
sci-render-kit/maintenance-report
```

Do not invent decorative internal versions
Preserve real WCAG/external/runtime versions when genuinely known

## Hard rules

1. Schema does not imply backend support
2. Do not silently change DPI, format, uncertainty semantics, or declared data
3. Claim bindings are explicit only and are never inferred from titles, legends, pixels, prose, or data values
4. Claim relation labels are communication declarations, not verified entailment
5. Process disclosure is bounded and does not adjudicate authorship, peer review, or truth
6. Unknown provider/model/version/review/source metadata remains unknown
7. The canonical renderer does not perform AI-text/pixel detection to infer AI authorship/use
8. Assertion basis records how a field entered evidence and never upgrades a value to correctness
9. Communication coverage remains dimensional and must not become an unsupported aggregate quality score
10. Coverage ratios are not probability, entailment, evidence sufficiency, or provenance soundness
11. Bounds alone are not a confidence interval or probability model
12. WCAG scope stays exact and project all-pairs checks remain extra safeguards
13. CVD simulation is extra and not a normative WCAG certification test
14. Publisher presets are snapshots/config targets, not acceptance validators
15. Matplotlib extension remains explicit and must avoid hidden monkeypatching
16. Optional R/Node source does not prove runtime availability
17. Figure evidence is handoff, not truth
18. Communication transfer may copy declared context but must not inherit scientific validity, entailment, evidence sufficiency, statistical validity, peer review, publisher acceptance, or WCAG conformance
19. Communication transfer must not infer context from pixels, captions, filenames, or prose
20. Unsupported experimental methods fail explicitly rather than fabricate output
21. Experimental importability does not make canonical capability
22. Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge-gate architecture

## Communication-audit invariants

`core/claim_binding_audit.py` may record findings plus coverage dimensions such as binding counts and evidence-context ratios

```text
assertion basis != correctness
communication coverage != entailment
coverage ratio != probability
supports evidence-context coverage != evidence sufficiency
coverage != provenance soundness
```

Keep `aggregate_score: null` unless a future validated evaluation design explicitly justifies a composite score

## Communication-transfer invariants

`core/communication_transfer.py` is a bounded view over an existing figure-evidence sidecar

It may carry

```text
claim communication
upstream research refs
uncertainty semantics
process disclosure
communication audit
runtime validation
```

Required boundaries

```text
transfer != entailment
upstream ref != inherited validity
uncertainty metadata != statistical validation
publisher target != acceptance
accessibility metadata != WCAG certification
human review != peer review
```

Destination and purpose are caller-declared when present and must not be inferred

## Maintenance cadence

`MAINTENANCE_CADENCE.md` and `maintenance/cadence.yaml` define the active daily / weekly / monthly maintenance contract

Local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of YYYY-MM-DD
```

Daily maintenance

- start from current `main`
- correct demonstrated recipe/evidence/backend/profile drift only
- preserve explicit claim bindings, uncertainty labels, WCAG scope, publisher boundaries, and real runtime versions
- do not rewrite historical snapshots or invent a daily feature

Weekly maintenance

- reconcile implementation, machine contracts, Research Contract, Figure Claim Contract, Communication Transfer Contract, Agent Guide, Frontier Alignment, and upstream profile names
- review backend capability truth, uncertainty semantics, WCAG scope, publisher wording, and communication-transfer non-inheritance
- inventory the prior seven days of stage snapshots without rewriting them

Monthly or explicit phase-close maintenance

- build a month-to-date or explicit phase-close canonical hash baseline
- inventory historical snapshots and review deprecation candidates manually
- confirm no publisher/accessibility/runtime finding has become a scientific verdict
- state explicitly whether the month or research phase is actually closed

On 2026-08-30 the August maintenance record is month-to-date, not final calendar-month close

```text
maintenance clean != scientific validity
weekly consistency != entailment
monthly baseline != reproduction
publisher profile != acceptance
accessibility support != WCAG certification
```

The scanner does not render figures, inspect pixels, run tests, validate statistics, certify WCAG conformance, or predict publisher acceptance

## Change ownership

| Goal | Primary files | Synchronize |
|---|---|---|
| recipe field | `metadata/recipe.schema.yaml` | runtime + docs + evidence semantics |
| claim binding/audit/coverage | `core/claim_binding_audit.py`, `core/figure_evidence.py` | Assertion Basis + Figure Claim Contract + Manifest + examples |
| communication transfer | `core/communication_transfer.py` | Communication Transfer Contract + machine contract + examples + frontier notes |
| maintenance cadence | `core/maintenance_cadence.py`, `maintenance/cadence.yaml` | Maintenance Cadence + Stage index + Manifest + Agent Guide |
| process disclosure | recipe schema + figure evidence | public contracts |
| runtime rule | `quality/rules.yaml`, `sci_render.py` | severity + docs |
| accessibility | `core/accessibility.py`, `sci_render.py` | a11y + backend truth |
| backend | corresponding adapter | manifest/provenance capability truth |
| publisher profile | `profiles/*.yaml` | source status + acceptance false |
| public capability | README / Architecture / Contracts / Manifest | update together when semantics change |

## Cross-repository references

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
sci-render-kit/communication-transfer
```

These are optional handoff references, not direct coupling or inherited scientific validity

## Experimental semantics

- `projection`: PCA/projection metrics and t-SNE not implemented
- `uncertainty_legend`: typed uncertainty metadata
- `superposition`: deterministic variant layering
- `time_crystal`: periodic waveform utility
- `observer_dashboard`: caller-fed telemetry

Metaphorical filenames are not scientific capability evidence

## Local maintenance boundary

Manual commands may be used when useful
Their success is not scientific validity, publisher acceptance, WCAG certification, or independent reproduction
