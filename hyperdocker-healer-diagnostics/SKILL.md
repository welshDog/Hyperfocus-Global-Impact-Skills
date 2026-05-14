# [SKILL] HyperDocker Healer Diagnostics

> A diagnostic playbook Skill for Healer‑Agent and friends: how to investigate, stabilise, and report Docker/container issues in the HyperCode V2.4 stack without panic.

## [MAP] Purpose

This Skill gives Healer‑Agent and other infra‑aware agents a **structured, calm procedure** for:

- Diagnosing container problems (crash loops, OOMs, healthcheck failures).
- Using the existing observability stack (Prometheus, Grafana, Loki, Tempo) effectively.
- Suggesting safe, incremental actions that respect HyperCode's Sacred Rules and Gordon‑approved patterns.

Tuned to current state: 29 containers, Gordon Tier 2 complete (OTLP, Redis, rate limits, circuit breakers), memory limits applied to all services.

---

## [CONTEXT] Known Incident Patterns

Healer‑Agent must internalise these historical patterns:

| Exit Code | Pattern | Fix Applied |
|-----------|---------|-------------|
| 137 | OOM — agent‑x building ~30 images without memory limit | Memory cap per service |
| 128 | SIGTERM under stress | Review resource/queue usage |
| Auth loop | POSTGRESPASSWORD mismatch between container env and DB | Unix socket `ALTER USER` + compose fallback sync |

---

## [FLOW] Standard Diagnostic Procedure

When Healer‑Agent detects a problem, follow this order:

1. **Check container status**
   - `docker compose ps`
   - Note containers that are `unhealthy`, `Restarting`, or exiting.

2. **Check health endpoints**
   - `GET /health` and `GET /metrics` for affected services.

3. **Review logs**
   - `docker logs <service> --tail 200`
   - Look for: OOMKilled, auth failures, connection timeouts.

4. **Consult observability stack**
   - Grafana at `localhost:3001` — Tempo traces, Loki logs, Prometheus metrics.

5. **Summarise and propose**
   - Which service affected → symptoms → suspected cause → next steps.

---

## [PLAYBOOK] OOM & Resource Issues (Exit 137)

1. Confirm via logs + `docker stats --no-stream`.
2. Check current memory limits in compose for the service.
3. Look for runaway workloads (builds, batch jobs).
4. Suggest (do not directly apply):
   - Reduce concurrent work (worker count, queue depth).
   - Split heavy jobs into smaller tasks.
   - Slightly increase memory limit — flag for human review.

❌ Never: switch to unlimited memory or remove limits.

---

## [PLAYBOOK] Auth & DB Connection Problems

For hypercode‑core ↔ Postgres auth failures:

1. Recognise previous root cause: POSTGRESPASSWORD mismatch.
2. Safe recovery (human executes):
   - `docker exec -it postgres psql -U postgres`
   - `ALTER USER postgres WITH PASSWORD '<new-password>';`
   - Sync compose fallback and secrets files.
3. Confirm recovery via `/health` and basic queries.

❌ Never: force delete volumes or containers.

---

## [PLAYBOOK] Healthcheck & Service Degradation

If a service is `unhealthy` but still running:

1. Inspect healthcheck definition in Dockerfile or compose.
2. Verify health endpoint is accessible and fast.
3. If thresholds are too tight, suggest adjusted timeout/interval values.
4. For services without healthchecks, propose adding one (simple HTTP 200).

---

## [ACTIONS] What Healer‑Agent May Propose

✅ **Safe to propose:**
- Restart a single non‑critical container.
- Temporarily disable a noisy chaos test.
- Reduce concurrency or pause heavy background work.

❌ **Must not suggest:**
- Bringing the entire stack down without a back‑up plan.
- Deleting volumes, databases, or long‑lived data.
- Rotating secrets without updating all dependent services.

---

## [LOAD] How to Load This Skill

### Claude Code
```bash
curl -O https://raw.githubusercontent.com/welshDog/Hyperfocus-Global-Impact-Skills/main/hyperdocker-healer-diagnostics/SKILL.md
```
Then: Claude Code → Settings → Skills → Import → select `SKILL.md`

### HyperAgent‑SDK CLI
```bash
node cli/index.js skills load ./skills/hyperdocker-healer-diagnostics/SKILL.md
```

### Best Starter Prompt
```
Use the HyperDocker Healer Diagnostics skill. Container <service-name> is restarting. Run the standard diagnostic procedure and give me a calm summary + one next step.
```

---

## [STYLE] Calm, Neurodivergent‑Friendly Communication

- Calm, non‑alarming language always.
- Short summary first, details after.
- One small, clear recommended next step.
- Celebrate stabilisation: "Nice one, BROski♾️ — all services back to healthy."
