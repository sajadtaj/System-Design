# AGENTS.tools.md

# Purpose: Tooling Contract for Agents (Python-first Stack)
# Language: Persian (UTF-8)

# Rule:
Agent MUST treat this document as the single source of truth for:
- انتخاب ابزار
- ساخت Boilerplate
- اجرای فریم‌ورک‌ها
- نصب و اجرای dependencyها

Agent MUST prefer the tools listed here over any hand-made structure, code, or inferred framework behavior.

---

## 0) قوانین سخت‌گیرانه و یکپارچگی (Agent MUST)

### 0.1) اصل عدم بداهه‌سازی (No Improvisation)
1) Agent حق ندارد برای مواردی که **ابزار رسمی یا Template استاندارد وجود دارد**:
   - فریم‌ورک
   - ساختار پروژه
   - اپلیکیشن
   - دیاگرام
   - مستندات
   به‌صورت دستی فولدر، فایل یا Boilerplate تولید کند.

   این شامل (ولی محدود به) موارد زیر است:
   - Django / DRF
   - Cookiecutter / Copier
   - Flutter
   - Airflow
   - Docker / Docker Compose
   - Mermaid / MkDocs

2) تنها استثنا:
   - ابزار رسمی پاسخگوی نیاز نباشد، یا
   - تغییر صرفاً یک **Customization کوچک و مشخص** روی خروجی Boilerplate باشد  
   (در این حالت Agent MUST دلیل را شفاف گزارش کند).

---

### 0.2) اصل عدم تعارض ابزارها (No Tool / Framework Conflict)
3) Agent MUST از ابزارهایی استفاده کند که **با استک اصلی پروژه سازگار و غیررقیب هستند**.

   مثال‌های ممنوع (نمونه):
   - وجود Django ⇒ استفاده از Flask یا FastAPI ممنوع
   - وجود DRF ⇒ معرفی یا استفاده از API framework جایگزین ممنوع
   - وجود uv ⇒ استفاده از pip/venv به‌صورت موازی ممنوع
   - وجود MkDocs ⇒ ساخت سیستم مستندسازی موازی ممنوع

4) Agent حق معرفی یا استفاده از ابزار جدیدی که:
   - نقش تکراری دارد
   - یا با ابزار موجود هم‌پوشانی مفهومی دارد  
   را **بدون تایید صریح** ندارد.

---

### 0.3) اصل یکپارچگی معماری (Architectural Integrity)
5) Agent MUST:
   - ساختار پروژه
   - انتخاب ابزار
   - روش اجرا
   - و نحوه scaffold  
   را **منطبق با معماری موجود پروژه** نگه دارد.

6) Agent نباید:
   - معماری جدید پیشنهاد کند
   - یا ابزار جدید وارد کند
   مگر این‌که:
   - اثر آن بر Backend، DB، DevOps، Data Engineering مشخص شده باشد
   - مزایا / ریسک‌ها شفاف اعلام شود
   - و تایید گرفته شود

---

### 0.4) نسخه، تکرارپذیری و لاگ
7) قبل از اجرای هر دستور، Agent MUST:
   - نسخه ابزار را چاپ و ثبت کند
   - از مسیر اجرای دستور مطمئن باشد

8) این فایل فقط **نسخه مرجع/حداقل** را مشخص می‌کند.
   - پین نسخه واقعی MUST در یکی از موارد زیر انجام شود:
     - `pyproject.toml`
     - `requirements*.txt`
     - `package.json`
     - `Dockerfile`
     - lockfileها

---

### 0.5) Encoding و داده
9) Agent MUST از UTF-8 در تمام موارد زیر استفاده کند:
   - فایل‌های متنی
   - کد
   - مستندات
   - داده‌های فارسی در DB و UI

---

### 0.6) حدود اختیار Agent
10) Agent MUST فقط از دستورالعمل‌های همین فایل برای:
    - نصب ابزار
    - اجرای ابزار
    - Scaffold
    - Format / Lint / Test
    استفاده کند.

