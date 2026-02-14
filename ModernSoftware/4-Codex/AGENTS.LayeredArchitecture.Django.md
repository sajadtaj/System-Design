# AGENTS.LayeredArchitecture.Django.md

# Purpose: Django/DRF Layered Architecture Contract for Agents (Scalable + Maintainable)

# Language: Persian (UTF-8)

## 0) Scope و پیش‌فرض‌ها

این سند برای سرویس‌های Python که با Django + Django REST Framework (DRF) پیاده‌سازی می‌شوند و نقش Backend/API یا Engine-backed API دارند معتبر است.
این سند مکمل `AGENTS.tools.md` است و Agent MUST از ابزارها و الگوهای آن پیروی کند.

---

## 1) مدل لایه‌ها در Django/DRF (Mapping استاندارد)

### 1.1) لایه Interface (Presentation / API)

**هدف:** دریافت/اعتبارسنجی ورودی، احراز هویت اولیه، اعمال مجوزها، تبدیل به Command/DTO، و بازگرداندن Response.
**مصادیق (در Django/DRF):**

- `urls.py` (route definitions)
- `views.py` / `viewsets.py` / `api_views.py`
- `serializers.py` (فقط serialization/validation سطح API)
- `permissions.py` / `throttles.py` (اگر سطح API)
- `schema.py` (OpenAPI annotations)

**قانون سخت:** Interface MUST NOT شامل منطق دامنه (Business Rules) یا Queryهای پیچیده DB باشد.

### 1.2) لایه Application (UseCase / Service / Orchestration)

**هدف:** orchestration، مرز تراکنش، مدیریت خطاها، سیاست‌ها، و هماهنگی بین domain و persistence.
**مصادیق پیشنهادی:**

- `app_services/` یا `usecases/` یا `services/`
- کلاس/تابع‌های UseCase مثل: `CreateOrder`, `TransferFunds`, `GenerateSignal`

**قانون سخت:** Transaction boundary MUST فقط اینجا تعریف شود.

### 1.3) لایه Domain (Business / Core)

**هدف:** قوانین، محاسبات، invariants، مدل‌های دامنه (نه الزاماً ORM).
**مصادیق پیشنهادی:**

- `domain/` شامل entities/value objects/policies
- `domain/services/` برای rules محض

**قانون سخت:** Domain MUST NOT به Django/DRF/ORM/HTTP/Settings وابسته باشد.

### 1.4) لایه Infrastructure (Persistence + Integrations)

**هدف:** دیتابیس، ORM queries کنترل‌شده، repositoryها، ارتباط با سرویس‌های خارجی، cache، queue.
**مصادیق:**

- `repositories/`
- `infra/db/`
- `clients/` (HTTP/Kafka/...)
- `adapters/` (map کردن domain ↔ ORM)

**قانون سخت:** Infrastructure MUST NOT تصمیم بیزینسی بگیرد (فقط IO و mapping).

### 1.5) لایه Database

- migrations (`migrations/`)
- schema decisions (index/constraints)
- DB encoding/collation (UTF-8 برای داده فارسی)

---

## 2) ماتریس ممنوعیت وابستگی (MUST / MUST NOT)

### 2.1) قوانین Import/Call

1) Domain MUST NOT import از:

   - Django
   - DRF
   - ORM Models
   - settings
   - clients/repositories
2) Interface MUST NOT:

   - مستقیم repository/ORM query سنگین اجرا کند
   - مستقیم transaction مدیریت کند
   - منطق دامنه را در Serializer/View پیاده کند
3) Application MAY:

   - Domain را import کند
   - Repository Interfaceها یا abstraction را صدا بزند
   - transaction boundary را اعمال کند
4) Infrastructure MAY:

   - Domain types را import کند (برای mapping)
   - ولی MUST NOT business rule ایجاد کند

### 2.2) Anti-patternهای ممنوع

- God App (یک app همه‌چیز را بلعیده)
- Fat View / Fat Serializer
- Direct DB access از View/Serializer
- Circular imports بین apps
- Shared “utils” بی‌قاعده که تبدیل به dumping ground شود

---

## 3) استاندارد API: Lifecycle + Versioning + Deprecation

### 3.1) API Lifecycle (حداقل الزامات)

Agent MUST برای هر endpoint جدید:

1) Contract را مشخص کند (request/response schema).
2) Error format و status codes را ثابت نگه دارد.
3) Changelog و deprecation policy را رعایت کند (برای breaking change نسخه جدید لازم است).

### 3.2) Versioning (DRF)

DRF چند scheme برای versioning دارد و نسخه از URL یا Header تعیین می‌شود. :contentReference[oaicite:0]{index=0}

**Policy پیشنهادی (پایدار و قابل مشاهده):**

- مسیرها MUST شامل نسخه باشند: `/api/v1/...`
- تغییرات Breaking MUST در نسخه جدید انجام شود (v2).
- Non-breaking تغییرات (افزودن فیلد optional) می‌تواند داخل همان نسخه انجام شود.

**قانون سخت:**

- Agent MUST یک scheme واحد انتخاب کند و در کل سرویس ثابت نگه دارد (ترکیب چند scheme ممنوع مگر با تایید).

---

## 4) AuthN/AuthZ/Token (Django + DRF)

### 4.1) ترتیب اجرای DRF

