#!/usr/bin/env python3
"""Optional accessibility contracts for sci-render-kit.

These checks exercise figure-level accessibility semantics only. They do not
claim whole-document WCAG conformance and are not GitHub merge policy.
"""

from __future__ import annotations

import os
import sys
import unittest

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.accessibility import (
    PROFILE,
    build_accessibility_manifest,
    distinct_style_signatures,
    resolve_series_styles,
)
from sci_render import evaluate_pre_render_rules, load_yaml


class TestAccessibilityContract(unittest.TestCase):
    def setUp(self):
        self.rules = load_yaml("quality/rules.yaml")

    def test_required_alt_text_is_an_error_finding(self):
        recipe = {
            "type": "line-chart",
            "data": {"a": [1, 2]},
            "aesthetics": {"palette": ["#0072B2"]},
            "accessibility": {"require_alt_text": True},
            "output": {},
        }
        findings = evaluate_pre_render_rules(recipe, {}, self.rules)
        missing = [item for item in findings if item["check_id"] == "text-alternative"]
        self.assertEqual(len(missing), 1)
        self.assertEqual(missing[0]["severity"], "error")

        recipe["accessibility"]["alt_text"] = "Series a increases from 1 to 2."
        findings = evaluate_pre_render_rules(recipe, {}, self.rules)
        self.assertFalse(any(item["check_id"] == "text-alternative" for item in findings))

    def test_redundant_styles_are_unique_for_multiseries(self):
        labels = ["control", "treatment", "baseline"]
        styles = resolve_series_styles(labels, {"redundant_encoding": "required"})
        self.assertEqual(len(styles), len(labels))
        self.assertEqual(distinct_style_signatures(styles), len(labels))

    def test_generated_styles_scale_beyond_eight_series_without_colliding(self):
        labels = [f"series-{index}" for index in range(32)]
        styles = resolve_series_styles(labels, {"redundant_encoding": "required"})
        self.assertEqual(len(styles), 32)
        self.assertEqual(distinct_style_signatures(styles), 32)
        self.assertEqual(styles["series-0"]["line_style"], "-")
        self.assertNotEqual(styles["series-0"], styles["series-8"])
        for chart_type in ("line-chart", "scatter-plot", "bar-chart"):
            self.assertEqual(distinct_style_signatures(styles, chart_type=chart_type), 32)
            recipe = {
                "type": chart_type,
                "data": {label: [index] for index, label in enumerate(labels)},
                "accessibility": {"redundant_encoding": "required"},
                "output": {},
            }
            findings = evaluate_pre_render_rules(recipe, {}, self.rules)
            self.assertFalse(
                any(item["check_id"] == "non-color-cue" for item in findings),
                findings,
            )

    def test_effective_cues_ignore_unrendered_style_fields(self):
        styles = {
            "a": {"marker": "o", "line_style": "-", "hatch": "//"},
            "b": {"marker": "o", "line_style": ":", "hatch": "//"},
        }
        self.assertEqual(distinct_style_signatures(styles), 2)
        self.assertEqual(distinct_style_signatures(styles, chart_type="line-chart"), 2)
        self.assertEqual(distinct_style_signatures(styles, chart_type="scatter-plot"), 1)
        self.assertEqual(distinct_style_signatures(styles, chart_type="bar-chart"), 1)

        for chart_type in ("scatter-plot", "bar-chart"):
            recipe = {
                "type": chart_type,
                "data": {"a": [1], "b": [2]},
                "accessibility": {
                    "redundant_encoding": "required",
                    "series_styles": styles,
                },
                "output": {},
            }
            findings = evaluate_pre_render_rules(recipe, {}, self.rules)
            self.assertTrue(
                any(item["check_id"] == "non-color-cue" for item in findings),
                findings,
            )

    def test_generated_style_budget_does_not_hide_collisions(self):
        labels = [f"series-{index}" for index in range(33)]
        styles = resolve_series_styles(labels, {"redundant_encoding": "required"})
        self.assertLess(distinct_style_signatures(styles), len(labels))
        for chart_type in ("line-chart", "scatter-plot", "bar-chart"):
            self.assertLess(distinct_style_signatures(styles, chart_type=chart_type), 33)
            recipe = {
                "type": chart_type,
                "data": {label: [index] for index, label in enumerate(labels)},
                "accessibility": {"redundant_encoding": "required"},
                "output": {},
            }
            findings = evaluate_pre_render_rules(recipe, {}, self.rules)
            self.assertTrue(
                any(item["check_id"] == "non-color-cue" for item in findings),
                findings,
            )

    def test_declared_adjacency_only_checks_declared_pairs(self):
        recipe = {
            "type": "line-chart",
            "data": {"a": [1, 2], "b": [2, 3], "c": [3, 4]},
            "aesthetics": {"palette": ["#000000", "#0072B2", "#D55E00"]},
            "accessibility": {"adjacent_pairs": [["b", "c"]]},
            "output": {},
        }
        findings = evaluate_pre_render_rules(recipe, {}, self.rules)
        adjacency = [item for item in findings if item["check_id"] == "declared-adjacency"]
        self.assertTrue(any("(b, c)" in item["message"] for item in adjacency), adjacency)
        self.assertFalse(any("(a, b)" in item["message"] for item in adjacency), adjacency)

    def test_all_pairs_palette_policy_is_project_warning(self):
        recipe = {
            "type": "line-chart",
            "data": {"a": [1], "b": [2]},
            "aesthetics": {
                "palette": ["#0072B2", "#D55E00"],
                "adjacency_check": True,
            },
            "output": {},
        }
        findings = evaluate_pre_render_rules(recipe, {}, self.rules)
        items = [item for item in findings if item["check_id"] == "palette-adjacency"]
        self.assertTrue(items)
        self.assertTrue(all(item["severity"] == "warning" for item in items))
        self.assertTrue(all("project" in item["message"].lower() for item in items))

    def test_cvd_check_is_project_warning_not_wcag_certificate(self):
        recipe = {
            "type": "line-chart",
            "data": {"a": [1, 2]},
            "aesthetics": {
                "palette": ["#CC79A7"],
                "background": "#FFFFFF",
            },
            "output": {},
        }
        findings = evaluate_pre_render_rules(recipe, {}, self.rules)
        cvd = [item for item in findings if item["check_id"] == "cvd-contrast"]
        self.assertTrue(cvd)
        self.assertTrue(all(item["severity"] == "warning" for item in cvd))
        self.assertTrue(
            all("not a WCAG-mandated" in item.get("details", {}).get("standard_scope", "") for item in cvd)
        )

    def test_accessibility_manifest_preserves_scope_and_non_color_cues(self):
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

    def test_backend_capability_matrix_does_not_claim_parity(self):
        from sci_render import BACKEND_ACCESSIBILITY_CAPABILITIES

        self.assertIn("redundant-series-style", BACKEND_ACCESSIBILITY_CAPABILITIES["matplotlib"])
        self.assertNotIn("redundant-series-style", BACKEND_ACCESSIBILITY_CAPABILITIES["ggplot2"])
        self.assertNotIn("redundant-series-style", BACKEND_ACCESSIBILITY_CAPABILITIES["observable"])


if __name__ == "__main__":
    unittest.main()
