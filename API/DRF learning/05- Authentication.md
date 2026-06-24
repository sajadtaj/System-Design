قبل از رفتن به فصل 05 یک نکته مهم وجود دارد.

ترتیبی که ابتدا تعریف کرده بودیم:

```text
05- Authentication
06- Permissions
```

از نظر مستندات رسمی درست است، اما از نظر آموزش عملی یک نقص دارد:

کاربر هنوز نمی‌داند:

* User در DRF چگونه در Request قرار می‌گیرد.
* Session چیست.
* Token چیست.
* چرا اصلاً Authentication لازم است.

بنابراین فصل 05 باید با معماری شروع شود و نباید مستقیماً وارد Token Authentication شود.

---

# 05 - Authentication

## اهداف فصل

در پایان این فصل:

* مفهوم Authentication را درک می‌کنید.
* تفاوت Authentication و Authorization را می‌شناسید.
* با Session Authentication آشنا می‌شوید.
* با Basic Authentication آشنا می‌شوید.
* با Token Authentication آشنا می‌شوید.
* نحوه شناسایی کاربر در DRF را یاد می‌گیرید.
* Authentication را روی ViewSet و Generic Views اعمال می‌کنید.

---

# مقدمه

تا اینجا APIهای ما برای همه کاربران قابل دسترس بودند.

هر شخصی می‌توانست:

```http
GET /api/books/
POST /api/books/
DELETE /api/books/1/
```

را اجرا کند.

در پروژه واقعی چنین چیزی قابل قبول نیست.

قبل از اینکه بتوانیم دسترسی کاربران را کنترل کنیم باید بدانیم:

```text
این درخواست توسط چه کسی ارسال شده است؟
```

وظیفه پاسخ به این سؤال بر عهده Authentication است.

---

# Authentication چیست؟

Authentication یعنی:

```text
اثبات هویت کاربر
```

سیستم بررسی می‌کند:

```text
شما چه کسی هستید؟
```

---

مثال دنیای واقعی:

ورود به حساب بانکی

```text
نام کاربری
+
رمز عبور
↓
احراز هویت
```

---

در DRF نیز دقیقاً همین اتفاق رخ می‌دهد.

---

# Authentication و Authorization

بسیاری از توسعه‌دهندگان این دو مفهوم را اشتباه می‌گیرند.

---

## Authentication

```text
Who are you?
```

شما چه کسی هستید؟

---

## Authorization

```text
What can you do?
```

چه کاری مجاز هستید انجام دهید؟

---

مثال:

```text
کاربر وارد سیستم شد
↓
Authentication

کاربر می‌تواند حذف انجام دهد؟
↓
Authorization
```

---

# جایگاه Authentication در معماری DRF

```text
Request
    ↓
Authentication
    ↓
request.user
    ↓
Permission
    ↓
View
```

---

پس از احراز هویت:

```python
request.user
```

مقداردهی می‌شود.

---

# Anonymous User

اگر کاربر احراز هویت نشده باشد:

```python
request.user
```

برابر است با:

```python
AnonymousUser
```

---

مثال:

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.views import APIView
from rest_framework.response import Response


class CurrentUserAPIView(APIView):

    def get(self, request):

        return Response({
            "user": str(request.user)
        })
```

---

# Authentication های موجود در DRF

DRF چند مکانیزم اصلی ارائه می‌دهد:

```text
SessionAuthentication

BasicAuthentication

TokenAuthentication
```

---

# Session Authentication

مکانیزم پیش‌فرض Django.

کاربر:

```text
Login
↓
Session
↓
Cookie
↓
Request
```

---

معمولاً برای:

* Django Admin
* Template Rendering
* پروژه‌های سنتی Django

استفاده می‌شود.

---

# فعال‌سازی Session Authentication

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication"
    ]
}
```

---

# Basic Authentication

در هر درخواست:

```text
username
password
```

ارسال می‌شود.

---

نمونه Header:

```http
Authorization: Basic XXXXXXXXX
```

---

