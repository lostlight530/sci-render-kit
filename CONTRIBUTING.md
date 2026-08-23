# Contributing

Contributions should strengthen the figure compiler's explicit contracts rather than only add another renderer or experimental module.

## Setup

```bash
python -m pip install pyyaml jsonschema matplotlib numpy pillow
make test
```

## Rules

- Update schema, quality gates, implementation, tests, and docs together for new recipe fields.
- Keep policy centralized in `sci_render.py`; adapters render validated intent.
- Do not mark a backend capability Implemented until the backend actually realizes it.
- Preserve WCAG scope: color must not be the only required cue (SC 1.4.1), short text alternatives support non-text content (SC 1.1.1), and SC 1.4.11 applies to graphical objects/boundaries required for understanding rather than every palette pair by default.
- Label project-strict rules as project rules.
- Keep Matplotlib provenance/reproducibility behavior in the base adapter and accessibility policy in the public adapter where possible.
- New generated sidecars must be ignored and included in output-integrity reasoning.
- Do not use “100% reproducible” or “WCAG conformant” unless a much broader system-level claim has actual evidence.
- Experimental modules remain Experimental until wired into the canonical dispatcher with tests.

## Testing

Legacy renderer/gate/profile/provenance behavior belongs in `tests/test_all.py`. Accessibility contract and sidecar behavior belongs in `tests/test_accessibility.py`.

Optional R/Node runtime tests may skip when their ecosystems are absent; do not interpret a skip as verified parity.
