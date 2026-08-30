# Debugging playbook

## Purpose

Produce a reproducible diagnosis and the smallest validated correction without destroying evidence or unrelated production state.

## 1. Freeze evidence

Before changing anything:

- copy/preserve the original `.blend`, autosave candidates, external dependencies, caches, crash logs, console output, and failing render/export;
- record exact Blender patch, OS, GPU/driver, device/backend, extensions, file revision, scene/view layer/frame/mode/engine;
- write expected versus observed behavior and exact reproduction steps;
- note whether opening the file requires trusted scripts.

If the file is untrusted, keep auto-execution disabled. Do not run embedded scripts merely to reproduce a visual symptom.

## 2. Reproduce and bound

Answer:

- Every time or intermittent?
- One frame or range?
- One object/material/action/view layer/engine/device or all?
- Viewport, final render, export, importer, or target consumer?
- Existing file only or minimal scene?
- First bad version/revision?

Create a diagnostic copy. Change one dimension at a time and log the result.

## 3. Select a branch

### Invisible or wrong object

Check scene/view layer/collection/local view, viewport/render visibility, frame/animation, transforms/scale/clipping, material alpha/holdout, modifier/node output, library/override dependency, then target export visibility.

### Geometry or shading corruption

Check base mesh, normals, transforms, modifier order, evaluated mesh, triangulation, UV/tangent, material normal/displacement, then exporter/consumer recomputation.

### Rig or animation failure

Check rest pose/roll/hierarchy, owner/target spaces, constraints/drivers, action slot/NLA/time, IK/FK, evaluated matrices, bake/export range, then consumer skeleton/root policy.

### Simulation failure

Check scale/time base, initial intersections, solver input topology/modifier order, substeps/collision, cache lineage/range, seed/version, then render representation.

### Render failure or mismatch

Check active camera/scene/view layer/frame, engine/device, visibility, lights/world/material output, samples/paths/EEVEE limitation, memory/log, passes/color/output path, then external viewer.

### Python/add-on failure

Use the first traceback. Check version, registration, `poll`/context/mode, stale RNA references, background support, handlers/timers/threads, file paths/encoding, then minimal fixture.

### Crash/freeze

Preserve crash log. Compare factory-startup isolated preferences, add-ons disabled, CPU/GPU or supported backend, reduced data class, clean file with appended subsets, and exact patch. Monitor RAM/VRAM.

### Export mismatch

Compare authoring data, evaluated delivery copy, exporter settings/serialized file, independent import, and actual consumer using a tiny contract fixture.

## 4. Form falsifiable hypotheses

Write each as:

> If **cause** is responsible, then changing **one variable** should produce **observable result** while other conditions stay fixed.

Rank by evidence and cost. Run the cheapest discriminating test, not the easiest random tweak.

## 5. Minimize

On a diagnostic copy:

- delete/isolate half the suspect objects/collections at a time;
- mute half the modifier/node/constraint chain;
- replace materials with constants;
- reduce frame range/resolution/samples/solver density;
- append only the suspect asset to a clean file;
- replace external dependencies with known fixtures.

Binary isolation is for diagnosis, not a production fix. Keep notes so the minimum reproducer retains the failure.

## 6. Correct at the cause

Design the smallest change that explains why it works. Preserve source and rollback. Avoid applying modifiers, clearing caches, resetting preferences, reinstalling, or deleting data unless the diagnosis specifically requires it and the target is exact.

## 7. Validate

- original reproduction no longer fails;
- minimal reproducer passes;
- adjacent operations and representative frames pass;
- output boundary matches the claim: viewport, render, export, or consumer;
- performance/memory is not materially regressed;
- reopen/restart/re-run works when relevant;
- logs contain no new first-order errors.

## 8. Report

Use this compact format:

```text
Result: fixed / probable cause / blocked
Environment: Blender patch, OS, device, file revision
Symptom: expected vs observed
Root cause: evidence and discriminating test
Change: exact scoped correction
Validation: tests and outputs
Unchanged: protected scope
Remaining risk: untested boundaries
Rollback: preserved source/version
```

## Escalation package

For a Blender bug report or source investigation, provide a minimal `.blend`/script, exact steps, exact version/build, system info, crash/debug log, expected/actual result, and regression range if known. Remove private data and secrets. Confirm the minimal file still reproduces before sharing.
