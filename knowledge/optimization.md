# Optimization

## Scope

Use for viewport latency, dependency-graph cost, Geometry Nodes performance, simulation time, render time, memory/VRAM, file I/O, startup, and workstation planning.

## Optimize a measured bottleneck

Define the metric and test scene:

- viewport frame time and interaction latency;
- dependency-graph evaluation time;
- simulation seconds per frame;
- render initialization versus samples/render time;
- peak RAM/VRAM and residency/spill;
- file open/save/link time;
- export/import time;
- final asset size and target runtime cost.

Record exact Blender patch, hardware, device/backend, driver, scene/frame, viewport mode, render settings, and warm/cold cache. Do not compare numbers captured under different contracts.

## Decompose before changing

### CPU/evaluation

Likely drivers: object count, modifiers, constraints, drivers, dependency cycles, Python handlers, Geometry Nodes graph, simulation, scene update, and draw preparation.

Tests:

- toggle collections/object types in groups;
- compare static frame versus animated scrub;
- isolate modifiers/constraints/handlers;
- compare instances versus realized/unique objects;
- inspect console/log timings where available.

### GPU/viewport

Likely drivers: geometry, shading/material compilation, transparency, shadows, overlays, texture residency, subdivision, curves/hair, volumes, and driver/backend issues.

Tests:

- compare solid/material/rendered modes;
- disable overlays, shadows, volumes, and transparency separately;
- inspect VRAM and driver logs;
- test factory-startup and alternate supported backend/device only on a preserved configuration.

### Cycles render

Separate scene synchronization/BVH, shader compile, texture upload, sampling, denoising, and output write. A faster sampling device may not improve a scene dominated by synchronization or memory spill.

### I/O

Inspect external texture/cache counts and sizes, network latency, compression, packed data, missing-path searches, and file-system behavior. A smaller compressed file can save storage while opening/saving more slowly.

## Geometry strategy

- Use instances for repeated geometry while operations and consumer allow them.
- Reduce evaluated geometry, not only base-mesh counts.
- Use viewport/render quality tiers for subdivision, particles, curves, volumes, and Geometry Nodes.
- Cull by camera/distance only with a stable visibility contract.
- Preserve silhouette, deformation zones, shading splits, and attachment points when simplifying.
- Avoid Realize Instances until required.
- Use proxy/collision geometry separate from visual geometry.

## Texture and material strategy

- Size textures from screen coverage and reuse/tiling strategy.
- Use appropriate bit depth and compression for signal type.
- Consolidate material/node logic when it reduces compilation/evaluation without destroying maintainability.
- Avoid duplicated image data and accidental unique material copies.
- Test mip/texture cache behavior and peak residency.

## Scene and pipeline strategy

- Link/reference reusable assets and publish stable versions.
- Load only required collections/assets for the task.
- Separate heavy simulation/render data from interactive work where the pipeline supports it.
- Keep caches and renders versioned and outside hot source files when practical.
- Remove orphan data only after inventory and explicit cleanup intent; file size alone is not proof data is safe to delete.

## Render strategy

- Optimize the dominant noise/path, not global samples first.
- Use adaptive sampling and denoising with temporal review.
- Tune bounces, caustics, volumes, subdivision, curves, light tree/path guiding, persistent data, and tiling only with before/after evidence.
- Render image sequences for recovery and parallelism.
- Measure representative hard frames, not an easy frame.

## Hardware decisions

Current system requirements and drivers are drift-prone. Recheck before purchase advice. Use Blender Open Data filtered by Blender version and backend, then evaluate capacity and non-render workloads separately.

Workstation choice should include:

- VRAM for peak scene residency;
- RAM for CPU render, simulations, caches, and fallback;
- CPU single-thread/parallel behavior for the actual workload;
- storage capacity, sequential throughput, random I/O, and backup;
- thermal/power stability over long renders;
- display GPU contention if the same GPU renders and drives the UI.

## Quality-preserving validation

Every optimization needs a baseline and comparison:

- same camera, frame, resolution, seed/settings, color transform, and input revision;
- timing after controlled warm-up;
- image difference or approved visual comparison;
- geometry/deformation/attribute/export checks;
- memory peak and failure behavior;
- worst-case and representative-frame sampling.

Do not accept a speedup that silently changes animation, visibility, lighting energy, normals, UVs, passes, or output color outside tolerance.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Low viewport FPS, fast render | Separate draw/material/overlay/object-count cost from Cycles sampling |
| High FPS until scrubbing | Inspect dependency graph, rigs, drivers, simulations, and handlers |
| GPU much slower than expected | Check synchronization, memory spill, backend/device, driver, and scene type |
| File opens slowly | Test external path/network search, packed data, linked libraries, caches, and compression |
| Geometry Nodes graph explodes memory | Find realization, domain conversion, list growth, or duplicated high-cost branches |
| Optimization changes look | Use fixed comparison frames and difference/target review before accepting |

## Authoritative anchors

- [Blender 5.2 Cycles render settings](https://docs.blender.org/manual/en/5.2/render/cycles/render_settings/index.html)
- [Blender 5.2 Geometry Nodes](https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/index.html)
- [Blender 5.2 GPU troubleshooting](https://docs.blender.org/manual/en/5.2/troubleshooting/gpu/index.html)
- [Blender system requirements](https://www.blender.org/download/requirements/)
- [Blender Open Data](https://opendata.blender.org/about/)
