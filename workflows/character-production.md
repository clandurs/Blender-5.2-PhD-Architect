# Character production workflow

## Outcome

A character whose source sculpt/model, production topology, UVs/textures, materials, rig, animation, and delivery package are traceable and independently validated.

Read the modeling, sculpting, topology, UV, materials, rigging, animation, and pipeline modules as needed. Do not collapse all approval into “looks good in Blender.”

## Phase 0 — Character contract

Capture:

- concept/reference, style, proportions, sex/age/species where relevant, costume/gear boundaries;
- target cameras, close-up distance, poses, facial/hand requirements, and animation set;
- Blender 5.2 patch, target engine/renderer, unit/axes/facing, file format;
- triangle/vertex, influences, bones, morphs, material slots, textures, and memory budgets;
- modular clothing/equipment, body-under-clothes policy, and attachment sockets;
- LOD, collision, ragdoll, cloth/hair, and physics requirements;
- approval renders and consumer test.

Gate: no topology or rig architecture is finalized until the deformation and delivery contracts exist.

## Phase 1 — Design and primary form

1. Build a proportion/blockout model at target scale.
2. Establish silhouette, landmarks, mass, costume thickness, and major separations.
3. Test front/side/three-quarter and target camera views.
4. Test neutral pose plus representative extreme pose proxies.
5. Resolve hand/face/gear proportions before tertiary detail.

Evidence: turntable or agreed views, dimensions, scale/origin screenshot/data, known design exceptions.

Gate: approve primary/secondary form; tertiary detail cannot compensate for an unresolved silhouette.

## Phase 2 — High-resolution source

1. Choose voxel/dyntopo/multires/fixed topology deliberately.
2. Separate parts when clothing, equipment, bake control, or material ownership benefits.
3. Develop primary, secondary, then tertiary detail.
4. Preserve an immutable high source for baking.
5. Test thin parts, intersections, mouth/eyes, hands, joints, and hidden-body policy.

Evidence: high-source version, transform/dimension record, reference-aligned renders.

Gate: the accepted high source is frozen for the bake version; later changes create a new bake lineage.

## Phase 3 — Production topology

1. Mark deformation zones, facial loops, openings, gear contacts, and silhouette-critical regions.
2. Retopologize with purpose-driven density.
3. Establish target triangulation policy.
4. Test subdivision if used and bind a temporary rig for extreme-pose topology checks.
5. Create LOD strategy from silhouette/deformation needs, not uniform ratios.

Evidence: mesh statistics after delivery modifiers, wireframes, extreme poses, normals/manifold report.

Gate: topology passes deformation and silhouette before UV finalization.

## Phase 4 — UVs and bakes

1. Define texture sets/UDIMs/atlases, unique/overlap policy, density, and padding.
2. Unwrap and checker-test.
3. Freeze low triangulation, smoothing, and tangent basis.
4. Build cages or matched-part bake setup.
5. Bake normals, AO/curvature/ID/height only as required; record settings.
6. Test normal maps in the actual target renderer.

Evidence: high/low/cage versions, checker views, bake manifest, target-renderer test.

Gate: no texture painting on a UV/bake state likely to change without an explicit rework decision.

## Phase 5 — Materials and textures

1. Author color and data textures under the locked color contract.
2. Validate materials under neutral and target lighting.
3. Build Cycles/EEVEE/engine variants only when required.
4. Test skin, eyes, hair, cloth, metal, and transparency at grazing angles and target distance.
5. Profile shader/material-slot/texture memory.

Evidence: neutral-light lookdev, close/medium/distant views, channel/color-space manifest, target shader test.

## Phase 6 — Rig and deformation

1. Lock rest pose, bone roll/naming, deform skeleton, control architecture, and export skeleton.
2. Bind and refine weights across the required pose set.
3. Add twist distribution and correctives after base weights/topology pass.
4. Test clothing/gear attachments and body intersections.
5. Validate controls, IK/FK, spaces, scale, drivers, and performance.

Evidence: rig version, pose matrix, deformation review, influence/bone checks, clean export skeleton.

Gate: rig approval is separate from animation and consumer import.

## Phase 7 — Animation and dynamics

1. Define actions, ranges, root motion, loop convention, and transition needs.
2. Block, refine, and polish representative clips.
3. Test two-cycle loops, contacts, foot slide, and extreme deformation.
4. Add cloth/hair secondary motion only after base motion passes.
5. Bake supported delivery channels on a copy.

Evidence: action manifest, viewport review, rendered representative frames, baked comparison.

## Phase 8 — Delivery and consumer validation

1. Generate a clean delivery copy from the accepted source versions.
2. Apply only authorized export conversions.
3. Export with recorded settings and checksums.
4. Independently inspect/re-import.
5. Validate in the actual consumer: scale, facing, skeleton, materials, textures, morphs, clips, root motion, LODs, sockets, and runtime performance.

Final report: exact versions, source/publish lineage, what passed, what remains consumer-specific, and rollback path.

## Stop conditions

Stop and surface a decision when the user must choose a rest pose, destructive topology/UV change, new external dependency, experimental physics, incompatible target limitation, or a material budget change. Do not silently trade deformation, likeness, or target compatibility for speed.
