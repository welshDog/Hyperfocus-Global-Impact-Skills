# [SKILL] Hyperfocus Zone – Agent Swarm Core

> Neurodivergent-first skill package that teaches agents how to run the BROski Hyperfocus Zone: chunk tasks, sync Obsidian, gamify with BROski$, and keep the stack calm.

## [MAP] What This Skill Does

When loaded into Claude Code, HyperAgent-SDK, or any compliant agent runtime, this Skill gives agents the ability to:

- [CHUNK] Break big goals into 5–15 minute Hyperfocus chunks with clear next actions.
- [VAULT] Sync an Obsidian vault (HyperFocus z0ne Brain) into the HyperCode V2.4 ecosystem via Minio/Chroma.
- [GAMIFY] Award BROski$ and pet XP for completed milestones via the existing token APIs.
- [SPLIT] Fan out large tasks into parallel sub-agents using crew-orchestrator.
- [CALM] Enter Focus Panic Mode when things feel overwhelming (rate limits, OOM risk, error storms).
- [SNAPSHOT] Take Session Snapshots for later review (logs, stats, notes) and append them to the vault.

This Skill assumes the HyperCode V2.4 stack is running with:

- 29/29 containers healthy and Gordon Tier 2 complete (OTLP, cache, rate limits, circuit breakers).
- Redis DB 1 (cache) and DB 2 (rate limiting) split correctly.
- BROski token economy and Stripe flows live.
- MCP-GitHub gateway available on agent-net.

## [USAGE] How Agents Should Use It

### Claude Code / Claude API

Use this as a **Skill file**. For Claude Code, load it via the Skills UI or CLI. For Claude API, include it in the system messages or as a loaded Skill.

Example (Claude Code):

1. Download this file as `Hyperfocus-Zone-Agent-Swarm.SKILL.md`.
2. Open Claude Code → Skills → "Import from file" → select the Skill file.
3. In a new session, call the provided commands, for example:
   - `/hyperfocus:chunk-task "Finish BROski Hyperfocus Zone MVP"`
   - `/hyperfocus:obsidian-sync "~/vaults/BROski-Hyperfocus-z0ne"`

### HyperAgent-SDK / CLI

In the HyperAgent-SDK repo:

```bash
node cli/index.js skills load ./skills/Hyperfocus-Zone-Agent-Swarm.SKILL.md
node cli/index.js agents list
```

Agents such as `agent-x`, `healer-agent`, and `crew-orchestrator` can then be instructed (via tasks) to call the flows defined in this Skill.

---

## [COMMANDS] Slash Commands & Behaviours

Below are the main commands this Skill defines. Each section explains **intent**, **behaviour**, and **how agents should call it**.

### 1. `/hyperfocus:chunk-task`

**Intent:**
Turn an overwhelming goal into a tiny stack of 5–15 minute steps with strong first-move energy for ADHD brains.

**Call:**
```text
/hyperfocus:chunk-task "<big-goal>"
```

**Behaviour:**
- Read the goal and produce 3–7 steps, each completable in ~5–15 minutes.
- Mark 1 step as **DO THIS FIRST**.
- For each step, generate:
  - A short command (e.g. `run tests`, `wire webhook`, `write SKILL header`).
  - A suggested agent (e.g. `agent-x`, `healer-agent`, `hyper-architect`).
  - An optional BROski$ reward (e.g. `+50` for completing the step).
- When running inside HyperCode V2.4, emit a machine-readable JSON block so crew-orchestrator can register each step as a task.

**Agent Notes:**
- Always prefer shorter, clearer steps over perfection.
- Use language that is encouraging and non-judgemental.
- Never prescribe time beyond a rough estimate.

---

### 2. `/hyperfocus:obsidian-sync`

**Intent:**
Sync an Obsidian vault (Hyperfocus Zone brain) into the HyperCode ecosystem so agents can see notes as tasks, not just text.

