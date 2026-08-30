# Cinematic production workflow

## Outcome

A versioned cinematic shot/sequence from brief through edit, assets, animation, effects, lighting, render, composite, sound handoff, and final encoded delivery.

## Phase 0 — Delivery and creative contract

Define:

- narrative beat, duration, audience, framing/aspect, resolution, frame rate, and audio time base;
- visual language, reference, camera/lens policy, color pipeline, and delivery codec/container;
- shot list/edit ownership, handles, naming, and review cadence;
- asset/character/environment needs and reuse;
- simulation/VFX requirements;
- render engine, passes, hardware/farm, storage, and schedule;
- acceptance evidence and archival package.

Gate: time base, aspect, color, naming, shot structure, and final delivery requirements are locked before expensive final work.

## Phase 1 — Storyboard, animatic, and edit

1. Translate the brief into shots and beats.
2. Build storyboard/Grease Pencil/rough 3D panels.
3. Assemble animatic with audio/reference timing.
4. Validate continuity, screen direction, pacing, composition, and total duration.
5. Assign shot IDs and handle ranges.

Evidence: versioned animatic and shot manifest.

Gate: edit/shot durations are approved; later timing changes carry explicit rework impact.

## Phase 2 — Layout and cameras

1. Assemble proxy environments/characters.
2. Lock scene scale, camera projection/lens/sensor, aspect, safe areas, and movement.
3. Validate parallax, eyelines, staging, and transitions in sequence.
4. Use motion tracking/solve workflow for plates and verify across depth.
5. Publish camera/layout per shot.

Gate: camera/layout approval precedes detailed animation, simulation, and final lighting.

## Phase 3 — Asset production and look development

- build/publish only assets required by shot coverage;
- validate character/environment workflows independently;
- establish neutral lookdev, material library, texture/color-space rules, and hero detail;
- test Cycles/EEVEE feature requirements early;
- define asset version update and shot override policy.

Evidence: shot asset manifest and approved lookdev frames.

## Phase 4 — Animation and effects

1. Block, spline, and polish to approved camera/edit.
2. Lock animation driving simulations.
3. Run coarse then final cloth/hair/fluid/particle/Geometry Nodes effects.
4. Preserve cache lineage and experimental fallbacks.
5. Validate silhouettes, contacts, timing, and temporal stability through shots/cuts.

Gate: animation and effects pass before final rendering.

## Phase 5 — Lighting

1. Establish sequence lighting continuity and shot-specific hierarchy.
2. Match plates where applicable.
3. Test representative hard frames under final materials and color management.
4. Configure view layers/passes/AOVs and holdouts/light links deliberately.
5. Profile render time, memory, and noise; optimize by measured cause.

Evidence: approved lighting frames, render settings/version, pass test.

## Phase 6 — Render

1. Lock scene, camera, assets, caches, engine, device, samples, color, passes, and output path.
2. Render a small final-quality wedge/crop and representative frame set.
3. Render versioned image sequences with logs and restartability.
4. Validate completeness, stale/mixed frames, bit depth, channels, alpha, and color.
5. Preserve raw scene-linear render outputs.

A completed render process is not visual acceptance. Review the pixels.

## Phase 7 — Composite and delivery

1. Ingest under the locked color/alpha contract.
2. Integrate passes/plates, grade, grain, defocus, distortion, and effects.
3. Review over multiple backgrounds when alpha matters.
4. Validate frame sequence and shot edit.
5. Encode/mux final video/audio after image-sequence approval.
6. Inspect final container metadata, frame rate, duration, audio sync, resolution, color, and playback.

## Archive

Archive manifests, exact Blender/extension versions, OCIO config, assets, cameras, scenes, caches or regeneration instructions, raw renders, composites, final delivery, logs, and checksums. Record which derived data can be safely regenerated.

## Stop conditions

Stop for a decision when edit/camera/color/time base changes, a missing asset threatens the shot, experimental effects lack fallback, render budget requires visible compromise, or final delivery terms conflict with the approved master.
