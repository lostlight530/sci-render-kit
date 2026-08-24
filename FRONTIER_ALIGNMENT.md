# Frontier Alignment — 2026-08-25

**Repository:** `sci-render-kit`  
**Status:** research-positioning snapshot; non-normative companion to `RESEARCH_CONTRACT.md`  
**Scope:** scientific communication, uncertainty semantics, accessibility, provenance and evidence-preserving figure artifacts in AI-assisted/autonomous research

## 1. Why this calibration exists

The role of scientific figures changes when more of the research lifecycle is produced or mediated by AI agents.

Two 2026 signals are especially relevant:

- *Provenance grounds trust in autonomous science* (Nature Computational Science, 20 Aug 2026) argues that autonomous science needs complete, re-openable records of what was reasoned, done and measured so results can be audited and corrected.
- The Nature Computational Science editorial *Responsible and transparent use of AI in scientific publishing* (20 Aug 2026) emphasizes transparency, accountability and human oversight as AI becomes embedded across research and scientific communication.

These publications do not validate this repository. They clarify why a rendered chart should be treated as an evidence-bearing research artifact rather than only a visual output file.

## 2. Repository role in that frontier

`sci-render-kit` occupies the **evidence-aware scientific-communication plane**:

```text
research result + context + uncertainty semantics
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
- What does the displayed uncertainty actually mean?
- Which accessibility cues were declared and emitted?
- Which publisher preset was targeted?
- Which runtime findings were warnings versus hard errors?
- What claims are explicitly **not** established by the figure?

This is the purpose of `render-manifest@2`, `provenance@2`, `a11y@1` and `figure-evidence@1`.

## 4. Provenance does not rescue misleading visualization

The growing emphasis on provenance in autonomous science should not be misread as permission to treat provenance as scientific validity.

```text
provenance != truth
replayable render != reproduced scientific result
checksum != correct analysis
publisher alignment != acceptance
accessible encoding != whole-publication conformance
beautiful figure != strong evidence
```

A perfectly traceable figure can still visualize a flawed analysis. The value of provenance is that the flaw can be located, inspected and corrected more reliably.

## 5. Uncertainty semantics are part of the artifact

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

## 6. Accessibility is scientific robustness, not decoration

The current WCAG 2.2-aligned project rules remain relevant to scientific communication because a figure that communicates a series only through hue can lose meaning for some readers or output conditions.

Current bounded principles include:

- provide text alternatives when required;
- do not rely on color as the only necessary information channel when redundant encoding is declared;
- check contrast for graphical objects/boundaries that are actually required for understanding against adjacent colors;
- keep all-pairs palette checks and CVD simulation labeled as project safeguards rather than universal WCAG mandates.

The repository therefore treats accessibility metadata as part of the figure evidence record, while keeping `conformance_claim: false`.

## 7. Relation to plotting and publication ecosystems

### Matplotlib / ggplot2 / Observable Plot

These are rendering ecosystems and remain valuable backend/tool layers. `sci-render-kit` should not compete with them on primitive plotting breadth.

Its contribution is the contract around rendering:

- declarative research context;
- uncertainty meaning;
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

## 8. Cross-repository interpretation

```text
auto-doc-engine
artifact / source packaging
        |
        v
epistemic-pipeline
claims / evidence / conflicts / lineage
        |
        v
sci-render-kit
uncertainty-aware scientific communication / figure evidence
```

A figure should therefore be able to reference upstream evidence without pretending to inherit upstream truth.

For example:

```text
claim_refs[]
evidence_envelope_ref
provenance_ref
uncertainty.semantics
```

are lineage/context fields. They do not certify the underlying claim.

## 9. Research-engineering thesis

The repository's current thesis is:

> Scientific communication becomes more auditable when a figure is treated as a reproducible, provenance-aware and semantically bounded research artifact rather than an isolated image file.

This is intentionally narrower than claiming that automated visualization can validate science.

## 10. What should not be added merely because AI scientific publishing is accelerating

This calibration does **not** justify:

- an LLM that decides whether a figure is scientifically correct;
- automatic journal-acceptance claims;
- converting every runtime warning into a hard gate;
- treating all palette-pair contrast as a universal WCAG requirement;
- silently renaming arbitrary bounds as confidence intervals;
- replacing mature rendering backends with a bespoke plotting engine;
- adding GitHub-native CI/merge governance as scientific architecture.

The pipeline should remain explicit, backend-bounded and evidence-preserving.

## 11. Primary external references

Checked 2026-08-25:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). DOI: https://doi.org/10.1038/s43588-026-01035-4
2. **Responsible and transparent use of AI in scientific publishing.** Nature Computational Science 6, 803 (2026). DOI: https://doi.org/10.1038/s43588-026-01043-4
3. Canty RB, Abolhasani M. **The past, present and future of self-driving laboratories.** Nature Reviews Chemistry 10, 523–537 (2026). DOI: https://doi.org/10.1038/s41570-026-00847-2
4. W3C WCAG 2.2 — Understanding SC 1.4.11 Non-text Contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
5. W3C WCAG 2.2 Understanding documents: https://www.w3.org/WAI/WCAG22/understanding/

## 12. Bottom line

`sci-render-kit` is not another plotting library. Its research-engineering role is to preserve **scientific communication semantics**—especially uncertainty, provenance, accessibility and artifact identity—across the final transition from research result to figure.
