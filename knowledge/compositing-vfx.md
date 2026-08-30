# Compositing and VFX

## Scope

Use for render passes, compositor architecture, color correction, keying, masking, motion tracking, camera/object solves, stabilization, CG integration, and image-sequence delivery.

## Establish the image contract

Record:

- resolution, pixel aspect, frame rate, frame numbering, handles, and missing-frame policy;
- source/delivery color spaces, OCIO configuration, view, and output transform;
- straight versus premultiplied alpha expectation;
- channels/passes, bit depth, compression, and data-window/display-window behavior;
- camera/lens/distortion metadata and plate transformations;
- whether the compositor output is final delivery or an intermediate scene-linear sequence.

Compositing errors often arise from metadata and interpretation rather than node math.

## Node-graph architecture

Organize a composite in stages:

1. **Ingest:** image sequence, render layers, plate, matte, metadata assumptions.
2. **Normalize:** color space, alpha convention, resolution/crop, distortion state.
3. **Core integration:** key/matte, premultiply discipline, transforms, grade, light wrap, depth/atmosphere, grain.
4. **Diagnostics:** matte view, difference, over/under exposure, channel inspection, edge view.
5. **Output:** Composite for intended result and File Output nodes for durable intermediates/deliverables.

Group repeatable operations with clear color/alpha expectations. Do not hide a view transform or destructive clamp inside a utility group.

## Alpha and edges

Know whether RGB is already multiplied by alpha. Operations such as blur, grade, transform, and merge can produce dark/bright fringes if alpha convention is wrong. Diagnose by viewing RGB, alpha, and result over black, gray, and white backgrounds.

Do not repair a systemic premultiplication error by eroding every matte. Fix the convention at the boundary.

## Pass reasoning

- Use combined beauty when it is sufficient; add passes only for a named control.
- Data passes such as depth, normal, vector, index/ID, and cryptographic mattes have different filtering and color requirements from beauty passes.
- Depth is camera-space data whose range and anti-aliasing behavior matter; normalize based on scene/camera facts.
- Motion/vector passes must align with shutter, frame, and compositor expectations.
- Reconstructing beauty from lighting passes can diverge if emission, transparency, volumes, or denoising are omitted.

Verify pass completeness with a controlled test before rendering the full shot.

## Tracking and matchmove

1. Preserve original plate and metadata.
2. Apply lens-distortion policy consistently.
3. Track distributed features with parallax and duration.
4. Reject drifting/outlier tracks based on trajectory, not only solve error.
5. Solve camera/object motion and establish scene orientation and scale from known references.
6. Validate with proxy geometry across depth and throughout the shot.
7. Render CG with matching camera, motion blur, distortion state, and color pipeline.

An aggregate solve error is diagnostic, not acceptance. Look for local sliding and depth-dependent drift.

## CG integration

Match:

- camera/lens/distortion and motion blur;
- illumination direction, softness, intensity ratios, and environment;
- contact shadows, reflections, holdouts, and occlusion;
- depth haze, defocus, chromatic behavior, grain/noise, and sharpness;
- black/white levels and scene/display color transforms.

Integrate in scene-linear space when the pipeline calls for it, then apply the approved display/output transform at delivery.

## 5.2 notes

**[5.2]** The compositor supports node-based image processing and 5.2 adds/changes File Output extension control, image creation, and gizmo behavior. Do not assume scene output settings fully determine File Output node naming/extension behavior; inspect both.

**[5.2]** Compositor node groups can be used in sequencer strips/modifiers. Validate context-specific input/output behavior before treating a group as interchangeable between scene compositor and sequencer.

## Validation gates

- Frame range, numbering, resolution, aspect, color, alpha, and channel contract are explicit.
- Composite holds over multiple backgrounds with no fringe or matte contamination.
- Passes are interpreted as color or data correctly.
- Tracking/matchmove holds across depth and full duration.
- CG integration matches focus, blur, grain, distortion, lighting, and black level.
- File Output and Composite outputs are both inspected; paths and extensions are correct.
- Final sequence has no missing, duplicated, stale, or mixed-version frames.
- Delivery is checked in an independent viewer under known color management.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Dark fringe around CG | View unpremultiplied/premultiplied RGB and alpha over multiple backgrounds |
| Depth effect inverted or flat | Inspect camera-space depth range and normalization, not the color viewer alone |
| Track solve low error but visible slide | Inspect individual tracks and proxy geometry through shot depth |
| Output extension unexpected | Compare File Output node setting with scene output setting in 5.2 |
| Composite differs in external viewer | Compare OCIO config, view/output transform, alpha, and file metadata |
| Stale frames survive rerender | Version output directory or verify frame timestamps/hashes and completeness |

## Authoritative anchors

- [Blender 5.2 Compositing](https://docs.blender.org/manual/en/5.2/compositing/index.html)
- [Blender 5.2 compositor usage](https://docs.blender.org/manual/en/5.2/compositing/usage.html)
- [Blender 5.2 Movie Clip Editor](https://docs.blender.org/manual/en/5.2/movie_clip/index.html)
- [Blender 5.2 Compositor release notes](https://developer.blender.org/docs/release_notes/5.2/compositor/)
- [OpenColorIO](https://opencolorio.org/)
- [OpenEXR technical introduction](https://openexr.com/en/latest/TechnicalIntroduction.html)
