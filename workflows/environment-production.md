# Environment production workflow

## Outcome

A scalable environment assembled from measured modules, reusable assets, materials, procedural systems, lighting, collision, LODs, and delivery data with reproducible performance.

## Phase 0 — Environment contract

Define:

- gameplay/cinematic/visualization purpose and target camera/player metrics;
- world scale, grid/module dimensions, origin/streaming partition, axes, and bounds;
- art direction, biome/era, composition landmarks, traversal and sightlines;
- target renderer/engine, lighting model, time/weather variants;
- triangle, object, draw-call, material, texture, shader, memory, and load budgets;
- collision, navigation, interaction, destruction, and physics requirements;
- procedural versus hand-authored ownership and deterministic seed policy.

Gate: scale, modular grid, camera/traversal metrics, and delivery budgets are approved before kit production.

## Phase 1 — Blockout and composition

1. Create a simple measured blockout.
2. Validate traversal widths, heights, cover/sightlines, camera composition, and landmark hierarchy.
3. Test perspective and scale with human/player/camera proxies.
4. Define streaming/shot/collection boundaries and coordinate-origin policy.
5. Review from target views and movement paths.

Evidence: dimensions, overview, target camera/path captures, blockout version.

## Phase 2 — Kit and asset taxonomy

Build an inventory:

- structural modules, trims, transitions, corners, caps, doors/windows;
- hero props, mid-frequency props, scatter/debris, decals, foliage;
- terrain/cliffs/water/volumes;
- collision and proxy assets;
- material/trim/decal libraries.

For each kit, define pivot, dimensions, snap points, naming, UV/material strategy, variants, LODs, and collision. Test a small assembly for seams, repetition, rotation, and negative-space coverage before producing the full kit.

Gate: kit proof assembles the intended spaces without scale drift or unfillable seams.

## Phase 3 — Asset production

1. Model source assets with deliberate modifier/procedural architecture.
2. Preserve silhouette at intended distances.
3. Use trim/tiling/atlas/unique textures according to the material contract.
4. Create collision and LODs from functional needs.
5. Publish assets independently before broad scene assembly.

Evidence: per-asset manifest, geometry statistics, UV/material checks, LOD/collision test.

## Phase 4 — Procedural population

1. Define inputs, exclusions, density, scale, orientation, biome/material rules, and stable IDs.
2. Keep instances until realization is required.
3. Separate artist masks from generated results.
4. Add camera/distance/region culling only when target behavior is defined.
5. Profile representative worst-case regions.
6. Lock Blender 5.2-specific Geometry Nodes features and provide baked/export fallback.

Evidence: node-group interface/version, seed, counts, memory/evaluation timing, diagnostic views.

Gate: system is deterministic under permitted upstream edits and stays within budgets.

## Phase 5 — Materials, lighting, and atmosphere

1. Establish color management and neutral lookdev.
2. Build scalable tiling/trim/decal materials; verify real-world scale and color/data inputs.
3. Define primary light/weather/time states.
4. Add fog/volumes, practicals, reflection/probe strategy, and grading only after base lighting holds.
5. Test interior/exterior transitions, camera-edge EEVEE behavior, and Cycles convergence where relevant.

Evidence: material library version, lighting state renders, exposure/color record, performance.

## Phase 6 — Scene optimization

- measure object/dependency cost, evaluated geometry, instances, materials, textures, VRAM/RAM, render time, and load/save;
- establish viewport/final quality tiers;
- consolidate only where it improves target metrics without destroying ownership or culling;
- validate occlusion/streaming partitions in the actual consumer;
- inspect heavy frames/regions, not an empty overview.

## Phase 7 — Delivery

1. Publish versioned asset library and environment assembly.
2. Validate missing paths, linked/override dependencies, color config, Geometry Nodes assets, and caches.
3. Build delivery packages by partition with manifests/checksums.
4. Test clean import/load in the actual consumer.
5. Walk/fly/render target paths and verify collision, LODs, seams, materials, lighting, performance, and origin behavior.

## Stop conditions

Stop for an owner decision when a kit metric changes, a hero asset breaks budget, procedural realization changes editability, a new format loses required features, or optimization would alter composition/quality outside the accepted tolerance.
