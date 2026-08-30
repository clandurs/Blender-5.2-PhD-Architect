"""Compare Blender character audit JSON files without modifying either source."""
import argparse, json, sys
from pathlib import Path


PRESERVED_MESH_FIELDS = (
    "vertices", "edges", "polygons", "triangles", "uv_layers", "materials", "basis_geometry_sha256"
)


def by_name(records):
    return {record["name"]: record for record in records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline")
    parser.add_argument("candidate")
    parser.add_argument("--output", required=True)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--expected-changes")
    args = parser.parse_args()
    baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    candidate = json.loads(Path(args.candidate).read_text(encoding="utf-8"))
    expected = json.loads(Path(args.expected_changes).read_text(encoding="utf-8")) if args.expected_changes else {}
    allowed_bones = {name: set(values) for name, values in expected.get("allowed_added_bones", {}).items()}
    changes = []
    base_meshes, cand_meshes = by_name(baseline.get("meshes", [])), by_name(candidate.get("meshes", []))
    for name in sorted(set(base_meshes) | set(cand_meshes)):
        if name not in base_meshes or name not in cand_meshes:
            changes.append({"kind": "mesh_presence", "name": name, "baseline": name in base_meshes, "candidate": name in cand_meshes})
            continue
        for field in PRESERVED_MESH_FIELDS:
            if base_meshes[name].get(field) != cand_meshes[name].get(field):
                changes.append({"kind": "mesh_field", "name": name, "field": field,
                                "baseline": base_meshes[name].get(field), "candidate": cand_meshes[name].get(field)})
    base_arms, cand_arms = by_name(baseline.get("armatures", [])), by_name(candidate.get("armatures", []))
    for name in sorted(set(base_arms) | set(cand_arms)):
        if name not in base_arms or name not in cand_arms:
            changes.append({"kind": "armature_presence", "name": name, "baseline": name in base_arms, "candidate": name in cand_arms})
        else:
            before = set(base_arms[name].get("bone_names", []))
            after = set(cand_arms[name].get("bone_names", []))
            removed, added = before - after, after - before
            unexpected_added = added - allowed_bones.get(name, set())
            if removed or unexpected_added:
                changes.append({"kind": "bone_names", "name": name, "removed": sorted(removed),
                                "unexpected_added": sorted(unexpected_added), "allowed_added": sorted(added - unexpected_added)})
    base_actions, cand_actions = by_name(baseline.get("actions", [])), by_name(candidate.get("actions", []))
    base_action_names, cand_action_names = set(base_actions), set(cand_actions)
    expected_added_actions = expected.get("expected_added_actions", {})
    allowed_added_actions = set(expected_added_actions)
    allowed_removed_actions = set(expected.get("allowed_removed_actions", []))
    unexpected_added_actions = sorted((cand_action_names - base_action_names) - allowed_added_actions)
    unexpected_removed_actions = sorted((base_action_names - cand_action_names) - allowed_removed_actions)
    missing_expected_additions = sorted(allowed_added_actions - (cand_action_names - base_action_names))
    if unexpected_added_actions or unexpected_removed_actions or missing_expected_additions:
        changes.append({"kind": "action_presence", "unexpected_added": unexpected_added_actions,
                        "unexpected_removed": unexpected_removed_actions,
                        "missing_expected_additions": missing_expected_additions})
    required_action_fields = {"frame_range", "fps", "loop", "root_motion"}
    for name in sorted(allowed_added_actions & cand_action_names):
        contract = expected_added_actions[name]
        missing_contract_fields = sorted(required_action_fields - set(contract))
        mismatched = {field: {"expected": value, "candidate": cand_actions[name].get(field)}
                      for field, value in contract.items() if cand_actions[name].get(field) != value}
        if missing_contract_fields or mismatched:
            changes.append({"kind": "added_action_contract", "name": name,
                            "missing_contract_fields": missing_contract_fields, "mismatched": mismatched})
    allowed_action_changes = {name: set(fields) for name, fields in expected.get("allowed_action_changes", {}).items()}
    for name in sorted(base_action_names & cand_action_names):
        changed_fields = {field for field in ("frame_range", "fps", "loop", "root_motion", "fcurves", "keyframes")
                          if base_actions[name].get(field) != cand_actions[name].get(field)}
        unexpected_fields = changed_fields - allowed_action_changes.get(name, set())
        if unexpected_fields:
            changes.append({"kind": "action_fields", "name": name,
                            "unexpected_fields": sorted(unexpected_fields)})
    candidate_actions = sorted(cand_action_names)
    report = {
        "strict_preservation_pass": not changes,
        "changes": changes,
        "baseline_actions": sorted(item["name"] for item in baseline.get("actions", [])),
        "candidate_actions": candidate_actions,
    }
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    if args.strict and changes:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
