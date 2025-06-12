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

```bash
# Install dependencies
pip install pyyaml jsonschema

# Run the validation script
./validate.sh cad_manifest.yaml schema/cad_manifest.schema.json
```

### Docker Validation

```bash
# Build the validation Docker image
docker build -t cad-manifest-validator .

# Validate a manifest file
docker run --rm -v /path/to/your/cad_manifest.yaml:/app/manifest.yaml cad-manifest-validator manifest.yaml
```

### Pre-commit Hook

Add this to your pre-commit config to validate manifest files before commit:

```yaml
-   repo: local
    hooks:
    -   id: validate-manifest
        name: validate manifest
        entry: python -c "import yaml, json, jsonschema, sys; schema = json.load(open('schema/cad_manifest.schema.json')); manifest = yaml.safe_load(open(sys.argv[1])); jsonschema.validate(instance=manifest, schema=schema); print('✅ Manifest is valid!')"
        language: python
        files: cad_manifest\.yaml$
        additional_dependencies: [pyyaml, jsonschema]
```

## Contributing

Contributions to improve the schema are welcome. Please submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright

Copyright (c) 2025 IT'IS Foundation
