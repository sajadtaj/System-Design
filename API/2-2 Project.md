# طرح کلی پروژه

```
hello-rest/
├─ app/
│  ├─ __init__.py
│  ├─ config.py
│  ├─ logging_conf.py
│  ├─ deps.py
│  ├─ models.py
│  ├─ main.py
│  └─ api/
│     └─ v1/
│        └─ routes.py
├─ tests/
│  ├─ test_health.py
│  └─ test_items.py
├─ .env.example
├─ Dockerfile
├─ docker-compose.yml
├─ Makefile
├─ pyproject.toml
├─ README.md
└─ .gitignore
```

## اهداف پوشش داده‌شده

* نسخه‌بندی API: `/api/v1`
* اصول REST: منابع `/items` با GET/POST/GET{id}/DELETE
* قرارداد و مستندات: OpenAPI خودکار + توضیحات و تگ‌ها
* امنیت ساده: API Key در هدر `X-API-Key` (خوانده از ENV)
* ریت‌لیمیت سبک: in-memory per-IP (برای دمو)
* مشاهده‌پذیری: `/metrics` با Prometheus Instrumentator
* لاگ ساختاریافته: تنظیم logging
* تست: `pytest` + `httpx` (async client)
* کیفیت کد: `ruff`, `black`, `mypy` (در صورت نیاز فعال)
* داکر و Compose + Makefile اجرایی

---

# فایل‌ها (با مشخصات تغییر)

## 1) مسیر: `app/config.py`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: پیکربندی پروژه و متغیرهای محیطی (UTF-8). پایه برای امنیت و پورت.
* بخش‌های وابسته: `deps.py`, `main.py`

```python
# app/config.py
from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_name: str = "hello-rest"
    api_v1_prefix: str = "/api/v1"
    host: str = os.getenv("APP_HOST", "0.0.0.0")
    port: int = int(os.getenv("APP_PORT", "8080"))
    api_key: str = os.getenv("API_KEY", "dev-key")  # برای دمو
    rate_limit_per_minute: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "60"))
    enable_metrics: bool = os.getenv("ENABLE_METRICS", "true").lower() == "true"

settings = Settings()
```

## 2) مسیر: `app/logging_conf.py`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: لاگ ساختاریافته و یکدست.
* وابسته: `main.py`

```python
# app/logging_conf.py
import logging
import sys

def configure_logging() -> None:
    handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )
    handler.setFormatter(fmt)
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.handlers.clear()
    root.addHandler(handler)
```

## 3) مسیر: `app/deps.py`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: وابستگی‌ها (auth, rate limit) را جدا نگه داریم (SOLID).
* وابسته: `routes.py`, `main.py`

```python
# app/deps.py
import time
from fastapi import Header, HTTPException, status, Request
from app.config import settings

# Auth: API Key در هدر
async def api_key_auth(x_api_key: str = Header(default=None)):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")
    return True

# Rate limiting بسیار ساده (in-memory) فقط برای دمو
# کلید: (client_ip, current_minute) -> count
_rate_counters = {}

def _rate_key(ip: str, minute_bucket: int):
    return f"{ip}:{minute_bucket}"

async def rate_limit(request: Request):
    ip = request.client.host if request.client else "unknown"
    minute_bucket = int(time.time() // 60)
    key = _rate_key(ip, minute_bucket)
    current = _rate_counters.get(key, 0) + 1
    _rate_counters[key] = current
    if current > settings.rate_limit_per_minute:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
```

## 4) مسیر: `app/models.py`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: DTOها/اسکیماها جدا؛ تست‌پذیری بهتر.
* وابسته: `routes.py`

```python
# app/models.py
from pydantic import BaseModel, Field
from typing import Optional

class ItemIn(BaseModel):
    name: str = Field(..., min_length=1, max_length=64)
    description: Optional[str] = Field(None, max_length=256)

class ItemOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
```

## 5) مسیر: `app/api/v1/routes.py`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: جداسازی روت‌های نسخه v1؛ الگوی توسعه‌پذیر.
* وابسته: `main.py`, `models.py`, `deps.py`