تنظیمات:

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication"
    ]
}
```

---

# مشکلات Basic Authentication

در پروژه‌های Production به ندرت استفاده می‌شود.

زیرا:

```text
در هر درخواست
نام کاربری و رمز عبور
ارسال می‌شود.
```

---

# Token Authentication

امروزه رایج‌ترین مدل کلاسیک DRF.

فرآیند:

```text
Login
    ↓
Token
    ↓
Client
    ↓
Authorization Header
```

---

# نصب Token Authentication

فایل:

```text
MyProject/config/settings.py
```

```python
INSTALLED_APPS = [
    ...
    "rest_framework.authtoken"
]
```

---

Migration:

```bash
python manage.py migrate
```

---

# فعال‌سازی Token Authentication

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication"
    ]
}
```

---

# ساخت Token

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.authtoken.models import Token

token = Token.objects.create(
    user=user
)
```

---

# دریافت Token

فایل:

```text
MyProject/config/urls.py
```

```python
from rest_framework.authtoken.views import (
    obtain_auth_token
)

urlpatterns = [
    path(
        "api/token/",
        obtain_auth_token
    )
]
```

---

درخواست:

```http
POST /api/token/
```

Body:

```json
{
    "username": "admin",
    "password": "123456"
}
```

---

پاسخ:

```json
{
    "token": "xxxxxxxxxxxxxxxx"
}
```

---

# استفاده از Token

در تمام درخواست‌ها:

```http
Authorization: Token xxxxxxxxxxxxx
```

---

# اعمال Authentication روی View

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.authentication import (
    TokenAuthentication
)

from rest_framework.views import APIView


class BookAPIView(APIView):

    authentication_classes = [
        TokenAuthentication
    ]
```

---

# اعمال Authentication روی ViewSet

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.authentication import (
    TokenAuthentication
)

from rest_framework.viewsets import (
    ModelViewSet
)


class BookViewSet(ModelViewSet):

    authentication_classes = [
        TokenAuthentication
    ]
```

---

# تنظیم سراسری Authentication

به جای تعریف روی همه Viewها:

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES": [

        "rest_framework.authentication.TokenAuthentication"
    ]
}
```

---

# خطاهای رایج

## فراموش کردن Header

خطا:

```http
401 Unauthorized
```

---

## فراموش کردن migrate

خطا:

```text
authtoken_token does not exist
```

---

## اشتباه در فرمت Header

اشتباه:

```http
Authorization: Bearer xxxxx
```

برای TokenAuthentication کلاسیک.

---

صحیح:

```http
Authorization: Token xxxxx
```

---

# Authentication در پروژه‌های مدرن

امروزه بیشتر پروژه‌های:

* Flutter
* React
* Vue

به جای Token Authentication از JWT استفاده می‌کنند.

اما برای درک DRF ابتدا باید Token Authentication را یاد بگیریم.

در انتهای فصل‌های امنیتی JWT را نیز بررسی خواهیم کرد.

---

# Best Practices

1. Authentication را به صورت سراسری تنظیم کنید.
2. از HTTPS استفاده کنید.
3. Tokenها را در لاگ ذخیره نکنید.
4. Authentication را از Permission جدا نگه دارید.
5. برای SPA و Mobile استفاده از JWT را بررسی کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Authentication چیست.
* تفاوت آن با Authorization چیست.
* Session Authentication چگونه کار می‌کند.
* Basic Authentication چیست.
* Token Authentication چیست.
* چگونه Authentication را روی Viewها اعمال کنیم.

در فصل بعد یاد می‌گیریم که پس از شناسایی کاربر، چگونه سطح دسترسی او را کنترل کنیم.

## منابع رسمی

* Authentication
* SessionAuthentication
* BasicAuthentication
* TokenAuthentication

[https://www.django-rest-framework.org/api-guide/authentication/](https://www.django-rest-framework.org/api-guide/authentication/)

نکته بازبینی برای نسخه نهایی کتاب: در انتهای فصل 06 (Permissions)، یک ضمیمه با عنوان «JWT در پروژه‌های Flutter و React» اضافه شود؛ زیرا JWT در مستندات رسمی DRF نیست و معمولاً با پکیج‌های جانبی مانند `djangorestframework-simplejwt` پیاده‌سازی می‌شود.

