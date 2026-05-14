# [INFO] Hyperfocus Global Impact Skills

> [BRAIN] Modular AI Skills for neurodivergent empowerment, mental health, education, sustainability & global communities! -

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-10%2F15-brightgreen.svg)](#skills-available-now)
[![Contributors](https://img.shields.io/badge/Contributors-Welcome-orange.svg)](CONTRIBUTING.md)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%2B-success.svg)](#accessibility-commitment)

![Skills Constellation Map](media/skills-constellation-map.png)

---

## [MAP] What Are Hyperfocus Skills?

Hyperfocus Global Impact Skills are **modular AI capabilities** that teach Claude and other AI agents to support:

- [BRAIN] **Neurodivergent Empowerment** (ADHD, dyslexia, autism support)
- <3 **Mental Health & Wellbeing** (tracking, pattern recognition, privacy-first)
- [DOCS] **Accessible Education** (microlearning, text-to-speech, adaptive)
- [IMAGE] **Environmental Sustainability** (carbon tracking, green optimization)
- [BROFIST] **Global Community** (multilingual, governance, collaboration)
- 🐳 **HyperDocker DevOps** (Dockerfile hardening, Compose guardrails, container diagnostics)

**Built by neurodivergent developers, for everyone.** [WORLD]

---

## [START] Start Here → Pick a Skill → Paste the Prompt

> **New here?** Every Skill has a `SKILL.md` file. Load it into Claude Code or the HyperAgent‑SDK, then paste the "Best Starter Prompt" from inside that file.

### Load into Claude Code
```bash
# 1. Download any SKILL.md from a skill folder below
curl -O https://raw.githubusercontent.com/welshDog/Hyperfocus-Global-Impact-Skills/main/<skill-folder>/SKILL.md

# 2. Claude Code → Settings → Skills → Import → select SKILL.md
```

### Load into HyperAgent‑SDK
```bash
npm install -g @w3lshdog/hyper-agent
node cli/index.js skills load ./SKILL.md
node cli/index.js agents list
```

> **Naming rule:** All skill files are always called `SKILL.md` (lowercase) inside their own folder. Never `.SKILL.md`.

---

## [MAP] Skills Available Now

| Skill | Domain | Status | Path | Best Prompt |
|-------|--------|--------|------|-------------|
| Focus Coach | Neurodivergent | ✅ Production | [View](./focus-coach/) | `"Help me chunk this task using the Focus Coach skill"` |
| Accessible Design | Neurodivergent | ✅ Production | [View](./accessible-design/) | `"Review this UI using Accessible Design skill"` |
| Mental Energy Logger | Neurodivergent | ✅ Production | [View](./mental-energy-logger/) | `"Log my energy level and suggest next action"` |
| NeuroHealth Tracker | Global Health | ✅ Production | [View](./neurohealth-tracker/) | `"Track today's symptoms and patterns"` |
| HyperLearn | Education | ✅ Production | [View](./hyperlearn/) | `"Turn this topic into a 10-min microlesson"` |
| Carbon Coach | Sustainability | ✅ Production | [View](./carbon-coach/) | `"Estimate my dev workflow's carbon footprint"` |
| Hyperfocus Zone Agent Swarm | Neurodivergent / Dev Infra | 🟡 In Progress | [View](./Hyperfocus-Zone-Agent-Swarm.SKILL.md) | `"/hyperfocus:chunk-task 'Finish my MVP'"` |
| HyperDocker Image Optimizer | DevOps / Docker | 🟡 In Progress | [View](./hyperdocker-image-optimizer/) | `"Use Image Optimizer skill to refactor this Dockerfile"` |
| HyperDocker Compose Guardian | DevOps / Docker | 🟡 In Progress | [View](./hyperdocker-compose-guardian/) | `"Use Compose Guardian before editing docker-compose.yml"` |
| HyperDocker Healer Diagnostics | DevOps / Docker | 🟡 In Progress | [View](./hyperdocker-healer-diagnostics/) | `"Run Healer Diagnostics on restarting container <name>"` |
| Symptom Analysis | Global Health | 🔧 In Progress | Coming Soon | — |
| Outbreak Alert | Global Health | 📋 Planned | Coming Soon | — |
| Skill Assessment | Education | 📋 Planned | Coming Soon | — |
| Micro-Mentoring | Education | 📋 Planned | Coming Soon | — |
| Energy Dashboard | Sustainability | 📋 Planned | Coming Soon | — |

---

## [ENERGY] Get Started In 60 Seconds

### For Claude Code Users
```bash
# Clone the repo
git clone https://github.com/welshDog/Hyperfocus-Global-Impact-Skills.git
cd Hyperfocus-Global-Impact-Skills

# Load a Skill (example: Focus Coach)
claude load-skill ./focus-coach
```

### For Claude API Users
```python
from anthropic import Anthropic

# Load any Skill
with open('./hyperdocker-compose-guardian/SKILL.md', 'r') as f:
    skill_content = f.read()

client = Anthropic(api_key="your-key")
# Use skill_content in your API requests!
```

### For Claude.ai Web Users
1. Download any `SKILL.md` file from a skill folder
2. Go to claude.ai → Settings → Skills
3. Upload the SKILL.md file
4. Start using it in your chats! [CHAT]

---

## [STAR] Why This Matters

- **10% of people have dyslexia** - most apps aren't designed for them
- **8M+ US adults have ADHD** - executive function support is critical
- **Mental health apps with gamification** show 2-3x higher engagement
- **Digital carbon footprint** is growing - developers need tracking tools
- **Neurodivergent learners** thrive with adaptive, multimodal education

**We're fixing that.** Every Skill we build helps someone in the world. <3

---

## [BROFIST] Contributing

We welcome contributions from:
- [LAPTOP] Developers (any skill level!)
- [ART] Designers & UX experts
- [ACCESS] Accessibility advocates
- [BRAIN] Neurodivergent community members
- [WORLD] Anyone passionate about inclusive tech

**See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started!**

Quick ways to contribute:
1. [STAR] Star this repo
2. [BUG] Report bugs or suggest improvements
3. [WIP] Build a new Skill (we have templates!)
4. [DOCS] Improve documentation
5. [ANNOUNCE] Share with your communities

---

## [CHART] Roadmap

- [x] **Phase 1:** Foundation (6 Skills built) ✅
- [x] **Phase 1.5:** HyperDocker + Agent Swarm Skills ✅
- [ ] **Phase 2:** Domain expansion (5 more Skills) 🔧
- [ ] **Phase 3:** Community Hub & marketplace
- [ ] **Phase 4:** Global impact & research

[View Full Roadmap →](docs/ROADMAP.md)

---

## [LICENSE] License

Apache 2.0 - Free forever, open-source, community-driven.

**TL;DR:** Use freely, modify, distribute. Just keep it open and credit the project! <3

---

## [LINK] Links

- **Website:** [hyperfocuszone.com](https://hyperfocuszone.com)
- **GitHub:** [welshDog/Hyperfocus-Global-Impact-Skills](https://github.com/welshDog/Hyperfocus-Global-Impact-Skills)
- **Issues:** [Report bugs or request features](https://github.com/welshDog/Hyperfocus-Global-Impact-Skills/issues)

---

**Built with <3 in Wales, UK 🏴󠁧󠁢󠁷󠁬󠁳󠁿**

*"Every brain deserves technology that works FOR them."* [STAR]

Let's light up the world! [BROFIST]
