# 18 - Schemas

## اهداف فصل

در پایان این فصل:

* مفهوم Schema را درک می‌کنید.
* تفاوت Schema و Metadata را می‌فهمید.
* با OpenAPI آشنا می‌شوید.
* نحوه تولید Schema در DRF را یاد می‌گیرید.
* Swagger و ReDoc را می‌شناسید.
* با drf-spectacular آشنا می‌شوید.
* می‌توانید API خود را مستندسازی کنید.

---

# Schema چیست؟

Schema یعنی:

```text id="s1"
توصیف ساختاری API
```

---

به زبان ساده:

Schema سندی است که توضیح می‌دهد:

* چه Endpointهایی وجود دارد.
* چه Requestهایی پذیرفته می‌شوند.
* چه Responseهایی برگردانده می‌شوند.
* Authentication چگونه انجام می‌شود.
* چه Status Codeهایی وجود دارند.

---

# چرا Schema مهم است؟

فرض کنید API زیر را ساخته‌اید:

```http id="s2"
GET /api/books/

POST /api/books/

GET /api/books/{id}/
```

---

از کجا Frontend یا Mobile Team متوجه شوند:

* فیلدها چیست؟
* نوع داده چیست؟
* کدام فیلد اجباری است؟

---

پاسخ:

```text id="s3"
Schema
```

---

# تفاوت Metadata و Schema

Metadata:

```text id="s4"
اطلاعات یک Endpoint
```

---

Schema:

```text id="s5"
توصیف کامل کل API
```

---

Metadata:

```http id="s6"
OPTIONS /api/books/
```

---

Schema:

```text id="s7"
کل پروژه
```

---

# OpenAPI چیست؟

امروزه استاندارد صنعت:

```text id="s8"
OpenAPI Specification
```

است.

---

تقریباً تمام ابزارهای مدرن:

* Swagger
* ReDoc
* Postman
* Insomnia

از OpenAPI استفاده می‌کنند.

---

# نمونه Schema

نمونه ساده:

```yaml id="s9"
paths:

  /books:

    get:
      summary: List Books

    post:
      summary: Create Book
```

---

نیازی نیست YAML را حفظ کنید.

---

مهم این است که بدانید:

```text id="s10"
Schema
```

منبع اصلی مستندات API است.

---

# تولید Schema در DRF

DRF قابلیت تولید Schema را دارد.

---

فایل:

```text id="s11"
MyProject/config/urls.py
```

```python id="s12"
from rest_framework.schemas import (
    get_schema_view
)
```

---

```python id="s13"
schema_view = (
    get_schema_view(
        title="Book API",
        description="DRF Book Example",
        version="1.0.0"
    )
)
```

---

```python id="s14"
urlpatterns = [

    path(
        "schema/",
        schema_view
    )
]
```

---

اکنون:

```http id="s15"
/schema/
```

---

Schema پروژه را نمایش می‌دهد.

---

# مشکل Schema پیش‌فرض DRF

برای پروژه‌های کوچک مناسب است.

---

اما در پروژه‌های واقعی:

```text id="s16"
محدودیت دارد.
```

---

به همین دلیل اکثر تیم‌ها از:

```text id="s17"
drf-spectacular
```

استفاده می‌کنند.

---

# drf-spectacular

محبوب‌ترین ابزار OpenAPI برای DRF.

---

نصب:

```bash id="s18"
pip install drf-spectacular
```

---

# تنظیمات

فایل:

```text id="s19"
MyProject/config/settings.py
```

```python id="s20"
REST_FRAMEWORK = {

    "DEFAULT_SCHEMA_CLASS":

        "drf_spectacular.openapi.AutoSchema"
}
```

---

# افزودن URL

فایل:

```text id="s21"
MyProject/config/urls.py
```

```python id="s22"
from drf_spectacular.views import (

    SpectacularAPIView,

    SpectacularSwaggerView,

    SpectacularRedocView
)
```

---

```python id="s23"
urlpatterns += [

    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),

    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        )
    ),

    path(
        "api/redoc/",
        SpectacularRedocView.as_view(
            url_name="schema"
        )
    )
]
```

