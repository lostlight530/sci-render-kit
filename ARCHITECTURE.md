# Architecture — sci-render-kit

> Calibrated 2026-08-26. This document describes scientific-figure runtime and evidence semantics, not GitHub platform governance.

## 1. Thesis

A scientific figure is not only pixels. It is a bounded transformation from declared data/specification into a visual artifact plus evidence describing what was rendered, which upstream claims it is declared to communicate, under which backend/profile/process context, and what the runtime checks actually established.

The canonical architecture separates:

1. **declaration** — recipe, research context, claim bindings, uncertainty semantics, process disclosure, accessibility intent;
2. **runtime validation** — explicit machine rules with severity;
3. **capability resolution** — what the selected backend can actually produce;
4. **rendering** — backend-specific implementation;
5. **artifact evidence** — manifest, provenance, accessibility and figure-evidence sidecars;
6. **claim communication** — explicit visual-to-claim references, never inferred truth;
7. **process disclosure** — declared AI assistance/tool and human-review context;
8. **publisher-target alignment** — sourced preset comparison, not acceptance certification.

## 2. Canonical flow

```text
[YAML Recipe]
  data / aesthetics / output
  research_context
    ├─ artifact/evidence/provenance refs
    ├─ claim_refs[]
    └─ claim_bindings[]
  uncertainty
  process_disclosure
  accessibility
        ↓
[P0 JSON Schema]
        ↓
[P1 Runtime Findings]
 error / warning / info
        ↓
[Backend Capability Resolution]
        ↓
[Adapter]
        ↓
[Figure]
 + render-manifest@2
 + provenance@2       (Matplotlib)
 + a11y@1             (when declared)
        ↓
[P2 Artifact Integrity]
        ↓
[P3 Publisher-target Alignment]
        ↓
[figure-evidence@2]
  ├─ figure-claim-binding@1
  └─ process-disclosure@1
```

P0–P3 are runtime phases. They are not GitHub merge gates.

## 3. Declaration plane

### 3.1 Recipe identity

`metadata/recipe.schema.yaml` is the canonical recipe contract. The recipe file has a byte-level SHA-256; its structured recipe object has a canonical JSON SHA-256 in figure evidence. These identities answer different questions and must not be conflated.

### 3.2 Research context

`research_context` can carry references such as:

```text
artifact_id
source_refs[]
evidence_envelope_ref
provenance_ref
data_artifact_ref
claim_refs[]
claim_bindings[]
```

These references are handoff metadata. The renderer does not independently validate the scientific truth of upstream claims or dereference opaque URIs automatically.

### 3.3 Claim communication

A broad `claim_refs[]` list associates the figure with upstream claim IDs.

For finer-grained auditing, `claim_bindings[]` declares relationships such as:

```yaml
- visual_ref: series:treated
  claim_refs: [claim_2]
  relation: illustrates
  evidence_ref: evidence/run-042.evidence.json
```

The supported relation vocabulary is intentionally small:

```text
supports
illustrates
contextualizes
compares
derived-from
```

The semantics are **declarative communication intent**, not automatic entailment.

The renderer does not inspect the title, legend, data values, or image pixels to infer missing bindings. `figure-evidence@2` records `inferred_bindings: false`.

### 3.4 Uncertainty semantics

An interval must state what it means. `uncertainty.kind` distinguishes standard error, standard deviation, confidence/credible/bootstrap/quantile intervals, min-max ranges and heuristic bounds.

A pair of lower/upper numbers is never automatically promoted to a confidence interval. Coverage/frequentist/Bayesian semantics remain the responsibility of the upstream analysis that produced the interval.

### 3.5 Process disclosure

`process_disclosure` optionally declares:

