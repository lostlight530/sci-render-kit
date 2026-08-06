"""
Quantum Superposition Layer - Multi-State Data Visualization
[EXPERIMENTAL] Not yet integrated into the main rendering pipeline.

In quantum mechanics, superposition allows a particle to exist in
multiple states simultaneously until observed. This layer enables
data to exist in multiple visual states at once, with the final
rendering determined by the observer's perspective.

Real-world: Multi-state rendering with perspective-dependent output.
"""

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any, Callable
from enum import Enum


class ObserverMode(Enum):
    OVERVIEW = "overview"
    DETAIL = "detail"
    COMPARISON = "comparison"
    TEMPORAL = "temporal"


@dataclass
class SuperpositionState:
    """A single state in a superposition."""

    state_id: str
    label: str
    weight: float = 1.0
    visual_properties: Dict[str, Any] = field(default_factory=dict)
    condition: Optional[Callable[[Dict[str, Any]], bool]] = None


class SuperpositionLayer:
    """Multi-state data layer with observer-dependent rendering."""

    def __init__(self):
        self._states: Dict[str, SuperpositionState] = {}
        self._observations: List[Dict[str, Any]] = []

    def add_state(self, state: SuperpositionState) -> None:
        """Add a state to the superposition."""
        self._states[state.state_id] = state

    def collapse(
        self, observer_mode: ObserverMode, context: Dict[str, Any] = None
    ) -> Optional[SuperpositionState]:
        """Collapse the superposition based on observer mode."""
        context = context or {}

        eligible_states = []
        for state in self._states.values():
            if state.condition is None or state.condition(context):
                eligible_states.append(state)

        if not eligible_states:
            return None

        mode_preferences = {
            ObserverMode.OVERVIEW: lambda s: -s.weight,
            ObserverMode.DETAIL: lambda s: s.weight,
            ObserverMode.COMPARISON: lambda s: 0,
            ObserverMode.TEMPORAL: lambda s: s.weight,
        }

        eligible_states.sort(key=mode_preferences.get(observer_mode, lambda s: 0))

        collapsed = eligible_states[0]

        observation = {
            "timestamp": __import__("time").time(),
            "observer_mode": observer_mode.value,
            "collapsed_state": collapsed.state_id,
            "eligible_count": len(eligible_states),
        }
        self._observations.append(observation)

        return collapsed

    def superpose(self, state_ids: List[str]) -> Dict[str, Any]:
        """Compute the superposition of multiple states."""
        result = {}
        states = [self._states[sid] for sid in state_ids if sid in self._states]

        if not states:
            return result

        total_weight = sum(s.weight for s in states)
        if total_weight == 0:
            return result

        all_keys = set()
        for s in states:
            all_keys.update(s.visual_properties.keys())

        for key in all_keys:
            weighted_sum = 0.0
            for state in states:
                val = state.visual_properties.get(key, 0)
                if isinstance(val, (int, float)):
                    weighted_sum += val * state.weight
                else:
                    weighted_sum = val
                    break

            if isinstance(weighted_sum, float):
                result[key] = weighted_sum / total_weight
            else:
                result[key] = weighted_sum

        return result

    def interference_pattern(self, state_a: str, state_b: str) -> float:
        """Compute interference between two states."""
        sa = self._states.get(state_a)
        sb = self._states.get(state_b)
        if not sa or not sb:
            return 0.0

        return sa.weight * sb.weight * math.cos(sa.weight - sb.weight)

    def list_states(self) -> List[str]:
        """List all state IDs in the superposition."""
        return list(self._states.keys())

    def observation_history(self) -> List[Dict[str, Any]]:
        """Get history of collapse observations."""
        return list(self._observations)

    def reset(self) -> None:
        """Reset the superposition to its initial state."""
        self._observations.clear()
