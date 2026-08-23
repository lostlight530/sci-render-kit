# Agent Guide — sci-render-kit

This file is the operational contract for agents modifying the repository. Public capability claims must remain aligned across `README.md`, `ARCHITECTURE.md`, `MANIFEST.yaml`, schemas, gates, adapters, and tests.

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

## 2. Full deterministic contract

```bash
python -m pip install pyyaml jsonschema matplotlib numpy pillow
make test
```

GitHub Actions runs the same contract with Python 3.12. R/Node runtime remains optional unless the workflow explicitly provisions those ecosystems.

## 3. Hard rules

1. **Unified validation.** New public policy goes through `sci_render.py`; adapters should not each invent a different validation model.
2. **Backend truth.** Schema support does not imply backend support. Update `BACKEND_ACCESSIBILITY_CAPABILITIES` only after actual rendering behavior and tests exist.
3. **Use of Color.** If `redundant_encoding: required`, supported multi-series charts must expose non-color cues. Do not satisfy this by merely adding another color.
4. **WCAG scope.** `adjacent_pairs` models actual graphical adjacency for SC 1.4.11 support. The legacy all-pairs adjacency gate is a stricter project policy, not the normative WCAG scope.
5. **Text alternatives.** `require_alt_text: true` must gate missing short alternatives. Do not claim that a sidecar alone makes a final website/PDF accessible; publishing-layer association still matters.
6. **CVD is separate.** Machado simulation is a project safeguard, not a WCAG success criterion.
7. **Matplotlib layering.** Keep `matplotlib_base.py` as the stable render/provenance core. The public adapter may add policy behavior but must preserve existing exported APIs.
8. **Dumb adapters.** Backend adapters translate validated intent into backend-specific rendering; they are not alternative policy engines.
9. **No fake reproducibility.** Checksums/provenance improve traceability but do not justify “100% reproducible” claims.
10. **No fake conformance.** `sci-render-kit/a11y@1` explicitly carries `conformance_claim: false`.
11. **Experimental stays Experimental.** projection/time_crystal/uncertainty_legend/observer_dashboard/superposition are not integrated capabilities.
12. **Optional ecosystems stay optional.** A skipped R/Node E2E test is neither a failure nor proof of runtime parity.

## 4. Where to change what

| Goal | Primary files | Required follow-up |
|---|---|---|
| recipe field | `metadata/recipe.schema.yaml` | gate/backend/tests/docs |
| accessibility rule | `core/accessibility.py`, `sci_render.py`, `quality/gates.yaml` | `tests/test_accessibility.py` |
| Matplotlib non-color encoding | `backends/matplotlib_adapter.py` | preserve base API + E2E test |
| base Matplotlib rendering/provenance | `backends/matplotlib_base.py` | old `tests/test_all.py` contract |
| new backend capability | adapter + capability matrix | real E2E or explicit optional-runtime test |
| publication profile | `profiles/*.yaml`, `profiles/README.md` | source/verification date + P3 tests |
| named palette | `core/palettes.py` | type/availability/CVD metadata + tests |
| provenance | Matplotlib base + P2 gate | checksum/readback tests |
| public capability | README/ARCHITECTURE/MANIFEST | update together |

## 5. Accessibility invariants

For `redundant_encoding: required` on a supported multi-series chart:

- every series label resolves to a style signature,
- signatures are distinct across the visible series,
- color remains available but is not the only series cue,
- `.a11y.json` records the actual cues used.

For `adjacent_pairs`:

- labels must exist in the recipe data,
- only declared pairs are checked by the WCAG-scoped adjacency gate,
- a separate legacy all-pairs project gate may still run if `aesthetics.adjacency_check` is explicitly enabled.

## 6. Completion gate

Before a PR is ready:

- `make test` is the intended contract,
- capability matrices match actual backend behavior,
- new recipe fields are in schema and docs,
- generated sidecars are gitignored,
- no external standard is paraphrased more strongly than its real scope,
- no experimental module was silently promoted.
