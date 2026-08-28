# Agent Guide — sci-render-kit

This is the operational contract for agents modifying the repository. Keep runtime code, schemas, profiles, evidence sidecars and public documentation semantically aligned.

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
```

Do not invent decorative internal versions. Preserve real WCAG/external/runtime versions when genuinely known.

## Hard rules

1. Schema does not imply backend support.
2. Do not silently change DPI, format, uncertainty semantics or declared data.
3. Claim bindings are explicit only; never infer them from titles, legends, pixels, prose or data values.
4. Claim relation labels are communication declarations, not verified entailment.
5. Process disclosure is bounded; tool/provider IDs and human review do not adjudicate authorship, peer review or truth.
6. Unknown provider/model/version/review/source metadata remains unknown; never guess.
7. The canonical renderer does not perform AI-text/pixel detection to infer AI authorship/use; preserve `automatic_ai_detection_used: false` unless a real separate detector is explicitly implemented.
8. Assertion basis records how a field entered evidence; it never upgrades a value to correctness.
9. Communication coverage remains dimensional. Do not create an unsupported aggregate scientific/communication quality score.
10. Coverage ratios are not probability, entailment, evidence sufficiency or provenance soundness.
11. Bounds alone are not a confidence interval or probability model.
12. WCAG scope stays exact; project all-pairs checks are extra safeguards.
13. CVD simulation is extra, not a normative WCAG certification test.
14. Publisher presets are snapshots/config targets, not acceptance validators.
15. Matplotlib extension remains explicit; avoid hidden monkeypatching.
16. Optional R/Node source does not prove runtime availability.
17. Figure evidence is handoff, not truth.
18. Communication transfer may copy declared context, but it must not inherit scientific validity, entailment, evidence sufficiency, statistical validity, peer review, publisher acceptance or WCAG conformance.
19. Communication transfer must not infer context from pixels, captions, filenames or prose.
20. Unsupported experimental methods fail explicitly rather than fabricate output.
21. Experimental importability does not make canonical capability.
22. Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge-gate architecture.

## Communication-audit invariants

`core/claim_binding_audit.py` may record findings plus coverage dimensions such as binding counts and evidence-context ratios.

```text
assertion basis != correctness
communication coverage != entailment
coverage ratio != probability
supports evidence-context coverage != evidence sufficiency
coverage != provenance soundness
```

Keep `aggregate_score: null` unless a future validated evaluation design explicitly justifies a composite score.

## Communication-transfer invariants

`core/communication_transfer.py` is a bounded view over an existing figure-evidence sidecar.

It may carry:

```text
claim communication
upstream research refs
uncertainty semantics
process disclosure
communication audit
runtime validation
```

Required boundaries:

```text
transfer != entailment
upstream ref != inherited validity
uncertainty metadata != statistical validation
publisher target != acceptance
accessibility metadata != WCAG certification
human review != peer review
```

Destination and purpose are caller-declared when present. Do not infer them.

## Change ownership

| Goal | Primary files | Synchronize |
|---|---|---|
| recipe field | `metadata/recipe.schema.yaml` | runtime + docs + evidence semantics |
| claim binding/audit/coverage | `core/claim_binding_audit.py`, `core/figure_evidence.py` | Assertion Basis + Figure Claim Contract + Manifest + examples |
| communication transfer | `core/communication_transfer.py` | Communication Transfer Contract + machine contract + examples + frontier notes |
| process disclosure | recipe schema + figure evidence | public contracts |
| runtime rule | `quality/rules.yaml`, `sci_render.py` | severity + docs |
| accessibility | `core/accessibility.py`, `sci_render.py` | a11y + backend truth |
| backend | corresponding adapter | manifest/provenance capability truth |
| publisher profile | `profiles/*.yaml` | source status + acceptance false |
| public capability | README / Architecture / Contracts / Manifest | update together when safe |

## Cross-repository references

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
sci-render-kit/communication-transfer
```

These are optional handoff references, not direct coupling or inherited scientific validity.

## Experimental semantics

- `projection`: PCA/projection metrics; t-SNE not implemented;
- `uncertainty_legend`: typed uncertainty metadata;
- `superposition`: deterministic variant layering;
- `time_crystal`: periodic waveform utility;
- `observer_dashboard`: caller-fed telemetry.

Metaphorical filenames are not scientific capability evidence.

## Local maintenance

Local commands may be used manually. Their success is not scientific validity, publisher acceptance, WCAG certification or independent reproduction.
