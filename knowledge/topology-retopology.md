# Topology and retopology

## Scope

Use for edge flow, deformation topology, subdivision surfaces, cleanup, remeshing, normal/bake stability, game-ready meshes, and LODs.

## Topology is a contract

“Clean topology” means topology that satisfies a named operation. Define which of these matters:

- articulation and skin deformation;
- subdivision and smooth curvature;
- hard-surface shading and beveling;
- UV seams and texture baking;
- simulation or collision;
- manufacturing/manifold output;
- runtime triangle and vertex cost;
- morph targets or shape keys;
- exporter and target-engine constraints.

Quads are useful for loop editing, subdivision, and many deformation patterns. Triangles are the actual primitive for many runtimes and can be placed deliberately. N-gons can be efficient on stable planar surfaces but are risky when their triangulation, deformation, or shading is not controlled. Judge the result, not the polygon label.

## Deformation topology

- Allocate loops where curvature must change under pose.
- Orient flow around joints to support compression on one side and extension on the other.
- Keep poles away from the highest deformation and highlight-flow zones when possible.
- Give elbows, knees, shoulders, hips, mouth corners, eyelids, and fingers enough geometry for the required pose range—not a generic loop count.
- Test twist distribution, not only bending.
- Preserve volume with topology, weights, corrective shapes, or a deliberate combination.

Neutral-pose inspection cannot validate deformation. Use extreme but valid poses and the target skinning system.

## Subdivision topology

Control surface shape with edge spacing and continuity rather than dense support loops everywhere. Inspect:

- base cage silhouette;
- extraordinary vertices and pole valence;
- boundary behavior and creases;
- long thin faces or uneven aspect ratios;
- shrinkage around openings;
- modifier order relative to mirror, boolean, bevel, displacement, and armature.

If a surface pinches, isolate the base topology and subdivision result before adding normals or shading fixes. A normal modifier can hide a symptom without repairing the surface.

## Retopology method

1. Freeze or version the reference sculpt/scan and its transform.
2. Mark functional regions: deformation rings, openings, contacts, sharp transitions, material boundaries, and bake-critical silhouette.
3. Build large patches and loops before filling small gaps.
4. Use snapping/shrinkwrap with an offset that avoids z-fighting; check front and back of thin forms.
5. Maintain consistent but purpose-driven density. Add geometry where silhouette, deformation, or bake projection needs it.
6. Resolve poles in low-stress areas.
7. Test subdivision and deformation early, not after the whole mesh is filled.
8. Create UVs and a bake fixture using the actual target triangulation/tangent policy.

**[5.2]** Blender's automatic remesh tools are valuable for rebuilding density, but the Manual explicitly distinguishes them from manual retopology for animation-ready deformation.

## Cleanup and triangulation

Before delivery, inspect:

- duplicate and near-duplicate vertices;
- zero-area faces, loose elements, interior faces, non-manifold boundaries;
- inconsistent normals and custom split normals;
- material, UV, color, weight, and sharp-edge discontinuities;
- accidental disconnected islands;
- long thin triangles and unstable n-gon triangulation.

If the consumer triangulates differently, triangulate in Blender on the delivery copy before normal-map baking and export. Preserve the editable quad source separately.

## LOD design

LODs are not uniform decimation targets. Preserve:

- outer silhouette and major negative spaces;
- deformation joints and skinning behavior;
- UV/material boundaries needed by the target;
- shading edges and baked-normal consistency;
- attachment sockets and collision-relevant points.

Validate LOD transitions at actual screen coverage and motion. A static wireframe comparison is insufficient.

## Validation gates

- Topology purpose and consumer are named.
- Deformation passes representative extreme poses.
- Subdivision has no unacceptable pinching or shrinkage at delivery level.
- Normals, UVs, tangents, weights, and shape keys remain valid after final operations.
- Triangulation is deterministic at the bake/export boundary.
- Mesh statistics meet budget after modifiers, not only on the base cage.
- High/low bake shows no projection gaps, skew, or tangent discontinuity beyond acceptance thresholds.
- Consumer import preserves silhouette, normals, skeleton, and morphs as required.

## Failure signatures

| Symptom | Test |
| --- | --- |
| Shoulder collapses | Pose with arm elevation and twist; separate weights from missing support topology |
| Normal map seams appear | Compare UV split, smoothing split, tangent basis, and post-bake triangulation |
| Smooth viewport, faceted export | Inspect exported normals/tangents and consumer recomputation policy |
| Retopo shrinks away from sculpt | Inspect shrinkwrap direction/offset and cage subdivision separately |
| Decimated LOD pops | Compare silhouette and vertex positions at transition screen size |
| Manifold check fails | Identify whether openings are intentional before closing geometry |

## Authoritative anchors

- [Blender 5.2 Remeshing and Retopology](https://docs.blender.org/manual/en/5.2/modeling/meshes/retopology.html)
- [Blender 5.2 Modeling](https://docs.blender.org/manual/en/5.2/modeling/index.html)
- [CMU 15-462/662 description](https://15462.courses.cs.cmu.edu/spring2023/courseinfo)
