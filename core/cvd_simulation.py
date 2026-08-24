"""Color Vision Deficiency (CVD) simulation using Machado et al. (2009).
[IMPLEMENTED] Used by an optional project runtime safeguard.

The matrices simulate full-severity protanopia, deuteranopia and tritanopia.
The repository may compare simulated colors against a declared background, but
**WCAG 2.2 does not mandate this simulation test or a universal post-simulation
3:1 threshold**. The check is an additional project safeguard alongside more
direct requirements such as non-color redundant encoding and contrast for
specific graphical objects/boundaries when those boundaries are required for
understanding.
"""

from __future__ import annotations

from typing import Dict, List, Tuple

import numpy as np

CVD_TYPES = ("protanopia", "deuteranopia", "tritanopia")

# Machado, Oliveira & Fernandes (2009), severity 1.0 matrices.
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
    """Return an RGB approximation under the selected full-severity matrix."""
    if cvd_type not in MACHADO_2009:
        raise ValueError(f"unknown CVD type {cvd_type!r}; available: {', '.join(CVD_TYPES)}")
    if len(rgb) != 3 or any(not 0 <= int(channel) <= 255 for channel in rgb):
        raise ValueError(f"rgb must contain three channels in [0,255], got {rgb!r}")
    vector = np.asarray(rgb, dtype=float)
    transformed = MACHADO_2009[cvd_type] @ vector
    return tuple(int(round(value)) for value in np.clip(transformed, 0, 255))


def cvd_contrast_report(
    rgb: Tuple[int, int, int],
    bg_rgb: Tuple[int, int, int],
    contrast_fn,
) -> List[Tuple[str, float]]:
    """Return project contrast diagnostics under each CVD simulation, worst first."""
    report = []
    for cvd_type in CVD_TYPES:
        ratio = contrast_fn(
            simulate_cvd(rgb, cvd_type),
            simulate_cvd(bg_rgb, cvd_type),
        )
        report.append((cvd_type, float(ratio)))
    return sorted(report, key=lambda item: item[1])
