# Frontier Research Stage J / 2026-Q2 — bounded research handoff
- Date 2026-10-19; source `lostlight530/sci-render-kit`; review [RESEARCH_REVIEW.md](RESEARCH_REVIEW.md); synthesis [STAGE_SYNTHESIS.md](STAGE_SYNTHESIS.md).
- Eligible transfer: contextual knowledge about **Grammar, prerelease and modern text shaping**, supported by 3 first-party releases and their exact dates.
- J-O1 — Vega-Lite target and data-spec hashes: Declarative spec and bound data identity must be retained separately; tooltip/cursor grammar can vary with runtime. [Source](https://github.com/vega/altair/releases/tag/v6.1.0).
- J-O2 — Matplotlib pre-GA compatibility: Release candidate availability is not stable release availability; its status and dates require separate treatment. [Source](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0rc2).
- J-O3 — Text/font shaping overhaul: Font shaping and bidi layout can change human-readable figure meaning, separate from plotting data. [Source](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0).
- Unsafe to transfer: benchmark score, runtime capability, local defect, independent validation, security compliance or other repositories' truth states.
- Unknowns: `render success != scientific validity; accessibility support != WCAG certification; checksum != reproduction; profile != publisher acceptance`. Cross-repository analogy is a research question only: `handoff != authority transfer`; `claim transfer != acceptance`.
