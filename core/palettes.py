"""
Named palette registry — curated, CVD-annotated color scales
[IMPLEMENTED] Consumed by ``aesthetics.palette_name`` (series charts) and
the P1 ``palette-name`` quality gate.

Each entry declares:
- ``kind``: ``categorical`` (离散分类) / ``sequential`` (顺序色阶) /
  ``diverging`` (发散色阶)
- ``cvd_safety``: ``high`` / ``medium`` / ``unverified`` — 色盲安全性级别
- ``source``: 出处标准 / 文献
- ``availability``: 各后端的可得性（诚实声明；非内置的不伪装成内置）
- ``colors``: categorical 色板的 hex 序列（后端无关，与 R/JS 对齐风格一致）

Only categorical palettes resolve to hex lists here. Sequential/diverging
scales are referenced by name (``mpl_name``) and validated against the
active backend at render time.
"""

from typing import Dict, List

PALETTE_REGISTRY: Dict[str, dict] = {
    "okabe-ito": {
        "kind": "categorical",
        "cvd_safety": "high",
        "source": "Okabe & Ito (2008), Color Universal Design",
        "availability": {"matplotlib": "builtin(hex)", "ggplot2": "builtin(hex)", "observable": "builtin(hex)"},
        "colors": [
            "#E69F00", "#56B4E9", "#009E73", "#F0E442",
            "#0072B2", "#D55E00", "#CC79A7", "#000000",
        ],
    },
    "petroff10": {
        "kind": "categorical",
        "cvd_safety": "high",
        "source": "Petroff (2021) arXiv:2107.02270; matplotlib >= 3.10 color_sequences",
        "availability": {"matplotlib": "builtin (color_sequences['petroff10'])", "ggplot2": "hex 内嵌", "observable": "hex 内嵌"},
        "colors": [
            "#3F90DA", "#FFA90E", "#BD1F01", "#94A4A2", "#832DB6",
            "#A96B59", "#E76300", "#B9AC70", "#717581", "#92DADD",
        ],
    },
    "viridis": {
        "kind": "sequential",
        "cvd_safety": "high",
        "source": "Garnier (2018) viridis; matplotlib 默认感知均匀色阶",
        "availability": {"matplotlib": "builtin colormap", "ggplot2": "viridisLite::viridis", "observable": "Plot scheme"},
        "mpl_name": "viridis",
    },
    "cividis": {
        "kind": "sequential",
        "cvd_safety": "high",
        "source": "Nuñez et al. (2018) cividis — CVD 下感知线性",
        "availability": {"matplotlib": "builtin colormap", "ggplot2": "viridisLite::cividis", "observable": "Plot scheme"},
        "mpl_name": "cividis",
    },
    "mako": {
        "kind": "sequential",
        "cvd_safety": "unverified",
        "source": "seaborn mako（感知均匀）；本仓库未独立验证其 CVD 安全性",
        "availability": {"matplotlib": "不可用（非内置，需 seaborn）", "ggplot2": "不可用", "observable": "不可用"},
        "mpl_name": None,
    },
    "berlin": {
        "kind": "diverging",
        "cvd_safety": "high",
        "source": "Crameri (2021) Scientific Colour Maps v8",
        "availability": {"matplotlib": "不可用（非内置，需 cmcrameri）", "ggplot2": "不可用", "observable": "不可用"},
        "mpl_name": None,
    },
    "managua": {
        "kind": "diverging",
        "cvd_safety": "high",
        "source": "Crameri (2021) Scientific Colour Maps v8",
        "availability": {"matplotlib": "不可用（非内置，需 cmcrameri）", "ggplot2": "不可用", "observable": "不可用"},
        "mpl_name": None,
    },
    "vanimo": {
        "kind": "diverging",
        "cvd_safety": "high",
        "source": "Crameri (2021) Scientific Colour Maps v8",
        "availability": {"matplotlib": "不可用（非内置，需 cmcrameri）", "ggplot2": "不可用", "observable": "不可用"},
        "mpl_name": None,
    },
}


def available_palettes() -> List[str]:
    """全部已注册色板名。"""
    return sorted(PALETTE_REGISTRY)


def describe_palette(name: str) -> dict:
    """返回色板元数据；未知名称抛 ValueError（列出可用名）。"""
    if name not in PALETTE_REGISTRY:
        raise ValueError(
            f"未知色板 '{name}'，可用: {', '.join(available_palettes())}"
        )
    return PALETTE_REGISTRY[name]


def resolve_categorical(name: str, n: int = None) -> List[str]:
    """解析 categorical 色板的 hex 序列（可选截取前 n 色）。

    非 categorical 色板（sequential/diverging）抛 ValueError ——
    色阶请通过 ``aesthetics.cmap`` 声明并由后端按名解析。
    """
    entry = describe_palette(name)
    if entry["kind"] != "categorical":
        raise ValueError(
            f"色板 '{name}' 是 {entry['kind']} 色阶，不是分类色板；"
            f"顺序/发散色阶请用 aesthetics.cmap 声明"
        )
    colors = list(entry["colors"])
    return colors if n is None else colors[:n]
