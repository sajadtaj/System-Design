
### ✅ `AGENTS.md` — Root Agent Constitution (Policy Router + Precedence Lock)

**Language:** `en-UTF8`
**Status:** `Active`
**Purpose:** Enforce deterministic, auditable, conflict-free execution by Agent.

---

#### **0. Purpose**

This document is the **constitutional foundation** for all Agent actions in this repository.
Before any action (analysis, coding, file modification, command execution), the Agent **MUST** read and comply with this file.

It:

- Fixes Single Sources of Truth (SoT)
- Locks guideline precedence
- Makes reference paths immutable (only modifiable here)
- Standardizes **Stop** and **Conflict Resolution** behavior
- Eliminates guessing, ad-hoc path creation, or improvisation

---

#### **1. Reference Files (Immutable SoT Paths)**

##### **1.1. Agent MUST use exactly these three reference files**

> Paths may change in the future. **This section is the only authorized location for path updates.**
> Agent **MUST NOT** use any other path unless explicitly modified here.

- **`ARCHITECTURE_CONTRACT`**: `./AGENTS.LayeredArchitecture.Django.md`*(May later be replaced by one of:)*

  - `./AGENTS.MicrokernelArchitecture.Engine.md`
  - `./AGENTS.MicroservicesArchitecture.airflow.md`
- **`TOOLING_CONTRACT`**: `./AGENTS.tools.md`
- **`GUIDELINE_GATEWAY`**: `./assistant/guideline/root-guideline-and-invocation.json`

##### **1.2. Path Change Policy**

- Agent **MUST NEVER** change these paths autonomously.
- Any path change = **Structural Change** → requires **explicit user approval**.

---

#### **2. Precedence Order (Mandatory Conflict Resolution)**

In case of **any conflict or contradiction**, the following order applies:

1. **`AGENTS.md` (this file)** — highest authority
2. **`ARCHITECTURE_CONTRACT`** — service-specific architecture rules
3. **`TOOLING_CONTRACT`** — tooling, scaffolding, execution standards
4. **`GUIDELINE_GATEWAY` and all sub-guidelines** — operational policies

**Rule:**
If any guideline recommends something explicitly prohibited by Architecture/Tooling contracts:
→ Agent **MUST HALT** and issue a **Conflict Report** (Section 7).

---

#### **3. Non-Negotiable Hard Rules**

##### **3.1. No Guessing**

Agent **MUST** base all decisions **only** on:

- `truth_sources` defined in `GUIDELINE_GATEWAY`
- Reference files listed in Section 1
  → **Guessing, assumption, or path/code generation without SoT backing is FORBIDDEN.**

##### **3.2. No Improvisation in Scaffolding**

Agent **MUST** use official tools/Templates when available (e.g., Django, Cookiecutter, Copier, Docker).→ **Manual boilerplate generation is FORBIDDEN**, except:

- Tool fails to respond, **OR**
- Change is a **tiny, documented customization** on top of official output
  → In either case, Agent **MUST justify** the exception.

##### **3.3. UTF-8 End-to-End**

Agent **MUST enforce UTF-8** in:

- All text files
- Code
- Documentation
- Persian/RTL data in DB, UI, logs, APIs

##### **3.4. Structural Changes Require Approval**

The following changes are **FORBIDDEN without explicit user approval**:

- Add/remove dependencies
- Change tool/framework versions or pins
- Modify service topology or architecture boundaries
- Change AuthN/AuthZ strategy or API versioning scheme
- Alter DB schema policy or migration strategy
- Modify reference file paths (Section 1)

---

#### **4. Command Execution Protocol**

Agent **MUST** align behavior with `invocation_flows` in `GUIDELINE_GATEWAY`.

| User Command                 | Agent Flow                                      |
| ---------------------------- | ----------------------------------------------- |
| `make_plan`                | →`invocation_flows.make_plan`                |
| `make_task`                | →`invocation_flows.make_task`                |
| `execute_task`             | →`invocation_flows.execute_task`             |
| `milestone_completion`     | →`invocation_flows.milestone_completion`     |
| `manual_consistency_check` | →`invocation_flows.manual_consistency_check` |