11) حدس، تقلید از پروژه‌های دیگر، یا مسیرسازی دستی **ممنوع** است.

---

## 1) ماتریس ابزارها (قابل اجرا توسط Agent)

> نکات نسخه‌ها:
>
> - این فایل نسخه مرجع / پایدار ابزارها را مشخص می‌کند.
> - Agent MUST نسخه واقعی اجراشده را با دستور Version Check ثبت کند.
> - هر تغییر نسخه یا dependency نیازمند تایید است.

---

### 1.1) Python

- Name: Python
- Version (Minimum): 3.11
- Usage: Runtime اصلی بک‌اند، اسکریپت‌ها، ETL
- Install (Linux): از repo رسمی سیستم یا pyenv (ترجیح تیم را در پروژه مشخص کنید)
- Version Check:
  - `python --version`
- Agent Instructions:
  - اجرای اسکریپت‌ها فقط با `uv run ...` (اگر uv فعال است) انجام شود.
  - اجرای مستقیم `python` فقط وقتی مجاز است که uv در محیط موجود نباشد.

---

### 1.2) uv (Python package manager / runner)

- Name: uv
- Version (Minimum): 0.4.x
- Usage:
  - ساخت venv، نصب dependency، اجرای ابزارها بدون فعال‌سازی دستی venv
  - جایگزین سریع‌تر pip/venv در بسیاری از سناریوها
- Install:
  - طبق مستند رسمی uv (روش سازمان شما): معمولاً یکی از این‌ها:
    - `curl -LsSf https://astral.sh/uv/install.sh | sh`
    - یا نصب از package manager سیستم
- Version Check:
  - `uv --version`
- Agent Instructions (MUST):
  - نصب:
    - `uv sync` (اگر پروژه lock دارد)
    - یا `uv pip install -r requirements.txt` (اگر requirements دارید)
  - اجرا:
    - `uv run python -m ...`
    - `uv run pytest`
    - `uv run ruff check .`
  - Agent نباید dependency جدید اضافه کند مگر با تایید، و باید در lockfile ثبت شود.

---

### 1.3) Django

- Name: Django
- Version (Minimum): 4.2 (LTS)
- Usage:
  - وب‌اپ/بک‌اند، ORM، migrations، admin
- Install:
  - داخل پروژه:
    - `uv add django==<PINNED_VERSION>`
    - یا در `pyproject.toml` پین شود
- Version Check:
  - `uv run python -c "import django; print(django.get_version())"`
- Agent Instructions (MUST):
  - ایجاد پروژه/اپ فقط با دستورات Django:
    - `uv run django-admin startproject <name> .`
    - `uv run python manage.py startapp <appname>`
  - migrations:
    - `uv run python manage.py makemigrations`
    - `uv run python manage.py migrate`
  - اجرای dev server:
    - `uv run python manage.py runserver 0.0.0.0:8000`
  - Agent حق ندارد ساختار پروژه را دستی ایجاد کند اگر startproject/startapp قابل استفاده است.

---

### 1.4) Django REST Framework (اگر API دارید)

- Name: djangorestframework
- Version (Minimum): 3.14+
- Usage: ساخت APIهای REST، serializer/viewset/router
- Install:
  - `uv add djangorestframework==<PINNED_VERSION>`
- Version Check:
  - `uv run python -c "import rest_framework; print(rest_framework.__version__)"`
- Agent Instructions:
  - ساخت endpointها با الگوهای DRF (ViewSet/Router) و تست API (pytest یا Django test).
  - Agent نباید endpoint خام و ناسازگار با ساختار فعلی پروژه بسازد.

---

### 1.5) PostgreSQL (DB)

- Name: PostgreSQL
- Version (Minimum): 14+
- Usage: DB اصلی (ACID)، migrations، query optimization
- Install:
  - معمولاً با Docker image یا نصب سیستم
