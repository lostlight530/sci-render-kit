"""Periodic waveform and procedural-animation utilities.
[EXPERIMENTAL] Not integrated into the canonical renderer.

The historical ``TimeCrystal`` naming is retained for compatibility. This
module generates ordinary periodic functions over time; it does not model a
physical time crystal, spontaneous time-translation symmetry breaking, or any
quantum many-body system.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class CrystalPattern(Enum):
    SINE = "sine"
    COSINE = "cosine"
    TRIANGLE = "triangle"
    SAWTOOTH = "sawtooth"
    SQUARE = "square"


@dataclass
class TimeCrystalState:
    """Compatibility record for one periodic waveform channel."""

    name: str
    frequency: float
    amplitude: float = 1.0
    phase: float = 0.0
    pattern: CrystalPattern = CrystalPattern.SINE

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("name must be non-empty")
        self.frequency = float(self.frequency)
        self.amplitude = float(self.amplitude)
        self.phase = float(self.phase)
        if self.frequency < 0:
            raise ValueError("frequency must be non-negative")


class PeriodicWaveformEngine:
    """Evaluate named deterministic periodic waveform channels."""

    def __init__(self):
        self._states: Dict[str, TimeCrystalState] = {}
        self._origin = time.monotonic()

    def add_state(self, state: TimeCrystalState) -> None:
        self._states[state.name] = state

    def remove_state(self, name: str) -> None:
        self._states.pop(name, None)

    @staticmethod
    def _wave(pattern: CrystalPattern, angle: float) -> float:
        if pattern == CrystalPattern.SINE:
            return math.sin(angle)
        if pattern == CrystalPattern.COSINE:
            return math.cos(angle)
        phase = (angle / (2 * math.pi)) % 1.0
        if pattern == CrystalPattern.TRIANGLE:
            return 1.0 - 4.0 * abs(phase - 0.5)
        if pattern == CrystalPattern.SAWTOOTH:
            return 2.0 * phase - 1.0
        if pattern == CrystalPattern.SQUARE:
            return 1.0 if phase < 0.5 else -1.0
        raise ValueError(f"unsupported pattern: {pattern}")

    def value(self, name: str, t: Optional[float] = None) -> float:
        state = self._states.get(name)
        if state is None:
            raise KeyError(f"unknown waveform state: {name}")
        elapsed = (time.monotonic() - self._origin) if t is None else float(t)
        angle = 2.0 * math.pi * state.frequency * elapsed + state.phase
        return state.amplitude * self._wave(state.pattern, angle)

    def snapshot(self, t: Optional[float] = None) -> Dict[str, float]:
        elapsed = (time.monotonic() - self._origin) if t is None else float(t)
        return {name: self.value(name, elapsed) for name in sorted(self._states)}

    def sample(self, name: str, start: float, stop: float, count: int) -> List[dict]:
        if count < 2:
            raise ValueError("count must be >= 2")
        if stop < start:
            raise ValueError("stop must be >= start")
        step = (stop - start) / (count - 1)
        return [
            {"t": start + index * step, "value": self.value(name, start + index * step)}
            for index in range(count)
        ]

    def reset_origin(self) -> None:
        self._origin = time.monotonic()

    def summary(self) -> dict:
        return {
            "channels": sorted(self._states),
            "semantics": "deterministic_periodic_waveform_not_physical_time_crystal",
        }


# Historical compatibility name.
TimeCrystal = PeriodicWaveformEngine
