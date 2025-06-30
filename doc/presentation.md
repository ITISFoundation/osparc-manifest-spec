---
marp: true
theme: default
paginate: true
style: |
  section {
    background-image: url('https://avatars.githubusercontent.com/u/32800832?s=280&v=4');
    background-repeat: no-repeat;
    background-position: bottom 20px right 20px;
    background-size: 80px 80px;
  }

  section.title {
    background-position: bottom 20px right 20px;
    background-size: 100px 100px;
  }

  section pre {
    font-size: 0.55em;
    line-height: 1.1;
  }

  section code {
    font-size: 0.55em;
  }
---

<!-- _class: title -->

# HORNET Manifests Specification

## Standardized CAD Component Description for Simulations

**IT'IS Foundation**

📖 **Repository:** https://github.com/ITISFoundation/hornet-manifest-spec

---

## What is HORNET Manifests?

🌐 **Standardized JSON schemas** for describing CAD components and preparing them for computational simulations

### Key Benefits:

- 🔍 **Discoverability** — Index CAD assets for simulation workflows
- 🔄 **Interoperability** — Reference components across tools and platforms
- 📂 **Structure** — Hierarchical organization for simulation setups
- 💾 **Consistency** — Schema validation ensures data integrity
- 🧪 **Simulation-Ready** — Comprehensive preparation for numerical analysis

---

## Two Main Manifest Types

### 📐 CAD Manifest (`cad_manifest.json`)

- Describes CAD components, assemblies, and files
- Tree-like structure with metadata (IDs, types, descriptions)
- File references (STEP, SolidWorks, etc.)

### ⚡ Simulation Manifest (`sim_manifest.json`)

- Maps CAD components to simulation properties
- Material assignments for physical calculations
- Boundary conditions and semantic tags
- Direct incorporation into computational models

**Validation:** VS Code, GitHub Actions, pre-commit hooks, or online tools

---

## CAD Manifest Example

Describes CAD components, assemblies, and files with metadata:

```json
{
  "$schema": "https://itisfoundation.github.io/hornet-manifest-spec/schema/cad_manifest.schema.json",
  "repository": "https://github.com/myorg/cad-project",
  "components": [{
    "id": "SimplePart",
    "type": "part",
    "description": "A basic part component",
    "files": [
      { "path": "parts/SimplePart.SLDPRT", "type": "solidworks_part" },
      { "path": "exports/SimplePart.step", "type": "step_export" }
    ]
  }]
}
```

---

## Simulation Manifest Example

Maps CAD components to simulation properties:

```json
{
  "$schema": "https://itisfoundation.github.io/hornet-manifest-spec/schema/sim_manifest.schema.json",
  "mappings": [{
    "component_ref": {
      "cad_manifest_path": "./cad_manifest.json",
      "component_id": "SimplePart"
    },
    "material": { "name": "Titanium" },
    "boundary_conditions": ["insulating"],
    "tags": ["biocompatible"]
  }]
}
```
