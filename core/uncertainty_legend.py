"""
Uncertainty Principle Legend - Adaptive Precision Visualization
[EXPERIMENTAL] Not yet integrated into the main rendering pipeline.

Inspired by Heisenberg's uncertainty principle: the more precisely you
know one property, the less precisely you can know a complementary one.
This legend system visualizes data uncertainty by blurring or sharpening
visual elements based on confidence levels.

Real-world: Confidence-aware visualization with adaptive precision.
"""

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any


@dataclass
class UncertaintyBound:
    """A bound on how uncertain a value is."""

    value: float
    lower_bound: float
    upper_bound: float
    confidence: float = 1.0

    @property
    def uncertainty_range(self) -> float:
        return self.upper_bound - self.lower_bound

    @property
    def relative_uncertainty(self) -> float:
        if self.value == 0:
            return 0.0
        return self.uncertainty_range / (2 * abs(self.value))


class UncertaintyLegend:
    """Legend system for visualizing data uncertainty."""

    def __init__(self, max_blur: float = 10.0, max_opacity: float = 0.3):
        self.max_blur = max_blur
        self.max_opacity = max_opacity
        self._bounds: Dict[str, UncertaintyBound] = {}

    def register_bound(self, name: str, bound: UncertaintyBound) -> None:
        """Register an uncertainty bound for a data point."""
        self._bounds[name] = bound

    def blur_radius(self, name: str) -> float:
        """Compute blur radius based on uncertainty."""
        bound = self._bounds.get(name)
        if not bound:
            return 0.0

        uncertainty = bound.relative_uncertainty
        return min(self.max_blur, uncertainty * self.max_blur)

    def opacity(self, name: str) -> float:
        """Compute opacity based on confidence."""
        bound = self._bounds.get(name)
        if not bound:
            return 1.0

        return max(self.max_opacity, bound.confidence)

    def error_bar(self, name: str) -> Optional[Tuple[float, float, float]]:
        """Get error bar data: (value, lower, upper)."""
        bound = self._bounds.get(name)
        if not bound:
            return None
        return (bound.value, bound.lower_bound, bound.upper_bound)

    def confidence_interval_width(self, name: str) -> float:
        """Get the width of the confidence interval."""
        bound = self._bounds.get(name)
        if not bound:
            return 0.0
        return bound.uncertainty_range

    def render_legend(self) -> List[Dict[str, Any]]:
        """Generate legend entries for visualization."""
        entries = []
        for name, bound in self._bounds.items():
            entries.append(
                {
                    "name": name,
                    "value": bound.value,
                    "lower": bound.lower_bound,
                    "upper": bound.upper_bound,
                    "confidence": bound.confidence,
                    "blur_radius": self.blur_radius(name),
                    "opacity": self.opacity(name),
                    "relative_uncertainty": bound.relative_uncertainty,
                }
            )
        return entries

    def complementarity_check(self, name_a: str, name_b: str) -> Optional[float]:
        """Check if two values exhibit uncertainty complementarity.

        Returns the product of their relative uncertainties.
        If this exceeds a threshold, the pair is complementary
        (like position and momentum in quantum mechanics).
        """
        bound_a = self._bounds.get(name_a)
        bound_b = self._bounds.get(name_b)
        if not bound_a or not bound_b:
            return None

        return bound_a.relative_uncertainty * bound_b.relative_uncertainty

    def aggregate_uncertainty(self, names: List[str]) -> float:
        """Compute aggregate uncertainty across multiple data points."""
        uncertainties = []
        for name in names:
            bound = self._bounds.get(name)
            if bound:
                uncertainties.append(bound.relative_uncertainty)

        if not uncertainties:
            return 0.0

        return math.sqrt(sum(u**2 for u in uncertainties) / len(uncertainties))
