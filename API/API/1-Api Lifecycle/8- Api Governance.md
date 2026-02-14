
# **فصل ۸ — Governance & API Platform

راهنمای جامع، روایی، مفهومی، عملیاتی**

---

# **۰) مقدمهٔ روایی**

وقتی سازمان‌ها کوچک هستند، APIها اکثراً «لوکال»، «آزاد» و «بدون مقررات» ساخته می‌شوند؛ یک تیم Backend هرچه نیاز دارد می‌نویسد و منتشر می‌کند.
اما در یک سازمان متوسط به بالا:

* تعداد APIها زیاد می‌شود
* تیم‌ها متعدد می‌شوند
* نسخه‌گذاری‌ها پیچیده می‌شود
* امنیت اهمیت حیاتی پیدا می‌کند
* معماری توزیع‌شده رشد می‌کند
* نیاز به هم‌خوانی طراحی (Design Consistency) پیش می‌آید
* مصرف‌کنندگان API داخلی / خارجی / شرکایی می‌شوند

اینجاست که **API Governance** و **API Platform** دیگر یک انتخاب نیست، بلکه یک ضرورت است.

در واقع:

> Governance کاری می‌کند که «APIها نه فقط کار کنند، بلکه *درست* کار کنند، *مشابه* کار کنند، و *قابل اتکا* باشند.»

Postman، GitHub، Google API Fabric، Internal API Catalogs، OpenAPI Style Guides — همه در جهت همین هدف حرکت کرده‌اند.

---

# **۱) Definition of API Platform

تعریف پلتفرم API**

### **تعریف کلان / روایی**

پلتفرم API یعنی «زیربنایی که همهٔ APIهای سازمان را زیر یک سقف مدیریت می‌کند.»
این پلتفرم قرار نیست فقط یک Gateway باشد؛
بلکه یک **مجموعهٔ کامل ابزارها و استانداردها** است که API را از ایده تا تولید و بعد از تولید مدیریت می‌کند.

### **تعریف دقیق / مهندسی**

An **API Platform** is a *governed, standardized, discoverable, secure environment* for:

* Design
* Versioning
* Documentation
* Testing
* Deployment
* Monitoring
* Policy Enforcement
* Lifecycle Governance
* Internal API Cataloging
* Developer Experience (DX)

در واقع API Platform یک لایهٔ فرهنگی + فنی است:

```
API Platform = Tooling + Standards + Governance + Catalog + Security
```

### مثال‌های واقعی:

* **Postman API Platform** → API Governance, Style Guides, Catalog, CI/CD Integration
* **Google API Platform** → gRPC/REST Governance, API Linter, API Producer Portal
* **Netflix** → Paved Path API Platform
* **Shopify** → API Style Framework + Versioning Governance

---

# **۲) Governance Models

(مرکزیت‌یافته / غیرمتمرکز / هیبرید)**

API Governance سه الگوی اصلی دارد:

---

## **۲.۱. مدل Centralized Governance (متمرکز)**

### توصیف

یک تیم مرکزی به نام **API Governance Team** وجود دارد و تمام APIها باید:

* استانداردها را رعایت کنند
* طراحی‌شان بررسی شود
* نسخه‌گذاری تایید شود
* امنیت تایید شود

### مزایا

* Consistency بالا
* امنیت یکپارچه
* پیاده‌سازی ساده در سازمان‌های کوچک

### معایب

* کند شدن توسعه
* ایجاد bottleneck
* نارضایتی تیم‌های توسعه

### مثال واقعی

بانک‌ها و سازمان‌های Enterprise بزرگ.

---

## **۲.۲. مدل Decentralized Governance (غیرمتمرکز)**

### توصیف

هر تیم آزادی دارد API خود را با سرعت بالا توسعه دهد.
Governance فقط به صورت «راهنما» (Guideline) است، نه قانون.

### مزایا

* سرعت بالا
* استقلال تیم‌ها
* مناسب برای سازمان‌های Agile

### معایب

