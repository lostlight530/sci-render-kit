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

Project evidence identifiers are stable semantic names. File existence does not imply scientific validity.

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
      relation: supports
      evidence_ref: evidence/run-42.evidence.json

process_disclosure:
  ai_assistance: used
  ai_tools: [declared-tool-id]
  human_review: partial
```

```text
binding != entailment
evidence ref != evidence sufficiency
human review != peer review
```

## Assertion basis in figure evidence

A bounded evidence excerpt can look like:

```json
{
  "figure": {
    "file_sha256": "sha256:...",
    "identity_basis": "runtime-observed-local-bytes"
  },
  "claim_communication": {
    "assertion_basis": "recipe-declared",
    "inferred_bindings": false
  },
  "process_disclosure": {
    "basis": "recipe-declared",
    "automatic_ai_detection_used": false
  }
}
```

```text
recipe-declared = where the relation came from
recipe-declared != scientifically verified
```

## Communication coverage example

`communication_audit.coverage` may contain:

```json
{
  "counts": {
    "figure_claim_count": 2,
    "valid_binding_count": 2,
    "indexed_claims_with_binding_count": 2,
    "supports_binding_count": 1,
    "supports_with_evidence_context_count": 1
  },
  "ratios": {
    "indexed_claim_binding_ratio": 1.0,
    "supports_evidence_context_ratio": 1.0
  },
  "aggregate_score": null
}
```

Interpretation:

```text
indexed_claim_binding_ratio=1.0
  = every figure-level indexed claim has at least one valid binding

supports_evidence_context_ratio=1.0
  = every declared supports binding has some declared evidence/audit/provenance context

neither ratio = truth / entailment / evidence sufficiency / probability
```

## Accessibility example

```yaml
accessibility:
  require_alt_text: true
  alt_text: "Line chart comparing the declared series over six observations."
  redundant_encoding: required
```

WCAG-related checks are scoped design support, not whole-document conformance certification.

## Uncertainty example

```yaml
uncertainty:
  kind: confidence-interval
  level: 0.95
  semantics: "95% interval from the declared upstream analysis"
  source_ref: analysis.json
```

The renderer preserves this declaration but does not validate the upstream statistical method.

## Optional backends

```bash
python3 sci_render.py examples/line_chart.yaml --profile presentation --backend ggplot2
python3 sci_render.py examples/line_chart.yaml --profile presentation --backend observable
```

Adapter source presence does not prove optional R/Node runtime availability. Observable HTML retains a declared external Plot dependency unless separately vendored.

## Local maintenance

Local checks are optional maintenance aids, not GitHub merge gates, scientific validation, WCAG certification or publisher acceptance.
