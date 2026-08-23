#!/usr/bin/env python3
"""Accessibility contract tests for sci-render-kit."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.accessibility import (
    PROFILE,
    build_accessibility_manifest,
    distinct_style_signatures,
    resolve_series_styles,
)
from sci_render import load_yaml, run_quality_gates


class TestAccessibilityContract(unittest.TestCase):
    def setUp(self):
        self.gates = load_yaml("quality/gates.yaml")

    def test_required_alt_text_is_enforced(self):
        recipe = {
            "type": "line-chart",
            "data": {"a": [1, 2]},
            "aesthetics": {"palette": ["#0072B2"]},
            "accessibility": {"require_alt_text": True},
            "output": {},
        }
        errors = run_quality_gates(recipe, {}, self.gates)
        self.assertTrue(any("SC 1.1.1" in error for error in errors), errors)
        recipe["accessibility"]["alt_text"] = "Series a increases from 1 to 2."
        errors = run_quality_gates(recipe, {}, self.gates)
        self.assertFalse(any("SC 1.1.1" in error for error in errors), errors)

    def test_redundant_styles_are_unique_for_multiseries(self):
        labels = ["control", "treatment", "baseline"]
        styles = resolve_series_styles(labels, {"redundant_encoding": "required"})
        self.assertEqual(len(styles), len(labels))
        self.assertEqual(distinct_style_signatures(styles), len(labels))

    def test_declared_adjacency_checks_only_declared_pairs(self):
        recipe = {
            "type": "line-chart",
            "data": {"a": [1, 2], "b": [2, 3], "c": [3, 4]},
            "aesthetics": {"palette": ["#000000", "#0072B2", "#D55E00"]},
            "accessibility": {"adjacent_pairs": [["b", "c"]]},
            "output": {},
        }
        errors = run_quality_gates(recipe, {}, self.gates)
        self.assertTrue(any("SC 1.4.11" in error and "(b, c)" in error for error in errors), errors)
        # a/b are not declared adjacent, so their relationship is not tested by this gate.
        self.assertFalse(any("(a, b)" in error for error in errors), errors)

    def test_manifest_keeps_text_and_non_color_cues(self):
        recipe = {
            "id": "accessible",
            "type": "line-chart",
            "data": {"a": [1], "b": [2]},
            "accessibility": {
                "alt_text": "Two-series comparison.",
                "redundant_encoding": "required",
            },
        }
        manifest = build_accessibility_manifest(recipe, ["#000000", "#0072B2"])
        self.assertEqual(manifest["profile"], PROFILE)
        self.assertEqual(manifest["alt_text"], "Two-series comparison.")
        self.assertFalse(manifest["standards_scope"]["conformance_claim"])
        self.assertTrue(all("non_color_cue" in series for series in manifest["series"]))

    def test_matplotlib_cli_emits_accessibility_sidecar_and_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            recipe_path = out / "recipe.yaml"
            recipe = {
                "id": "accessible-e2e",
                "type": "line-chart",
                "data": {"control": [1, 2, 3], "treatment": [1, 3, 5]},
                "aesthetics": {
                    "palette": ["#000000", "#0072B2"],
                    "background": "#FFFFFF",
                },
                "accessibility": {
                    "require_alt_text": True,
                    "alt_text": "Control rises slowly while treatment rises faster.",
                    "redundant_encoding": "required",
                    "adjacent_pairs": [["control", "treatment"]],
                },
                "output": {
                    "dir": str(out),
                    "filename": "accessible.png",
                    "format": "png",
                },
            }
            recipe_path.write_text(yaml.safe_dump(recipe, sort_keys=False), encoding="utf-8")
            proc = subprocess.run(
                ["python3", "sci_render.py", str(recipe_path), "--profile", "presentation", "--backend", "matplotlib"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + "\n" + proc.stderr)
            image = out / "accessible.png"
            sidecar = out / "accessible.a11y.json"
            self.assertTrue(image.exists())
            self.assertTrue(sidecar.exists())
            payload = json.loads(sidecar.read_text(encoding="utf-8"))
            self.assertEqual(payload["alt_text"], recipe["accessibility"]["alt_text"])
            self.assertEqual(payload["redundant_encoding"], "required")
            self.assertTrue(all("non_color_cue" in item for item in payload["series"]))
            try:
                from PIL import Image
                with Image.open(image) as opened:
                    self.assertEqual(opened.info.get("srk:alt-text"), recipe["accessibility"]["alt_text"])
            except ImportError:
                pass

    def test_non_matplotlib_backend_does_not_fake_redundant_style_support(self):
        with tempfile.TemporaryDirectory() as tmp:
            recipe_path = Path(tmp) / "recipe.yaml"
            recipe = {
                "id": "backend-a11y",
                "type": "line-chart",
                "data": {"a": [1], "b": [2]},
                "aesthetics": {"palette": ["#000000", "#0072B2"]},
                "accessibility": {"redundant_encoding": "required"},
                "output": {"dir": tmp, "filename": "x.html", "format": "html"},
            }
            recipe_path.write_text(yaml.safe_dump(recipe, sort_keys=False), encoding="utf-8")
            proc = subprocess.run(
                ["python3", "sci_render.py", str(recipe_path), "--profile", "presentation", "--backend", "observable"],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("BACKEND_ACCESSIBILITY_MISMATCH", proc.stdout)


if __name__ == "__main__":
    unittest.main()
