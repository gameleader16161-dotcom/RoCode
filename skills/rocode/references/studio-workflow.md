# Tool capability adapter and execution checkpoints

Copyright (c) 2026 QFR Studios.

The installed integration defines what is possible. Discover tools and read their parameter schemas rather than copying imaginary calls from a tutorial. Some Studio integrations expose `list_roblox_studios`, `search_game_tree`, `script_read`, `execute_luau`, `search_asset`, `insert_asset`, and `screen_capture`; these names are examples, not guaranteed APIs.

## Capability → workflow

| Available capability | Use | When absent |
|---|---|---|
| Studio discovery | Select intended instance/place; use its observed ID | Do not guess a place ID |
| Tree/property inspection | Read existing map, GUI, scripts, and scope | Ask only if target ambiguity blocks a safe edit |
| Script source inspection | Inspect third-party and incumbent behavior | Do not claim an asset's scripts were reviewed |
| Asset search + insertion | Curate suitable models into a safe staging context | Use original kit or provide sourcing suggestions |
| Bounded Luau execution | Build/edit scoped assemblies and run explicit diagnostics | Deliver source and placement instructions |
| Screen capture | Review actual scene and GUI at player height | State visual verification remains pending |
| Play/stop and logs | Verify routes, interactions, GUI state, errors | State runtime verification remains pending |
| Device simulation | Test required viewport/input combinations | Provide a concrete remaining device test list |
| Performance profiling | Measure representative scenes and effects | Avoid numeric performance claims |

Avoid changing camera or simulator settings permanently unless that is the requested output; restore temporary inspection settings where possible.

## Stages

**Interview:** no scene mutation while the user is still selecting design direction. Read-only inspection is allowed.

**Representative slice:** after the user says start or delegates the remaining choices, create scoped folders/models with clear names. Keep originals intact when revising an existing asset. Make one coherent slice with working movement and interaction, then inspect it.

**Expansion:** reuse dimensions and visual rules from the checked slice. Make reversible batches, yield during heavy work according to tool guidance, and inspect errors before continuing.

**Review:** use [quality-review.md](quality-review.md). Store observations, fixes, screenshots if available, and open verification items in the project's work directory. Never substitute a fabricated screenshot for missing access.

**Delivery:** provide changed scope, tested evidence, known limits, and how to run the result. Publishing a Roblox experience, buying an asset, or uploading third-party content requires the user's authorization for that action; map design permission alone is not publication permission.

## Reusable helpers

The shipped `assets/Geometry.luau` and `assets/SceneAudit.luau` are original source modules. Inspect them, copy only needed helpers into the project's normal module location, and load them from that known local instance. Do not call an unknown asset ID through `require`. They are not automatically inserted or executed when the skill is installed.
