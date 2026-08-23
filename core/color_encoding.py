"""Project color encoding utilities.
[IMPLEMENTED] Used by recipe palette resolution and runtime contrast rules.

The historical class name ``CognitiveColorEncoder`` is retained for API
compatibility. The implementation provides a **project convention** for mapping
selected labels to colors plus ordinary categorical and continuous sRGB color
selection. It does not claim universal psychological meaning, perceptual
uniformity, or color-vision-deficiency safety for every generated combination.
"""

from __future__ import annotations

import colorsys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class SemanticColor:
    name: str
    hex_code: str
    rgb: Tuple[int, int, int]
    hsl: Tuple[float, float, float]
    semantic_tags: List[str] = field(default_factory=list)
    semantics: str = "project_color_convention"


class CognitiveColorEncoder:
    """Compatibility name for the repository's semantic/categorical color mapper."""

    # Okabe-Ito-inspired categorical sequence used as a project default.
    CATEGORICAL_PALETTE = [
        (0, 114, 178),
        (230, 159, 0),
        (0, 158, 115),
        (204, 121, 167),
        (86, 180, 233),
        (240, 228, 66),
        (213, 94, 0),
        (0, 0, 0),
    ]
    # Historical compatibility alias.
    PERCEPTUAL_PALETTE = CATEGORICAL_PALETTE

    # These mappings are project conventions for common dashboard/research
    # labels. They are not universal human semantic associations.
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

    @staticmethod
    def _to_color(name: str, rgb: Tuple[int, int, int], tags: List[str]) -> SemanticColor:
        r, g, b = rgb
        h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        return SemanticColor(
            name=name,
            hex_code=f"#{r:02X}{g:02X}{b:02X}",
            rgb=rgb,
            hsl=(h, s, l),
            semantic_tags=tags,
        )

    def _init_default_palette(self) -> None:
        for name, rgb in self.SEMANTIC_MAP.items():
            self._color_registry[name] = self._to_color(name, rgb, [name])

    def encode(self, semantic_tag: str) -> Optional[SemanticColor]:
        """Resolve one repository-defined semantic label, case-insensitively."""
        return self._color_registry.get(str(semantic_tag).lower())

    def encode_value(self, value: float, min_val: float = 0, max_val: float = 1) -> SemanticColor:
        """Map a number to a simple sRGB interpolation, not a perceptual color space."""
        normalized = (value - min_val) / (max_val - min_val) if max_val != min_val else 0.5
        normalized = max(0.0, min(1.0, float(normalized)))
        start_rgb = (213, 94, 0)
        end_rgb = (0, 158, 115)
        rgb = tuple(
            int(round(start + (end - start) * normalized))
            for start, end in zip(start_rgb, end_rgb)
        )
        color = self._to_color(f"scale_{normalized:.2f}", rgb, ["scale"])
        color.semantics = "linear_srgb_interpolation_not_perceptually_uniform"
        return color

    def encode_category(self, category: str, index: int) -> SemanticColor:
        rgb = self.CATEGORICAL_PALETTE[index % len(self.CATEGORICAL_PALETTE)]
        color = self._to_color(str(category), rgb, [str(category)])
        color.semantics = "project_categorical_palette_assignment"
        return color

    @staticmethod
    def contrast_ratio(color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> float:
        """Calculate WCAG relative-luminance contrast ratio.

        Uses the current sRGB linearization breakpoint 0.04045. Applicability of
        a particular ratio threshold still depends on the relevant WCAG success
        criterion and the visual object's role.
        """

        def luminance(rgb):
            def linearize(channel):
                value = channel / 255.0
                return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4

            return (
                0.2126 * linearize(rgb[0])
                + 0.7152 * linearize(rgb[1])
                + 0.0722 * linearize(rgb[2])
            )

        l1 = luminance(color1)
        l2 = luminance(color2)
        lighter, darker = max(l1, l2), min(l1, l2)
        return (lighter + 0.05) / (darker + 0.05)

    def resolve_series_palette(self, labels: List[str]) -> List[str]:
        """Resolve known project semantic labels, otherwise categorical fallback."""
        resolved = []
        for index, label in enumerate(labels):
            color = self.encode(str(label)) or self.encode_category(str(label), index)
            resolved.append(color.hex_code)
        return resolved

    def get_palette(self, n: int) -> List[SemanticColor]:
        if n < 0:
            raise ValueError("n must be non-negative")
        return [self.encode_category(f"palette_{index}", index) for index in range(n)]


# Preferred descriptive alias for new callers.
SemanticColorEncoder = CognitiveColorEncoder
