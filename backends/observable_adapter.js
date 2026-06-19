#!/usr/bin/env node
/**
 * Observable Plot 后端适配器 — 将 YAML 配方渲染为交互式 HTML
 * 依赖：Observable Plot 库（通过 CDN 或 npm）
 */

const fs = require('fs');
const path = require('path');
const yaml = require('yaml'); // 若本地无 yaml 包，需 npm install yaml

function loadRecipe(recipePath) {
  const content = fs.readFileSync(recipePath, 'utf-8');
  return yaml.parse(content);
}

function loadProfile(name) {
  const profilePath = path.join('profiles', `${name}.yaml`);
  if (!fs.existsSync(profilePath)) return {};
  const content = fs.readFileSync(profilePath, 'utf-8');
  return yaml.parse(content);
}

function validateRecipe(recipe) {
  const errors = [];
  const required = ['type', 'data', 'aesthetics'];
  for (const key of required) {
    if (!recipe[key]) errors.push(`缺少必需字段: ${key}`);
  }
  if (!recipe.output) errors.push('缺少 output 配置');
  return errors;
}

function generateHTML(recipe, profile) {
  const aesthetics = { ...profile.aesthetics, ...recipe.aesthetics };
  const data = recipe.data;
  const chartType = recipe.type;
  
  const palette = aesthetics.palette || ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#000000'];
  
  let plotCode = '';
  
  if (chartType === 'line-chart') {
    const marks = Object.entries(data).map(([label, values], i) => {
      const color = palette[i % palette.length];
      const points = values.map((y, x) => ({ x, y, series: label }));
      return JSON.stringify(points);
    });
    
    plotCode = `
const data = [${marks.join(', ')}].flat();
const plot = Plot.plot({
  marks: [
    Plot.lineY(data, { x: "x", y: "y", stroke: "series", strokeWidth: 2 }),
    Plot.dot(data, { x: "x", y: "y", stroke: "series", fill: "series", r: 4 })
  ],
  color: { domain: ${JSON.stringify(Object.keys(data))}, range: ${JSON.stringify(palette.slice(0, Object.keys(data).length))} },
  style: { fontFamily: "${aesthetics.font || 'sans-serif'}", fontSize: "${aesthetics.font_size || 12}px" }
});
    `;
  } else if (chartType === 'scatter-plot') {
    const marks = Object.entries(data).map(([label, [x, y]], i) => {
      const color = palette[i % palette.length];
      const points = x.map((xi, j) => ({ x: xi, y: y[j], series: label }));
      return JSON.stringify(points);
    });
    
    plotCode = `
const data = [${marks.join(', ')}].flat();
const plot = Plot.plot({
  marks: [
    Plot.dot(data, { x: "x", y: "y", stroke: "series", fill: "series", r: 5, strokeWidth: 1 })
  ],
  color: { domain: ${JSON.stringify(Object.keys(data))}, range: ${JSON.stringify(palette.slice(0, Object.keys(data).length))} }
});
    `;
  } else {
    plotCode = `// TODO: 实现 ${chartType} 的 Observable Plot 渲染`;
  }
  
  return `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>${aesthetics.title || 'Chart'}</title>
  <script src="https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6"></script>
  <style>
    body { font-family: ${aesthetics.font || 'sans-serif'}; margin: 20px; }
    #chart { max-width: 100%; }
  </style>
</head>
<body>
  <h2>${aesthetics.title || 'Chart'}</h2>
  <div id="chart"></div>
  <script type="module">
${plotCode}
document.getElementById("chart").appendChild(plot);
  </script>
</body>
</html>`;
}

function writeManifest(recipe, profile, outputPath) {
  const manifest = {
    generated_at: new Date().toISOString(),
    generator: 'sci-render-kit/observable',
    recipe: recipe.id || 'unknown',
    profile: profile.name || 'default',
    backend: 'observable',
    output: outputPath
  };
  const manifestPath = outputPath.replace(/\.[^.]+$/, '.manifest.json');
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));
}

function render(recipePath, profileName = 'presentation') {
  const recipe = loadRecipe(recipePath);
  
  const errors = validateRecipe(recipe);
  if (errors.length > 0) {
    console.error('❌ 配方验证失败:');
    errors.forEach(e => console.error(`  - ${e}`));
    process.exit(1);
  }
  
  const profile = loadProfile(profileName);
  const html = generateHTML(recipe, profile);
  
  const output = recipe.output;
  const outputDir = output.dir || 'output';
  if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });
  
  const outputPath = path.join(outputDir, output.filename || 'figure.html');
  fs.writeFileSync(outputPath, html, 'utf-8');
  
  console.log(`✅ 已生成交互式图表: ${outputPath}`);
  writeManifest(recipe, profile, outputPath);
}

// CLI
const args = process.argv.slice(2);
if (args[0] === 'render' && args[1]) {
  const profile = args[2] || 'presentation';
  render(args[1], profile);
} else {
  console.log('用法: node backends/observable_adapter.js render <recipe.yaml> [profile]');
}
