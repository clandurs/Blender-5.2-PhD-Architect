# Animation and Evidence

Before keying, record action name, FPS, inclusive frame range, looping, root motion, active side, contact frame, anticipation, recovery, weapon state, foot/root constraints, and export target.

Key the fewest controls needed for readable motion. Check gameplay and side silhouettes. For strikes, verify anticipation, acceleration, contact, follow-through, recovery, planted feet, stable root, and self-intersection at game distance.

Produce audit JSON before/after, standardized palm/side/three-quarter deformation views, contact/recovery views, save/reopen verification, and a comparison report for preserved mesh basis, materials, UV layers, bones, and actions.

Visual QA covers silhouette, intersections, volume, pose readability, and style. Structured QA covers counts, identity, preservation, weights, bone/action contracts, and determinism. Neither replaces the other.

For authorized rig/action changes, pass `compare_audits.py` an expected-change JSON such as `{"allowed_added_bones":{"Armature":["finger_index_01.R"]},"expected_added_actions":{"BW_Male_UnarmedPunch_R":{"frame_range":[1.0,25.0],"fps":24.0,"loop":false,"root_motion":"in_place"}},"allowed_removed_actions":[],"allowed_action_changes":{}}`. Each new action requires exact frame range, FPS, loop, and root-motion fields; optional F-curve/key counts may also be frozen. Set the Blender action custom properties `bw_looping` and `bw_root_motion` so the audit can prove those terms. Added and removed actions are compared symmetrically; existing action fields stay strict unless explicitly allowed. Mesh basis, topology, materials, and UVs remain strict unless the phase authorizes mesh changes and uses a separately reviewed baseline.
