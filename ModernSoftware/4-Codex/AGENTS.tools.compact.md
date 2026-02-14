TOOLING_POLICY: AGENTS.tools.md
LANG: fa-UTF8
RULE: Prefer official tools over hand-made boilerplate

HARD_RULES (MUST):

1. No manual scaffolding if official tool exists (Django/DRF/Cookiecutter/Copier/Flutter/Airflow/Docker/Mermaid/MkDocs)
   - Exception: tool fails OR tiny customization (must justify)
2. No tool conflict: e.g. Django → no Flask/FastAPI; uv → no pip/venv; MkDocs → no custom docs
3. Maintain architectural integrity: no new arch/tools without impact analysis (Backend/DB/DevOps/Data) + approval
4. Print version before execution: for audit/reproducibility
5. Pin versions in: pyproject.toml, requirements.txt, package.json, Dockerfile, lockfiles
6. UTF-8 everywhere: text files, code, DB, UI (esp. Persian data)
7. Use ONLY commands in this doc; no guesswork, no external patterns

TOOL_MATRIX (Pinned versions; lock in config files):

Python: ≥3.11 → `python --version`; run via `uv run python -m ...`
uv: ≥0.4 → `uv --version`; sync: `uv sync`; run: `uv run ...`; no deps without approval
Django: ≥4.2 (LTS) → `uv run django-admin startproject <name> .`; `manage.py startapp/makemigrations/migrate/runserver`
DRF: ≥3.14 → use ViewSet/Serializer/Router; no raw endpoints; test with pytest
PostgreSQL: ≥14 → UTF-8 encoding + proper collation; schema via migration only; explain perf risk for heavy changes
Docker: ≥24 → no raw install if Dockerfile exists; use minimal/non-root base images
Docker Compose: ≥2.20 → use `docker compose` (v2); never `docker-compose` unless locked by project
Ruff: ≥0.5 → `ruff check .`; `ruff check . --fix`; `ruff format .`; no manual formatting
Pytest: ≥7 → `pytest -q`; tests required for core logic changes
pre-commit: ≥3 → `pre-commit install`; `pre-commit run --all-files`; use for lint/format pre-commit
Mermaid: ≥10 → keep `.mmd`; render: `mmdc -i X.mmd -o X.svg`; no manual SVG/diagrams
Node.js: ≥18/20 LTS → for Mermaid/JS tools; use lockfile (package-lock/pnpm-lock)
Airflow: ≥2.7 → use Docker Compose install; follow DAG naming; control XCom size, logging, retry, idempotency
Flutter: ≥3.16 → use `flutter create`; no manual struct
Cookiecutter: 2.6.0 → `uv add --dev cookiecutter==2.6.0`; `uv run cookiecutter <URL>`; for standard project/app boilerplate
Cookiecutter-Django: template repo (e.g. https://github.com/cookiecutter/cookiecutter-django); for production-ready Django; record commit/tag used
Copier: 2.3.1 → `uv add --dev copier==2.3.1`; `copier copy <template> <dest>`; `copier update <dest>`; for internal templates only (not Django-from-scratch)
MkDocs: 1.6.1 → `uv add --dev mkdocs==1.6.1`; `mkdocs new`, `serve`, `build`; no custom doc systems
Material for MkDocs: 9.7.1 → default theme if MkDocs used
drf-spectacular: 0.29.0 → `uv add drf-spectacular`; auto OpenAPI 3; annotate serializers/responses; no manual API docs
drf-spectacular-sidecar: 2025.12.1 → offline Swagger/Redoc; prefer if CDN restricted
pytest-django: 4.11.1 → required for DRF/Django tests
mypy + django-stubs + django-stubs-ext: 1.19.1 + 5.2.8 → only if repo config enables mypy; no new type system
djangorestframework-stubs: 3.16.6 → only if mypy enabled

STANDARD_RUNBOOK:

1. Setup:`uv --version`, `uv sync`, `uv run python --version`, `uv run ruff --version`, `uv run pytest --version`
2. Quality:`uv run ruff format .`, `uv run ruff check .`, `uv run pytest -q`
3. Services:
   `docker compose up -d`, `docker compose ps`, `docker compose logs -f --tail=200 <service>`

FORBIDDEN (MUST NOT):

- Tools outside this list (no approval → halt)
- Manual boilerplate when tool exists
- Untracked/version change (no pin/approval)
- Binary/large files in repo (no approval)
- Code gen without lint/test
- Conflicting frameworks (e.g. DRF + FastAPI)
- Custom doc systems when MkDocs/Mermaid exist
- Non-UTF-8 encoding for Persian data
- `python` direct exec when `uv run` available
