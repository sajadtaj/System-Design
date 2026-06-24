# 09 - Versioning

## اهداف فصل

در پایان این فصل:

* مفهوم API Versioning را درک می‌کنید.
* دلیل استفاده از Versioning را می‌فهمید.
* انواع Versioning در DRF را می‌شناسید.
* Versioning را در پروژه‌های DRF پیاده‌سازی می‌کنید.
* به نسخه API از طریق `request.version` دسترسی پیدا می‌کنید.
* برای تغییرات آینده API طراحی بهتری انجام می‌دهید.

---

# مقدمه

فرض کنید امروز API زیر را منتشر کرده‌اید:

```http
GET /api/books/
```

پاسخ:

```json
{
    "id": 1,
    "title": "Django REST Framework"
}
```

---

شش ماه بعد تصمیم می‌گیرید:

* فیلدهای جدید اضافه کنید.
* ساختار پاسخ را تغییر دهید.
* برخی فیلدها را حذف کنید.

مثلاً:

```json
{
    "id": 1,
    "title": "Django REST Framework",
    "author": "Sajad"
}
```

---

مشکل چیست؟

ممکن است:

* Mobile App
* React Frontend
* سایر Clientها

هنوز نسخه قدیمی API را مصرف کنند.

---

در نتیجه:

```text
API Breaking Change
```

رخ می‌دهد.

---

Versioning برای حل این مشکل ایجاد شده است.

---

# Versioning چیست؟

Versioning یعنی:

```text
امکان پشتیبانی همزمان
از چند نسخه API
```

---

مثال:

```http
/api/v1/books/
/api/v2/books/
```

---

یا:

```http
/api/books/?version=v1
/api/books/?version=v2
```

---

هدف:

```text
تغییر API
بدون شکستن Clientهای قدیمی
```

---

# چرا Versioning مهم است؟

فرض کنید:

نسخه اول:

```json
{
    "title": "DRF"
}
```

---

نسخه دوم:

```json
{
    "book_title": "DRF"
}
```

---

Client قدیمی:

```text
title
```

را انتظار دارد.

---

اما API:

```text
book_title
```

برمی‌گرداند.

---

در نتیجه:

```text
Client Crash
```

---

Versioning این مشکل را حل می‌کند.

---

# Versioning در DRF

تمام Versioningهای DRF از کلاس‌های زیر مشتق می‌شوند:

```python
rest_framework.versioning.BaseVersioning
```

---

DRF چند استراتژی آماده ارائه می‌دهد:

```python
URLPathVersioning

NamespaceVersioning

AcceptHeaderVersioning

QueryParameterVersioning

HostNameVersioning
```

---

# محل تنظیم Versioning

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_VERSIONING_CLASS":
        "...",

    "DEFAULT_VERSION": "v1",

    "ALLOWED_VERSIONS": [
        "v1",
        "v2",
    ],

    "VERSION_PARAM": "version",
}
```

---

# QueryParameterVersioning

ساده‌ترین روش.

---

فعال‌سازی:

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_VERSIONING_CLASS":

        "rest_framework.versioning.QueryParameterVersioning",

    "DEFAULT_VERSION": "v1",

    "ALLOWED_VERSIONS": [

        "v1",
        "v2",
    ],

    "VERSION_PARAM": "version",
}
```

---

درخواست:

```http
GET /api/books/?version=v1
```

---

نسخه دوم:

```http
GET /api/books/?version=v2
```

---

# دسترسی به نسخه جاری

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)
```

---

```python
class BookAPIView(APIView):

    def get(
        self,
        request
    ):

        return Response({
            "version":
                request.version
        })
```

---

خروجی:

```json
{
    "version": "v1"
}
```

---

# استفاده واقعی از Version

فایل:

```text
MyProject/books/views.py
```

```python
class BookAPIView(APIView):

    def get(
        self,
        request
    ):

        if request.version == "v1":

            return Response({
                "title": "DRF"
            })

        return Response({
            "title": "DRF",
            "author": "Sajad"
        })
```

---

# URLPathVersioning

یکی از محبوب‌ترین روش‌ها.

---

ساختار:

```http
/api/v1/books/
/api/v2/books/
```

---

فعال‌سازی:

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_VERSIONING_CLASS":

        "rest_framework.versioning.URLPathVersioning"
}
```

---

# تنظیم URL

فایل:

```text
MyProject/config/urls.py
```

```python
from django.urls import (
    path
)

from books.views import (
    BookAPIView
)
```

---

```python
urlpatterns = [

    path(
        "api/<str:version>/books/",
        BookAPIView.as_view(),
    )
]
```

---

درخواست:

```http
GET /api/v1/books/
```

---

یا:

```http
GET /api/v2/books/
```

---

# مزایای URLPathVersioning

مزایا:

```text
واضح

ساده

محبوب

مناسب Public API
```

---

معایب:

```text
URLهای بیشتر
```

---

# NamespaceVersioning

نسخه‌بندی از طریق Django Namespace.

---

ساختار:

فایل:

```text
MyProject/books/v1/urls.py
```

---

```python
app_name = "v1"
```

---

فایل:

