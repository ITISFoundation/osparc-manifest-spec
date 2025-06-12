#!/bin/bash
# filepath: scripts/validate-uvx.sh
# Run validation script using uv to automatically handle dependencies

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Default values
MANIFEST_PATH=${1:-"cad_manifest.json"}
SCHEMA_PATH=${2:-"schema/cad_manifest.schema.json"}

# Run the validation script with uv run
# This handles installing and managing Python dependencies on the fly
uv run --with jsonschema "$SCRIPT_DIR/validate.py" "$MANIFEST_PATH" "$SCHEMA_PATH"
