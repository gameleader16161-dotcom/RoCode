# روكود · RoCode

### A Roblox design skill by **QFR Studios**

**Ask first. Build with intent. Review the actual result.**

روكود سكيلة لكودكس لتصميم خرائط Roblox وواجهاتها: تبدأ بفهم ذوقك، وتحوّل إجاباتك إلى اتجاه فني وخطة بناء، وتستفيد من الـToolbox، ثم تراجع التنفيذ داخل Studio عندما تتوفر الأدوات.

**Copyright (c) 2026 QFR Studios · MIT License**

## كيف تبدأ؟

بعد تثبيتها، اكتب:

```text
استخدم $rocode وصمملي ماب. اسألني عن الستايل أولًا، وكمل معي الأسئلة لحد ما أحكيلك ابدأ.
```

أول سؤال إذا الستايل مش محدد:

> كيف بدك ستايل الماب؟ كلاسيكي مستوحى من روبلوكس 2007، مستقبلي، كرتوني، واقعي، فانتازي، أو خليط؟

بعد إجابتك، تكمل بأسئلة مرتبطة باختياراتك: نوع اللعب، المكان، المناطق، العناصر المميزة، الإضاءة، الأسطح، الحركة، الأصول، والـGUI. سؤال واحد في كل مرة افتراضيًا، مع حفظ الإجابات بدل تكرارها. إذا قلت **«اسألني أكثر»** تتعمق؛ وإذا قلت **«اختار الباقي وابدأ»** تنتقل للبناء وتوضح افتراضاتها.

التثبيت بحد ذاته لا يرسل رسالة ولا يفتح Roblox Studio. تبدأ المقابلة عند استدعاء السكيلة أو وصول طلب تصميم مناسب. السكيلة توجه سلوك المساعد؛ جودة التنفيذ تعتمد أيضًا على النموذج، المراجع، والأدوات المتصلة.

## What is included

- **An adaptive design interview:** Arabic-friendly, style-first, one topic at a time, with saved decisions and explicit delegation.
- **Art direction:** era, palette roles, silhouettes, materials, face treatment, composition, landmarks, and environmental storytelling.
- **Construction guidance:** shared dimensions, pivots, corners, openings, collision, and selected-pair seam diagnosis.
- **Toolbox curation:** search before reinventing complex props, inspect staged assets, harmonize their style, and record provenance.
- **Roblox GUI craft:** coherent icons and typography, responsive layout, real interaction states, Arabic checks, and multiple inputs.
- **Motion and code:** native TweenService/constraints/animation, interruptible transitions, cleanup, reduced motion, and server authority.
- **Evidence-based review:** separate rendered/playtested observations from static checks and unverified work.
- **Original helpers:** a Python brief manager, Luau geometry helpers, a read-only scene report, and optional Studio geometry checks.

## Install into Codex

### From the GitHub repository

Ask Codex's installed skill installer:

```text
Use $skill-installer to install the skill at skills/rocode from https://github.com/gameleader16161-dotcom/rocode.
```

### From a downloaded or cloned copy

Use Python 3.10+ from this repository folder:

```sh
python scripts/install.py
```

The default destination is `~/.agents/skills/rocode`. The installer prints the destination and refuses to overwrite an existing installation. To use a custom supported skills directory, pass its **parent**:

```sh
python scripts/install.py --skills-dir /path/to/your/skills
```

For a project-local install, use that project's `.agents/skills` directory. Install a single copy to avoid duplicate skill names. Existing environments that discover `~/.codex/skills` can use it through `--skills-dir`; discovery paths depend on the host/version.

You can also manually copy the entire `skills/rocode` folder into a supported skill directory. Codex detects skills automatically; restart it if RoCode does not appear. [Official skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Studio connection

For actual scene editing, connect a trusted Roblox Studio integration that exposes the capabilities you need. RoCode discovers available tools rather than hardcoding one connector's schema. It does **not** bundle an MCP server, credentials, or a Studio plugin.

| Capability | What it unlocks |
|---|---|
| Scene/script inspection and scoped Luau execution | Inspect and edit existing maps and GUI |
| Asset search and insertion | Curate Creator Store/Toolbox assets |
| Screen capture and playtest controls | Review the rendered result and actual player path |
| Device emulation and logs | Verify layout, inputs, and runtime issues |
| Profiling | Measure performance on representative scenes |

Without Studio access, it can still interview, write the brief, and deliver implementation source. It must report that rendering and runtime verification remain pending. It never invents asset IDs, screenshots, or test results.

## Classic surfaces

RoCode distinguishes legacy `Studs`, `Inlet`, and `Universal` surface visuals from modern material/texture workflows. It does not rely on old surface joints for mechanisms or claim that the current engine exactly reproduces the 2007 renderer. Smooth areas remain useful when intentional; the goal is a coherent finished map, not detail on every face. [Roblox SurfaceType reference](https://create.roblox.com/docs/reference/engine/enums/SurfaceType).

## Brief manager

Run from the **game project's** working folder, using the installed script's path:

```sh
python /path/to/rocode/scripts/brief.py init
python /path/to/rocode/scripts/brief.py set style "modern classic"
python /path/to/rocode/scripts/brief.py set gameplay "island obby"
python /path/to/rocode/scripts/brief.py next
python /path/to/rocode/scripts/brief.py ready --mode delegated --user-quote "Choose the rest and start"
```

The default state file is `work/rocode/brief.json`. Put `--file path/to/brief.json` **before** the subcommand to override it. `set --source proposed` records a suggestion without marking the topic answered. A changed decision invalidates an old readiness checkpoint. The CLI records the user instruction; it cannot authenticate whether a model has quoted that instruction truthfully.

`next` gives a fallback topic order. The assistant should adapt questions to the actual conversation and use the deeper branches in the interview guide. This script is not a language model and cannot prove that an aesthetic decision is good.

## Validate and evaluate

```sh
python -m unittest discover -s tests -v
python scripts/check_package.py
```

These run with Python's standard library and no network. They check brief behavior, installation boundaries, local reference integrity, original attribution, and packaging. Use [evals/scenarios.md](evals/scenarios.md) for realistic conversational and Studio evaluation.

**Initial validation scope:** automated Python and package checks plus static Luau review. The Luau modules have not been executed in Studio as part of this release. `Geometry.spec.luau` is provided for a later explicit Studio check. No generated-map quality benchmark or FPS claim is implied.

## Repository layout

```text
skills/rocode/
  SKILL.md                 Skill entry point
  agents/openai.yaml       Codex display metadata
  references/              Interview, art, construction, assets, GUI, motion, QA
  scripts/brief.py          Local design-state helper
  assets/                  Original example and Luau source helpers
  LICENSE, NOTICE          Attribution travels with installation
scripts/                   Local installer and package checker
tests/                     Automated helper/packaging tests
evals/                     Behavior scenarios and evidence requirements
LICENSE, NOTICE            QFR Studios copyright and MIT terms
```

## Rights and attribution

RoCode's original instructions and helper source are released under the [MIT License](LICENSE), copyright **QFR Studios**. Preserve the license/copyright notice in redistributed copies. The RoCode name and QFR Studios branding are not a claim to Roblox or OpenAI affiliation.

No third-party Toolbox models, paid assets, or private icon packs are bundled. Their rights remain with their respective owners. This license does not assign ownership of your game to QFR Studios or require an in-game watermark. Design guidance, API names, and implementation patterns do not grant rights to redistribute somebody else's art.
