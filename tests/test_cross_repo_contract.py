"""Consumer-oriented figure evidence contract with ephemeral upstream fixtures."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import yaml

from core.figure_evidence import build_figure_evidence, write_figure_evidence
from core.communication_transfer import build_communication_transfer

ROOT = Path(__file__).resolve().parents[1]


class CrossRepositoryContract(unittest.TestCase):
    def test_figure_handoff_retains_declared_upstream_evidence_and_claims(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            upstream = {}
            for name, profile in (
                ("envelope", "epistemic-pipeline/evidence-envelope"),
                ("claim", "epistemic-pipeline/claim-verification"),
                ("artifact", "auto-doc-engine/artifact-record"),
            ):
                p = root / (name + ".json")
                p.write_text(json.dumps({"profile": profile}), encoding="utf-8")
                upstream[name] = p
            figure = root / "figure.png"
            figure.write_bytes(b"bounded fixture figure bytes")
            recipe_file = root / "recipe.yaml"
            profile_file = root / "profile.yaml"
            recipe_file.write_text("id: fixture\n", encoding="utf-8")
            profile_file.write_text("name: fixture\n", encoding="utf-8")
            recipe = {
                "id": "fixture", "type": "line-chart",
                "data": {"series": [1, 2]},
                "research_context": {
                    "artifact_id": "upstream-artifact",
                    "evidence_envelope_ref": str(upstream["envelope"]),
                    "claim_audit_ref": str(upstream["claim"]),
                    "data_artifact_ref": str(upstream["artifact"]),
                    "claim_refs": ["c1"],
                    "claim_bindings": [{
                        "visual_ref": "series:series", "claim_refs": ["c1"],
                        "relation": "illustrates",
                    }],
                },
                "uncertainty": {
                    "kind": "heuristic-bound",
                    "semantics": "Project-bounded fixture, not statistical confidence",
                },
            }
            record = build_figure_evidence(
                recipe_path=str(recipe_file), recipe=recipe,
                profile_path=str(profile_file), profile={"name": "fixture"},
                backend="matplotlib", output_path=figure, findings=[],
            )
            self.assertEqual(record["profile"], "sci-render-kit/figure-evidence")
            self.assertEqual(record["claim_communication"]["claim_refs"], ["c1"])
            self.assertFalse(record["claim_communication"]["inferred_bindings"])
            for field, fixture in (
                ("evidence_envelope", upstream["envelope"]),
                ("claim_audit", upstream["claim"]),
                ("data_artifact", upstream["artifact"]),
            ):
                self.assertEqual(
                    record["upstream_research"][field]["file_sha256"],
                    "sha256:" + hashlib.sha256(fixture.read_bytes()).hexdigest(),
                )
            self.assertFalse(record["upstream_research"]["scientific_validity_inherited"])
            self.assertFalse(record["scientific_validity_claim"])
            self.assertEqual(record["reproducibility"]["level"], "R1")

            evidence_path = write_figure_evidence(record, figure)
            handoff = build_communication_transfer(evidence_path)
            self.assertEqual(handoff["profile"], "sci-render-kit/communication-transfer")
            self.assertEqual(handoff["claim_communication"]["claim_refs"], ["c1"])
            self.assertEqual(handoff["uncertainty"]["kind"], "heuristic-bound")
            self.assertFalse(handoff["transfer_constraints"]["scientific_validity_inherited"])
            self.assertFalse(handoff["transfer_constraints"]["independent_reproduction_inherited"])

    def test_codemeta_v4_citation_identity_stays_consistent(self):
        meta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))
        cff = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
        self.assertEqual(meta["@context"], "https://w3id.org/codemeta/4.0")
        self.assertEqual(meta["codeRepository"], cff["repository-code"])
        self.assertEqual(meta["identifier"], "https://doi.org/" + cff["identifiers"][0]["value"])
        self.assertNotIn("relatedSoftware", meta)


if __name__ == "__main__":
    unittest.main()
