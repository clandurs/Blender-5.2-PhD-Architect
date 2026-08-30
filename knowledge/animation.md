# Animation

## Scope

Use for keyframing, F-Curves, actions, action slots, NLA, drivers, shape-key animation, loops, root motion, baking, timing, and delivery clips.

## Animation contract

Define:

- frame rate, time base, frame range, handles, pre/post-roll, and output cadence;
- shot animation versus reusable clip;
- root motion and in-place policy;
- object/bone/property channels that are authoritative;
- rotation modes and interpolation requirements;
- loop, contact, trajectory, and transition constraints;
- target engine/exporter sampling and compression;
- approval views and representative render frames.

Changing frame rate after animation changes the relationship between frames and time. Treat it as a retiming operation, not a harmless scene setting.

## Pose-to-motion workflow

1. Establish staging, camera, and key story/gameplay beats.
2. Block poses and contact frames with stepped or deliberately simple interpolation.
3. Check silhouette, balance, line of action, gaze, prop contact, and screen direction.
4. Refine spacing and arcs in world and local space.
5. Polish overlap, settle, facial/finger detail, and secondary motion only after timing holds.
6. Validate at playback speed and through target camera; curve-editor beauty does not guarantee readable motion.

Use motion paths and trajectory plots to expose discontinuities. A smooth F-Curve can still produce a poor spatial arc because transforms compose through a hierarchy.

## F-Curves and interpolation

- Use Bezier handles for controlled easing, linear for constant parameter rate, and constant for holds/blocking.
- Inspect overshoot and handle coupling on contacts, mechanical limits, and loop boundaries.
- Choose Euler or quaternion rotation based on control needs and interpolation behavior. Record Euler order when used.
- Avoid gratuitous keys. Dense baking is appropriate at a delivery boundary, not as the default authoring form.
- When cleaning curves, compare motion in world space and preserve contacts; numerical simplification can introduce visible sliding.

## Actions, slots, and NLA

Treat actions as named animation data with ownership and range, not as an informal storage bin.

- Declare which data-block and slot an action targets.
- Give clips explicit start/end, cycle behavior, root policy, and required rig version.
- Use NLA for composition, blending, repetition, and non-destructive sequencing; inspect strip time, influence, blend mode, extrapolation, and action range separately.
- Do not push action data into NLA or stash it without confirming where the active editable animation now lives.
- Preserve an authoring copy before baking NLA/constraints to delivery keys.

## Loops and transitions

For a seamless loop:

- compare pose and derivatives at the boundary, not only first/last values;
- account for cyclic modifiers, duplicated terminal frames, and the consumer's inclusive/exclusive frame convention;
- verify root displacement and heading;
- render at least two consecutive cycles to expose a wrap discontinuity;
- inspect secondary motion, particles, cloth, and animated shaders across the seam.

An animation that loops in Blender's playback can still contain a duplicated export frame or non-looping simulation.

## Constraints, drivers, and baking

When motion comes from constraints, drivers, parenting, motion paths, or procedural systems, the visible transform may differ from keyed channels. Bake the evaluated result on a delivery copy when the consumer does not reproduce the dependency graph.

Record sample rate, visual keying, clear-constraints policy, object/bone space, and curve simplification. Compare pre/post bake at representative frames and contacts.

## 5.2 notes

**[5.2]** Playback loop modes were expanded in Blender 5.2. They control interactive playback behavior, not the mathematical contents of an action or exported clip. Do not cite a successful Bounce/Stop playback as evidence of a valid delivery loop.

**[5.2]** The 5.2 release notes describe pose and Graph Editor behavior changes. Recheck automation that invokes renamed/new operators or assumes defaults.

## Validation gates

- Frame rate, ranges, handles, and clip naming match the delivery contract.
- Blocking and final motion read through the target camera and at real-time playback.
- Contacts do not slide beyond tolerance; arcs and spacing remain intentional.
- No unintended F-Curve overshoot, discontinuity, or unkeyed dependency.
- Loops pass two-cycle playback and export/import boundary checks.
- Constraint/driver/NLA result matches baked delivery within tolerance.
- Root motion, scale, rotation modes, and interpolation survive the target consumer.
- Representative rendered frames and motion blur are evaluated, not only viewport playback.

## Failure signatures

| Symptom | Test |
| --- | --- |
| Foot slides despite fixed keys | Inspect world-space foot motion, parent/root motion, IK influence, and curve handles |
| Rotation takes long path | Compare Euler order, quaternion interpolation, and angle wrapping |
| NLA clip changes timing | Inspect action range, strip scale/repeat, scene time, and extrapolation |
| Loop pops only after export | Compare inclusive end-frame convention and duplicate terminal key |
| Baked motion drifts | Increase sample rate, inspect constraint spaces, and compare evaluated matrices |
| Playback drops frames | Distinguish display performance from actual frame timing/render output |

## Authoritative anchors

- [Blender 5.2 Animation & Rigging](https://docs.blender.org/manual/en/5.2/animation/index.html)
- [Blender 5.2 Animation & Rigging release notes](https://developer.blender.org/docs/release_notes/5.2/animation_rigging/)
- [MIT 6.837 Computer Graphics](https://ocw.mit.edu/courses/6-837-computer-graphics-fall-2012/) for evergreen animation and transformation principles
