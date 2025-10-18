#!/bin/bash

# Hyperfocus Global Impact Skills - GitHub Setup Script
# Run this after creating your GitHub repository

echo "🌟 Setting up Hyperfocus Global Impact Skills repository..."

# Initialize git if not already done
if [ ! -d .git ]; then
    git init
    echo "✅ Git initialized"
fi

# Create proper folder structure
echo "📁 Creating folder structure..."

mkdir -p focus-coach
mkdir -p accessible-design
mkdir -p mental-energy-logger
mkdir -p neurohealth-tracker
mkdir -p hyperlearn
mkdir -p carbon-coach
mkdir -p docs
mkdir -p .github/workflows

# Move Skills to folders
echo "📦 Organizing Skills..."

mv focus-coach_SKILL.md focus-coach/SKILL.md
mv accessible-design_SKILL.md accessible-design/SKILL.md
mv mental-energy-logger_SKILL.md mental-energy-logger/SKILL.md
mv neurohealth-tracker_SKILL.md neurohealth-tracker/SKILL.md
mv hyperlearn_SKILL.md hyperlearn/SKILL.md
mv carbon-coach_SKILL.md carbon-coach/SKILL.md

# Create LICENSE file
echo "📜 Creating LICENSE file..."
cat > LICENSE << 'EOF'
Apache License 2.0

Copyright 2025 Hyperfocus Zone

Licensed under the Apache License, Version 2.0...
(Full text at: https://www.apache.org/licenses/LICENSE-2.0)
EOF

# Create CODE_OF_CONDUCT.md
echo "🤝 Creating Code of Conduct..."
cat > CODE_OF_CONDUCT.md << 'EOF'
# Contributor Covenant Code of Conduct

We are committed to providing a welcoming and inclusive experience for everyone.

## Our Pledge
- Be respectful and kind
- Welcome diverse perspectives
- Use inclusive language
- Accept constructive feedback

## Neurodivergent-Friendly Communication
- Be clear and direct
- Be patient with clarification requests
- Respect different communication styles
- Avoid sarcasm and ambiguity

## Report Issues
Contact: conduct@hyperfocuszone.com
EOF

# Create .gitignore
echo "🚫 Creating .gitignore..."
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
.env
venv/

# Node
node_modules/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
EOF

# Stage all files
echo "➕ Staging files..."
git add .

# Initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial release: 6 production-ready Skills

- Focus Coach: ADHD task management
- Accessible Design: Neurodivergent UI/UX patterns
- Mental Energy Logger: Mood & energy tracking
- NeuroHealth Tracker: Medication & cannabis tracking
- HyperLearn: Adaptive microlearning
- Carbon Coach: Sustainability tracking

Includes comprehensive documentation and contribution guidelines.

Built with 💚 by Hyperfocus Zone"

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Next steps:"
echo "1. Create repository on GitHub: hyperfocus-zone/global-impact-skills"
echo "2. Add remote: git remote add origin https://github.com/hyperfocus-zone/global-impact-skills.git"
echo "3. Push: git push -u origin main"
echo ""
echo "🌟 Let's light up the world!"
