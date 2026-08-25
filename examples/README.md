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

The preferred current upstream profile is `epistemic-pipeline/evidence-envelope@2`.

The renderer records references in `sci-render-kit/figure-evidence@2`; it does not independently adjudicate the upstream claims.

## Bind visual objects to upstream claims

When a figure contains multiple panels or series, the recipe can declare which visual object is intended to communicate which upstream claim:

```yaml
research_context:
  evidence_envelope_ref: evidence/run-042.evidence.json
  claim_refs: [claim_1, claim_2]
  claim_bindings:
    - visual_ref: panel:A
      claim_refs: [claim_1]
      relation: contextualizes
    - visual_ref: series:treatment
      claim_refs: [claim_2]
      relation: illustrates
      evidence_ref: evidence/run-042.evidence.json
```

Allowed relation labels:

```text
supports
illustrates
contextualizes
compares
derived-from
```

These bindings are declarative communication metadata. The renderer does not inspect titles, legends, data values or pixels to infer missing links.

The evidence sidecar therefore records:

```text
claim_communication.profile = sci-render-kit/figure-claim-binding@1
claim_communication.inferred_bindings = false
```

Do not interpret a `supports` label as automatically verified entailment or evidence sufficiency.

## Declare figure-generation process context

A recipe may also disclose AI assistance and human-review state:

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools:
    - provider/model or tool identifier declared by the author
  human_review: reviewed
  disclosure_ref: methods/figure-disclosure.md
```

The figure evidence record stores this as:

```text
sci-render-kit/process-disclosure@1
```

Boundaries:

```text
AI disclosure ≠ authorship adjudication
AI tool identity ≠ output validity
human review ≠ peer review
human review ≠ scientific truth
```

Missing disclosure values are represented as `not_declared`, not optimistic defaults.

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

Claim-binding and process-disclosure fields live in the figure evidence contract and do not imply that a rendering backend independently understands or validates their epistemic meaning.

## Observable HTML

The Observable adapter generates HTML using pinned `@observablehq/plot@0.6.17/+esm`. The generated artifact still needs browser network access to the CDN. Its render manifest records that environment boundary instead of claiming offline reproducibility.

## Publisher-target findings

```bash
python3 sci_render.py recipes/line-chart.yaml --profile nature --backend matplotlib
```

A PNG may produce a publisher-target warning if it falls outside the profile's current preferred format. This is **alignment evidence**, not a Nature acceptance/compliance result.

Nature's current profile was reverified on 2026-08-24 for its represented main-figure guidance scope. Science/Cell/IEEE presets remain explicitly dated 2026-08-19 snapshots until reverified.

Declaring AI assistance or human review does not convert publisher-target checking into AI-policy compliance validation.

## Figure evidence v2

Successful unified runs emit:

```text
sci-render-kit/figure-evidence@2
```

with bounded sections for:

```text
upstream_research
claim_communication
process_disclosure
uncertainty
runtime_validation
reproducibility
```

and explicit false flags for scientific/statistical/causal validity, authorship, peer review and publisher acceptance.

## Experimental examples are not canonical

`projection.py`, `uncertainty_legend.py`, `superposition.py`, `time_crystal.py`, and `observer_dashboard.py` remain Experimental. Their current mechanics are documented in README/Architecture and are not invoked by `sci_render.py`.

## Optional local checks

```bash
make test
```

This is a manual maintenance command, not a GitHub merge gate. The 2026-08-26 maintenance pass updates local contract files but does not use test execution as completion evidence.
