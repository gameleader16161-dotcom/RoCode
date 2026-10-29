# Evidence-based quality review

Copyright (c) 2026 QFR Studios.

Finish only the checks relevant to the requested work. Resolve visible defects in scope and report unavailable checks without pretending to pass them.

| Dimension | Acceptance evidence | Typical repair |
|---|---|---|
| Identity | Player-height view matches agreed style, palette, and landmark | Fix material/shape mismatch; remove unrelated props |
| Construction | Intended structural joins are continuous; no unintended floor holes or z-fighting | Correct kit boundaries, pivots, or dimensions |
| Playability | Spawn → first task → next objective works with intended avatar | Adjust collision, clearance, route, or checkpoint |
| Composition | Main route and objective are readable; zones have distinct roles | Change hierarchy, sightline, grouping, or lighting |
| Materials | Texture density and face treatment fit object purpose and scale | Normalize imported assets; simplify noisy regions |
| GUI | Required actions and state transitions work; no critical clipping at target sizes | Repair layout, constraints, focus, and feedback |
| Motion | Rapid reversal works; effects clean up; reduced-motion path remains legible | Cancel stale tweens, disconnect, gate decorative loops |
| Code | No new relevant runtime errors; server validates important outcomes | Fix actual failures and authority boundaries |
| Assets | Inserted assets have provenance and script-review status | Stage, inspect, replace, or document unknowns |
| Performance | Representative measurement on agreed targets, if tools exist | Reduce expensive density/replication/effects; remeasure |

## Review sequence

1. Look at the representative slice from player height and the first intended approach. Check silhouette, value grouping, surface scale, and accidental seams in one pass.
2. Walk the first player journey. Test intended openings, stairs, moving elements, camera clearance, and interaction feedback.
3. Test GUI at target sizes and relevant inputs. Include long text, empty/full state, an error, rapid open/close, and motion preferences where supported.
4. Inspect relevant logs and available performance measurements. A clean edit-time audit is not a playtest.
5. Fix the demonstrated issues, then repeat only checks affected by the repair or remaining uncertainty.

Use these labels in the final report:

- **Observed in Studio:** rendered screenshot or actual playtest, with view/device/context.
- **Checked statically:** source, dimensions, or hierarchy inspected without runtime proof.
- **Needs live verification:** exact remaining action and why it could not be performed.

Do not assign yourself a "10/10" score as evidence. A generated JSON brief is not a completed map. A seam helper only checks its supported geometry, and an asset scan does not certify safety.
