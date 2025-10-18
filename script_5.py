
# Create CONTRIBUTING.md - how others can contribute to the project

contributing_guide = """# Contributing to Hyperfocus Global Impact Skills 🤝

**Thank you for your interest in contributing!** Whether you're neurodivergent yourself, an accessibility advocate, a developer, or just someone who wants to help—**you belong here**.

---

## 💚 Code of Conduct

We're committed to providing a welcoming, inclusive, and harassment-free experience for everyone. Please read our [Code of Conduct](./CODE_OF_CONDUCT.md) before contributing.

**TL;DR:**
- Be respectful and kind
- Welcome diverse perspectives
- No discrimination, harassment, or trolling
- Constructive feedback only
- Neurodivergent-friendly communication (clear, direct, patient)

---

## 🎯 Ways to Contribute

### 1. Build a New Skill
See [Creating Your First Skill](#creating-a-new-skill) below.

### 2. Improve Existing Skills
- Fix bugs or unclear instructions
- Add more examples
- Improve accessibility
- Optimize performance
- Add test coverage

### 3. Documentation
- Fix typos or broken links
- Improve clarity
- Add tutorials or guides
- Translate to other languages

### 4. Testing & Feedback
- Test Skills with Claude
- Report bugs or issues
- Suggest improvements
- Share user experience insights

### 5. Accessibility Audits
- Check WCAG compliance
- Test with screen readers
- Validate color contrast
- Ensure dyslexia-friendly formatting

### 6. Community Building
- Answer questions in Discussions
- Share Skills on social media
- Host workshops or tutorials
- Organize Skill-a-thon events

---

## 🛠️ Creating a New Skill

### Step 1: Plan Your Skill

**Ask yourself:**
- What problem does this Skill solve?
- Who benefits from it?
- Does it fit one of our 5 domains? (Neurodivergent, Health, Education, Sustainability, Community)
- Is it accessible by design?

**Good Skill Ideas:**
✅ Financial budgeting for ADHD users  
✅ Job interview prep for autistic candidates  
✅ Accessible recipe converter (clear steps, timers)  
✅ Burnout prevention tracker  
✅ Green hosting comparison tool  

**Not Skill Ideas (too broad):**
❌ "General productivity"  
❌ "Health tracking" (too vague)  
❌ "Education system" (needs to be more specific)  

### Step 2: Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR-USERNAME/global-impact-skills.git
cd global-impact-skills

# Create a branch
git checkout -b skill/your-skill-name
```

### Step 3: Create Skill Folder Structure

```bash
mkdir your-skill-name
cd your-skill-name

# Create required files
touch SKILL.md
touch README.md
mkdir examples
mkdir resources
mkdir scripts   # optional
mkdir tests     # optional
```

### Step 4: Write SKILL.md

```yaml
---
name: your-skill-name
description: Clear, concise description (max 200 chars)
version: 1.0.0
dependencies: []  # e.g., ["python>=3.8", "requests>=2.28"]
---

# Your Skill Name

Brief introduction explaining what this Skill does.

## Purpose

Bullet list of what this Skill helps users accomplish.

## Instructions

Clear step-by-step instructions for Claude on how to use this Skill.

### Section 1
Details...

### Section 2
Details...

## Examples

### Example 1: [Scenario Name]

**User**: "Example user query"

**[Skill Name] Response**:
"Example response showing the Skill in action..."

### Example 2: [Another Scenario]

(Repeat for 3-5 examples)

## Guidelines

### DO:
✅ Guideline 1
✅ Guideline 2

### DON'T:
❌ Anti-pattern 1
❌ Anti-pattern 2

## Best Practices

Additional tips, technical notes, integration points, etc.

---

**Notes**: Any disclaimers or additional context.
```

### Step 5: Write README.md

```markdown
# Your Skill Name

User-facing documentation (less technical than SKILL.md).

## What It Does

Clear explanation for end users.

## How to Use It

### With Claude Code
\`\`\`bash
claude load-skill ./your-skill-name
\`\`\`

### With Claude API
\`\`\`python
# Example code
\`\`\`

## Examples

Show real usage examples.

## Credits

Who built this? Any inspirations or resources?
```

### Step 6: Add Examples

Create `examples/example-1.md` with real usage scenarios:

```markdown
# Example: [Scenario Name]

## Context
What situation is this example addressing?

## Conversation
**User**: "Query"
**Skill**: "Response"

## Outcome
What was achieved?
```

### Step 7: Accessibility Check

**Before submitting, verify:**
- ✅ Typography follows dyslexia guidelines (sans-serif, 12pt+, letter spacing)
- ✅ Color contrast ratios meet WCAG AA (4.5:1 minimum)
- ✅ No autoplay, flashing, or excessive animations
- ✅ Clear headings hierarchy (H1 → H2 → H3)
- ✅ Bullet points used for lists
- ✅ No walls of text (max 5 sentences per paragraph)
- ✅ Examples use friendly, non-judgmental language

### Step 8: Test with Claude

1. Load your Skill into Claude Code or API
2. Try all your example scenarios
3. Test edge cases
4. Verify it works as expected

### Step 9: Update Main README

Add your Skill to the main `README.md`:

```markdown
| [Your Skill Name](./your-skill-name/) | ✅ **Production** | Brief description |
```

### Step 10: Commit and Push

```bash
git add .
git commit -m "Add: Your Skill Name for [purpose]"
git push origin skill/your-skill-name
```

### Step 11: Open Pull Request

1. Go to GitHub
2. Click "Compare & Pull Request"
3. Fill out the PR template:
   - What does this Skill do?
   - Who benefits from it?
   - Have you tested it?
   - Screenshots/examples (if applicable)

**We'll review within 48-72 hours!** 🎉

---

## 🧪 Testing Guidelines

### Manual Testing

**Test your Skill with Claude:**
1. Load it via Claude Code or API
2. Run through all examples in your SKILL.md
3. Try unexpected inputs
4. Verify error handling
5. Check accessibility features

### Automated Testing (Optional)

If your Skill includes scripts:

```python
# tests/test_your_skill.py
import pytest

def test_basic_functionality():
    # Your test code
    assert True
```

Run tests:
```bash
pytest tests/
```

---

## 📝 Style Guide

### Writing Style
- **Friendly & casual** ("Hey BRO", "Let's do this!")
- **Non-judgmental** (no shaming for struggles)
- **Action-oriented** (clear next steps)
- **Encouraging** (celebrate small wins)

### Code Style
- **Python:** Follow PEP 8
- **JavaScript:** Follow Airbnb style guide
- **Comments:** Explain WHY, not just WHAT

### Accessibility Style
- **Fonts:** Sans-serif only (Arial, Verdana)
- **Sizes:** 12pt minimum body text, 14pt preferred
- **Colors:** Dark grey on cream (not pure black/white)
- **Spacing:** 1.5-2.0 line height, generous margins
- **No italics, ALL CAPS, or ligatures**

### Markdown Formatting
```markdown
# H1 for main title (once per file)
## H2 for major sections
### H3 for subsections
#### H4 sparingly

- Bullet points for lists
- **Bold** for emphasis (not italics)
- `code` for technical terms
- [Links](url) for references
```

---

## 🐛 Reporting Bugs

**Found a bug?** Open an issue!

### Bug Report Template

```markdown
**Skill Name:** [Which Skill has the issue?]

**Description:** 
Clear description of the bug.

**Steps to Reproduce:**
1. Step 1
2. Step 2
3. Bug occurs

**Expected Behavior:**
What should happen?

**Actual Behavior:**
What actually happened?

**Environment:**
- Claude version: [e.g., Claude Code 1.2.0]
- OS: [e.g., macOS 14.0]
- Skill version: [e.g., 1.0.0]

**Screenshots/Logs:**
(If applicable)
```

---

## 💡 Feature Requests

Have an idea? We'd love to hear it!

### Feature Request Template

```markdown
**Feature Name:** [Clear, descriptive name]

**Problem:**
What problem does this solve?

**Proposed Solution:**
How would this feature work?

**Alternatives Considered:**
Any other approaches?

**Who Benefits:**
Which user groups would this help?

**Priority:**
- [ ] Nice to have
- [ ] Important
- [ ] Critical
```

---

## 🏆 Recognition

**Contributors will be recognized:**
- 📝 Added to CONTRIBUTORS.md
- 🏅 Credited in Skill README files
- 🎉 Shoutouts on social media
- 💰 BROski$ coins in our gamification system (if applicable)
- 🌟 Special badges for major contributions

**Top Contributors:**
- Badge: "Skill Architect" (5+ Skills)
- Badge: "Accessibility Champion" (major accessibility contributions)
- Badge: "Community Leader" (helps onboard new contributors)

---

## ❓ Questions?

**Need help?**
- 📖 Read the [Getting Started Guide](./docs/getting-started.md)
- 💬 Ask in [GitHub Discussions](https://github.com/hyperfocus-zone/global-impact-skills/discussions)
- 🐛 Open an [Issue](https://github.com/hyperfocus-zone/global-impact-skills/issues)
- 📧 Email: contribute@hyperfocuszone.com (coming soon)

**Not sure where to start?**
- Look for issues labeled `good first issue`
- Check the [Roadmap](./docs/ROADMAP.md) for planned Skills
- Ask in Discussions: "I want to help, where should I start?"

---

## 🙏 Thank You

Every contribution—no matter how small—makes a difference.

Whether you're fixing a typo, building a new Skill, or sharing feedback, **you're helping create a more accessible, inclusive, and empowering AI ecosystem.**

**Let's build this constellation together!** 🌟👊

---

**Remember:** Perfect is the enemy of done. Don't wait for your contribution to be perfect—we'll iterate together! 💚
"""

with open('CONTRIBUTING.md', 'w', encoding='utf-8') as f:
    f.write(contributing_guide)

print("[SUCCESS] CONTRIBUTING.md created!")
print("[FILE] Complete guide for community contributions")
