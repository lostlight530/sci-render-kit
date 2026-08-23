# Publication Profiles

Profiles encode measurable publication constraints; they are not opaque visual themes.

Current profiles:

| Profile | Purpose |
|---|---|
| `nature` | Nature-family figure constraints snapshot |
| `science` | Science figure constraints snapshot |
| `cell` | Cell figure constraints snapshot |
| `ieee` | IEEE figure constraints snapshot |
| `presentation` | Internal/general presentation defaults, not an external journal specification |

Each externally sourced profile should carry `source_url` and `verified_date`. These values document the research snapshot used by the repository; publishers may update instructions later.

P3 currently uses profile fields for checks such as:

- vector-format expectations,
- minimum DPI,
- `max_width_in`,
- `max_height_in` where declared,
- font/size constraints represented by the profile.

Accessibility is intentionally **not hidden inside journal profiles**. A publication profile answers “what does this target venue constrain?”; the recipe-level `accessibility` object answers “what non-text/text-alternative and redundant-encoding contract does this figure declare?”. Keeping them separate prevents a journal name from being treated as an automatic accessibility certification.

Example:

```bash
python3 sci_render.py recipes/accessible-line-chart.yaml --profile presentation --backend matplotlib
```

For a journal-targeted recipe, combine the same accessibility contract with a current journal profile and let P1/P2/P3 report independent failures.
