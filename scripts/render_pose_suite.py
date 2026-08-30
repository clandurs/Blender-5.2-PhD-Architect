"""Render repeatable pose evidence without saving the opened Blender file."""
import argparse, json, math, sys
from pathlib import Path

import bpy
from mathutils import Vector


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args(argv)


def apply_state(armature, state):
    for bone in armature.pose.bones:
        bone.rotation_mode = "XYZ"
        bone.location = (0, 0, 0)
        bone.rotation_euler = (0, 0, 0)
        bone.scale = (1, 1, 1)
    missing = []
    for name, degrees in state.items():
        bone = armature.pose.bones.get(name)
        if bone is None:
            missing.append(name)
            continue
        bone.rotation_euler = tuple(math.radians(value) for value in degrees)
    bpy.context.view_layer.update()
    return missing


def snapshot_pose(armature):
    return {bone.name: {"rotation_mode": bone.rotation_mode, "location": tuple(bone.location),
                        "rotation_euler": tuple(bone.rotation_euler), "rotation_quaternion": tuple(bone.rotation_quaternion),
                        "rotation_axis_angle": tuple(bone.rotation_axis_angle), "scale": tuple(bone.scale)}
            for bone in armature.pose.bones}


def restore_pose(armature, snapshot):
    for bone in armature.pose.bones:
        saved = snapshot[bone.name]
        bone.location = saved["location"]
        bone.scale = saved["scale"]
        bone.rotation_mode = saved["rotation_mode"]
        if bone.rotation_mode == "QUATERNION":
            bone.rotation_quaternion = saved["rotation_quaternion"]
        elif bone.rotation_mode == "AXIS_ANGLE":
            bone.rotation_axis_angle = saved["rotation_axis_angle"]
        else:
            bone.rotation_euler = saved["rotation_euler"]
    bpy.context.view_layer.update()


def ensure_camera(scene):
    data = bpy.data.cameras.new("BW_EvidenceCamera")
    camera = bpy.data.objects.new("BW_EvidenceCamera", data)
    scene.collection.objects.link(camera)
    data.type = "ORTHO"
    scene.camera = camera
    return camera


def aim(camera, target, direction, distance):
    direction = Vector(direction).normalized()
    camera.location = target + direction * distance
    camera.rotation_euler = (target - camera.location).to_track_quat("-Z", "Y").to_euler()


def main():
    args = parse_args()
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    armature = bpy.data.objects.get(manifest["armature"])
    if armature is None or armature.type != "ARMATURE":
        raise RuntimeError("Manifest armature is missing or is not an armature")
    scene = bpy.context.scene
    resolution = int(manifest.get("resolution", 512))
    scene.render.resolution_x = resolution
    scene.render.resolution_y = resolution
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = True
    scene.render.engine = "BLENDER_WORKBENCH"
    camera = ensure_camera(scene)
    original_pose = snapshot_pose(armature)
    results = []
    try:
        for shot in manifest.get("shots", []):
            state_name = shot["state"]
            missing = apply_state(armature, manifest.get("states", {}).get(state_name, {}))
            target_bone = armature.pose.bones.get(shot["target_bone"])
            if target_bone is None:
                raise RuntimeError(f"Target bone not found: {shot['target_bone']}")
            target = armature.matrix_world @ target_bone.center
            aim(camera, target, shot.get("direction", [1, -1, 0.5]), float(shot.get("distance", 1.0)))
            camera.data.ortho_scale = float(shot.get("ortho_scale", 0.4))
            output = output_dir / f"{shot['name']}.png"
            scene.render.filepath = str(output)
            bpy.ops.render.render(write_still=True)
            results.append({"name": shot["name"], "state": state_name, "path": str(output), "missing_pose_bones": missing})
    finally:
        restore_pose(armature, original_pose)
        bpy.data.objects.remove(camera, do_unlink=True)
    Path(args.report).write_text(json.dumps({"renders": results}, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
