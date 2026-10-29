# Precise modular construction

Copyright (c) 2026 QFR Studios.

## Agree on coordinates

- Use one local origin per building or kit, explicit pivots, a shared module size, wall thickness, floor level, and trim profile. Grid spacing is project-dependent; do not hardcode a universal stud value.
- Calculate shared boundaries once. Derive adjoining positions from endpoints and dimensions rather than independently guessing their centers.
- Measure avatar width, height, and required movement for the intended rig. Test stairs, jumps, head clearance, doorway openings, and camera passage in play mode.
- Keep visual seams intentional: panel joints, door openings, and expansion joints are not automatically defects. Record intended openings in the brief or kit notes.

## Continuous wall example

For a wall along a floor-plane segment A→B at the same base height:

`length = |B - A|`, `center = (A + B)/2 + Vector3.yAxis * height/2`.

A Part with `Size = Vector3.new(thickness, height, length)` and `CFrame.lookAt(center, center + (B-A).Unit)` spans the segment along local Z. See [Geometry.luau](../assets/Geometry.luau). Reject zero-length or sloped floor segments unless the builder explicitly supports them. Part endpoints are centerline boundaries; choose one corner join strategy rather than treating thick perpendicular walls as magically flush.

At corners choose a butt joint, a corner post, or a deliberately overlapping structural join. Avoid coplanar visible overlays that cause z-fighting. For openings, derive left/right jambs and lintel from the same opening bounds.

## Gap diagnosis

1. Identify the affected pair and intended shared edge, not every possible pair in the entire place.
2. Compare face separation along the intended normal and tangential overlap in the pair's local geometry.
3. For axis-aligned modules, compare min/max bounds with a project-appropriate tolerance. A world-axis bounding box can be a candidate filter, not proof for rotated parts or meshes.
4. Use oriented bounds or actual face geometry for rotated pieces; inspect visually for irregular meshes and CSG.
5. Correct the source dimensions/pivots or kit placement logic. Do not hide a floor hole under clutter.

`Geometry.seamOnAxis` handles **same-rotation rectangular block pairs only**, in A's local axes. Its limitation is deliberate. Do not claim it detects arbitrary map holes, openings, overlapping meshes, or the manifold quality of terrain.

## Physical and visual checks

- Anchor structural geometry deliberately. Decide collision separately from appearance; small decorative props often do not need collision.
- Preserve intended gameplay physics, constraints, and moving parts. Do not anchor every descendant indiscriminately.
- Check duplicate geometry, floating props, stair lips, hidden collision walls, blocked spawn points, and parts crossing paths.
- Reuse logical assemblies. Avoid a single monolithic script that generates an entire place, GUI, economy, and effects in one unreviewable operation.
- Build in bounded batches, yield appropriately, inspect counts, and use undo/checkpoints supported by the connected tooling. Do not freeze Studio with huge loops.

The read-only helper [SceneAudit.luau](../assets/SceneAudit.luau) lists actionable **candidates** under an explicitly supplied root. It never removes scripts, anchors parts, repairs a map, or proves an asset safe.
