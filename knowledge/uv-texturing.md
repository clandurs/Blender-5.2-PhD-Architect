# UVs and texturing

## Scope

Use for UV architecture, seams, unwrapping, packing, texel density, UDIM decisions, texture baking, texture painting, and delivery maps.

## Start with the texture contract

Record:

- target renderer/material model and texture semantics;
- map list, channels, bit depth, file format, compression, and alpha meaning;
- color versus data texture interpretation;
- texture resolution, number of sets/tiles, memory budget, and mip behavior;
- tangent basis and normal-map convention;
- mirrored/overlapped UV policy;
- padding requirement at every target mip level;
- whether the consumer supports UDIMs, multiple UV sets, or material IDs.

Do not unwrap before deciding whether unique pixels, symmetry, trim sheets, tiling materials, decals, lightmaps, or atlas batching drive the asset.

## Seam strategy

Place seams where they minimize combined cost:

- low visibility or natural construction boundaries;
- hard normal breaks and material boundaries when alignment reduces duplication;
- areas that allow low-distortion flattening;
- places that remain stable under deformation;
- boundaries compatible with paint and bake workflow.

Every seam may duplicate runtime vertices and create filtering/bake risk. Fewer seams are not automatically better if the result is stretched or unpaintable.

## Unwrap and density method

1. Apply or account for object scale before comparing texel density.
2. Establish seams and unwrap by surface type; do not use one projection for every island.
3. Measure stretch using a checker at target scale.
4. Normalize density according to the visibility contract. Faces needing close detail may intentionally receive more area.
5. Orient islands when it helps anisotropic materials, trim sheets, hand painting, or compression.
6. Pack with target padding and rotation constraints.
7. Test mips or downscaled textures; a full-resolution screenshot hides bleed.

**[Pipeline choice]** Overlap/mirror only when unique wear, baked lighting, text, normal handedness, and downstream processing do not require unique pixels.

## Baking method

Treat a bake as a reproducible mapping from a named high source to a named low target:

- freeze transforms and final low triangulation;
- use the target tangent basis and normal orientation;
- separate intersecting parts or use matched naming when needed;
- build/inspect a cage instead of guessing ray distance;
- preserve sufficient padding/dilation;
- record selected-to-active, extrusion, ray, margin, device, and color settings;
- save high, low, cage, bake settings, and output hashes/version together.

For normal maps, a later topology, UV, smoothing, or triangulation change can invalidate the bake. Re-bake rather than hand-patching systemic errors.

## Texture semantics

**[Evergreen]** Color-managed values and physical data are different signal classes.

- Base color/emission imagery usually carries color meaning.
- Roughness, metallic, normal, height, masks, IDs, and packed channels are data and must not receive a display-referred color transform.
- Normal maps require a declared tangent/object/world space and channel orientation.
- Displacement requires scale, midpoint, and subdivision/tessellation agreement.
- Alpha may mean opacity, coverage, transmission control, or a packed data channel; name it.

Do not diagnose a “wrong texture” until verifying file path, active image, UV map, node connection, color-space interpretation, channel swizzle, and material/render settings.

## UDIM, atlas, and trim choices

- **UDIM:** high-resolution film/VFX asset sets; confirm consumer, renderer, and file-management support.
- **Atlas:** fewer material bindings and predictable runtime packaging; raises cross-asset update and padding coordination costs.
- **Trim sheet:** excellent for repeated architectural/hard-surface detail; constrains unique wear and requires disciplined UV orientation.
- **Tiling material plus masks/decals:** scalable environments; evaluate repetition, decal cost, and shader complexity.

## Validation gates

- Checker test shows acceptable stretch at target camera distance.
- Density and intentional exceptions are documented.
- Islands remain inside required tile/UV range; no accidental overlap.
- Padding survives the smallest tested mip/output scale.
- High/low/cage alignment produces clean projection at seams and tight gaps.
- Each image has correct color/data interpretation and channel mapping.
- Target renderer displays normals, alpha, roughness, and displacement correctly.
- Texture memory and material binding count meet the platform budget.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Checker density differs by object | Compare world scale, UV area, and object scale separately |
| Dark/bright roughness | Inspect image color-space interpretation before remapping values |
| Green channel appears inverted | Verify target normal convention and swizzle on a known test normal |
| Seams appear only at distance | Test lower mips and increase padding/dilation rather than hiding at full resolution |
| Bake projects unrelated parts | Isolate parts, matched naming, or cage intersections |
| Export ignores a UV set | Inspect exported attribute name/order and consumer support |

## Authoritative anchors

- [Blender 5.2 UV mapping](https://docs.blender.org/manual/en/5.2/modeling/meshes/uv/index.html)
- [Blender 5.2 Rendering](https://docs.blender.org/manual/en/5.2/render/index.html)
- [OpenColorIO](https://opencolorio.org/) for color-management contracts
- [Khronos glTF Registry](https://registry.khronos.org/glTF/) for runtime texture/material interchange
