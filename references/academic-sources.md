# Academic computer-graphics sources

Verified: **2026-08-30**. These sources support **[Evergreen]** principles. They do not define Blender 5.2 UI, API, exporter, or render-engine behavior.

## Core curricula

### MIT OpenCourseWare — 6.837 Computer Graphics

[Course page](https://ocw.mit.edu/courses/6-837-computer-graphics-fall-2012/)

Institutional scope: transformations, the graphics pipeline, ray tracing, texture mapping, shadows, sampling, global illumination, splines, animation, and color.

Use it to explain:

- coordinate transforms and camera projection;
- sampling, aliasing, reconstruction, and why “more samples” is not a universal fix;
- local versus global illumination;
- texture mapping and animation fundamentals.

Do not use its historical software details as modern workstation or Blender guidance.

### Carnegie Mellon Graphics — 15-362 / 15-462

[Current CMU Graphics course index](https://graphics.cs.cmu.edu/courses/) and [15-462/662 course description](https://15462.courses.cs.cmu.edu/spring2023/courseinfo)

Institutional scope: geometry, rendering, animation, imaging, sampling, parameterization, subdivision, meshing, spatial structures, radiometry, reflectance, path tracing, physically based animation, inverse kinematics, and numerical methods.

Use it to reason about:

- mesh representation and parameterization;
- subdivision and surface continuity;
- Monte Carlo variance and importance sampling;
- kinematics, skinning assumptions, and physical integration;
- the difference between an algorithmic cause and a Blender UI symptom.

### Stanford Computer Graphics Laboratory

[Graphics course catalog](https://graphics.stanford.edu/courses/) and [CS 348B image-synthesis course](https://graphics.stanford.edu/courses/cs348b-03/)

Institutional scope: geometric transformations, cameras, sampling, reflection, texture, radiometry, Monte Carlo integration, light transport, volume scattering, and physically based rendering.

Use it to explain:

- lens/projection choices independently of Blender controls;
- BRDF/BSDF intuition and energy behavior;
- path-tracing noise sources;
- why light size, distance, solid angle, and material roughness interact;
- the mathematical meaning behind render settings.

## How to cite academic material

Use academic sources for the principle, then pair them with a Blender 5.2 source for the control that implements or approximates it. Example:

> **[Evergreen]** Monte Carlo estimators converge statistically; structured noise can remain objectionable at finite samples. **[5.2]** Cycles exposes adaptive sampling and denoising controls documented in the 5.2 Manual.

Avoid claims like “CMU recommends this Blender modifier order.” A course may explain evaluation or geometry, but the Blender Manual defines the modifier stack.

## Evidence cautions

- Course material may be old while the mathematics remains valid. Label the principle, not the software environment, evergreen.
- A lecture overview establishes topic authority but may not justify a precise formula. Link a specific lecture or primary paper when exact derivation matters.
- Artistic heuristics such as edge-loop placement, visual hierarchy, or appealing timing need task-specific evaluation; they are not mathematical laws.
- University affiliation does not automatically make every hosted student artifact authoritative.