```python
# app/api/v1/routes.py
from fastapi import APIRouter, Depends, Query, Path, status, HTTPException
from typing import List, Optional
from app.models import ItemIn, ItemOut
from app.deps import api_key_auth, rate_limit

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(api_key_auth), Depends(rate_limit)],
)

# در دمو از in-memory storage استفاده می‌کنیم
_DB = {}
_SEQ = 0

@router.get("/health", tags=["health"], dependencies=[])
async def health():
    return {"status": "ok"}

@router.post("", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
async def create_item(payload: ItemIn) -> ItemOut:
    global _SEQ
    _SEQ += 1
    obj = {"id": _SEQ, "name": payload.name, "description": payload.description}
    _DB[_SEQ] = obj
    return obj  # FastAPI آن را به ItemOut تبدیل می‌کند

@router.get("", response_model=List[ItemOut])
async def list_items(
    q: Optional[str] = Query(None, description="فیلتر بر اساس نام"),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
) -> List[ItemOut]:
    items = list(_DB.values())
    if q:
        items = [it for it in items if q.lower() in it["name"].lower()]
    start = (page - 1) * size
    end = start + size
    return items[start:end]

@router.get("/{item_id}", response_model=ItemOut)
async def get_item(item_id: int = Path(..., ge=1)) -> ItemOut:
    obj = _DB.get(item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int = Path(..., ge=1)):
    if item_id in _DB:
        del _DB[item_id]
        return
    raise HTTPException(status_code=404, detail="Not found")
```

## 6) مسیر: `app/main.py`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: مونتاژ برنامه، متریک‌ها، رویدادهای شروع/خاموش، و متادیتا.
* وابسته: `config.py`, `logging_conf.py`, `routes.py`

```python
# app/main.py
from fastapi import FastAPI
from app.config import settings
from app.logging_conf import configure_logging
from app.api.v1.routes import router as v1_items
import logging

configure_logging()
log = logging.getLogger("hello-rest")

app = FastAPI(
    title="Hello REST",
    description="Hello-world REST API with versioning, auth, rate-limit, and metrics.",
    version="1.0.0",
    openapi_tags=[
        {"name": "items", "description": "عملیات CRUD ساده روی اقلام"},
        {"name": "health", "description": "سلامت سرویس"},
    ],
)

# متریک‌ها
if settings.enable_metrics:
    try:
        from prometheus_fastapi_instrumentator import Instrumentator
        Instrumentator().instrument(app).expose(app, include_in_schema=False)
        log.info("metrics enabled on /metrics")
    except Exception as e:
        log.warning("metrics disabled: %s", e)

# مسیرهای نسخه‌دار
app.include_router(v1_items, prefix=settings.api_v1_prefix)

@app.on_event("startup")
async def on_startup():
    log.info("app starting: %s", settings.app_name)

@app.on_event("shutdown")
async def on_shutdown():
    log.info("app shutting down")
```

## 7) مسیر: `tests/test_health.py`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: اطمینان از سلامت endpoint.
* وابسته: `main.py`

```python
# tests/test_health.py
import pytest
from httpx import AsyncClient
from app.main import app
from app.config import settings

@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get(f"{settings.api_v1_prefix}/items/health")
        assert resp.status_code == 200
        assert resp.json() == {"status": "ok"}
```

## 8) مسیر: `tests/test_items.py`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: Happy pathهای اصلی CRUD + Auth + Pagination.
* وابسته: `main.py`, `config.py`

```python
# tests/test_items.py
import pytest
from httpx import AsyncClient
from app.main import app
from app.config import settings

HEADERS = {"X-API-Key": settings.api_key}

@pytest.mark.asyncio
async def test_crud_and_list():
    async with AsyncClient(app=app, base_url="http://test", headers=HEADERS) as ac:
        # ایجاد
        r = await ac.post(f"{settings.api_v1_prefix}/items", json={"name": "alpha"})
        assert r.status_code == 201
        item = r.json()
        assert item["id"] >= 1

        # دریافت
        r = await ac.get(f"{settings.api_v1_prefix}/items/{item['id']}")
        assert r.status_code == 200
        assert r.json()["name"] == "alpha"

        # فهرست با pagination
        r = await ac.get(f"{settings.api_v1_prefix}/items?page=1&size=10")
        assert r.status_code == 200
        assert isinstance(r.json(), list)

        # حذف
        r = await ac.delete(f"{settings.api_v1_prefix}/items/{item['id']}")
        assert r.status_code == 204

@pytest.mark.asyncio
async def test_auth_required():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get(f"{settings.api_v1_prefix}/items")
        assert r.status_code == 401
```