```text
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

The renderer records these fields in `sci-render-kit/process-disclosure@1` but does not use them to infer scientific validity, authorship, peer review or publisher compliance.

Missing values become `not_declared`, never silently `none` or `reviewed`.

### 3.6 Accessibility intent

Recipe-level accessibility remains separate from publisher profiles:

- text alternative / long description;
- whether non-color redundant encoding is required;
- per-series marker/line/hatch overrides;
- actual adjacent graphical-series pairs.

The schema declares intent. Backend capability still determines what can be realized.

## 4. Runtime-quality plane

The active catalog is `quality/rules.yaml` with profile `sci-render-kit/runtime-quality@1`.

Each finding has:

```text
check_id
level
severity
message
details
```

Only `severity: error` stops the render. Warnings are retained as evidence.

This matters because these conditions are not equivalent:

- malformed recipe;
- unsupported backend/output pair;
- missing required accessibility cue;
- project CVD robustness warning;
- publisher-format preference mismatch.

One boolean “quality gate passed” cannot faithfully represent all of them.

The schema validates claim-binding/process-disclosure structure, but the runtime does not turn those declarations into a scientific truth check.

## 5. Accessibility / WCAG scope

The runtime supports selected WCAG 2.2 design boundaries without claiming whole-publication conformance:

- **SC 1.1.1**: short text-alternative contract;
- **SC 1.4.1**: color cannot be the only required distinction when redundant encoding is required;
- **SC 1.4.11**: contrast for graphical objects/boundaries required for understanding, including explicitly declared adjacent series where applicable.

`aesthetics.adjacency_check` is an intentionally stricter project all-pairs rule. It is not a universal WCAG requirement.

Machado CVD simulation is another project safeguard, not a WCAG success criterion.

`core/accessibility.py` emits `sci-render-kit/a11y@1` with `conformance_claim: false`.

## 6. Publisher-profile plane

Profiles contain two categories of data:

- `publication`: machine-readable target-alignment fields used by P1/P3;
- `aesthetics`: actual defaults merged into rendering.

Every external profile exposes `source_url`, `verified_date`, `source_status` and `verification_scope`.

A profile can therefore say “reverified publisher guidance” or “historical local snapshot” instead of silently presenting every number as equally current.

`acceptance_claim: false` is the default scientific boundary.

Process disclosure is orthogonal: `human_review: reviewed` or `ai_assistance: used` does not change P3 into a publisher-policy compliance engine.

## 7. Backend plane

### 7.1 Matplotlib

```text
matplotlib_adapter.py
  -> explicit accessibility render/metadata functions
  -> matplotlib_base.render(..., render_logic_fn=..., metadata_fn=...)
