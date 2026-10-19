# Frontier Research Month Reconstruction — 2026-08

## Identity and temporal integrity
- Repository: `lostlight530/sci-render-kit`; Stage: K / 2026-Q3
- Historical event window: 2026-08-01 to 2026-08-31
- Reconstruction performed: 2026-10-19; source-access date: 2026-10-19
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION`; achieved coverage: `SOURCE_BOUNDED`
- Result: `SELECTED_SOURCE_OBJECTS`

## Source discovery actually executed
GitHub repository Releases REST listing and, for each included release, exact `/repos/{owner}/{repo}/releases/tags/{tag}` retrieval. Initial surface restricted to the selected official release families relevant to this repository lens; release `published_at` used to attribute the event to its month, except original release-note calendar references retained as notes. No systematic literature-wide search, independent scientific replication or guarantee of exhausting even adjacent projects.

## Selected events and evidence
- **2026-08-25 · plotly/plotly.py v7.0.0** — Plotly.js 4.0, removed Mapbox/Orca/legacy Kaleido and Figure Factory APIs. [Primary release](https://github.com/plotly/plotly.py/releases/tag/v7.0.0)
  - *Evidence-bound interpretation:* Major upgrades can remove exporters and traces, change MathJax/color parsing and transform chart output identity; compatibility requires explicit migration rather than an assumed equivalent figure.
  - *Negative space:* Release lists supported migrations but does not prove that legacy figures remain semantically equivalent.

## Month analysis
These selected release objects matter to scientific figure evidence, declarative grammar, rendering stacks, uncertainty, accessibility, communication and publication transfer. The distinction is **upstream published behavior versus reproducible downstream execution**: the official release record can document the upstream change, but this research has not run the release in this repository, replayed its outputs or independently validated its results. The records above may belong to the same upstream-origin family; repeated vendor claims are not independent corroboration.

## Forward boundary
- No modification to earlier monthly history or Stage H.
- Native runtime drift: `UNKNOWN / NOT_AUDITED`; no code or contract change.
- Parent [Stage brief](STAGE_BRIEF.md); subsequent [quarter synthesis](STAGE_SYNTHESIS.md).
