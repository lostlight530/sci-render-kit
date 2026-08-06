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

Each profile YAML follows this schema:

```yaml
name: nature
aesthetics:
  font: serif
  font_size: 8
  figsize: [3.5, 2.5]
  dpi: 300
  palette:
    - "#E69F00"
    - "#56B4E9"
    - "#009E73"
    - "#F0E442"
    - "#0072B2"
    - "#D55E00"
    - "#CC79A7"
    - "#000000"
output:
  formats: [pdf, eps]
  vector_required: true
```

## Adding a Custom Profile

1. Create `profiles/your_profile.yaml` following the structure above.
2. Reference it via `--profile your_profile` when invoking `sci_render.py`.
3. The CLI will automatically validate the profile against quality gates.
