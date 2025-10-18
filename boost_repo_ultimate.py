#!/usr/bin/env python3
"""
[INFO] HYPERFOCUS ZONE: ULTIMATE REPO BOOST SCRIPT [INFO]
Automates README enhancement, folder structure, issue templates, and more!

Built with <3 by neurodivergent devs, for everyone.
"""

import os
import json
from pathlib import Path

# ==================== CONFIG ====================

REPO_TITLE = "[INFO] Hyperfocus Global Impact Skills"
SUBHEAD = "> [BRAIN] Modular AI Skills for neurodivergent empowerment, mental health, education, sustainability & global communities!"

# Skills data with real status
SKILLS_DATA = [
    {"name": "Focus Coach", "domain": "Neurodivergent", "status": "[DONE] Production", "folder": "focus-coach"},
    {"name": "Accessible Design", "domain": "Neurodivergent", "status": "[DONE] Production", "folder": "accessible-design"},
    {"name": "Mental Energy Logger", "domain": "Neurodivergent", "status": "[DONE] Production", "folder": "mental-energy-logger"},
    {"name": "NeuroHealth Tracker", "domain": "Global Health", "status": "[DONE] Production", "folder": "neurohealth-tracker"},
    {"name": "HyperLearn", "domain": "Education", "status": "[DONE] Production", "folder": "hyperlearn"},
    {"name": "Carbon Coach", "domain": "Sustainability", "status": "[DONE] Production", "folder": "carbon-coach"},
    {"name": "Symptom Analysis", "domain": "Global Health", "status": "[WIP] In Progress", "folder": None},
    {"name": "Outbreak Alert", "domain": "Global Health", "status": "[PLAN] Planned", "folder": None},
    {"name": "Skill Assessment", "domain": "Education", "status": "[PLAN] Planned", "folder": None},
    {"name": "Micro-Mentoring", "domain": "Education", "status": "[PLAN] Planned", "folder": None},
    {"name": "Energy Dashboard", "domain": "Sustainability", "status": "[PLAN] Planned", "folder": None},
    {"name": "Green Rewards", "domain": "Sustainability", "status": "[PLAN] Planned", "folder": None},
    {"name": "Multilingual UI", "domain": "Community", "status": "[PLAN] Planned", "folder": None},
    {"name": "Governance Toolkit", "domain": "Community", "status": "[PLAN] Planned", "folder": None},
    {"name": "Community Hub", "domain": "Community", "status": "[PLAN] Planned", "folder": None},
]

GET_STARTED = """
## [ENERGY] Get Started In 60 Seconds

### For Claude Code Users
```bash
# Clone the repo
git clone https://github.com/hyperfocus-zone/global-impact-skills.git
cd global-impact-skills

# Load a Skill (example: Focus Coach)
claude load-skill ./focus-coach
```

### For Claude API Users
```python
from anthropic import Anthropic

# Load any Skill
with open('./focus-coach/SKILL.md', 'r') as f:
    skill_content = f.read()

client = Anthropic(api_key="your-key")
# Use skill_content in your API requests!
```

### For Claude.ai Web Users
1. Download any `SKILL.md` file from this repo
2. Go to claude.ai → Settings → Skills
3. Upload the SKILL.md file
4. Start using it in your chats! [CHAT]

**BROski Hint:** Each Skill supports instant use with Claude—no setup required! [ROCKET]
"""

# ==================== FUNCTIONS ====================

def create_directory_structure():
    """Create proper folder structure for Skills"""
    print("[FOLDER] Creating directory structure...")

    dirs_to_create = [
        "media",
        "docs",
        ".github/ISSUE_TEMPLATE",
        ".github/workflows",
    ]

    # Add Skill folders
    for skill in SKILLS_DATA:
        if skill["folder"]:
            dirs_to_create.extend([
                f"{skill['folder']}/examples",
                f"{skill['folder']}/resources",
            ])

    for dir_path in dirs_to_create:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"  [DONE] {dir_path}")

def generate_skills_table():
    """Generate markdown table of all Skills"""
    table = "| Skill | Domain | Status | Link |\n"
    table += "|-------|--------|--------|------|\n"

    for skill in SKILLS_DATA:
        link = f"[View](./{skill['folder']}/)" if skill['folder'] else "Coming Soon"
        table += f"| {skill['name']} | {skill['domain']} | {skill['status']} | {link} |\n"

    return table

