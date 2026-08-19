"""
Cognitive Color Encoding - Semantic Color Mapping System
[IMPLEMENTED] Integrated into the main rendering pipeline.

Maps data semantics to perceptually distinct colors, ensuring that
visualization color choices carry meaning rather than aesthetic whim.

Integration points:
- ``sci_render.py`` quality gate ``palette-contrast`` (P1) uses
  ``CognitiveColorEncoder.contrast_ratio`` to enforce WCAG non-text
  contrast (>= 3.0) between palette colors and the declared background.
- Backend adapters resolve ``aesthetics.semantic_palette: true`` via
  ``CognitiveColorEncoder.resolve_series_palette`` so that series named
  after semantic tags (e.g. ``positive`` / ``negative`` / ``stable``)
  automatically receive their semantic colors.

Real-world: Semantic color theory and perceptual color spaces.
"""

import colorsys
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Any


@dataclass
class SemanticColor:
    """A color with associated semantic meaning."""

    name: str
    hex_code: str
    rgb: Tuple[int, int, int]
    hsl: Tuple[float, float, float]
    semantic_tags: List[str] = field(default_factory=list)
    contrast_ratio: float = 1.0


class CognitiveColorEncoder:
    """Semantic color mapping system for data visualization."""

    PERCEPTUAL_PALETTE = [
        (0, 114, 178),  # Blue - trust, stability
        (230, 159, 0),  # Orange - energy, warmth
        (0, 158, 115),  # Green - growth, positive
        (204, 121, 167),  # Pink - creativity, emotion
        (86, 180, 233),  # Sky - clarity, openness
        (240, 228, 66),  # Yellow - attention, caution
        (213, 94, 0),  # Vermillion - danger, critical
        (0, 0, 0),  # Black - authority, finality
    ]

    SEMANTIC_MAP = {
        "positive": (0, 158, 115),
        "negative": (213, 94, 0),
        "neutral": (86, 180, 233),
        "critical": (213, 94, 0),
        "stable": (0, 114, 178),
        "energetic": (230, 159, 0),
        "creative": (204, 121, 167),
        "attention": (240, 228, 66),
    }

    def __init__(self):
        self._color_registry: Dict[str, SemanticColor] = {}
        self._init_default_palette()

    def _init_default_palette(self) -> None:
        """Initialize the default semantic palette."""
        for name, (r, g, b) in self.SEMANTIC_MAP.items():
            hex_code = f"#{r:02X}{g:02X}{b:02X}"
            h, s, l = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
            self._color_registry[name] = SemanticColor(
                name=name,
                hex_code=hex_code,
                rgb=(r, g, b),
                hsl=(h, s, l),
                semantic_tags=[name],
            )

    def encode(self, semantic_tag: str) -> Optional[SemanticColor]:
        """Get the semantic color for a given tag."""
        return self._color_registry.get(semantic_tag)

    def encode_value(
        self, value: float, min_val: float = 0, max_val: float = 1
    ) -> SemanticColor:
        """Map a continuous value to a color on a perceptual scale."""
        normalized = (
            (value - min_val) / (max_val - min_val) if max_val != min_val else 0.5
        )
        normalized = max(0.0, min(1.0, normalized))

        start_rgb = (213, 94, 0)
        end_rgb = (0, 158, 115)
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * normalized)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * normalized)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * normalized)

        return SemanticColor(
            name=f"scale_{normalized:.2f}",
            hex_code=f"#{r:02X}{g:02X}{b:02X}",
            rgb=(r, g, b),
            hsl=colorsys.rgb_to_hls(r / 255, g / 255, b / 255),
            semantic_tags=["scale"],
        )

    def encode_category(self, category: str, index: int) -> SemanticColor:
        """Map a categorical value to a perceptually distinct color."""
        palette = self.PERCEPTUAL_PALETTE
        r, g, b = palette[index % len(palette)]

        return SemanticColor(
            name=category,
            hex_code=f"#{r:02X}{g:02X}{b:02X}",
            rgb=(r, g, b),
            hsl=colorsys.rgb_to_hls(r / 255, g / 255, b / 255),
            semantic_tags=[category],
        )

    def contrast_ratio(
        self, color1: Tuple[int, int, int], color2: Tuple[int, int, int]
    ) -> float:
        """Calculate WCAG contrast ratio between two colors."""

        def luminance(rgb):
            def adjust(c):
                c = c / 255.0
                return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

            return (
                0.2126 * adjust(rgb[0])
                + 0.7152 * adjust(rgb[1])
                + 0.0722 * adjust(rgb[2])
            )

        l1 = luminance(color1)
        l2 = luminance(color2)
        lighter = max(l1, l2)
        darker = min(l1, l2)
        return (lighter + 0.05) / (darker + 0.05)

    def resolve_series_palette(self, labels: List[str]) -> List[str]:
        """Resolve hex colors for a list of series labels.

        Labels matching a known semantic tag (case-insensitive) receive
        their semantic color; all other labels receive perceptually
        distinct palette colors by index.
        """
        resolved = []
        for i, label in enumerate(labels):
            color = self.encode(str(label).lower())
            if color is None:
                color = self.encode_category(str(label), i)
            resolved.append(color.hex_code)
        return resolved

    def get_palette(self, n: int) -> List[SemanticColor]:
        """Get n perceptually distinct colors."""
        colors = []
        for i in range(n):
            r, g, b = self.PERCEPTUAL_PALETTE[i % len(self.PERCEPTUAL_PALETTE)]
            colors.append(
                SemanticColor(
                    name=f"palette_{i}",
                    hex_code=f"#{r:02X}{g:02X}{b:02X}",
                    rgb=(r, g, b),
                    hsl=colorsys.rgb_to_hls(r / 255, g / 255, b / 255),
                    semantic_tags=[f"palette_{i}"],
                )
            )
        return colors
