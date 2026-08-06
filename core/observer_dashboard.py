"""
Observer Effect Dashboard - Real-Time Visualization Telemetry
[EXPERIMENTAL] Not yet integrated into the main rendering pipeline.

In quantum mechanics, the observer effect states that the act of
observation changes the system being observed. This dashboard applies
that principle to visualization itself: it monitors how rendering
choices affect the viewer's understanding, creating a feedback loop
between visualization and comprehension.

Real-world: Real-time analytics dashboard with interaction tracking.
"""

import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Callable
from collections import defaultdict, deque


@dataclass
class InteractionEvent:
    """A single viewer interaction event."""

    event_type: str
    timestamp: float = field(default_factory=time.time)
    target_element: str = ""
    duration: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ComprehensionMetric:
    """A metric tracking how well the viewer understands the data."""

    metric_name: str
    value: float
    timestamp: float = field(default_factory=time.time)
    context: Dict[str, Any] = field(default_factory=dict)


class ObserverEffectDashboard:
    """Real-time dashboard tracking visualization-viewer interaction."""

    def __init__(self, window_size: int = 1000):
        self.window_size = window_size
        self._interactions: deque = deque(maxlen=window_size)
        self._comprehension: deque = deque(maxlen=window_size)
        self._element_focus: Dict[str, int] = defaultdict(int)
        self._event_type_counts: Dict[str, int] = defaultdict(int)
        self._render_callbacks: List[Callable] = []
        self._insights: List[str] = []

    def record_interaction(self, event: InteractionEvent) -> None:
        """Record a viewer interaction."""
        self._interactions.append(event)
        self._element_focus[event.target_element] += 1
        self._event_type_counts[event.event_type] += 1

        self._detect_insights(event)

    def record_comprehension(self, metric: ComprehensionMetric) -> None:
        """Record a comprehension metric."""
        self._comprehension.append(metric)

    def _detect_insights(self, event: InteractionEvent) -> None:
        """Detect patterns in viewer behavior."""
        if event.event_type == "hover" and event.duration > 5.0:
            self._insights.append(
                f"Long hover on {event.target_element} - possible confusion or interest"
            )

        recent_hovers = [
            e for e in list(self._interactions)[-10:] if e.event_type == "hover"
        ]
        if len(recent_hovers) >= 5:
            elements = set(e.target_element for e in recent_hovers)
            if len(elements) == 1:
                self._insights.append(
                    f"Repeated focus on {elements.pop()} - high interest area"
                )

    def register_render_callback(self, callback: Callable) -> None:
        """Register a callback for dashboard rendering."""
        self._render_callbacks.append(callback)

    def focus_distribution(self) -> Dict[str, float]:
        """Compute the distribution of viewer attention across elements."""
        total = sum(self._element_focus.values())
        if total == 0:
            return {}
        return {
            element: count / total for element, count in self._element_focus.items()
        }

    def engagement_score(self) -> float:
        """Compute overall viewer engagement score (0-1)."""
        if not self._interactions:
            return 0.0

        unique_elements = len(set(e.target_element for e in self._interactions))
        total_interactions = len(self._interactions)
        avg_duration = sum(e.duration for e in self._interactions) / total_interactions

        element_score = min(1.0, unique_elements / 10)
        interaction_score = min(1.0, total_interactions / 100)
        duration_score = min(1.0, avg_duration / 5.0)

        return (element_score + interaction_score + duration_score) / 3

    def comprehension_trend(self) -> List[float]:
        """Get the trend of comprehension metrics over time."""
        return [m.value for m in self._comprehension]

    def dashboard_data(self) -> Dict[str, Any]:
        """Generate complete dashboard data for rendering."""
        return {
            "total_interactions": len(self._interactions),
            "unique_elements": len(self._element_focus),
            "focus_distribution": self.focus_distribution(),
            "engagement_score": self.engagement_score(),
            "comprehension_trend": self.comprehension_trend(),
            "event_type_counts": dict(self._event_type_counts),
            "recent_insights": self._insights[-5:],
            "timestamp": time.time(),
        }

    def render(self) -> Dict[str, Any]:
        """Render the dashboard and trigger callbacks."""
        data = self.dashboard_data()
        for callback in self._render_callbacks:
            try:
                callback(data)
            except Exception:
                pass
        return data

    def reset(self) -> None:
        """Reset all tracking data."""
        self._interactions.clear()
        self._comprehension.clear()
        self._element_focus.clear()
        self._event_type_counts.clear()
        self._insights.clear()
