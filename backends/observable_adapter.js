#!/usr/bin/env node
/**
 * Observable Plot backend for interactive HTML figures.
 *
 * The generated HTML pins @observablehq/plot 0.6.17 through the documented
 * jsDelivr ESM bundle. The artifact therefore has a declared runtime network
 * dependency unless the dependency is separately vendored; manifest evidence
 * is R1 replay-addressable, not an offline-reproduction claim.
 */

const fs = require('fs');
const path = require('path');
const yaml = require('yaml');
const crypto = require('crypto');

const PLOT_VERSION = '0.6.17';
const PLOT_ESM_URL = `https://cdn.jsdelivr.net/npm/@observablehq/plot@${PLOT_VERSION}/+esm`;
const MANIFEST_PROFILE = 'sci-render-kit/render-manifest@2';

function loadYaml(filePath) {
  const value = yaml.parse(fs.readFileSync(filePath, 'utf-8'));
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    throw new Error(`YAML root must be a mapping: ${filePath}`);
  }
  return value;
}

function loadRecipe(recipePath) {
  return loadYaml(recipePath);
}

function loadProfile(name) {
  const profilePath = path.join('profiles', `${name}.yaml`);
  if (!fs.existsSync(profilePath)) return {};
  return loadYaml(profilePath);
}

function stableNormalize(value) {
  if (Array.isArray(value)) return value.map(stableNormalize);
  if (value && typeof value === 'object') {
    return Object.fromEntries(
      Object.keys(value).sort().map((key) => [key, stableNormalize(value[key])])
    );
  }
  return value;
}

function canonicalSha256(value) {
  const text = JSON.stringify(stableNormalize(value));
  return 'sha256:' + crypto.createHash('sha256').update(text, 'utf8').digest('hex');
}

function fileSha256(filePath) {
  if (!filePath || !fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) return null;
  return 'sha256:' + crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
}

function validateRecipe(recipe) {
  const errors = [];
  for (const key of ['type', 'data', 'aesthetics', 'output']) {
    if (!(key in recipe)) errors.push(`missing required field: ${key}`);
  }
  return errors;
}

function semanticPalette(labels) {
  const semanticMap = {
    positive: '#009E73', negative: '#D55E00', neutral: '#56B4E9',
    critical: '#D55E00', stable: '#0072B2', energetic: '#E69F00',
    creative: '#CC79A7', attention: '#F0E442'
  };
  const fallback = ['#0072B2', '#E69F00', '#009E73', '#CC79A7', '#56B4E9', '#F0E442', '#D55E00', '#000000'];
  return labels.map((label, index) => semanticMap[String(label).toLowerCase()] || fallback[index % fallback.length]);
}

