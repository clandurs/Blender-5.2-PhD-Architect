# Rigging, Weights, and Correctives

Use Rigify when an animator-facing control rig helps. Fit its metarig to the actual mesh before generation. Use a minimal deform skeleton when an engine, existing hierarchy, or bone contract controls compatibility.

Place joint pivots at real bend rows. Normalize bone roll and local flexion axes so each digit curls in its measured plane. Treat thumb opposition as a separate compound motion.

Weight in this order: wrist/palm ownership; isolated digit chains; proximal-to-distal transitions; normalization and target influence ceiling (commonly four for game assets); seven-state deformation tests; Preserve Volume comparison.

Add correctives only after topology, pivots, axes, and weights pass. Drive local shapes from the smallest stable bone-transform set. Correct knuckle, palm, thumb-pad, and web-space volume; never conceal torn or missing topology. Test intermediate values as well as the final fist.
