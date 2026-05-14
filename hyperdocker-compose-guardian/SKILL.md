# [SKILL] HyperDocker Compose Guardian

> A safety‑first Docker Compose skill that teaches agents how to modify, extend, and debug `docker-compose.yml` for HyperCode V2.4 without breaking networks, secrets, or observability.

## [MAP] Purpose

This Skill gives agents a rulebook for working with compose files in the Hyperfocus ecosystem:

- Respect the **five‑network** isolation model (app‑net, data‑net, obs‑net, agent‑net, etc.).
- Use the **correct active Prometheus config** and avoid stale files.
- Preserve **resource limits, healthchecks, and secrets** patterns already in place.
- Keep the stack aligned with Gordon Tier 1+2 observability guarantees.

Agents should treat these instructions as constraints any time they suggest changing compose or Prometheus configs for HyperCode and related repos.

---

## [CONTEXT] HyperCode Compose Model

Key facts agents must remember:

- The main stack is defined in `docker-compose.yml`, with secrets injected via `docker-compose.secrets.yml` that must always be used alongside it.
- There are 29 services/containers across multiple networks, all expected to be healthy.
- Networks:
  - `app-net` – core app services.
  - `data-net` – Redis, Postgres, Chroma, Minio (internal only, no internet).
  - `obs-net` – Prometheus, Grafana, Loki, Tempo (metrics/logging only).
  - `agent-net` – AI agents, MCP gateway, orchestrators.
- Active Prometheus config lives at `monitoring/prometheus/prometheus.yml`; the root `prometheus.yml` is stale/unused and must not be edited.

---

## [RULES] Networks & Isolation

When adding or modifying services:

- Only attach services to the networks they truly need.
  - Database and storage services must remain isolated on `data-net` and not exposed to the public internet.
  - Observability stack components (Prometheus, Grafana, Loki, Tempo) stay on `obs-net` plus internal links as needed.
  - Agents communicate over `agent-net` and should not be given unnecessary access to `obs-net` or `data-net` unless explicitly required.
- Do not introduce new networks without a clear design reason.

Agents should:

- Keep network connectivity minimal and principle‑of‑least‑privilege.
- Call out any suggestion that would expose internal services directly to the outside world.

---

## [RULES] Secrets & Environment

Compose changes must follow these patterns:

- **Secrets**
  - Use Docker secrets and `.txt` files for sensitive values.
  - Do not hardcode secrets or `.env` values into the compose file.
  - For HyperCode core, remember that secrets were recovered and moved into `.env` and secrets files in a controlled way.
- **Envfile Tech Debt**
  - hypercode-core currently relies on host‑side variable substitution; long‑term we will add `env_file: .env` under the service.
  - Agents may suggest this improvement but should mark it as a change that needs human approval.

Agents should never:

- Suggest committing `.env` files or raw secrets into Git.
- Merge schemas between Supabase and the V2.4 Postgres instance.

---

## [RULES] Resource Limits & Healthchecks

Resource limits:

- All services already have memory limits configured to prevent OOM cascades:
  - `agent-x: 1G` | `hypercode-core: 1.5G` | `postgres: 2G`
- Agents must preserve these limits and should not remove them.
- Limit increases are incremental, justified, and always flagged for human review.

Healthchecks:

- 29 containers have healthchecks wired in.
- New services or fixes must:
  - Follow the same style: `curl -f http://localhost:<port>/health` or `/ready`.
  - Keep healthchecks fast and non‑destructive.

---

## [RULES] Prometheus & Observability

Prometheus configuration:

- ✅ Only edit `monitoring/prometheus/prometheus.yml`
- ❌ Never edit the root‑level `prometheus.yml` (stale)
- After changes, reload Prometheus: `curl -X POST localhost:9090/-/reload`

Telemetry:

- OTLP traces → Tempo at `http://tempo:4317`
- Logs → Loki/Promtail
- Metrics → Prometheus → Grafana

Ensure any new service exposing metrics is compatible with Prometheus scraping.

---

## [PRACTICAL] Typical Agent Tasks

When an agent is asked to work on compose files:

1. **Identify the goal**: new service, network change, env fix, or observability tweak.
2. **Check existing patterns** in `docker-compose.yml` and `docker-compose.secrets.yml`.
3. **Propose a change** that:
   - Attaches to correct networks only.
   - Preserves or adds resource limits.
   - Adds or reuses healthchecks.
   - Keeps secrets externalised.
4. **Call out risks** and recommend human review for impactful changes.

Always suggest running `docker compose ps` and hitting health endpoints to validate.

---

## [LOAD] How to Load This Skill

### Claude Code
```bash
curl -O https://raw.githubusercontent.com/welshDog/Hyperfocus-Global-Impact-Skills/main/hyperdocker-compose-guardian/SKILL.md
```
Then: Claude Code → Settings → Skills → Import → select `SKILL.md`

### HyperAgent‑SDK CLI
```bash
node cli/index.js skills load ./skills/hyperdocker-compose-guardian/SKILL.md
```

### Best Starter Prompt
```
Use the HyperDocker Compose Guardian skill before making any change to docker-compose.yml. Check networks, limits, healthchecks, and secrets compliance.
```

---

## [STYLE] Explanation for Humans

Use short, clear sentences and bullet points. Highlight what changed and why. Emphasise safety: "Networks preserved", "Secrets untouched", "Healthchecks added". Celebrate wins: "Nice one, BROski♾️ — stack is safer and clearer now."
