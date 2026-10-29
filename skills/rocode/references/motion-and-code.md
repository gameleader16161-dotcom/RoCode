# Motion and maintainable Luau

Copyright (c) 2026 QFR Studios.

## Purposeful movement

Use motion to explain an action, focus attention once, or suggest life: a door, a fan, a buoy, a readable objective marker. Do not animate every prop. Match motion to its physical purpose; avoid fake bobbing on heavy fixed machinery.

Implement with TweenService, AnimationController/Animator, appropriate constraints, or other native Roblox APIs. Pick physics for physical interaction and cosmetic client animation for non-authoritative decoration when appropriate. Do not assume old Hinge or Motor surface settings provide working modern mechanisms.

Suggested **starting values**, adjustable to context:

| Role | Duration | Motion |
|---|---|---|
| Press feedback | 0.10–0.15 s | Small UIScale change; retain color/focus feedback |
| Hover/focus | 0.15–0.20 s | Small value or position change |
| Panel open | 0.20–0.30 s | Short translation and fade; no giant zoom |
| Panel close | 0.12–0.20 s | Quicker, smaller departure |
| One-time group entrance | 0.03–0.05 s stagger | Small bounded group; no long serial wait |

Keep a single motion token module. Cancel or retarget active tweens before starting replacements, retain current values for smooth interruption, and prevent stale completion handlers from hiding reopened panels. Disconnect events and cancel owned animations when UI/controllers are destroyed.

Provide a reduced-motion preference when the scope includes motion settings. Honor engine/device preferences if the current API supports them and they are actually available. Disable decorative loops and replace large movement with static cues or gentle fades. Never invent a browser `prefers-reduced-motion` API inside Luau.

No permanent per-part Heartbeat connection for thousands of decorations. Use bounded controllers, distance/visibility gating, shared updates, or authored animations, then profile representative hardware. Measure draw calls, frame time, instances, memory, and replication where tools expose them; do not promise an FPS figure from static code.

## Code architecture

- Separate generated map structures, client GUI/controllers, shared configuration, and authoritative server gameplay. Extend existing architecture instead of adding a competing framework.
- Favor small ModuleScripts with explicit responsibility. Use strict typing where compatible with the project; avoid remote `loadstring` and opaque runtime dependencies.
- The server validates type, range, context, permissions, and rate of client requests. It owns currency, inventory, progression, damage, and shared outcomes. A client button may request a reward; it cannot grant one authoritatively.
- Treat Instance lifetimes and connections explicitly. Avoid duplicate event connections when reopening a panel or re-running setup.
- Save the project with native undo/checkpoints or source control as available before bulk changes. Work in small batches, check logs, and do not remove unrelated scripts or replace the whole place to fix one corner.
- Validate the current API from official documentation for unfamiliar or version-sensitive behavior. Do not port CSS, browser DOM code, GSAP, or web rendering assumptions into Roblox.

Reference: [Securing the client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary).
