"""Interaction telemetry accumulator for visualization research.

[EXPERIMENTAL] Not integrated into the canonical rendering pipeline.

The historical module name ``observer_dashboard`` is retained for import
compatibility. The implementation records caller-supplied interaction events and
caller-supplied metrics in bounded deques, then exposes descriptive aggregates.
It does not observe users by itself, infer comprehension, run a real-time server,
or establish causal effects of visualization choices.
"""

from __future__ import annotations

import time
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Any, Callable, Deque, Dict, List


@dataclass
class InteractionEvent:
    """One caller-supplied interaction event."""

    event_type: str
    timestamp: float = field(default_factory=time.time)
    target_element: str = ""
    duration: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not str(self.event_type).strip():
            raise ValueError("event_type must be non-empty")
        if self.duration < 0:
            raise ValueError("duration must be >= 0")


@dataclass
class ComprehensionMetric:
    """Caller-supplied named metric; the module does not validate its construct."""

    metric_name: str
    value: float
    timestamp: float = field(default_factory=time.time)
    context: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not str(self.metric_name).strip():
            raise ValueError("metric_name must be non-empty")


class ObserverEffectDashboard:
    """Compatibility name for a bounded descriptive telemetry accumulator."""

    PROFILE = "sci-render-kit/interaction-telemetry@1"

    def __init__(self, window_size: int = 1000):
        if window_size < 1:
            raise ValueError("window_size must be >= 1")
        self.window_size = window_size
        self._interactions: Deque[InteractionEvent] = deque(maxlen=window_size)
        self._comprehension: Deque[ComprehensionMetric] = deque(maxlen=window_size)
        self._element_focus: Dict[str, int] = defaultdict(int)
        self._event_type_counts: Dict[str, int] = defaultdict(int)
        self._render_callbacks: List[Callable[[Dict[str, Any]], None]] = []
        self._signals: List[dict] = []

    def record_interaction(self, event: InteractionEvent) -> None:
        """Record one supplied event and update descriptive counts."""
        self._interactions.append(event)
        self._element_focus[event.target_element] += 1
        self._event_type_counts[event.event_type] += 1
        self._derive_signals(event)

    def record_comprehension(self, metric: ComprehensionMetric) -> None:
        """Store a supplied metric without claiming it measures true comprehension."""
        self._comprehension.append(metric)

    def _derive_signals(self, event: InteractionEvent) -> None:
        """Create bounded heuristic interaction signals, not psychological conclusions."""
        if event.event_type == "hover" and event.duration > 5.0:
            self._signals.append(
                {
                    "type": "long-hover",
                    "target": event.target_element,
                    "semantics": "interaction heuristic; may reflect interest, confusion, inactivity, or another cause",
                }
            )

        recent_hovers = [item for item in list(self._interactions)[-10:] if item.event_type == "hover"]
        if len(recent_hovers) >= 5:
            elements = {item.target_element for item in recent_hovers}
            if len(elements) == 1:
                self._signals.append(
                    {
                        "type": "repeated-hover-target",
                        "target": next(iter(elements)),
                        "semantics": "interaction concentration only; not a comprehension or attention diagnosis",
                    }
                )
        if len(self._signals) > self.window_size:
            self._signals = self._signals[-self.window_size :]

    def register_render_callback(self, callback: Callable[[Dict[str, Any]], None]) -> None:
        if not callable(callback):
            raise TypeError("callback must be callable")
        self._render_callbacks.append(callback)

    def focus_distribution(self) -> Dict[str, float]:
        """Return interaction-count proportions by target element."""
        total = sum(self._element_focus.values())
        if total == 0:
            return {}
        return {element: count / total for element, count in self._element_focus.items()}

    def interaction_activity_score(self) -> float:
        """Return a project heuristic activity score in [0,1], not engagement truth."""
        if not self._interactions:
            return 0.0
        unique_elements = len({event.target_element for event in self._interactions})
        total_interactions = len(self._interactions)
        avg_duration = sum(event.duration for event in self._interactions) / total_interactions
        element_component = min(1.0, unique_elements / 10.0)
        count_component = min(1.0, total_interactions / 100.0)
        duration_component = min(1.0, avg_duration / 5.0)
        return (element_component + count_component + duration_component) / 3.0

    def engagement_score(self) -> float:
        """Compatibility alias for ``interaction_activity_score``."""
        return self.interaction_activity_score()

    def comprehension_trend(self) -> List[float]:
        """Return supplied metric values in observation order."""
        return [metric.value for metric in self._comprehension]

    def dashboard_data(self) -> Dict[str, Any]:
        return {
            "profile": self.PROFILE,
            "total_interactions": len(self._interactions),
            "unique_elements": len(self._element_focus),
            "focus_distribution": self.focus_distribution(),
            "interaction_activity_score": self.interaction_activity_score(),
            "metric_values": self.comprehension_trend(),
            "event_type_counts": dict(self._event_type_counts),
            "recent_signals": self._signals[-5:],
            "generated_at_unix": time.time(),
            "semantics": {
                "server_or_sensor_built_in": False,
                "comprehension_inferred": False,
                "causal_effect_claim": False,
            },
        }

    def render(self) -> Dict[str, Any]:
        """Return dashboard data and invoke registered callbacks best-effort."""
        data = self.dashboard_data()
        for callback in self._render_callbacks:
            try:
                callback(data)
            except Exception:
                continue
        return data

    def reset(self) -> None:
        self._interactions.clear()
        self._comprehension.clear()
        self._element_focus.clear()
        self._event_type_counts.clear()
        self._signals.clear()
