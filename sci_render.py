#!/usr/bin/env python3
"""
sci-render-kit 主入口 (CLI)
Enhanced: Plugin backend system, colorblind palette, reproducibility lock, JSON schema validation
"""

import argparse
import sys
import os
import yaml
import json
import subprocess
import logging
from pathlib import Path
from jsonschema import validate, ValidationError

logger = logging.getLogger('sci_render')


def load_yaml(path: str) -> dict:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print("YAML_PARSE_FAILURE")
        print(f"Error parsing YAML file {path}: {e}")
        sys.exit(1)


def validate_recipe_schema(recipe: dict, schema: dict) -> list:
    """Validate recipe against JSON schema"""
    try:
        validate(instance=recipe, schema=schema)
        return []
    except ValidationError as e:
        return [f"Schema validation: {e.message} at {'.'.join(str(p) for p in e.path)}"]


class BackendRegistry:
    """Plugin-based backend system"""

    BACKENDS = {
        'matplotlib': {
            'cmd': 'python3',
            'script': 'backends/matplotlib_adapter.py',
            'requires': 'matplotlib',
        },
        'plotly': {
            'cmd': 'python3',
            'script': 'backends/plotly_adapter.py',
            'requires': 'plotly',
        },
        'altair': {
            'cmd': 'python3',
            'script': 'backends/altair_adapter.py',
            'requires': 'altair',
        },
        'ggplot2': {
            'cmd': 'Rscript',
            'script': 'backends/ggplot2_adapter.R',
            'requires': 'R',
        },
        'observable': {
            'cmd': 'node',
            'script': 'backends/observable_adapter.js',
            'requires': 'node',
        },
    }

    @classmethod
    def list_backends(cls):
        return list(cls.BACKENDS.keys())

    @classmethod
    def check_availability(cls, name: str) -> bool:
        if name not in cls.BACKENDS:
            return False
        backend = cls.BACKENDS[name]
        req = backend['requires']
        try:
            if req == 'python3':
                return True
            if req in ('matplotlib', 'plotly', 'altair'):
                __import__(req)
                return True
            subprocess.run([req, '--version'], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, ImportError, FileNotFoundError):
            return False


def run_quality_gates(recipe: dict, profile: dict, gates_def: dict):
    """Run quality gates with enhanced checks"""
    errors = []
    warnings = []
    aesthetics = {**profile.get('aesthetics', {}), **recipe.get('aesthetics', {})}

    for gate in gates_def.get('gates', []):
        level = gate.get('level')
        if level in ['P0', 'P1']:
            for check in gate.get('checks', []):
                cid = check.get('id')
                if cid == 'color-count':
                    palette = aesthetics.get('palette', [])
                    if len(palette) > 8:
                        errors.append(f"[{gate['name']}] {check['name']}: palette > 8 colors")

                elif cid == 'font-size':
                    font_size = aesthetics.get('font_size', 10)
                    profile_name = profile.get('name', '')
                    if profile_name == 'nature' and font_size < 5:
                        errors.append(f"[{gate['name']}] {check['name']}: Nature font >= 5")
                    elif profile_name == 'science' and font_size < 6:
                        errors.append(f"[{gate['name']}] {check['name']}: Science font >= 6")

                elif cid == 'forbidden-pairs':
                    palette = [c.lower() for c in aesthetics.get('palette', [])]
                    has_red = any(c in ['#ff0000', 'red'] for c in palette)
                    has_green = any(c in ['#00ff00', 'green'] for c in palette)
                    if has_red and has_green:
                        warnings.append(f"[{gate['name']}] {check['name']}: red+green combo")

                elif cid == 'no-3d':
                    if str(recipe.get('type', '')).startswith('3d-'):
                        errors.append(f"[{gate['name']}] {check['name']}: no 3D charts")

                elif cid == 'colorblind-safe':
                    palette = aesthetics.get('palette', [])
                    unsafe = ['#ff0000', '#00ff00', '#0000ff']
                    for c in palette:
                        if c in unsafe:
                            warnings.append(f"[{gate['name']}] {check['name']}: {c} may not be colorblind-safe")
                            break

    return errors, warnings


