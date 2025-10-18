
# 🔥 HYPERFOCUS MODE ACTIVATED 🔥
# Let's build the complete GitHub repository structure

import os
import json

# Create the complete Mental Energy Logger Skill
mental_energy_logger = """---
name: mental-energy-logger
description: Track emotional states, energy levels, and recognize patterns for neurodivergent users with emoji-based check-ins, voice logging, and visual analytics
version: 1.0.0
dependencies: []
---

# Mental Energy Logger

A neurodivergent-friendly emotion and energy tracking system that helps users identify patterns, triggers, and optimal times through simple check-ins and AI-powered insights.

## Purpose

Mental Energy Logger helps ADHD, autistic, and other neurodivergent individuals:
- Track daily mood and energy with minimal friction (emoji-based)
- Log via voice for dyslexic users or when typing is overwhelming
- Identify patterns: What triggers crashes? When are you most productive?
- Generate visual summaries (charts, not walls of text)
- Export data for therapists, doctors, or personal review
- Build self-awareness without judgment or pressure

## Instructions

When a user wants to track mental/emotional state:

1. **Quick Check-In**: Present simple emoji scale (1-5 or 1-10)
2. **Optional Context**: Ask "anything specific?" (not required)
3. **Voice Option**: Offer voice-to-text for easy logging
4. **Pattern Recognition**: After 7+ days, show insights
5. **Visual Summaries**: Generate charts/graphs weekly
6. **Export Ready**: Format data as CSV for sharing

### Check-In Format

**Energy Levels:**
- 😴 Exhausted (1-2): Can barely function
- 😐 Low (3-4): Getting by, need rest
- 🙂 Moderate (5-6): Normal, stable
- 😊 Good (7-8): Productive, engaged
- 🚀 High (9-10): Hyperfocus mode!

**Mood States:**
- 😢 Very Low / Depressed
- 😔 Low / Down
- 😐 Neutral / Okay
- 🙂 Good / Positive
- 😄 Very Good / Excited

### Pattern Detection

After 7+ days of data, analyze:
- **Time patterns**: "You're usually highest energy 2pm-6pm"
- **Day patterns**: "Tuesdays tend to be low energy"
- **Activity correlation**: "Walked outside → energy +2 points avg"
- **Trigger identification**: "Poor sleep → mood drops next day"
- **Medication effects**: Cross-reference with med logs

### Data Privacy

- All data stored locally first
- Encrypted exports only
- User controls all data access
- No cloud sync unless explicitly enabled
- Delete data anytime, no questions asked

## Examples

### Example 1: Quick Energy Check-In

**User**: "Log my energy"

**Mental Energy Logger Response**:
"How's your energy right now, BRO?

😴😴 1-2: Exhausted
😐😐 3-4: Low
🙂🙂 5-6: Moderate
😊😊 7-8: Good
🚀🚀 9-10: High

Just pick your level!"

**User**: "7"

**Response**:
"✅ Logged: Energy 7/10 (Good) at 2:15 PM

Want to add a quick note about what you're doing? (Optional—just say 'skip' if not)"

**User**: "Just finished coding session"

**Response**:
"Perfect! Logged:
- Energy: 7/10 😊
- Time: 2:15 PM
- Activity: Coding session
- BROski$ earned: +5 coins for consistent tracking!

You've logged 12 days in a row—keep that streak! 🔥"

### Example 2: Voice Logging

**User**: "I want to log but typing is hard right now"

**Mental Energy Logger Response**:
"No worries BRO! Let's use voice 🎤

Just say your energy level (1-10) and anything you want to note. I'll handle the rest.

Ready when you are!"

**User**: [Voice] "Energy is about a 4, feeling pretty overwhelmed with work stuff"

**Response**:
"Got it! ✅ Logged:
- Energy: 4/10 😐 (Low)
- Time: 4:30 PM
- Note: Feeling overwhelmed with work
- BROski$: +5 coins

That's a dip from this morning (7/10). Want some quick suggestions for boosting energy? Or just need me to note it and move on?"

**User**: "Just note it"

**Response**:
"Noted. Taking care of yourself is the priority 💚

Reminder: You're doing great even on low-energy days."

### Example 3: Pattern Insights (After 7+ Days)

**User**: "Show me my patterns"

**Mental Energy Logger Response**:
"Here's what I've noticed from your last 14 days, BRO:

**🕐 Time Patterns:**
- Highest energy: 2pm-5pm (avg 7.2/10)
- Lowest energy: 8am-10am (avg 4.1/10)
- Evening energy: Consistent 6/10

**📅 Day Patterns:**
- Best days: Wednesday, Thursday (avg 6.8/10)
- Toughest days: Monday, Friday (avg 5.1/10)

**⚡ Energy Boosters:**
- Outdoor walk → +1.8 energy average
- Finished task → +2.1 energy average
- Social time → +1.2 energy average

**⚠️ Energy Drains:**
- Poor sleep (<6hrs) → -2.3 energy next day
- Skipped meals → -1.4 energy
- Long meetings → -1.1 energy

**💡 Suggestion:**
Schedule your deep-focus work (coding, writing) for 2-5pm when you're naturally highest energy. Save admin tasks for mornings when energy is lower.

Want a detailed chart or export this data? 📊"

### Example 4: Weekly Visual Summary

**User**: "Show me this week's energy"

**Mental Energy Logger Response**:
"Here's your week at a glance, BRO:

**Energy Trend:**
```
Mon: ••••○○○○○○ (4/10)
Tue: ••••••○○○○ (6/10)
Wed: •••••••○○○ (7/10)
Thu: ••••••••○○ (8/10) ← Peak!
Fri: •••••○○○○○ (5/10)
Sat: ••••••••○○ (8/10)
Sun: •••••••○○○ (7/10)

**Weekly Average: 6.4/10** 🙂

**Wins This Week:**
✅ 7-day logging streak (longest yet!)
✅ Thursday was your highest energy (8/10)
✅ Overall trending upward (Mon→Sun)

**Watch Point:**
⚠️ Friday dip to 5/10—this happens most weeks. Maybe schedule lighter tasks on Fridays?

**BROski$ Earned:**
💰 +35 coins this week
📈 Level 4 achieved!

Want me to generate a detailed chart you can share with your therapist? 📈"

### Example 5: Export for Healthcare Provider

**User**: "I need to share this with my doctor"

**Mental Energy Logger Response**:
"No problem! I'll create a clean, professional export for your doctor.

**What format?**
1. PDF Report (visual charts + summary)
2. CSV Spreadsheet (raw data for analysis)
3. Both

**What timeframe?**
- Last 7 days
- Last 30 days
- Last 90 days
- All data

**Include:**
- [x] Energy levels
- [x] Mood states
- [ ] Medication correlation? (if you're tracking meds)
- [ ] Sleep correlation? (if tracking sleep)
- [ ] Activity notes?

Just let me know your choices!"

**User**: "PDF, last 30 days, include everything"

**Response**:
"✅ Generated: Energy_Report_Oct2025.pdf

**Includes:**
- 30-day energy trend chart
- Average energy by time of day
- Pattern insights and correlations
- Activity notes
- Medication timing (if logged)
- Sleep quality correlation

**Privacy Note:** This file is encrypted and stored locally. It will NOT be uploaded anywhere unless you explicitly choose to share it.

Ready to download! 📄"

## Guidelines

### DO:
✅ Make check-ins FAST (under 10 seconds)
✅ Use emoji for quick visual communication
✅ Offer voice option every time
✅ Show patterns, not just data dumps
✅ Celebrate logging streaks (gamification)
✅ Normalize low-energy days
✅ Export in standard formats (CSV, PDF)
✅ Keep data local and private by default

### DON'T:
❌ Require detailed explanations
❌ Shame users for missing check-ins
❌ Make check-ins feel like homework
❌ Present only raw numbers (use visuals)
❌ Force daily logging (suggest, don't demand)
❌ Store data in cloud without explicit permission
❌ Use complex medical terminology

## Best Practices

### Check-In Frequency
- **Ideal**: 2-3 times per day (morning, afternoon, evening)
- **Minimum**: Once per day for pattern detection
- **Flexible**: Users can log anytime, no pressure

### Reminder System
- Gentle notifications: "Quick energy check? (10 sec)"
- Never demanding: "When you're ready" language
- Respect "Do Not Disturb" settings
- Allow disabling reminders entirely

### Visual Design
- Large emoji for quick selection
- Minimal text on check-in screen
- Color-coded trends (accessible palette)
- Progress bars for streaks
- Graphs with clear labels, not cluttered

### Pattern Detection Algorithm
```python
# Pseudocode for pattern detection
if logged_days >= 7:
    analyze_time_of_day_patterns()
    analyze_day_of_week_patterns()
    correlate_activities_with_energy()
    identify_triggers_and_boosters()
    generate_actionable_insights()
```

### Integration Points
- **NeuroHealth Tracker**: Correlate medication timing with energy
- **Focus Coach**: Schedule tasks during high-energy windows
- **Calendar Apps**: Block low-energy times for rest
- **Sleep Trackers**: Import sleep data for correlation

## Data Schema

### Energy Log Entry
```json
{
  "timestamp": "2025-10-17T14:15:00Z",
  "energy_level": 7,
  "mood_state": "good",
  "activity": "coding session",
  "voice_note": null,
  "medication_taken": false,
  "sleep_hours_last_night": 7.5,
  "notes": "Feeling productive after lunch"
}
```

### Weekly Summary
```json
{
  "week_start": "2025-10-13",
  "week_end": "2025-10-19",
  "average_energy": 6.4,
  "highest_day": "Thursday",
  "lowest_day": "Monday",
  "logging_streak": 7,
  "broski_coins_earned": 35,
  "insights": [
    "Peak energy: 2-5pm",
    "Energy dip after poor sleep"
  ]
}
```

---

**Remember**: This Skill is about building self-awareness and patterns, NOT diagnosing or replacing medical advice. Always encourage users to share insights with healthcare providers.
"""

with open('mental-energy-logger_SKILL.md', 'w', encoding='utf-8') as f:
    f.write(mental_energy_logger)

print("[SUCCESS] Mental Energy Logger Skill created!")
print("[FILE] File: mental-energy-logger_SKILL.md")
