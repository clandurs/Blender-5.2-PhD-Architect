# Geometry Nodes

## Scope and 5.2 status

Use for procedural geometry, scattering, attribute processing, node tools, simulation/bake zones, reusable node assets, and Python-controlled modifiers.

**[5.2]** Geometry Nodes in Blender 5.2 includes lists, geometry bundles, collection-children access, sound-frequency sampling, empty-object modifiers, new attribute transfer/inspection operations, and performance changes. The modifier Python API changed to proper RNA properties. These are version-bound facts; do not backport them by assumption.

## Data-model reasoning

Before connecting nodes, identify:

- geometry components involved: mesh, curve, point cloud, instances, volume, and others supported by the graph;
- attribute domain: point, edge, face, face corner, spline, instance, etc.;
- data type and interpolation/conversion behavior;
- field versus single value versus list;
- geometry ownership and whether instances remain references or become realized geometry;
- coordinate space and transform at every object/collection boundary.

Most “wrong value” bugs are domain, context, or space bugs. Diagnose the data model before adding corrective math.

## Interface-first design

Define the node group as a tool/API:

- purpose and supported geometry;
- required inputs, units, ranges, defaults, and null behavior;
- outputs and preserved attributes;
- deterministic seed policy;
- performance envelope and known failure modes;
- Blender minimum/maximum version when 5.2 features are used.

Use descriptive socket names and panels. Keep stable identifiers when automation or published modifiers depend on them. Do not expose low-level implementation parameters that allow invalid states without a reason.

## Build in semantic stages

1. **Acquire:** input geometry, objects, collections, images, CSV/other sources.
2. **Normalize:** transforms, scale, domains, IDs, selections, and missing-data defaults.
3. **Generate/select:** topology, points, curves, masks, or candidate sets.
4. **Transform/solve:** placement, deformation, adjacency, proximity, or simulation.
5. **Attribute/material:** named outputs, IDs, UVs, normals, materials.
6. **Instance/realize:** retain instancing until operations or delivery require realization.
7. **Output:** geometry, diagnostic values, and explicit named attributes.

Create small diagnostic branches using Viewer/Spreadsheet inspection rather than inferring values from final geometry.

## Fields, lists, and bundles

- A field is evaluated in a geometry context; the same field can yield different values by domain/component.
- A list is an ordered variable-length value introduced as a core 5.2 data type. Large list operations can be expensive; measure them at target scale.
- A bundle groups named values. **[5.2]** Geometry bundles can attach data to geometry and carry it across modifier/object boundaries. Document bundle schema like an API; a silent name/type change is a breaking change.
- String fields exist in 5.2, while the release notes state string attributes are not yet supported in Geometry Nodes. Do not design a string-attribute handoff that the version cannot store.

## Instances and stable identity

Keep instances when repeated geometry should share data and operations support instances. Realization expands memory and topology and can alter attribute domains. Place Realize Instances at the latest justified point.

For randomization and simulation, derive stable IDs from durable source identity rather than transient point order when possible. Test after upstream topology/order changes. A fixed random seed is not enough if element identity changes.

## Performance method

- Measure final evaluated geometry and instances, not only source counts.
- Avoid repeated domain conversions, unnecessary realization, dense proximity operations, and duplicated expensive subgraphs.
- Cache/bake only when invalidation rules and storage ownership are defined.
- Compare viewport and render evaluation settings.
- Profile at target collection size, geometry density, and frame range.
- Provide quality tiers or culling for interactive work when final settings are expensive.

## Experimental physics

**[Experimental][5.2]** New Geometry Nodes cloth and hair dynamics are explicitly experimental. Any production proposal using them must include:

- an exact 5.2 patch lock;
- a frozen/baked output path;
- a legacy solver or non-simulated fallback;
- a compatibility test before opening/saving in another Blender version;
- explicit acceptance of potential design/API change.

## Python integration

**[5.2]** Do not use pre-5.2 custom-property access patterns for Geometry Nodes modifier inputs/outputs. Inspect the 5.2 RNA interface and release notes, and access `modifier.properties.inputs` / outputs according to the documented identifiers and types. Build automation against stable group interface identifiers and include a migration test.

## Validation gates

- Inputs/outputs have declared units, types, domains, defaults, and version requirements.
- Spreadsheet/Viewer checks confirm intermediate domains and values.
- Stable IDs preserve variation through permitted upstream edits.
- Missing object/collection/material inputs fail clearly or use documented defaults.
- Instance realization and attribute propagation are deliberate.
- Geometry counts, memory, and evaluation time meet target budgets.
- Seeds and bakes reproduce the expected result on a clean file/session.
- Python automation passes on Blender 5.2 using RNA properties.
- Experimental dependencies have frozen output and fallback.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Attribute changes after node insertion | Inspect domain/type before and after implicit conversion |
| Random layout changes after unrelated edit | Stable ID depends on point order or topology rather than durable identity |
| Memory jumps | Locate Realize Instances, dense mesh conversion, list growth, or repeated subgraph |
| Modifier input script fails after 5.2 migration | Replace legacy ID-property access with 5.2 RNA property access |
| Empty output | Inspect component type, selection field, missing input, and geometry socket separately |
| Simulation differs after reopen | Check bake/cache ownership, frame range, seed, version, and experimental status |

## Authoritative anchors

- [Blender 5.2 Geometry Nodes Manual](https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/index.html)
- [Blender 5.2 Geometry Nodes release notes](https://developer.blender.org/docs/release_notes/5.2/geometry_nodes/)
- [Blender 5.2 Python API release notes](https://developer.blender.org/docs/release_notes/5.2/python_api/)
- [Blender 5.2 Physics release notes](https://developer.blender.org/docs/release_notes/5.2/physics/)
