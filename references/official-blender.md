# Official Blender sources

Verified: **2026-08-30**. These links are the primary authority for Blender-specific claims in this repository. Versioned 5.2 pages are preferred over `latest` pages.

## Version contract

- [Blender 5.2 LTS Manual](https://docs.blender.org/manual/en/5.2/) — user-facing behavior, editors, operators, settings, file formats, and workflows. **Version-bound: 5.2.**
- [Blender 5.2 Python API](https://docs.blender.org/api/5.2/) — `bpy`, `bmesh`, `mathutils`, RNA types, operators, application data, and API gotchas. **Version-bound: 5.2.**
- [Blender 5.2 LTS release notes](https://developer.blender.org/docs/release_notes/5.2/) — additions, behavior changes, experimental features, and migration details. **Version-bound: 5.2.**
- [Compatibility notes](https://developer.blender.org/docs/release_notes/compatibility/) — cross-version breaking changes. It identifies Blender 5.2 LTS as the July 2026–July 2028 LTS line and records compatibility-sensitive changes such as Geometry Nodes modifier RNA properties. **Continuously maintained; check date.**
- [Blender Developer Documentation](https://developer.blender.org/docs/) — developer handbook, feature documentation, release notes, build and test guidance. **Current unless a page states a version.**

## Topic map

| Domain | Canonical source | Scope |
| --- | --- | --- |
| Modeling | [Modeling index](https://docs.blender.org/manual/en/5.2/modeling/index.html) | Meshes, curves, text, volumes, modifiers, Geometry Nodes |
| Modifier evaluation | [Modifier introduction](https://docs.blender.org/manual/en/5.2/modeling/modifiers/introduction.html) | Non-destructive stack, categories, order, applying |
| Sculpting and paint | [Sculpting & Painting](https://docs.blender.org/manual/en/5.2/sculpt_paint/index.html) | Brushes, masks, Face Sets, adaptive resolution, painting |
| Remeshing and retopology | [Remeshing and Retopology](https://docs.blender.org/manual/en/5.2/modeling/meshes/retopology.html) | Voxel/quad remesh limits and manual retopology |
| UVs | [UV mapping](https://docs.blender.org/manual/en/5.2/modeling/meshes/uv/index.html) | Seams, unwrap, packing, UV editing |
| Animation and rigging | [Animation & Rigging](https://docs.blender.org/manual/en/5.2/animation/index.html) | Keyframes, armatures, constraints, actions, drivers, shape keys |
| Geometry Nodes | [Geometry Nodes](https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/index.html) | Fields, attributes, instances, baking, tools, performance |
| Physics | [Physics](https://docs.blender.org/manual/en/5.2/physics/index.html) | Forces, particles, rigid/soft bodies, cloth, fluids, baking |
| Rendering | [Rendering](https://docs.blender.org/manual/en/5.2/render/index.html) | Engines, cameras, lights, materials, color, passes, output |
| Cycles | [Cycles render settings](https://docs.blender.org/manual/en/5.2/render/cycles/render_settings/index.html) | Device, sampling, paths, performance, film, curves, volumes |
| EEVEE | [EEVEE limitations](https://docs.blender.org/manual/en/5.2/render/eevee/limitations/limitations.html) | Raster-specific approximation and unsupported cases |
| Cameras | [Cameras](https://docs.blender.org/manual/en/5.2/render/cameras.html) | Projection, focal length, sensor, shift, clipping, depth of field |
| Compositing | [Compositing](https://docs.blender.org/manual/en/5.2/compositing/index.html) and [compositor usage](https://docs.blender.org/manual/en/5.2/compositing/usage.html) | Node processing, Viewer/Composite output, sequencer integration |
| Motion tracking | [Movie Clip Editor](https://docs.blender.org/manual/en/5.2/movie_clip/index.html) | Tracking, solving, stabilization, masking |
| Grease Pencil | [Grease Pencil](https://docs.blender.org/manual/en/5.2/grease_pencil/index.html) | Structure, modes, materials, modifiers, multiframe, animation |
| Files and assets | [Assets, Files, & Data System](https://docs.blender.org/manual/en/5.2/files/index.html) | Data-blocks, paths, link/append, overrides, assets, interchange |
| Simulation cache | [Baking physics simulations](https://docs.blender.org/manual/en/5.2/physics/baking.html) | Cache naming, frame range, bake/free behavior, disk caches |
| Command line | [Using Blender from the command line](https://docs.blender.org/manual/en/5.2/advanced/command_line/index.html) | Background work, rendering, Python, logging, debugging |
| Script trust | [Scripting & Security](https://docs.blender.org/manual/en/5.2/advanced/scripting/security.html) | Auto-execution risk and trusted-source controls |
| Extensions | [Creating Extensions](https://docs.blender.org/manual/en/5.2/advanced/extensions/index.html) and [How to Create Extensions](https://docs.blender.org/manual/en/5.2/advanced/extensions/getting_started.html) | Packages, manifests, add-ons, wheels, repositories |
| Crash diagnosis | [Crashes](https://docs.blender.org/manual/en/5.2/troubleshooting/crash.html) | recovery, crash logs, debug launchers, common resource failures |
| GPU diagnosis | [Troubleshooting Graphics Hardware](https://docs.blender.org/manual/en/5.2/troubleshooting/gpu/index.html) | drivers, viewport/EEVEE/Cycles symptoms, GPU isolation |

## Python authority

- [API Reference Usage](https://docs.blender.org/api/5.2/info_api_reference.html) — data access, RNA, operators, and how to map UI actions to Python.
- [Context Access](https://docs.blender.org/api/5.2/bpy.context.html) — context is read-only and depends on the active area/state.
- [Gotchas](https://docs.blender.org/api/5.2/info_gotcha.html) — official index for threading, operators, modes, memory, bones, paths, and encoding hazards.
- [Troubleshooting Errors & Crashes](https://docs.blender.org/api/5.2/info_gotchas_crashes.html) — invalid references after reallocation, mode changes, removals, and undo.
- [Python API 5.2 release notes](https://developer.blender.org/docs/release_notes/5.2/python_api/) — migration-sensitive API additions and changes. In 5.2, Geometry Nodes modifier inputs/outputs moved from custom-property access to RNA properties.

## 5.2 release-specific anchors

- [Geometry Nodes 5.2 release notes](https://developer.blender.org/docs/release_notes/5.2/geometry_nodes/) — geometry bundles, lists, collection children, sound sampling, empty-object modifiers, attribute operations, and performance changes.
- [Physics 5.2 release notes](https://developer.blender.org/docs/release_notes/5.2/physics/) — explicitly labels new Geometry Nodes cloth and hair systems experimental. Treat them as provisional and supply a fallback.
- [Animation & Rigging 5.2 release notes](https://developer.blender.org/docs/release_notes/5.2/animation_rigging/) — selection, playback loop modes, pose-library conversion behavior, and in-between tools.
- [Rendering 5.2 release notes](https://developer.blender.org/docs/release_notes/5.2/rendering/) — render-output control, color-space menus, camera input spaces, Time node, thin-wall shading, and SSS conversion.
- [Compositor 5.2 release notes](https://developer.blender.org/docs/release_notes/5.2/compositor/) — File Output extension control, new image/node behavior, and compositor gizmos.

## Source development

- [Building Blender](https://developer.blender.org/docs/handbook/building_blender/) — official build system, platform instructions, CMake, dependency update, and build output.
- [Navigating the Code](https://developer.blender.org/docs/handbook/new_developers/navigate_code/) — source layout, operator/UI discovery, DNA structures, and search strategy.
- [Automated test setup](https://developer.blender.org/docs/handbook/testing/setup/) — `make test`, CTest, Python/C++ test placement, and test data.

## Interpretation rules

1. A Manual page proves documented behavior, not that a specific file is configured correctly.
2. An API page proves an interface contract, not that a script is context-safe or crash-free in every state.
3. Release notes override generic assumptions about what changed in 5.2.
4. Developer documentation is authoritative for Blender source contribution, but current build requirements can drift after 5.2.
5. A page resolving under `latest` is not sufficient for a 5.2 claim when a versioned URL exists.
6. Documentation can contain errors. If observed behavior conflicts, reproduce on the exact patch release, check bug reports/release fixes, and label the result rather than silently choosing one.
