# Research Contract — 2026-08-23

Status: active architecture contract for scientific-figure claims, provenance, accessibility, and research-object interoperability.

`sci-render-kit` is the **scientific visualization and result-presentation plane** of the three-repository research toolchain. Its job is to turn a validated declarative recipe into a backend-bounded figure plus inspectable metadata. It does not decide whether the underlying scientific conclusion is true.

## 1. Bounded rendering contract

The intended canonical flow is:

`recipe + profile + data -> schema validation -> declared quality gates -> backend capability check -> render -> output checks -> reproducibility metadata`

Every step has a limited meaning. Passing all gates establishes only that the implemented predicates passed for the declared inputs, profile, backend, and environment.

## 2. Scientific-integrity boundary

The toolkit must not imply any of the following solely from a successful render:

- statistical significance;
- causal validity;
- adequate sample size;
- correct uncertainty modeling;
- absence of omitted or transformed observations;
- journal acceptance or full compliance with every editorial requirement;
- independent reproducibility of the scientific result.

A profile is a machine-checkable subset of declared publication constraints, not an authoritative replacement for current journal instructions or editorial review.

## 3. Provenance semantics

The repository distinguishes two different artifacts:

1. **Reproducibility manifest** — records declared recipe/profile/backend/environment information associated with a render.
2. **Matplotlib provenance sidecar / embedded metadata** — records content digests and render context for the implemented Matplotlib path.

Neither artifact is a proof of scientific truth or independent reproducibility. A timestamp is not a trusted external timestamp; a SHA-256 digest establishes byte identity under the recorded serialization, not semantic equivalence.

## 4. Reproducibility levels

The following are local project terms, not an external standard:

- **R0 — Traceable**: figure and metadata can be associated with their declared recipe/profile.
- **R1 — Replay-addressable**: data/spec/profile/output identities and digests plus tool revision are recorded.
- **R2 — Environment-bounded**: runtime/backend/dependency versions and external runtime assumptions are also recorded.
- **R3 — Reproduced**: a separate rerun has actually been executed and compared under a declared criterion.

Generating a manifest or `.prov.json` file alone does not justify `R3`.

## 5. Accessibility contract

WCAG 2.2 SC 1.4.11 requires sufficient contrast for non-text graphical objects that are required to understand content, relative to adjacent colors. It is not a universal rule that every pair of colors in a categorical palette must have 3:1 contrast.

Accordingly, this repository treats its opt-in `palette-adjacency` all-pairs check as a **project-specific stricter safeguard inspired by SC 1.4.11 / Technique G209**, not as a verbatim WCAG requirement. Other gates such as text contrast, palette/background contrast, and CVD simulation retain their own documented activation conditions and scope.

Accessibility checks reduce known visual barriers; they do not guarantee that a figure is accessible to every reader or in every publication context.

## 6. Backend capability truth

Backend independence means that one declarative recipe model can target multiple adapters **within each adapter's declared capability set**. It does not mean every recipe/output combination works identically everywhere.

Current declared output capabilities are:

- Matplotlib: PNG, SVG, PDF;
- ggplot2: PNG, SVG, PDF;
- Observable: HTML.

Unsupported combinations must fail explicitly before being reported as successful. Backend/runtime availability and semantic parity remain separate questions.

## 7. Cross-repository handoff contract

Preferred upstream fields from `auto-doc-engine`, `epistemic-pipeline`, or another research layer are:

```text
artifact_id
source_refs[]
content_or_data_sha256
run_or_analysis_ref
uncertainty_semantics
provenance_ref
validation_status
```

Preferred figure-side outputs are:

```text
figure_id
recipe_sha256
input_data_sha256
profile_id
backend_id
output_sha256
manifest_ref
provenance_ref
quality_gate_status
```

These fields define an interoperability boundary only. The three repositories remain independently runnable and are not claimed to call each other directly.

## 8. RO-Crate interoperability target

RO-Crate 1.3 was published as a Recommendation on 2026-06-22 and is a useful current packaging target for research objects and contextual metadata.

For this repository, **RO-Crate 1.3 is proposed interoperability only**. The current manifest and `.prov.json` sidecar are not RO-Crates. A future exporter could package the figure, recipe, profile, source data, software context, and render action into a crate, but that requires a conforming writer/validator and executable tests.

## 9. Ecosystem observations on 2026-08-23

External versions are recorded for situational awareness, not as automatic compatibility claims:

- Matplotlib stable latest observed version: 3.11.1 (released 2026-07-17). Existing repository evidence must remain tied to the versions actually tested; documentation must not silently upgrade that evidence to 3.11.x compatibility.
- WCAG reference baseline: W3C WCAG 2.2, including SC 1.4.3 and SC 1.4.11.

## 10. Shared scientific-integrity rules

1. A quality gate is only as broad as its implemented predicate.
2. A publication profile is not journal acceptance.
3. Provenance is not truth.
4. A visual encoding must not imply unsupported certainty, causality, or significance.
5. Backend fallbacks/skips/optional runtimes must not be counted as successful evidence.
6. External standards are cited with their scope; stricter project policy is labeled as project policy.
7. Experimental modules remain experimental until they enter the canonical path with tests.

## 11. Primary references

Retrieved 2026-08-23:

- RO-Crate 1.3 Specification: https://www.researchobject.org/ro-crate/1.3/
- FAIR Principle R1.2: https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/
- W3C WCAG 2.2 SC 1.4.11: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- W3C Technique G209: https://www.w3.org/WAI/WCAG22/Techniques/general/G209
- Matplotlib release notes: https://matplotlib.org/stable/users/release_notes.html