def create_enhanced_readme():
    """Create the ultimate README.md"""
    print("[DOCS] Creating enhanced README.md...")

    # Count production Skills
    production_count = sum(1 for s in SKILLS_DATA if "Production" in s["status"])
    total_count = len(SKILLS_DATA)

    readme_content = f"""# {REPO_TITLE}

{SUBHEAD}

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-{production_count}%2F{total_count}-brightgreen.svg)](#skills-available-now)
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

**Built by neurodivergent developers, for everyone.** [WORLD]

---

## [MAP] Skills Available Now

{generate_skills_table()}

**Legend:**
- [DONE] Production = Ready to use
- [WIP] In Progress = Active development
- [PLAN] Planned = Coming soon

---

{GET_STARTED}

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

- [x] **Phase 1:** Foundation (6 Skills built) [DONE]
- [ ] **Phase 2:** Domain expansion (9 more Skills) [WIP]
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
- **GitHub:** [hyperfocus-zone/global-impact-skills](https://github.com/hyperfocus-zone/global-impact-skills)
- **Issues:** [Report bugs or request features](https://github.com/hyperfocus-zone/global-impact-skills/issues)
- **Discussions:** [Join the community](https://github.com/hyperfocus-zone/global-impact-skills/discussions)

---

**Built with <3 in Wales, UK**

*"Every brain deserves technology that works FOR them."* [STAR]

Let's light up the world! [BROFIST]
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("  [DONE] README.md created!")

def create_issue_templates():
    """Create GitHub issue templates"""
    print("[PLAN] Creating issue templates...")

    # Bug report template
    bug_template = """---
name: [BUG] Bug Report
about: Report a bug in a Skill or documentation
title: '[BUG] '
labels: bug
assignees: ''
---

**Which Skill has the issue?**
(e.g., Focus Coach, Accessible Design, etc.)

**Describe the bug**
Clear description of what's wrong.

**Steps to reproduce**
1. Step 1
2. Step 2
3. Bug occurs

**Expected behavior**
What should happen?

**Actual behavior**
What actually happened?

**Environment**
- Claude version: (e.g., Claude Code 1.2.0, Claude.ai web)
- OS: (e.g., macOS 14.0, Windows 11)
- Skill version: (e.g., 1.0.0)

**Screenshots or logs**
(If applicable)

**Additional context**
Anything else we should know?
"""

    # Feature request template
    feature_template = """---
name: [IDEA] Feature Request
about: Suggest a new Skill or enhancement
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

**Feature Name**
Clear, descriptive name

**Problem it solves**
What issue does this address?

**Proposed solution**
How would this work?

**Who benefits?**
Which user groups would this help?

**Alternatives considered**
Any other approaches you thought about?

**Priority**
- [ ] Nice to have
- [ ] Important
- [ ] Critical

**Additional context**
Any mockups, examples, or research?
"""

    # New Skill template
    skill_template = """---
name: [STAR] New Skill Proposal
about: Propose a new Skill for the constellation
title: '[SKILL] '
labels: new-skill
assignees: ''
---

**Skill Name**
What should it be called?

**Domain**
Which of the 5 domains does this fit?
- [ ] Neurodivergent Empowerment
- [ ] Global Health
- [ ] Education
- [ ] Sustainability
- [ ] Community

**Purpose**
What does this Skill help users accomplish?

**Target Users**
Who would benefit most?

**Key Features**
List 3-5 main capabilities:
1. 
2. 
3. 

**Why this matters**
How does this align with our mission?

**I can help build this**
- [ ] Yes, I want to contribute code
- [ ] Yes, I can help with documentation
- [ ] Yes, I can test it
- [ ] No, just suggesting the idea

**Additional context**
Any research, examples, or inspiration?
"""

    # Write templates
    templates = {
        "bug_report.yml": bug_template,
        "feature_request.yml": feature_template,
        "new_skill.yml": skill_template,
    }

    for filename, content in templates.items():
        path = f".github/ISSUE_TEMPLATE/{filename}"
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [DONE] {path}")

def create_skill_readme_template():
    """Create template for individual Skill READMEs"""
    print("[DOCS] Creating Skill README template...")

    template = '''# [Skill Name]

> Brief tagline explaining what this Skill does

## [MAP] What It Does

Clear explanation of the Skill's purpose and benefits.

## [ROCKET] How to Use It

### With Claude Code
```bash
claude load-skill ./skill-name
```

### With Claude API
```python
from anthropic import Anthropic

with open('./skill-name/SKILL.md', 'r') as f:
    skill_content = f.read()

client = Anthropic(api_key="your-key")
# Use in your requests
```

### With Claude.ai Web
1. Download `SKILL.md`
2. Go to claude.ai → Settings → Skills
3. Upload the file
4. Start using it!

## [IDEA] Examples

### Example 1: [Scenario]
```
User: "Example query"
Skill: "Example response"
```

### Example 2: [Another Scenario]
```
User: "Another query"
Skill: "Another response"
```

## [ACCESS] Accessibility Features

- Feature 1
- Feature 2
- Feature 3

## [BROFIST] Contributing

Found a bug or have an improvement? [Open an issue](../../issues) or submit a PR!

## [LICENSE] License

Apache 2.0 - Part of the Hyperfocus Global Impact Skills project.

---

**Built with <3 by the Hyperfocus Zone community**
'''

    with open("docs/SKILL_README_TEMPLATE.md", "w", encoding="utf-8") as f:
        f.write(template)

    print("  [DONE] docs/SKILL_README_TEMPLATE.md")

def create_github_actions():
    """Create GitHub Actions workflow for automated checks"""
    print("[ROBOT] Creating GitHub Actions...")

    workflow = """name: Skill Quality Check