function generateHTML(recipe, profile) {
  const aesthetics = { ...(profile.aesthetics || {}), ...(recipe.aesthetics || {}) };
  const data = recipe.data || {};
  const chartType = recipe.type;
  const access = recipe.accessibility || {};
  const labels = Object.keys(data);
  let palette = aesthetics.palette || ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#000000'];
  if (aesthetics.semantic_palette && ['line-chart', 'bar-chart', 'scatter-plot', 'boxplot', 'histogram'].includes(chartType)) {
    palette = semanticPalette(labels);
  }

  const plotOptions = `
    width: ${Math.max(1, Math.round((aesthetics.figsize?.[0] || 6) * 96))},
    height: ${Math.max(1, Math.round((aesthetics.figsize?.[1] || 4) * 96))},
    x: {label: ${JSON.stringify(aesthetics.x_label || null)}},
    y: {label: ${JSON.stringify(aesthetics.y_label || null)}},
    style: {fontFamily: ${JSON.stringify(aesthetics.font || 'sans-serif')}, fontSize: ${JSON.stringify(`${aesthetics.font_size || 12}px`)}}
  `;

  let plotCode = '';
  if (chartType === 'line-chart') {
    const mapped = Object.entries(data).flatMap(([label, values]) =>
      values.map((y, x) => ({x, y, series: label}))
    );
    plotCode = `
const data = ${JSON.stringify(mapped)};
const plot = Plot.plot({
  ${plotOptions},
  marks: [
    Plot.lineY(data, {x: "x", y: "y", stroke: "series", strokeWidth: 2}),
    Plot.dot(data, {x: "x", y: "y", stroke: "series", fill: "series", r: 4})
  ],
  color: {domain: ${JSON.stringify(labels)}, range: ${JSON.stringify(palette.slice(0, labels.length))}}
});`;
  } else if (chartType === 'scatter-plot') {
    const mapped = [];
    for (const [label, pair] of Object.entries(data)) {
      if (!Array.isArray(pair) || pair.length !== 2) throw new Error(`scatter series ${label} must be [x_values, y_values]`);
      const [x, y] = pair;
      for (let index = 0; index < x.length; index += 1) mapped.push({x: x[index], y: y[index], series: label});
    }
    plotCode = `
const data = ${JSON.stringify(mapped)};
const plot = Plot.plot({
  ${plotOptions},
  marks: [Plot.dot(data, {x: "x", y: "y", stroke: "series", fill: "series", r: 5, strokeWidth: 1})],
  color: {domain: ${JSON.stringify(labels)}, range: ${JSON.stringify(palette.slice(0, labels.length))}}
});`;
  } else if (chartType === 'bar-chart') {
    const mapped = Object.entries(data).map(([category, value]) => ({category, value}));
    plotCode = `
const data = ${JSON.stringify(mapped)};
const plot = Plot.plot({
  ${plotOptions},
  marks: [Plot.barY(data, {x: "category", y: "value", fill: "category"})],
  color: {domain: ${JSON.stringify(labels)}, range: ${JSON.stringify(palette.slice(0, labels.length))}}
});`;
  } else if (chartType === 'heatmap') {
    const matrix = data.matrix || [];
    if (!matrix.length || !Array.isArray(matrix[0])) throw new Error('heatmap matrix must be non-empty');
    const rowLabels = data.row_labels || Array.from({length: matrix.length}, (_, i) => `R${i + 1}`);
    const colLabels = data.col_labels || Array.from({length: matrix[0].length}, (_, i) => `C${i + 1}`);
    const mapped = [];
    matrix.forEach((row, i) => row.forEach((value, j) => mapped.push({row: rowLabels[i], col: colLabels[j], value})));
    plotCode = `
const data = ${JSON.stringify(mapped)};
const plot = Plot.plot({
  ${plotOptions},
  color: {scheme: ${JSON.stringify(aesthetics.cmap || 'viridis')}},
  marks: [
    Plot.cell(data, {x: "col", y: "row", fill: "value"}),
    Plot.text(data, {x: "col", y: "row", text: d => String(d.value)})
  ]
});`;
  } else if (chartType === 'boxplot') {
    const mapped = [];
    Object.entries(data).forEach(([group, values]) => values.forEach((value) => mapped.push({group, value})));
    plotCode = `
const data = ${JSON.stringify(mapped)};
const plot = Plot.plot({
  ${plotOptions},
  marks: [Plot.boxY(data, {x: "group", y: "value", fill: "group"})],
  color: {domain: ${JSON.stringify(labels)}, range: ${JSON.stringify(palette.slice(0, labels.length))}}
});`;
  } else if (chartType === 'histogram') {
    const mapped = (data.values || []).map((value) => ({value}));
    const color = palette[0] || '#1f77b4';
    const bins = aesthetics.bins || 10;
    plotCode = `
const data = ${JSON.stringify(mapped)};
const plot = Plot.plot({
  ${plotOptions},
  marks: [Plot.rectY(data, Plot.binX({y: "count"}, {x: "value", thresholds: ${Number(bins)}, fill: ${JSON.stringify(color)}}))]
});`;
  } else {
    throw new Error(`unsupported chart type: ${chartType}`);
  }

  const title = String(aesthetics.title || recipe.name || recipe.id || 'Chart');
  const altText = String(access.alt_text || title);
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${title.replaceAll('&', '&amp;').replaceAll('<', '&lt;')}</title>
  <style>
    body { font-family: ${JSON.stringify(aesthetics.font || 'sans-serif')}; margin: 20px; }
    #chart { max-width: 100%; }
  </style>
</head>
<body>
  <h2>${title.replaceAll('&', '&amp;').replaceAll('<', '&lt;')}</h2>
  <div id="chart" role="img" aria-label=${JSON.stringify(altText)}></div>
  <script type="module">
import * as Plot from ${JSON.stringify(PLOT_ESM_URL)};
${plotCode}
document.getElementById("chart").appendChild(plot);
  </script>
</body>
</html>`;
}

function writeManifest(recipe, profile, recipePath, profileName, outputPath) {
  const profilePath = path.join('profiles', `${profileName}.yaml`);
  const manifest = {
    profile: MANIFEST_PROFILE,
    generated_at: new Date().toISOString(),
    generator: 'sci-render-kit',
    recipe: {
      id: recipe.id || 'unknown',
      canonical_sha256: canonicalSha256(recipe),
      file_sha256: fileSha256(recipePath),
      source: recipePath
    },
    target_profile: {
      id: profile.name || profileName,
      canonical_sha256: canonicalSha256(profile),
      file_sha256: fileSha256(profilePath)
    },
    backend: {
      name: 'observable',
      version: PLOT_VERSION,
      runtime: `Node ${process.version}; browser ESM dependency at view time`
    },
    output: outputPath,
    output_sha256: fileSha256(outputPath),
    parameters: {
      aesthetics: {...(profile.aesthetics || {}), ...(recipe.aesthetics || {})},
      data_canonical_sha256: canonicalSha256(recipe.data || {}),
      data_keys: Object.keys(recipe.data || {})
    },
    provenance: {
      sidecar: null,
      accessibility_sidecar: recipe.accessibility ? path.basename(outputPath).replace(/\.[^.]+$/, '.a11y.json') : null,
      figure_evidence_sidecar: null
    },
    external_dependencies: [{
      name: '@observablehq/plot',
      version: PLOT_VERSION,
      url: PLOT_ESM_URL,
      required_at_view_time: true,
      bundled_in_output: false
    }],
    reproducibility: {
      level: 'R1',
      semantics: 'HTML and dependency identity are replay-addressable; offline replay requires vendoring/snapshotting the ESM dependency.',
      independently_rerun: false
    }
  };
  const manifestPath = outputPath.replace(/\.[^.]+$/, '.manifest.json');
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n', 'utf-8');
}

function render(recipePath, profileName = 'presentation') {
  const recipe = loadRecipe(recipePath);
  const errors = validateRecipe(recipe);
  if (errors.length) throw new Error(errors.join('; '));
  const profile = loadProfile(profileName);
  const html = generateHTML(recipe, profile);
  const output = recipe.output;
  const outputDir = output.dir || 'output';
  fs.mkdirSync(outputDir, {recursive: true});
  const outputPath = path.join(outputDir, output.filename || 'figure.html');
  fs.writeFileSync(outputPath, html, 'utf-8');
  console.log(`saved: ${outputPath}`);
  writeManifest(recipe, profile, recipePath, profileName, outputPath);
}

const args = process.argv.slice(2);
if (args[0] === 'render' && args[1]) {
  let profile = 'presentation';
  const flagIndex = args.indexOf('--profile');
  if (flagIndex !== -1 && args[flagIndex + 1]) profile = args[flagIndex + 1];
  else if (args[2] && !args[2].startsWith('--')) profile = args[2];
  render(args[1], profile);
} else {
  console.log('usage: node backends/observable_adapter.js render <recipe.yaml> [--profile <name>]');
  process.exitCode = 2;
}
