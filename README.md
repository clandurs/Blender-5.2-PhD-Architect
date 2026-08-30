# Blender 5.2 PhD Architect

> **GitHub description:** Expert Blender 5.2 workflows, diagnostics, automation, and pipeline architecture.

An expert-level Codex skill for designing, diagnosing, automating, and validating Blender 5.2 LTS work. It combines version-locked Blender guidance with durable computer-graphics principles and production pipeline standards.

## What it covers

- Modeling, sculpting, topology, retopology, UVs, texturing, materials, and shaders.
- Rigging, skinning, animation, Geometry Nodes, physics, and Grease Pencil.
- Lighting, cameras, Cycles, EEVEE, compositing, tracking, and VFX.
- Python automation, add-ons, extensions, performance, troubleshooting, and production pipelines.
- Character, environment, animation, procedural, cinematic, and debugging workflows.

The skill is a decision system, not a mirror of the Blender manual. It tells an agent what to inspect, which evidence matters, where Blender 5.2 changed behavior, what is destructive, and how to validate a result at the correct boundary.

## Install

Copy the `blender-5-2-phd-architect` directory into your Codex skills directory. Invoke it as:

```text
$blender-5-2-phd-architect
```

Automatic discovery remains enabled. The folder and invocation name use `5-2` because Codex skill names allow lowercase letters, digits, and hyphens; the product title remains “Blender 5.2 PhD Architect.”

## Example requests

```text
Use $blender-5-2-phd-architect to diagnose why this rig deforms correctly in Blender but not after glTF export.
```

```text
Use $blender-5-2-phd-architect to design a deterministic Geometry Nodes scattering system for Blender 5.2 and identify every experimental dependency.
```

```text
Use $blender-5-2-phd-architect to build a Cycles optimization plan from scene evidence without reducing final-frame quality.
```

## Repository map

```text
blender-5-2-phd-architect/
|-- SKILL.md
|-- README.md
|-- CONTRIBUTING.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- official-blender.md
|   |-- academic-sources.md
|   `-- production-pipeline-sources.md
|-- knowledge/
|   |-- modeling.md
|   |-- sculpting.md
|   |-- topology-retopology.md
|   |-- uv-texturing.md
|   |-- materials-shaders.md
|   |-- rigging.md
|   |-- animation.md
|   |-- geometry-nodes.md
|   |-- simulations.md
|   |-- lighting-camera.md
|   |-- cycles-eevee-rendering.md
|   |-- compositing-vfx.md
|   |-- grease-pencil.md
|   |-- python-scripting.md
|   |-- addons-tools.md
|   |-- optimization.md
|   |-- troubleshooting.md
|   `-- production-pipelines.md
|-- workflows/
|   |-- character-production.md
|   |-- environment-production.md
|   |-- animation-production.md
|   |-- procedural-production.md
|   |-- cinematic-production.md
|   `-- debugging-playbook.md
`-- scripts/
    `-- validate_repository.py
```

## Source model

Blender-specific behavior is grounded in the [Blender 5.2 Manual](https://docs.blender.org/manual/en/5.2/), [Blender 5.2 Python API](https://docs.blender.org/api/5.2/), [Blender 5.2 release notes](https://developer.blender.org/docs/release_notes/5.2/), and [Blender Developer Documentation](https://developer.blender.org/docs/). Blender Studio guidance is treated as a proven production example, not a universal mandate. University material supplies evergreen graphics theory; OpenColorIO, OpenEXR, OpenUSD, Khronos glTF, and the VFX Reference Platform supply external pipeline contracts.

Every technical module distinguishes **[5.2]**, **[Evergreen]**, **[Pipeline choice]**, **[Experimental]**, and **[Inference]** claims. The verified source registry is in `references/` and is dated so later maintainers know when to recheck it.

## Validation

Run:

```powershell
python scripts/validate_repository.py
```

The validator checks required files, skill frontmatter, the GitHub description length, unfinished placeholders, internal Markdown links, and whether every external citation appears in the verified source registry. Use `--online` to request live HTTP checks when network access is available.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions must preserve version labels, cite primary sources, avoid copied manual prose, and add observable validation criteria rather than unsupported “best practices.”

## License

No repository license is selected. Choose one before public redistribution; this avoids assigning legal terms the repository owner did not request.
