#!/bin/bash
# filepath: scripts/validate-uvx.sh
# Run validation script using uvx to automatically handle dependencies

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Default values
MANIFEST_PATH=${1:-"cad_manifest.yaml"}
SCHEMA_PATH=${2:-"schema/cad_manifest.schema.json"}

# Run the validation script with uvx
uvx --deps pyyaml,jsonschema "$SCRIPT_DIR/validate.py" "$MANIFEST_PATH" "$SCHEMA_PATH"
