# Examples

## Baseline render

```bash
python3 sci_render.py examples/line_chart.yaml --profile nature --backend matplotlib
```

A successful unified render may produce:

```text
<figure>
<figure>.manifest.json
<figure>.prov.json        # Matplotlib path
<figure>.a11y.json        # when accessibility is declared
<figure>.evidence.json
```

Project-owned evidence identifiers are stable names:

```text
sci-render-kit/render-manifest
sci-render-kit/provenance
sci-render-kit/a11y
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

Do not infer scientific validity from the existence of these files.

## Claim communication example

```yaml
research_context:
  artifact_id: experiment-42
  evidence_envelope_ref: evidence/run-42.evidence.json
  claim_audit_ref: claim-audits/run-42.claim-audit.json
  claim_refs: [claim_42]
  claim_bindings:
    - visual_ref: series:treated
      claim_refs: [claim_42]
      relation: illustrates
      evidence_ref: evidence/run-42.evidence.json

process_disclosure:
  ai_assistance: used
  ai_tools: [declared-tool-id]
  human_review: partial
```

This records declared communication/process context only:

```text
binding != entailment
evidence ref != evidence sufficiency
human review != peer review
```

## Accessibility example

```yaml
accessibility:
  require_alt_text: true
  alt_text: "Line chart comparing the declared series over six observations."
  redundant_encoding: required
```

WCAG-related checks are scoped design support, not whole-document conformance certification.

## Optional backends

```bash
python3 sci_render.py examples/line_chart.yaml --profile presentation --backend ggplot2
python3 sci_render.py examples/line_chart.yaml --profile presentation --backend observable
```

Adapter source presence does not prove the optional R/Node runtime exists. Observable HTML also has a declared external Plot dependency at view time unless separately vendored.