* APIها شلخته، نامنظم، غیرهماهنگ
* امنیت پراکنده
* مشکلاتی در کشف (Discoverability)

### مثال واقعی

Uber، Spotify، Pinterest در دوره‌های رشد اولیه.

---

## **۲.۳. مدل Hybrid Governance (بهترین مدل)**

ترکیب:

* آزادی تیم‌ها
* همراه با Rules ثابت که نباید شکسته شوند
* همراه با ابزارهای خودکار مثل Linting، Style Guide و CI Checks

### چرا مدل برتر است؟

* سرعت حفظ می‌شود
* کیفیت تضمین می‌شود
* سلیقهٔ شخصی تبدیل به استاندارد سازمانی می‌شود

### مثال واقعی

Netflix, Google, Shopify, Meta

---

# **۳) Standards, Style Guides, Linting**

این یکی از مهم‌ترین ستون‌های Governance است.

---

## **۳.۱. Style Guide چیست؟**

Style Guide یعنی:

> «قوانینی که طراحی API سازمان را یکپارچه، استاندارد و بدون تناقض می‌کند.»

مانند:

* URL Structure

  ```
  /users/{id}/orders
  /products/{id}
  ```

* Consistent HTTP verbs

  * GET → retrieve
  * POST → create
  * PATCH → update

* Consistent error model

  * همیشه ساختار خطا یکسان باشد

* Consistent pagination

* Naming conventions

  * snake_case یا camelCase؟
  * جمع/مفرد؟

---

## **۳.۲. Linting چیست؟**

Linting یعنی:

> چک خودکار API Spec برای مطابقت با Style Guide.

ابزارها:

* Postman API Governance
* Spectral (OpenAPI Linter)
* Google API Linter
* Redocly Lint
* Stoplight Spectral

### مثال واقعی

در Postman:

```
APIs → Select Spec → Governance → Apply Style Guide
```

Postman خودش:

* مسائل را تشخیص می‌دهد
* Severity تعیین می‌کند (error/warning/info)
* مسیر رفع مشکل را پیشنهاد می‌دهد

---

# **۴) API Discoverability & Internal API Catalogs**

وقتی API زیاد می‌شود، بدون یک **Catalog** هیچ‌کس نمی‌داند:

* چه APIهایی داریم
* کدام API قابل استفاده است
* کدام deprecated است
* کدام نسخه‌ها فعال هستند
* چه تیمی مسؤول هر API است
* مستندات رسمی کجاست

### API Catalog چیست؟

فرهنگ‌نامه‌ای از APIهای سازمان.

### ویژگی‌های یک API Catalog خوب:

* Tagging
* Versioning
* Ownership
* Documentation
* Schema / Types
* Security classification
* Usage analytics

### مثال‌های واقعی Catalog

* Postman Public Workspace + Private API Catalog
* Google API Directory
* GitHub Internal API Hub
* Redocly API Registry

### در Postman نسخه جدید:

```
Sidebar → APIs
→ Import Spec
→ It becomes part of API Catalog
→ Automatically linked to Collections, Tests, Monitors
```

---

# **۵) Security Governance & Zero Trust API Security**

این بخش هستهٔ اصلی API Governance در معماری‌های مدرن است.

## ۵.۱ Zero Trust چیست؟

اصل Zero Trust:

> «هیچ ارتباطی را ایمن فرض نکن؛ همیشه اعتبارسنجی کن.»

در API یعنی:

* Authn + Authz همیشه فعال
* Secret rotation
* Rate-limiting
* Input validation
* Event Logging
* Trust boundaries مشخص
* Access Token Scopes دقیق

### ابزارهای اصلی در API Security Governance

* API Gateway policies (Kong, Apigee, NGINX, AWS API Gateway)
* Security Rules (OAuth2 Scopes, JWT Claims, mTLS, IP Restrictions)
* API Key Rotations
* Threat Detection (OWASP API Security Top 10)

---

# ========

# **IN ACTION — بخش عملیاتی فصل Governance & API Platform**

# ========

