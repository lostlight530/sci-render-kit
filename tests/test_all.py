#!/usr/bin/env python3
"""Optional local contracts for the current sci-render-kit architecture.

This file is intentionally lightweight: it describes current machine-readable
interfaces without treating a local test run as GitHub merge policy, publisher
acceptance, scientific validation, or independent reproduction.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.figure_evidence import PROFILE as FIGURE_EVIDENCE_PROFILE, build_figure_evidence
from core.projection import PCAProjection, ProjectionQualityMetrics, TSNEProjection
from core.uncertainty_legend import UncertaintyBound
from sci_render import _rule_index, has_errors


ROOT = Path(__file__).resolve().parents[1]


class TestRepositoryContracts(unittest.TestCase):
    def test_active_machine_contracts_exist(self):
        for relative in (
            "metadata/recipe.schema.yaml",
            "metadata/reproducibility.schema.yaml",
            "quality/rules.yaml",
            "RESEARCH_CONTRACT.md",
            "MANIFEST.yaml",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)
        self.assertFalse((ROOT / "quality/gates.yaml").exists())

    def test_runtime_rule_catalog_is_severity_aware(self):
        catalog = yaml.safe_load((ROOT / "quality/rules.yaml").read_text(encoding="utf-8"))
        self.assertEqual(catalog["profile"], "sci-render-kit/runtime-quality@1")
        index = _rule_index(catalog)
        self.assertIn("text-alternative", index)
        self.assertEqual(index["text-alternative"]["severity"], "error")
        self.assertEqual(index["cvd-contrast"]["severity"], "warning")
        self.assertEqual(index["preferred-format"]["severity"], "warning")
        self.assertTrue(has_errors([{"severity": "warning"}, {"severity": "error"}]))
        self.assertFalse(has_errors([{"severity": "warning"}, {"severity": "info"}]))

    def test_recipe_schema_carries_research_and_uncertainty_semantics(self):
        schema = yaml.safe_load((ROOT / "metadata/recipe.schema.yaml").read_text(encoding="utf-8"))
        props = schema["properties"]
        self.assertIn("research_context", props)
        self.assertIn("uncertainty", props)
        uncertainty = props["uncertainty"]
        self.assertEqual(set(uncertainty["required"]), {"kind", "semantics"})
        kinds = set(uncertainty["properties"]["kind"]["enum"])
        self.assertIn("confidence-interval", kinds)
        self.assertIn("credible-interval", kinds)
        self.assertIn("heuristic-bound", kinds)

    def test_render_manifest_schema_is_r1_not_r3_claim(self):
        schema = yaml.safe_load((ROOT / "metadata/reproducibility.schema.yaml").read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["profile"]["const"], "sci-render-kit/render-manifest@2")
        rendered = json.dumps(schema, ensure_ascii=False)
        self.assertIn("R1", rendered)
        self.assertNotIn('"level": "R3"', rendered)

    def test_profiles_expose_evidence_state(self):
        expected = {
            "nature": "publisher_guidance_reverified",
            "science": "snapshot_not_reverified_2026_08_24",
            "cell": "snapshot_not_reverified_2026_08_24",
            "ieee": "snapshot_not_reverified_2026_08_24",
            "presentation": "internal_project_preset",
        }
        for name, status in expected.items():
            profile = yaml.safe_load((ROOT / f"profiles/{name}.yaml").read_text(encoding="utf-8"))
            self.assertEqual(profile["source_status"], status)
            self.assertFalse(profile["publication"]["acceptance_claim"])


class TestFigureEvidence(unittest.TestCase):
    def test_figure_evidence_keeps_handoff_and_scientific_boundaries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            recipe = root / "recipe.yaml"
            profile = root / "profile.yaml"
            output = root / "figure.png"
            manifest = root / "figure.manifest.json"
            recipe.write_text("id: r\n", encoding="utf-8")
            profile.write_text("name: p\n", encoding="utf-8")
            output.write_bytes(b"figure")
            manifest.write_text('{"profile":"sci-render-kit/render-manifest@2"}\n', encoding="utf-8")

            evidence = build_figure_evidence(
                recipe={
                    "id": "r",
                    "research_context": {"evidence_envelope_ref": "upstream.evidence.json"},
                    "uncertainty": {
                        "kind": "heuristic-bound",
                        "semantics": "project score range, not a confidence interval",
                    },
                },
                recipe_path=str(recipe),
                profile={"name": "p", "source_status": "internal_project_preset"},
                profile_path=str(profile),
                backend="matplotlib",
                output_path=str(output),
                manifest_path=str(manifest),
                provenance_path=None,
                accessibility_path=None,
                runtime_findings=[{"severity": "warning", "check_id": "example"}],
            )

            self.assertEqual(evidence["profile"], FIGURE_EVIDENCE_PROFILE)
            self.assertEqual(FIGURE_EVIDENCE_PROFILE, "sci-render-kit/figure-evidence@1")
            self.assertFalse(evidence["scientific_validity_claim"])
            self.assertEqual(evidence["reproducibility"]["level"], "R1")
            self.assertEqual(
                evidence["research_context"]["evidence_envelope_ref"],
                "upstream.evidence.json",
            )
            self.assertEqual(evidence["uncertainty"]["kind"], "heuristic-bound")


class TestExperimentalHonesty(unittest.TestCase):
    def test_uncertainty_bound_does_not_default_to_confidence_interval(self):
        bound = UncertaintyBound(
            value=10.0,
            lower_bound=8.0,
            upper_bound=12.0,
            semantics="engineering tolerance supplied by caller",
        )
        self.assertEqual(bound.kind, "heuristic-bound")
        self.assertEqual(bound.interval_width, 4.0)
        self.assertEqual(bound.confidence_interval_width(), 4.0)

    def test_tsne_is_explicitly_not_implemented(self):
        import numpy as np

        with self.assertRaises(NotImplementedError):
            TSNEProjection().fit_transform(np.array([[0.0, 0.0], [1.0, 1.0]]))

    def test_pca_and_projection_metrics_are_computed_not_constants(self):
        import numpy as np

        data = np.array([[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [2.0, 2.0, 0.1], [3.0, 3.0, 0.0]])
        projected = PCAProjection(n_components=2).fit_transform(data)
        self.assertEqual(projected.shape, (4, 2))
        stress = ProjectionQualityMetrics.stress(data, projected)
        self.assertGreaterEqual(stress, 0.0)
        self.assertLessEqual(stress, 1.0)
        trust = ProjectionQualityMetrics.trustworthiness(data, projected, k=1)
        cont = ProjectionQualityMetrics.continuity(data, projected, k=1)
        self.assertGreaterEqual(trust, 0.0)
        self.assertLessEqual(trust, 1.0)
        self.assertGreaterEqual(cont, 0.0)
        self.assertLessEqual(cont, 1.0)


if __name__ == "__main__":
    unittest.main()
