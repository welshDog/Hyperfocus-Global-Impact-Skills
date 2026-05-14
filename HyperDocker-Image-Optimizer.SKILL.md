# [SKILL] HyperDocker Image Optimizer

> A neurodivergent‑friendly Docker skill that teaches agents how to design, refactor, and harden Dockerfiles for the HyperCode V2.4 ecosystem without breaking sacred rules.

## [MAP] What This Skill Covers

This Skill trains agents to:

- Design **multi‑stage Dockerfiles** for Python, Node/TypeScript, and static frontends.
- Keep images **small, cache‑friendly, and secure** while respecting existing conventions.
- Add or fix **HEALTHCHECK** instructions in a safe, consistent way.
- Apply **resource limits and security best practices** aligned with HyperCode V2.4.
- Avoid all patterns that violate the project’s **Sacred Rules** (secrets, imports, images, etc.).

It is tuned for your current stack:

- Python services built on `python:3.11-slim` split into Part A / Part B Dockerfiles. [cite:13]
- Trivy scanning in CI, target of 0 critical CVEs and hardened Dockerfiles. [cite:12]
- 29 containers with memory limits configured to prevent OOM cascades. [cite:12]

Agents should treat these instructions as **constraints and best practices** whenever they touch Dockerfiles in HyperCode or related repos.

---

## [CONTEXT] HyperCode Docker Baseline

When optimising Dockerfiles for this ecosystem, assume:

- Services are orchestrated via `docker-compose.yml` with multiple networks and strict isolation (app‑net, data‑net, obs‑net, agent‑net). [cite:13]
- Security is enforced by: Trivy CI, Docker secrets, rate‑limit and circuit breaker patterns, and no `.env` files in Git. [cite:12][cite:13]
- Memory limits are already defined in compose (e.g. agent‑x 1G, core 1.5G, Postgres 2G) and must not be removed. [cite:12]

This Skill should **never suggest**:

- Bypassing Trivy, removing healthchecks, or disabling resource limits.
- Baking secrets, API keys, or `.env` content into images.
- Using heavyweight base images where slimmer variants exist.

---

## [GUIDE] Multi‑Stage Build Patterns

### Python Services (HyperCode Core & Agents)

When refactoring or designing Dockerfiles for Python‑based services:

1. **Use multi‑stage builds**:
   - `builder` stage: install build dependencies, compile wheels, run asset builds.
   - `runtime` stage: copy only the necessary wheels and application code.
2. Base images:
   - Prefer `python:3.11-slim` for runtime stages.
   - For builder stages, consider `python:3.11-slim` plus build tools only when needed.
3. Layering:
   - Group `apt-get` installs into a single `RUN` with `--no-install-recommends` and clean cache.
   - Install Python deps with pinned versions where possible.

Agents should:

- Preserve existing entrypoints and health endpoints.
- Keep the service compatible with existing OTLP, Redis, and HTTP instrumentation.

### Node / Frontend / Static Assets

For Node‑based or static frontends:

- Use a builder stage with Node (or appropriate tool) to build assets.
- Use a minimal runtime image (e.g. nginx, caddy, or an app server) to serve compiled assets only.
- Avoid shipping dev dependencies and build tools in the final image.

---

## [RULES] HEALTHCHECK Conventions

Agents must follow these conventions when adding or adjusting healthchecks:

- Prefer simple HTTP checks hitting `/health` or `/ready` endpoints where they exist.
- For observability tools (Loki, Promtail, auxiliary agents) use existing patterns:
  - `curl -f http://localhost:<port>/ready` or `wget -q http://localhost:<port>/ready` as already used for similar services. [cite:13]
- Ensure healthchecks are **fast** and do not load databases unnecessarily.

For containers currently missing healthchecks but tracked as TODOs (e.g. certain log/metrics components), agents can:

- Propose healthcheck snippets using the same style as the ones that were added for other services.
- Note that healthchecks must be non‑destructive and safe in all environments.

---

## [SECURITY] Hardening & CVE Reduction

This Skill emphasises:

- Keeping attack surface minimal: remove compilers, build tools, and unused packages from the runtime stage.
- Ensuring images pass Trivy with 0 critical CVEs before merging, in line with existing security hardening work. [cite:12]
- Following existing patterns for:
  - Non‑root users where practical.
  - Read‑only filesystem plus tmpfs for writable paths.
  - Dropping unnecessary capabilities if the service does not need them.

Agents should:

- Suggest specific improvements (e.g. move a vulnerable package to build stage only) rather than generic “secure this”.
- Preserve compatibility with the current monitoring and logging setup.

---

## [PRACTICAL] How Agents Should Use This Skill

When asked to optimise or create Dockerfiles:

1. **Assess the current state**:
   - Identify duplicate or unnecessary layers.
   - Check if a multi‑stage build can reduce size.
   - Look for installed tools not required at runtime.
2. **Propose a multi‑stage refactor** consistent with this Skill.
3. **Add/align HEALTHCHECKs** using existing patterns.
4. **Call out any risky changes explicitly** and recommend human review before applying.

When unsure, agents must:

- Ask clarifying questions about the environment.
- Default to conservative refactors that improve clarity and size without changing the external behaviour.

---

## [STYLE] Neurodivergent‑Friendly Explanations

When presenting Dockerfile changes to the user:

- Use short, clear sentences first, then optional deeper explanations.
- Show before/after snippets in small chunks.
- Highlight quick wins (smaller image, fewer layers, added healthcheck).
- Celebrate progress explicitly (e.g. “Nice one, BROski♾️ — image is leaner and safer now.”).

This keeps Docker optimisation in line with the Hyperfocus Zone ethos.
