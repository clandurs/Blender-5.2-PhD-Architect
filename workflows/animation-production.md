# Animation production workflow

## Outcome

A shot or reusable clip with a locked time/camera/rig contract, approved motion, controlled secondary simulation, and validated render or engine delivery.

## Phase 0 — Intake

Capture:

- brief, performance reference, dialogue/audio, shot/clip purpose;
- exact rig/model/material versions and compatibility;
- frame rate, start/end, handles, resolution, camera, and output;
- root motion, loop, contact, transition, and consumer requirements;
- simulation, facial, lip-sync, prop, and crowd dependencies;
- review stages and final acceptance evidence.

Run a rig preflight: rest pose, controls, spaces, IK/FK, deformation extremes, scale, action ownership, drivers, and viewport performance. Do not animate a rig whose delivery skeleton or control behavior is still undefined unless the risk is accepted.

## Phase 1 — Layout and staging

1. Establish camera, screen direction, eyelines, character/prop positions, and broad timing.
2. Use proxy assets when final assets are not needed for staging.
3. Check silhouette, composition, cut continuity, and physical reach/contact.
4. Lock or version the camera before detailed polish.

Evidence: playblast/layout render with frame burn-in and exact versions.

Gate: staging, camera, shot length, and key beats are approved.

## Phase 2 — Blocking

1. Create key storytelling/gameplay poses and contact frames.
2. Keep interpolation controlled so review reads pose/timing rather than accidental splines.
3. Check balance, line of action, arcs, gaze, prop contact, and silhouette.
4. For loops, establish boundary pose/root policy now.

Evidence: blocking playblast at real frame rate and target camera.

Gate: performance intent and timing are accepted before spline/polish.

## Phase 3 — Spline/refinement

1. Convert/refine interpolation deliberately.
2. Fix world-space trajectories, spacing, and contacts before secondary overlap.
3. Inspect Graph Editor and motion paths, but judge through the camera at speed.
4. Match IK/FK and space switches without pops.
5. Keep curve/key density appropriate for authoring; do not bake yet.

Evidence: spline playblast plus focused contact/arc checks.

## Phase 4 — Polish

- refine overlap, settle, fingers, face, eye direction, breathing, and microtiming;
- remove curve overshoot and contact slide;
- test deformation at extreme frames and repair weights/correctives in the proper asset version;
- for loops, inspect two consecutive cycles and consumer end-frame convention;
- review motion blur/DOF on representative rendered frames.

Gate: base animation passes before simulations are used to conceal or enhance it.

## Phase 5 — Secondary dynamics

1. Lock the driving animation version.
2. Establish scale, collisions, warm-up, solver settings, and cache lineage.
3. Run coarse tests, then final bake.
4. Preserve accepted cache and inspect contact/fast-motion/boundary frames.
5. For experimental 5.2 Geometry Nodes physics, lock the patch and create a frozen fallback.

Evidence: cache manifest, bake completion, representative render/playblast.

## Phase 6 — Bake and delivery

For engine/format delivery:

1. Duplicate to a delivery scene/copy.
2. Bake evaluated object/bone/property motion over exact range/sample rate.
3. Remove unsupported rig mechanisms only from delivery copy.
4. Enforce action naming, root policy, skeleton, morph, and influence limits.
5. Export and test in the actual consumer.

For rendered shots:

1. Lock assets, caches, camera, lighting, color, passes, and output path.
2. Render representative hard frames.
3. Render a recoverable image sequence.
4. Composite, review, and encode after sequence validation.

## Final gates

- Correct rig/camera/audio/asset versions.
- Motion reads at speed and target view.
- Contacts, arcs, deformation, loops, and root motion pass.
- Dynamics cache is versioned and reproducible/frozen.
- Baked/exported motion matches authoring within tolerance.
- Consumer or final-render output—not only Blender viewport—passes.

## Stop conditions

Stop when a camera or timing change invalidates approved polish, a rig revision breaks animation, an experimental solver has no fallback, or delivery constraints require destructive rebaking. Surface the rework scope before proceeding.
