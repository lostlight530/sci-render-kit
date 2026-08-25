# Frontier Alignment — 2026-08-25 / 2026-08-26 delta

**Repository:** `sci-render-kit`  
**Status:** research-positioning snapshot; non-normative companion to `RESEARCH_CONTRACT.md`  
**Scope:** scientific communication, claim-to-visual bindings, process disclosure, uncertainty semantics, accessibility, provenance and evidence-preserving figure artifacts in AI-assisted/autonomous research

## 1. Why this calibration exists

The role of scientific figures changes when more of the research lifecycle is produced or mediated by AI agents.

Recent 2026 signals are especially relevant:

- *Provenance grounds trust in autonomous science* (Nature Computational Science, 20 Aug 2026) argues that autonomous science needs complete, re-openable records of what was reasoned, done and measured so results can be audited and corrected.
- The Nature Computational Science editorial *Responsible and transparent use of AI in scientific publishing* (20 Aug 2026) emphasizes transparency, accountability and human oversight as AI becomes embedded across research and scientific communication.
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents* (arXiv:2608.18312, 18 Aug 2026) argues that model-call logging alone is insufficient and that claims, evidence, artifacts and verification records need portable audit relations.
- *EarthVerse* (arXiv:2608.23525, 24 Aug 2026) evaluates scientific agents on package-scoped investigations requiring heterogeneous evidence selection, transparent calculations, source reconciliation and provenance preservation; its results show that local answer-unit success can remain far above strict end-to-end consistency.

These publications do not validate this repository. They clarify why a rendered chart should be treated as an evidence-bearing research artifact with explicit claim and process context rather than only a visual output file.

## 2. Repository role in that frontier

`sci-render-kit` occupies the **evidence-aware scientific-communication plane**:

```text
research result + context + claim refs + uncertainty + process disclosure
        -> declarative recipe
        -> runtime visual/accessibility findings
        -> backend-bounded render
        -> manifest / provenance / accessibility sidecars
        -> publisher-target findings
        -> figure evidence envelope
```

The repository does not decide whether a scientific conclusion is true. It attempts to keep the transition from analysis to visual communication explicit enough that important semantics are not silently lost during rendering.

## 3. Why scientific communication needs an evidence contract

A conventional plotting API mainly answers:

> How should these values be drawn?

An evidence-aware figure pipeline also needs to answer:

- Which data or upstream artifact produced this figure?
- Which recipe/profile/backend was used?
- Which output bytes correspond to that execution?
- Which upstream claims is the figure declared to communicate?
- Which panel/series/visual object is declared to relate to which claim?
- What does the displayed uncertainty actually mean?
- Which accessibility cues were declared and emitted?
- Was AI assistance or human review declared for the communication step?
- Which publisher preset was targeted?
- Which runtime findings were warnings versus hard errors?
- What claims are explicitly **not** established by the figure?

This is the purpose of `render-manifest@2`, `provenance@2`, `a11y@1`, `figure-claim-binding@1`, `process-disclosure@1` and `figure-evidence@2`.

## 4. Claim-aware communication: the 2026-08-26 delta

Before today's update, the figure evidence record could carry upstream `claim_refs[]`, but it could not state which visual object was intended to communicate which claim.

Today the recipe contract adds explicit bindings:

```yaml
research_context:
  claim_refs: [claim_1, claim_2]
  claim_bindings:
    - visual_ref: panel:A
      claim_refs: [claim_2]
      relation: illustrates
      evidence_ref: evidence/run-042.evidence.json
```

The figure evidence profile is now:

```text
sci-render-kit/figure-evidence@2
```

with communication subprofile:

```text
sci-render-kit/figure-claim-binding@1
```

The renderer never infers these bindings from chart text, values or pixels:

```text
inferred_bindings: false
```

That makes the audit relation explicit without inventing an automatic scientific-interpretation engine.

Hard boundaries:

```text
visual binding != verified entailment
supports label != evidence sufficiency
illustrates label != causal support
claim reference != claim truth
```

## 5. Process disclosure at the communication layer

The recipe also gains optional:

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools:
    - provider/model or tool identifier declared by the author
  human_review: reviewed
  disclosure_ref: methods/figure-disclosure.md
