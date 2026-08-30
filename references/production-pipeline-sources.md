# Production, workstation, and interchange sources

Verified: **2026-08-30**. Use these sources for production patterns and external contracts. Except for Blender Foundation properties, they do not define Blender behavior.

## Blender Studio pipeline

- [Blender Studio pipeline introduction](https://studio.blender.org/tools/pipeline-overview/introduction) — design documents and guides for artists and technical directors across asset creation, shot assembly, animation, lighting, rendering, and review.
- [Blender Studio Tools and Pipeline](https://studio.blender.org/tools/) — production-tested Blender-centric tooling. The site describes the current Studio pipeline, so treat details as **current**, not automatically Blender 5.2-specific.
- [Blender Studio Asset Pipeline](https://studio.blender.org/tools/addons/asset_pipeline) — task-layer ownership, publish/pull behavior, staged and sandbox publishes, and hooks.

Use these as worked production patterns. Adopt only after matching team size, storage, review, version control, and asset complexity. “Blender Studio does it” is evidence of viability, not proof it is the best policy for every project.

## Color and image interchange

- [OpenColorIO](https://opencolorio.org/) — Academy Software Foundation color-management system designed for motion-picture and VFX production. Use for terminology and pipeline contracts around configurations, color spaces, displays, and views.
- [OpenEXR technical introduction](https://openexr.com/en/latest/TechnicalIntroduction.html) — channels, parts, views, deep data, compression, windows, and portability. Use when choosing render outputs and compositing handoffs.

Pipeline rules:

- Tag texture inputs by semantic role. Color textures and data maps normally need different transforms.
- Keep scene-linear working data distinct from display/view transforms.
- Use an image sequence for recoverable long renders; choose OpenEXR when high dynamic range, passes, or compositing latitude are required.
- Do not infer correct color from a viewport screenshot without recording configuration, view, exposure, display, and output transform.

## Scene and runtime interchange

- [Introduction to OpenUSD](https://openusd.org/release/intro.html) — layered scene description, composition arcs, references, payloads, variants, assets, and scalable collaboration.
- [Khronos glTF Registry](https://registry.khronos.org/glTF/) — normative glTF 2.0 specification and extension registry for runtime 3D delivery.

Use USD when layered scene composition and non-destructive overrides are the central requirement. Use glTF when compact runtime delivery and interoperable scene/mesh/material/animation transfer are central. Neither format is a lossless substitute for a working `.blend` authoring file.

The exporter and target importer define the practical supported subset. Validate a fresh export in the actual consumer; a successful Blender re-import is only an intermediate check.

## Software compatibility

- [VFX Reference Platform](https://vfxplatform.com/) — annual target versions for common VFX libraries and Linux build compatibility. The CY2026 platform is relevant to software released in 2026, but Blender's own bundled versions remain authoritative for Blender.

Use the platform when building binary extensions, integrating libraries, or designing a studio environment. Do not force its versions onto a stock Blender installation without checking Blender's build configuration.

## Workstation and benchmarking

- [Blender system requirements](https://www.blender.org/download/requirements/) — current minimum/recommended OS, CPU, RAM, GPU, display, and peripheral guidance. **Drift-prone:** recheck before purchase advice.
- [Blender Open Data](https://opendata.blender.org/about/) — community-submitted, versioned CPU/GPU Cycles benchmark results and methodology.

Hardware method:

1. Start from the exact workload: Cycles or EEVEE, GPU memory footprint, simulation type, texture set, viewport complexity, and output cadence.
2. Confirm 5.2 backend and driver support in the versioned Manual.
3. Compare devices using Blender Open Data filtered to the relevant Blender version and backend.
4. Treat aggregate benchmark score as render throughput, not as proof of viewport, sculpt, simulation, encoding, stability, thermals, or capacity.
5. Size VRAM/RAM for peak scene residency and failure recovery, not only average render time.

## Pipeline contract checklist

Record these before building interchange automation:

- authoring unit, world scale, up/forward axes, handedness, and origin policy;
- object, data-block, bone, material, texture, action, and file naming;
- accepted mesh primitives, maximum influences, morph targets, constraints, cameras, lights, and animation interpolation;
- material model and texture channel packing;
- color configuration and output transforms;
- file/path encoding, relative-path policy, case sensitivity, and package boundaries;
- version ownership, publish state, dependency lock, and rollback;
- producer validation, independent re-import, and actual consumer validation.
