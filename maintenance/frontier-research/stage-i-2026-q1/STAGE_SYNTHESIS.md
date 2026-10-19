# Frontier Research Stage Synthesis — I / 2026-Q1

## 0. Identity and status
- Repository: `lostlight530/sci-render-kit`
- Window: `2026-01-01 through 2026-03-31`; record type: `RETROSPECTIVE`
- Synthesis and research date: `2026-10-19`; specification: `2026-09-19-first-batch`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`
- Evidence coverage actually achieved: `SOURCE_BOUNDED`, not field-comprehensive or independently replicated
- Status: `COMPLETE` as a bounded document research project; stage disposition: `FRONTIER_STAGE_COMPLETE`
- Review independence: `SAME_PRODUCER_REVIEW`; independent validation **not established**.

## 1. Research questions revisited
| Question | Outcome | Research evidence | Scope limit |
|---|---|---|---|
| What versioned upstream changes matter? | `ANSWERED_WITHIN_SELECTED_RELEASES` | I1, I2, I3 | Official project release descriptions |
| What evidence/provenance relations arise? | `BOUNDED_INTERPRETATION` | Part analyses + EVIDENCE_CHART | Not adoption or experimental performance |
| Is a current repository defect confirmed? | `UNRESOLVED / NOT_AUDITED` | No current-runtime audit | Upstream changes cannot prove current drift |

## 2. Inputs, selection and actual methods
- Stage Brief post-selection reconstruction protocol; [2026-01](MONTH_2026_01_RECONSTRUCTION.md), [2026-02](MONTH_2026_02_RECONSTRUCTION.md), [2026-03](MONTH_2026_03_RECONSTRUCTION.md).
- 3 selected versioned upstream release object(s), each independently inspectable in `I1`, `I2`, `I3`; the register and evidence chart preserve version/source mapping.
- Actual search/navigation: bounded GitHub release listings and selected tag descriptions, inspected 2026-10-19. No comprehensive literature search, independent evidence chaining, version-controlled installations, or experiments.
- All three months have at least one selected upstream release, but field completeness cannot be inferred.

## 3. Quarterly research narrative: change and persistence
Stage H / 2025-Q4 distinguished dependency floors, Python wrapper, grammar/JS renderer and generated spec identity; a successful render remained non-validating.
- **2026-01-14, vega-lite v6.4.2:** Tooltip formatting and legend repair. A stable high-level spec may acquire different tooltip/legend behavior under a patch-level compiler revision.
- **2026-02-20, plotly.js v3.4.0:** Legend-title and interaction semantics. Interactive figure semantics depend on the JS engine revision and user action, not just a static image.
- **2026-03-02, plotly.py v6.6.0:** Renderer/export patch and side effects. A wrapper patch can change diagnostics/export interpretation independent of scientific data or plot recipe.

Across these objects, the quarter's useful change is a sharper distinction between **released interface/standard state** and **observed execution state**. Where more than one object was selected, their relationship is an analytic comparison of provenance/identity surfaces, not a claimed causal dependency. Where the source density is low, the conclusion is correspondingly narrow.

## 4. Mechanism and cross-Part synthesis
1. **Tooltip formatting and legend repair:** Vega-Lite 6.4.2 fixes tooltip custom formatter behavior and legend merging with explicit scale/range/domain. The research interpretation is: A stable high-level spec may acquire different tooltip/legend behavior under a patch-level compiler revision.

2. **Legend-title and interaction semantics:** Plotly.js 3.4.0 adds clickable legend titles to toggle groups, multi-axis shape references and dashed marker lines. The research interpretation is: Interactive figure semantics depend on the JS engine revision and user action, not just a static image.

3. **Renderer/export patch and side effects:** Plotly.py 6.6.0 fixes a global warning-format side effect and a spurious write_image engine deprecation warning, and updates its underlying JS. The research interpretation is: A wrapper patch can change diagnostics/export interpretation independent of scientific data or plot recipe.

The stable technical mechanism is that changing software/specification versions can change which inputs, policies, parsers, environments, visual semantics, or evidence relations are possible. **Possibility ≠ realization**: any claim about realized behavior needs an identifiable repository revision, configuration and corresponding run/output evidence. The Stage Parts are conceptually connected through the repository's lens (scientific communication, versioned figure/rendering state, accessibility, reproducibility, uncertainty display and publisher transfer), not merged into a single experimental dataset.

## 5. Previous-stage delta, counterevidence and evidence maturity
- `NEW / STRENGTHENED`: selected release facts recorded in the Parts; new versioned source identities explicitly attached.
- `PERSISTENT`: render success != scientific validity; claim binding != entailment; uncertainty metadata != statistical validation; accessibility support != WCAG certification; checksum != independent reproduction.
- `NOT_COMPARABLE`: heterogeneous releases have no shared quantitative evaluator and are not a performance time series.
- Strong counter-reading: the apparent direction of progress partly reflects **source selection** and release-note authorship, not independent field-wide adoption.
- Source maturity: `PUBLISHED_UPSTREAM_RELEASE_RECORD`; independent downstream execution, conformance, scientific replication, user impact and `sci-render-kit` deployment are `UNKNOWN / NOT_TESTED`.
- No selected independent contrary source was examined; lack of reported contradiction is not a proof of universal agreement.

## 6. Temporal integrity and current repository assessment
Publisher release dates belong to 2026-Q1; the research and read date is 2026-10-19. No backdating as contemporary work. Earlier native Stages and old longitudinal files are preserved as their actual historical observations. This Stage identifies **no verified implementation drift** because it did **not** run a current-repository audit; it does not assert an all-clear. `NO_RUNTIME_CHANGE` and `NO_CONTRACT_CHANGE` are the changes enacted by this research-only artifact.

## 7. Review, limitations and handoff
See [RESEARCH_REVIEW.md](RESEARCH_REVIEW.md) for a same-producer review of temporal placement, source claims, negative space and boundary compliance. It is not independent review. See [STAGE_HANDOFF.md](STAGE_HANDOFF.md) for transferable research questions. Strongest limitations: single-origin release sources, source-bounded coverage, uneven monthly selection, absent independent reproduction, and no runtime/experiment verification.

## 8. Conclusion
`FRONTIER_STAGE_COMPLETE — SOURCE_BOUNDED_DOCUMENT_RESEARCH_ONLY`.

What was completed: a dated, independently navigable **research-documentation Stage**, with selected source facts, research Parts, month records, comparison and critical boundaries. What was not completed: a scientific validation of underlying software, runtime conformance check, exhaustive field synthesis or local experimental reproduction.
