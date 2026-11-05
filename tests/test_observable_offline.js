#!/usr/bin/env node
/* Offline packaging contract test: local-byte identity, not browser/JS library conformance. */
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const crypto = require('node:crypto');
const {execFileSync, spawnSync} = require('node:child_process');

const ROOT = path.resolve(__dirname, '..');
function hash(file) {
  return 'sha256:' + crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
}
function run(recipe, args = []) {
  return execFileSync(process.execPath, [
    'backends/observable_adapter.js', 'render', recipe, '--profile', 'presentation', ...args
  ], {cwd: ROOT, encoding: 'utf8', stdio: 'pipe'});
}
function makeRecipe(root, name) {
  const file = path.join(root, name + '.yaml');
  const outputDir = path.join(root, 'output');
  fs.writeFileSync(file, [
    'id: offline-test',
    'type: line-chart',
    'data:',
    '  series: [1, 2]',
    'aesthetics: {}',
    'output:',
    '  dir: ' + JSON.stringify(outputDir),
    '  filename: ' + name + '.html',
    '  format: html'
  ].join('\n') + '\n', 'utf8');
  return {file, outputDir};
}
const root = fs.mkdtempSync(path.join(os.tmpdir(), 'sci-render-offline-'));
try {
  const assets = path.join(root, 'assets');
  fs.mkdirSync(assets);
  const d3 = path.join(assets, 'd3.min.js');
  const plot = path.join(assets, 'plot.umd.min.js');
  // Deliberate dummy byte fixtures: no claim that actual Plot/D3 ran in a browser.
  fs.writeFileSync(d3, 'window.d3 = {};\n', 'utf8');
  fs.writeFileSync(plot, 'window.Plot = {};\n', 'utf8');

  const offline = makeRecipe(root, 'offline');
  run(offline.file, ['--offline-assets', assets]);
  const html = fs.readFileSync(path.join(offline.outputDir, 'offline.html'), 'utf8');
  assert.ok(html.includes('offline.d3.min.js'));
  assert.ok(html.includes('offline.plot.umd.min.js'));
  assert.ok(html.includes('const Plot = window.Plot'));
  assert.ok(!html.includes('cdn.jsdelivr.net'));
  const manifest = JSON.parse(fs.readFileSync(path.join(offline.outputDir, 'offline.manifest.json'), 'utf8'));
  assert.equal(manifest.offline_assets_copied, true);
  assert.equal(manifest.external_dependencies.length, 2);
  for (const dep of manifest.external_dependencies) {
    assert.equal(dep.required_at_view_time, false);
    assert.equal(dep.bundled_in_output, true);
    assert.equal(dep.version_verified, false);
    assert.equal(dep.version, null);
    assert.equal(dep.file_sha256, hash(path.join(offline.outputDir, dep.file)));
  }

  const originalHtml = html;
  fs.writeFileSync(plot, 'window.Plot = {changed: true};\n', 'utf8');
  const refused = spawnSync(process.execPath, [
    'backends/observable_adapter.js', 'render', offline.file,
    '--offline-assets', assets
  ], {cwd: ROOT, encoding: 'utf8'});
  assert.notEqual(refused.status, 0, 'conflicting bundle copy must fail');
  assert.ok(refused.stderr.includes('different bytes'));
  assert.equal(fs.readFileSync(path.join(offline.outputDir, 'offline.html'), 'utf8'), originalHtml);

  const online = makeRecipe(root, 'online');
  run(online.file);
  const onlineHtml = fs.readFileSync(path.join(online.outputDir, 'online.html'), 'utf8');
  assert.ok(onlineHtml.includes('cdn.jsdelivr.net'));
  const onlineManifest = JSON.parse(fs.readFileSync(path.join(online.outputDir, 'online.manifest.json'), 'utf8'));
  assert.equal(onlineManifest.offline_assets_copied, false);
  assert.equal(onlineManifest.external_dependencies[0].required_at_view_time, true);
  console.log(JSON.stringify({tests: ['offline', 'no-remote-import', 'byte-identities', 'conflicting-output-rejected', 'online-default'], passed: 5}));
} finally {
  fs.rmSync(root, {recursive: true, force: true});
}
