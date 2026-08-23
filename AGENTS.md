# Agent Guide — sci-render-kit

This file is the operational guide for agents modifying the repository. Public capability claims must remain aligned across `README.md`, `ARCHITECTURE.md`, `MANIFEST.yaml`, schemas, runtime quality rules, adapters, and tests.

## 1. Canonical architecture

```text
recipe.schema.yaml
  -> sci_render.py (P0/P1 + backend capability)
  -> backend adapter
  -> output
  -> P2/P3

Matplotlib path:
backends/matplotlib_adapter.py
  -> backends/matplotlib_base.py

Accessibility evidence:
core/accessibility.py
  -> <output>.a11y.json
```

## 2. Local checks

When useful:

```bash
python -m pip install pyyaml jsonschema matplotlib numpy pillow
make test
```

These are manual maintenance checks, not an automated merge gate. R/Node runtime remains optional unless a developer explicitly provisions those ecosystems locally.

## 3. Hard rules

1. **Unified validation.** New public policy goes through `sci_render.py`; adapters should not each invent a different validation model.
2. **Backend truth.** Schema support does not imply backend support. Update `BACKEND_ACCESSIBILITY_CAPABILITIES` only after actual rendering behavior exists.
3. **Use of Color.** If `redundant_encoding: required`, supported multi-series charts must expose non-color cues. Do not satisfy this by merely adding another color.
4. **WCAG scope.** `adjacent_pairs` models actual graphical adjacency for SC 1.4.11 support. The legacy all-pairs adjacency rule is a stricter project policy, not the normative WCAG scope.
5. **Text alternatives.** `require_alt_text: true` must reject missing short alternatives. Do not claim that a sidecar alone makes a final website/PDF accessible; publishing-layer association still matters.
6. **CVD is separate.** Machado simulation is a project safeguard, not a WCAG success criterion.
7. **Matplotlib layering.** Keep `matplotlib_base.py` as the stable render/provenance core. The public adapter may add policy behavior but must preserve existing exported APIs and direct-script import bootstrap.
8. **Dumb adapters.** Backend adapters translate validated intent into backend-specific rendering; they are not alternative policy engines.
9. **No fake reproducibility.** Checksums/provenance improve traceability but do not justify “100% reproducible” claims.
10. **No fake conformance.** `sci-render-kit/a11y@1` explicitly carries `conformance_claim: false`.
11. **Experimental stays Experimental.** projection/time_crystal/uncertainty_legend/observer_dashboard/superposition are not integrated capabilities.
12. **Optional ecosystems stay optional.** An unexecuted R/Node E2E path is neither a failure nor proof of runtime parity.

## 4. Where to change what

| Goal | Primary files | Required follow-up |
|---|---|---|
| recipe field | `metadata/recipe.schema.yaml` | runtime rule/backend/docs; nearest local check when useful |
| accessibility rule | `core/accessibility.py`, `sci_render.py`, `quality/gates.yaml` | keep scope explicit |
| Matplotlib non-color encoding | `backends/matplotlib_adapter.py` | preserve base API + direct-run bootstrap |
| base Matplotlib rendering/provenance | `backends/matplotlib_base.py` | preserve existing public behavior |
| new backend capability | adapter + capability matrix | actual implementation or explicit optional-runtime status |
| publication profile | `profiles/*.yaml`, `profiles/README.md` | source/verification date + P3 semantics |
| named palette | `core/palettes.py` | type/availability/CVD metadata |
| provenance | Matplotlib base + P2 rule | checksum/readback semantics |
| public capability | README/ARCHITECTURE/MANIFEST | update together |

## 5. Accessibility invariants

For `redundant_encoding: required` on a supported multi-series chart:

- every series label resolves to a style signature,
- signatures are distinct across the visible series,
- color remains available but is not the only series cue,
- `.a11y.json` records the actual cues used.

For `adjacent_pairs`:

- labels must exist in the recipe data,
- only declared pairs are checked by the WCAG-scoped adjacency rule,
- a separate legacy all-pairs project rule may still run if `aesthetics.adjacency_check` is explicitly enabled.

## 6. Consistency

Keep capability matrices aligned with actual backend behavior, keep new recipe fields synchronized across schema and docs, keep generated sidecars ignored, and do not paraphrase external standards more strongly than their real scope. None of these consistency rules require GitHub Actions or a merge gate.
