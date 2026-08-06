"""
Time Crystal Animation - Periodic Motion Engine
[EXPERIMENTAL] Not yet integrated into the main rendering pipeline.

Time crystals are structures that repeat in time rather than space.
This module creates animations with temporal periodicity - patterns
that oscillate, breathe, and pulse with mathematical precision.

Real-world: Procedural animation with mathematical periodicity.
"""

import math
import time
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Callable, Any
from enum import Enum


class WaveformType(Enum):
    SINE = "sine"
    SQUARE = "square"
    TRIANGLE = "triangle"
    SAWTOOTH = "sawtooth"
    PULSE = "pulse"


@dataclass
class TimeCrystal:
    """A time crystal with periodic temporal structure."""

    name: str
    frequency: float
    amplitude: float
    phase: float = 0.0
    waveform: WaveformType = WaveformType.SINE
    harmonics: List[float] = field(default_factory=list)
    damping: float = 0.0

    def value_at(self, t: float) -> float:
        """Get the crystal's value at time t."""
        base = self._waveform_value(t)

        for i, harmonic_amp in enumerate(self.harmonics):
            harmonic_freq = self.frequency * (i + 2)
            base += harmonic_amp * self._waveform_value(t, harmonic_freq)

        if self.damping > 0:
            base *= math.exp(-self.damping * t)

        return base

    def _waveform_value(self, t: float, freq: float = None) -> float:
        """Compute waveform value at time t."""
        f = freq if freq else self.frequency
        phase = 2 * math.pi * f * t + self.phase

        if self.waveform == WaveformType.SINE:
            return self.amplitude * math.sin(phase)
        elif self.waveform == WaveformType.SQUARE:
            return self.amplitude * (1 if math.sin(phase) >= 0 else -1)
        elif self.waveform == WaveformType.TRIANGLE:
            return self.amplitude * (2 / math.pi) * math.asin(math.sin(phase))
        elif self.waveform == WaveformType.SAWTOOTH:
            normalized = (phase / (2 * math.pi)) % 1.0
            return self.amplitude * (2 * normalized - 1)
        elif self.waveform == WaveformType.PULSE:
            duty = 0.3
            normalized = (phase / (2 * math.pi)) % 1.0
            return self.amplitude if normalized < duty else 0.0
        return 0.0


class TimeCrystalAnimation:
    """Animation engine driven by time crystals."""

    def __init__(self):
        self._crystals: Dict[str, TimeCrystal] = {}
        self._start_time = time.time()

    def add_crystal(self, crystal: TimeCrystal) -> None:
        """Add a time crystal to the animation."""
        self._crystals[crystal.name] = crystal

    def frame(self, t: float = None) -> Dict[str, float]:
        """Generate a frame of animation values."""
        if t is None:
            t = time.time() - self._start_time

        return {name: crystal.value_at(t) for name, crystal in self._crystals.items()}

    def animate_property(
        self,
        crystal_name: str,
        property_name: str,
        target_obj: Any,
        duration: float = None,
    ) -> Callable:
        """Create an animation callback for a specific property."""
        crystal = self._crystals.get(crystal_name)
        if not crystal:
            return lambda t: None

        start = time.time()

        def update(t: float = None):
            current_t = t if t else time.time() - start
            if duration and current_t > duration:
                return
            value = crystal.value_at(current_t)
            setattr(target_obj, property_name, value)

        return update

    def superposition(self, crystal_names: List[str], t: float = None) -> float:
        """Compute the superposition of multiple crystals."""
        if t is None:
            t = time.time() - self._start_time

        total = 0.0
        for name in crystal_names:
            crystal = self._crystals.get(name)
            if crystal:
                total += crystal.value_at(t)
        return total

    def interference(self, name_a: str, name_b: str, t: float = None) -> float:
        """Compute interference pattern between two crystals."""
        if t is None:
            t = time.time() - self._start_time

        a = self._crystals.get(name_a)
        b = self._crystals.get(name_b)
        if not a or not b:
            return 0.0

        return a.value_at(t) * b.value_at(t)

    def list_crystals(self) -> List[str]:
        """List all crystal names."""
        return list(self._crystals.keys())
