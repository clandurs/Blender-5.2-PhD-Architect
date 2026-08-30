# Materials and shaders

## Scope

Use for physically based look development, stylized shaders, texture/node architecture, engine compatibility, shader debugging, and material handoff.

## Separate appearance from implementation

Define the visual contract first:

- material identity and physical/stylized intent;
- reference lighting conditions and target cameras;
- surface, volume, displacement, emission, and transparency needs;
- Cycles, EEVEE, viewport, export, or multi-engine targets;
- texture/data inputs, coordinate spaces, scale, and variation;
- performance and portability budget.

Then choose the node implementation. A complicated graph is not more accurate; it is more expensive to understand, compile, evaluate, and translate.

## Physically based reasoning

**[Evergreen]** A BSDF describes how light interacts with a surface, not merely its displayed color. Diagnose materials under controlled lighting:

- Base color/albedo should not contain baked specular highlights unless the art style requires them.
- Metallic is a material-class decision, not a generic “shininess” control.
- Roughness changes highlight spread and reflected-environment clarity; inspect at grazing angles.
- Index-of-refraction/specular behavior, transmission, subsurface, coat, sheen, and thin-wall behavior must match the material model and renderer.
- Bump changes shading normals; displacement changes geometry/silhouette when sufficient tessellation exists.
- Energy gain from arbitrary shader addition can produce unstable results. If intentionally nonphysical, label the art-direction reason.

## Node architecture

Structure reusable materials in layers:

1. **Inputs:** images, attributes, UV/object/generated coordinates, scale parameters.
2. **Signal preparation:** mapping, channel separation, range remap, normal conversion.
3. **Material logic:** masks, weathering, edge/height logic, variation.
4. **Shading:** surface/volume/displacement model.
5. **Output:** explicit render target when engine-specific variants are required.

Expose artist-facing controls with units and useful ranges. Name node groups by purpose, not implementation detail. Avoid hidden dependencies on object names or undeclared attributes.

Use node groups for coherent reuse, but do not create a monolith that forces every material to compile unused branches. Prefer composable groups with stable interfaces.

## 5.2 engine distinctions

**[5.2]** Cycles is a path tracer and EEVEE is an interactive raster-based engine with approximations and explicit limitations. Shared node graphs do not guarantee identical images.

For parity-sensitive work:

- inventory unsupported/approximated nodes and effects;
- test transparency, refraction, displacement, volumes, SSS, light probes, and passes independently;
- use engine-targeted Material Output nodes only when divergence is deliberate and documented;
- compare under matched color management, exposure, world, lights, camera, and resolution.

**[5.2]** Rendering release notes add Thin Wall behavior to Principled BSDF and change/convert some SSS behavior. Cite the 5.2 release notes when migrating a material library.

## Color management

Do not use the display as an implicit color pipeline. Record:

- OCIO configuration;
- input color space for each image;
- scene-linear working assumptions;
- display, view, look, exposure, and gamma controls;
- output transform and file encoding.

Never “fix” a data map by changing its values until confirming it was not transformed as color. Never bake a display view into a texture unless the delivery contract calls for display-referred pixels.

## Debugging method

When a material looks wrong, reduce the graph:

1. Verify object/material assignment and active material slots.
2. Replace the surface with a constant shader to separate geometry/lighting from texture logic.
3. Preview each scalar/vector/color input directly.
4. Verify UV/attribute name, domain, coordinate space, and scale.
5. Inspect image path, packing, bit depth, alpha, and color-space setting.
6. Reintroduce normal, displacement, transmission, and volume one at a time.
7. Compare Cycles and EEVEE only after each works independently.

## Validation gates

- Material reads correctly under neutral, grazing, and target lighting.
- Inputs use declared color/data semantics and channel mapping.
- Roughness/specular/transmission behavior remains plausible across exposure and environment changes.
- No undeclared attribute, object-name, UV-map, or external-path dependency.
- Cycles/EEVEE divergence is either within acceptance or explicitly authored.
- Shader compilation/evaluation cost is measured on representative assets.
- Exported material matches the target format's supported subset; unsupported procedural detail is baked deliberately.
- Texture and shader version are tied to the published asset.

## Failure signatures

| Symptom | Test |
| --- | --- |
| Material looks correct only under one HDRI | Test neutral studio lights and grazing angles; likely baked lighting or overfit ranges |
| Roughness appears too glossy | Inspect data-map color transform, inversion, and value range |
| Black/flickering surface | Disconnect displacement/normal/volume, inspect normals and NaN-producing math |
| EEVEE differs from Cycles | Check EEVEE limitations and isolate approximated features, not generic “quality” |
| Export is flat | Determine which procedural nodes/material extensions the target actually supports and bake missing signals |
| Node edits affect unrelated assets | Inspect shared data-block/group ownership and intended linking |

## Authoritative anchors

- [Blender 5.2 Rendering](https://docs.blender.org/manual/en/5.2/render/index.html)
- [Blender 5.2 EEVEE limitations](https://docs.blender.org/manual/en/5.2/render/eevee/limitations/limitations.html)
- [Blender 5.2 Rendering release notes](https://developer.blender.org/docs/release_notes/5.2/rendering/)
- [Stanford CS 348B](https://graphics.stanford.edu/courses/cs348b-03/) for evergreen light-transport and reflection theory
- [OpenColorIO](https://opencolorio.org/) for color-pipeline terminology
