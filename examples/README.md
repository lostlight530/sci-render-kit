# Examples

## Baseline render

```bash
python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend matplotlib
```

## Accessible multi-series render

```bash
python3 sci_render.py recipes/accessible-line-chart.yaml --profile presentation --backend matplotlib
```

The accessible example declares:

- short and long text alternatives,
- `redundant_encoding: required`,
- an actual adjacent series pair,
- explicit output/provenance settings.

The Matplotlib path produces the figure plus `.manifest.json`, `.prov.json`, and `.a11y.json`. The series are differentiated by color **and** marker/line style.

## Strict project-wide palette-pair policy

The older all-pairs policy is still available:

```yaml
aesthetics:
  palette: ["#000000", "#0072B2"]
  adjacency_check: true
```

This is intentionally stricter than WCAG SC 1.4.11's actual-adjacent-object scope. Use `accessibility.adjacent_pairs` when you want the WCAG-scoped boundary model.

## Text alternative requirement

```yaml
accessibility:
  require_alt_text: true
  alt_text: "Treatment increases more quickly than control."
```

A missing `alt_text` in this mode is rejected before rendering.

## Backend capability honesty

A recipe requesting non-color redundant encoding on a backend that has not implemented those style mappings fails before dispatch:

```text
BACKEND_ACCESSIBILITY_MISMATCH
```

Today Matplotlib implements redundant series styling. R/Observable support for that specific capability remains Not Integrated.

## Journal gate demo

```bash
python3 sci_render.py recipes/line-chart.yaml --profile nature --backend matplotlib
```

A PNG recipe can be rejected by the Nature P3 vector-format gate. This is a deliberate contract failure, not a renderer crash.

## Verification

```bash
make test
```

The repository contract covers legacy rendering/provenance and the new accessibility profile. R/Node E2E checks remain environment-dependent and may skip when runtimes are absent.
