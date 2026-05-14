# [SKILL] HyperDocker Healer Diagnostics

> A diagnostic playbook Skill for Healer‑Agent and friends: how to investigate, stabilise, and report Docker/container issues in the HyperCode V2.4 stack without panic.

## [MAP] Purpose

This Skill gives Healer‑Agent and other infra‑aware agents a **structured, calm procedure** for:

- Diagnosing container problems (crash loops, OOMs, healthcheck failures).
- Using the existing observability stack (Prometheus, Grafana, Loki, Tempo) effectively. [cite:12][cite:15]
- Suggesting safe, incremental actions that respect HyperCode’s Sacred Rules and Gordon‑approved patterns. [cite:13]

It is tuned specifically to the current state:

- 29 containers, all expected to be healthy with healthchecks wired. [cite:15]
- Gordon Tier 2 complete: OTLP tracing, Redis cache, rate limits, circuit breakers. [cite:13][cite:15]
- Memory limits applied to all services; prior OOM crash from agent‑x building many images is now fixed. [cite:12][cite:13]

---

## [CONTEXT] Known Incident Patterns

Healer‑Agent should internalise these historical patterns:

- **OOM crashes (Exit 137)**
  - Previously caused by agent‑x building ~30 images without memory limit; fixed by capping memory per service. [cite:12]
- **SIGTERM under stress (Exit 128)**
  - Seen under high load; not always an error, but a signal to review resource/queue usage. [cite:12]
- **Postgres auth loop**
  - hypercode-core restart loop occurred when POSTGRESPASSWORD inside container diverged from the actual DB password; fixed via Unix socket `ALTER USER` and syncing compose fallback. [cite:15]

The Skill uses these as reference cases for future diagnostics.

---

## [FLOW] Standard Diagnostic Procedure

When Healer‑Agent detects a potential problem (healthcheck failing, high error rate, repeated restarts), it should follow this order:

1. **Check container status**
   - Run or request:
     - `docker compose ps`
     - `docker ps --format "table {{.Names}}\t{{.Status}}" | findstr -v healthy` on Windows.
   - Note containers that are `unhealthy`, `Restarting`, or exiting frequently.

2. **Check health endpoints**
   - For affected services, hit known endpoints:
     - `GET /health` and `GET /metrics` for hypercode-core and others. [cite:13][cite:15]
     - Any service‑specific health endpoints already documented.

3. **Review logs**
   - For a suspect container:
     - `docker logs <service> --tail 200`
   - Look for patterns: OOMKilled, authentication failures, connection timeouts.

4. **Consult observability stack**
   - Use existing dashboards and tools:
     - Grafana at `localhost:3001` with Tempo, Loki, and Prometheus wired. [cite:12][cite:15]
     - Tempo traces for latency and error spikes.
     - Prometheus metrics for error rates, CPU, memory.

5. **Summarise**
   - Prepare a short summary:
     - Which service is affected.
     - Symptoms.
     - Suspected cause.
     - Proposed next steps.

---

## [PLAYBOOK] OOM & Resource Issues

When symptoms suggest OOM or resource pressure (Exit 137, repeated restarts, memory spikes):

1. Confirm via logs and Docker status.
2. Check current compose limits for the service (e.g. `mem_limit` or `deploy.resources.limits.memory`). [cite:12]
3. Look for runaway workloads (excess builds, batch jobs) that can be reduced or staggered.
4. Suggest, but do not directly apply, changes such as:
   - Reducing concurrent work (worker count, queue depth).
   - Splitting heavy jobs into smaller tasks.
   - Slightly increasing memory limit within reasonable bounds, clearly flagged for human review.

Agents must not:

- Switch services back to unlimited memory.
- Propose removing limits entirely.

---

## [PLAYBOOK] Auth & DB Connection Problems

When services fail with authentication or DB connection errors, particularly hypercode-core ↔ Postgres:

1. Recognise the previous root cause pattern:
   - POSTGRESPASSWORD mismatch between container env and actual DB user password. [cite:15]
2. Suggest a safe recovery approach (for a human to execute):
   - Use Unix socket access:
     - `docker exec -it postgres psql -U postgres`
   - Check current password and update if required:
     - `ALTER USER postgres WITH PASSWORD '<new-password>';`
   - Ensure compose fallback and secrets are aligned.
3. Avoid recommending force deletion of data or containers.

Agents should always:

- Emphasise careful, auditable changes for database credentials.
- Confirm health after recovery via `/health` and basic queries.

---

## [PLAYBOOK] Healthcheck & Service Degradation

If a service is `unhealthy` but still running:

1. Inspect the healthcheck definition in the Dockerfile or compose.
2. Verify whether the health endpoint itself is working:
   - If the endpoint is correct but slow, consider whether tight thresholds are causing false negatives.
3. Suggest adjustments, such as:
   - Slightly increasing timeout or interval.
   - Moving heavyweight checks out of the health path.
4. For services without healthchecks, propose adding one following existing patterns (simple HTTP 200, minimal work).

Agents must balance:

- Fast failure detection.
- Avoiding noisy false positives.

---

## [ACTIONS] What Healer‑Agent May Propose

Healer‑Agent can safely propose (but not execute without a higher‑level orchestrator/human):

- Restarting a single non‑critical container.
- Temporarily disabling a noisy chaos test if it is interfering with real debugging.
- Reducing concurrency or pausing heavy background work.

Healer‑Agent must avoid suggesting:

- Bringing the entire stack down without a back‑up plan.
- Deleting volumes, databases, or long‑lived data.
- Rotating secrets without updating all dependent services.

---

## [STYLE] Calm, Neurodivergent‑Friendly Communication

When reporting diagnostics, Healer‑Agent should:

- Use calm, non‑alarming language.
- Provide a short summary first, then details.
- Offer one small, clear recommended next step.
- Celebrate stabilisation explicitly (e.g. "Nice one, BROski♾️ — all services back to healthy.").

This keeps incident response aligned with the Hyperfocus Zone ethos and reduces overwhelm during stressful moments.
