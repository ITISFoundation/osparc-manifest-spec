# oSPARC CAD Manifest Specification

This repository contains the schema specification for CAD manifests used in oSPARC projects.

## Purpose

The oSPARC CAD Manifest Specification defines a standard way to describe CAD components and their associated files in an external repository. This enables:

- Consistent tracking of CAD files across projects
- Automated validation of repository contents
- Better integration with oSPARC platforms and services

## Schema

The JSON Schema definition is available at:
[https://itisfoundation.github.io/osparc-manifest-spec/schema/cad_manifest.schema.json](https://itisfoundation.github.io/osparc-manifest-spec/schema/cad_manifest.schema.json)

## Usage

1. Add a `cad_manifest.json` file to your CAD repository root
2. Include the GitHub Actions workflow for validation (see below)
3. Structure your manifest according to the schema

### Example Manifest

```json
{
  "manifest_version": "1.0",
  "repository": "https://github.com/YourOrg/your-cad-repo",
  "components": [
    {
      "name": "Component1",
      "description": "Description of component",
      "files": [
        {
          "path": "cad/Component1.SLDASM",
          "type": "solidworks_assembly"
        },
        {
          "path": "cad/Component1.step",
          "type": "step_export"
        }
      ]
    }
  ]
}
```

## Validation

To validate your manifest, add the GitHub Actions workflow to your repository:

### GitHub Actions Validation

Create a file `.github/workflows/validate-cad-manifest.yml` in your repository with the following content:

```yaml
name: Validate CAD Manifest

on:
  push:
    paths:
      - 'cad_manifest.json'
  pull_request:
    paths:
      - 'cad_manifest.json'
  workflow_dispatch:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - run: pip install jsonschema

      - name: Download schema
        run: |
          curl -Lo schema.json https://itisfoundation.github.io/osparc-manifest-spec/schema/cad_manifest.schema.json

      - name: Validate
        run: |
          python -c "import json, jsonschema; jsonschema.validate(json.load(open('cad_manifest.json')), json.load(open('schema.json'))); print('✅ Valid manifest')"
```

This workflow will automatically validate your manifest file against the latest schema whenever it changes or when manually triggered.

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