- Version Check:
  - داخل کانتینر: `psql --version`
- Agent Instructions (MUST):
  - هر تغییری در schema باید با migration مدیریت شود.
  - برای داده فارسی: encoding پایگاه داده باید UTF-8 باشد و collation مناسب تعریف شود.
  - Agent باید برای تغییرات سنگین، ریسک performance (index، query plan) را توضیح دهد.

---

### 1.6) Docker

- Name: Docker Engine
- Version (Minimum): 24+
- Usage: کانتینرسازی سرویس‌ها
- Install: طبق مستند رسمی Docker برای OS
- Version Check:
  - `docker --version`
- Agent Instructions:
  - Agent نباید سرویس‌ها را روی سیستم «خام» نصب کند اگر Dockerfile/Compose وجود دارد.
  - هر تغییر در image باید با cache و امنیت (non-root, minimal base) سنجیده شود.

---

### 1.7) Docker Compose

- Name: Docker Compose (v2)
- Version (Minimum): 2.20+
- Usage: اجرای چند سرویس (Postgres, Redis, Django, Airflow, etc.)
- Version Check:
  - `docker compose version`
- Agent Instructions (MUST):
  - بالا آوردن محیط:
    - `docker compose up -d`
  - مشاهده لاگ:
    - `docker compose logs -f --tail=200 <service>`
  - Agent نباید دستورهای قدیمی `docker-compose` را پیشنهاد دهد مگر اینکه پروژه همین را قفل کرده باشد.

---

### 1.8) Ruff (Lint/Format)

- Name: ruff
- Version (Minimum): 0.5+
- Usage: lint + formatter سریع برای Python
- Install:
  - `uv add --dev ruff==<PINNED_VERSION>`
- Version Check:
  - `uv run ruff --version`
- Agent Instructions (MUST):
  - lint:
    - `uv run ruff check .`
  - autofix (در صورت مجاز بودن):
    - `uv run ruff check . --fix`
  - format:
    - `uv run ruff format .`
  - Agent نباید فرمتینگ دستی انجام دهد وقتی formatter موجود است.

---

### 1.9) Pytest (Tests)

- Name: pytest
- Version (Minimum): 7+
- Usage: تست واحد/یکپارچه
- Install:
  - `uv add --dev pytest==<PINNED_VERSION>`
- Version Check:
  - `uv run pytest --version`
- Agent Instructions:
  - هر تغییر در منطق حساس باید تست اضافه/به‌روزرسانی داشته باشد.
  - اجرای تست‌ها:
    - `uv run pytest -q`

---

### 1.10) pre-commit (Quality Gate)

- Name: pre-commit
- Version (Minimum): 3+
- Usage: اجرای خودکار lint/format قبل از commit
- Install:
  - `uv add --dev pre-commit==<PINNED_VERSION>`
- Version Check:
  - `uv run pre-commit --version`
- Agent Instructions:
  - نصب hooks:
    - `uv run pre-commit install`
  - اجرا:
    - `uv run pre-commit run --all-files`

---

### 1.11) Mermaid (Docs Diagrams)

- Name: Mermaid
- Version (Minimum): CLI 10+
- Usage: تولید دیاگرام از متن (C4، sequence، flow)
- Install:
  - Node.js لازم است
  - `npm i -g @mermaid-js/mermaid-cli`
- Version Check:
  - `mmdc --version`
- Agent Instructions (MUST):
  - Agent باید دیاگرام‌ها را در `.mmd` نگه دارد و خروجی تصویر را در مسیر مستندات تولید کند.
  - Agent نباید تصویر را دستی بکشد یا SVG خام بسازد وقتی mermaid-cli قابل استفاده است.
  - نمونه تولید:
    - `mmdc -i diagram.mmd -o diagram.svg`

---

### 1.12) Node.js (برای Mermaid CLI و ابزارهای فرانت/Docs)

