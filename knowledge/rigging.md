# Rigging

## Scope

Use for armature architecture, controls, constraints, IK/FK, skinning, corrective deformation, drivers, retargeting, and export skeletons.

## Define the rig contract

Record before building:

- character/prop purpose, pose range, required controls, and animator skill level;
- exact rest pose, world scale, object transforms, origin, axes, and facing direction;
- deformation skeleton versus control/mechanism bones;
- naming, side tokens, hierarchy, bone roll, and collection organization;
- target consumer, supported constraints, influence limit, root motion, and animation format;
- shape-key/corrective policy and whether the rig must survive link/override workflows;
- performance budget in viewport and target runtime.

A Blender rig can be excellent for animation and still be unsuitable for export. Design the authoring rig and delivery skeleton as related but distinct systems.

## Architecture

Separate responsibilities:

- **Deform bones:** stable hierarchy and names, minimal set, exportable transforms.
- **Controls:** animator-facing shapes and channels, ergonomic selection, meaningful spaces.
- **Mechanism bones:** constraints, pivots, roll extraction, twist distribution, stretch, and helper math.
- **Correctives:** pose-space deformation or shape keys for residual volume/form errors.

Do not expose implementation channels to animators unless needed. Lock or hide channels that create invalid states, but preserve a documented method to inspect the underlying system.

## Coordinate and roll discipline

Bone local axes and roll affect constraints, mirroring, twist, and export. Establish roll conventions before weighting. Inspect local axes in bent and mirrored chains. A visually aligned bone can still have incompatible local axes.

Apply object-level transforms only after checking existing animation, children, constraints, and mesh binding. Keep armature and mesh scale coherent. Inconsistent scale can appear as constraint drift, exporter scale multiplication, or physics instability.

## IK/FK and spaces

- Define which chains need IK, FK, stretch, pole targets, pinning, and space switching.
- Match IK and FK at the transform level, including scale and roll, not just visible position.
- Make pole placement stable through the expected range; near-collinear chains are numerically ambiguous.
- Specify whether space switches preserve world pose and how keys are inserted.
- Test parent, world, root, chest, head, prop, and custom spaces with animation already present.

Constraint order and influence are evaluation logic. When diagnosing, mute constraints one at a time and inspect the dependency path rather than moving constraints randomly.

## Skinning

Start with automatic or envelope weights only as initialization. Then validate:

- normalized weights and intended non-deforming vertices;
- maximum influences required by the target;
- shoulder/hip elevation, elbow/knee compression, wrist/ankle bend, forearm twist, neck/jaw, fingers, and contact areas;
- Preserve Volume behavior where appropriate;
- twist-bone distribution and skin sliding;
- topology density and loop flow, not weights alone.

Use corrective shapes after base topology and weights are sound. Correctives should address pose-specific residual error, not conceal a broken hierarchy or wrong rest pose.

## Drivers and dependencies

Treat driver expressions as executable logic and document every custom property, variable, space, and range. Avoid name-fragile paths when stable references are possible. Test dependency cycles and library override behavior.

Untrusted rigs can contain Python drivers or scripts. Follow the script security policy before enabling execution.

## Export and retargeting

For delivery:

1. Duplicate or derive a clean export skeleton.
2. Map authoring controls to deform-bone transforms.
3. Bake evaluated transforms over the exact frame range and sample rate required.
4. Remove unsupported constraints, control shapes, and mechanism data only from the delivery copy.
5. Enforce target influence limits and bone/vertex budgets.
6. Export and validate in the actual consumer.

Retargeting requires a declared source/target rest-pose relationship, bone map, scale, root policy, and rotation handling. Similar bone names are insufficient.

## 5.2 notes

**[5.2]** The animation/rigging release notes document pose-library behavior when source and target rotation modes differ. Do not assume a pose authored in one Euler order carries its original order metadata into every conversion.

**[5.2]** Animation and armature operators changed in 5.2, but these workflow conveniences do not alter the fundamental need to validate hierarchy, local axes, constraints, and deformation.

## Validation gates

- Rest pose, scale, axes, hierarchy, bone roll, and naming match the contract.
- Controls are understandable, channels are intentional, and space switches preserve pose where promised.
- IK/FK matching passes at multiple poses and non-default scales if supported.
- Extreme-pose deformation passes silhouette, volume, intersection, and contact checks.
- No unexpected dependency cycles, missing driver paths, or override failures.
- Export copy contains only intended bones and baked channels.
- Consumer import preserves hierarchy, transforms, skinning, root motion, and clips.
- Rig performance is measured on a representative shot, not an empty scene.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Limb flips | Inspect pole alignment, chain collinearity, local axes, and IK limits |
| Mirrored side twists differently | Compare bone roll and constraint spaces, not just mirrored positions |
| Mesh collapses at 180° twist | Compare weight distribution, twist bones, and volume-preserving skinning |
| Constraint works until parent changes | Inspect owner/target spaces and dependency order |
| Export bones are rotated/scaled | Compare rest pose, object transforms, exporter axis conversion, and baked result |
| Pose asset changes unexpectedly | Check source/target rotation modes and Euler order conversion |

## Authoritative anchors

- [Blender 5.2 Animation & Rigging](https://docs.blender.org/manual/en/5.2/animation/index.html)
- [Blender 5.2 Animation & Rigging release notes](https://developer.blender.org/docs/release_notes/5.2/animation_rigging/)
- [Blender 5.2 Scripting & Security](https://docs.blender.org/manual/en/5.2/advanced/scripting/security.html)
- [CMU 15-462/662](https://15462.courses.cs.cmu.edu/spring2023/courseinfo) for evergreen kinematics and animation principles
