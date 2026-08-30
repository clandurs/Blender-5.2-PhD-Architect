# Procedural production workflow

## Outcome

A versioned procedural system with a stable artist-facing interface, declared data model, deterministic behavior, measured performance, and a controlled bake/export path.

## Phase 0 — System specification

Define:

- user problem and tasks the system replaces;
- supported input geometry/components and coordinate spaces;
- artist inputs, units, ranges, defaults, and error states;
- output geometry, attributes, materials, instances, and diagnostics;
- stable ID/seed policy and allowed upstream changes;
- interactive/final scale, memory, and evaluation budget;
- Blender 5.2 feature/API dependencies;
- publish, bake, export, and fallback requirements.

Gate: the interface and acceptance examples exist before a large graph is built.

## Phase 1 — Minimal proof

1. Build the smallest graph/script that proves the central rule.
2. Use primitive fixtures and expose intermediate values in Spreadsheet/Viewer or structured logs.
3. Verify domain, type, coordinate space, identity, and instance behavior.
4. Create one negative/missing-input case.
5. Record expected output counts and invariants.

Gate: data semantics pass before visual complexity is added.

## Phase 2 — Interface architecture

- group controls by artist task;
- use names, units, ranges, and defaults that prevent invalid states;
- hide implementation details;
- define material/object/collection dependencies and null behavior;
- preserve stable socket/property identifiers for automation;
- version any geometry-bundle/list schema used across boundaries.

For node tools, distinguish interactive selection/context inputs from modifier inputs. For Python, distinguish RNA data operations from context-sensitive operators.

## Phase 3 — Production logic

Build semantic stages: acquire, normalize, generate/select, transform/solve, assign attributes/materials, instance/realize, output. Encapsulate reusable logic only when it has a coherent contract.

Use stable IDs for randomization. A fixed seed with unstable element order is not deterministic. Test after allowed topology, collection-order, and transform changes.

**[5.2]** If using lists or geometry bundles, document names/types and verify performance at target lengths. If using Geometry Nodes physics, label it experimental and maintain a non-experimental/frozen path.

## Phase 4 — Robustness

Test:

- empty geometry and missing dependencies;
- very small/large scale;
- negative, zero, and boundary parameter values;
- multiple components and instances;
- nonuniform transforms;
- renamed/reordered inputs where allowed;
- repeated execution and file reopen;
- linked/library/asset usage;
- background automation if claimed.

Failure should be visible and actionable, not a silent empty output unless empty is the documented result.

## Phase 5 — Performance

Measure target and worst-case inputs. Locate:

- instance realization;
- geometry/list growth;
- repeated proximity/raycast/domain conversion;
- duplicated subgraphs;
- high-frequency Python handlers/operators;
- cache/bake I/O.

Provide preview/final quality tiers or culling only if their behavior is predictable. Record geometry/instance counts, evaluation time, and memory.

## Phase 6 — Publish and delivery

1. Mark node groups/tools as assets or package add-ons/extensions as appropriate.
2. Record Blender minimum/maximum compatibility, dependencies, interface version, and examples.
3. Validate in a clean file/preferences context.
4. Create a bake/realize/export copy for consumers that cannot run the system.
5. Compare baked/delivery output with procedural source.
6. Publish immutable/versioned system plus manifest and rollback.

## Acceptance gates

- Interface is task-oriented and stable.
- Data types/domains/spaces and schemas are declared.
- Determinism holds under allowed changes.
- Missing/invalid inputs behave clearly.
- Performance fits target scale.
- 5.2 API automation passes.
- Experimental dependencies have a frozen fallback.
- Clean-file and delivery-consumer tests pass.

## Stop conditions

Stop for a decision when stable identity cannot be guaranteed, the target cannot support required attributes/instances, realization exceeds budget, an experimental feature is the only path, or an interface change would break published users.
