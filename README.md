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

#### Using standard Python:

```bash
# Install dependencies
pip install pyyaml jsonschema

# Run the validation script
python scripts/validate.py cad_manifest.yaml schema/cad_manifest.schema.json
```

#### Using uv (recommended):

```bash
# Install uv if not already installed
pip install uv

# Run with automatic dependency management
uv pip install pyyaml jsonschema
python scripts/validate.py cad_manifest.yaml schema/cad_manifest.schema.json

# Or using the uvx wrapper script (automatically installs dependencies)
./scripts/validate-uvx.sh cad_manifest.yaml schema/cad_manifest.schema.json
```

### Docker Validation

```bash
# Build the validation Docker image
docker build -t cad-manifest-validator .

# Validate a manifest file
docker run --rm -v /path/to/your/cad_manifest.yaml:/app/cad_manifest.yaml cad-manifest-validator cad_manifest.yaml
```

### Pre-commit Hook

Add this to your pre-commit config to validate manifest files before commit:

```yaml
-   repo: local
    hooks:
    -   id: validate-manifest
        name: validate manifest
        entry: python scripts/validate.py
        language: python
        files: cad_manifest\.yaml$
        additional_dependencies: [pyyaml, jsonschema]
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
- Docker-in-Docker for testing validation in containers

## Contributing

Contributions to improve the schema are welcome. Please submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright

Copyright (c) 2025 IT'IS Foundation
