# 17 - Metadata

## اهداف فصل

در پایان این فصل:

* مفهوم Metadata در DRF را درک می‌کنید.
* با متد HTTP `OPTIONS` آشنا می‌شوید.
* نحوه تولید Metadata توسط DRF را می‌فهمید.
* با `SimpleMetadata` آشنا می‌شوید.
* می‌دانید Metadata چه تفاوتی با Schema دارد.
* موارد استفاده واقعی Metadata را می‌شناسید.

---

# Metadata چیست؟

Metadata یعنی:

```text id="m1"
اطلاعات درباره API
نه خود داده‌های API
```

---

مثال:

داده واقعی:

```json id="m2"
{
    "id": 1,
    "title": "DRF"
}
```

---

Metadata:

```json id="m3"
{
    "name": "Book List",
    "renders": [
        "application/json"
    ],
    "parses": [
        "application/json"
    ]
}
```

---

Metadata درباره API توضیح می‌دهد.

نه درباره کتاب‌ها.

---

# Metadata چه کاربردی دارد؟

کمک می‌کند Client متوجه شود:

* چه متدهایی مجاز هستند.
* چه فیلدهایی وجود دارند.
* چه فرمت‌هایی پشتیبانی می‌شوند.
* چه داده‌ای باید ارسال شود.

---

# متد OPTIONS

در HTTP متدی به نام:

```http id="m4"
OPTIONS
```

وجود دارد.

---

وظیفه آن:

```text id="m5"
دریافت اطلاعات Endpoint
```

است.

---

مثال:

```http id="m6"
OPTIONS /api/books/
```

---

پاسخ:

```json id="m7"
{
    "name": "Book List",
    "description": "",
    "renders": [
        "application/json"
    ],
    "parses": [
        "application/json"
    ]
}
```

---

# تفاوت GET و OPTIONS

GET:

```http id="m8"
GET /api/books/
```

---

داده برمی‌گرداند.

---

OPTIONS:

```http id="m9"
OPTIONS /api/books/
```

---

اطلاعات Endpoint را برمی‌گرداند.

---

# Metadata در Browsable API

وقتی وارد صفحه Browsable API می‌شوید:

```text id="m10"
DRF
```

از Metadata برای ساخت فرم‌ها استفاده می‌کند.

---

مثال:

اگر Serializer داشته باشیم:

فایل:

```text id="m11"
MyProject/books/serializers.py
```

```python id="m12"
class BookSerializer(
    serializers.Serializer
):

    title = (
        serializers.CharField()
    )

    pages = (
        serializers.IntegerField()
    )
```

---

Browsable API می‌تواند تشخیص دهد:

```text id="m13"
title → text input

pages → number input
```

---

این اطلاعات از Metadata استخراج می‌شوند.

---

# SimpleMetadata

پیاده‌سازی پیش‌فرض DRF.

---

فایل:

```text id="m14"
rest_framework.metadata.SimpleMetadata
```

---

این کلاس اطلاعات پایه Endpoint را تولید می‌کند.

---

# مشاهده Metadata

فایل:

```text id="m15"
MyProject/books/views.py
```

```python id="m16"
class BookAPIView(
    APIView
):
    ...
```

---

در ترمینال:

```bash id="m17"
curl -X OPTIONS \
http://localhost:8000/api/books/
```

---

پاسخ Metadata را مشاهده خواهید کرد.

---

# غیرفعال کردن Metadata

فایل:

```text id="m18"
MyProject/config/settings.py
```

```python id="m19"
REST_FRAMEWORK = {

    "DEFAULT_METADATA_CLASS":
        None
}
```

---

معمولاً این کار توصیه نمی‌شود مگر در شرایط خاص.

---

# Custom Metadata

گاهی اطلاعات پیش‌فرض کافی نیست.

---

فایل:

```text id="m20"
MyProject/common/metadata.py
```

```python id="m21"
from rest_framework.metadata import (
    SimpleMetadata
)
```

---

```python id="m22"
class CustomMetadata(
    SimpleMetadata
):

    def determine_metadata(
        self,
        request,
        view
    ):

        metadata = (
            super()
            .determine_metadata(
                request,
                view
            )
        )

        metadata["version"] = (
            "v1"
        )

        return metadata
```

---

# فعال‌سازی

فایل:

```text id="m23"
MyProject/config/settings.py
```

```python id="m24"
REST_FRAMEWORK = {

    "DEFAULT_METADATA_CLASS":

        "common.metadata.CustomMetadata"
}
```

---

اکنون:

```http id="m25"
OPTIONS
```

---

شامل:

```json id="m26"
{
    "version": "v1"
}
```

نیز خواهد بود.

---

# Metadata و Serializer

Metadata می‌تواند اطلاعاتی درباره فیلدها ارائه کند.

---

مثال:

```python id="m27"
title = serializers.CharField(
    required=True
)
```

---

Metadata تشخیص می‌دهد:

```text id="m28"
required = true
```

---

و آن را در پاسخ OPTIONS قرار می‌دهد.

---

# Metadata و Authentication

Metadata معمولاً تحت همان قوانین:

```text id="m29"
Authentication
Permission
```

کار می‌کند.

---

بنابراین اگر Endpoint محافظت شده باشد:

```http id="m30"
OPTIONS
```

نیز ممکن است نیازمند احراز هویت باشد.

---

# Metadata و Schema

بسیار مهم:

---

Metadata:

```text id="m31"
اطلاعات لحظه‌ای Endpoint
```

---

Schema:

```text id="m32"
توصیف کامل API
```

---

مثال:

Metadata:

```json id="m33"
{
    "name": "Book List"
}
```

---

Schema:

```yaml id="m34"
paths:
  /books:
    get:
      ...
```

---

به همین دلیل:

```text id="m35"
Metadata
```

و

```text id="m36"
Schema
```

دو مفهوم متفاوت هستند.

---

# آیا در پروژه‌های واقعی استفاده می‌شود؟

صادقانه:

```text id="m37"
کمتر از گذشته
```

---

امروزه بیشتر ابزارها روی:

```text id="m38"
OpenAPI
Swagger
```

متمرکز هستند.

---

اما هنوز:

* Browsable API
* ابزارهای داخلی DRF
* برخی Clientهای پویا

از Metadata استفاده می‌کنند.

---

# خطاهای رایج

## اشتباه گرفتن Metadata با Schema

این دو جایگزین یکدیگر نیستند.

---

## وابستگی کامل به Metadata

امروزه:

```text id="m39"
OpenAPI Schema
```

اهمیت بیشتری دارد.

---

## سفارشی‌سازی بیش از حد

Metadata باید سبک و ساده بماند.

---

# Best Practices

1. Metadata را بشناسید اما روی Schema سرمایه‌گذاری کنید.
2. برای APIهای عمومی OpenAPI مهم‌تر است.
3. از Custom Metadata فقط در صورت نیاز استفاده کنید.
4. تفاوت Metadata و Schema را فراموش نکنید.
5. از OPTIONS برای بررسی قابلیت‌های Endpoint استفاده کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Metadata چیست.
* OPTIONS چیست.
* SimpleMetadata چگونه کار می‌کند.
* چگونه Metadata سفارشی بسازیم.
* Metadata چه تفاوتی با Schema دارد.
* در پروژه‌های مدرن چه جایگاهی دارد.

---

فصل بعدی:

```text id="m40"
18 - Schemas
```

---

## منابع رسمی

* Metadata

[DRF Metadata Documentation](https://www.django-rest-framework.org/api-guide/metadata/?utm_source=chatgpt.com)

