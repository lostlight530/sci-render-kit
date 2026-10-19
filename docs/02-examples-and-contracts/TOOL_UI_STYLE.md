# Three-Repository Evidence Console — UI Style & Interaction Contract

**Owner:** sci-render-kit communication/presentation plane, 2026-10-19
**Artifact:** [ui/tri_repo_console.html](../../ui/tri_repo_console.html)

## Purpose

Offline, local-first viewer for JSON receipts produced by each repository's tool_cli.py. It is a human review surface, not an execution engine, provider terminal, live GitHub dashboard, automatic scientific evaluator, or WCAG certification

## Design language

Visual direction: calm research operations console — dark navy workbench, restrained mint state highlights, high density with generous card padding, explicit state text. No gradient-as-evidence, no scores fabricated from source data

| Token | Hex | Use |
|---|---|---|
| bg | #09111d | page background |
| panel | #111e2d | evidence surfaces |
| panel2 | #162537 | local distinction |
| line | #293d51 | neutral boundaries |
| fg | #e8f0f6 | primary reading text |
| muted | #9db1c5 | descriptive metadata |
| accent | #62ddc1 | selected state/action |
| warn | #ffd18a | warnings (only with text) |
| danger | #ffa39c | failure (only with text) |

Typography: operating-system sans stack for body, monospaced pre for exact JSON; heading 30–47 px responsive, body 15 px. Layout: 235 px static sidebar at wide widths; single-column responsive mobile; summary cards wrap at 900 / 500 px

## Observable interaction

1. User selects or drags one local JSON file, limited to 2 MiB
2. Browser parses JSON locally using File.text; page issues no fetch or storage calls
3. Profile whitelist: three named repository prefixes with /tool-adapter (native Tool CLI and approval-first plan), /tool-execution, /agent-plan, /tool-catalog; never accept arbitrary prefix
4. Text nodes use textContent rather than HTML injection; no dynamic innerHTML with user JSON
5. Show repository, execution status, actual requested vs completed steps, per-step tool status and input digest; raw JSON can be expanded for review
6. Unknown and failure status remain textual and are not guessed from badge colors

## Accessibility and boundaries

- File chooser, focus-visible buttons, keyboard Enter/Space upload zone, semantic summary and live region
- No screenshots or color contrast tests in this PR demonstrate WCAG compliance
- Green success means a local tool returned a success envelope, NOT source truth, CI success or independent reproduction
- Importing a receipt is not executing its tool or approving a write
- Current repository/CI state is not fetched or represented; display is point-in-time evidence from the imported file
- The historical experimental core/observer_dashboard.py remains untouched and unintegrated; name similarity is not evidence of runtime support

## Next verification gate

Test visually with desktop/mobile viewport, keyboard-only navigation, screen reader if available, and malicious JSON containing angle brackets or script-looking strings. Review both pass and fail snapshots. Browser-based visual verification is **NOT_EXECUTED** unless a matching run report is attached to the change

## Canonical native adapter compatibility

The integrated Tool CLI emits `<repo>/tool-adapter` with `status: ok/error/approval_required`, `tool: agent_plan`, and nested `result.step_results` (or `result.proposed_steps` before approval). The console normalizes only these presentation fields, preserves the original JSON, and never treats `ok` as scientific verification. The earlier /tool-execution and /agent-plan records remain readable as dated alternate shapes; no implicit conversion of evidence authority is performed.
