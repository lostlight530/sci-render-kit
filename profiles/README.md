# Publication Profiles

Profiles are machine-readable **publisher-target presets**, not official publisher validators and not opaque visual themes.

## Evidence fields

Every externally sourced profile should declare:

```text
source_url
verified_date
source_status
verification_scope
publication.authority
publication.acceptance_claim
```

`source_status` distinguishes a profile that was rechecked against current publisher guidance from a retained historical project snapshot.

Current state on 2026-08-24:

| Profile | Evidence state | Meaning |
|---|---|---|
| `nature` | `publisher_guidance_reverified` | represented main-figure guidance scope was rechecked on 2026-08-24 |
| `science` | `snapshot_not_reverified_2026_08_24` | local 2026-08-19 preset retained; recheck before submission |
| `cell` | `snapshot_not_reverified_2026_08_24` | local 2026-08-19 preset retained; recheck before submission |
| `ieee` | `snapshot_not_reverified_2026_08_24` | local 2026-08-19 preset retained; venue-specific requirements can differ |
| `presentation` | `internal_project_preset` | internal readable default, no external authority |

All current profiles use:

```text
publication.acceptance_claim: false
```

## `publication` vs `aesthetics`

`publication` contains fields used for target-alignment findings, such as:

- preferred / required output formats;
- raster minimum DPI where the represented guidance supports one;
- font-size ranges;
- maximum width / height represented by the preset.

`aesthetics` contains defaults actually merged into rendering:

- font and font size;
- figure size;
- DPI;
- line widths;
- palette.

Keeping these two roles separate prevents a render default from being mistaken for a complete publisher rulebook.

## P3 semantics

P3 is **publisher-target alignment**.

A P3 warning means the current recipe differs from a machine-readable target preference. It is not a rejection and not a publisher compliance certificate.

A profile should use a hard `required_formats` or equivalent error-level field only when the repository intentionally models that constraint as a required precondition for the current profile scope. Default publisher preferences should remain warnings.

## Nature snapshot

The represented Nature profile was reverified on 2026-08-24 for the scope documented in `profiles/nature.yaml`, including main-figure widths/heights, standard editable font guidance and initial-submission raster guidance. The profile intentionally does not claim to encode every figure class, production instruction or editorial requirement.

## Accessibility remains recipe-level

Accessibility is intentionally not hidden inside a journal/profile name. A publication target and an accessibility contract answer different questions.

Use recipe-level fields for:

```yaml
accessibility:
  require_alt_text: true
  alt_text: "..."
  redundant_encoding: required
```

A publisher profile does not automatically certify those concerns.

## Maintenance rule

When a publisher updates guidance:

1. update only fields supported by the current authoritative source;
2. update `verified_date` and `verification_scope`;
3. preserve any figure-type or submission-stage qualifications;
4. never silently promote an old local snapshot to current publisher guidance;
5. keep README, Research Contract, Manifest and runtime semantics aligned.
