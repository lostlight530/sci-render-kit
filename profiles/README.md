# sci-render-kit Profiles

Profile files declare journal-specific rendering constraints: fonts, color palettes, figure dimensions, and output format requirements.

## Available Profiles

| Profile | File | Target |
|---------|------|--------|
| Nature | `nature.yaml` | Nature journal standards |
| Science | `science.yaml` | Science journal standards |
| IEEE | `ieee.yaml` | IEEE conference/journal standards |
| Presentation | `presentation.yaml` | Slide-friendly defaults |

## Profile Structure

Each profile YAML follows this structure (all fields under `aesthetics` are
merged with — and can be overridden by — the recipe's own `aesthetics`):

```yaml
name: nature
journal: Nature
aesthetics:
  font: "Arial"
  font_size: 5            # 期刊最小字号（P1 font-size 门禁校验）
  figsize: [3.5, 2.45]    # 推荐图幅（英寸）
  dpi: 300                # 期刊最低 DPI（P3 dpi-check 门禁校验）
  max_width_in: 7.2       # 双栏版宽上限（P3 size-check 门禁校验）
  line_width: 1.0
  axes_linewidth: 0.5
  palette:
    - "#E69F00"
    - "#56B4E9"
    - "#009E73"
    - "#F0E442"
    - "#0072B2"
    - "#D55E00"
    - "#CC79A7"
    - "#000000"
  constraints:            # 人类可读的约束摘要（与质量门规则对应）
    - "矢量格式优先 (PDF/EPS)"
    - "字号 ≥ 5pt"
```

Enforcement notes:

- `font_size`, `dpi`, `max_width_in` are machine-checked by quality gates
  (see `quality/gates.yaml`); `constraints` is the human-readable summary.
- For `nature` / `science`, the P3 `vector-format` gate additionally requires
  the recipe to declare `output.format: pdf` (or `eps`).

## Adding a Custom Profile

1. Create `profiles/your_profile.yaml` following the structure above.
2. Reference it via `--profile your_profile` when invoking `sci_render.py`.
3. The CLI loads the profile and merges it into both the pre-render (P0/P1)
   and post-render (P2/P3) quality-gate evaluation. A missing profile file
   aborts the run with `MISSING_PROFILE`.
