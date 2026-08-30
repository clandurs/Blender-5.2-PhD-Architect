# Troubleshooting

## Scope

Use for incorrect scene behavior, UI/display issues, render failures, crashes, corrupt or missing data, Python/add-on failures, performance regressions, and interchange mismatches. For the executable procedure, also read `../workflows/debugging-playbook.md`.

## Evidence-first diagnosis

Start with an exact symptom:

- What was expected?
- What was observed?
- Which Blender patch, OS, hardware/driver, file revision, frame, scene, view layer, engine, mode, and action reproduce it?
- Is it deterministic?
- What changed last?
- Does it occur in a minimal scene or only this file?

Preserve the original file, crash logs, console output, screenshots/renders, and reproducible steps before resetting preferences, deleting caches, applying modifiers, or resaving.

## Classify the layer

| Layer | Examples | First distinctions |
| --- | --- | --- |
| Data | missing object, wrong UV, corrupt path | Outliner/data-blocks, ownership, file paths, attributes |
| Evaluation | modifier/constraint/driver/node wrong | stack/order, dependency graph, frame, mode, context |
| Display | invisible/glitched viewport | overlays, clipping, shading mode, local view, GPU/driver |
| Render | black/noisy/different output | engine, visibility, lights, passes, device, color, output |
| Automation | operator/API/add-on error | version, context, registration, stale RNA references, background mode |
| Interchange | export/import mismatch | serialized subset, axes/units, triangulation, materials, skeleton, consumer |
| Resource | crash/freeze/out-of-memory | RAM/VRAM, driver, scene density, cache, recursion, external process |

Do not cross layers prematurely. A viewport screenshot cannot prove export data; a re-import cannot prove target-engine behavior.

## Isolation ladder

Use the least destructive step that distinguishes hypotheses:

1. Reproduce in the preserved file and record exact steps.
2. Save a diagnostic copy.
3. Change one variable: frame, mode, engine, device, visibility group, modifier, add-on, or output.
4. Test a minimal scene or append only the suspected asset into a clean file.
5. Start with factory settings/temporary isolated preferences without overwriting the user's configuration.
6. Compare CPU/GPU or alternative supported backend for GPU/render symptoms.
7. Test another exact Blender patch only when compatibility/regression is a hypothesis; never resave the only copy.
8. Inspect release/compatibility notes, known bugs, logs, and source paths when needed.

Track each test, result, and eliminated hypothesis. Random changes destroy diagnostic information.

## Crash and recovery

**[5.2]** Common crash categories include memory exhaustion, graphics hardware/driver problems, Blender bugs, Python misuse, and problematic files.

Recovery order:

1. Preserve original, autosave/recovery candidates, and crash log.
2. Duplicate before opening in another patch or using recovery tools.
3. Try factory-startup or official debug launchers in an isolated diagnostic run.
4. If file-specific, append/link small groups into a clean file to isolate the offending data.
5. If GPU-specific, collect driver/system info and compare supported backend/CPU paths.
6. If Python-specific, use fault handler/logs and inspect stale data references, threading, handlers, and recent mutations.

Do not repeatedly open/save a suspected corrupt file over itself.

## Missing or invisible data

Check in order:

- correct scene, view layer, collection, local view, hide/disable/render visibility;
- object existence and data-block link/user count;
- frame, action, driver, constraint, and transform;
- clipping, scale, origin, camera, and world position;
- material alpha/holdout and render visibility;
- dependency/library availability and override state;
- geometry generated only at evaluation/render time.

## Render failure

Capture console/log output and inspect:

- active camera, scene, view layer, engine, device, frame, and output path;
- lights/world, render visibility, holdouts, collections, and material output;
- memory/device errors, unsupported shader/EEVEE feature, and missing textures;
- color/view transform when the pixels exist but appear wrong;
- File Output versus scene output behavior;
- command-line argument order in automation.

## Python/add-on failure

- confirm exact 5.2 API and extension version;
- check console traceback from first error, not cascading errors;
- inspect operator `poll`, context, mode, active data, and background support;
- re-fetch RNA collections after mode/data reallocation;
- test clean preferences with only the suspect add-on;
- verify symmetric register/unregister and removal of handlers/timers/keymaps;
- do not enable untrusted code to “see if it fixes it.”

## Interchange failure

Build a tiny contract fixture containing one known mesh, material, skeleton/clip, camera/light if supported, and named attributes. Compare:

1. Blender authoring data.
2. Evaluated delivery copy.
3. Exported file contents/options.
4. Independent importer result.
5. Actual target consumer.

This locates whether the loss occurs before export, in serialization, in import, or in runtime interpretation.

## When to inspect Blender source

For a reproducible undocumented behavior, use the Developer Documentation to locate the operator/UI property, source module, DNA/RNA definition, or test. Source inspection can explain implementation but does not replace a user-visible reproduction. If contributing a fix, build the correct branch and run relevant official tests.

## Validation of a diagnosis

A diagnosis is strong when:

- the symptom is reproducible;
- one hypothesis predicts the result of a discriminating test;
- changing/removing the cause changes the symptom;
- the fix works on the original scenario and a minimal fixture;
- no unrelated production state was destroyed;
- regression checks cover adjacent behavior.

Use **probable cause** when evidence is incomplete. Do not label an unreproduced guess “root cause.”

## Authoritative anchors

- [Blender 5.2 Crashes](https://docs.blender.org/manual/en/5.2/troubleshooting/crash.html)
- [Blender 5.2 GPU troubleshooting](https://docs.blender.org/manual/en/5.2/troubleshooting/gpu/index.html)
- [Blender 5.2 command line](https://docs.blender.org/manual/en/5.2/advanced/command_line/index.html)
- [Official API Gotchas](https://docs.blender.org/api/5.2/info_gotcha.html)
- [Troubleshooting Python errors and crashes](https://docs.blender.org/api/5.2/info_gotchas_crashes.html)
- [Navigating Blender source](https://developer.blender.org/docs/handbook/new_developers/navigate_code/)
