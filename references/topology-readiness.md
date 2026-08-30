# Topology Readiness

Inspect connected components, loose vertices, boundary/non-manifold edges, separate fingers, wrist continuity, edge flow, joint density, long triangles crossing joints, poles on creases, internal shells, holes, tunnels, and the triangulated count.

Each intended joint needs multiple usable deformation rows around its pivot. The bend crease must compress while the outer arc stretches without exposing a void. Digits must remain individually selectable without unintended bridges.

Stop before weights or animation when a joint lacks usable loops, digits are fused, a hole/tunnel intersects the bend, or a basic bend tears, spikes, hooks, or collapses. Decimation, voxel remesh, Preserve Volume, bone-roll changes, and shape keys do not replace articulation topology. Use controlled retopology or a suitable donor only with authority for that material change.

Global counts cannot prove joint readiness. Before the audit, provide `--joint-contract joints.json`, mapping each target mesh object to its intended joints, for example `{"Body":["index_01_R","index_02_R"]}`. Only named target meshes receive those requirements, so hair, eyes, and clothing do not falsely fail. A missing/renamed contract target forces the top-level barrier to `FAIL`. Create each corresponding `QA_JOINT_<id>` vertex group, such as `QA_JOINT_index_01_R`. Mark the target object's `qa_joint_verdict::<id>` custom property as `PASS` or `FAIL` after retaining a wireframe/bend-row view. Missing groups fail; missing verdicts produce `MANUAL_VISUAL_REQUIRED`. The audit includes triangles crossing each region boundary and reports edge length relative to regional scale.
