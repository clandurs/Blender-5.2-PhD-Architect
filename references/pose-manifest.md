# Pose Render Manifest

`render_pose_suite.py` accepts JSON with `armature`, `resolution`, `states`, and `shots`. A state maps pose-bone names to XYZ Euler degrees. A shot provides `name`, `state`, `target_bone`, `direction`, `distance`, and `ortho_scale`.

```json
{"armature":"Armature","resolution":512,"states":{"open":{},"fist":{"finger_index_01.R":[0,0,65]}},"shots":[{"name":"fist_side","state":"fist","target_bone":"hand.R","direction":[1,-1,0.4],"distance":1.0,"ortho_scale":0.35}]}
```

The script restores pose transforms afterward and never saves the `.blend`.

Use absolute paths for the manifest, output directory, and report when invoking Blender in background mode because Blender may change its process working directory after loading a file.