```

The adapter no longer mutates module-global base functions during a render. The base renderer remains the code-generation/provenance implementation and receives extension functions explicitly.

The output DPI is the merged profile/recipe DPI. The renderer no longer silently applies `max(dpi, 300)`.

Matplotlib evidence:

- `sci-render-kit/render-manifest@2`
- `sci-render-kit/provenance@2`
- embedded metadata where supported

### 7.2 ggplot2

The R adapter records the same `render-manifest@2` identity categories and the R/ggplot2 runtime when executed. It does not currently implement the Matplotlib redundant-series-style contract.

### 7.3 Observable Plot

The generated HTML pins `@observablehq/plot@0.6.17/+esm`. The manifest records that browser viewing still requires the CDN/network, so the artifact must not be described as offline environment-complete evidence.

Claim-binding and process-disclosure records live in the figure evidence layer; rendering backends are not required to understand or verify their epistemic meaning.

## 8. Figure evidence plane

`core/figure_evidence.py` creates:

```text
sci-render-kit/figure-evidence@2
```

after successful artifact checks.

It references available artifacts with SHA-256 rather than duplicating payloads and records:

- recipe/profile/output identities;
- manifest/provenance/accessibility references;
- backend;
- upstream research context;
- uncertainty declaration;
- runtime findings;
- local reproducibility semantics;
- `figure-claim-binding@1` communication records;
- `process-disclosure@1` AI/human-review metadata;
- explicit scientific/statistical/causal/authorship/peer-review/publisher false-claim flags.

### 8.1 Claim communication subprofile

```text
sci-render-kit/figure-claim-binding@1
```

contains:

```text
claim_refs[]
bindings[]
binding_count
inferred_bindings: false
```

A binding is useful because a later auditor can determine whether `panel:A` or `series:treated` was intended to communicate a particular upstream claim. It is not useful as a truth oracle.

### 8.2 Process-disclosure subprofile

```text
sci-render-kit/process-disclosure@1
```

contains declared AI assistance/tool identifiers and human-review state.

The field set is compatible in spirit with `auto-doc-engine` process disclosure and downstream/upstream references from `epistemic-pipeline/evidence-envelope@2`, but no repository import or shared runtime is required.

## 9. Why the 2026-08-26 delta matters

Recent autonomous-science work distinguishes generic operation telemetry from scientific claim/artifact auditability.

- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents* argues for portable relations among claims, evidence, artifacts, runs and verification records rather than relying only on model-call logs.
- *EarthVerse* evaluates package-scoped scientific investigations and reports a large gap between completing local answer units and satisfying strict end-to-end consistency across evidence, units, calculations and interpretation.
- Nature Computational Science's August 2026 editorial position emphasizes transparency, accountability and human oversight in AI-assisted scientific publishing.

For a visualization system, the bounded consequence is clear:

> preserve what the recipe says a visual object communicates, preserve the process context, and do not silently upgrade either record into scientific validity.

## 10. Reproducibility model

Local terminology:

- **R0 Traceable** — artifact association exists;
- **R1 Replay-addressable** — stable content identities and references are recorded;
- **R2 Environment-bounded** — sufficient runtime/dependency assumptions are also captured;
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion.

A single successful render, a claim binding, or a process disclosure cannot self-award R3.

## 11. Experimental plane

Experimental modules remain outside the dispatcher.

- `projection.py`: centered-SVD PCA and actual neighborhood-rank metrics; t-SNE is explicit Not Implemented rather than a fake approximation.
- `uncertainty_legend.py`: typed interval/heuristic-bound metadata; no Heisenberg analogy as statistical evidence.
- `superposition.py`: deterministic variant layering; no quantum interference model.
- `time_crystal.py`: deterministic periodic waveform utility; no time-crystal physics simulation.
- `observer_dashboard.py`: caller-fed interaction telemetry; no automatic comprehension/causal inference.

Historical filenames may remain for compatibility. Their documentation must describe implemented mechanics, not metaphorical physics.

## 12. Cross-repository research architecture

```text
auto-doc-engine
  research artifact identity + declared AI/human-review process context
        ↓
epistemic-pipeline
  claim-index@1 + evidence-envelope@2 + provider/review disclosure
        ↓
sci-render-kit
  figure-claim-binding@1 + uncertainty + accessibility + figure-evidence@2
```

The repositories remain independently runnable. Interoperability is expressed through artifacts and contracts, not hidden imports.

## 13. Maintenance architecture

Optional local commands may inspect repository contracts:

```bash
make test
```

They are maintenance aids only. The architecture explicitly does **not** require GitHub Actions, CodeQL, dependency bots, branch-protection rules or merge gates.

Hard rules for future work:

1. Declaration does not imply backend support.
2. A warning is not automatically an error.
3. Publisher alignment is not publisher acceptance.
4. Provenance is not truth.
5. Visual-to-claim binding is not verified entailment.
6. AI disclosure is not authorship adjudication.
7. Human review is not peer review or scientific truth.
8. Interval semantics must be declared rather than guessed.
9. Color semantics are project conventions unless stronger evidence exists.
10. Whole-publication accessibility cannot be inferred from a figure sidecar.
11. No experimental module may return fabricated metrics or pretend to implement an algorithm it does not implement.
12. New evidence profiles must distinguish byte identity, structured identity and scientific meaning.
13. Public docs, schemas, runtime rules and backend behavior must describe the same capability boundary.
