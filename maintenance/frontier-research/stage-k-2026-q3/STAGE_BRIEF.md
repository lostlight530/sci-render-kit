# Frontier Research Stage K / 2026-Q3 — research brief
- Repository: `lostlight530/sci-render-kit`; source window 2026-07-01–2026-09-30; `RETROSPECTIVE`.
- Protocol recorded 2026-10-19 **after targeted source discovery**, not preregistered during the historical months.
- Specification: `2026-09-19-first-batch`; design `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`; status `COMPLETE`.
## Rationale and research question
**Theme:** Patch fidelity, major export migration and runtime floors. **Question:** How does patch fidelity, major export migration and runtime floors change the evidence needed to assess figure evidence, scientific claim binding, wrapper/JS renderer revisions, accessibility, export and backend identity without inferring local implementation?
## Eligibility and source method
On 2026-10-19, inspect the selected publishers' GitHub `GET /repos/{owner}/{repo}/releases?per_page=100&page=1` and exact `/releases/tags/{tag}` records. Select dated release/version objects inside the quarter relevant to the repository lens; one release is one object, even with many reported features. Exclude outside-window dates and undated speculation. Mark prereleases precisely, not as GA. The sample is neither exhaustive external research nor independent reproduction.
## Research Parts / unit of analysis
- K-O1 — How do patch-level rendering changes relate to evidence communication?; publisher [matplotlib/matplotlib v3.11.1](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.1) dated 2026-07-18
- K-O2 — Which export/trace contracts can fail after a major wrapper migration?; publisher [plotly/plotly.py v7.0.0](https://github.com/plotly/plotly.py/releases/tag/v7.0.0) dated 2026-08-25
- K-O3 — How does Python version belong to declarative visualization identity?; publisher [vega/altair v6.3.0](https://github.com/vega/altair/releases/tag/v6.3.0) dated 2026-09-15
- K-O4 — When is the renderer backend an irreducible figure identity field?; publisher [matplotlib/matplotlib v3.11.2](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2) dated 2026-09-11
## Charting and review plan
Version/date, object/source identity, publisher-stated behavior, analytic interpretation, alternative reading, source-family independence and missing local verification. A producer review can close a source-bounded documentary Stage if its limitations are explicit; independent scholarly review is not claimed.
Hard boundary: `render success != scientific validity; accessibility support != WCAG certification; checksum != reproduction; profile != publisher acceptance`.