در DRF، احراز هویت در ابتدای پردازش view انجام می‌شود، قبل از permission و throttling. :contentReference[oaicite:1]{index=1}
Permissions همراه با authentication و throttling تعیین می‌کنند دسترسی مجاز است یا نه. :contentReference[oaicite:2]{index=2}

### 4.2) سیاست‌های الزامی

1) Authentication MUST یکپارچه و مرکزی تعریف شود (settings/REST_FRAMEWORK).
2) Authorization MUST با Permission classes پیاده شود (نه شرط‌های ad-hoc داخل view).
3) Throttling MUST برای endpointهای حساس (login/otp/reset/...) فعال باشد. :contentReference[oaicite:3]{index=3}
4) Token/credentials MUST فقط روی HTTPS منتقل شوند (اجباری). :contentReference[oaicite:4]{index=4}

### 4.3) Token Handling (قواعد اجرایی)

- Token MUST NOT در URL/querystring ارسال شود (مگر قرارداد رسمی و تایید).
- Token MUST در header استاندارد ارسال شود (مثلاً Authorization).
- Logها MUST NOT شامل token/secret باشند.

---

## 5) Models (ORM) و مرز Domain

### 5.1) قانون اصلی

- Django Models نماینده persistence هستند، نه الزاماً domain.
- Domain model (اگر دارید) MUST از ORM مستقل باشد.

### 5.2) قواعد ORM برای اسکیل

1) Queryهای پیچیده MUST در repository/infra تجمیع شوند، نه در view.
2) N+1 و query explosion MUST کنترل شود (select_related/prefetch_related در infra).
3) Migrationهای schema MUST کوچک، قابل rollback و قابل deploy باشند.
4) داده فارسی: UTF-8 end-to-end (DB + app + API).

---

## 6) Serializer, View, URL Routing

### 6.1) Serializer

- Serializer MUST:
  - validation سطح API انجام دهد
  - mapping ساده request↔domain DTO
- Serializer MUST NOT:
  - business rule سنگین اجرا کند
  - repository/ORM query انجام دهد

### 6.2) View/ViewSet

- View MUST:
  - فقط orchestration سطح HTTP را انجام دهد
  - permission/throttle را اعمال کند
  - UseCase را صدا بزند
- View MUST NOT:
  - transaction boundary تعریف کند
  - query پیچیده DB انجام دهد
  - قوانین دامنه را inline پیاده کند

### 6.3) urls.py

- مسیرها MUST:
  - نسخه‌دار باشند (`/api/v1/`)
  - namespaced باشند تا تعارض route کم شود
- ساختار URL باید قابل نگهداری باشد (include + namespace). (توصیه عملی در اکوسیستم Django رایج است، اما Agent باید با ساختار پروژه شما هم‌راستا باشد.)

---

## 7) Settings و Configuration

### 7.1) اصول

1) Settings MUST به تفکیک محیط باشند (dev/stage/prod) اگر پروژه چند محیط دارد.
2) Secrets MUST از env تامین شوند، نه hardcode.
3) REST_FRAMEWORK settings MUST مرکزی نگه داشته شود:
   - default authentication
   - default permissions
   - throttling
   - pagination
   - versioning scheme

### 7.2) سیاست تغییرات

- تغییر settings که رفتار عمومی API را تغییر می‌دهد (auth/versioning/throttle) تغییر ساختاری است و بدون تایید ممنوع.

---

## 8) App Design (Django apps) و SOLID

### 8.1) تقسیم‌بندی appها

- Appها MUST دامنه‌محور باشند (نه “core همه‌کاره”).
- هر app SHOULD یک bounded context مشخص داشته باشد.

### 8.2) SOLID (قابل اجرا برای Agent)

- SRP: View/Serializer/UseCase/Repository هرکدام فقط یک مسئولیت.
- OCP: افزودن feature جدید با افزودن UseCase/Policy، نه دستکاری گسترده.
- DIP: لایه Application به interface repository وابسته باشد، نه implementation مستقیم (در حد نیاز پروژه).

---

## 9) Testing (اجباری برای تغییرات حساس)

### 9.1) سطوح تست

1) Unit (Domain): بدون Django/DB
2) Application tests: با mock/fake repository
3) API tests: DRF client، permission/throttle/versioning

### 9.2) قوانین

- هر endpoint جدید MUST حداقل:
  - یک تست permission
  - یک تست success path
  - یک تست validation error
- breaking change MUST تست سازگاری نسخه‌ها/routeها را پوشش دهد.

---

## 10) معماری قابل اسکیل: چک‌های سلامت (Fitness Checks)

Agent SHOULD (و اگر CI دارید MUST) چک‌های زیر را enforce کند:

1) Domain import ممنوع از Django/DRF
2) View import ممنوع از repository impl
3) Transaction.atomic فقط در Application layer
4) Schema/OpenAPI تولیدی باید endpointهای جدید را پوشش دهد
5) Throttle فعال برای endpointهای حساس

---

## 11) Protocol اجرایی برای Agent (در هر تغییر)

Agent MUST قبل از اعمال تغییر:

1) لایه‌ی کد را مشخص کند (Interface/Application/Domain/Infra/DB)
2) اثر تغییر روی:
   - API contract/version
   - DB schema/migrations
   - security (auth/authz/token)
   - performance (queries)
   - tests
     را گزارش کند
3) اگر تعارض با قوانین این سند یا `AGENTS.tools.md` بود:
   - تغییر را متوقف کند
   - تعارض را گزارش کند
   - برای استثناء، Exception Record پیشنهاد دهد

---