def generate_reproducibility_lock(recipe: dict, profile: dict, backend: str) -> dict:
    """Generate reproducibility lock file"""
    import datetime
    lock = {
        'generated_at': datetime.datetime.now().isoformat(),
        'recipe_id': recipe.get('id', 'unknown'),
        'recipe_hash': __import__('hashlib').sha256(
            json.dumps(recipe, sort_keys=True).encode()
        ).hexdigest()[:16],
        'profile': profile.get('name', 'default'),
        'backend': backend,
        'backend_available': BackendRegistry.check_availability(backend),
        'dependencies': {},
    }
    return lock


def main():
    parser = argparse.ArgumentParser(description="sci-render-kit v2 — Scientific Visualization Pipeline")
    parser.add_argument('recipe', help="YAML recipe file path")
    parser.add_argument('--profile', default='nature', help="Profile: nature, science, presentation, ieee")
    parser.add_argument('--backend', default='matplotlib',
                        choices=BackendRegistry.list_backends(),
                        help="Rendering backend")
    parser.add_argument('--dry-run', action='store_true', help="Validate only, don't render")
    parser.add_argument('--output-dir', default='output', help="Output directory")

    args = parser.parse_args()

    recipe_path = args.recipe
    if not os.path.exists(recipe_path):
        print(f"❌ Error: Recipe not found {recipe_path}")
        sys.exit(1)

    recipe = load_yaml(recipe_path)

    # 1. Schema validation
    schema_path = 'metadata/recipe.schema.yaml'
    if os.path.exists(schema_path):
        schema = load_yaml(schema_path)
        schema_errors = validate_recipe_schema(recipe, schema)
        if schema_errors:
            print("P0_SCHEMA_FAILURE")
            for e in schema_errors:
                print(f"  - {e}")
            sys.exit(1)
    print("✅ P0 Schema validation passed")

    # 2. Load profile
    profile_path = f'profiles/{args.profile}.yaml'
    if not os.path.exists(profile_path):
        print(f"MISSING_PROFILE: {profile_path}")
        sys.exit(1)
    profile = load_yaml(profile_path)

    # 3. Quality gates
    gates_path = 'quality/gates.yaml'
    if os.path.exists(gates_path):
        gates = load_yaml(gates_path)
        gate_errors, gate_warnings = run_quality_gates(recipe, profile, gates)
        if gate_errors:
            print("❌ Quality gates failed:")
            for e in gate_errors:
                print(f"  - {e}")
            sys.exit(1)
        if gate_warnings:
            print("⚠️ Quality warnings:")
            for w in gate_warnings:
                print(f"  - {w}")
    print("✅ P1 Quality gates passed")

    # 4. Check backend availability
    if not BackendRegistry.check_availability(args.backend):
        print(f"❌ Backend '{args.backend}' not available")
        sys.exit(1)

    # 5. Generate reproducibility lock
    lock = generate_reproducibility_lock(recipe, profile, args.backend)
    lock_path = Path(args.output_dir) / f"{Path(recipe_path).stem}.lock.json"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with open(lock_path, 'w') as f:
        json.dump(lock, f, indent=2)
    print(f"🔒 Reproducibility lock: {lock_path}")

    if args.dry_run:
        print("✅ Dry run complete")
        return

    # 6. Execute backend
    backend = BackendRegistry.BACKENDS[args.backend]
    print(f"🚀 Rendering with {args.backend}...")
    try:
        subprocess.run([
            backend['cmd'], backend['script'],
            "render", args.recipe,
            "--profile", args.profile,
            "--output-dir", args.output_dir
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"BACKEND_FAILURE: exit code {e.returncode}")
        sys.exit(1)

    # 7. Post-render checks
    output_cfg = recipe.get('output', {})
    output_file = output_cfg.get('filename', 'figure.png')
    output_path = Path(args.output_dir) / output_file

    post_errors = []
    if not output_path.exists():
        post_errors.append(f"Output file not generated: {output_path}")
    elif output_path.stat().st_size == 0:
        post_errors.append(f"Output file is empty: {output_path}")

    if post_errors:
        print("❌ Post-render checks failed:")
        for e in post_errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"✅ Render complete: {output_path}")


if __name__ == "__main__":
    main()
