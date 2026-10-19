# Frontier Research Stage K / 2026-Q3 — structured evidence chart
- Extracted 2026-10-19; no invented flow counts, effect size or universal quality score.
| Versioned object | Direct publisher observation | Research interpretation | Competing interpretation / limitation |
|---|---|---|---|
| K-O1 / v3.11.1 | Matplotlib 3.11.1 reports tight-layout, 3D aspect and PDF font glyph fixes. | Patch releases can change visible publication artifacts without changing data inputs. | No PDF, 3D or layout pixel diff was executed. |
| K-O2 / v7.0.0 | Plotly.py 7.0 bundles plotly.js 4, removes legacy Mapbox traces and legacy Orca/Kaleido image export paths. | Wrapper major, JS engine and export backend are independent compatibility gates for saved figure recipes. | No old/new renderer execution or publisher-target check. |
| K-O3 / v6.3.0 | Altair 6.3.0 drops Python 3.10 support and expands parameter expressions while tightening invalid argument errors. | Dependency floors and stricter grammar validation affect whether the same declared recipe can execute. | No environment compatibility matrix or interaction replay ran. |
| K-O4 / v3.11.2 | Matplotlib 3.11.2 reports PDF hexbin clipping, Cairo glyph, WebAgg/Qt HiDPI and GIF skew fixes. | One plotting recipe may differ across backend export targets even on the same scientific dataset. | Only specified failure modes are evidenced; no backend experiment. |
Finding class: upstream version statement supported by one publisher-family source; downstream execution, independence and current repository drift remain `NOT_ASSESSED`.
