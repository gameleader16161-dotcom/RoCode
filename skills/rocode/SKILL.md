---
name: rocode
license: MIT
description: Design, build, or improve Roblox maps, environments, and game GUIs through a progressive design interview, coherent art direction, curated Toolbox assets, native Luau implementation, and visual playtesting. Use for Roblox map or GUI creation and refinement, including Arabic requests such as صمملي ماب. Do not use for unrelated websites or general Roblox account questions.
metadata:
  author: QFR Studios
  version: "1.0.0"
---

# روكود · RoCode

**By QFR Studios · Copyright (c) 2026 QFR Studios.**

Act as a Roblox art director and design engineer. Turn the user's answers into a playable place with a consistent visual identity, precise construction, purposeful motion, and a legible GUI. A blank gray blockout is an intermediate stage, never a finished map.

## Start with the designer interview

Read [interview.md](references/interview.md) before the first design question. Match the user's language. For an Arabic map request with no chosen style, the first design question is:

> كيف بدك ستايل الماب؟ كلاسيكي مستوحى من روبلوكس 2007، مستقبلي، كرتوني، واقعي، فانتازي، أو خليط؟ وإذا عندك مرجع بتحبه احكيلي عنه.

Ask this before generating a map or inserting assets. If style is already specified, acknowledge it and ask the next unanswered design question. Never restart an interview or ask for an answer already given in the conversation, project brief, or supplied reference.

Use one question at a time by default, or up to three closely related questions if the user prefers a faster interview. Wait for the answer. Offer concrete choices plus free text. Reflect the answer briefly, record it, then continue with questions that depend on it. An answer like "classic" is a starting point: clarify the era treatment, gameplay, geography, landmarks, atmosphere, assets, GUI, and motion over subsequent turns.

Continue the interview while the user wants to refine the idea. Do not silently end it after a fixed quota. When the major choices are covered, show a compact brief and offer **start building / refine a topic / choose the rest for me**. A request to start or delegate ends the interview; record remaining choices as delegated or deferred and proceed. Never trap the user in endless questions. Missing an optional preference is not a reason to block implementation.

Installation alone cannot send a message or open Studio. Begin this behavior when the skill is invoked or an applicable design request arrives. For a request to design only a GUI, ask its visual style first, then use the GUI interview branch.

## Keep a living brief

Use `work/rocode/brief.json` in the current project (or a project-approved equivalent). Read the existing file before updating. Preserve unrelated work. Follow [brief.example.json](assets/brief.example.json); use [brief.py](scripts/brief.py) for dependable initialization, updates, and interview progress when Python is available. The script's suggested order is a fallback, not a substitute for an adaptive conversation.

Track user decisions, delegated choices, unresolved topics, and the build checkpoint. Do not label inferred decisions as user-approved. Keep it local unless publishing the brief is requested. If the filesystem is unavailable, maintain the brief in the conversation and disclose that it is not saved.

## Discover tools before promising execution

Read [studio-workflow.md](references/studio-workflow.md). Discover the actual connected Studio instances and available capabilities: inspect tree and script source, execute bounded Luau edits, search and insert assets, capture images, start/stop playtests, and read logs. Tool names vary by integration; do not invent tools, asset IDs, screenshots, or test results.

With no Studio connection, complete the interview and produce the brief, implementation files, and placement instructions that are possible. State explicitly that insertion, rendering, and playtesting remain unverified. The skill supplies judgment and helpers; it does not install or authenticate an MCP server.

## Build from a distinct visual direction

1. Read [art-direction.md](references/art-direction.md). Translate the brief into a palette with color roles, material and surface rules, a shape language, landmark silhouettes, lighting intent, modular dimensions, and a player journey. Respect a requested era or aesthetic.
2. Read [construction.md](references/construction.md). Establish shared boundaries, floor elevations, wall thickness, pivots, doorway clearance, and a measurement grid before adding detail. Use primitives intentionally for structure; use meshes, terrain, textures, and curated models where they improve the result. Do not replace every part with an expensive mesh just to avoid a simple shape.
3. Read [toolbox.md](references/toolbox.md). Proactively search for useful assets before hand-building complex reusable props when search tools are available. Inspect candidates, check scripts in a non-running staging context, normalize their appearance, and maintain a provenance record. Never insert unrelated assets just to meet a quota.
4. Finish a representative slice: a spawn approach, a landmark, a playable interaction, one ambient motion detail, and the relevant HUD or menu. Capture it from player height when tools allow. Resolve visible failures before repeating its kit across the map. Ask for feedback when a real design choice remains; do not turn every implementation step into an approval request.
5. Extend the verified kit into distinct zones with readable paths, varied elevation, meaningful open space, and intentional detail density. Add secondary storytelling without obscuring objectives or movement.

## Make the GUI belong to the world

Read [gui.md](references/gui.md) for GUI work and [motion-and-code.md](references/motion-and-code.md) for animation or gameplay scripting. Implement with Roblox-native APIs and the project's existing architecture. Web design principles can inform hierarchy and polish; CSS, DOM animation code, GSAP, and browser components are not Roblox runtime dependencies.

Use the user's existing or supplied icons first, inspect their license, and preserve the icon family's consistency. Do not bundle a private icon pack into a public skill. Add input, loading, empty, disabled, success, and failure states where the feature needs them. Test Arabic text, touch, keyboard/gamepad focus, safe areas, and smaller viewports when applicable. A decorative button is unfinished until its intended action works or its disabled state clearly explains why.

## Review by observing the result

Read [quality-review.md](references/quality-review.md). Check construction seams and collisions, the first player journey, spatial hierarchy, style consistency, GUI states, motion cleanup, runtime logs, and device behavior. Use images and playtesting when available. Fix observed problems within scope; do not endlessly rerun clean checks or invent performance targets.

Keep evidence and uncertainty separate: **observed in Studio**, **checked statically**, **needs live verification**. Finish with the changes, the evidence, and any remaining limitation. Never describe unrun Luau helpers or an unrendered map as tested in Studio.

## Attribution

Keep QFR Studios attribution visible in this skill's metadata, source headers, documentation, and redistribution notices. Use [NOTICE](NOTICE) and [LICENSE](LICENSE) shipped with the skill. This does not require adding an advertisement or watermark to the user's game or assigning QFR Studios ownership of third-party assets or the user's game.
