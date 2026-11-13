# Release and Archival Policy

This repository treats `main` as the current repository state and release tags as immutable point-in-time snapshots.

## Policy

- Create a release or tag only from a reviewed and merged `main` revision.
- A release records a historical snapshot; it does not override later repository state, governance, contracts, or evidence.
- Release identifiers may be repository-specific. Do not invent a semantic version where the repository has not established one.
- Add `version`, `date-released`, DOI, SWHID, or other archival identifiers to citation metadata only after those identifiers actually exist.
- Do not rewrite historical tags or releases to reflect later corrections; publish a new release or correction record instead.
- Archive externally only after the release snapshot and its metadata have been validated.

For current repository truth, follow the repository's native implementation, evidence, governance, and recovery surfaces rather than citation or archival metadata.

## Initial archived software publication — 2026-09-16

The repository has a public Zenodo software publication dated **2026-09-16**.

- DOI: `10.5281/zenodo.22791375`
- DOI resolver: `https://doi.org/10.5281/zenodo.22791375`
- Code repository: `https://github.com/lostlight530/sci-render-kit`

This DOI is an archival publication identifier, not a moving identifier for every later `main` revision. Later repository changes must not be represented as part of the archived publication unless a new archival release explicitly includes them.

A future archived release should preserve this record as point-in-time publication history and use its own confirmed release metadata. DOI presence, citation metadata, or archival availability does not by itself establish render validity, scientific validity, accessibility certification, publisher acceptance, or reproduction.

## Verified archived version lineage (2026-10-10)

The September 16 publication described above is the **initial archival snapshot**; it is not the only release now registered under this software concept. The citation/CodeMeta DOI `10.5281/zenodo.22791375` is the **concept DOI**, not the DOI for the latest specific release.

| Archived release | Published/release date | Immutable version DOI |
| --- | --- | --- |
| `v2026.09-open-research-baseline` | 2026-09-16 | [`10.5281/zenodo.22791376`](https://doi.org/10.5281/zenodo.22791376) |
| `v2026.09-natural-month-close` | 2026-09-30 | [`10.5281/zenodo.23068472`](https://doi.org/10.5281/zenodo.23068472) |
| `v2026.10-open-research-production-framework` | 2026-10-04 | [`10.5281/zenodo.23137219`](https://doi.org/10.5281/zenodo.23137219) |

The October GitHub release [`v2026.10-open-research-production-framework`](https://github.com/lostlight530/sci-render-kit/releases/tag/v2026.10-open-research-production-framework) reports `published_at=2026-10-04T13:00:39Z`. These identifiers are confirmed public release/DOI records, **not a claim that present `main` was frozen in that snapshot**. The existing `CITATION.cff` September 16 date remains a recorded archival baseline; do not silently rewrite it into a present-day retrieval or publication date. This documentation note creates **no new software release, DOI, prospective observation, or evidence of external research adoption**. The [independent identity audit](https://github.com/lostlight530/research-software-identity-audit) observes ten fixed software objects and remains an external control repository, not an eleventh research sample.

## Archived checkpoint — 2026-10-14

The fourth archived version is [v2026.10-fourteen-day-evidence-checkpoint](https://github.com/lostlight530/sci-render-kit/releases/tag/v2026.10-fourteen-day-evidence-checkpoint).

- Version DOI: [10.5281/zenodo.23365525](https://doi.org/10.5281/zenodo.23365525)
- GitHub `published_at`: `2026-10-14T11:15:18Z`
- Tagged source commit: [`a48dc7375aac3526b5a0a133d0a1f435dcf935e7`](https://github.com/lostlight530/sci-render-kit/tree/a48dc7375aac3526b5a0a133d0a1f435dcf935e7)
- Software-family concept DOI: [10.5281/zenodo.22791375](https://doi.org/10.5281/zenodo.22791375)

Use the version DOI for this exact checkpoint and the concept DOI for the software family. `CITATION.cff` and CodeMeta retain the family identifier and recorded September 16 baseline date. Later changes to `main` belong to subsequent repository state; the checkpoint tag remains unchanged.

### 软件版本与图表数据身份 / Software-version and figure-data identities

**中文**：历史 GitHub tag、归档版本 DOI 及引用文件中明确固定的发布信息，保留其原始发行身份；concept DOI `10.5281/zenodo.22791375` 标识 Sci Render 软件版本家族，具体复现应引用相应 version DOI、commit、输入数据、配方、后端版本与产物回执；图表发布、科研阶段闭环与科学有效性是不同事件，不能仅凭软件归档或图片输出声称已验证

**English**: Historical tags, archived version DOIs and release-specific citation fields retain their original publication identity. Concept DOI `10.5281/zenodo.22791375` identifies the Sci Render software family; reproducibility requires the relevant version DOI, commit, input data, recipe, backend version and artifact receipt. Figure publication, research-stage closure and scientific validity are different events; a software archive or rendered image does not certify validation

## Open-science reuse and research records

- Cite the software family through [CITATION.cff](CITATION.cff) or [CodeMeta](codemeta.json); cite the version DOI above when a result depends on this checkpoint.
- Use the linked tagged source commit for code inspection and retrieval, and record the revision, environment, procedure and observed result when performing a rerun.
- Follow [OPEN_RESEARCH.md](OPEN_RESEARCH.md) and the repository-native research contracts; use [RESEARCH_TEMPLATE.md](RESEARCH_TEMPLATE.md) for a new bounded research record where a more specific native template does not apply.
- Reuse repository-owned material under [LICENSE](LICENSE), preserve [authorship attribution](AUTHORS), and submit changes through [CONTRIBUTING.md](CONTRIBUTING.md).
- Keep later findings and corrections in new dated records so the archived checkpoint remains recoverable.


## Latest archived checkpoint — 2026-11-10

The latest archived repository snapshot is `v2026.11-ten-day-evidence-checkpoint`.

- GitHub Release: [v2026.11-ten-day-evidence-checkpoint](https://github.com/lostlight530/sci-render-kit/releases/tag/v2026.11-ten-day-evidence-checkpoint)
- GitHub release published: `2026-11-10T14:40:48Z`
- Tagged source commit: [`4c46164e2474f80e565520ad7fc6842933000c4b`](https://github.com/lostlight530/sci-render-kit/commit/4c46164e2474f80e565520ad7fc6842933000c4b)
- Zenodo exact-version record: [10.5281/zenodo.24112475](https://doi.org/10.5281/zenodo.24112475)
- Software-family concept DOI: [10.5281/zenodo.22791375](https://doi.org/10.5281/zenodo.22791375)

The Zenodo version record identifies the exact GitHub tag as its source reference. This is an immutable 2026-11-10 snapshot; subsequent changes on `main` are not part of this archive. The concept DOI remains the software-family identifier and is intentionally distinct from the version DOI.
