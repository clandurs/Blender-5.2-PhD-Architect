# Production pipelines

## Scope

Use for project architecture, asset libraries, link/append/overrides, naming, publishing, versioning, color, caches, renders, interchange, multi-artist ownership, and reproducible automation.

## Build contracts, not folders alone

A production pipeline defines:

- data ownership and authoritative source;
- work-in-progress, review, approved, staged, and published states;
- dependency versions and compatibility;
- naming, units, axes, color, frame, and file/path conventions;
- how assets are composed into shots/scenes;
- validation and approval evidence;
- rollback, archival, and migration.

A neat directory tree without these semantics is storage, not a pipeline.

## Source, work, and publish

Separate:

- **Source:** editable procedural/high-resolution/art-authoring files.
- **Work:** artist iterations, local caches, previews, and temporary renders.
- **Publish:** immutable or versioned data approved for downstream use.
- **Delivery:** format/package tailored to a consumer.

Do not let a consumer link to an artist's mutable work file when it expects a stable publish. Do not destroy the source to make a delivery smaller.

## Blender data architecture

**[5.2]** Blender files contain interrelated data-blocks. Use:

- **Link** when consumers should reference authoritative external data.
- **Append** when the consumer needs an independent copy.
- **Library overrides** when linked data needs controlled local edits.
- **Asset libraries/catalogs** for curated reusable data-blocks with discoverable meaning.

Before choosing, define who owns geometry, materials, rig, animation, and shot overrides. Test update propagation and conflict behavior with a tiny fixture. Shared data can be efficient but surprising; make single-user only when divergence is intended.

## Naming and identity

Names should encode stable identity, not every mutable property. Define machine-parseable rules for:

- project/sequence/shot/asset/variant/task/version;
- objects, collections, data-blocks, bones, materials, actions, node groups, images, and caches;
- side tokens and hierarchy;
- publish and delivery files.

Use persistent IDs or manifest records when renaming is expected. A name-based script needs collision handling and ownership checks.

## Paths and dependencies

- Choose relative versus absolute paths based on package mobility and shared storage.
- Define case-sensitivity and Unicode policy across platforms.
- Detect missing files before publish.
- Decide whether to pack small self-contained dependencies or keep large/shared data external.
- Version textures, caches, OCIO configs, extensions, fonts, and external libraries alongside the asset manifest.
- Never publish machine-local temporary or download paths.

## Multi-artist ownership

Blender Studio's task-layer/publish patterns demonstrate one viable ownership model. For any team workflow, define:

- which task owns each object/data category;
- how changes are pushed/pulled/merged;
- what can be overridden;
- staged/sandbox versus active publish;
- conflict, surrender, review, and rollback behavior.

Adopt only the complexity the team needs. A solo project may need versioned publishes and manifests but not a merge service.

## Color, render, and cache contracts

Lock:

- OCIO configuration and version;
- input color-space rules and naming;
- working/render/display/output transforms;
- render engine/build/device policy where reproducibility matters;
- frame range/numbering, passes, OpenEXR channels, bit depth, compression, and alpha;
- cache solver/version, seed, frame range, name, directory, and dependency revision.

Renders and caches are derived data with lineage. Store enough metadata to know which source and settings produced them.

## Interchange decisions

| Need | Likely format direction | Caveat |
| --- | --- | --- |
| Preserve Blender authoring | `.blend` plus dependencies | Not a neutral consumer format; executable content may exist |
| Runtime asset delivery | glTF/GLB | Supported subset; validate materials, skinning, morphs, animation in target |
| Layered scene composition | USD | Composition is powerful; Blender/consumer feature subsets vary |
| High-dynamic-range image/pass exchange | OpenEXR | Define channels, windows, alpha, compression, and color |
| Simple geometry exchange | OBJ/PLY/STL or target format | Usually loses richer scene/material/animation semantics |

Do not select format by popularity. Build a contract fixture and test the exact exporter/importer versions.

## Automation and manifests

A publish manifest should record:

- asset/shot ID and version;
- source revision and Blender exact version;
- dependencies and hashes/versions;
- units/axes/frame rate/color config;
- exported files, options, and checksums;
- validation results and known exceptions;
- owner/reviewer and timestamp.

Automations should preflight, fail closed, write to a staging location, validate, then atomically/explicitly promote. Avoid partial publishes with a final-looking version name.

## Security and reproducibility

Blend-files, drivers, scripts, and extensions may execute code. Treat external packages as untrusted until inspected. Keep auto-execution and online access governed. Pin extensions and Python dependencies; a “latest” dependency defeats reproducibility.

## Publish gates

- Source and publish ownership are named.
- Blender exact patch, extensions, color config, and dependencies are locked/recorded.
- No missing, absolute machine-local, or unauthorized external paths.
- Geometry/rig/material/animation/cache/render validations match the asset type.
- Fresh consumer import passes, not only Blender re-import.
- Manifest and checksums match closed files.
- Publish is immutable/versioned and rollback exists.
- WIP, staged, active, and delivery states cannot be confused by naming/location.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Shot changes when artist saves asset | Consumer links mutable work rather than versioned publish |
| Override breaks after update | Ownership/hierarchy/path changed beyond override contract |
| Render differs across machines | Compare Blender patch, extensions, OCIO, dependencies, device, paths, and caches |
| Export references missing textures | Package/relative-path and manifest preflight failed |
| Two artists overwrite data | Ownership and publish/merge state are not explicit |
| “Approved” file cannot be reproduced | Source revision, settings, dependency, and manifest lineage are missing |

## Authoritative anchors

- [Blender 5.2 Assets, Files, & Data System](https://docs.blender.org/manual/en/5.2/files/index.html)
- [Blender Studio pipeline introduction](https://studio.blender.org/tools/pipeline-overview/introduction)
- [Blender Studio Asset Pipeline](https://studio.blender.org/tools/addons/asset_pipeline)
- [OpenColorIO](https://opencolorio.org/)
- [OpenEXR technical introduction](https://openexr.com/en/latest/TechnicalIntroduction.html)
- [Introduction to OpenUSD](https://openusd.org/release/intro.html)
- [Khronos glTF Registry](https://registry.khronos.org/glTF/)
- [VFX Reference Platform](https://vfxplatform.com/)
