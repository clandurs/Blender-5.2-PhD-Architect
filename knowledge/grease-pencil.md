# Grease Pencil

## Scope

Use for 2D/3D drawing, storyboards, line art, cut-out or frame-by-frame animation, Grease Pencil materials, modifiers, rigging, compositing, and hybrid scenes.

## Data and style contract

Define:

- final camera, projection, resolution, frame rate, and delivery engine;
- stroke/fill style, line weight behavior, palette, and material ownership;
- layer organization, naming, masks, blending, and edit permissions;
- frame-by-frame, interpolation, rigged deformation, generated line art, or hybrid method;
- whether depth, lighting, holdouts, and 3D occlusion are artistic or physically spatial;
- target export/render format and downstream support.

Grease Pencil is spatial drawing data, not simply raster paint. Camera distance, object scale, layer transforms, stroke radius, material, modifiers, and render settings interact.

## Structure

Organize by semantic function:

- character/prop/background/FX ownership;
- line, fill, shadow, highlight, matte, and guide roles;
- shot or asset layering;
- locked reference and editable production layers;
- material slots with stable names and intended stroke/fill behavior.

Avoid a single giant object/layer when different elements need independent timing, depth, masks, review, or reuse. Avoid excessive fragmentation when it makes timing and material management brittle.

## Drawing and cleanup

1. Establish camera and scale before finalizing line weight.
2. Block with simple strokes and clear silhouettes.
3. Use multiframe/onion-skin tools to maintain volume and arcs.
4. Clean stroke direction, point density, joins, overlaps, and fill closure at target resolution.
5. Use sculpt/edit operations for form correction; preserve intentional hand variation.
6. Test materials and antialiasing in the final render engine.

Point density should represent curvature and deformation needs. Excess points raise edit cost and can create noisy interpolation; too few points flatten curves.

## Animation approaches

- **Frame-by-frame:** maximal drawing control; plan exposure and key/breakdown/in-between ownership.
- **Interpolated drawing:** efficient for compatible stroke topology; inspect correspondences and shape collapse.
- **Rigged:** efficient for reusable/cut-out motion; test stroke deformation, thickness, and overlaps.
- **Modifier-driven:** useful for build, noise, time offsets, color, and procedural effects; preserve stack order and output reproducibility.
- **Line Art:** useful for derived lines from 3D geometry; validate occlusion, material/collection filters, camera, and temporal stability.

Combine methods only with a clear priority when two systems affect the same stroke property.

## Materials and rendering

**[5.2]** Grease Pencil uses dedicated stroke/fill material behavior and supports its own modifiers and modes. Do not assume standard mesh shader-node behavior applies identically.

Validate:

- stroke/fill visibility and material slot assignment;
- opacity and blend behavior over varied backgrounds;
- depth ordering, z-fighting, and camera clipping;
- EEVEE/Cycles feature support and pass behavior;
- line thickness at final resolution and camera distance;
- compositing/holdout requirements.

## Hybrid 2D/3D scenes

- Lock camera and projection decisions early.
- Establish whether strokes live in world, object, surface, view, or screen-oriented space.
- Use guides and proxy geometry for consistent perspective.
- Test depth intersections and shadows deliberately; accidental 3D correctness can conflict with graphic design.
- Render representative motion because line-art and modifier evaluation can flicker even when a still looks correct.

## Validation gates

- Layer, object, material, and timing ownership is clear.
- Stroke density and line weight hold at final camera and resolution.
- Fills remain closed/intentional through animation.
- Interpolation or rigging preserves form without unexpected stroke correspondence.
- Modifiers and line art are temporally stable across representative frames.
- Depth, masks, opacity, and blend behavior pass over target backgrounds.
- Render/export preserves intended stroke, fill, timing, and camera behavior.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Lines change apparent width | Compare world/object scale, camera distance, stroke radius, and modifier settings |
| Fill disappears | Inspect stroke closure, material fill state, self-intersection, and layer visibility |
| In-between shape collapses | Inspect stroke/point correspondence; use redraw or compatible topology |
| Line Art flickers | Test occlusion/topology/camera thresholds across adjacent frames |
| Depth order changes unexpectedly | Inspect 3D position, layer/order policy, z-offset, and camera clipping |
| Export loses style | Confirm target format supports Grease Pencil; otherwise render/bake to supported representation |

## Authoritative anchors

- [Blender 5.2 Grease Pencil](https://docs.blender.org/manual/en/5.2/grease_pencil/index.html)
- [Blender 5.2 Animation & Rigging](https://docs.blender.org/manual/en/5.2/animation/index.html)
- [Blender 5.2 Compositing](https://docs.blender.org/manual/en/5.2/compositing/index.html)