```

This becomes:

```text
sci-render-kit/process-disclosure@1
```

inside `figure-evidence@2`.

The goal is transparent process context, not automated authorship or editorial judgment:

```text
AI disclosure != authorship adjudication
AI tool identity != output validity
human review != peer review
human review != truth
process disclosure != publisher compliance
```

Missing values become `not_declared`, not optimistic defaults.

## 6. EarthVerse and the communication end of end-to-end consistency

EarthVerse is useful because it exposes a broader scientific-agent failure mode: a system can do many individual subtasks correctly and still fail to preserve a consistent chain across evidence, units, calculations and interpretation.

The visualization step is one place where that chain can break silently.

Examples:

- a valid upstream claim is visualized with the wrong data subset;
- an uncertainty interval is drawn but its statistical meaning is lost;
- a figure caption suggests a stronger claim than the upstream evidence object supports;
- a multi-panel figure no longer makes clear which claim belongs to which panel.

`sci-render-kit` cannot automatically solve those scientific problems, but `figure-claim-binding@1`, uncertainty semantics and artifact identity make the communication transition more inspectable.

## 7. Provenance does not rescue misleading visualization

The growing emphasis on provenance in autonomous science should not be misread as permission to treat provenance as scientific validity.

```text
provenance != truth
replayable render != reproduced scientific result
checksum != correct analysis
claim binding != verified inference
publisher alignment != acceptance
accessible encoding != whole-publication conformance
beautiful figure != strong evidence
```

A perfectly traceable figure can still visualize a flawed analysis. The value of provenance is that the flaw can be located, inspected and corrected more reliably.

## 8. Uncertainty semantics are part of the artifact

AI-assisted pipelines make it especially easy to turn a pair of lower/upper bounds into a visually authoritative shaded interval without preserving what the interval means.

The repository therefore keeps uncertainty as a typed/declarative object rather than a styling option.

Examples remain intentionally distinct:

```text
standard deviation
standard error
confidence interval
credible interval
quantile interval
bootstrap interval
min-max range
heuristic bound
```

A renderer may faithfully draw any of them while still being unable to judge whether the upstream method was statistically appropriate.

That boundary is a feature, not a missing autonomous-judgment module.

## 9. Accessibility is scientific robustness, not decoration

The current WCAG 2.2-aligned project rules remain relevant to scientific communication because a figure that communicates a series only through hue can lose meaning for some readers or output conditions.

Current bounded principles include:

- provide text alternatives when required;
- do not rely on color as the only necessary information channel when redundant encoding is declared;
- check contrast for graphical objects/boundaries that are actually required for understanding against adjacent colors;
- keep all-pairs palette checks and CVD simulation labeled as project safeguards rather than universal WCAG mandates.

The repository therefore treats accessibility metadata as part of the figure evidence record, while keeping `conformance_claim: false`.

## 10. Relation to plotting and publication ecosystems

### Matplotlib / ggplot2 / Observable Plot

These are rendering ecosystems and remain valuable backend/tool layers. `sci-render-kit` should not compete with them on primitive plotting breadth.

Its contribution is the contract around rendering:

- declarative research context;
- explicit claim-to-visual communication links;
- uncertainty meaning;
- process disclosure;
- backend capability truth;
- artifact identity;
- provenance/accessibility sidecars;
- publisher-target alignment;
- cross-tool evidence handoff.

### Publisher figure guidance

Publisher profiles are practical targets, not scientific validators. A profile mismatch can warn that a declared output is poorly aligned with a submission target; a match cannot establish acceptance, editorial quality or scientific correctness.

### Autonomous-science systems

An autonomous scientific agent can generate an analysis and then call a plotting library directly. The missing question is whether the resulting visual artifact preserves enough upstream research context to be audited later.

That is the layer this repository is designed to provide.

## 11. Cross-repository interpretation

```text
auto-doc-engine
artifact / source packaging + declared AI/human-review context
        |
        v
epistemic-pipeline
claim-index@1 / evidence-envelope@2 / provider-review disclosure
        |
        v
sci-render-kit
figure-claim-binding@1 / uncertainty / accessibility / figure-evidence@2
```

A figure should therefore be able to reference upstream evidence without pretending to inherit upstream truth.

For example:

```text
claim_refs[]
claim_bindings[]
evidence_envelope_ref
provenance_ref
uncertainty.semantics
process_disclosure
```

are lineage/context/communication fields. They do not certify the underlying claim.

## 12. Research-engineering thesis

The repository's current thesis is:

> Scientific communication becomes more auditable when a figure is treated as a provenance-aware, claim-linked, process-disclosed and semantically bounded research artifact rather than an isolated image file.

This is intentionally narrower than claiming that automated visualization can validate science.

## 13. What should not be added merely because AI scientific publishing is accelerating

This calibration does **not** justify:

- an LLM that decides whether a figure is scientifically correct;
- automatic inference of visual-to-claim bindings;
- automatic journal-acceptance claims;
- converting every runtime warning into a hard gate;
- treating AI disclosure as authorship adjudication;
- treating human review as peer review;
- treating all palette-pair contrast as a universal WCAG requirement;
- silently renaming arbitrary bounds as confidence intervals;
- replacing mature rendering backends with a bespoke plotting engine;
- adding GitHub-native CI/merge governance as scientific architecture.

The pipeline should remain explicit, backend-bounded and evidence-preserving.

## 14. Primary external references

Checked through 2026-08-26:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). https://doi.org/10.1038/s43588-026-01035-4
2. **Responsible and transparent use of AI in scientific publishing.** Nature Computational Science 6, 803 (2026). https://doi.org/10.1038/s43588-026-01043-4
3. Yin X, Du M, Prince MH, Cherukara MJ. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents.** arXiv:2608.18312. https://arxiv.org/abs/2608.18312
4. Cui Z, et al. **EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards.** arXiv:2608.23525. https://arxiv.org/abs/2608.23525
5. Canty RB, Abolhasani M. **The past, present and future of self-driving laboratories.** Nature Reviews Chemistry 10, 523–537 (2026). https://doi.org/10.1038/s41570-026-00847-2
6. W3C WCAG 2.2 — Understanding SC 1.4.11 Non-text Contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast

## 15. Bottom line

`sci-render-kit` is not another plotting library. Its research-engineering role is to preserve **scientific communication semantics**—especially claim bindings, uncertainty, process disclosure, provenance, accessibility and artifact identity—across the final transition from research result to figure.
