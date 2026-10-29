# Art direction that changes construction decisions

Copyright (c) 2026 QFR Studios.

## Make a compact visual contract

Record five concrete decisions before detail work:

1. **Visual thesis:** one sentence connecting setting, era, and mood. Example: a sunny classic harbor with oversized industrial silhouettes and a warm lighthouse as the destination.
2. **Color roles:** large-area base, secondary structure, focal accent, interaction cue, and danger cue. Record actual Color3 values or hex values. Do not use the same saturated accent on every object.
3. **Shape language:** proportions, roof/edge treatment, modular sizes, and a few repeated motifs. Repeat a motif deliberately, then vary scale and use by zone.
4. **Material grammar:** which material or surface belongs on each object family; density and texture scale at player distance; exposed vs hidden faces.
5. **Lighting and depth:** key direction, readable shadow, foreground/midground/background separation, landmark visibility. Keep exposure and bloom subordinate to legibility.

Save the contract with the brief; let an existing project design document remain authoritative when preserving a place.

## Style examples, not mandatory presets

| Direction | Forms and surfaces | Lighting and GUI |
|---|---|---|
| 2007-inspired classic | Strong simple silhouettes, limited bright palette, purposeful studs/inlets, modular structures | Clear daylight; square, crisp panels and readable labels |
| Modern classic | Classic geometry and surface rhythm with richer prop composition and restrained edge detail | Better depth and atmosphere; classic character with modern usability |
| Futuristic | Deliberate panel seams, structural frames, contrasting dense and quiet areas | Emissive accents as guidance; no bloom fog hiding all geometry |
| Cartoon | Chunky readable proportions, curated textures, exaggerated landmark silhouette | Broad value groups; expressive cohesive icon family |
| Realistic | Believable scale, material transitions, restrained wear, sourced meshes where needed | Consistent light and material response; subdued HUD hierarchy |

## Surface decisions

What the user calls an old "patterned part" may mean Studs, Inlet, or Universal. These belong to the legacy `SurfaceType` API; joint behavior is deprecated. Verify current Roblox documentation and actual rendering before choosing a legacy visual technique. Do not use Hinge/Motor surfaces to build working mechanisms; use modern constraints or appropriate animation.

Use modern Materials, textures/decals, mesh detail, or SurfaceAppearance on MeshParts where appropriate. Do not imply SurfaceAppearance works as a universal texture component on ordinary Parts. Do not promise the exact historic 2007 rendering from a current enum alone.

Choose exposed face treatment by purpose:

- Classic walkway: a consistent pattern on its visible top can reinforce the style; sidewalls can stay quieter.
- Structural wall: material and proportion first; a trim, inset, or alternating module can articulate its scale.
- Machine: coherent casing, controls and fasteners; a few high-value details near interaction points.
- Water, glass, foliage: use their own material logic instead of applying studs indiscriminately.

Smooth surfaces are useful breathing space. Ban accidental unfinished default blocks, not intentional simplicity. Avoid adding six decals per part or thousands of decorative micro-parts when one texture/mesh solves the visual need.

## Composition and environmental story

Stage the player view with a nearby frame, a readable playable middle distance, and a landmark beyond. Give each zone a memorable silhouette or role. Place decorative clusters near meaningful transitions; leave movement lanes and useful negative space clear.

For each detail ask: does it improve silhouette, material read, interaction, navigation, or story? Remove repetitive noise that helps none of those. An intentionally empty plaza is different from an unfinished map; accidental construction holes are a separate defect.
