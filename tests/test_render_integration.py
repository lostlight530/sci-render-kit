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



    def test_figure_evidence_writer_preserves_legacy_stage_symlink_target(self):
        from core.figure_evidence import write_figure_evidence

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            protected = root / "protected.txt"
            protected.write_text("PRESERVE", encoding="utf-8")
            figure = root / "figure.png"
            output = figure.with_suffix(".evidence.json")
            old_stage = output.with_suffix(".evidence.json.tmp")
            try:
                old_stage.symlink_to(protected)
            except (OSError, NotImplementedError) as exc:
                self.skipTest(f"symbolic links unavailable: {exc}")

            actual = write_figure_evidence({"figure_id": "f1"}, figure)
            self.assertEqual(actual, output)
            self.assertEqual(protected.read_text(encoding="utf-8"), "PRESERVE")
            self.assertTrue(old_stage.is_symlink())
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8"))["figure_id"], "f1"
            )



class MatplotlibTemporaryFileSafety(unittest.TestCase):
    def test_backend_preserves_preexisting_generated_script(self):
        from backends import matplotlib_base

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            output_dir = root / "output"
            output_dir.mkdir()
            reserved_script = output_dir / "_generated_render.py"
            reserved_script.write_text("PRESERVE\n", encoding="utf-8")
            recipe_path = root / "recipe.yaml"
            recipe_path.write_text(
                yaml.safe_dump({
                    "type": "line-chart",
                    "data": {"series": [1, 2]},
                    "aesthetics": {},
                    "output": {
                        "dir": str(output_dir),
                        "filename": "figure.png",
                        "format": "png",
                    },
                }),
                encoding="utf-8",
            )
            executed_scripts = []

            def fake_run(command, check):
                executed_scripts.append(Path(command[1]))
                (output_dir / "figure.png").write_bytes(b"figure")

            with (
                patch.object(matplotlib_base, "load_profile", return_value={"name": "nature"}),
                patch.object(matplotlib_base, "build_provenance", return_value={}),
                patch.object(matplotlib_base, "generate_python_code", return_value="# generated\n"),
                patch.object(matplotlib_base.subprocess, "run", side_effect=fake_run),
                patch.object(matplotlib_base, "write_provenance_sidecar"),
                patch.object(matplotlib_base, "write_manifest"),
            ):
                matplotlib_base.render(str(recipe_path))

            self.assertEqual(reserved_script.read_text(encoding="utf-8"), "PRESERVE\n")
            self.assertEqual(len(executed_scripts), 1)
            self.assertNotEqual(executed_scripts[0], reserved_script)
            self.assertFalse(executed_scripts[0].exists())
            self.assertEqual(list(output_dir.glob(".sci-render-*.py")), [])

    def test_accessibility_adapter_preserves_legacy_manifest_temp_symlink(self):
        from backends import matplotlib_adapter

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            output_dir = root / "output"
            output_dir.mkdir()
            figure = output_dir / "figure.png"
            manifest = figure.with_suffix(".manifest.json")
            manifest.write_text(
                json.dumps({"profile": "sci-render-kit/render-manifest", "provenance": {}}),
                encoding="utf-8",
            )
            protected = root / "protected.txt"
            protected.write_text("PRESERVE", encoding="utf-8")
            legacy_temp = manifest.with_suffix(".manifest.json.tmp")
            try:
                legacy_temp.symlink_to(protected)
            except (OSError, NotImplementedError) as exc:
                self.skipTest(f"symbolic links unavailable: {exc}")

            recipe = {
                "output": {"dir": str(output_dir), "filename": figure.name},
                "accessibility": {"alt_text": "A line chart."},
            }

            def emit_manifest(*args, **kwargs):
                manifest.write_text(
                    json.dumps({"profile": "sci-render-kit/render-manifest", "provenance": {}}),
                    encoding="utf-8",
                )

            with (
                patch.object(matplotlib_adapter.base, "load_recipe", return_value=recipe),
                patch.object(matplotlib_adapter.base, "render", side_effect=emit_manifest),
            ):
                matplotlib_adapter.render("unused-recipe.yaml")

            self.assertEqual(protected.read_text(encoding="utf-8"), "PRESERVE")
            self.assertTrue(legacy_temp.is_symlink())
            updated = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(updated["accessibility"]["profile"], "sci-render-kit/a11y")


if __name__ == "__main__":
    unittest.main()
