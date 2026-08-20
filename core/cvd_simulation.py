"""
Color Vision Deficiency (CVD) simulation — Machado et al. (2009)
[IMPLEMENTED] Consumed by the P1 ``cvd-contrast`` quality gate.

Implements the physiologically-based 3x3 transformation matrices from
Machado, Oliveira & Fernandes (2009), "A Physiologically-based Model for
Simulation of Color Vision Deficiency" (severity 1.0, i.e. full
dichromacy), for the three common deficiency types:

- ``protanopia``   (L-cone absent, ~1.3% of males)
- ``deuteranopia`` (M-cone absent, ~1.2% of males)
- ``tritanopia``   (S-cone absent, rare)

Integration point:
- ``sci_render.py`` quality gate ``cvd-contrast`` (P1): when a recipe
  declares ``background`` or enables ``semantic_palette``, every effective
  palette color is re-evaluated against the background under all three
  simulations and must keep WCAG non-text contrast >= 3.0 (SC 1.4.11)
  post-simulation.

Depends on NumPy (already required by the matplotlib backend).
"""

from typing import Dict, List, Tuple

import numpy as np

CVD_TYPES = ("protanopia", "deuteranopia", "tritanopia")

# Machado et al. (2009), severity 1.0 (full dichromacy).
MACHADO_2009: Dict[str, np.ndarray] = {
    "protanopia": np.array(
        [
            [0.152286, 1.052583, -0.204868],
            [0.114503, 0.786281, 0.099216],
            [-0.003882, -0.048116, 1.051998],
        ]
    ),
    "deuteranopia": np.array(
        [
            [0.367322, 0.860646, -0.227968],
            [0.280085, 0.672501, 0.047413],
            [-0.011820, 0.042940, 0.968881],
        ]
    ),
    "tritanopia": np.array(
        [
            [1.255528, -0.076749, -0.178779],
            [-0.078411, 0.930809, 0.147602],
            [0.004733, 0.691367, 0.303900],
        ]
    ),
}


def simulate_cvd(rgb: Tuple[int, int, int], cvd_type: str) -> Tuple[int, int, int]:
    """Simulate how ``rgb`` appears under the given CVD type.

    Returns an (r, g, b) tuple of ints clipped to [0, 255].
    Raises ``ValueError`` for unknown CVD types.
    """
    if cvd_type not in MACHADO_2009:
        raise ValueError(
            f"未知 CVD 类型 '{cvd_type}'，可用: {', '.join(CVD_TYPES)}"
        )
    v = np.asarray(rgb, dtype=float)
    out = MACHADO_2009[cvd_type] @ v
    return tuple(int(round(x)) for x in np.clip(out, 0, 255))


def cvd_contrast_report(
    rgb: Tuple[int, int, int],
    bg_rgb: Tuple[int, int, int],
    contrast_fn,
) -> List[Tuple[str, float]]:
    """Contrast of ``rgb`` vs ``bg_rgb`` under each CVD simulation.

    ``contrast_fn`` is a ``(rgb, rgb) -> float`` WCAG contrast function
    (e.g. ``CognitiveColorEncoder.contrast_ratio``). Returns a list of
    ``(cvd_type, ratio)`` sorted worst-first.
    """
    report = []
    for cvd_type in CVD_TYPES:
        ratio = contrast_fn(simulate_cvd(rgb, cvd_type), simulate_cvd(bg_rgb, cvd_type))
        report.append((cvd_type, ratio))
    report.sort(key=lambda item: item[1])
    return report