**Call:**
```text
/hyperfocus:obsidian-sync "<vault-path-or-profile>"
```

**Behaviour:**
- Treat the path as a logical reference (agents should not assume direct disk access unless configured).
- The expected environment:
  - Obsidian vault content is mirrored into Minio (object storage) on `data-net`.
  - Chroma or a similar vector store is available for embeddings.
- When invoked:
  1. List vault notes in a configurable `tasks/` or `projects/` folder.
  2. Parse headings, checkboxes, and tags to infer tasks.
  3. For each actionable note, emit a short spec:
     - `title`, `description`, `repo`, `service`, `priority`, `estimated_time`.
  4. Optionally emit a `spec-kit` spec that can be fed into Spec Kit or open-swe.

**Agent Notes:**
- When unsure, ask the user which part of the vault to treat as tasks.
- Maintain privacy: never exfiltrate or repeat private details outside the Hyperfocus environment.

---

### 3. `/hyperfocus:quick-win`

**Intent:**
Find a 30–90 minute upgrade that gives a visible dopamine hit and moves the Hyperfocus Zone forward.

**Call:**
```text
/hyperfocus:quick-win "<area-or-feature>"
```

**Behaviour:**
- Look at the current context (WHATS_DONE, CLAUDE_CONTEXT, issues, NEXT_STEPS/etc.) and pick a single, well-scoped improvement.
- Generate a tiny plan:
  - 3–5 steps, each 5–15 minutes.
  - Clear definition of done (e.g. new endpoint returns 200, dashboard panel visible, test passing).
- When inside a repo with Git access:
  - Suggest a branch name: `feat/quick-<slug>`.
  - Suggest a commit message.
  - Optionally outline a very small PR description.

**Agent Notes:**
- Favour safety and observability over risky refactors.
- Good examples: adding a missing healthcheck, wiring a dashboard panel, improving a small error message flow.

---

### 4. `/hyperfocus:gamify`

**Intent:**
Reward progress with BROski$ tokens and pet XP, wired into the existing BROski token economy.

**Call:**
```text
/hyperfocus:gamify "<milestone>" [amount]
```

**Behaviour:**
- Treat this as a request to **propose** a reward, not to directly move money.
- In HyperCode V2.4, the real reward flows through the secure APIs:
  - `POST /api/v1/economy/award-from-course` with the right secret.
  - Stripe webhooks already award starter/builder/hyper bundles.
- This Skill:
  - Suggests a sensible BROski$ amount (250, 500, 1000) based on difficulty.
  - Suggests a pet XP change or rarity bump if BROskiPets is wired in.
  - Emits a short, celebratory message suitable for Discord/broski-bot.

**Agent Notes:**
- Never assume access to secrets or direct Stripe control.
- Stay within the patterns defined in the backend services.

---

### 5. `/hyperfocus:hyper-split`

**Intent:**
Take an intimidating project and fan it out to multiple specialised agents for parallel progress.

**Call:**
```text
/hyperfocus:hyper-split "<big-task>"
```

**Behaviour:**
- Identify 2–4 natural sub-domains (e.g. infra, backend, frontend, docs).
- For each sub-domain:
  - Propose a specialist agent (e.g. infra-healer, hyper-architect, docs-scribe).
  - Produce a 3–5 step mini-plan.
- Emit an execution graph that crew-orchestrator can use:
  - Nodes: tasks.
  - Edges: dependencies.
- When possible, ensure plans are compatible with existing chaos tests, healthchecks, and circuit breakers.

**Agent Notes:**
- Prefer fewer, well-defined sub-agents over a noisy swarm.
- Respect current system limits and memory caps.

---

### 6. `/hyperfocus:focus-panic`

**Intent:**
Provide a safe, calm-down sequence when the user or system feels overloaded.

**Call:**
```text
/hyperfocus:focus-panic
```