در این بخش، پروژه Django تو + Postman را وارد مرحله Governance می‌کنیم.

---

# **Action 1 — ایجاد API Style Guide در Postman**

### مسیر:

```
APIs → Create Style Guide
```

### داخل Style Guide قوانین زیر را اضافه کن:

#### Rule 1 — naming

```
paths:
  pattern: "^/[a-z]+(/[a-z0-9]+)*$"
error: "Path must be lowercase and use kebab-case or snake-case"
```

#### Rule 2 — error model استاندارد

بررسی وجود فیلدها:

```
components.schemas.Error:
  required:
    - error
    - message
```

#### Rule 3 — versioning

```
Every path MUST start with /api/v{number}/
```

---

# **Action 2 — lint کردن Spec API تو**

Spec فعلی تو (که خودت فرستادی):

```
APIs → Import → OpenAPI 3.1 → Select Spec
Governance → Apply Style Guide
```

Postman:

* تمام مشکلات رعایت‌نشده را پیدا می‌کند
* Severity تعیین می‌کند
* پیشنهاد رفع مشکل می‌دهد

این می‌شود **Governance Automation**.

---

# **Action 3 — ساخت Internal API Catalog**

### مرحله ۱

Specهای v1 و v2 را وارد Postman:

```
APIs → Import → OpenAPI Spec
```

### مرحله ۲

برای هر API تعیین کن:

* Team owner
* Version
* Status (active / deprecated)
* Tags (orders, products, users)

### مرحله ۳

API Catalog ساخته می‌شود و سازمان تو می‌تواند:

* APIها را جستجو کند
* نسخه‌بندی را دنبال کند
* مشخص کند چه سرویس‌هایی به چه سرویس‌هایی وابسته‌اند

---

# **Action 4 — Security Governance Checklist**

برای پروژه Django:

### در سطح Postman:

* تعیین Authentication Type (No Auth, API Key, OAuth2)
* تعریف Token rotation
* تعیین محدودیت‌ها در Test Scripts:

```javascript
pm.test("Authorization exists", () => {
  pm.expect(pm.request.headers.get("Authorization")).to.not.be.undefined
})
```

### در Backend (Django):

* فعال‌سازی DRF Authentication
* فعال‌سازی JWT یا OAuth2
* محدودسازی endpointها
* فعال‌سازی rate limiting (django-ratelimit)

---

# **Action 5 — Governance برای Versioning v1 / v2**

چک‌های سبک در Postman:

* مسیرهای v1 باید immutable باشند
* مسیرهای v2 باید Breaking Changes مستند داشته باشند
* Spec v1 و v2 هر دو در Catalog نگهداری شوند

به این شکل:

```
APIs
 ├── Order API v1
 └── Order API v2
```

---

# **Action 6 — فرآیند رسمی Governance (Template پیشنهادی)**

این فرآیند در شرکت‌های واقعی استفاده می‌شود:

### ۱) Proposal

طراح API یک ADR / RFC داخلی می‌نویسد.

### ۲) Style Guide Check

Linting Postman + Spectral اجرا می‌شود.

### ۳) Security Review

تیم امنیت Scopes و Threat Model را بررسی می‌کند.

### ۴) Versioning Approval

تیم API تصمیم می‌گیرد تغییر **Minor** است یا **Major**.

### ۵) Merge + Release

Pipeline CI/CD → Publish Spec + Update Catalog.

### ۶) Monitoring & Observability

با استفاده از فصل ۷.

این چرخه، API Platform را به یک **سیستم پایدار، امن و کنترل‌شده** تبدیل می‌کند.

---

# **نتیجهٔ فصل ۸**

تو اکنون می‌دانی:

* API Platform چیست
* Governance چه مدل‌هایی دارد
* چگونه Style Guide می‌سازیم
* چرا Linting ضروری است
* چگونه API Catalog را ایجاد و مدیریت می‌کنیم
* Zero Trust چگونه روی API اعمال می‌شود
* و نهایتاً چگونه Governance عملیاتی می‌شود
