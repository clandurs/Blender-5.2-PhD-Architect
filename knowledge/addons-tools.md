# Add-ons and tools

## Scope

Use for Blender add-on design, 5.2 extension packaging, operators, panels, properties, keymaps, handlers, timers, migrations, distribution, and testing.

## Choose script, add-on, or extension

- **One-off script:** narrow task, no maintained UI/distribution requirement.
- **Add-on code:** reusable in-Blender feature with registration and possibly UI.
- **Extension package:** distributable add-on/theme with manifest, compatibility metadata, packaging, install/update workflow.
- **External process/tool:** heavy independent computation, service integration, or work that should not share Blender's memory/thread model.

Avoid building an add-on when a 30-line deterministic script is the maintained outcome. Avoid a one-off script when users need versioned installation, preferences, and repeatable UI.

## Extension contract

**[5.2]** A Blender extension package uses `blender_manifest.toml`; an add-on extension includes an `__init__.py` and declared metadata. Record:

- stable package ID, name, semantic version, maintainer, license, tags, and website/support;
- minimum Blender version and maximum exclusive version when known;
- platform and wheel requirements;
- permissions/online access and why they are needed;
- migration and data compatibility policy;
- build, validate, install-from-disk, and uninstall tests.

The package ID is an API. Renaming it can strand preferences, stored references, and update paths.

## Registration lifecycle

Registration and unregistration must be symmetric:

- classes in dependency order;
- properties removed from RNA types;
- handlers, timers, message-bus subscriptions, draw callbacks, and keymaps cleaned up;
- icons/previews and external resources released;
- no duplicate registration after reload;
- no background thread survives disable/unregister.

Store owner tokens/references needed for cleanup. A disabled add-on should stop affecting Blender without restart.

## Operator and UI design

- Operators validate context in `poll()` and validate data again in `execute()`.
- Use properties with useful names, units, ranges, and defaults.
- Support undo only when the operation genuinely participates safely.
- Report actionable errors; do not swallow exceptions.
- Panels should expose user decisions, status, and recovery—not mirror every internal variable.
- Long operations need progress, cancellation, and a defined partial-output policy.
- Keymaps must be scoped, discoverable, configurable, and removed on unregister.

Prefer the data API for deterministic work. Do not make a panel click sequence the internal architecture.

## State and persistence

Choose storage intentionally:

- operator properties for one invocation;
- add-on preferences for user-wide configuration;
- scene/object/property groups for file-owned data;
- external config for pipeline-owned data when appropriate.

Version persisted schemas. Migrate explicitly and preserve a rollback/copy when transformation is destructive. Never store secrets in blend-file custom properties or preferences that may be shared.

## Internet and trust

Add-ons are executable code. Inspect third-party packages before enabling. If an add-on uses the internet, respect Blender's online-access state and provide a clear offline failure path. Do not download and execute arbitrary code or mutate external services without the user's authorization.

## Performance

- Avoid heavy work in draw callbacks, dependency-graph handlers, or high-frequency timers.
- Debounce updates and respond only to relevant changes.
- Do not scan the whole file on every UI draw.
- Release evaluated meshes/images and temporary data.
- Profile with representative scenes and repeated enable/disable/reload cycles.

## Compatibility

Pin API claims to 5.2. Use compatibility/release notes for changed RNA and behavior. Where supporting multiple Blender versions, isolate adapters and test each supported version; sprawling inline version conditionals become unmaintainable.

## Validation gates

- Extension manifest validates and package installs from disk on clean 5.2 preferences.
- Enable, disable, re-enable, reload, and uninstall leave no duplicate classes/handlers/keymaps/timers.
- Operators pass valid/invalid context tests and undo/cancel behavior.
- Persistent data migrates or fails clearly without loss.
- Background mode behavior is tested or declared unsupported.
- Online access and external side effects are explicit and user-controlled.
- No secrets or machine-specific absolute paths ship in the package.
- Minimal fixtures and representative production files pass.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| “Already registered” on reload | Audit symmetric unregister and module reload state |
| Disabled add-on still runs | Inspect handlers, timers, message bus, draw callbacks, threads, and keymaps |
| UI freezes | Move heavy work out of draw/update callbacks; add bounded/cancelable execution |
| Operator works only from one editor | Make context requirement explicit or use data API |
| Preferences disappear after rename | Package/property identifiers changed without migration |
| Install fails on another machine | Inspect manifest, Blender version bounds, platform wheels, and bundled paths |

## Authoritative anchors

- [Blender 5.2 Creating Extensions](https://docs.blender.org/manual/en/5.2/advanced/extensions/index.html)
- [Blender 5.2 How to Create Extensions](https://docs.blender.org/manual/en/5.2/advanced/extensions/getting_started.html)
- [Blender 5.2 Python API](https://docs.blender.org/api/5.2/)
- [Official API Gotchas](https://docs.blender.org/api/5.2/info_gotcha.html)
- [Blender 5.2 Scripting & Security](https://docs.blender.org/manual/en/5.2/advanced/scripting/security.html)
