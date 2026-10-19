# Scientific figure Tool / CLI / Agent console

> Current implementation surface · 2026-10-19 · `sci-render-kit/tool-adapter`

## Where this sits

```text
caller / human / independent agent
    ├─ import agent_tools.tool_definitions() → JSON Schema declarations
    ├─ import agent_tools.execute_tool_call(name, arguments)
    └─ tool_cli.py (JSON / styled terminal / offline HTML)
                    ↓
          explicit allowlist dispatch
                    ↓
             existing core modules
                    ↓
        typed result + explicit error/domain finding
```

This is an **opt-in, local, synchronous** tool adapter. The caller orchestrates model decisions, approvals and persistence. No background agent, scheduler, online gateway, MCP server, remote model SDK, external provider authentication, unrestricted shell or automatic repository edits are introduced.

## Registered tools

`figure_audit` loads a local recipe and installed publisher preset, enforces the current JSON Schema, runs P1 visual and claim-communication findings, and explicitly does *not* render. `communication_transfer` delegates to `core.communication_transfer.build_communication_transfer` from an existing figure-evidence sidecar; it makes no acceptance or reproduction claim.

Tool names, required arguments and JSON Schema are inspected with `list` and `describe`. The registry rejects unknown tool names, unexpected argument keys, wrong value types and malformed JSON before calling implementation. Runtime paths are caller-supplied and are *not* sandboxed; execute only with appropriate filesystem permissions and inspect untrusted inputs independently.

## CLI: immediate practical use

From this repository root with its existing Python dependencies installed:

```bash
python3 tool_cli.py list --format text
python3 tool_cli.py describe figure_audit
python3 tool_cli.py invoke figure_audit --args '{"recipe":"recipes/accessible-line-chart.yaml","profile":"nature"}' --format text
python3 tool_cli.py invoke communication_transfer --args '{"figure_evidence":"output/accessible-line-chart.evidence.json","destination":"local review","purpose":"handoff"}'
```

**JSON-first automation** (single JSON object on stdout, no ANSI escape sequences):

```bash
python3 tool_cli.py list
python3 tool_cli.py invoke figure_audit --args-file request.json > result.json
cat request.json | python3 tool_cli.py invoke figure_audit --args-file - > result.json
```

To generate a **standalone offline UI report**:

```bash
python3 tool_cli.py invoke figure_audit --args '{"recipe":"recipes/accessible-line-chart.yaml","profile":"nature"}' --format html --output output/tool-inspection.html
```

Open the resulting HTML file locally. It is a static report; it does not fetch content, execute JavaScript, host a server or provide live agent control.

## Programmatic Agent binding (no vendor SDK needed)

```python
import json
from agent_tools import tool_definitions, execute_tool_call

definitions = tool_definitions()  # agent/model-side function declarations
assert len(definitions) == 2

# The caller chooses an allowlisted function and supplies validated arguments.
name = "figure_audit"
arguments = { "recipe": "recipes/accessible-line-chart.yaml" }
result = execute_tool_call(name, arguments)
assert result["tool"] == name
print(json.dumps(result, ensure_ascii=False))
```

Stringified JSON arguments are also supported for provider-neutral function-call transport, but there is no built-in provider loop, approval policy, retry orchestration or MCP protocol conformance.

## Stable result contract

```json
{
  "profile": "sci-render-kit/tool-adapter",
  "tool": "an-allowlisted-tool",
  "status": "ok",
  "result": {},
  "error": null,
  "scientific_validity_claim": false,
  "remote_provider_called": false
}
```

The execution status reports whether **tool invocation succeeded**, not whether domain findings passed. For CLI automation, exit 0 means invocation and domain checks passed; exit 1 means an invocation or domain check failed; exit 2 means writing the requested output report failed. Error responses include `error.code` such as `UNKNOWN_TOOL`, `INVALID_ARGUMENT` or `EXECUTION_FAILED`. Failures are valid evidence and must not be rewritten into successes.

`figure_audit` is a pre-render inspect-only tool and is **not** a wrapper claiming `sci_render.py` end-to-end rendering. For actual generated PNG/SVG/PDF evidence, use the repository-owned `python3 sci_render.py ...` CLI with the existing backend contracts. A `check_status:failed` result means project predicates failed, not scientific falsehood. Accessible cue contracts do not constitute WCAG certification.

## UI style and accessibility scope

The console shares a single visual language across all three repositories:

| Surface | Design | Reliability boundary |
|---|---|---|
| `--format json` | stable key structure, machine-readable, no decorative output | truth comes only from `status` and domain findings |
| `--format text` | compact cyan console frame, explicit EXECUTED / CHECK FAILED headings | ANSI only for interactive TTY, removable with `--no-color` or `NO_COLOR` |
| `--format html` | navy/teal editorial style, responsive cards, system typography, auto light/dark mode, readable monospace blocks | local static HTML with escaped user data and **no scripts** |

Color is never the only status indicator. A result can be `EXECUTED` while its research/diagnostic meaning stays bounded; a human should still review the original evidence and source.

## Test and operational verification

```bash
python3 -m unittest tests.test_tool_cli -v
python3 tool_cli.py list
python3 tool_cli.py list --format html --output output/tool-catalog.html
```

These are executable instructions, **not a claim that any runner, GitHub Actions, security review or independent reproduction passed**. The adapter is optional and deliberately does not alter the canonical scientific/runtime paths.

For the three-repository chain, produce upstream artifact/claim/figure sidecars with each repository's native runtime first; then use these explicit read/transfer tools for portable handoffs. There are no hidden direct cross-repository imports, shared secrets, or automatic promotion of source evidence into scientific truth.