```text
MyProject/books/v2/urls.py
```

---

```python
app_name = "v2"
```

---

فایل:

```text
MyProject/config/urls.py
```

```python
path(
    "api/v1/",
    include(
        (
            "books.v1.urls",
            "v1"
        )
    )
)
```

---

مزیت:

```text
جداسازی کامل نسخه‌ها
```

---

مناسب:

```text
APIهای بزرگ
```

---

# AcceptHeaderVersioning

نسخه از طریق Header ارسال می‌شود.

---

فعال‌سازی:

```python
REST_FRAMEWORK = {

    "DEFAULT_VERSIONING_CLASS":

        "rest_framework.versioning.AcceptHeaderVersioning"
}
```

---

درخواست:

```http
Accept: application/json; version=v1
```

---

یا:

```http
Accept: application/json; version=v2
```

---

مزیت:

```text
URL ثابت
```

---

معایب:

```text
پیچیدگی بیشتر
```

---

# HostNameVersioning

نسخه در دامنه مشخص می‌شود.

---

مثال:

```http
v1.api.example.com
```

---

```http
v2.api.example.com
```

---

کاربرد:

```text
سازمان‌های بزرگ
```

---

# بهترین روش برای اکثر پروژه‌ها

برای اکثر پروژه‌های Django/DRF:

```text
URLPathVersioning
```

یا:

```text
NamespaceVersioning
```

بهترین انتخاب است.

---

دلیل:

* خوانایی بالا
* مستندسازی ساده
* پشتیبانی بهتر

---

# Versioning و Serializer

سناریوی رایج:

نسخه اول:

فایل:

```text
MyProject/books/serializers.py
```

```python
class BookSerializerV1(
    serializers.ModelSerializer
):
    ...
```

---

نسخه دوم:

```python
class BookSerializerV2(
    serializers.ModelSerializer
):
    ...
```

---

انتخاب Serializer:

فایل:

```text
MyProject/books/views.py
```

```python
def get_serializer_class(
    self
):

    if (
        self.request.version
        == "v1"
    ):

        return BookSerializerV1

    return BookSerializerV2
```

---

# Versioning و View

گاهی کل Business Logic تغییر می‌کند.

---

مثال:

```python
if request.version == "v1":
    ...
```

---

اما در پروژه‌های بزرگ بهتر است:

```text
views_v1.py

views_v2.py
```

داشته باشید.

---

# نکته معماری

اشتباه:

```python
if version == ...
elif version == ...
elif version == ...
elif version == ...
```

در یک فایل.

---

بعد از چند سال:

```text
کد غیرقابل نگهداری
```

خواهد شد.

---

# استراتژی پیشنهادی

ساختار:

```text
MyProject/

books/

├── v1/
│   ├── serializers.py
│   ├── views.py
│   └── urls.py

├── v2/
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
```

---

مزایا:

* جداسازی کامل
* تست آسان‌تر
* حذف نسخه‌های قدیمی ساده‌تر

---

# چه زمانی Version جدید بسازیم؟

نیازی نیست برای هر تغییر:

```text
v3

v4

v5
```

بسازید.

---

Version جدید زمانی لازم است که:

```text
Breaking Change
```

داشته باشید.

---

# نمونه Breaking Change

حذف فیلد:

```json
{
    "title": "DRF"
}
```

---

تغییر به:

```json
{
    "book_title": "DRF"
}
```

---

یا:

```json
{
    "title": {
        "fa": "...",
        "en": "..."
    }
}
```

---

# خطاهای رایج

## Versioning خیلی زود

پروژه هنوز Client ندارد.

اما:

```text
v1

v2

v3
```

ساخته شده است.

---

## نگهداری نسخه‌های قدیمی برای همیشه

باعث افزایش هزینه نگهداری می‌شود.

---

## تغییر API بدون Version

باعث شکستن Clientها می‌شود.

---

## منطق پیچیده Version در یک View

کد را غیرقابل نگهداری می‌کند.

---

# Best Practices

1. فقط هنگام Breaking Change نسخه جدید ایجاد کنید.
2. برای پروژه‌های عمومی از URLPathVersioning استفاده کنید.
3. نسخه‌های قدیمی را زمان‌بندی‌شده حذف کنید.
4. Serializerها را بین نسخه‌ها جدا کنید.
5. مستندات هر نسخه را مستقل نگهداری کنید.
6. از Versioning از روز اول پروژه‌های عمومی استفاده کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Versioning چیست.
* چرا در APIها ضروری است.
* انواع Versioning در DRF چیست.
* QueryParameterVersioning چگونه کار می‌کند.
* URLPathVersioning چگونه پیاده‌سازی می‌شود.
* NamespaceVersioning چیست.
* AcceptHeaderVersioning چیست.
* چگونه Serializer و View را بر اساس Version تغییر دهیم.
* بهترین ساختار معماری برای مدیریت نسخه‌ها چیست.

فصل بعدی:

```text
10 - Throttling
```

---

## منابع رسمی

* Versioning

[DRF Versioning Documentation](https://www.django-rest-framework.org/api-guide/versioning/?utm_source=chatgpt.com)

