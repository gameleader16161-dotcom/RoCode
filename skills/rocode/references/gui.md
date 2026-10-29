# Roblox GUI craft

Copyright (c) 2026 QFR Studios.

## Choose a coherent system

Extract the world's palette, shape language, and tone. Define text roles, spacing steps, panel treatment, outline use, icon family, control states, and motion tokens in one reusable theme ModuleScript. Respect the existing UI architecture, including frameworks already in the project.

Ask whether the GUI should follow the world literally or form a quieter functional layer. A classic place can have square, crisp panels; it does not require illegible tiny text. A cartoon UI can be expressive without outlining every label equally.

Use supplied/local icon packs when available and licensed. A private pack path is user-specific context, not a public dependency. Inspect licenses and keep required notices. Never substitute emoji as production icons simply because they are easy to type, and do not claim third-party icon authorship.

## Layout and legibility

- Use AnchorPoint, UDim2, layouts, padding, and constraints intentionally. Combine scale for responsive placement with offsets for stable spacing; do not stretch every control with raw screen percentages.
- Use UIListLayout/UIGridLayout for repeated controls, UIPadding for consistent inset, and AutomaticSize or ScrollingFrame canvas sizing when content varies.
- Use UISizeConstraint, UIAspectRatioConstraint, and UITextSizeConstraint where needed. TextScaled without bounds can make labels unreadable; prefer a deliberate text hierarchy and enough room for translation.
- Test actual Arabic strings and mixed Arabic/Latin numbers. Do not reverse characters manually. Check reading order, punctuation, line breaking, truncation, and directional icons using the current engine's supported localization features.
- Keep frequently changing counters stable in width. Use an appropriate available font and adequate reserved space rather than pretending browser `font-variant-numeric` exists in Roblox.
- Use ScreenGui safe-area behavior appropriate to the target platform; check top bar, device cutouts, touch controls, and modal overlap in the emulator.
- Aim for touch targets around 44×44 screen pixels or larger at the tested viewport, with separation. Verify AbsoluteSize on device; Roblox offsets and final physical pixel size need inspection under scaling.
- Match icons' optical weight and alignment with labels. Use a consistent family; silhouettes and transparent padding can make mathematically centered art look off-center.

## Interaction and state

Use GuiButton.Activated for actions that need mouse, touch, and gamepad compatibility. Hover can enrich desktop behavior but cannot be the only cue. Set up sensible Selectable behavior, visible focus/selection, and navigation where gamepad/keyboard operation is required.

Define the actual action and all relevant states before polishing: default, selected, pressed, unavailable, loading, empty, success, and error. A purchase needs server-confirmed results and failure handling; a nice-looking fake purchase button is not complete. Restore focus after closing a modal and avoid duplicate activations.

Motion guidelines are in [motion-and-code.md](motion-and-code.md). Prefer subtle press feedback and short contextual transitions. Do not replay a grand entrance every time a player opens a high-frequency inventory panel. Keep key information visible when reduced motion is enabled.

## Verification matrix

Check small portrait/landscape phone, tablet if targeted, and desktop using the connected device simulator when available. Test long translated labels, zero and large counter values, empty/full inventory, slow response, errors, and rapid open/close. Inspect the actual rendered GUI in play mode; edit-time trees alone cannot establish usability.

References: [Size modifiers and constraints](https://create.roblox.com/docs/ui/size-modifiers), [Position and size UI objects](https://create.roblox.com/docs/ui/position-and-size).
