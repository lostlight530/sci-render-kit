# Contributing

Contributions should strengthen the figure compiler's explicit research and rendering semantics rather than only add another renderer or experimental module.

## Setup

```bash
python -m pip install pyyaml jsonschema matplotlib numpy pillow
```

`make test` is available as an optional local maintenance check. It is not a GitHub merge gate.

## Rules

- Update schema, runtime quality rules, implementation, and docs together for new recipe fields.
- Keep policy centralized in `sci_render.py`; adapters render validated intent.
- Do not mark a backend capability Implemented until the backend actually realizes it.
- Preserve WCAG scope: color must not be the only required cue (SC 1.4.1), short text alternatives support non-text content (SC 1.1.1), and SC 1.4.11 applies to graphical objects/boundaries required for understanding rather than every palette pair by default.
- Label project-strict rules as project rules.
- Keep Matplotlib provenance/reproducibility behavior in the base adapter and accessibility policy in the public adapter where possible.
- Preserve the public Matplotlib adapter's direct-script repository-root import bootstrap.
- New generated sidecars must be ignored and included in output-integrity reasoning.
- Do not use “100% reproducible” or “WCAG conformant” unless a much broader system-level claim has actual evidence.
- Experimental modules remain Experimental until wired into the canonical dispatcher.

## Local checks

Legacy renderer/profile/provenance behavior can be inspected with `tests/test_all.py`; accessibility contract and sidecar behavior can be inspected with `tests/test_accessibility.py` when useful. Optional R/Node runtime paths may remain unexecuted when their ecosystems are absent; do not interpret that as verified parity.