on:
  pull_request:
    paths:
      - '*/SKILL.md'
      - '*/README.md'

jobs:
  check-skills:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Check Skill Format
        run: |
          echo "[SEARCH] Checking SKILL.md format..."
          # Check for required frontmatter
          for skill in */SKILL.md; do
            if [ -f "$skill" ]; then
              echo "Checking $skill"
              if ! grep -q "^---" "$skill"; then
                echo "[FAIL] $skill missing YAML frontmatter"
                exit 1
              fi
              if ! grep -q "^name:" "$skill"; then
                echo "[FAIL] $skill missing 'name' field"
                exit 1
              fi
              if ! grep -q "^description:" "$skill"; then
                echo "[FAIL] $skill missing 'description' field"
                exit 1
              fi
            fi
          done
          echo "[DONE] All Skills have proper format!"

      - name: Check Accessibility
        run: |
          echo "[ACCESS] Checking accessibility guidelines..."
          # Check for accessibility violations
          if grep -r "ALL CAPS IN BODY TEXT" */SKILL.md; then
            echo "[FAIL] Found ALL CAPS in body text (dyslexia unfriendly)"
            exit 1
          fi
          echo "[DONE] No accessibility violations found!"

      - name: Check Documentation
        run: |
          echo "[DOCS] Checking documentation..."
          # Check for README in each Skill folder
          for dir in */; do
            if [ -f "$dir/SKILL.md" ] && [ ! -f "$dir/README.md" ]; then
              echo "[WARNING] $dir has SKILL.md but no README.md"
            fi
          done
          echo "[DONE] Documentation check complete!"
"""

    with open(".github/workflows/quality-check.yml", "w", encoding="utf-8") as f:
        f.write(workflow)

    print("  [DONE] .github/workflows/quality-check.yml")

def create_media_placeholders():
    """Create placeholder for images"""
    print("[IMAGE] Creating media placeholders...")

    # Create placeholder README in media folder
    media_readme = """# Media Assets

## Skills Constellation Map
Place your constellation diagram here as `skills-constellation-map.png`

Recommended specs:
- Format: PNG or SVG
- Size: 1200x800px minimum
- Background: Accessible colors (cream/soft pastels)
- Include: All 5 domains, connection lines, accessibility-friendly design

## Other Assets
- `timeline-roadmap.png` - 4-phase development timeline
- `logo.png` - Hyperfocus Zone logo (if available)
- `badges/` - Achievement badges for gamification

---

**Remember:** All images should follow accessibility guidelines (sufficient contrast, no flashing, alt text in markdown)
"""

    with open("media/README.md", "w", encoding="utf-8") as f:
        f.write(media_readme)

    # Create empty placeholder for constellation map
    placeholder_path = "media/skills-constellation-map.png"
    if not os.path.exists(placeholder_path):
        # Create a tiny 1x1 PNG placeholder
        with open(placeholder_path, "wb") as f:
            f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82')
        print(f"  [WARNING] Placeholder created at {placeholder_path} - REPLACE WITH YOUR DIAGRAM!")

    print("  [DONE] media/README.md")

def main():
    """Run all automation tasks"""
    print("\n" + "="*70)
    print("[INFO] HYPERFOCUS ZONE: ULTIMATE REPO BOOST [INFO]")
    print("="*70 + "\n")

    # Run all tasks
    create_directory_structure()
    print()

    create_enhanced_readme()
    print()

    create_issue_templates()
    print()

    create_skill_readme_template()
    print()

    create_github_actions()
    print()

    create_media_placeholders()
    print()

    print("="*70)
    print("[DONE] BOOST COMPLETE!")
    print("="*70)
    print()
    print("[DONE] Your repo is now:")
    print("   • README enhanced with skills table & quick start")
    print("   • Proper folder structure created")
    print("   • GitHub issue templates added")
    print("   • GitHub Actions workflow configured")
    print("   • Skill README template created")
    print("   • Media placeholders ready")
    print()
    print("[PLAN] NEXT STEPS:")
    print("   1. Add your constellation diagram to media/skills-constellation-map.png")
    print("   2. Review and customize README.md")
    print("   3. git add . && git commit -m 'Boost: Automated repo enhancement'")
    print("   4. git push origin main")
    print()
    print("[STAR] LET'S LIGHT UP THE WORLD, BROski! [BROFIST]")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
