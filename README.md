# 📘 oSPARC CAD Manifest Specification

The oSPARC CAD Manifest Specification defines a standard way to describe CAD components and their associated files in an external repository. This enables:

* 🌐 **Discoverability** — Enables services (e.g. o²S²PARC) to index CAD assets.
* 📂 **Structure** — Defines a clear component hierarchy.
* 💾 **Consistency** — Prevents typos or missing fields with schema validation.
* 🛠️ **Interoperability** — Makes CAD data machine-readable and reusable.

## 🔗 TL;DR

* Write your manifest in **JSON**, include a `$schema` reference
* Use **VS Code**, **GitHub Actions**, **pre‑commit**, or **online tools** to validate
* All tools reuse the same JSON Schema — no duplicate logic needed 👍

## 📋 What's in this Repository

This repository contains:

* 🧩 The **JSON Schema** definition file at [`schema/cad_manifest.schema.json`](schema/cad_manifest.schema.json)
* 📝 **Examples** of valid manifest files at [`examples/`](examples/)
* 🛠️ **Validation tools** and instructions for integration


## 🧩 Schema

A **JSON Schema** describing how to create a valid `cad_manifest.json`.
It standardizes:

* ⚙️ The **structure** (components, assemblies, parts)
* ℹ️ Component **metadata** (name, type, description, files)
* 🧰 File references (paths and types like STEP/SolidWorks)

## 💡 Simple Example

Here's a minimal example of a valid `cad_manifest.json`:

```json
{
  "$schema": "https://itisfoundation.github.io/osparc-manifest-spec/schema/cad_manifest.schema.json",
  "repository": "https://github.com/myorg/cad-project",
  "components": [
    {
      "name": "SimpleAssembly",
      "type": "assembly",
      "description": "A basic assembly with one part",
      "files": [
        { "path": "assemblies/SimpleAssembly.SLDASM", "type": "solidworks_assembly" }
      ],
      "components": [
        {
          "name": "SimplePart",
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

## 🛠️ Different Ways to Validate your `cad_manifest.json`

### 1. ✅ In VS Code

Ensure your manifest begins like this:

```json
{
  "$schema": "https://itisfoundation.github.io/osparc-manifest-spec/schema/cad_manifest.schema.json",
  "repository": "...",
  "components": [ ... ]
}
```

VS Code (with built‑in JSON support) will:

* Fetch the schema automatically
* Show red squiggles for structural issues
* Offer autocompletion


### 2. ✅ Using GitHub Actions

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



## Contributing

Contributions to improve the schema are welcome. Please submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Copyright

Copyright (c) 2025 IT'IS Foundation
