---
name: blender-5-2-phd-architect
description: Govern Blender 5.2 work, including interactive and background processes, with source preservation, topology readiness, rigging, weights, corrective shapes, animation authoring, deterministic scripts, and evidence. Use for every Blender task; apply only the relevant stages for static mesh, character, rendering, inspection, automation, export preparation, or troubleshooting work.
---

# Blender 5.2 PHD Architect

Use a five-stage workflow that fails early on bad deformation topology and produces reproducible evidence. Preserve accepted sources; work only on versioned copies. Treat external downloads, paid services, Unity import, export, and project changes as separate permissions.

Apply this skill to every Blender invocation, including background-mode commands. For non-character work, use the preservation, deterministic-execution, evidence, and retry rules while skipping irrelevant character stages.

## Route the work

1. **Topology readiness** — inspect joint loops, digit separation, manifold state, triangle flow, and deformation density. Read [topology-readiness.md](references/topology-readiness.md).
2. **Rig construction** — build or normalize a suitable deform skeleton; use Rigify when an animator-facing control rig helps, or a minimal deform rig when export compatibility controls. Read [rigging-and-weights.md](references/rigging-and-weights.md).
3. **Weights and correctives** — isolate digit weights, normalize influences, test volume preservation, then add narrowly driven corrective shapes only where sound topology and weights still need help. Read [rigging-and-weights.md](references/rigging-and-weights.md).
4. **Animation authoring** — freeze the action contract before keying, author contact and recovery deliberately, and keep looping/root-motion behavior explicit. Read [animation-and-evidence.md](references/animation-and-evidence.md).
5. **Automated evidence** — audit the `.blend`, render standardized pose views, save/reopen, and compare accepted geometry against the candidate. Read [animation-and-evidence.md](references/animation-and-evidence.md) and [pose-manifest.md](references/pose-manifest.md).

Consult [official-sources.md](references/official-sources.md) when a Blender behavior or API detail affects a decision.

## Enforce the deformation barrier

Do not try to repair absent articulation topology by repeatedly changing bone roll, weights, angles, Preserve Volume, or shape keys. Stop rigging and identify a topology repair when any intended joint lacks usable bend loops, digits are fused, the mesh has a hole or internal tunnel near deformation, or prior tests produce tearing, voids, spikes, hooks, or collapse.

When Mode 1 fails, skip Modes 2–4. Run only non-mutating Mode 5 inspection/evidence to record the HOLD and the exact failed joint regions.

For hands, require these proof states before authoring a combat action: open, relaxed, half curl, closed fist, thumb opposition, individual index flexion, and wrist flexion/extension.

A closed fist must place fingertips toward the palm, lock the thumb naturally outside the fingers, preserve the knuckle block and palm/thumb-pad volume, and avoid intersections visible at game distance.

## Prefer deterministic execution

Use Blender background mode for audits and evidence when practical:

```text
blender --background character.blend --python scripts/blender_character_audit.py -- --output audit.json --joint-contract joints.json
blender --background character.blend --python scripts/render_pose_suite.py -- --manifest poses.json --output-dir renders --report render-report.json
python scripts/compare_audits.py baseline.json candidate.json --output comparison.json --strict --expected-changes expected.json
```

Scripts inspect or render but never save over the source `.blend`. Keep manual sculpting, retopology, weighting, and keyframing inside the explicitly authorized character copy.

## Keep changes bounded

- Record source path/hash, output path, Blender version, character and rig identities, topology counts, and action contract.
- Separate mesh repair, rigging, action creation, export, and Unity integration into independently reviewable outcomes.
- Permit one normal build and one bounded correction for the same defect. Repeated failure means the method or prerequisite is wrong; stop and redesign instead of renaming the retry.
- Never claim a render proves UV bytes, topology identity, weights, or hidden intersections. Pair visual evidence with structured audits.
- Preserve non-target geometry, materials, textures, UVs, armatures, actions, and source bytes unless the authorization explicitly includes them.

## Completion report

State which stages completed; source and output identities; topology, bone, weight, action, and render evidence; visual defects or remaining risks; and the narrow next readiness state supported by evidence.
