# Research Contract — sci-render-kit

**Status:** active architecture contract  
**Calibrated:** 2026-08-27

`sci-render-kit` is the scientific-communication plane of the research toolchain. It compiles a declared recipe into a backend-bounded figure plus inspectable evidence. It does **not** decide whether the underlying scientific conclusion is true.

## 1. Canonical flow

```text
recipe + data + research_context + claim_bindings + uncertainty + process_disclosure
  -> P0 schema
  -> P1 runtime findings
  -> backend capability resolution
  -> render
  -> render-manifest / provenance / accessibility sidecars
  -> P2 artifact-integrity findings
  -> P3 publisher-target findings
  -> figure-evidence
```

P0–P3 are runtime phases, not GitHub merge gates.

## 2. Stable project identifiers

Project-owned profiles use stable semantic identifiers and do not carry decorative release suffixes:

```text
sci-render-kit/runtime-quality
sci-render-kit/render-manifest
sci-render-kit/provenance
sci-render-kit/a11y
sci-render-kit/figure-claim-binding
sci-render-kit/figure-claim-audit
sci-render-kit/process-disclosure
sci-render-kit/figure-evidence
```

Do not append `@1`, `@2`, `/v1` or similar counters unless the repository later adopts an actual compatibility/versioning regime.

This rule does **not** remove real external or runtime versions. Examples that remain valid evidence include WCAG 2.2, RO-Crate 1.3, CFF 1.2.0, the actual Matplotlib/NumPy/Python/ggplot2 versions used for a render, and the pinned Observable Plot dependency.

## 3. Scientific-integrity boundary

A successful render does not prove:

- scientific truth or causal validity;
- statistical significance or adequate sample size;
- correct preprocessing, missing-data treatment or uncertainty estimation;
- logical entailment from a claim binding;
- source credibility or evidence sufficiency;
- authorship, originality or peer review;
- journal acceptance or whole-publication accessibility;
- independent reproduction of a scientific result.

The evidence record therefore keeps explicit false claims for scientific, statistical, causal, authorship, peer-review and publisher-acceptance status.

## 4. Runtime validation semantics

The active catalog is `quality/rules.yaml` with profile `sci-render-kit/runtime-quality`.

- `error`: the declared render/artifact contract cannot currently be satisfied;
- `warning`: retain as evidence without upgrading to scientific failure;
- `info`: explanatory observation.

`runtime_validation` is structured process evidence, not a scientific-validity verdict.

## 5. Claim-to-visual communication

Figure-level references:

```yaml
research_context:
  claim_refs: [claim_1, claim_2]
```

Visual-level bindings:

```yaml
research_context:
  claim_bindings:
    - visual_ref: panel:A
      claim_refs: [claim_2]
      relation: illustrates
      evidence_ref: evidence/run-042.evidence.json
```

Allowed relation labels are `supports`, `illustrates`, `contextualizes`, `compares`, and `derived-from`.

These are declared communication semantics only. The renderer does not infer bindings from titles, legends, pixels, labels, prose or data values.

```text
claim reference != claim truth
visual binding != verified entailment
supports label != evidence sufficiency
illustrates label != causal support
```

`core/claim_binding_audit.py` checks declared metadata consistency only. It does not inspect pixels, dereference remote evidence, verify citations or adjudicate truth.

## 6. Process disclosure

Recipes may declare:

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools: [declared-tool-id]
  human_review: reviewed
  disclosure_ref: methods/figure-disclosure.md
