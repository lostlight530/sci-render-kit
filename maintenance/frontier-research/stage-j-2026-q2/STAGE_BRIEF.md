# Frontier Research Stage J / 2026-Q2 — research brief
- Repository: `lostlight530/sci-render-kit`; source window 2026-04-01–2026-06-30; `RETROSPECTIVE`.
- Protocol recorded 2026-10-19 **after targeted source discovery**, not preregistered during the historical months.
- Specification: `2026-09-19-first-batch`; design `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`; status `COMPLETE`.
## Rationale and research question
**Theme:** Grammar, prerelease and modern text shaping. **Question:** How does grammar, prerelease and modern text shaping change the evidence needed to assess figure evidence, scientific claim binding, wrapper/JS renderer revisions, accessibility, export and backend identity without inferring local implementation?
## Eligibility and source method
On 2026-10-19, inspect the selected publishers' GitHub `GET /repos/{owner}/{repo}/releases?per_page=100&page=1` and exact `/releases/tags/{tag}` records. Select dated release/version objects inside the quarter relevant to the repository lens; one release is one object, even with many reported features. Exclude outside-window dates and undated speculation. Mark prereleases precisely, not as GA. The sample is neither exhaustive external research nor independent reproduction.
## Research Parts / unit of analysis
- J-O1 — Why must a spec hash not erase data-binding identity?; publisher [vega/altair v6.1.0](https://github.com/vega/altair/releases/tag/v6.1.0) dated 2026-04-21
- J-O2 — What evidence can an RC provide before GA publication?; publisher [matplotlib/matplotlib v3.11.0rc2](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0rc2) dated 2026-05-13 (release candidate)
- J-O3 — Which font/locale environment must accompany reproducible multilingual figures?; publisher [matplotlib/matplotlib v3.11.0](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0) dated 2026-06-12
## Charting and review plan
Version/date, object/source identity, publisher-stated behavior, analytic interpretation, alternative reading, source-family independence and missing local verification. A producer review can close a source-bounded documentary Stage if its limitations are explicit; independent scholarly review is not claimed.
Hard boundary: `render success != scientific validity; accessibility support != WCAG certification; checksum != reproduction; profile != publisher acceptance`.
