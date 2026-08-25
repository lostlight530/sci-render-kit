# Contributing

Contributions should strengthen explicit scientific-figure semantics rather than only increase renderer/module count.

## Setup

```bash
python -m pip install pyyaml jsonschema matplotlib numpy pillow
```

`make test` is an optional local maintenance command. It is not GitHub merge policy.

## Contribution rules

- Update schema, runtime rules, implementation, evidence profiles and docs together when a public recipe field changes.
- Active runtime rules live in `quality/rules.yaml`; do not restore the retired `quality/gates.yaml` model.
- Keep validation centralized in `sci_render.py`; backend adapters implement validated intent within declared capabilities.
- Use `error / warning / info` deliberately. Publisher preferences and project robustness heuristics should not silently become hard failures.
- Do not mark a backend capability Implemented until actual rendering behavior exists.
- Preserve WCAG scope: text alternatives support non-text content, color cannot be the only required cue, and SC 1.4.11 applies to graphical objects/boundaries required for understanding relative to adjacent colors.
- Label all-pairs palette checking and CVD simulation as project safeguards rather than normative WCAG requirements.
- Treat semantic color labels as project conventions unless stronger evidence exists.
- Uncertainty requires explicit `kind` and `semantics`; do not infer confidence/credible intervals from lower/upper bounds alone.
- Claim-to-visual relations must be recipe-declared. Do not infer bindings from titles, legends, pixels, labels, or data values.
- Treat `supports` / `illustrates` / other binding labels as communication metadata, not verified entailment or evidence sufficiency.
- Process disclosure is metadata only: AI/tool identifiers do not adjudicate authorship; `human_review: reviewed` is not peer review.
- Missing disclosure must remain `not_declared` rather than being upgraded to optimistic defaults.
- Preserve publisher profile evidence state (`source_url`, `verified_date`, `source_status`, `verification_scope`, `acceptance_claim: false`).
- Preserve Matplotlib's explicit extension-hook architecture; do not mutate base-renderer globals to add accessibility behavior.
- Do not silently change declared DPI/output format to make a profile appear to pass.
- Keep `render-manifest@2`, `provenance@2`, `a11y@1`, `figure-claim-binding@1`, `process-disclosure@1`, and `figure-evidence@2` semantics distinct.
- Current upstream Epistemic handoff target is `epistemic-pipeline/evidence-envelope@2`; do not add hidden direct runtime coupling.
- New generated sidecars must be gitignored and reflected in artifact-integrity reasoning.
- Do not use “100% reproducible”, “journal compliant”, “scientifically validated”, “peer reviewed”, or “WCAG conformant” unless the broader claim has independent evidence.
- Experimental modules remain Experimental until the canonical dispatcher actually consumes them.
- If an algorithm is not implemented, fail explicitly rather than returning plausible-looking placeholder values.
- Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge-gate language as part of repository architecture.

## Research-integrity boundary

A figure recipe/evidence record may establish declared communication and process context. It does not prove:

```text
claim truth
verified entailment
evidence sufficiency
statistical validity
causal validity
authorship
peer review
publisher acceptance
independent reproduction
```

## Local contract files

`tests/test_all.py` and `tests/test_accessibility.py` document current interfaces and invariants. They may be run manually when useful, but changing them is not evidence that they were executed and passing.

Optional R/Node paths may remain unexecuted when those runtimes are absent; unexecuted is not verified parity.