## 9) مسیر: `.env.example`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: پیکربندی نمونه، UTF-8.
* وابسته: `config.py`

```dotenv
# UTF-8
APP_HOST=0.0.0.0
APP_PORT=8080
API_KEY=dev-key
RATE_LIMIT_PER_MINUTE=60
ENABLE_METRICS=true
```

## 10) مسیر: `pyproject.toml`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: مدیریت وابستگی‌ها و ابزارها.
* وابسته: همه

```toml
[project]
name = "hello-rest"
version = "0.1.0"
description = "Hello-world REST API (FastAPI) with auth, rate-limit, metrics, tests"
requires-python = ">=3.10"
dependencies = [
  "fastapi>=0.115.0",
  "uvicorn[standard]>=0.30.0",
  "pydantic>=2.7.0",
  "prometheus-fastapi-instrumentator>=6.1.0",
  "python-dotenv>=1.0.1"
]

[project.optional-dependencies]
dev = [
  "pytest>=8.0.0",
  "pytest-asyncio>=0.23.0",
  "httpx>=0.27.0",
  "ruff>=0.6.0",
  "black>=24.0.0",
  "mypy>=1.10.0",
  "types-requests"
]

[tool.pytest.ini_options]
asyncio_mode = "auto"

[tool.black]
line-length = 100
target-version = ["py310", "py311", "py312"]

[tool.ruff]
line-length = 100
select = ["E","F","I","UP"]
```

## 11) مسیر: `Makefile`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: توسعه و CI محلی را ساده کند.
* وابسته: `pyproject.toml`, `Dockerfile`

```makefile
.PHONY: venv install run test lint fmt type docker-build up down openapi

venv:
	python -m venv .venv

install:
	. .venv/bin/activate && pip install -U pip && pip install -e .[dev]

run:
	. .venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

test:
	. .venv/bin/activate && pytest -q

lint:
	. .venv/bin/activate && ruff check .

fmt:
	. .venv/bin/activate && black .

type:
	. .venv/bin/activate && mypy app

docker-build:
	docker build -t hello-rest:latest .

up:
	docker compose up -d

down:
	docker compose down

openapi:
	curl -s http://localhost:8080/openapi.json | jq .
```

## 12) مسیر: `Dockerfile`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: اجرای کانتینری و انتشار ساده.
* وابسته: `pyproject.toml`, `app/*`

```dockerfile
# syntax=docker/dockerfile:1.6
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app
COPY pyproject.toml /app/
RUN pip install --upgrade pip && pip install ".[dev]" --no-cache-dir || true

COPY app /app/app
COPY .env.example /app/.env

EXPOSE 8080
CMD ["python", "-m", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080"]
```

## 13) مسیر: `docker-compose.yml`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: اجرای ساده لوکال + پیکربندی ENV.
* وابسته: `Dockerfile`

```yaml
version: "3.9"
services:
  api:
    build: .
    image: hello-rest:latest
    container_name: hello-rest
    environment:
      - APP_HOST=0.0.0.0
      - APP_PORT=8080
      - API_KEY=dev-key
      - RATE_LIMIT_PER_MINUTE=60
      - ENABLE_METRICS=true
    ports:
      - "8080:8080"
```

## 14) مسیر: `README.md`

* نوع تغییر: ایجاد فایل (Full file)
* چرا: مستند کوتاه و قابل اجرا.

````markdown
# Hello REST (FastAPI)

## Run (local)
```bash
make venv install
make run
````

Verify:

* OpenAPI UI: [http://localhost:8080/docs](http://localhost:8080/docs)
* Health: `curl -i http://localhost:8080/api/v1/items/health`

## Auth

Send header: `X-API-Key: dev-key`

## Examples

Create:

```bash
curl -s -X POST "http://localhost:8080/api/v1/items" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-key" \
  -d '{"name":"alpha","description":"اولین"}'
```