- Name: Node.js
- Version (Minimum): 18 LTS یا 20 LTS
- Usage: اجرای ابزارهای JS مثل mermaid-cli
- Install: nvm یا بسته رسمی OS
- Version Check:
  - `node --version`
  - `npm --version`
- Agent Instructions:
  - برای وابستگی‌های JS، ترجیحاً از lockfile استفاده شود (package-lock / pnpm-lock).

---

### 1.13) Airflow (اگر در پروژه دارید)

- Name: Apache Airflow
- Version (Minimum): 2.7+
- Usage: ارکستریشن DAG، زمان‌بندی ETL/استراتژی‌ها
- Install:
  - ترجیحاً با Docker Compose (نه نصب خام روی OS)
- Version Check:
  - داخل کانتینر: `airflow version`
- Agent Instructions:
  - DAG جدید باید با الگوی پروژه و naming convention همخوان باشد.
  - Agent باید logging، retry policy، idempotency، و XCom حجم بالا را کنترل کند.

---

### 1.14) Flutter (اگر موبایل دارید)

- Name: Flutter SDK
- Version (Minimum): 3.16+
- Usage: اپ موبایل
- Install: طبق مستند رسمی Flutter
- Version Check:
  - `flutter --version`
- Agent Instructions:
  - ساخت پروژه/feature با CLI رسمی Flutter.
  - Agent نباید ساختار دستی بسازد وقتی `flutter create` قابل استفاده است.

---

### 1.15) Cookiecutter (Project Scaffolding)
- Name: cookiecutter
- Version (Stable): 2.6.0
- Usage:
  - ساخت سریع اسکلت پروژه/اپ از روی Template استاندارد
  - جلوگیری از “دست‌ساز” کردن ساختارها توسط Agent
- Install:
  - `uv add --dev cookiecutter==2.6.0`
- Version Check:
  - `uv run cookiecutter --version`
- Agent Instructions (MUST):
  - برای ساخت boilerplate های استاندارد، اولویت با Cookiecutter است نه ایجاد دستی پوشه/فایل.
  - ساخت پروژه از Template:
    - `uv run cookiecutter <TEMPLATE_GIT_URL_OR_PATH>`
  - Agent باید خروجی را فقط در مسیرهای مجاز ریپو تولید کند و فایل‌های تولیدشده را بی‌دلیل بازنویسی نکند.

---

### 1.16) Cookiecutter Django (Production-ready Django Boilerplate)
- Name: cookiecutter-django (template, not a Python library)
- Version (Stable): بر اساس ریلیزهای رسمی پروژه (template repo)
- Usage:
  - ساخت پروژه Django تولیدی (production-ready) با ساختار استاندارد و best-practice های رایج
  - مناسب وقتی می‌خواهی از صفر یک ریپو/سرویس Django بسازی
- Install:
  - نیاز به نصب جداگانه ندارد؛ با Cookiecutter اجرا می‌شود.
- Version Check:
  - Agent باید commit/tag استفاده‌شده از repo را ثبت کند (برای reproducibility).
- Agent Instructions (MUST):
  - وقتی هدف “ساخت پروژه Django از صفر” است، Agent باید اول از این Template استفاده کند؛
    سپس فقط customization های لازم را اعمال کند.
  - دستور نمونه:
    - `uv run cookiecutter https://github.com/cookiecutter/cookiecutter-django`
  - Agent باید خروجی را در مسیر روت سرویس موردنظر تولید کند و سپس تنظیمات پروژه شما (Docker Compose، envها، نام سرویس‌ها) را با پروژه فعلی هم‌راستا کند.

---

### 1.17) Copier (Template Engine for Internal/Reusable Scaffolds)
- Name: copier
- Version (Stable): 2.3.1  (اگر در پروژه شما نیاز به نسخه بالاتر بود، باید پین شود)
- Usage:
  - ساخت Templateهای داخلی تیم/سازمان (مثلاً قالب استاندارد برای هر microservice Django، هر app، هر library)
  - قابلیت update کردن پروژه‌های ساخته‌شده از template (برای Agent خیلی مهم است)