---

# Swagger چیست؟

Swagger یک رابط گرافیکی برای API است.

---

مثال:

```text id="s24"
GET /books/

POST /books/
```

---

همراه با:

* پارامترها
* Authentication
* Responseها

نمایش داده می‌شود.

---

مزایا:

* تست API
* مستندسازی
* آموزش تیم

---

# ReDoc چیست؟

جایگزین Swagger.

---

تمرکز بیشتر روی:

```text id="s25"
خوانایی مستندات
```

---

بسیاری از شرکت‌ها:

```text id="s26"
Swagger
```

برای توسعه‌دهندگان

و:

```text id="s27"
ReDoc
```

برای مستندات رسمی استفاده می‌کنند.

---

# مستندسازی Endpoint

مثال:

فایل:

```text id="s28"
MyProject/books/views.py
```

---

```python id="s29"
from drf_spectacular.utils import (
    extend_schema
)
```

---

```python id="s30"
@extend_schema(
    summary="Book List",
    description="Returns all books"
)
class BookListAPIView(
    ListAPIView
):
    ...
```

---

اکنون Swagger توضیحات بهتری نمایش می‌دهد.

---

# مستندسازی پارامترها

مثال:

```http id="s31"
GET /books/?title=django
```

---

می‌توان پارامترها را نیز مستندسازی کرد.

---

این موضوع در پروژه‌های بزرگ بسیار مهم است.

---

# Authentication در Schema

اگر JWT استفاده می‌کنید:

فصل:

```text id="s32"
06.1 JWT
```

---

باید در Schema نیز مشخص شود.

---

تا Swagger بداند:

```text id="s33"
Bearer Token
```

مورد نیاز است.

---

# مزیت بزرگ OpenAPI

یک Frontend Developer می‌تواند:

```text id="s34"
بدون خواندن کد Backend
```

---

API را درک کند.

---

حتی برخی ابزارها قادرند:

```text id="s35"
Client Code Generation
```

انجام دهند.

---

# آیا Schema را باید دستی نوشت؟

در DRF:

```text id="s36"
خیر
```

---

بخش زیادی از آن خودکار تولید می‌شود.

---

اما:

```text id="s37"
توضیحات
مثال‌ها
Business Rules
```

را بهتر است تکمیل کنید.

---

# خطاهای رایج

## نداشتن مستندات API

بزرگ‌ترین اشتباه پروژه‌های داخلی.

---

## استفاده از مستندات Word یا PDF

مستندات باید:

```text id="s38"
Live
```

باشند.

---

Swagger و ReDoc این مشکل را حل می‌کنند.

---

## عدم مستندسازی Authentication

کاربر نمی‌داند چگونه به API متصل شود.

---

## توضیح ندادن پارامترها

باعث سردرگمی Frontend می‌شود.

---

# Best Practices

1. از OpenAPI استفاده کنید.
2. برای پروژه‌های جدید از drf-spectacular استفاده کنید.
3. Swagger را برای توسعه فعال کنید.
4. توضیحات Endpointها را تکمیل کنید.
5. Authentication را مستندسازی کنید.
6. مستندات را همزمان با توسعه API به‌روزرسانی کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Schema چیست.
* تفاوت Metadata و Schema چیست.
* OpenAPI چیست.
* چگونه Schema تولید کنیم.
* Swagger چیست.
* ReDoc چیست.
* drf-spectacular چیست.
* چگونه API را مستندسازی کنیم.

---

# نکته مهم برای پروژه‌های واقعی

امروزه در اکثر پروژه‌های DRF جدید:

```text id="s39"
drf-spectacular
+
Swagger
+
OpenAPI
```

عملاً استاندارد صنعت محسوب می‌شوند.

اگر فقط یک ابزار از کل این فصل را انتخاب کنید، آن ابزار:

```text id="s40"
drf-spectacular
```

خواهد بود.

---

فصل بعدی:

```text id="s41"
19 - Testing
```

---

## منابع رسمی

* Schemas

[DRF Schemas Documentation](https://www.django-rest-framework.org/api-guide/schemas/?utm_source=chatgpt.com)

