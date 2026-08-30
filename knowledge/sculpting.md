# Sculpting

## Scope and version notes

Use for high-resolution form, concept sculpting, corrective shape work, scan cleanup, brush assets, masks, Face Sets, and the sculpt-to-production handoff. Blender mode behavior is **[5.2]**; anatomy, form hierarchy, curvature, and sampling limits are **[Evergreen]**.

## Select the resolution model

Choose deliberately:

- **Voxel remesh:** uniform spatial resolution and rapid topology renewal. Good for merging volumes and early/mid form; it discards production edge flow and can erode thin features.
- **Dynamic topology:** local tessellation driven by strokes. Good for exploratory localized detail; harder to reproduce and unsuitable when existing UVs/topology must survive.
- **Multiresolution:** stable base topology with sculpt levels. Good when low-resolution topology, UVs, and subdivision-compatible detail must coexist; modifier ordering and base-mesh edits require care.
- **Fixed mesh:** best for shape-key/corrective edits or modest sculpt changes on production topology.

**[5.2]** The Manual warns that predictable brush behavior depends on meaningful/applied mesh scale. Do not apply scale blindly on a rigged or animated object; test on a duplicate and preserve dependencies.

## Form hierarchy

Evaluate at three bands:

1. **Primary:** mass, proportion, silhouette, center of gravity, large planes.
2. **Secondary:** joints, folds, muscle/fat relationships, construction seams, medium breaks.
3. **Tertiary:** pores, scratches, weave, tool marks, microfolds.

Do not add tertiary detail to hide unresolved primary form. Verify each band with a lighting setup that reveals it: silhouette and flat lighting for primary; broad grazing light for secondary; close-up target lighting for tertiary.

## Controlled sculpt workflow

1. Duplicate or version the source. Record dimensions, transforms, topology, UVs, shape keys, multires levels, and modifier stack.
2. Establish symmetry policy. Use symmetry for efficiency, then break it only where the design or pose needs asymmetry.
3. Block primary masses with low enough resolution that large edits stay smooth.
4. Use masks and Face Sets as edit organization, not as substitutes for separate semantic parts when the pipeline requires parts.
5. Increase resolution only when the current level cannot represent a required feature.
6. Periodically test silhouette at target distance and a neutral material.
7. For characters, test joints and contact areas in pose before committing surface detail.
8. At handoff, choose retopology/bake, multires displacement, direct high-poly render, or decimated delivery explicitly.

## Surface and brush diagnosis

- If strokes vary with view or object transform, isolate scale, brush falloff, front-face settings, spacing, and topology density.
- If detail tears or becomes faceted, inspect local triangle size and whether the selected resolution system can support the frequency.
- If smoothing destroys form, work at the correct resolution band and reduce strength; smoothing is not a replacement for sound base form.
- If thin walls collapse during remesh, compare voxel size to wall thickness and consider temporary solid support or separate parts.
- If masks/Face Sets vanish during conversion, test attribute preservation on a small duplicate before processing the asset.

## Retopology and baking handoff

The sculpt is a geometric reference, not automatically the production mesh. Define:

- deformation zones and required loop directions;
- target triangle count and LOD policy;
- UV set and texel density;
- bake ray/cage policy, tangent basis, and target normal format;
- whether displacement or vector displacement is required;
- what high-frequency detail belongs in geometry versus normal/height/roughness maps.

Keep the exact high and low pair used for baking. A changed high sculpt or low topology invalidates prior maps even if filenames remain unchanged.

## Validation gates

- Primary form works in silhouette and orthographic/perspective views relevant to delivery.
- No accidental scale mismatch, hidden duplicate surface, self-intersection, or paper-thin region that breaks downstream work.
- Resolution is justified by visible detail; memory use remains within the workstation budget.
- Multires levels, sculpt base, UVs, and topology remain coherent if multires is used.
- Retopology conforms without avoidable shrinkage and deforms in target poses.
- Bake comparison uses the intended target tangent basis and target renderer.
- Tertiary detail remains visible but does not alias or shimmer at target output resolution.

## Failure signatures

| Symptom | Likely distinction |
| --- | --- |
| Brush feels elliptical or strength changes by axis | Test object scale and transforms before brush settings |
| Voxel remesh deletes fingers/straps | Feature thickness is below effective voxel resolution |
| Multires reports topology conflict | Base topology or modifier relationship changed; do not force-apply without a preserved source |
| Bake looks swollen | Cage/ray distance, scale, or low/high alignment is wrong rather than the sculpt itself |
| Skin pores shimmer in animation | Detail frequency exceeds sampling/texture/output capacity |
| Sculpt is good but rig fails | Retopology/deformation contract was missing; proceed through topology and rig validation |

## Authoritative anchors

- [Blender 5.2 Sculpting & Painting](https://docs.blender.org/manual/en/5.2/sculpt_paint/index.html)
- [Blender 5.2 Remeshing and Retopology](https://docs.blender.org/manual/en/5.2/modeling/meshes/retopology.html)
- [CMU Graphics courses](https://graphics.cs.cmu.edu/courses/) for evergreen meshing and surface principles
