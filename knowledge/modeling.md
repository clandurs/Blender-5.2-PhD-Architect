# Modeling

## Scope and version notes

Use this module for mesh/curve construction, hard-surface and organic blockout, modifier architecture, precision modeling, and geometry handoff. Blender's tool inventory is **[5.2]**; proportion, form, continuity, and coordinate mathematics are **[Evergreen]**.

## Choose the representation before the tool

Start from the required edits and final consumer:

- **Direct mesh:** best when topology itself is the product or vertex-level control matters.
- **Modifier stack:** best when parameters, variants, and reversible iteration matter.
- **Curves:** best for paths, profiles, cables, trim, typography-like forms, and controlled sweep geometry.
- **Geometry Nodes:** best for rules, repetition, data-driven variation, or reusable operators; read `geometry-nodes.md`.
- **Sculpt:** best for rapid continuous form and high-frequency surface design; read `sculpting.md`.
- **Volume/remesh:** best for union-like blockout or scan cleanup, not for preserving production topology.

Do not choose “all quads,” “non-destructive,” or “procedural” as goals by themselves. Choose them only when they reduce a known downstream cost.

## Modeling contract

Before building, record:

- target dimensions, unit interpretation, origin, pivot, axes, and symmetry;
- silhouette and feature tolerances;
- camera distance and smallest visible detail;
- deformation, subdivision, boolean, bevel, collision, baking, or manufacturing needs;
- final triangle/vertex, material-slot, UV, and draw-call budgets;
- whether the result remains editable or must be frozen for export.

Work at a meaningful scale. Unapplied nonuniform object scale changes the effective behavior of bevels, arrays, textures, constraints, physics, and many tools. Applying scale is destructive to transform history and may affect animation or children, so inspect dependencies before doing it.

## Modifier architecture

**[5.2]** Blender modifiers evaluate from top to bottom. Order is part of the model, not cosmetic UI organization.

Reason in semantic stages:

1. **Source and symmetry:** mirror, array, curve-driven construction.
2. **Primary shape:** booleans, solidify, lattice, deform operations.
3. **Topology conditioning:** weld, remesh, triangulate when required.
4. **Surface response:** bevel, weighted/smoothed normals, subdivision.
5. **Delivery:** decimation, final triangulation, export-only corrections.

This is a reasoning template, not a fixed order. For example, bevel-before-boolean and boolean-before-bevel solve different edge problems. State why each stage needs the output of the stage above it.

Applying a modifier should be a gate:

- preserve a source copy or version;
- confirm modifier evaluation at render level, not only viewport level;
- identify attributes, shape keys, instances, and shared data that may change;
- confirm whether downstream tools need the procedural inputs;
- compare mesh counts and shading before/after.

## Hard-surface method

1. Block primary volumes at target dimensions.
2. Establish construction logic: panels, cuts, fasteners, seams, thickness, and assembly.
3. Test silhouette from delivery cameras before adding microdetail.
4. Use boolean operands with deliberate topology and naming; keep cutters in a controlled collection.
5. Design edge treatment from physical scale and shot distance. A bevel that exists only to catch highlights should be sized in world units, not by habit.
6. Inspect planar shading, normal continuity, and reflections under a broad area light or studio HDRI.
7. Freeze only at the handoff boundary and keep a procedural source.

## Organic and subdivision method

- Build low-frequency form before edge density.
- Place control loops according to silhouette, curvature change, and deformation—not a uniform grid.
- Avoid extraordinary vertices in high-curvature or strongly deforming areas when they create visible pinching.
- Test the actual subdivision level used in render and export.
- Keep base topology simple enough that edits remain coherent.
- Use real extreme poses for deforming forms; a neutral pose hides topology failures.

## Precision and transforms

Use numeric entry, snapping, local orientations, transform pivots, and dimensions deliberately. Distinguish object-space edits from mesh-space edits. If an apparent modeling error changes when the object rotation or scale changes, test transforms before rebuilding topology.

For repeated parts, prefer linked object data or instances when edits should propagate and downstream formats support them. Make single-user data only when divergence is intentional.

## Validation gates

- Dimensions, origin, axes, object transforms, and handedness match the contract.
- Silhouette and negative space pass at target cameras and distances.
- No unintended duplicate vertices, zero-area faces, internal faces, non-manifold boundaries, or flipped normals.
- Modifier viewport/render toggles and levels are intentional.
- Boolean and bevel results remain stable under representative edits.
- Smooth/flat boundaries and custom normal behavior match the target renderer/exporter.
- Material slots, UV layers, color attributes, vertex groups, and shape keys survive any conversion.
- A fresh export/re-import matches geometry, but final acceptance occurs in the actual consumer.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Bevel width varies unexpectedly | Compare applied versus unapplied scale on a duplicate |
| Boolean flickers or leaves slivers | Inspect coplanar surfaces, tiny edges, normals, solver, and operand scale |
| Subdivision pinches | Disable modifiers below Subdivision and inspect poles/edge spacing at base level |
| Shading bands on planar faces | Compare flat shading, face normals, triangulation, and normal modifiers separately |
| Export shape differs | Apply the exporter's modifier/triangulation policy on a duplicate and inspect serialized result |
| File becomes uneditable | Count applied stacks and lost construction objects; restore procedural source rather than patching the frozen mesh |

## Authoritative anchors

- [Blender 5.2 Modeling](https://docs.blender.org/manual/en/5.2/modeling/index.html)
- [Blender 5.2 modifier introduction](https://docs.blender.org/manual/en/5.2/modeling/modifiers/introduction.html)
- [CMU Graphics courses](https://graphics.cs.cmu.edu/courses/) for evergreen geometry and subdivision theory