```

Allowed values:

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

Missing values remain `not_declared`. Tool/provider/model identifiers are declarations, not vendor-verified provenance.

```text
AI disclosure != authorship adjudication
human review != peer review
human review != truth
process disclosure != publisher compliance
```

## 7. Uncertainty semantics

Supported declared kinds include:

```text
standard-error
standard-deviation
confidence-interval
credible-interval
min-max-range
quantile-interval
bootstrap-interval
heuristic-bound
```

Every uncertainty declaration should preserve its human-readable semantics and, when applicable, level/source context.

Lower/upper bounds alone do not establish a confidence interval, credible interval or probability model.

## 8. Artifact identity and evidence

### Render manifest

All active backends emit `sci-render-kit/render-manifest`. The record preserves available recipe/data/profile/output identities and backend/runtime context.

### Matplotlib provenance

The Matplotlib path emits `sci-render-kit/provenance`, including actual runtime/library versions where available. These real versions are provenance and must not be replaced with guessed values.

### Accessibility sidecar

When accessibility is declared, the unified path emits `sci-render-kit/a11y` with `conformance_claim: false`.

### Figure evidence

The unified CLI emits `sci-render-kit/figure-evidence`, which can reference:

- figure bytes and SHA-256;
- recipe/profile identities;
- render manifest, provenance and accessibility sidecars;
- upstream artifact/evidence/provenance references;
- declared claim communication;
- process disclosure;
- uncertainty semantics;
- runtime findings;
- local reproducibility state.

It is a project-owned handoff record, not an external standard.

## 9. Reproducibility levels

These are local project terms:

- **R0 — Traceable**: figure and declared sources can be associated;
- **R1 — Replay-addressable**: stable recipe/data/profile/output identities and references are recorded;
- **R2 — Environment-bounded**: important backend/runtime/dependency assumptions are also recorded;
- **R3 — Reproduced**: a separate rerun was actually executed and compared under a declared criterion.

A manifest, checksum, provenance sidecar, accessibility record, figure evidence record, claim binding or process disclosure never self-awards R3.

## 10. Accessibility boundary

The repository supports selected WCAG 2.2 design concerns without claiming whole-document conformance:

- SC 1.1.1 — text-alternative support;
- SC 1.4.1 — color should not be the sole required information channel;
- SC 1.4.11 — contrast for graphical objects/boundaries required for understanding.

`accessibility.adjacent_pairs` models declared adjacency. `aesthetics.adjacency_check` is an optional stricter all-pairs project safeguard, not a universal WCAG palette rule. Machado-style CVD simulation is an extra project safeguard, not a WCAG-mandated test.

## 11. Publisher-target boundary

Publisher profiles are sourced project presets, not official submission validators. Preserve source state, verification date/scope and `acceptance_claim: false`.

A P3 match means only that implemented preset predicates did not report a mismatch. It does not imply journal acceptance or exhaustive publisher compliance.

## 12. Backend capability truth

Declared output support:

- Matplotlib: PNG, SVG, PDF;
- ggplot2: PNG, SVG, PDF;
- Observable Plot: HTML.

Backend source presence does not prove runtime availability or semantic parity. Matplotlib currently carries the integrated redundant-series style path; ggplot2 and Observable do not claim the same mapping. Observable HTML pins a real Plot dependency and still requires that dependency at view time unless separately vendored.

## 13. Cross-repository handoff

The repositories remain independently runnable.

```text
auto-doc-engine
  artifact record / process disclosure
        ↓ optional reference
epistemic-pipeline
  claim-verification / evidence-envelope
        ↓ optional reference
sci-render-kit
  figure-claim-binding / figure-evidence
```

A reference is a handoff relationship, not direct runtime coupling and not inherited scientific validity.

## 14. RO-Crate interoperability

RO-Crate 1.3 is a useful external packaging target. `sci-render-kit` does not currently claim that its manifest, provenance, accessibility, claim-audit or figure-evidence sidecars are RO-Crates.

## 15. Experimental modules

Experimental filenames must be interpreted by implemented mechanics, not metaphor:

- `projection.py`: centered-SVD PCA and neighborhood/projection metrics; t-SNE not implemented;
- `uncertainty_legend.py`: typed uncertainty metadata;
- `superposition.py`: deterministic variant layering;
- `time_crystal.py`: periodic waveform utility, not physical time-crystal simulation;
- `observer_dashboard.py`: caller-fed telemetry, not automatic comprehension or causal inference.

## 16. Shared hard boundaries

```text
Render success ≠ scientific truth
Runtime validation ≠ scientific validity
Visual-to-claim binding ≠ verified entailment
AI disclosure ≠ authorship adjudication
Human review ≠ peer review
Publisher alignment ≠ acceptance
Provenance ≠ truth
Checksum ≠ reproduction
Interval bounds ≠ confidence interval
Accessibility sidecar ≠ whole-publication WCAG conformance
Experimental implementation ≠ canonical capability
```

## 17. Maintenance rule

Local checks may be used manually when useful. GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions and merge gates are not part of this repository's architecture.
