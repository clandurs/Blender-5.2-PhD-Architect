# Simulations

## Scope

Use for rigid body, cloth, soft body, fluid/smoke/fire/liquid, particles, dynamic hair, force fields, collision, and Geometry Nodes simulations.

## Simulation contract

Record:

- solver and Blender exact patch version;
- unit scale, gravity, frame rate, time scale, start state, warm-up, and frame range;
- topology and modifier state presented to the solver;
- collision geometry, margins/thickness, substeps, iterations, and material parameters;
- determinism/repeatability requirement and seed;
- cache directory, cache name, storage mode, version, owner, and invalidation rules;
- target fidelity, render representation, and bake budget.

Simulation settings are dimensional. A cloth preset or collision margin is meaningless without scale, topology density, and time step.

## General method

1. Work on a versioned scene and save it before disk caching.
2. Reduce to one emitter/dynamic object, one collider, and a short frame range.
3. Fix initial intersections and unapplied/inconsistent transforms.
4. Establish stable coarse behavior before increasing resolution, substeps, particles, or secondary effects.
5. Add modifiers in deliberate evaluation order. Confirm whether the solver sees the base or deformed mesh.
6. Name caches when more than one cache/system can exist on an object.
7. Clear or version a cache whenever a dependency changes; never trust a stale preview.
8. Bake the final range, then validate representative and boundary frames.

**[5.2]** Blender's general bake system protects baked settings until the bake is freed. Clearing/freeing is destructive to cached results; preserve the accepted bake or cache directory before doing it.

## Solver-specific diagnosis

### Cloth and soft bodies

- Use mesh density and edge structure appropriate to bending/stretching behavior.
- Eliminate initial penetrations and inspect collision thickness relative to scale.
- Place subdivision/smoothing after simulation when the intent is to smooth the solved surface; pre-solver subdivision changes the physical system and cost.
- Test fast motion with higher quality/substeps only after confirming scale and collision path.

### Rigid bodies

- Use simple, closed collision shapes where possible.
- Distinguish visual mesh from collision mesh.
- Check mass ratios, origin, center of mass, scale, deactivation, and constraint frames.
- A tunneling object may need continuous collision/substeps or a better collider, not merely more visual geometry.

### Fluids, smoke, and fire

- Domain bounds and voxel resolution dominate memory and detail.
- Validate source/flow behavior at coarse resolution.
- Treat adaptive domain, noise, mesh, and particles as separate cost/quality stages.
- Record cache type and directory; moving the blend-file can break relative cache assumptions.

### Hair and particles

- Separate guide/control density from render child/interpolated density.
- Validate surface attachment, rest pose, collisions, and grooming before increasing render density.
- Inspect temporal stability and root motion.

### Geometry Nodes dynamics

**[Experimental][5.2]** The new Geometry Nodes cloth/hair systems are experimental. Lock the patch release, bake/freeze accepted output, and keep a fallback. General simulation-zone systems still require explicit state, ID, frame, cache, and invalidation reasoning.

## Determinism and caches

A cached result is evidence only when lineage is known. Record:

- scene/version hash or revision;
- solver settings and relevant object dependencies;
- start/end, seed, cache index/name, and directory;
- whether the cache is replay, modular, all/final, in-memory, disk, or packed;
- completion status and validation frames.

Do not overwrite an accepted cache with a test bake. Use versioned directories or immutable publishes.

## Validation gates

- Scale, time base, gravity, start state, and transforms match the contract.
- No initial intersections or unintended open/non-manifold collision surfaces.
- Coarse solve is stable before high-resolution features.
- The solver receives the intended modifier/topology state.
- Cache lineage, name, range, and completion are recorded.
- Reopen/replay or clean-session bake reproduces the accepted result where determinism is required.
- Boundary frames and fast-motion/contact events are inspected.
- Render geometry/material/volume matches the cache, not a stale viewport state.
- Experimental output is frozen and has a fallback.

## Failure signatures

| Symptom | Test |
| --- | --- |
| Explodes on frame one | Check initial overlap, scale, normals, extreme stiffness, and time step |
| Looks different after changing an unrelated setting | Cache was invalidated/stale or dependency graph changed |
| Fast object passes through collider | Test substeps, collision thickness, speed, and collider simplicity |
| Fluid detail never improves | Confirm domain resolution and that mesh/noise stage was actually rebaked |
| Bake button unavailable/settings locked | Existing bake must be preserved or freed deliberately |
| Two caches overwrite each other | Name caches and isolate storage paths |

## Authoritative anchors

- [Blender 5.2 Physics](https://docs.blender.org/manual/en/5.2/physics/index.html)
- [Blender 5.2 Baking Physics Simulations](https://docs.blender.org/manual/en/5.2/physics/baking.html)
- [Blender 5.2 Physics release notes](https://developer.blender.org/docs/release_notes/5.2/physics/)
- [CMU Graphics courses](https://graphics.cs.cmu.edu/courses/) for evergreen numerical and physically based animation principles
