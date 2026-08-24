"""Named palette registry for scientific-figure rendering.

[IMPLEMENTED] Categorical entries can be consumed through
``aesthetics.palette_name``. Sequential/diverging entries are descriptive
registry records unless the selected backend explicitly exposes the referenced
colormap.

Metadata in this registry is intentionally evidence-bounded:
- ``kind`` describes intended data semantics;
- ``cvd_note`` records design/source context, not a universal accessibility
  guarantee;
- ``availability`` says what this repository can actually resolve today;
- source citations identify provenance for the palette definition.

A palette registry entry does not establish WCAG conformance, perceptual
uniformity in every viewing environment, or suitability for every dataset.
"""

from __future__ import annotations

from typing import Dict, List, Optional

PALETTE_REGISTRY: Dict[str, dict] = {
    "okabe-ito": {
        "kind": "categorical",
        "source": "Okabe & Ito, Color Universal Design guidance",
        "cvd_note": "widely used color-universal-design categorical palette; still pair with non-color cues when information requires it",
        "availability": {
            "matplotlib": "project hex sequence",
            "ggplot2": "project hex sequence",
            "observable": "project hex sequence",
        },
        "colors": [
            "#E69F00", "#56B4E9", "#009E73", "#F0E442",
            "#0072B2", "#D55E00", "#CC79A7", "#000000",
        ],
    },
    "petroff10": {
        "kind": "categorical",
        "source": "Petroff (2021), arXiv:2107.02270; available in recent Matplotlib color sequences",
        "cvd_note": "designed for color-vision-deficiency robustness; repository runtime safeguards still apply independently",
        "availability": {
            "matplotlib": "project hex sequence / recent Matplotlib color sequence",
            "ggplot2": "project hex sequence",
            "observable": "project hex sequence",
        },
        "colors": [
            "#3F90DA", "#FFA90E", "#BD1F01", "#94A4A2", "#832DB6",
            "#A96B59", "#E76300", "#B9AC70", "#717581", "#92DADD",
        ],
    },
    "viridis": {
        "kind": "sequential",
        "source": "viridis family; Matplotlib built-in sequential colormap",
        "cvd_note": "designed for perceptual robustness; not a whole-figure accessibility guarantee",
        "availability": {
            "matplotlib": "builtin colormap",
            "ggplot2": "runtime package-dependent",
            "observable": "backend scheme-dependent",
        },
        "mpl_name": "viridis",
    },
    "cividis": {
        "kind": "sequential",
        "source": "Nuñez et al. (2018), cividis",
        "cvd_note": "designed with CVD/perceptual considerations; repository does not treat the name as a conformance certificate",
        "availability": {
            "matplotlib": "builtin colormap",
            "ggplot2": "runtime package-dependent",
            "observable": "backend scheme-dependent",
        },
        "mpl_name": "cividis",
    },
    "mako": {
        "kind": "sequential",
        "source": "seaborn mako",
        "cvd_note": "not independently validated by this repository",
        "availability": {
            "matplotlib": "not builtin; external seaborn required",
            "ggplot2": "not provided by this repository",
            "observable": "not provided by this repository",
        },
        "mpl_name": None,
    },
    "berlin": {
        "kind": "diverging",
        "source": "Crameri Scientific Colour Maps",
        "cvd_note": "external scientific-colour-map design; not independently certified by this repository",
        "availability": {
            "matplotlib": "not builtin; external cmcrameri required",
            "ggplot2": "not provided by this repository",
            "observable": "not provided by this repository",
        },
        "mpl_name": None,
    },
    "managua": {
        "kind": "diverging",
        "source": "Crameri Scientific Colour Maps",
        "cvd_note": "external scientific-colour-map design; not independently certified by this repository",
        "availability": {
            "matplotlib": "not builtin; external cmcrameri required",
            "ggplot2": "not provided by this repository",
            "observable": "not provided by this repository",
        },
        "mpl_name": None,
    },
    "vanimo": {
        "kind": "diverging",
        "source": "Crameri Scientific Colour Maps",
        "cvd_note": "external scientific-colour-map design; not independently certified by this repository",
        "availability": {
            "matplotlib": "not builtin; external cmcrameri required",
            "ggplot2": "not provided by this repository",
            "observable": "not provided by this repository",
        },
        "mpl_name": None,
    },
}


def available_palettes() -> List[str]:
    """Return registered palette names."""
    return sorted(PALETTE_REGISTRY)


def describe_palette(name: str) -> dict:
    """Return a palette metadata record or raise for an unknown name."""
    if name not in PALETTE_REGISTRY:
        raise ValueError(f"unknown palette '{name}'; available: {', '.join(available_palettes())}")
    return dict(PALETTE_REGISTRY[name])


def resolve_categorical(name: str, n: Optional[int] = None) -> List[str]:
    """Resolve a registered categorical palette to project-owned hex values."""
    entry = describe_palette(name)
    if entry["kind"] != "categorical":
        raise ValueError(
            f"palette '{name}' is {entry['kind']}; categorical series require a categorical palette; "
            "use a backend colormap field for sequential/diverging scales"
        )
    colors = list(entry["colors"])
    if n is None:
        return colors
    if n < 0:
        raise ValueError("n must be >= 0")
    return colors[:n]
