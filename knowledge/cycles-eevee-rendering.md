# Cycles and EEVEE rendering

## Scope

Use for render-engine selection, sampling, denoising, light paths, GPU/CPU devices, temporal stability, memory/performance, and final output.

## Choose the engine from the acceptance contract

**Cycles** is appropriate when path-traced light transport, engine-supported physical effects, or final fidelity dominate. **EEVEE** is appropriate when interactivity, raster performance, stylized output, or real-time-like constraints dominate. Workbench is appropriate for technical/modeling previews.

Do not frame the choice as “good versus fast.” Ask:

- Which light/material/volume/transparency effects are required?
- Is exact Cycles/EEVEE parity required?
- What is the per-frame and total render budget?
- Is the output still, animation, viewport capture, or interactive experience?
- Which passes and compositing controls are required?
- What hardware, VRAM/RAM, backend, and farm environment are available?

**[5.2]** EEVEE is an interactive raster engine with documented limitations: screen/depth approximations, feature differences, half-precision constraints in parts of the pipeline, GPU-only rendering, no multi-GPU support, and platform/headless caveats. Check the specific limitation rather than increasing generic “quality.”

## Cycles convergence

**[Evergreen]** Path tracing is stochastic. Diagnose the noise source:

- direct-light sampling;
- diffuse/glossy/transmission paths;
- small bright emitters or caustics;
- volumes;
- motion blur/depth of field;
- insufficient path contribution or fireflies;
- denoiser input quality.

Method:

1. Render a small crop at final resolution and representative frame.
2. Inspect noisy passes/regions and material/light paths.
3. Fix lighting/material pathologies before globally multiplying samples.
4. Use adaptive sampling and noise threshold based on visual target.
5. Tune bounce limits only with side-by-side evidence; lower bounces can alter energy, not just speed.
6. Use clamping only when accepted bias is preferable to rare high-energy samples.
7. Evaluate denoising for detail loss and temporal artifacts, not only still-frame cleanliness.

More samples reduce random variance but do not fix wrong normals, missing UVs, firefly-generating shader design, insufficient geometry, bad color management, or deterministic EEVEE artifacts.

## EEVEE method

- Identify whether the effect depends on off-screen information, multiple depth layers, transparent sorting, accurate refraction, light probes, shadow memory, or an unsupported node.
- Build reflection/probe/raytracing and thickness strategies explicitly.
- Validate camera-edge behavior and occlusion because screen/depth techniques can fail there.
- Test blended and dithered materials under the actual pass/raytracing requirements.
- Profile the target GPU; viewport speed on the authoring workstation is not the delivery budget.

## Device and memory

For Cycles, select supported CPU/GPU backends using the 5.2 Manual and current driver requirements. Benchmark the actual scene or representative scenes. Blender Open Data is useful for render throughput, not for capacity or every workflow.

When GPU rendering fails:

- inspect backend/device selection and scene Render Device;
- record driver, GPU, VRAM, Blender patch, and kernel/console error;
- compare CPU and GPU on the same frame;
- reduce memory dimensions independently: textures, subdivision, curves/hair, volumes, geometry, passes, and persistent data;
- do not interpret slow system-memory spill as healthy VRAM fit.

## Temporal rendering

For animation:

- render an image sequence, not a single long video, when recoverability and compositing matter;
- test high-motion, transparency, volume, depth-of-field, and lighting-change frames;
- inspect denoising flicker, sample-pattern noise, fireflies, shadow/reflection popping, and simulation/cache stability;
- use identical seeds/settings only when they produce the intended temporal behavior;
- encode/mux after the image sequence has passed review.

## Output and color

Use OpenEXR when the pipeline needs scene-linear HDR, multiple passes, or compositing latitude. Record channels, bit depth, compression, view transform policy, and premultiplication. A display transform belongs in review/delivery according to the color contract, not silently in the working render.

**[5.2]** Render output saving behavior and File Output controls changed in 5.2. Automation should set and verify actual output behavior rather than assuming older defaults.

## Validation gates

- Engine choice is tied to required effects and budget.
- Representative frames/crops pass at final resolution.
- Cycles noise is characterized by pass/path; denoise does not erase required detail or flicker.
- EEVEE limitations are tested at camera edges, occlusion, transparency, probes, and target GPU.
- Device/backend/driver and memory peak are recorded.
- View layers, passes, color config, view, exposure, format, bit depth, channels, and output path match delivery.
- Animation is recoverable as a verified sequence before final encoding.
- Render logs and output files confirm completion; a zero exit code alone is not visual acceptance.

## Failure signatures

| Symptom | Discriminating test |
| --- | --- |
| Noise remains after large sample increase | Inspect specific pass/path, small emitters, caustics, volumes, and shader energy |
| Denoised animation crawls/flickers | Compare raw sequence and temporal detail at representative motion |
| GPU out of memory | Reduce one residency class at a time; compare peak VRAM and CPU render |
| EEVEE reflections vanish off-screen | Test documented screen/depth limitations and probe/raytracing alternatives |
| Render is saved with wrong appearance | Separate scene-linear pixels, view transform, output encoding, and external viewer |
| Farm differs from workstation | Compare exact Blender patch, dependencies, paths, devices, OCIO, and environment |

## Authoritative anchors

- [Blender 5.2 Cycles render settings](https://docs.blender.org/manual/en/5.2/render/cycles/render_settings/index.html)
- [Blender 5.2 EEVEE limitations](https://docs.blender.org/manual/en/5.2/render/eevee/limitations/limitations.html)
- [Blender 5.2 Rendering release notes](https://developer.blender.org/docs/release_notes/5.2/rendering/)
- [Blender Open Data](https://opendata.blender.org/about/) for versioned render benchmarks
- [OpenEXR technical introduction](https://openexr.com/en/latest/TechnicalIntroduction.html)
- [Stanford CS 348B](https://graphics.stanford.edu/courses/cs348b-03/) for evergreen sampling and light transport