- Install:
  - `uv add --dev copier==2.3.1`
- Version Check:
  - `uv run copier --version`
- Agent Instructions (MUST):
  - برای قالب‌های داخلی سازمان، Copier ترجیح دارد چون قابلیت update دارد.
  - ساخت از template:
    - `uv run copier copy <TEMPLATE_GIT_URL_OR_PATH> <DEST_DIR>`
  - آپدیت پروژه‌ای که قبلاً از template ساخته شده:
    - `uv run copier update <DEST_DIR>`
  - Agent نباید template جدید اختراع کند؛ اگر نیاز شد، اول template داخلی را توسعه بدهد (با تایید).

استناد نسخه:

نکته سخت‌گیرانه برای جلوگیری از آشفتگی:
اگر Cookiecutter Django را برای ساخت سرویس‌های جدید انتخاب می‌کنی، Copier را فقط برای templateهای داخلی تیم نگه دار (نه برای ساخت Django از صفر). این یعنی تداخل عملیاتی هم نداری.

---

### 1.18) MkDocs (Project Documentation Site)
- Name: mkdocs
- Version (Stable): 1.6.1
- Usage:
  - تبدیل مستندات Markdown به سایت مستندات قابل جستجو (برای پروژه‌های چند سرویس خیلی مفید است)
- Install:
  - `uv add --dev mkdocs==1.6.1`
- Version Check:
  - `uv run mkdocs --version`
- Agent Instructions (MUST):
  - Agent نباید سیستم مستندسازی جدید اختراع کند.
  - ساخت سایت docs:
    - `uv run mkdocs new docs-site`
  - اجرای لوکال:
    - `uv run mkdocs serve -a 0.0.0.0:8008`
  - ساخت خروجی:
    - `uv run mkdocs build`

---

### 1.19) Material for MkDocs (Theme)
- Name: mkdocs-material
- Version (Stable): 9.7.1
- Usage:
  - قالب حرفه‌ای و استاندارد برای MkDocs (خوانایی و ناوبری بهتر)
- Install:
  - `uv add --dev mkdocs-material==9.7.1`
- Version Check:
  - `uv run python -c "import mkdocs_material; print('ok')"`  (یا بررسی از lockfile)
- Agent Instructions (MUST):
  - اگر MkDocs استفاده شد، Theme پیش‌فرض باید mkdocs-material باشد مگر خلافش تایید شود.

---


---

###  افزودن ابزارهای استاندارد “API Contract/Schema” برای سرعت و دقت Agent (ویژه DRF)

این‌ها تداخل با DRF ندارند؛ برعکس، جلوی “حدس‌سازی” Agent برای API docs و client generation را می‌گیرند.

### 1.20) drf-spectacular (OpenAPI 3 for DRF)
- Name: drf-spectacular
- Version (Stable): 0.29.0
- Usage:
  - تولید خودکار OpenAPI 3 از کد DRF (Schema/Docs/Contract)
  - کاهش خطا در مستندسازی و هماهنگی فرانت/موبایل
- Install:
  - `uv add drf-spectacular==0.29.0`
- Version Check:
  - `uv run python -c "import drf_spectacular; print(drf_spectacular.__version__)"`
- Agent Instructions (MUST):
  - هر API جدید باید در Schema قابل مشاهده باشد (Serializer/Responseها درست annotate شوند).
  - Agent حق ندارد API doc دستی جدا از کد بنویسد وقتی schema generator داریم.

---

### 1.21) drf-spectacular-sidecar (Swagger/Redoc Static Assets)
- Name: drf-spectacular-sidecar
- Version (Stable): 2025.12.1
- Usage:
  - سرو کردن UIهای Swagger/Redoc بدون وابستگی به CDN (مناسب محیط‌های محدود)
