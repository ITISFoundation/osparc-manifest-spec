#!/usr/bin/env python3
# filepath: scripts/validate.py
"""
Validate a CAD manifest against a schema.
Uses uv style dependencies.

Dependencies:
- jsonschema

When used with uv:
    uv run --with jsonschema ./scripts/validate.py path/to/manifest.json path/to/schema.json
"""

import json
import sys


def main():
    """Validate a manifest file against a schema."""
    # Parse arguments
    if len(sys.argv) < 2:
        manifest_path = "cad_manifest.json"
    else:
        manifest_path = sys.argv[1]

    if len(sys.argv) < 3:
        schema_path = "schema/cad_manifest.schema.json"
    else:
        schema_path = sys.argv[2]

    try:
        # Dynamically import dependencies
        import jsonschema

        # Load schema
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)

        # Load manifest
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        # Validate
        jsonschema.validate(instance=manifest, schema=schema)
        print(f"✅ Manifest {manifest_path} is valid!")
        return 0
    except ImportError as e:
        print(f"❌ Missing dependency: {e}", file=sys.stderr)
        print(
            "Run: uv run --with jsonschema ./scripts/validate.py",
            file=sys.stderr,
        )
        return 1
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}", file=sys.stderr)
        return 1
    except Exception as e:  # pylint: disable=broad-except
        # We want to catch all errors to provide a clean error message
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
