
GUIDE: AGENTS.LayeredArchitecture.Django
LANG: en-UTF8
PURPOSE: Enforce scalable, maintainable Django/DRF layered architecture.
SCOPE: Python services using Django + DRF as backend/API engine.
DEPENDS: AGENTS.tools.md (P1), codebase-awareness-and-docgen-dependency (P0)

LAYER_MAPPING:

- Interface (API): urls.py, views/viewsets, serializers (input/output only), permissions, schema.py
  → MUST NOT contain domain logic or heavy DB queries
- Application (UseCase): app_services/ or usecases/ (e.g. CreateOrder)
  → MUST own transaction boundaries (transaction.atomic)
- Domain (Core): domain/ (entities, value objects, policies)
  → MUST be pure Python; NO Django/DRF/ORM/settings imports
- Infrastructure (Persistence/Integrations): repositories/, infra/db/, clients/, adapters/
  → MAY map domain ↔ ORM; MUST NOT make business decisions
- Database: migrations/, schema (indexes/constraints), UTF-8 encoding (Persian data)

DEPENDENCY_RULES (MUST):

- Domain → NO Django/DRF/ORM/settings/clients
- Interface → NO direct ORM queries, NO transaction control, NO domain logic in serializers/views
- Application → MAY import Domain + Repository interfaces (NOT impl)
- Infrastructure → MAY import Domain types (for mapping only)

ANTI-PATTERNS (FORBIDDEN):

- God App, Fat View/Serializer
- Direct DB access from View/Serializer
- Circular app imports
- Unstructured "utils" dumping ground

API_LIFECYCLE (MUST):

1. Contract: request/response schema (drf-spectacular)
2. Error model: fixed envelope (error.code, error.message, trace_id)
3. Versioning: URI-based (/api/v1/...); breaking changes → new version
4. Deprecation: documented, non-breaking in same version

AUTHN/AUTHZ (MUST):

- Centralized REST_FRAMEWORK.auth/perm config
- Permission classes (not ad-hoc view checks)
- Throttling on sensitive endpoints (login/otp/reset)
- HTTPS-only token transport
- Token in header (Authorization), NEVER in URL
- Logs MUST NOT contain tokens/secrets

ORM_RULES (MUST):

- Models = persistence, NOT domain
- Domain model (if used) MUST be ORM-agnostic
- Complex queries → repository (infra), NOT view
- N+1 → controlled via select_related/prefetch_related
- Migrations: small, rollback-safe, deployable
- UTF-8 end-to-end (DB → app → API)

SERIALIZER/VIEW (MUST):

- Serializer: input validation + simple DTO mapping; NO business logic, NO DB queries
- View: HTTP orchestration only; call UseCase; apply perm/throttle; NO transaction, NO domain logic
- urls.py: versioned (/api/v1/...), namespaced, include-based

SETTINGS (MUST):

- Env-based secrets (NO hardcode)
- REST_FRAMEWORK: centralized auth/perm/throttle/versioning/pagination
- Multi-env support (dev/stage/prod) if needed
- Breaking config changes → require approval

APP_DESIGN (MUST):

- Apps = domain-bounded contexts (NOT monolithic "core")
- SRP: View / UseCase / Domain / Infra each single responsibility
- OCP: extend via new UseCase/Policy, NOT modify existing
- DIP: Application → Repository interface, NOT impl

TESTING (MUST for sensitive changes):

- Domain: unit (no Django/DB)
- Application: with mock/fake repo
- API: DRF test client (perm/success/validation/error)
- Each new endpoint → ≥1 perm test, 1 success, 1 validation error
- Breaking change → version compatibility test

FITNESS_CHECKS (MUST enforce in CI):

1. Domain imports Django/DRF → FAIL
2. View imports repo impl → FAIL
3. transaction.atomic outside Application → FAIL
4. OpenAPI schema missing new endpoints → FAIL
5. Throttle missing on sensitive endpoints → FAIL

EXECUTION_PROTOCOL (Agent MUST):

1. Identify layer of change (Interface/App/Domain/Infra/DB)
2. Report impact on:
   - API contract/version
   - DB schema/migrations
   - Security (auth/authz/token)
   - Performance (queries)
   - Tests
3. If conflict with this guide or AGENTS.tools.md:
   - HALT
   - Report conflict (per guideline-priority-and-resolution §8)
   - Propose Exception Record if needed
