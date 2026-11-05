"""Real Matplotlib render, using isolated temporary outputs.

This tests final sidecar byte consistency, not publication acceptance,
pixel parity, WCAG conformance, scientific truth, or independent reproduction.
"""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


class RenderIntegration(unittest.TestCase):
    def test_real_matplotlib_output_and_terminal_sidecar_identity(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            recipe = yaml.safe_load(
                (ROOT / "recipes/accessible-line-chart.yaml").read_text(encoding="utf-8")
            )
            # The source demo is 10pt, while the Nature target caps at 7pt.
            # Keep strict P1 policy intact and make this fixture profile-valid.
            recipe["aesthetics"]["font_size"] = 7
            recipe["output"]["dir"] = str(root)
            recipe_file = root / "render.yaml"
            recipe_file.write_text(
                yaml.safe_dump(recipe, allow_unicode=True), encoding="utf-8"
            )
            completed = subprocess.run(
                [
                    sys.executable, "sci_render.py", str(recipe_file),
                    "--backend", "matplotlib", "--profile", "nature",
                ],
                cwd=ROOT, text=True, capture_output=True, timeout=90,
                check=False,
            )
            self.assertEqual(
                completed.returncode, 0,
                f"render stdout:\n{completed.stdout}\nrender stderr:\n{completed.stderr}",
            )
            figure = root / "accessible-line-chart.png"
            manifest_file = figure.with_suffix(".manifest.json")
            evidence_file = figure.with_suffix(".evidence.json")
            for file in (figure, manifest_file, evidence_file):
                self.assertTrue(file.is_file(), str(file))
            manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
            evidence = json.loads(evidence_file.read_text(encoding="utf-8"))
            self.assertEqual(manifest["figure_evidence"]["sidecar"], evidence_file.name)
            self.assertEqual(manifest["accessibility"]["profile"], "sci-render-kit/a11y")
            self.assertEqual(evidence["figure"]["file_sha256"], digest(figure))
            ref = next(
                x for x in evidence["artifacts"]
                if x["kind"] == "render-manifest"
            )
            self.assertEqual(ref["file_sha256"], digest(manifest_file))
            self.assertFalse(evidence["scientific_validity_claim"])
            print(json.dumps({
                "scenario": "matplotlib-terminal-manifest-identity",
                "result": "PASS", "exit_code": completed.returncode,
                "figure_sha256": digest(figure),
                "manifest_sha256": digest(manifest_file),
                "evidence_sha256": digest(evidence_file),
                "scientific_validity_claim": False,
            }, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