- Install:
  - `uv add drf-spectacular-sidecar==2025.12.1`
- Version Check:
  - `uv run python -c "import drf_spectacular_sidecar; print('ok')"`
- Agent Instructions:
  - اگر محدودیت شبکه/سیاست امنیتی داری، sidecar ترجیح دارد.

---

---

###  افزودن ابزارهای افزایش سرعت Agent در تغییرات Django (تست/تایپ چکینگ) — بدون کانفلیکت

### 1.22) pytest-django (Django Testing with pytest)
- Name: pytest-django
- Version (Stable): 4.11.1
- Usage:
  - تست سریع‌تر و استانداردتر Django/DRF با pytest
- Install:
  - `uv add --dev pytest-django==4.11.1`
- Version Check:
  - `uv run pytest --version`
- Agent Instructions (MUST):
  - هر تغییر API/Business Rule باید حداقل یک تست مرتبط داشته باشد.

---

### 1.23) mypy + django-stubs + django-stubs-ext (Static Typing for Django)
- Name: mypy
- Version (Stable): 1.19.1
- Name: django-stubs
- Version (Stable): 5.2.8
- Name: django-stubs-ext
- Version (Stable): 5.2.8
- Usage:
  - کاهش خطای رگرسیونی با تایپ‌چک در پروژه Django
  - کمک مستقیم به Agent برای refactor امن
- Install:
  - `uv add --dev mypy==1.19.1 django-stubs==5.2.8 django-stubs-ext==5.2.8`
- Version Check:
  - `uv run mypy --version`
- Agent Instructions (MUST):
  - Agent فقط وقتی تایپ‌چک را پیشنهاد می‌دهد که تنظیمات mypy در repo مشخص باشد.
  - Agent نباید type system جدید تعریف کند؛ فقط مطابق config موجود پروژه.

---

### 1.24) djangorestframework-stubs (Typing for DRF)
- Name: djangorestframework-stubs
- Version (Stable): 3.16.6
- Usage:
  - تکمیل تایپ‌های DRF برای mypy (Refactor امن‌تر)
- Install:
  - `uv add --dev djangorestframework-stubs==3.16.6`
- Version Check:
  - `uv run python -c "import rest_framework_stubs; print('ok')"`  (یا بررسی از lockfile)
- Agent Instructions:
  - فقط در صورتی فعال شود که تیم تصمیم گرفته mypy را وارد CI کند.

---


## 2) دستورالعمل اجرای استاندارد (Runbook کوتاه برای Agent)

### 2.1) نصب/آماده‌سازی پروژه (Python + uv)

1) `uv --version`
2) `uv sync`  (اگر lockfile دارید)
3) `uv run python --version`
4) `uv run ruff --version`
5) `uv run pytest --version`

### 2.2) کیفیت کد

- `uv run ruff format .`
- `uv run ruff check .`
- `uv run pytest -q`

### 2.3) اجرای سرویس‌ها با Docker Compose

- `docker compose up -d`
- `docker compose ps`
- `docker compose logs -f --tail=200 <service>`

---

## 3) ممنوعیت‌ها (Agent MUST NOT)

- نصب/استفاده از ابزارهای خارج از این لیست بدون تایید
- ساخت دستی Boilerplate وقتی ابزار رسمی موجود است
- تغییر نسخه‌ها بدون ثبت و تایید
- نوشتن فایل‌های باینری یا بزرگ داخل ریپو مگر با تایید
- تولید کد بدون اجرای حداقل یک lint/test مرتبط

---

## 4) TODO برای تیم (اختیاری)

- پین دقیق نسخه‌ها:
  - Python / Django / DRF / Airflow / Ruff / Pytest / Node / Mermaid
- اضافه کردن مسیرهای دقیق پروژه (مثلاً Src/, ExcDoc/, etc.) و قوانین ممنوعیت در همین فایل
