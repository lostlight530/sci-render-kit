"""Deterministic variant-layer utilities.
[EXPERIMENTAL] Not integrated into the canonical renderer.

The historical ``SuperpositionEngine`` name is retained for compatibility. The
implementation stores alternative visualization states and can combine numeric
properties using explicitly declared normalized weights. This is ordinary
variant aggregation, not quantum superposition or wave interference.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class VisualizationState:
    state_id: str
    data: Dict[str, Any]
    weight: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.state_id:
            raise ValueError("state_id must be non-empty")
        self.weight = float(self.weight)
        if self.weight < 0:
            raise ValueError("weight must be non-negative")


class VariantLayerEngine:
    """Store named alternatives and compute transparent weighted aggregates."""

    def __init__(self):
        self._states: Dict[str, VisualizationState] = {}

    def add_state(self, state: VisualizationState) -> None:
        self._states[state.state_id] = state

    def remove_state(self, state_id: str) -> None:
        self._states.pop(state_id, None)

    def get_state(self, state_id: str) -> Optional[VisualizationState]:
        return self._states.get(state_id)

    def states(self) -> List[VisualizationState]:
        return list(self._states.values())

    def normalized_weights(self) -> Dict[str, float]:
        total = sum(state.weight for state in self._states.values())
        if total <= 0:
            return {state_id: 0.0 for state_id in self._states}
        return {state_id: state.weight / total for state_id, state in self._states.items()}

    def weighted_numeric_merge(self) -> Dict[str, float]:
        """Weighted-average shared numeric keys; missing/non-numeric values are ignored."""
        weights = self.normalized_weights()
        accum: Dict[str, float] = {}
        used_weight: Dict[str, float] = {}
        for state_id, state in self._states.items():
            weight = weights.get(state_id, 0.0)
            for key, value in state.data.items():
                if isinstance(value, bool) or not isinstance(value, (int, float)):
                    continue
                accum[key] = accum.get(key, 0.0) + float(value) * weight
                used_weight[key] = used_weight.get(key, 0.0) + weight
        return {
            key: accum[key] / used_weight[key]
            for key in accum
            if used_weight.get(key, 0.0) > 0
        }

    def select_max_weight(self) -> Optional[VisualizationState]:
        if not self._states:
            return None
        return max(self._states.values(), key=lambda state: (state.weight, state.state_id))

    def interference_pattern(self, *args, **kwargs):
        """Removed compatibility method: no physical wave-interference model exists."""
        raise NotImplementedError(
            "VariantLayerEngine does not model quantum/wave interference. "
            "Use explicit deterministic aggregation appropriate to the data semantics."
        )

    def summary(self) -> dict:
        return {
            "state_count": len(self._states),
            "normalized_weights": self.normalized_weights(),
            "semantics": "deterministic_variant_layering_not_quantum_superposition",
        }


# Historical compatibility name.
SuperpositionEngine = VariantLayerEngine
