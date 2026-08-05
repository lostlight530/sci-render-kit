# Sci Render Kit Scientific Closure Design

Date: 2026-08-05
Status: approved design baseline
Base: `main@a193ddc0013dda2524f8ff10910eee86633708d5`

## Objective

Make the declarative scientific-rendering toolkit truthful, safe, backend-aware, and reproducible while preserving `sci_render.py`, existing recipe/profile paths, and the root README.

## Verified starting point

The repository contains the CLI, schemas, quality gates, profiles, recipes, Python/R/JavaScript adapters, declarative engine, transforms, Plotly support, and tests. It has no GitHub workflow or cloud test evidence. Calculation transforms dynamically evaluate generated expressions. Several backend chart branches return TODO code rather than a supported result. The root README links to a missing `profiles/README.md`. Current capability declarations do not provide an enforceable backend-by-chart matrix.

## Architecture decision

Recipes are validated before transformation or dispatch. Data transforms use a parsed arithmetic/filter expression language with an allowlist of fields, literals, operators, and pure functions; arbitrary code execution is impossible. Every backend advertises an explicit capability matrix. A declared combination must either render and produce validated provenance or fail before code generation with a structured unsupported-capability error.

The data flow is:

`recipe + profile + data -> schema validation -> quality gates -> safe transforms -> capability resolution -> backend render -> output + reproducibility manifest`

The reproducibility manifest binds recipe, profile, data, backend, tool version, environment, and output through SHA-256 digests. Metadata claims distinguish captured facts from user-supplied annotations.

## Planned change set

- Replace dynamic calculation execution with a safe expression parser; transformations do not mutate caller-owned input records.
- Fail closed for unknown transforms, operators, marks, profiles, backends, and malformed values.
- Define and enforce a backend capability matrix consistent with `MANIFEST.yaml` and the recipe schema.
- Implement every currently declared chart/backend path or explicitly remove it from that backend's declared capability; no TODO code may be emitted as a successful render.
- Validate generated filenames and paths, prevent traversal, and make output plus manifest publication atomic.
- Strengthen provenance with canonical serialization and input/spec/profile/output digests.
- Add `profiles/README.md` as the missing profile contract without modifying the root README.
- Add deterministic tests for schema validation, quality gates, transforms, code generation, capability negotiation, manifest integrity, and stable hashes.
- Add adversarial tests for expression injection, malicious fields and paths, invalid numeric values, unsupported combinations, missing runtimes, and interrupted rendering.
- Add reproducibility, evidence, AI-use, security, contribution, and repo-specific GitHub governance files.
- Add least-privilege GitHub verification, CodeQL, and dependency-maintenance workflows pinned to immutable action commits.

## Scientific integrity rules

Visual defaults may not imply statistical significance, uncertainty, causality, or sample adequacy. Missing values, transformations, aggregation, binning, uncertainty encodings, and excluded observations must be represented in the manifest. Color profiles require accessible contrast and must not rely on color alone for categorical distinction. Backends must preserve semantic encodings even when visual implementations differ.

## Verification and acceptance

Cloud checks run on Python 3.12 and 3.14. All existing and new tests, `compileall`, schema checks, JavaScript syntax checks, and deterministic render-fixture comparisons must pass. Optional R, Matplotlib, Plotly, and YAML paths report tested, skipped-with-reason, or unsupported; a skip is never counted as evidence of successful rendering. Identical canonical inputs must produce identical spec and provenance digests.

## Non-goals

No root README edit, frontend, hosted dashboard, invented research result, package publication, Jules integration, or claim of pixel-identical output across different backend versions. Existing `sci_render.py` remains the stable entry point.

## Rollout and rollback

Implementation is isolated on `codex/scientific-closure-20260805` and delivered through one repository-specific pull request. Merge occurs only after cloud checks pass. Rollback is a single merge-commit revert; generated artifacts are not versioned and therefore require no repository migration.