**Rules:**

- Agent **MUST invoke ONLY relevant guidelines** (no over-inclusion)
- Agent **MUST respect P0 > P1 > P2 priority**
- Agent **MUST check all `stop_conditions` BEFORE execution**

---

#### **5. Change Classification (Mandatory for Guideline Selection)**

##### **5.1. API Change**

Triggered by change in:

- routes/urls
- views/viewsets
- serializers
- auth/permissions/throttling
- response schema, pagination, error format

→ Agent **MUST** invoke:

- `api-contract-and-versioning` (minimum)
- Enforce versioning, deprecation, OpenAPI contract

##### **5.2. DB Change**

Triggered by change in:

- models, migrations, indexes, constraints

→ Agent **MUST**:

- Report schema/perf risks
- Follow migration policy (small, rollback-safe, deployable)
- Add/update tests for schema changes

##### **5.3. Runtime/DevOps Change**

Triggered by change in:

- Docker/Compose/env/logging/observability

→ Agent **MUST** invoke:

- `observability-and-logging`
- Report impact on deploy, health checks, monitoring

##### **5.4. Pure Code / Refactor**

Triggered by change in logic/structure only

→ Agent **MUST**:

- Enforce `ARCHITECTURE_CONTRACT` layering
- Apply relevant `coding-solid-and-structure`, `coding-style-and-docstring` guidelines

---

#### **6. Mandatory Output Contract**

##### **6.1. For every code/file change (`execute_task` or similar)**

Agent **MUST** include at start of response:

```
File Path: <path>
File Name: <name>
Class/Function Name: <name> (if applicable)
What changed: <concise description>
Why changed: <rationale>
Affected parts: DB / DevOps / API / Data / None
Replacement: full / partial
```

##### **6.2. Applied Guidelines**

Agent **MUST** declare:
`Applied Guidelines: [list]`
→ At minimum, all guidelines used per `GUIDELINE_GATEWAY.invocation_flows`

##### **6.3. Stop Mode**

If any `stop_condition` is met:
→ Agent **MUST output ONLY**:

```
[STOP] Gap Report:
- Missing: <what’s missing>
- Required: <file/command needed>
- Next Step: <exact user action>
```

→ **NO** code, NO execution, NO suggestions beyond recovery path.

---

#### **7. Conflict Report Format (Mandatory)**

On conflict (doc mismatch or missing input), Agent **MUST** output **exactly**:

```
Conflict Type: Hard / Soft / Coverage
Guidelines Involved: [id1, id2, ...]
What conflicts: <1-sentence precise description>
Priority Decision: <winning guideline + why (cite precedence)>
Blocked On: <missing_input / decision_required>
Next Step: <exact user action to resolve>
```

→ Format **MUST** match `guideline-priority-and-resolution §8`.

---

#### **8. Multi-Service Support (Future-Proofing)**

This repo may contain multiple services with different architectures.

**Rule:**

- Each service **MAY** have its own `ARCHITECTURE_CONTRACT` (e.g., `./serviceA/AGENTS.*.md`)
- Agent **MUST** use the **closest** `AGENTS.*.md` in the service’s path
- **Global precedence order (Section 2) still applies**

---

#### **9. Pre-Merge Checklist (Agent MUST Verify)**

Before any merge proposal, Agent **MUST confirm**:

- [ ] All `stop_conditions` checked
- [ ] Tools used per `TOOLING_CONTRACT` (no manual scaffolding)
- [ ] Architecture per `ARCHITECTURE_CONTRACT`
- [ ] API/DB/Runtime impact reported (if applicable)
- [ ] Minimum tests added/updated (if behavior changed)
- [ ] `Applied Guidelines` declared
- [ ] **Zero guessing** — all decisions backed by SoT
