# Lighting and camera

## Scope

Use for light design, exposure, camera/lens choice, composition, depth of field, matching live footage, shot continuity, and lighting diagnostics.

## Separate four systems

Diagnose independently:

1. **Scene radiometry:** emitters, world, geometry scale, materials, and light transport.
2. **Camera model:** projection, focal length/field of view, sensor fit, shift, clipping, focus, and motion blur.
3. **Composition:** staging, screen direction, hierarchy, silhouette, and negative space.
4. **Display/output:** color configuration, view, exposure, display, and output transform.

A “dark render” can arise in any of these systems. Do not increase light power until identifying which one.

## Lighting method

- Define the motivated or stylized source direction and hierarchy.
- Start with one dominant source and world/environment contribution; add lights only for a named visual job.
- Use source size to shape shadow softness and highlight size, distance to control falloff/solid angle, and geometry to shape occlusion.
- Inspect albedo/roughness under neutral light before compensating for a broken material with lighting.
- Evaluate practicals/emission for visible appearance separately from their ability to illuminate the scene.
- Use light linking deliberately and document it; hidden inclusion/exclusion rules make shots hard to debug.
- Test shot-to-shot exposure and direction continuity in sequence, not as isolated stills.

## Camera method

**[5.2]** Blender cameras expose perspective, orthographic, and panoramic modes with engine-specific support. EEVEE limitations should be checked before choosing a projection.

Record:

- focal length or field of view and sensor dimensions/fit;
- camera transform, shift, clipping, safe areas, resolution/aspect, and pixel aspect;
- focus target/distance, aperture, blade/bokeh settings, and motion blur shutter;
- lens distortion or tracking calibration handled outside the ideal camera model.

Choose focal length and camera position together. Moving the camera changes perspective; changing focal length at fixed position changes framing without changing perspective relationships. Use lens shift rather than tilting when architectural verticals must remain parallel and the shot intent supports it.

Depth of field must be validated at final resolution. Viewport approximations, sample count, transparency, and render engine can alter the result.

## Matching footage

For a matchmove/VFX camera:

- confirm clip resolution, pixel aspect, frame rate, sensor/lens metadata, and any crop/stabilization;
- track features with parallax and distribution, not only count;
- solve, inspect reprojection error and outliers, then establish ground/origin/scale using known scene facts;
- handle lens distortion consistently across tracking, CG render, and final composite;
- validate with test geometry that spans foreground, midground, and background.

A low aggregate solve error can hide local drift. Inspect tracks and CG alignment through the full shot.

## Exposure and color

Use exposure to place scene-linear values into a useful viewing range; use lights/materials to express scene relationships. Avoid per-shot arbitrary gamma changes that destroy pipeline consistency.

Record OCIO configuration, view, look, exposure, and display. A reference image should be compared in a known color space; screenshots are not sufficient provenance.

## Validation gates

- Camera projection, lens/sensor, aspect, shift, clipping, and focus match the shot contract.
- Composition reads at final crop, including titles/UI/safe areas when relevant.
- Lighting hierarchy and direction remain clear under target material response.
- No unintended clipping, fireflies, light leaks, or off-screen EEVEE dependence.
- Exposure/color settings are recorded and consistent across review/output.
- Depth of field and motion blur pass at final resolution and representative motion.
- Matchmove holds across depth and the entire frame range.
- Camera/light settings survive export only if the target format/consumer supports the same model.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Scene feels flat | Inspect source size/direction, material roughness, fill ratio, and exposure separately |
| Perspective looks wrong after matching framing | Compare camera position before changing focal length |
| CG slides over footage | Inspect individual track drift, lens distortion, frame rate, and scale/origin |
| Depth of field focuses behind subject | Verify focus object/distance in world units and evaluated camera transform |
| EEVEE reflection disappears at frame edge | Check documented screen/depth-based limitations and overscan/probe alternatives |
| Render differs from viewport | Match engine, color view, exposure, samples, lights, world, and visibility states |

## Authoritative anchors

- [Blender 5.2 Cameras](https://docs.blender.org/manual/en/5.2/render/cameras.html)
- [Blender 5.2 Rendering](https://docs.blender.org/manual/en/5.2/render/index.html)
- [Blender 5.2 EEVEE limitations](https://docs.blender.org/manual/en/5.2/render/eevee/limitations/limitations.html)
- [Stanford CS 348B](https://graphics.stanford.edu/courses/cs348b-03/) for evergreen cameras, radiometry, sampling, and light transport
- [OpenColorIO](https://opencolorio.org/) for color-management contracts
