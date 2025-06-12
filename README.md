# oSPARC CAD Manifest Specification

This repository contains the schema specification for CAD manifests used in oSPARC projects.

## Purpose

The oSPARC CAD Manifest Specification defines a standard way to describe CAD components and their associated files in a repository. This enables:

- Consistent tracking of CAD files across projects
- Automated validation of repository contents
- Better integration with oSPARC platforms and services

## Schema

The JSON Schema definition is available at:
[https://itisfoundation.github.io/osparc-manifest-spec/schema/cad_manifest.schema.json](https://itisfoundation.github.io/osparc-manifest-spec/schema/cad_manifest.schema.json)

## Usage

1. Add a `cad_manifest.yaml` file to your CAD repository root
2. Include the GitHub Actions workflow for validation
3. Structure your manifest according to the schema

### Example Manifest

```yaml
manifest_version: "1.0"
repository: "https://github.com/YourOrg/your-cad-repo"
components:
  - name: Component1
    description: Description of component
    files:
      - path: cad/Component1.SLDASM
        type: solidworks_assembly
      - path: cad/Component1.step
        type: step_export
```

## Validation

You can validate your manifest using the provided GitHub Actions workflow or with local tools:

### Command Line Validation

#### Using uv (recommended)

```bash
# Install uv if not already installed
pip install uv

# Run validation with automatic dependency management
./scripts/validate-uvx.sh cad_manifest.yaml schema/cad_manifest.schema.json

# Or directly with uv
uv run --with pyyaml --with jsonschema ./scripts/validate.py cad_manifest.yaml schema/cad_manifest.schema.json
```

#### Using standard Python (alternative)

```bash
# Install dependencies
pip install pyyaml jsonschema

# Run the validation script
python scripts/validate.py cad_manifest.yaml schema/cad_manifest.schema.json
```

### Pre-commit Hook

Add this to your pre-commit config to validate manifest files before commit:

```yaml
-   repo: local
    hooks:
    -   id: validate-manifest
        name: validate manifest
        entry: ./scripts/validate-uvx.sh
        language: system
        files: cad_manifest\.yaml$
```

### Development Container

This repository includes a devcontainer configuration for VS Code that provides a consistent development environment with all necessary dependencies pre-installed.

To use it:
1. Install the "Remote - Containers" extension in VS Code
2. Open the repository in VS Code
3. Click on the green button in the bottom-left corner and select "Reopen in Container"

The container includes:
- Python 3.12
- UV for dependency management
- Pre-commit and other development tools

## Contributing

Contributions to improve the schema are welcome. Please submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright

Copyright (c) 2025 IT'IS Foundation
