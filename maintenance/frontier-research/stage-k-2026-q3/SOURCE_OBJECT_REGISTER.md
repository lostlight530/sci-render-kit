# Source and Research-Object Register — K/2026-Q3

- Repository: `lostlight530/sci-render-kit`; constructed 2026-10-19; source cutoff 2026-10-19.
- Identity rule: **tagged upstream release object != release-note report**. Official release note and tag belong to one origin; separate release versions remain separate objects. Version existence does not entail local execution.

| Object ID | Canonical release object | GitHub release publication | Source ID | Original source family | URL | What is established / not established |
|---|---|---|---|---|---|---|
| O1 | plotly/plotly.py `v6.9.0` | 2026-07-09 | S1 | `plotly/plotly.py` | https://github.com/plotly/plotly.py/releases/tag/v6.9.0 | Published upstream release note describing bundled plotly.js update to 3.7.0 and marginal type validation; NOT local deployment or reproduction |
| O2 | plotly/plotly.py `v7.0.0` | 2026-08-25 | S2 | `plotly/plotly.py` | https://github.com/plotly/plotly.py/releases/tag/v7.0.0 | Published upstream release note describing Plotly.js 4.0, removed Mapbox/Orca/legacy Kaleido and Figure Factory APIs; NOT local deployment or reproduction |
| O3 | vega/altair `v6.3.0` | 2026-09-15 | S3 | `vega/altair` | https://github.com/vega/altair/releases/tag/v6.3.0 | Published upstream release note describing Python 3.10 dropped; parameterized datum expressions and stricter errors; NOT local deployment or reproduction |
| O4 | matplotlib/matplotlib `v3.11.2` | 2026-09-11 | S4 | `matplotlib/matplotlib` | https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2 | Published upstream release note describing PDF hexbin clipping and WebAgg/HiDPI rendering bug fixes; NOT local deployment or reproduction |

- Search/access date: 2026-10-19; release dates are upstream publication dates, not this repository's execution dates.
- Shared-origin dependence: any repeated releases from the same project remain **same-origin** even if separated by months. No independent reproducer linked/validated in this register.
- Source selection: purposefully chosen research objects from listed families; `SOURCE_BOUNDED` only, no exhaustive project-history claim.
