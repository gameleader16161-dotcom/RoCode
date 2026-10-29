# The RoCode design conversation

Copyright (c) 2026 QFR Studios.

The interview is a conversation across turns, not a form dumped into one response. Read the existing brief and the user's current request first. Ask only unresolved questions that change the design. Default to one per turn; do not send every question below at once.

## Conversation rules

- First unknown for map creation: **visual style**. Offer classic 2007-inspired, futuristic, cartoon, realistic, fantasy, hybrid, or the user's own description. Do not interpret the word "virtual" as an established Roblox property. Clarify whether it means surfaces, texture detail, atmosphere, or something else.
- Acknowledge an answer in one sentence and connect the next question to it: "تمام، كلاسيكي بألوان زاهية. شو نوع اللعب اللي بدك الماب تخدمه؟"
- Give about three useful choices when possible. "اختار عني" is always valid. Allow answers with images, references, free text, or multiple preferences.
- Save decisions with their origin. Mark your suggestions as proposed until accepted or delegated. User corrections supersede previous answers; update dependent decisions rather than keeping contradictory requirements.
- If the user answers several topics together, record all of them. Do not ask them again in the scheduled order.
- A supplied detailed brief can answer the entire interview. Do not force the style question when already answered.
- "ابدأ", "كفاية أسئلة", "اختار الباقي", "surprise me", or equivalent means proceed with explicit assumptions. Ask further only for a concrete blocker, such as an ambiguous destructive target or necessary missing tool access.
- "اسألني أكثر" means continue into the relevant detail branch. There is no mandatory maximum number of turns. Once the brief is actionable, offer the user control of when to build.
- Do not build, insert, or change the place while awaiting design answers. Read-only inspection and reference research may continue if useful.
- For an existing-place refinement, inspect the affected area and preserve the incumbent identity unless a redesign was requested. Scope the interview to what changes.

## Adaptive question bank

The order after style is flexible. Choose questions by their effect on the next design decision.

| Topic | Natural Arabic question / choices | Design consequence |
|---|---|---|
| Style | كيف بدك ستايل الماب؟ كلاسيكي، مستقبلي، كرتوني، واقعي، فانتازي، أو خليط؟ | Surface, silhouette, palette |
| Classic branch | قريب من 2007 فعلًا، ولا كلاسيكي مطوّر بتفاصيل وإضاءة أحدث؟ | Fidelity vs reinterpretation |
| Gameplay | شو نوع اللعبة؟ أوبي، محاكاة، قتال، استكشاف، رعب، أو فكرة ثانية؟ | Route, pacing, collision, sightlines |
| Audience | لمين التجربة، وبأي لغة؟ وفي شي لازم نراعيه بالقراءة أو الحركة؟ | Readability, tone, localization |
| Setting | وين بدك العالم؟ مدينة، جزيرة، مختبر، فضاء، غابة، أو غيره؟ | Geography, asset families |
| Scope | بدك لوبي، مرحلة واحدة، ولا عالم بمناطق؟ وقديش تقريبًا عدد اللاعبين؟ | Density, scale, spawn planning |
| Devices | موبايل وكمبيوتر، ولا كمان كنترولر؟ وأي جهاز نعتبره الحد الأدنى؟ | GUI and performance targets |
| Journey | شو أول شي اللاعب يشوفه ويعمله، ووين بده يوصل؟ | Landmark and first minute |
| Zones | شو المناطق الأساسية، وكيف بدك ترتبط ببعض؟ | Adjacency and navigation |
| Landmark | شو العنصر المميز اللي بدك اللاعب يتذكره؟ برج، بوابة، شجرة، سفينة؟ | Identity and focal point |
| Mood | جو مشمس ومريح، ليلي ونيون، غامض، أو غيره؟ | Lighting, sound, contrast |
| Palette | عندك ألوان أساسية أو ألوان ما بتحبها؟ | Color roles |
| Surface | بتحب النتوءات الكلاسيكية وين؟ الأرضيات، الأسطح العلوية، ولا بشكل محدود؟ | Material placement |
| Assets | نستخدم أصول مجانية مناسبة من الـToolbox؟ عندك باك أو موديلات نبدأ فيها؟ | Sourcing strategy and rights |
| Budget | نعتمد المجاني فقط؟ أي أصل مدفوع يحتاج قرارك قبل شرائه. | No assumed spending |
| Motion | شو الأشياء اللي بدك فيها حركة؟ أبواب، مراوح، منصات، مياه، نباتات؟ | Interaction and ambient detail |
| GUI | شو الواجهات المطلوبة؟ HUD، متجر، إنفنتوري، مهام، إعدادات، أو غيرها؟ | UI scope; "none" skips GUI branch |
| GUI branch | بدك الواجهة كلاسيكية مربعة، كرتونية بأيقونات مرسومة، ولا نظيفة وخفيفة؟ | Typography, icon and panel system |
| References | عندك صورة أو تجربة تعجبك؟ شو بالتحديد بتحب فيها؟ | Extract principles, avoid copying |
| Constraints | شو لازم نحافظ عليه؟ وشو ممنوع أو ما بدك تشوفه؟ | Scope boundaries |
| Readiness | هذا ملخص فكرتك. نبدأ، نعدّل جزء، ولا بدك أسئلة أعمق؟ | Transition to build |

### Useful depth branches

- **Obby:** expected skill level, checkpoint spacing, failure recovery, moving-platform timing, accessibility alternatives. Prototype jumps before dressing the route.
- **Combat:** mode, player count, cover rhythm, spawn protection, approach routes, readability of opponents. Validate visibility from gameplay height.
- **Simulator/tycoon:** repeated actions, economy UI, upgrades, plots, social hub, visual progression. Keep server authority over rewards.
- **Horror:** tension, visibility limits, navigation cues, sound cues, movement comfort. Do not make necessary interaction unreadable.
- **GUI only:** screen purpose, current hierarchy, art style, input devices, icon sources, text languages, data states, actions, motion preference. Do not ask about biomes or geography.

## Example: interview remains interactive

User: صمملي ماب.

RoCode: كيف بدك ستايل الماب؟ كلاسيكي مستوحى من روبلوكس 2007، مستقبلي، كرتوني، واقعي، فانتازي، أو خليط؟

User: كلاسيكي.

RoCode: تمام، كلاسيكي. بدك قريب من 2007 فعلًا، ولا كلاسيكي مطوّر بتفاصيل وإضاءة أحدث؟

User: كلاسيكي مطوّر، جزيرة أوبي، موبايل وكمبيوتر.

RoCode: تمام، جزيرة أوبي كلاسيكية مطوّرة للموبايل والكمبيوتر. بدك التحديات سهلة ومريحة، متوسطة، ولا صعبة؟

Record style, treatment, setting, gameplay, and devices now. Do not re-ask those five questions. Continue with the player's route, landmarks, surfaces, mood, assets, and GUI as needed.

User: اختار الباقي وابدأ.

RoCode: رح أعتمد مسار متوسط الصعوبة حول منارة، بألوان بحرية ونتوءات محدودة على الأسطح العلوية. هاي اختيارات مني لباقي التفاصيل، ورح أبدأ بمنطقة نموذجية قابلة للعب.

Then transition into the build workflow. These defaults belong to this example, not every future project.
