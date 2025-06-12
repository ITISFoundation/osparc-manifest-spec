#!/bin/bash
# Simple script to validate a CAD manifest against a schema

# Default values
MANIFEST_PATH=${1:-"cad_manifest.yaml"}
SCHEMA_PATH=${2:-"schema/cad_manifest.schema.json"}

# Validate the manifest
python -c "
import yaml
import json
import jsonschema
import sys

try:
    # Load schema
    with open('$SCHEMA_PATH', 'r') as f:
        schema = json.load(f)

    # Load manifest
    with open('$MANIFEST_PATH', 'r') as f:
        manifest = yaml.safe_load(f)

    # Validate
    jsonschema.validate(instance=manifest, schema=schema)
    print('✅ Manifest is valid!')
    sys.exit(0)
except Exception as e:
    print(f'❌ Error: {e}', file=sys.stderr)
    sys.exit(1)
"
