# F2 — Render Backend and Patch Stabilization

## Evidence
Plotly.py 6.1.0 was released 2025-05-15 with Kaleido >=1 support, widget/notebook fixes and MIME-renderer restoration for JupyterLab 4. Plotly.py 6.1.2 followed on 2025-05-27 with a type-checking/highlighting fix.

Matplotlib 3.10.3 is dated 2025-05-08 in official project history and represents another bugfix step in the 3.10 series.

Sources:
- https://github.com/plotly/plotly.py/releases/tag/v6.1.0
- https://github.com/plotly/plotly.py/releases/tag/v6.1.2
- https://matplotlib.org/3.10.9/users/prev_whats_new/github_stats_3.10.3.html

## Analysis
After a major renderer-stack change, reproducibility also depends on stabilization releases that repair backend, notebook and image-export behavior.

```text
major release support
!= all host/backend paths stable

patch release
!= every prior artifact invalid
```

Backend version, notebook host and export engine remain part of communication provenance.

## Outcome
`SUPPORTED_OBSERVATION`
