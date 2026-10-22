#!/usr/bin/env python3
"""Contract tests for the opt-in, allowlisted local Tool/CLI/Agent surface."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agent_tools import PROFILE, list_tool_names, tool_definitions, execute_tool_call
from tool_cli import _html_report, _human


ROOT = Path(__file__).resolve().parents[1]


class TestToolContract(unittest.TestCase):
    def test_registry_declarations_are_allowlisted(self):
        declarations = tool_definitions()
        names = [item["function"]["name"] for item in declarations]
        self.assertEqual(sorted(names), list_tool_names())
        self.assertEqual(len(names), 2)
        for item in declarations:
            schema = item["function"]["parameters"]
            self.assertEqual(item["type"], "function")
            self.assertFalse(schema["additionalProperties"])

    def test_unknown_and_invalid_arguments_fail_closed(self):
        unknown = execute_tool_call("arbitrary_python", {})
        self.assertEqual(unknown["error"]["code"], "UNKNOWN_TOOL")
        self.assertFalse(unknown["remote_provider_called"])
        self.assertFalse(unknown["scientific_validity_claim"])
        name = list_tool_names()[0]
        malformed = execute_tool_call(name, "{broken")
        self.assertEqual(malformed["error"]["code"], "INVALID_ARGUMENT")
        hidden = execute_tool_call(name, {"unsafe_cmd": "rm -rf /"})
        self.assertEqual(hidden["error"]["code"], "INVALID_ARGUMENT")

    def test_cli_registry_machine_json_and_offline_html(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tool_cli.py"), "list"],
            text=True, capture_output=True, check=True, cwd=ROOT,
        )
        parsed = json.loads(proc.stdout)
        self.assertEqual(parsed["profile"], PROFILE)
        self.assertEqual(len(parsed["result"]["tools"]), 2)
        self.assertNotIn("\x1b", proc.stdout)
        self.assertEqual(proc.stderr, "")
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "report.html"
            proc = subprocess.run(
                [sys.executable, str(ROOT / "tool_cli.py"), "list",
                 "--format", "html", "--output", str(path)],
                text=True, capture_output=True, check=True, cwd=ROOT,
            )
            self.assertEqual(proc.stdout, "")
            report = path.read_text(encoding="utf-8")
            self.assertIn("<!doctype html>", report)
            self.assertIn("@media(prefers-color-scheme:dark)", report)
            self.assertNotIn("<script", report)
            malicious = _html_report({"profile": PROFILE, "tool": "<script>alert(1)</script>",
                                      "status": "error", "result": None, "error": None})
            self.assertNotIn("<script>alert(1)</script>", malicious)
            self.assertIn("&lt;script&gt;", malicious)
            self.assertNotIn("\x1b", _human(parsed, color=False))

    def test_cli_invalid_arguments_machine_failure(self):
        name = list_tool_names()[0]
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tool_cli.py"), "invoke", name,
             "--args", '{"unexpected":true}'],
            text=True, capture_output=True, cwd=ROOT,
        )
        self.assertEqual(proc.returncode, 1)
        parsed = json.loads(proc.stdout)
        self.assertEqual(parsed["error"]["code"], "INVALID_ARGUMENT")


class TestRepoIntegration(unittest.TestCase):
    def test_real_recipe_audit_remains_nonrendering(self):
        value = execute_tool_call("figure_audit",
            {"recipe": str(ROOT / "recipes" / "accessible-line-chart.yaml"),
             "profile": "nature"})
        self.assertEqual(value["status"], "ok", value.get("error"))
        self.assertFalse(value["result"]["render_performed"])
        self.assertFalse(value["result"]["scientific_validity_claim"])
        self.assertIn(value["result"]["check_status"], {"observed", "failed"})

    def test_invalid_recipe_schema_is_structured_cli_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            invalid_recipe = Path(folder) / "invalid.yaml"
            invalid_recipe.write_text(
                "id: deliberately-missing-required-fields\n", encoding="utf-8"
            )
            args = {"recipe": str(invalid_recipe), "profile": "nature"}
            receipt = execute_tool_call("figure_audit", args)
            self.assertEqual(receipt["status"], "error", receipt)
            self.assertEqual(receipt["error"]["code"], "EXECUTION_FAILED")
            self.assertIn("schema validation failed", receipt["error"]["message"])
            proc = subprocess.run(
                [sys.executable, str(ROOT / "tool_cli.py"), "invoke",
                 "figure_audit", "--args", json.dumps(args)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(proc.returncode, 1, proc.stdout)
            self.assertFalse(proc.stderr, proc.stderr)
            cli_receipt = json.loads(proc.stdout)
            self.assertEqual(cli_receipt["status"], "error")
            self.assertEqual(cli_receipt["error"]["code"], "EXECUTION_FAILED")

    def test_transfer_rejects_nonobject_context_with_structured_failure(self):
        fields = (
            "claim_communication", "upstream_research", "uncertainty",
            "process_disclosure", "communication_audit", "runtime_validation",
            "reproducibility",
        )
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "malformed.evidence.json"
            for field in fields:
                for invalid in ([], ["unexpected"], "not-an-object", 7, False):
                    with self.subTest(field=field, invalid=invalid):
                        path.write_text(json.dumps({
                            "profile": "sci-render-kit/figure-evidence",
                            field: invalid,
                        }), encoding="utf-8")
                        response = execute_tool_call(
                            "communication_transfer", {"figure_evidence": str(path)}
                        )
                        self.assertEqual(response["status"], "error", response)
                        self.assertEqual(response["error"]["code"], "EXECUTION_FAILED")
                        self.assertIn(field, response["error"]["message"])
                        self.assertFalse(response["scientific_validity_claim"])

            path.write_text(json.dumps({
                "profile": "sci-render-kit/figure-evidence",
                "upstream_research": ["unexpected"],
            }), encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(ROOT / "tool_cli.py"), "invoke",
                 "communication_transfer", "--args",
                 json.dumps({"figure_evidence": str(path)})],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(proc.returncode, 1, proc.stdout)
            self.assertEqual(proc.stderr, "")
            receipt = json.loads(proc.stdout)
            self.assertEqual(receipt["error"]["code"], "EXECUTION_FAILED")
            self.assertIn("upstream_research", receipt["error"]["message"])

    def test_transfer_accepts_valid_and_nullable_optional_context(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "valid.evidence.json"
            path.write_text(json.dumps({
                "profile": "sci-render-kit/figure-evidence",
                "claim_communication": {"claim_refs": ["claim-1"], "bindings": []},
                "upstream_research": {"claim_audit": {"ref": "local-audit"}},
                "uncertainty": None,
                "process_disclosure": {},
                "communication_audit": {},
                "runtime_validation": {},
                "reproducibility": {"level": "R1"},
            }), encoding="utf-8")
            response = execute_tool_call(
                "communication_transfer", {"figure_evidence": str(path)}
            )
            self.assertEqual(response["status"], "ok", response)
            record = response["result"]
            self.assertEqual(record["claim_communication"]["claim_refs"], ["claim-1"])
            self.assertEqual(record["upstream_research"]["claim_audit"]["ref"], "local-audit")
            self.assertTrue(record["transfer_coverage"]["reproducibility_context_present"])
            self.assertFalse(record["transfer_constraints"]["scientific_validity_inherited"])
            self.assertFalse(record["independent_reproduction_claim"])

    def test_transfer_wrong_source_and_bad_profile(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "wrong.json"
            path.write_text('{"profile":"wrong"}', encoding="utf-8")
            value = execute_tool_call("communication_transfer",
                                      {"figure_evidence": str(path)})
            self.assertEqual(value["status"], "error")
        invalid = execute_tool_call("figure_audit",
            {"recipe": str(ROOT / "recipes" / "accessible-line-chart.yaml"),
             "profile": "../invalid"})
        self.assertEqual(invalid["error"]["code"], "EXECUTION_FAILED")


if __name__ == "__main__":
    unittest.main()
