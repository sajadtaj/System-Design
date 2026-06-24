# 10 - Throttling

## اهداف فصل

در پایان این فصل:

* مفهوم Throttling را درک می‌کنید.
* تفاوت Authentication، Permission و Throttling را می‌فهمید.
* Throttling را در DRF فعال می‌کنید.
* User Rate Limiting را پیاده‌سازی می‌کنید.
* Anonymous Rate Limiting را پیاده‌سازی می‌کنید.
* Scoped Throttling را یاد می‌گیرید.
* محدودیت‌های Throttling در DRF را می‌شناسید.
* برای Production تصمیم درستی می‌گیرید.

---

# مقدمه

فرض کنید API زیر را منتشر کرده‌اید:

```http
GET /api/books/
```

یک کاربر عادی:

```text
روزانه 100 درخواست
```

ارسال می‌کند.

---

اما یک Bot یا Script می‌تواند:

```text
1000 Request / second
```

ارسال کند.

---

نتیجه:

* افزایش مصرف CPU
* افزایش مصرف RAM
* فشار روی Database
* افزایش هزینه زیرساخت
* کاهش کیفیت سرویس

---

برای کنترل این وضعیت از:

```text
Throttling
```

استفاده می‌کنیم.

---

# Throttling چیست؟

Throttling یعنی:

```text
محدود کردن تعداد درخواست‌ها
در یک بازه زمانی مشخص
```

---

مثال:

```text
100 Request / hour
```

---

اگر کاربر بیشتر ارسال کند:

```http
429 Too Many Requests
```

دریافت خواهد کرد.

---

# تفاوت Authentication و Permission و Throttling

بسیاری از توسعه‌دهندگان این سه مفهوم را اشتباه می‌گیرند.

---

## Authentication

پرسش:

```text
چه کسی هستی؟
```

مثال:

```python
JWTAuthentication
```

---

## Permission

پرسش:

```text
اجازه انجام این کار را داری؟
```

مثال:

```python
IsAuthenticated
IsAdminUser
```

---

## Throttling

پرسش:

```text
چند بار می‌توانی این کار را انجام دهی؟
```

مثال:

```text
100 Request / hour
```

---

# معماری DRF Request Flow

```text
Request
   ↓
Authentication
   ↓
Permission
   ↓
Throttling
   ↓
View
   ↓
Response
```

---

# Throttle Classes

تمام Throttleها از:

```python
BaseThrottle
```

مشتق می‌شوند.

---

کلاس‌های آماده DRF:

```python
AnonRateThrottle

UserRateThrottle

ScopedRateThrottle
```

---

# فعال‌سازی سراسری

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_THROTTLE_CLASSES": [

        "rest_framework.throttling.AnonRateThrottle",

        "rest_framework.throttling.UserRateThrottle",
    ],

    "DEFAULT_THROTTLE_RATES": {

        "anon": "100/day",

        "user": "1000/day",
    }
}
```

---

# معنی تنظیمات

کاربران ناشناس:

```text
100 Request / day
```

---

کاربران لاگین‌شده:

```text
1000 Request / day
```

---

# فرمت Rate

ساختار:

```text
<number>/<period>
```

---

مثال:

```text
10/minute

100/hour

1000/day
```

---

واحدهای زمانی:

```text
second

minute

hour

day
```

---

# AnonRateThrottle

برای کاربران ناشناس.

---

تنظیم:

```python
"anon": "100/day"
```

---

کاربر بدون Login:

```http
GET /api/books/
```

---

بیش از:

```text
100 Request
```

---

پاسخ:

```http
429 Too Many Requests
```

---

# UserRateThrottle

برای کاربران احراز هویت شده.

---

تنظیم:

```python
"user": "1000/day"
```

---

هر User محدودیت مستقل دارد.

---

مثال:

```text
User A
1000 Request
```

---

```text
User B
1000 Request
```

---

# اعمال Throttle روی View خاص

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.views import (
    APIView
)

from rest_framework.throttling import (
    UserRateThrottle
)
```

---

```python
class BookAPIView(APIView):

    throttle_classes = [
        UserRateThrottle
    ]
```

---

در این حالت:

```text
فقط این View
```

Throttle خواهد داشت.

---

# ساخت Throttle سفارشی

فایل:

```text
MyProject/common/throttles.py
```

---

```python
from rest_framework.throttling import (
    UserRateThrottle
)
```

---

```python
class BookThrottle(
    UserRateThrottle
):

    scope = "books"
```

---

تنظیم:

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_THROTTLE_RATES": {

        "books": "50/hour"
    }
}
```

---

استفاده:

فایل:

```text
MyProject/books/views.py
```

```python
from common.throttles import (
    BookThrottle
)
```

---

```python
class BookAPIView(APIView):

    throttle_classes = [
        BookThrottle
    ]
```

---

نتیجه:

```text
50 Request / hour
```

---

# ScopedRateThrottle

برای Rate Limitهای متفاوت.

---

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.throttling import (
    ScopedRateThrottle
)
```

---

