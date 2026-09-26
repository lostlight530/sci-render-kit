# External GPT Reconciliation — Qi Frontier Annotation

**Repository:** lostlight530/sci-render-kit
**Date:** 2026-09-26
**Scope:** second-pass reconciliation of PR #61 annotation claims only
**Historical Stage rewrite:** NONE
**Runtime / contract change:** NONE

## Authority boundary

This file corrects the new Qi annotation forward

It does not rewrite Stage A-G and does not upgrade annotation prose into render validity, accessibility certification, scientific validity or publisher acceptance

## Confirmed temporal corrections

### C1 — Plotly.py 6.0.0

The Qi annotation states Plotly.py 6.0 was released on 2025-03-06 and describes it as near a Q1/Q2 boundary

The official Plotly.py changelog records:

    Plotly.py 6.0.0 = 2025-01-28

Source:

https://github.com/plotly/plotly.py/blob/main/CHANGELOG.md

Therefore 2025-01-28 belongs to 2025-Q1

The 2025-03-06 date and the Q1/Q2-boundary characterization in the Qi annotation are superseded by this correction

### C2 — Matplotlib 3.10.0

Matplotlib's official release documentation records 3.10.0 on 2024-12-13

Source:

https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html

The Stage D temporal placement is supported

### C3 — Matplotlib 3.10.5

The Qi annotation places Matplotlib 3.10.5 around June 2025 inside Stage F / 2025-Q2

Matplotlib's official release index records:

    Matplotlib 3.10.5 = 2025-07-31

Source:

https://matplotlib.org/stable/users/release_notes

Therefore 3.10.5 belongs to 2025-Q3, not Q2

The Stage F temporal placement is superseded

### C4 — Plotly.py 6.3.0

The official Plotly.py changelog records:

    Plotly.py 6.3.0 = 2025-08-12

Source:

https://github.com/plotly/plotly.py/blob/main/CHANGELOG.md

This supports Q3 placement

## Other evidence-boundary corrections

### C5 — line-count gate is not repository specification

The PR description mentions a ">=100 effective semantic lines" task gate

No such numeric minimum exists in the current frontier-research specification or README

It is task provenance, not repository doctrine

### C6 — unresolved exact dates remain unresolved

Claims whose exact date/version was not independently rechecked here, including Vega-Lite point-release timing, remain VERIFY_IN_PLACE or UNKNOWN where uncertainty remains

Do not infer correctness from thematic fit

### C7 — external review does not retroactively alter historical review identity

The Qi annotation is a new external review layer

    EXTERNAL_REVIEW_PRESENT_NOW
    != HISTORICAL_STAGE_REVIEW_INDEPENDENCE_ESTABLISHED

## Reconciled disposition

PR #61 remains useful as an external Stage A-G review, but the original temporal statements above must be read through this correction file

No historical Stage content is rewritten and no runtime, render or scientific capability claim is introduced
