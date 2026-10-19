# Frontier Research Stage I / 2026-Q1 — research brief
- Repository: `lostlight530/sci-render-kit`; source window 2026-01-01–2026-03-31; `RETROSPECTIVE`.
- Protocol recorded 2026-10-19 **after targeted source discovery**, not preregistered during the historical months.
- Specification: `2026-09-19-first-batch`; design `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`; status `COMPLETE`.
## Rationale and research question
**Theme:** Theme and interaction changes across patch releases. **Question:** How does theme and interaction changes across patch releases change the evidence needed to assess figure evidence, scientific claim binding, wrapper/JS renderer revisions, accessibility, export and backend identity without inferring local implementation?
## Eligibility and source method
On 2026-10-19, inspect the selected publishers' GitHub `GET /repos/{owner}/{repo}/releases?per_page=100&page=1` and exact `/releases/tags/{tag}` records. Select dated release/version objects inside the quarter relevant to the repository lens; one release is one object, even with many reported features. Exclude outside-window dates and undated speculation. Mark prereleases precisely, not as GA. The sample is neither exhaustive external research nor independent reproduction.
## Research Parts / unit of analysis
- I-O1 — Why does template precedence matter to a scientific figure?; publisher [plotly/plotly.py v6.5.1](https://github.com/plotly/plotly.py/releases/tag/v6.5.1) dated 2026-01-07
- I-O2 — Can visually similar static charts have different interactive meanings?; publisher [plotly/plotly.py v6.6.0](https://github.com/plotly/plotly.py/releases/tag/v6.6.0) dated 2026-03-02
## Charting and review plan
Version/date, object/source identity, publisher-stated behavior, analytic interpretation, alternative reading, source-family independence and missing local verification. A producer review can close a source-bounded documentary Stage if its limitations are explicit; independent scholarly review is not claimed.
Hard boundary: `render success != scientific validity; accessibility support != WCAG certification; checksum != reproduction; profile != publisher acceptance`.
