"""Read-only Blender character audit. Run after `--python ... -- --output audit.json`."""
import argparse, hashlib, json, sys
from pathlib import Path

import bpy
import bmesh
from mathutils import Vector


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def geometry_digest(mesh):
    h = hashlib.sha256()
    for vertex in mesh.vertices:
        h.update(f"v:{vertex.index}:{vertex.co.x:.9g},{vertex.co.y:.9g},{vertex.co.z:.9g};".encode())
    for polygon in mesh.polygons:
        h.update(("p:" + ",".join(map(str, polygon.vertices)) + ";").encode())
    return h.hexdigest()


def joint_regions(obj, mesh, required):
    result, present = [], set()
    groups = [group for group in obj.vertex_groups if group.name.startswith("QA_JOINT_")]
    for group in groups:
        joint = group.name[len("QA_JOINT_"):]
        present.add(joint)
        members = {vertex.index for vertex in mesh.vertices
                   for item in vertex.groups if item.group == group.index and item.weight >= 0.5}
        ratios, normalized_edges, crossing = [], [], 0
        points = [mesh.vertices[index].co for index in members]
        if points:
            low = Vector((min(point.x for point in points), min(point.y for point in points), min(point.z for point in points)))
            high = Vector((max(point.x for point in points), max(point.y for point in points), max(point.z for point in points)))
            scale = (high - low).length
        else:
            scale = 0.0
        for tri in mesh.loop_triangles:
            tri_set = set(tri.vertices)
            if not tri_set.intersection(members):
                continue
            if not tri_set.issubset(members):
                crossing += 1
            coords = [mesh.vertices[index].co for index in tri.vertices]
            lengths = [(coords[i] - coords[(i + 1) % 3]).length for i in range(3)]
            if min(lengths) > 0:
                ratios.append(max(lengths) / min(lengths))
            if scale > 0:
                normalized_edges.extend(length / scale for length in lengths)
        verdict = str(obj.get(f"qa_joint_verdict::{joint}", "MANUAL_VISUAL_REQUIRED")).upper()
        result.append({"name": group.name, "joint": joint, "vertices": len(members),
                       "intersecting_triangles": len(ratios), "crossing_triangles": crossing,
                       "max_triangle_edge_ratio": max(ratios, default=None),
                       "max_edge_to_region_scale": max(normalized_edges, default=None),
                       "manual_bend_row_verdict": verdict})
    missing = sorted(set(required) - present)
    unresolved = sorted(item["joint"] for item in result
                        if item["joint"] in required and item["manual_bend_row_verdict"] not in {"PASS", "FAIL"})
    failed = sorted(item["joint"] for item in result if item["manual_bend_row_verdict"] == "FAIL")
    status = "FAIL" if missing or failed else ("MANUAL_VISUAL_REQUIRED" if unresolved else "PASS")
    return {"required": sorted(required), "missing": missing, "failed": failed,
            "unresolved": unresolved, "barrier_status": status, "regions": result}


def mesh_record(obj, required_joints):
    mesh = obj.data
    mesh.calc_loop_triangles()
    bm = bmesh.new()
    bm.from_mesh(mesh)
    boundary = sum(1 for edge in bm.edges if edge.is_boundary)
    nonmanifold = sum(1 for edge in bm.edges if not edge.is_manifold and not edge.is_boundary)
    loose = sum(1 for vert in bm.verts if not vert.link_edges)
    bm.free()
    armature_objects = [mod.object for mod in obj.modifiers if mod.type == "ARMATURE" and mod.object]
    deform_names = {bone.name for armature in armature_objects for bone in armature.data.bones if bone.use_deform}
    deform_group_indices = {group.index for group in obj.vertex_groups if group.name in deform_names}
    influences = [sum(1 for item in vert.groups if item.weight > 0 and item.group in deform_group_indices)
                  for vert in mesh.vertices]
    return {
        "name": obj.name,
        "vertices": len(mesh.vertices),
        "edges": len(mesh.edges),
        "polygons": len(mesh.polygons),
        "triangles": len(mesh.loop_triangles),
        "boundary_edges": boundary,
        "nonmanifold_nonboundary_edges": nonmanifold,
        "loose_vertices": loose,
        "uv_layers": [layer.name for layer in mesh.uv_layers],
        "materials": [slot.material.name if slot.material else None for slot in obj.material_slots],
        "armature_modifiers": [mod.object.name if mod.object else None for mod in obj.modifiers if mod.type == "ARMATURE"],
        "vertex_groups": len(obj.vertex_groups),
        "unweighted_vertices": sum(1 for count in influences if count == 0),
        "max_influences": max(influences, default=0),
        "over_four_influences": sum(1 for count in influences if count > 4),
        "shape_keys": [key.name for key in mesh.shape_keys.key_blocks] if mesh.shape_keys else [],
        "joint_regions": joint_regions(obj, mesh, required_joints),
        "basis_geometry_sha256": geometry_digest(mesh),
    }


def armature_record(obj):
    return {
        "name": obj.name,
        "bones": len(obj.data.bones),
        "deform_bones": sum(1 for bone in obj.data.bones if bone.use_deform),
        "bone_names": sorted(bone.name for bone in obj.data.bones),
    }


def action_record(action):
    keys = sum(len(curve.keyframe_points) for curve in action.fcurves)
    scene = bpy.context.scene
    fps = scene.render.fps / scene.render.fps_base
    return {"name": action.name, "frame_range": list(action.frame_range), "fps": fps,
            "loop": action.get("bw_looping"), "root_motion": action.get("bw_root_motion"),
            "fcurves": len(action.fcurves), "keyframes": keys}


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--joint-contract", help="JSON mapping target mesh names to required QA_JOINT ids")
    args = parser.parse_args(argv)
    joint_contract = json.loads(Path(args.joint_contract).read_text(encoding="utf-8")) if args.joint_contract else {}
    blend = Path(bpy.data.filepath)
    mesh_objects = [obj for obj in sorted(bpy.data.objects, key=lambda x: x.name) if obj.type == "MESH"]
    mesh_names = {obj.name for obj in mesh_objects}
    missing_contract_meshes = sorted(set(joint_contract) - mesh_names)
    mesh_reports = [mesh_record(obj, joint_contract.get(obj.name, [])) for obj in mesh_objects]
    mesh_barriers = [item["joint_regions"]["barrier_status"] for item in mesh_reports
                     if item["joint_regions"]["required"]]
    overall_barrier = ("FAIL" if missing_contract_meshes or "FAIL" in mesh_barriers else
                       "MANUAL_VISUAL_REQUIRED" if "MANUAL_VISUAL_REQUIRED" in mesh_barriers else "PASS")
    report = {
        "blender_version": bpy.app.version_string,
        "blend_path": str(blend),
        "blend_sha256": sha256_file(blend) if blend.is_file() else None,
        "joint_contract": joint_contract,
        "missing_joint_contract_meshes": missing_contract_meshes,
        "topology_barrier_status": overall_barrier,
        "meshes": mesh_reports,
        "armatures": [armature_record(obj) for obj in sorted(bpy.data.objects, key=lambda x: x.name) if obj.type == "ARMATURE"],
        "actions": [action_record(action) for action in sorted(bpy.data.actions, key=lambda x: x.name)],
    }
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
