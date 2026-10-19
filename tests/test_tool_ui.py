#!/usr/bin/env python3
"""Static offline UI contract checks (not visual/browser accessibility certification)."""
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "ui/tri_repo_console.html"


class Elements(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.viewport = False
        self.external_scripts = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if "id" in data:
            self.ids.append(data["id"])
        if tag == "meta" and data.get("name") == "viewport":
            self.viewport = True
        if tag == "script" and data.get("src"):
            self.external_scripts.append(data["src"])


class TestOfflineUI(unittest.TestCase):
    def test_static_document_and_upload_semantics(self):
        content = UI.read_text(encoding="utf-8")
        parser = Elements()
        parser.feed(content)
        self.assertTrue(parser.viewport)
        self.assertFalse(parser.external_scripts)
        self.assertEqual(len(parser.ids), len(set(parser.ids)))
        for element in ("drop", "file", "repo", "status", "count", "steps", "raw"):
            self.assertIn(element, parser.ids)
        self.assertIn("textContent", content)
        self.assertNotIn(".innerHTML", content)
        self.assertNotIn("fetch(", content)
        self.assertIn("focus-visible", content)
        self.assertIn("tool-adapter", content)
        self.assertIn("step_results", content)
        self.assertIn("approval_required", content)
        self.assertIn("item.function?.name", content)

    def test_inline_javascript_parses_when_node_available(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node.js not installed; UI JS parse check optional")
        source = UI.read_text(encoding="utf-8").split("<script>", 1)[1].split("</script>", 1)[0]
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "console.js"
            path.write_text(source, encoding="utf-8")
            result = subprocess.run([node, "--check", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)


    def test_failed_import_clears_prior_receipt(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node.js not installed; UI state check optional")
        harness = r'''
const fs = require("node:fs");
const vm = require("node:vm");
const html = fs.readFileSync(process.argv[1], "utf8");
const script = html.split("<script>", 2)[1].split("</script>", 1)[0];
const elements = new Map();
function element(id) {
  if (!elements.has(id)) elements.set(id, {
    textContent: "", addEventListener() {}, click() {},
    classList: {add() {}, remove() {}},
  });
  return elements.get(id);
}
const context = {document: {getElementById: element}};
vm.createContext(context);
vm.runInContext(script, context);
for (const id of ["repo", "source", "origin", "raw"]) {
  element(id).textContent = "stale-" + id;
}
vm.runInContext('showError("invalid JSON")', context);
const expected = {
  repo: "未加载", status: "读取失败", steps: "invalid JSON", count: "—",
  source: "尚未读取 JSON", origin: "本地文件", raw: "没有导入记录",
};
for (const [id, value] of Object.entries(expected)) {
  if (element(id).textContent !== value) {
    process.stderr.write(id + " retains " + JSON.stringify(element(id).textContent) + "\n");
    process.exitCode = 1;
  }
}
'''
        result = subprocess.run(
            [node, "-e", harness, str(UI)], capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