**Behaviour:**
- Do **not** immediately restart or destroy infrastructure.
- Instead, propose a calm-down playbook, such as:
  1. Pause heavy work (load tests, big builds, mass refactors).
  2. Surface a single, small next step the user can do.
  3. Offer a short breathing or grounding exercise.
  4. Print a quick status summary (healthchecks, errors, queue depth).
- For automated environments, suggest non-destructive actions only (e.g. temporarily lowering concurrency or disabling non-essential agents).

**Agent Notes:**
- Language must be gentle, non-judgemental, and supportive.
- Never imply failure; emphasise recovery and pacing.

---

### 7. `/hyperfocus:morning-brief`

**Intent:**
Create a short, ADHD-friendly morning briefing from system data and notes.

**Call:**
```text
/hyperfocus:morning-brief
```

**Behaviour:**
- Pull in:
  - Recent activity (commits, deployments, major errors) if accessible.
  - Health summarised from metrics (services up/down, error spikes).
  - NEXT UP style bullets from existing planning docs.
- Output a brief with sections like:
  - **Status:** 2–4 bullets.
  - **Today’s Targets:** 3–5 bullets.
  - **One Tiny First Move:** 1 bullet.

**Agent Notes:**
- Focus on clarity over completeness.
- Great for starting a work session or rebooting after a break.

---

### 8. `/hyperfocus:zone-playground`

**Intent:**
Prepare or update a demo/playground experience (e.g. Hyperfocus Zone showcase site) so others can see and feel the system.

**Call:**
```text
/hyperfocus:zone-playground "<audience-or-goal>"
```

**Behaviour:**
- Suggest a plan for updating or deploying the playground:
  - What to show (agents, dashboards, pets, tokens).
  - How to deploy (e.g. Vercel, Docker profile, etc.).
  - What story to tell (for ADHD/neurodivergent developers).
- When integrated with MCP-GitHub/Vercel skills, this can be turned into concrete commands.

**Agent Notes:**
- Aim for a clear, emotionally resonant demo, not a full product rebuild.

---

### 9. `/hyperfocus:git-hook`

**Intent:**
Design a post-commit hook that ties Git activity into BROski$ and achievements.

**Call:**
```text
/hyperfocus:git-hook
```

**Behaviour:**
- Describe, in detail, how to:
  - Add a `post-commit` hook that calls a local script.
  - Have that script record commit metadata (author, message, size) and call a backend endpoint which can decide rewards.
  - Keep secrets and tokens out of Git; use env vars and Docker secrets.
- Provide a template script and hook example in the answer when requested.

**Agent Notes:**
- Never suggest committing secrets or private data.
- Design hooks to fail gracefully so they never block Git.

---

### 10. `/hyperfocus:snapshot`

**Intent:**
Capture the current state of the system and user context into a single snapshot.

**Call:**
```text
/hyperfocus:snapshot
```

**Behaviour:**
- Define what should be included in a snapshot, such as:
  - A summary of current tasks and their state.
  - High-level system health.
  - Any active incidents.
  - A short reflection written in the user’s tone.
- For Obsidian users, append it to a `Session Log` note.

**Agent Notes:**
- Snapshots are for humans first, agents second.
- Keep them readable, encouraging, and future-you friendly.

---

## [SAFETY] Constraints & Guardrails

- Always prioritise user consent, privacy, and emotional safety.
- Do not invent or assume secrets, tokens, or external access.
- Treat all commands as **plans and suggestions** until a human or trusted automation layer executes them.
- For any destructive or high-risk suggestion (e.g. deleting data, rotating keys, mass refactor), explicitly call it out and suggest human review.

---

## [ADAPTATION] Neurodivergent-Friendly Style

When using this Skill:

- Prefer short, clear sentences first, then optional deeper explanation.
- Use headings, bullets, and small chunks.
- Celebrate wins explicitly (e.g. "Nice one, BROski♾️!").
- Offer one tiny next action instead of a giant wall of tasks.

This keeps the Hyperfocus Zone aligned with the needs of ADHD, dyslexic, and autistic minds.
