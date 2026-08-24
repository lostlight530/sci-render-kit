"""Uncertainty / interval metadata utilities.
[EXPERIMENTAL] Not integrated into the canonical renderer.

The historical ``UncertaintyLegend`` and ``UncertaintyBound`` names remain for
compatibility. Bounds are not called confidence intervals merely because they
have lower/upper values: callers must declare the interval ``kind`` and its
statistical or engineering ``semantics``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

INTERVAL_KINDS = {
    "standard-error",
    "standard-deviation",
    "confidence-interval",
    "credible-interval",
    "min-max-range",
    "quantile-interval",
    "bootstrap-interval",
    "heuristic-bound",
    "not-applicable",
}

LEVEL_KINDS = {"confidence-interval", "credible-interval", "bootstrap-interval", "quantile-interval"}


@dataclass
class UncertaintyBound:
    """One explicitly typed interval around a reported value."""

    value: float
    lower: float
    upper: float
    confidence: Optional[float] = None  # deprecated compatibility alias for level
    label: str = ""
    kind: str = "heuristic-bound"
    semantics: str = "caller-supplied bound; no statistical coverage claim"
    level: Optional[float] = None
    source_ref: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.value = float(self.value)
        self.lower = float(self.lower)
        self.upper = float(self.upper)
        if self.lower > self.upper:
            raise ValueError("lower must be <= upper")
        if not self.lower <= self.value <= self.upper:
            raise ValueError("value must lie inside [lower, upper]")
        if self.kind not in INTERVAL_KINDS:
            raise ValueError(f"unknown interval kind: {self.kind}")
        if self.level is None and self.confidence is not None:
            self.level = float(self.confidence)
        if self.level is not None and not 0.0 < float(self.level) <= 1.0:
            raise ValueError("interval level must be within (0,1]")
        if self.level is not None and self.kind not in LEVEL_KINDS:
            self.metadata.setdefault(
                "level_warning",
                "a level was supplied for an interval kind without a standard coverage/credible interpretation",
            )
        self.confidence = self.level
        if not str(self.semantics).strip():
            raise ValueError("semantics must be non-empty")

    def interval_width(self) -> float:
        return self.upper - self.lower

    def confidence_interval_width(self) -> float:
        """Deprecated compatibility alias; returns width without asserting CI semantics."""
        return self.interval_width()

    def relative_width(self) -> Optional[float]:
        denominator = abs(self.value)
        return self.interval_width() / denominator if denominator > 0 else None

    def to_dict(self) -> dict:
        return {
            "label": self.label,
            "value": self.value,
            "lower": self.lower,
            "upper": self.upper,
            "width": self.interval_width(),
            "kind": self.kind,
            "level": self.level,
            "semantics": self.semantics,
            "source_ref": self.source_ref,
            "metadata": dict(self.metadata),
        }


class IntervalLegend:
    """Collection of explicitly typed interval records."""

    def __init__(self):
        self._bounds: List[UncertaintyBound] = []

    def add_bound(self, bound: UncertaintyBound) -> None:
        self._bounds.append(bound)

    def add_interval(
        self,
        *,
        value: float,
        lower: float,
        upper: float,
        kind: str,
        semantics: str,
        label: str = "",
        level: Optional[float] = None,
        source_ref: Optional[str] = None,
    ) -> UncertaintyBound:
        bound = UncertaintyBound(
            value=value,
            lower=lower,
            upper=upper,
            label=label,
            kind=kind,
            semantics=semantics,
            level=level,
            source_ref=source_ref,
        )
        self.add_bound(bound)
        return bound

    def get_bounds(self) -> List[UncertaintyBound]:
        return list(self._bounds)

    def total_uncertainty(self) -> float:
        """Compatibility metric: sum of interval widths, without statistical interpretation."""
        return sum(bound.interval_width() for bound in self._bounds)

    def relative_uncertainty(self) -> float:
        values = [bound.relative_width() for bound in self._bounds]
        defined = [value for value in values if value is not None]
        return sum(defined) / len(defined) if defined else 0.0

    def uncertainty_summary(self) -> Dict[str, Any]:
        by_kind: Dict[str, int] = {}
        for bound in self._bounds:
            by_kind[bound.kind] = by_kind.get(bound.kind, 0) + 1
        return {
            "count": len(self._bounds),
            "by_kind": by_kind,
            "total_interval_width": self.total_uncertainty(),
            "mean_relative_width": self.relative_uncertainty(),
            "semantics": "descriptive interval metadata; aggregation is not a probability statement",
        }

    def visualization_data(self) -> List[Dict[str, Any]]:
        return [bound.to_dict() for bound in self._bounds]

    def complementarity_check(self, *args, **kwargs) -> bool:
        """Removed physics metaphor; no position/momentum complementarity is represented."""
        raise NotImplementedError(
            "This module models declared research intervals, not quantum complementarity."
        )


# Historical compatibility name.
UncertaintyLegend = IntervalLegend
