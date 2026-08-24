# Examples

## Baseline render

```bash
python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend matplotlib
```

The unified CLI evaluates the active runtime rules, dispatches to Matplotlib, checks the generated artifacts, and writes a figure-evidence sidecar on a successful run.

## Accessible multi-series render

```bash
python3 sci_render.py recipes/accessible-line-chart.yaml --profile presentation --backend matplotlib
```

The recipe declares short/long text alternatives, redundant non-color encoding and explicit adjacent series. The current Matplotlib path can emit:

```text
figure
figure.manifest.json
figure.prov.json
figure.a11y.json
figure.evidence.json
```

The `.a11y.json` object describes the figure-level accessibility contract. It does not certify an enclosing PDF or website as WCAG conformant.

## Research-context handoff

A recipe may point to upstream analysis evidence without creating runtime coupling:

```yaml
research_context:
  artifact_id: analysis-042
  evidence_envelope_ref: evidence/run-042.evidence.json
  provenance_ref: provenance/run-042.prov.json
  claim_refs: [claim_1, claim_2]
```

The renderer records these references in `sci-render-kit/figure-evidence@1`; it does not independently adjudicate the upstream claims.

## Uncertainty semantics

When uncertainty is represented, declare what it means:

```yaml
uncertainty:
  kind: bootstrap-interval
  level: 0.95
  semantics: "95% percentile bootstrap interval over the declared resamples"
  source_ref: analysis-042
```

Do not label a generic lower/upper range as a confidence interval unless the upstream method actually supplies that interpretation.

## Project-strict palette policy

The optional all-pairs palette safeguard remains available:

```yaml
aesthetics:
  palette: ["#000000", "#0072B2"]
  adjacency_check: true
```

It is deliberately stricter than WCAG SC 1.4.11's actual required-object/adjacent-color scope. The corresponding finding is a project warning rather than a claim about universal WCAG conformance.

For actual graphical adjacency, declare the series pairs:

```yaml
accessibility:
  adjacent_pairs:
    - [control, treatment]
```

## Backend capability honesty

A recipe that requires non-color redundant series styling cannot silently fall back on a backend that has not implemented it. The unified CLI reports `BACKEND_ACCESSIBILITY_MISMATCH` before dispatch.

Current status:

- Matplotlib: redundant marker/line/hatch mapping implemented;
- ggplot2: not integrated for that capability;
- Observable: not integrated for that capability.

## Observable HTML

The Observable adapter generates HTML using pinned `@observablehq/plot@0.6.17/+esm`. The generated artifact still needs browser network access to the CDN. Its render manifest records that environment boundary instead of claiming offline reproducibility.

## Publisher-target findings

```bash
python3 sci_render.py recipes/line-chart.yaml --profile nature --backend matplotlib
```

A PNG may produce a publisher-target warning if it falls outside the profile's current preferred format. This is **alignment evidence**, not a Nature acceptance/compliance result.

Nature's current profile was reverified on 2026-08-24 for its represented main-figure guidance scope. Science/Cell/IEEE presets remain explicitly dated 2026-08-19 snapshots until reverified.

## Experimental examples are not canonical

`projection.py`, `uncertainty_legend.py`, `superposition.py`, `time_crystal.py`, and `observer_dashboard.py` remain Experimental. Their current mechanics are documented in README/Architecture and are not invoked by `sci_render.py`.

## Optional local checks

```bash
make test
```

This is a manual maintenance command, not a GitHub merge gate. The 2026-08-24 maintenance pass updates local contract files but does not claim those checks were run.
