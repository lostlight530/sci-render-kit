# 2026-Q4 / 10 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/sci-render-kit`; research month: `2026-10-01 through 2026-10-19`
- Stage owner: `L / 2026-Q4`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_OPEN — as of 2026-10-19`

## Selected events and evidence
### 2026-10-05 — Resize observer and responsive layout
- **Primary source:** https://github.com/plotly/plotly.js/releases/tag/v4.1.2 (`plotly/plotly.js@v4.1.2`, `S13`)
- **Publisher-described observation:** Plotly.js 4.1.2 changes responsive resizing to ResizeObserver instead of window resize events and documents image-export config in schema.
- **Analytic implication:** Viewport and host resize events are observable parts of interactive-figure reproducibility; host layout can modify what a recipient sees.
- **Alternative / qualification:** Responsiveness is not accessibility validation, scientific claim validation or guaranteed behavior in all host environments.
- **Research owner:** `L1` in this Stage; one originating source family, no independent validation.

### 2026-10-08 — Image-mark alignment correction
- **Primary source:** https://github.com/vega/vega-lite/releases/tag/v6.5.0 (`vega/vega-lite@v6.5.0`, `S14`)
- **Publisher-described observation:** Vega-Lite 6.5.0 fixes image-mark center alignment when a secondary channel is undefined.
- **Analytic implication:** Compiler revision changes spatial interpretation of a declarative spec even without changed data.
- **Alternative / qualification:** A scoped alignment fix is not an independent cross-version equivalence test.
- **Research owner:** `L2` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O13 / S13 (plotly.js v4.1.2), O14 / S14 (vega-lite v6.5.0) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. render success != scientific validity; claim binding != entailment; uncertainty metadata != statistical validation; accessibility support != WCAG certification; checksum != independent reproduction.
No `sci-render-kit` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.


## A1_STAGE_L_CONTENT_DECISIONS_2026_10_29

- Review producer: external independent GPT; exact source main `3396dfc98fdf43c788621374969a2200111a448d`; A1 Oct01–28 at N=Oct29 Asia/Shanghai.
- Stage-L native selection is event/state-triggered; do not invent a missing Daily on calendar days without a declared trigger.
- Current Stage-L selection is two versioned releases, O13/S13 Plotly.js and O14/S14 Vega-Lite; two source families are not a controlled experiment.
- Original source cutoff 2026-10-19; this new maintenance cutoff 2026-10-28 does not retroactively insert days into the original study.
- Source artifact scope: eight Stage-L dossier files and ten supporting acceptance/source-selection/longitudinal/router owners. Each receives a typed decision below.
- Method: native GitHub repository read, original Stage-L authorial text and bounded Oct19/28 evidence; no complete local repository build or browser-assisted figure inspection.
- W44 and October are OPEN; scientific Stage L Q4 final and calendar-month final not yet due.
- Earlier source/path-custody verdict `SEMANTIC_NOT_FULLY_ATTESTED` remains in force outside this 18-owner review.
- Rule: plot render success != scientific validity; claim binding != entailment; uncertainty metadata != calibrated coverage; schema support != WCAG certification.
- A1 review is a bounded content assessment; it does not authorize retrospective publisher acceptance, peer review or independent reproducibility claims.

### Per-original-artifact decisions
### R01 — `maintenance/frontier-research/stage-l-2026-q4/STAGE_BRIEF.md`
- Current Git source identity: `96129b7b7b3c…`; original dated owner and source attribution retained.
- Actual content judgment: research Q4 open, Oct19 cutoff, retrospective official release selection.
- SOP action **NO_FOLLOW_UP**; inferential boundary: Not preregistration or completed October; no output parity evidence.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R02 — `maintenance/frontier-research/stage-l-2026-q4/SOURCE_OBJECT_REGISTER.md`
- Current Git source identity: `304447c8189f…`; original dated owner and source attribution retained.
- Actual content judgment: O13/S13 Plotly.js v4.1.2 Oct05 and O14/S14 Vega-Lite v6.5.0 Oct08.
- SOP action **NO_FOLLOW_UP**; inferential boundary: Publisher release notes, not replicated implementation or user adoption.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R03 — `maintenance/frontier-research/stage-l-2026-q4/EVIDENCE_CHART.md`
- Current Git source identity: `a241e560d286…`; original dated owner and source attribution retained.
- Actual content judgment: F-L1 ResizeObserver response and F-L2 image-mark placement fix.
- SOP action **NO_FOLLOW_UP**; inferential boundary: Source assertion and researcher interpretation separated.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R04 — `maintenance/frontier-research/stage-l-2026-q4/L1_PLOTLYJS_V412.md`
- Current Git source identity: `eb7b941a5d73…`; original dated owner and source attribution retained.
- Actual content judgment: responsive resizing/host and export config from Plotly.js 4.1.2.
- SOP action **NO_FOLLOW_UP**; inferential boundary: No pixel-level layout comparison across host environments.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R05 — `maintenance/frontier-research/stage-l-2026-q4/L2_VEGALITE_V650.md`
- Current Git source identity: `e0e5bdf11779…`; original dated owner and source attribution retained.
- Actual content judgment: undefined secondary-channel image-mark center alignment in Vega-Lite 6.5.0.
- SOP action **NO_FOLLOW_UP**; inferential boundary: No local Vega-Lite compiler or figure parity replay.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R06 — `maintenance/frontier-research/stage-l-2026-q4/MONTH_2026_10_RECONSTRUCTION.md`
- Current Git source identity: `64faa2d1d877…`; original dated owner and source attribution retained.
- Actual content judgment: Oct05/08 native October research selection ending Oct19.
- SOP action **APPEND_RELATION**; inferential boundary: Current Oct29 maintenance cannot add November or close Q4.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R07 — `maintenance/frontier-research/stage-l-2026-q4/RESEARCH_REVIEW.md`
- Current Git source identity: `45728146f375…`; original dated owner and source attribution retained.
- Actual content judgment: self-review and partial methodological/source coverage.
- SOP action **NO_FOLLOW_UP**; inferential boundary: No independent render/accessibility science review.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R08 — `maintenance/frontier-research/stage-l-2026-q4/CONTRIBUTOR_STATEMENT.md`
- Current Git source identity: `750ab55a1d1d…`; original dated owner and source attribution retained.
- Actual content judgment: original ChatGPT-assisted Stage researcher attribution.
- SOP action **NO_FOLLOW_UP**; inferential boundary: External maintenance is not independent technical reviewer.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R09 — `maintenance/frontier-research/annotations/2026-10-19_STAGE_I_L_PRIMARY_RELEASE_AND_STRUCTURE_AUDIT.md`
- Current Git source identity: `60ff50620834…`; original dated owner and source attribution retained.
- Actual content judgment: selected publisher releases and stage-route structural audit.
- SOP action **BOUNDARY_UPDATE**; inferential boundary: Release-tag/route checks do not prove figure export, WCAG or claim entailment.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R10 — `maintenance/frontier-research/annotations/2026-10-28_A1_STAGE_SOURCE_CUSTODY.md`
- Current Git source identity: `a44ca4d79f11…`; original dated owner and source attribution retained.
- Actual content judgment: Oct01–27 360 tree entries and custody ledger, no rendering experiment.
- SOP action **BOUNDARY_UPDATE**; inferential boundary: Metadata census does not equal semantic contract examination.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R11 — `maintenance/frontier-research/annotations/2026-10-28_A2_STAGE_MONTH_RELATION.md`
- Current Git source identity: `2609f1d34909…`; original dated owner and source attribution retained.
- Actual content judgment: previous Oct28 relation inherited merged A1 source blob.
- SOP action **BOUNDARY_UPDATE**; inferential boundary: Prior current-main ancestor does not upgrade output parity evidence.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R12 — `maintenance/frontier-research/annotations/2026-10-28_MINIMAL_SOP_ACCEPTANCE_AUDIT.md`
- Current Git source identity: `7697010a3a8d…`; original dated owner and source attribution retained.
- Actual content judgment: SOP acceptance explicitly partial; no runtime science pass.
- SOP action **NO_FOLLOW_UP**; inferential boundary: Preserve status rather than silently mark checklist complete.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R13 — `maintenance/frontier-research/annotations/2026-10-28_OCTOBER_NATIVE_STAGE_GAP_RECOVERY_REGISTER.md`
- Current Git source identity: `17afcaf5aa58…`; original dated owner and source attribution retained.
- Actual content judgment: stage-triggered owner no false Daily due; checkpoint correction.
- SOP action **NO_FOLLOW_UP**; inferential boundary: D30 not due and missing named D7 file not itself an audit failure.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R14 — `maintenance/frontier-research/annotations/PARALLEL_SOURCE_SELECTION_RECONCILIATION_2026-10-19.md`
- Current Git source identity: `d1052bf1c8b4…`; original dated owner and source attribution retained.
- Actual content judgment: older PR #146 conflicted with newer native Stages.
- SOP action **NO_FOLLOW_UP**; inferential boundary: Candidate sources remain NOT_STAGE_ADMITTED.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R15 — `maintenance/frontier-research/annotations/expansion/2026-10-19_ALTAIR_620_INTERACTION_SOURCE_CANDIDATE.md`
- Current Git source identity: `2b8193be7b30…`; original dated owner and source attribution retained.
- Actual content judgment: superseded PR #150 Altair 6.2.0 interaction source candidate.
- SOP action **NO_FOLLOW_UP**; inferential boundary: Wrappers/candidates not silently accepted into original Stage.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R16 — `maintenance/frontier-research/annotations/expansion/2026-10-19_STAGE_I_K_PLOTLY_WRAPPER_SOURCE_DELTA.md`
- Current Git source identity: `c6826a4bf5fc…`; original dated owner and source attribution retained.
- Actual content judgment: retrospective Plotly.py wrapper expansion in I/K research chronology.
- SOP action **NO_FOLLOW_UP**; inferential boundary: Not a Stage owner update, current defect or wrapper equivalence proof.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R17 — `maintenance/frontier-research/longitudinal/LONGITUDINAL_SYNTHESIS_2026_YTD_2026-10-19.md`
- Current Git source identity: `0a5b90e54ca8…`; original dated owner and source attribution retained.
- Actual content judgment: Jan–Oct19 YTD I/J/K closed docs and L open.
- SOP action **NO_FOLLOW_UP**; inferential boundary: Do not infer Q4 or annual final, scientific truth or publisher approval.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### R18 — `MANIFEST.yaml`
- Current Git source identity: `2fff5d86a37d…`; original dated owner and source attribution retained.
- Actual content judgment: Oct23 manifest version and typed recipe/claim binding principles.
- SOP action **BOUNDARY_UPDATE**; inferential boundary: No browser visual/WCAG QA or local network/tool execution claimed.
- No original research file rewritten, no new local test, and no independent effect/result credit; successor relation lives in this October owner.
### October continuity, semantic conflicts and next test triggers
- O13 is the Plotly.js v4.1.2 release, not arbitrary Plotly.py wrapper objects; wrapper release candidates must not be collapsed into O13.
- O14 is the Vega-Lite v6.5.0 release, not the Altair 6.2.0 client-side wrapper candidate.
- ResizeObserver changes event observation. It does not prove identical viewport rendering, visual stability or export output on every recipient host.
- Vega-Lite's image-mark alignment change is conditional on undefined secondary channels; it does not imply all figure geometry is equivalent across compiler versions.
- Declarative recipe and underlying data version can remain constant while compiler layout changes; a true parity test requires pinned compiler and rendered artifact.
- Figure attachment hash and versioned recipe identity establish object custody, not reviewer-confirmed semantic equivalence.
- A human-accessible label or ARIA field in source format is not itself a browser-based assistive technology evaluation.
- Source-author review is same-producer quality check; a downstream independent reproduction requires a different verification actor and actual fixture outputs.
- Publisher release descriptions have direct authority for their claimed release, but cannot independently certify scientific content or this repository's runtime.
- The YTD longitudinal record holds I/J/K as source-bounded research documentation and Q4 OPEN; no annual publishable completion inferred.
- Prior parallel proposal #146 and #150 are research-source candidate history, not two new original Stage-L research outputs.
- No new permanent governance or compatibility rule can be promoted solely from this candidate and current source custody review.
- The Oct23 current manifest is a declared contract; native browser visual QA is explicitly not executed in its claimed surface.
- An actual renderer regression must capture exact input spec, engine version, target host, pixel/semantic diff and reviewed claim binding before marking PASS.
- To qualify scientific uncertainty display, need explicit uncertainty interval/statistical assumptions and validated chart mapping, not cosmetic presence.
- No new 2026-10-20..28 original Stage release events admitted without dated source-selection amendment and chart/review reconciliation.
- Cross-repository shared release identity is not independent confirmation; cite one publisher source family once per unique claim.
- D30 Oct30 audit is future at this source cutoff; D7/D10/D14 are checkpoint windows, not necessarily separate filenames.
- A1 current judgment: `BOUNDED_NATIVE_STAGE_DOCUMENT_REVIEW`; full source-corpus code/render semantic audit still `PARTIAL / NOT_ATTESTED`.
- Historical source-time findings preserved; only new successor section in October Stage-L monthly owner changed.


## A2_STAGE_L_MONTH_RELATION_2026_10_29_SCI

- Ten-repository A1 prerequisite: all 10 first-round PRs merged before branch; inherited exact `main=cbea0d55e969237445bb7ed7cfaa2c13c02ff2e6` and A1 month-owner blob `c6e5387abac99eb49be2b088cf7133997eb4f888`.
- Relation window Oct01–29 Asia/Shanghai. Original Stage-L selected source window remains bounded through Oct19; Oct20–29 GitHub maintenance is not another original research-stage episode.
- No new 2026-10-29 native Stage original trigger or independent same-day experiment was observed in current repository evidence; outcome for unobserved trigger = UNKNOWN/NOT_DUE_UNLESS_TRIGGERED.
- A1 per-document content decisions below are inherited from exact merged month owner; this A2 only maps their month-wide relations and Oct29 state, not a new review of all upstream releases.
- Stage-L quarter 2026-Q4 OPEN, 2026 YTD YEAR_OPEN, October natural month final NOT_DUE and D30 Oct30 checkpoint NOT_DUE.
- No fresh native tool, renderer, SDK, paper replication or CI test executed in this A2; all such evidence remains as explicitly recorded by original sources.
### Inherited source-owner and evidence-chain relationships
#### R01 — `maintenance/frontier-research/stage-l-2026-q4/STAGE_BRIEF.md`
- Source: Current Git source identity: `96129b7b7b3c…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: research Q4 open, Oct19 cutoff, retrospective official release selection.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: Not preregistration or completed October; no output parity evidence.
- A2 relation: source owner R01 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/stage-l-2026-q4/STAGE_BRIEF.md`; require forward method amendment plus new execution identity before research authority changes.
#### R02 — `maintenance/frontier-research/stage-l-2026-q4/SOURCE_OBJECT_REGISTER.md`
- Source: Current Git source identity: `304447c8189f…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: O13/S13 Plotly.js v4.1.2 Oct05 and O14/S14 Vega-Lite v6.5.0 Oct08.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: Publisher release notes, not replicated implementation or user adoption.
- A2 relation: source owner R02 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/stage-l-2026-q4/SOURCE_OBJECT_REGISTER.md`; require forward method amendment plus new execution identity before research authority changes.
#### R03 — `maintenance/frontier-research/stage-l-2026-q4/EVIDENCE_CHART.md`
- Source: Current Git source identity: `a241e560d286…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: F-L1 ResizeObserver response and F-L2 image-mark placement fix.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: Source assertion and researcher interpretation separated.
- A2 relation: source owner R03 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/stage-l-2026-q4/EVIDENCE_CHART.md`; require forward method amendment plus new execution identity before research authority changes.
#### R04 — `maintenance/frontier-research/stage-l-2026-q4/L1_PLOTLYJS_V412.md`
- Source: Current Git source identity: `eb7b941a5d73…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: responsive resizing/host and export config from Plotly.js 4.1.2.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: No pixel-level layout comparison across host environments.
- A2 relation: source owner R04 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/stage-l-2026-q4/L1_PLOTLYJS_V412.md`; require forward method amendment plus new execution identity before research authority changes.
#### R05 — `maintenance/frontier-research/stage-l-2026-q4/L2_VEGALITE_V650.md`
- Source: Current Git source identity: `e0e5bdf11779…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: undefined secondary-channel image-mark center alignment in Vega-Lite 6.5.0.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: No local Vega-Lite compiler or figure parity replay.
- A2 relation: source owner R05 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/stage-l-2026-q4/L2_VEGALITE_V650.md`; require forward method amendment plus new execution identity before research authority changes.
#### R06 — `maintenance/frontier-research/stage-l-2026-q4/MONTH_2026_10_RECONSTRUCTION.md`
- Source: Current Git source identity: `64faa2d1d877…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: Oct05/08 native October research selection ending Oct19.
- Evidence boundary: SOP action **APPEND_RELATION**; inferential boundary: Current Oct29 maintenance cannot add November or close Q4.
- A2 relation: source owner R06 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/stage-l-2026-q4/MONTH_2026_10_RECONSTRUCTION.md`; require forward method amendment plus new execution identity before research authority changes.
#### R07 — `maintenance/frontier-research/stage-l-2026-q4/RESEARCH_REVIEW.md`
- Source: Current Git source identity: `45728146f375…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: self-review and partial methodological/source coverage.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: No independent render/accessibility science review.
- A2 relation: source owner R07 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/stage-l-2026-q4/RESEARCH_REVIEW.md`; require forward method amendment plus new execution identity before research authority changes.
#### R08 — `maintenance/frontier-research/stage-l-2026-q4/CONTRIBUTOR_STATEMENT.md`
- Source: Current Git source identity: `750ab55a1d1d…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: original ChatGPT-assisted Stage researcher attribution.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: External maintenance is not independent technical reviewer.
- A2 relation: source owner R08 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/stage-l-2026-q4/CONTRIBUTOR_STATEMENT.md`; require forward method amendment plus new execution identity before research authority changes.
#### R09 — `maintenance/frontier-research/annotations/2026-10-19_STAGE_I_L_PRIMARY_RELEASE_AND_STRUCTURE_AUDIT.md`
- Source: Current Git source identity: `60ff50620834…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: selected publisher releases and stage-route structural audit.
- Evidence boundary: SOP action **BOUNDARY_UPDATE**; inferential boundary: Release-tag/route checks do not prove figure export, WCAG or claim entailment.
- A2 relation: source owner R09 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/annotations/2026-10-19_STAGE_I_L_PRIMARY_RELEASE_AND_STRUCTURE_AUDIT.md`; require forward method amendment plus new execution identity before research authority changes.
#### R10 — `maintenance/frontier-research/annotations/2026-10-28_A1_STAGE_SOURCE_CUSTODY.md`
- Source: Current Git source identity: `a44ca4d79f11…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: Oct01–27 360 tree entries and custody ledger, no rendering experiment.
- Evidence boundary: SOP action **BOUNDARY_UPDATE**; inferential boundary: Metadata census does not equal semantic contract examination.
- A2 relation: source owner R10 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/annotations/2026-10-28_A1_STAGE_SOURCE_CUSTODY.md`; require forward method amendment plus new execution identity before research authority changes.
#### R11 — `maintenance/frontier-research/annotations/2026-10-28_A2_STAGE_MONTH_RELATION.md`
- Source: Current Git source identity: `2609f1d34909…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: previous Oct28 relation inherited merged A1 source blob.
- Evidence boundary: SOP action **BOUNDARY_UPDATE**; inferential boundary: Prior current-main ancestor does not upgrade output parity evidence.
- A2 relation: source owner R11 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/annotations/2026-10-28_A2_STAGE_MONTH_RELATION.md`; require forward method amendment plus new execution identity before research authority changes.
#### R12 — `maintenance/frontier-research/annotations/2026-10-28_MINIMAL_SOP_ACCEPTANCE_AUDIT.md`
- Source: Current Git source identity: `7697010a3a8d…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: SOP acceptance explicitly partial; no runtime science pass.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: Preserve status rather than silently mark checklist complete.
- A2 relation: source owner R12 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/annotations/2026-10-28_MINIMAL_SOP_ACCEPTANCE_AUDIT.md`; require forward method amendment plus new execution identity before research authority changes.
#### R13 — `maintenance/frontier-research/annotations/2026-10-28_OCTOBER_NATIVE_STAGE_GAP_RECOVERY_REGISTER.md`
- Source: Current Git source identity: `17afcaf5aa58…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: stage-triggered owner no false Daily due; checkpoint correction.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: D30 not due and missing named D7 file not itself an audit failure.
- A2 relation: source owner R13 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/annotations/2026-10-28_OCTOBER_NATIVE_STAGE_GAP_RECOVERY_REGISTER.md`; require forward method amendment plus new execution identity before research authority changes.
#### R14 — `maintenance/frontier-research/annotations/PARALLEL_SOURCE_SELECTION_RECONCILIATION_2026-10-19.md`
- Source: Current Git source identity: `d1052bf1c8b4…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: older PR #146 conflicted with newer native Stages.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: Candidate sources remain NOT_STAGE_ADMITTED.
- A2 relation: source owner R14 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/annotations/PARALLEL_SOURCE_SELECTION_RECONCILIATION_2026-10-19.md`; require forward method amendment plus new execution identity before research authority changes.
#### R15 — `maintenance/frontier-research/annotations/expansion/2026-10-19_ALTAIR_620_INTERACTION_SOURCE_CANDIDATE.md`
- Source: Current Git source identity: `2b8193be7b30…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: superseded PR #150 Altair 6.2.0 interaction source candidate.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: Wrappers/candidates not silently accepted into original Stage.
- A2 relation: source owner R15 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/annotations/expansion/2026-10-19_ALTAIR_620_INTERACTION_SOURCE_CANDIDATE.md`; require forward method amendment plus new execution identity before research authority changes.
#### R16 — `maintenance/frontier-research/annotations/expansion/2026-10-19_STAGE_I_K_PLOTLY_WRAPPER_SOURCE_DELTA.md`
- Source: Current Git source identity: `c6826a4bf5fc…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: retrospective Plotly.py wrapper expansion in I/K research chronology.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: Not a Stage owner update, current defect or wrapper equivalence proof.
- A2 relation: source owner R16 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/annotations/expansion/2026-10-19_STAGE_I_K_PLOTLY_WRAPPER_SOURCE_DELTA.md`; require forward method amendment plus new execution identity before research authority changes.
#### R17 — `maintenance/frontier-research/longitudinal/LONGITUDINAL_SYNTHESIS_2026_YTD_2026-10-19.md`
- Source: Current Git source identity: `0a5b90e54ca8…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: Jan–Oct19 YTD I/J/K closed docs and L open.
- Evidence boundary: SOP action **NO_FOLLOW_UP**; inferential boundary: Do not infer Q4 or annual final, scientific truth or publisher approval.
- A2 relation: source owner R17 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `maintenance/frontier-research/longitudinal/LONGITUDINAL_SYNTHESIS_2026_YTD_2026-10-19.md`; require forward method amendment plus new execution identity before research authority changes.
#### R18 — `MANIFEST.yaml`
- Source: Current Git source identity: `2fff5d86a37d…`; original dated owner and source attribution retained.
- Current A1 judgment: Actual content judgment: Oct23 manifest version and typed recipe/claim binding principles.
- Evidence boundary: SOP action **BOUNDARY_UPDATE**; inferential boundary: No browser visual/WCAG QA or local network/tool execution claimed.
- A2 relation: source owner R18 remains original historical/Stage provenance; its October 1–28 judgment is inherited by exact A1 blob and cannot be promoted to a newly executed Oct29 Stage Part.
- Current-state action: retain the original selected/candidate/correction distinction for `MANIFEST.yaml`; require forward method amendment plus new execution identity before research authority changes.
### Oct29 original trigger check, selected-object chronology and independent authority
- L01: Stage-L October selected source O13/S13 Plotly.js v4.1.2 observed Oct05; native release family only.
- L02: Stage-L October selected O14/S14 Vega-Lite v6.5.0 observed Oct08; native source family differs from Plotly.
- L03: F-L1 ResizeObserver responsiveness is not byte-identical export layout across hosts.
- L04: F-L2 conditional image-mark center behavior does not prove figure-scientific truth or cross-version geometry parity.
- L05: Plotly.py wrapper candidate in historical I/K is distinct from selected Plotly.js stage object O13.
- L06: Altair interaction v6.2.0 candidate is not native Vega-Lite O14 selected-source amendment.
- L07: Source recipe and data identity alone do not certify actual rendered artifact or accessibility for users.
- L08: Browser visual WCAG and assistive-technology checks have NOT_EXECUTED evidence in current manifest.
- L09: Independent renderer replay requires pinned input, versions, environment, screenshot/structure diff and review.
- L10: Stage-L month Oct19 source cutoff and Oct29 current audit cutoff are separate; Nov/Dec Q4 still future.
### A2 evidence boundaries and governance
- Prior A1 was source-bounded content review of named owners; this A2 does not claim complete historical corpus/paper semantic verification.
- Stage-document presence is not experimental evidence, and missing date-specific Stage file is not necessarily missed scheduled Daily.
- October 2026 current month remains open; selected source families, version identity, reviewer independence, runtime status and factual conclusions remain distinct.
- Do not add invented 2026-10-29 original source ID, study Part, benchmark, source registry entry, final synthesis or contributor identity.
- D7/D10/D14 checkpoint statuses must come from owning logs/runner receipts, not filenames; D30 is not due Oct29.
- No original Stage I–L files, historical corrections, candidates, runtime code, MANIFEST or provenance records were modified.
- Actual verification performed: GitHub current main and A1 blob read; current source owner content relation and scoped pull-request diff checked.
- Actual verification not performed: full repo execution, live dependency conformance, independent upstream verification and scientific replication.
- A2 acceptance: OCT_MONTH_RELATION_AND_SELECTED_SOURCE_GOVERNANCE_UPDATED / BROADER_SEMANTIC_AND_RUNTIME_EVIDENCE_PARTIAL.