Verify: HTTP 201 + JSON with id

List:

```bash
curl -s -H "X-API-Key: dev-key" "http://localhost:8080/api/v1/items?page=1&size=5"
```

Get:

```bash
curl -s -H "X-API-Key: dev-key" "http://localhost:8080/api/v1/items/1"
```

Delete:

```bash
curl -i -X DELETE -H "X-API-Key: dev-key" "http://localhost:8080/api/v1/items/1"
```

## Metrics

`/metrics` (Prometheus exposition) if enabled.

````

## 15) مسیر: `.gitignore`
- نوع تغییر: ایجاد فایل (Full file)
- چرا: پاکیزگی ریپو.

```gitignore
.venv/
__pycache__/
*.pyc
dist/
*.egg-info/
.env
````

---

# دستور اجرا و تست

## اجرای لوکال

```bash
make venv install
make run
```

Verify:

* مرورگر: `http://localhost:8080/docs` (Swagger UI)
* OpenAPI JSON:

```bash
curl -s http://localhost:8080/openapi.json | jq '.info.title'
# انتظار: "Hello REST"
```

## تست‌ها

```bash
make test
```

Verify:

* انتظار: تمام تست‌ها سبز.

## اجرای داکر

```bash
make docker-build
make up
```

Verify:

```bash
curl -i http://localhost:8080/api/v1/items/health
# 200 OK و {"status":"ok"}
```

## نمونه درخواست‌ها (با احراز هویت هدر)

```bash
curl -s -X POST "http://localhost:8080/api/v1/items" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-key" \
  -d '{"name":"alpha"}' | jq
```

Verify:

* انتظار: `id` عددی و `name` برابر "alpha".

---

# نکات طراحی و پوشش الزامات

* نسخه‌بندی: همه‌ی مسیرها تحت `/api/v1` هستند (آماده برای `/api/v2`).
* REST تمیز: منابع (`/items`) با متدهای استاندارد؛ جستجو با `q` و pagination (`page`, `size`).
* امنیت پایه: API Key در هدر (برای دمو). در تولید بجای آن OAuth2/JWT پیشنهاد می‌شود.
* ریت‌لیمیت: ساده و in-memory (برای دمو). در تولید: Gateway (مثل Kong) یا Redis-based.
* مشاهده‌پذیری: `/metrics` برای Prometheus؛ بعداً می‌توان Grafana اضافه کرد.
* لاگ: ساختاریافته و یکدست؛ آماده‌ی جمع‌آوری توسط Fluent Bit/Vector.
* تست: `pytest` + `httpx`؛ پوشش happy-path و auth.
* مستندسازی: به‌صورت خودکار توسط FastAPI (OpenAPI/Swagger).
* UTF-8: همه فایل‌ها و `.env.example` بر این مبنا.

---

# ریسک‌ها و بهبودهای بعدی (صریح)

* ذخیره‌سازی فعلی in-memory است (صرفاً دمو). برای تولید باید یک لایه persistence (PostgreSQL) و لایه ریپازیتوری اضافه شود.
* ریت‌لیمیت in-memory در چند replica کارا نیست؛ باید به Gateway یا Redis منتقل شود.
* Auth واقعی (OAuth2/JWT) و مجوزها (RBAC/ABAC) لازم است.
* تست‌های خطا، تست‌های بار (Locust/k6)، و تست قرارداد (با OpenAPI schema) اضافه شوند.
* CI (GitHub Actions) و SAST (ruff/mypy) در pipeline ادغام شود.

---

# پیشنهاد ادغام با استک فعلی تو

* اگر خواستی با **Nginx** یا **Kong** جلو بگذاریم: مسیر `/api/` را پروکسی کنیم، TLS/RateLimit/Auth را به Gateway بسپاریم، لاگ‌ها را به OTEL/ELK وصل کنیم.
* برای **PostgreSQL**: ماژول `repository.py` و migration با Alembic اضافه می‌کنیم؛ DTO ↔️ ORM (SQLModel/SQLAlchemy).
* برای **Airflow**: اگر نیاز به orchestration داشتی، Endpoints خاصی می‌توانند با DAGها تعامل کنند (idempotent و امن).

---

