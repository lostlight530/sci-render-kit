#!/usr/bin/env python3
"""Provider-neutral, allowlisted, synchronous tool adapter.

Explicitly *not* an MCP server, arbitrary code executor, autonomous planner,
external LLM client, or scientific validation authority. No automatic writes.
"""
from __future__ import annotations

import json
from typing import Any

PROFILE = "sci-render-kit/tool-adapter"
_SPECS = [
  {
    "name": "figure_audit",
    "description": "Validate a local figure recipe and run pre-render and communication checks without rendering a figure.",
    "parameters": {
      "type": "object",
      "properties": {
        "recipe": {
          "type": "string",
          "description": "Recipe YAML file"
        },
        "profile": {
          "type": "string",
          "description": "Installed publisher preset name, default nature"
        }
      },
      "required": [
        "recipe"
      ],
      "additionalProperties": False
    }
  },
  {
    "name": "communication_transfer",
    "description": "Construct a bounded figure-evidence communication handoff in memory; does not assert publication or scientific truth.",
    "parameters": {
      "type": "object",
      "properties": {
        "figure_evidence": {
          "type": "string",
          "description": "Existing sci-render-kit/figure-evidence JSON sidecar"
        },
        "destination": {
          "type": "string",
          "description": "Caller-declared target"
        },
        "purpose": {
          "type": "string",
          "description": "Caller-declared purpose"
        }
      },
      "required": [
        "figure_evidence"
      ],
      "additionalProperties": False
    }
  }
]


TOOL_SPECS = {item["name"]: item for item in _SPECS}


def tool_definitions() -> list[dict]:
    """JSON-Schema function declarations usable by a caller-managed Agent."""
    return [{"type": "function", "function": {
        "name": spec["name"], "description": spec["description"],
        "parameters": spec["parameters"],
    }} for spec in _SPECS]


def _check_arguments(name: str, arguments: Any) -> dict:
    if not isinstance(arguments, dict):
        raise ValueError("arguments must be a JSON object")
    schema = TOOL_SPECS[name]["parameters"]
    properties = schema["properties"]
    unknown = set(arguments) - set(properties)
    if unknown:
        raise ValueError("unexpected argument(s): " + ", ".join(sorted(unknown)))
    missing = set(schema.get("required", [])) - set(arguments)
    if missing:
        raise ValueError("missing argument(s): " + ", ".join(sorted(missing)))
    for key, value in arguments.items():
        typ = properties[key]["type"]
        if typ == "string" and (not isinstance(value, str) or not value.strip()):
            raise ValueError(key + " must be a nonempty string")
        if typ == "boolean" and not isinstance(value, bool):
            raise ValueError(key + " must be a boolean")
        if typ == "array" and not isinstance(value, list):
            raise ValueError(key + " must be an array")
    return arguments


def _dispatch(name: str, a: dict) -> Any:
    if name == "figure_audit":
        from pathlib import Path
        from jsonschema import validate
        from sci_render import load_yaml, evaluate_pre_render_rules, has_errors
        from core.claim_binding_audit import audit_claim_communication
        root = Path(__file__).resolve().parent
        preset = a.get("profile", "nature")
        if "/" in preset or "\\" in preset or preset in {".", ".."}:
            raise ValueError("profile must be an installed preset name")
        recipe = load_yaml(a["recipe"])
        schema = load_yaml(str(root / "metadata" / "recipe.schema.yaml"))
        validate(instance=recipe, schema=schema)
        profile = load_yaml(str(root / "profiles" / (preset + ".yaml")))
        rules = load_yaml(str(root / "quality" / "rules.yaml"))
        visual = evaluate_pre_render_rules(recipe, profile, rules)
        communication = audit_claim_communication(recipe)
        combined = visual + communication
        return {"recipe_id": recipe.get("id"), "profile_target": preset,
                "check_status": "failed" if has_errors(combined) else "observed",
                "visual_findings": visual, "communication_findings": communication,
                "render_performed": False, "scientific_validity_claim": False}
    if name == "communication_transfer":
        from core.communication_transfer import build_communication_transfer
        return build_communication_transfer(a["figure_evidence"],
                                            destination=a.get("destination"),
                                            purpose=a.get("purpose"))
    raise ValueError("unknown tool")


def execute_tool_call(name: str, arguments: dict | str) -> dict:
    """Dispatch an allowlisted call and return a stable JSON-serializable envelope.

    String arguments are accepted for model function-call interoperability.
    Domain findings live inside result; status=ok never means scientific truth.
    """
    envelope = {
        "profile": PROFILE, "tool": name, "status": "error",
        "result": None, "error": None,
        "scientific_validity_claim": False,
        "remote_provider_called": False,
    }
    if name not in TOOL_SPECS:
        envelope["error"] = {"code": "UNKNOWN_TOOL", "message": "tool is not allowlisted"}
        return envelope
    try:
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError as exc:
                raise ValueError("arguments are not valid JSON") from exc
        checked = _check_arguments(name, arguments)
    except (ValueError, TypeError) as exc:
        envelope["error"] = {"code": "INVALID_ARGUMENT", "message": str(exc)}
        return envelope
    try:
        envelope["result"] = _dispatch(name, checked)
        envelope["status"] = "ok"
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        envelope["error"] = {"code": "EXECUTION_FAILED", "message": str(exc)}
    return envelope


def list_tool_names() -> list[str]:
    return sorted(TOOL_SPECS)
