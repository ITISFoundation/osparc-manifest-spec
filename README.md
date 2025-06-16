# HORNET CAD Manifest Specification


The Hornet CAD Manifest Specification defines a standard way to describe CAD components and their associated files in an external repository. This enables:

* 🌐 **Discoverability** — Enables services (e.g. o²S²PARC) to index CAD assets and integrate them in existing workflows e.g. in simulations.
* 📂 **Structure** — Defines a clear component hierarchy.
* 💾 **Consistency** — Prevents typos or missing fields with schema validation.
* 🛠️ **Interoperability** — Makes CAD data machine-readable and reusable.


### 🔗 TL;DR

How to create a CAD manifest that follows this spec?

* Write a manifest in **JSON** that identifies the different parts and assemblies of your CAD (see `examples/cad_manifest.json`)
  * include a `$schema` to a published version of this repository's `cad_manifest.schema.json`
* Use **VS Code**, **GitHub Actions**, **pre‑commit**, or **online tools** to validate
  * All tools reuse the same JSON Schema — no duplicate logic needed 👍

---

## 📋 What's in this Repository

This repository contains:

* 🧩 **JSON Schemas** for manifests:
  * [`schema/cad_manifest.schema.json`](schema/cad_manifest.schema.json) - For describing CAD components
  * [`schema/sim_manifest.schema.json`](schema/sim_manifest.schema.json) - For mapping CAD components to simulation properties
* 📝 **Examples** of valid manifest files at [`examples/`](examples/)
* 📚 **Vocabularies** at [`vocab/`](vocab/) for standardized terms
* 🛠️ **Validation tools** and instructions for integration

### 🧩 JSON Schemas

#### CAD Manifest Schema

A **JSON Schema** describing how to create a valid `cad_manifest.json`.
It standardizes:

* ⚙️ A **tree-like structure** of `components`, including assemblies and parts
* ℹ️ Component **metadata** (id, type, description, files)
* 🧰 File references (paths and types like STEP/SolidWorks)


#### Simulation Manifest Schema

A **JSON Schema** describing how to create a valid `sim_manifest.json`. 
It standardizes:

* 🔗 **Mapping** CAD components to simulation properties
* 🧪 **Material** assignments
* 🛠️ **Boundary conditions** for simulation setup
* 🏷️ **Semantic tags** for categorization

The simulation manifest connects components defined in a CAD manifest to simulation-specific properties, enabling direct use in computational simulations.

### 📚 Vocabulary Files

This specification includes standardized vocabularies to ensure consistency:

* [`vocab/semantic-tags.json`](vocab/semantic-tags.json) - Defines standardized tags for component roles (e.g., "electrical_interface", "biocompatible")
* [`vocab/boundary-conditions.json`](vocab/boundary-conditions.json) - Defines standardized boundary conditions for simulations (e.g., "electrical_contact", "insulating")

These vocabularies:
* Ensure consistent terminology across projects
* Allow validation of correct tag/condition usage
* Can be extended as needs evolve

### 💡 Simple Example

Here's a minimal example of a valid `cad_manifest.json`:

```json
{
  "$schema": "https://itisfoundation.github.io/hornet-manifest-spec/schema/cad_manifest.schema.json",
  "repository": "https://github.com/myorg/cad-project",
  "components": [
    {
      "id": "SimpleAssembly",
      "type": "assembly",
      "description": "A basic assembly with one part",
      "files": [
        { "path": "assemblies/SimpleAssembly.SLDASM", "type": "solidworks_assembly" }
      ],
      "components": [
        {
          "id": "SimplePart",
          "type": "part",
          "description": "A basic part component",
          "files": [
            { "path": "parts/SimplePart.SLDPRT", "type": "solidworks_part" },
            { "path": "exports/SimplePart.step", "type": "step_export" }
          ]
        }
      ]
    }
  ]
}
```

For more complex examples, see the [`examples/`](examples/) directory.

#### Simulation Manifest Example

Here's a minimal example of a valid `sim_manifest.json`:

```json
{
  "$schema": "https://itisfoundation.github.io/hornet-manifest-spec/schema/sim_manifest.schema.json",
  "mappings": [
    {
      "component_ref": {
        "cad_manifest_path": "./cad_manifest.json",
        "component_id": "SimplePart"
      },
      "material": {
        "name": "Titanium"
      },
      "boundary_conditions": ["insulating"],
      "tags": ["biocompatible"]
    }
  ]
}
```

For more complex examples, see the [`examples/`](examples/) directory.

### 🔄 Keeping Schemas and Vocabularies in Sync

The repository includes an automated sync mechanism:

* The script [`scripts/sync_vocab_to_schema.py`](scripts/sync_vocab_to_schema.py) ensures vocabulary terms are reflected in schema validation rules
* A pre-commit hook automatically runs this script to maintain synchronization
* This prevents vocabulary/schema drift and ensures consistent validation

### 🛠️ Different Ways to Validate your Manifests

![Schema validation](https://json-schema.org/img/json_schema.svg)

#### 1. ✅ In VS Code

Ensure your manifest begins like this:

```json
{
  "$schema": "https://itisfoundation.github.io/hornet-manifest-spec/schema/cad_manifest.schema.json",
  "repository": "...",
  "components": [ ... ]
}
```

VS Code (with built‑in JSON support) will:

* Fetch the schema automatically
* Show red squiggles for structural issues
* Offer autocompletion


#### 2. ✅ Using GitHub Actions

Add this workflow to [`.github/workflows/validate-manifest.yml`](.github/workflows/validate-manifest.yml) to your repo:

```yaml
- name: Extract schema URL
  id: get_schema
  runs: |
    echo "::set-output name=url::$(jq -r .\"$schema\" cad_manifest.json)"

- name: Validate manifest
  uses: sourcemeta/jsonschema@v9
  with:
    command: validate
    args: >
      --schema ${{ steps.get_schema.outputs.url }}
      --instance cad_manifest.json
```

This uses:

* 🐳 `jq` to read the `$schema` field
* ⚖️ `sourcemeta/jsonschema` to validate without custom scripts


#### 3. ✅ As a Pre-commit Hook

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/python-jsonschema/check-jsonschema
    rev: 0.33.0
    hooks:
      - id: check-jsonschema
        name: Validate CAD Manifest
        args: ["--schemafile", "cad_manifest.schema.json"]
        files: ^cad_manifest\.json$
```

This runs validation on staged edits to `cad_manifest.json` before commits.


#### 4. ✅ Online Validator

Use tools like:

* [**JSONSchema.dev**](https://jsonschema.dev/)
* [**JSON Schema Validator**](https://www.jsonschemavalidator.net/)

You can:

* Paste your `cad_manifest.json`
* Or load from URL
* The schema is fetched from its `$schema` header automatically


### 🎨 Generate UIs from the JSON Schema

You can automatically create user interfaces for editing `cad_manifest.json` files using these tools:

* **[JSON Schema Form Playground](https://rjsf-team.github.io/react-jsonschema-form/)** — Test RJSF instantly



## Contributing

Contributions to improve the schema are welcome. Please submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright

Copyright (c) 2025 IT'IS Foundation
