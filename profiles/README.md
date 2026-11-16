# Publication Profiles

## 中文专业正文对照 / Chinese technical counterpart

**具体研究对象 / Concrete subject:** 本专业文档给出真实图像编译能力的边界

**English owning title:** Publication Profiles

**图像证据判别 / Figure evidence reading:** 应分别取得源数据版本、recipe/profile、实际后端输出、manifest、声明绑定、上游 sidecar 与可访问性实测结果，不能将图像 bytes、示例文档或测试定义视为实际同行评审 / Keep source, recipe, backend, manifest and claim identities separate, verify the exact execution evidence before asserting quality or reproducibility

| English original section / 英文原章 | 中文对应定位 / Chinese section meaning |
| --- | --- |
| Evidence fields | 证据字段 |
| `publication` vs `aesthetics` | 该图像合同的局部机制与证据限制 |
| P3 semantics | 该图像合同的局部机制与证据限制 |
| Nature snapshot | 该图像合同的局部机制与证据限制 |
| Accessibility remains recipe-level | 该图像合同的局部机制与证据限制 |
| Maintenance rule | 该图像合同的局部机制与证据限制 |

**限界 / Limits:** 原有配置、图形行为与未知执行状态保持不变，本节不新增科学审定、出版接纳、WCAG 认证或真实浏览器通过声明 / Original behaviors and unknown states are unchanged, no scientific or publisher certification is implied


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
