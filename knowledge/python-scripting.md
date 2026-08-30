# Python scripting

## Scope

Use for `bpy`, RNA/data API, operators, `bmesh`, `mathutils`, background automation, batch processing, scene validation, tests, and Blender-source Python integration.

## Pin the runtime contract

Record exact Blender patch, platform, invocation, input files, enabled extensions, preferences, auto-execution policy, network policy, and outputs. Use the Blender-bundled Python/API for the target version; system Python compatibility is not implied.

## Prefer data APIs over UI context

**[5.2]** `bpy.data` addresses blend-file data; `bpy.context` exposes current UI/evaluation context and is read-only; `bpy.ops` invokes operators whose poll/context requirements mirror interactive tools.

Use direct RNA/data access when the operation is fundamentally data mutation and no operator-only behavior is needed. Use operators when they embody complex Blender behavior, but:

- check `poll()`;
- establish mode, active object, selection, area/region, view layer, and scene deliberately;
- do not assume an operator that works in the console works in background mode;
- capture returned status and verify postconditions.

Context overrides should be narrow and documented. UI automation is not a substitute for data/API automation when a stable API exists.

## Data lifetime and modes

The official API gotchas warn that Blender Python objects can reference internal memory that is freed or reallocated. Avoid keeping element references across:

- collection growth/removal;
- mesh/curve data rebuild;
- mode changes;
- undo/redo or modal activity;
- data-block removal.

Store stable names/indices/IDs when appropriate and re-fetch data after mutations. Do not access removed RNA objects. Use `bmesh` correctly for edit-mode mesh access and update the mesh through the supported path.

## Threading and long work

Blender's Python integration is not generally thread-safe. Do not leave Python threads running alongside Blender. Use external processes for independent CPU work, Blender timers/modal operators for cooperative UI work where appropriate, or background Blender processes for batch isolation.

Never mutate Blender data from an arbitrary worker thread.

## Script architecture

Build automations as explicit transactions:

1. **Parse:** arguments/config and version requirements.
2. **Preflight:** file existence, writable output, scene contract, dependencies, trusted-script policy.
3. **Inventory:** capture inputs and a summary before mutation.
4. **Transform:** perform deterministic, scoped changes.
5. **Validate:** assert geometry/data/render/export postconditions.
6. **Persist:** save/export to a new target unless overwrite is explicitly intended.
7. **Report:** structured result, warnings, output paths, timings, and nonzero failure.

Idempotency means a repeated run either produces the same result or detects a completed compatible state. Avoid `.001`-style name drift by resolving ownership and exact names.

## Background execution

Use Blender's command line for repeatable batch work. Argument order matters because Blender executes arguments in order and loading a blend-file can overwrite earlier settings.

For testing:

- use `--factory-startup` or controlled isolated preferences when appropriate;
- pass input file before settings that it would overwrite;
- place render-triggering arguments after output/engine/frame settings;
- capture stdout/stderr and logs;
- verify files and data, not only process exit;
- keep auto-execution disabled unless trusted content requires it and the task authorizes it.

## Version-sensitive APIs

**[5.2]** Geometry Nodes modifier properties changed from legacy custom-property patterns to RNA properties. Inspect `modifier.properties.inputs` and outputs via the 5.2 API/release notes. Add migration tests for scripts touching Geometry Nodes modifiers.

Do not use `bpy.app.version` checks alone to guess API behavior; feature-detect when reasonable and fail with a clear supported-version message.

## Testing

Create tiny fixture blend-files/scenes. Test:

- empty, minimal, representative, and malformed input;
- repeated execution;
- object/mode/selection independence;
- background versus UI where supported;
- missing data, non-ASCII paths/names, relative paths, and read-only outputs;
- rollback/partial failure;
- exact serialized or rendered postconditions appropriate to the task.

For Blender source contributions, follow the official build/test handbook and add Python tests where the behavior can be expressed there.

## Security

Python inside blend-files and extensions has broad host access. Do not enable auto-run on an untrusted file. Inspect scripts, registered text blocks, drivers, handlers, add-ons, and manifests. Never print secrets or embed credentials in a blend-file, script, log, or extension package.

## Validation gates

- Exact Blender 5.2 patch and invocation are recorded.
- Data API/operator choice and context dependencies are explicit.
- No stale RNA references survive reallocating operations.
- Script is deterministic/idempotent for the declared input class.
- Background run works if claimed; UI-only limitations are stated.
- Failures return clear diagnostics and do not silently save partial work.
- Outputs are validated and written to intended paths.
- Auto-execution/network/external processes remain within the trust contract.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Operator poll fails | Print/check mode, active object, selection, area/region, scene, and `poll()` |
| Script crashes after mode change | Re-fetch mesh/bone/point collections after reallocation |
| Works in UI, fails background | Remove UI-context operators or supply a supported data API path |
| Duplicate `.001` objects every run | Add ownership lookup and idempotent create/update behavior |
| Geometry Nodes property lookup fails | Migrate legacy custom-property code to 5.2 RNA properties |
| Process succeeds, output missing | Verify argument order, output path, save/render trigger, and postconditions |

## Authoritative anchors

- [Blender 5.2 Python API](https://docs.blender.org/api/5.2/)
- [API Reference Usage](https://docs.blender.org/api/5.2/info_api_reference.html)
- [Context Access](https://docs.blender.org/api/5.2/bpy.context.html)
- [Official API Gotchas](https://docs.blender.org/api/5.2/info_gotcha.html)
- [Troubleshooting Python crashes](https://docs.blender.org/api/5.2/info_gotchas_crashes.html)
- [Blender 5.2 command line](https://docs.blender.org/manual/en/5.2/advanced/command_line/index.html)
- [Blender 5.2 Python API release notes](https://developer.blender.org/docs/release_notes/5.2/python_api/)