```python
class BookAPIView(APIView):

    throttle_classes = [
        ScopedRateThrottle
    ]

    throttle_scope = "books"
```

---

تنظیم:

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_THROTTLE_RATES": {

        "books": "100/hour"
    }
}
```

---

# چند Scope مختلف

مثال:

```python
REST_FRAMEWORK = {

    "DEFAULT_THROTTLE_RATES": {

        "books": "100/hour",

        "login": "10/hour",

        "register": "5/hour"
    }
}
```

---

سناریو:

```text
Login API
```

محدودتر از:

```text
Book API
```

خواهد بود.

---

# Throttling برای Login

یکی از مهم‌ترین کاربردها.

---

مثال:

فایل:

```text
MyProject/accounts/views.py
```

```python
class LoginAPIView(APIView):

    throttle_classes = [
        ScopedRateThrottle
    ]

    throttle_scope = "login"
```

---

تنظیم:

```python
"login": "10/hour"
```

---

مزیت:

```text
جلوگیری از Brute Force
```

---

# پاسخ هنگام عبور از محدودیت

کد وضعیت:

```http
429 Too Many Requests
```

---

نمونه:

```json
{
    "detail":
        "Request was throttled."
}
```

---

# زمان انتظار

DRF معمولاً Headerهایی ارائه می‌دهد.

نمونه:

```text
Retry-After
```

---

یعنی:

```text
چه زمانی دوباره تلاش شود.
```

---

# Throttling و Cache

نکته بسیار مهم.

---

DRF اطلاعات Throttle را در:

```text
Cache Backend
```

نگهداری می‌کند.

---

اگر Cache نداشته باشید:

```text
LocMemCache
```

استفاده می‌شود.

---

در محیط Multi-Server این موضوع مشکل ایجاد می‌کند.

---

# محدودیت مهم DRF

طبق مستندات رسمی:

```text
Throttleها
برای امنیت قطعی طراحی نشده‌اند.
```

---

دلیل:

شرایط Race Condition.

---

بنابراین:

```text
DRF Throttling
```

برای:

```text
Business Rate Limiting
```

مناسب است.

---

اما برای:

```text
Security Enforcement
```

کافی نیست.

---

# Production Architecture

در پروژه‌های واقعی:

```text
Nginx
    ↓
API Gateway
    ↓
DRF Throttling
```

---

یا:

```text
Cloudflare
    ↓
Nginx
    ↓
DRF
```

---

در این معماری:

لایه‌های مختلف Rate Limit دارند.

---

# مثال واقعی

فرض کنید سامانه پیامک دارید.

API:

```http
POST /api/send-sms/
```

---

Throttle:

```text
5/minute
```

---

مزیت:

```text
جلوگیری از سوءاستفاده
```

---

# مثال Login

```http
POST /api/login/
```

---

Throttle:

```text
10/hour
```

---

مزیت:

```text
کاهش حملات Password Guessing
```

---

# مثال Search

```http
GET /api/books/?search=django
```

---

Throttle:

```text
100/minute
```

---

جلوگیری از:

```text
Database Abuse
```

---

# خطاهای رایج

## فراموش کردن Cache

باعث رفتار غیرمنتظره در Multi Instance می‌شود.

---

## Rate بسیار کم

مثال:

```python
"books": "1/hour"
```

---

تجربه کاربری بد.

---

## Rate بسیار زیاد

مثال:

```python
"books": "100000/hour"
```

---

عملاً بی‌فایده.

---

## استفاده از DRF به عنوان تنها لایه امنیتی

اشتباه معماری.

---

# نکته DevOps

برای محیط Production:

پیشنهاد:

```text
Redis Cache
```

---

به جای:

```text
LocMemCache
```

---

دلیل:

```text
چند سرور
یک وضعیت مشترک
```

---

فایل:

```text
MyProject/config/settings.py
```

نمونه:

```python
CACHES = {

    "default": {

        "BACKEND":
            "django.core.cache.backends.redis.RedisCache",

        "LOCATION":
            "redis://redis:6379/1",
    }
}
```

---

# Best Practices

1. Login API را Throttle کنید.
2. Register API را Throttle کنید.
3. Search API را Throttle کنید.
4. از ScopedRateThrottle استفاده کنید.
5. در Production از Redis استفاده کنید.
6. DRF Throttling را تنها لایه دفاعی قرار ندهید.
7. برای Multi-Instance از Cache مشترک استفاده کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Throttling چیست.
* تفاوت آن با Authentication و Permission چیست.
* AnonRateThrottle چیست.
* UserRateThrottle چیست.
* ScopedRateThrottle چیست.
* چگونه Throttle سفارشی بسازیم.
* نقش Cache در Throttling چیست.
* محدودیت‌های Throttling در DRF چیست.
* معماری مناسب Production چگونه است.

فصل بعدی:

```text
11 - Caching
```

---

## منابع رسمی

* Throttling

[DRF Throttling Documentation](https://www.django-rest-framework.org/api-guide/throttling/?utm_source=chatgpt.com)

