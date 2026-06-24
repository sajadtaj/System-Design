# 06 - Permissions

## اهداف فصل

در پایان این فصل:

* مفهوم Permission را در DRF درک می‌کنید.
* تفاوت Authentication و Permission را می‌شناسید.
* با Permissionهای داخلی DRF آشنا می‌شوید.
* Permission را روی APIView و ViewSet اعمال می‌کنید.
* Permission سفارشی می‌نویسید.
* کنترل دسترسی در سطح رکورد (Object Level Permission) را یاد می‌گیرید.

---

# مقدمه

در فصل قبل Authentication را بررسی کردیم.

Authentication فقط به این سؤال پاسخ می‌دهد:

```text
این کاربر چه کسی است؟
```

اما هنوز یک سؤال مهم باقی مانده است:

```text
آیا این کاربر مجاز به انجام این عملیات است؟
```

پاسخ این سؤال توسط Permission مشخص می‌شود.

---

# Permission چیست؟

Permission یا مجوز دسترسی تعیین می‌کند:

```text
این کاربر چه کاری می‌تواند انجام دهد؟
```

مثال:

```text
کاربر وارد سیستم شده است
          ↓
Authentication
          ↓
request.user
          ↓
Permissions
          ↓
اجازه یا عدم اجازه دسترسی
```

---

# تفاوت Authentication و Permission

## Authentication

```text
Who are you?
```

شما چه کسی هستید؟

---

## Permission

```text
What are you allowed to do?
```

مجاز به انجام چه کاری هستید؟

---

مثال:

```text
کاربر admin
       ↓
Authentication

کاربر می‌خواهد کتابی را حذف کند
       ↓
Permission
```

---

# جایگاه Permission در معماری DRF

```text
Request
    ↓
Authentication
    ↓
request.user
    ↓
Permissions
    ↓
View
    ↓
Response
```

اگر Permission رد شود:

```http
403 Forbidden
```

برگردانده می‌شود.

---

# Permissionهای آماده DRF

DRF چند Permission آماده ارائه می‌کند:

```python
AllowAny

IsAuthenticated

IsAdminUser

IsAuthenticatedOrReadOnly

DjangoModelPermissions

DjangoObjectPermissions
```

---

# AllowAny

اجازه دسترسی به همه کاربران.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.permissions import (
    AllowAny
)

from rest_framework.views import APIView


class PublicAPIView(APIView):

    permission_classes = [
        AllowAny
    ]
```

---

کاربر:

* لاگین کرده باشد
* لاگین نکرده باشد

فرقی ندارد.

---

# IsAuthenticated

فقط کاربران احراز هویت شده.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.views import APIView


class PrivateAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]
```

---

اگر Token معتبر وجود نداشته باشد:

```http
401 Unauthorized
```

---

# IsAdminUser

فقط کاربران Staff.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.permissions import (
    IsAdminUser
)


class AdminAPIView(APIView):

    permission_classes = [
        IsAdminUser
    ]
```

---

شرط:

```python
request.user.is_staff == True
```

---

# IsAuthenticatedOrReadOnly

یکی از پرکاربردترین Permissionها.

سناریو:

```text
همه بتوانند مشاهده کنند

فقط کاربران لاگین کرده
بتوانند تغییر ایجاد کنند
```

---

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)

from rest_framework.viewsets import (
    ModelViewSet
)


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]
```

---

نتیجه:

```http
GET     مجاز

POST    نیازمند Login

PUT     نیازمند Login

PATCH   نیازمند Login

DELETE  نیازمند Login
```

---

# اعمال Permission روی ViewSet

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.viewsets import (
    ModelViewSet
)


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [
        IsAuthenticated
    ]
```

---

# اعمال Permission روی APIView

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.views import (
    APIView
)


class UserProfileAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]
```

---

# تنظیم سراسری Permission

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_PERMISSION_CLASSES": [

        "rest_framework.permissions.IsAuthenticated"
    ]
}
```

---

در این حالت همه APIها نیازمند Login خواهند بود.

---

# Permission سفارشی

گاهی Permissionهای آماده کافی نیستند.

مثال:

```text
فقط مدیر سیستم
اجازه حذف کتاب را داشته باشد
```

---

فایل:

```text
MyProject/books/permissions.py
```

```python
from rest_framework.permissions import (
    BasePermission
)


class IsLibraryManager(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return request.user.is_staff
```

---

استفاده:

فایل:

```text
MyProject/books/views.py
```

```python
from .permissions import (
    IsLibraryManager
)


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [
        IsLibraryManager
    ]
```

---

# Object Level Permission چیست؟

گاهی دسترسی وابسته به رکورد است.

مثال:

```text
هر کاربر
فقط بتواند کتاب‌های خودش را ویرایش کند.
```

---

مدل:

فایل:

```text
MyProject/books/models.py
```

```python
from django.contrib.auth.models import User


class Book(models.Model):

    title = models.CharField(
        max_length=200
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
```

---

Permission:

فایل:

```text
MyProject/books/permissions.py
```

```python
from rest_framework.permissions import (
    BasePermission
)


class IsOwnerPermission(
    BasePermission
):

    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        return obj.owner == request.user
```

---

استفاده:

فایل:

```text
MyProject/books/views.py
```

```python
class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [
        IsOwnerPermission
    ]
```

---

# ترکیب چند Permission

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)


class AdminBookViewSet(
    ModelViewSet
):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminUser
    ]
```

---

همه Permissionها باید True برگردانند.

---

# DjangoModelPermissions

اتصال Permissionها به سیستم Permission داخلی Django.

مثال:

```python
add_book

change_book

delete_book

view_book
```

---

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.permissions import (
    DjangoModelPermissions
)


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [
        DjangoModelPermissions
    ]
```

---

# DjangoObjectPermissions

نسخه پیشرفته‌تر.

دسترسی در سطح رکورد.

معمولاً همراه پکیج‌هایی مانند:

```text
django-guardian
```

استفاده می‌شود.

---

# خطاهای رایج

## اشتباه گرفتن Authentication و Permission

بسیار رایج است.

```text
Authentication
↓
شناسایی کاربر

Permission
↓
کنترل دسترسی
```

---

## فراموش کردن Permission

نتیجه:

```text
API عمومی می‌شود.
```

---

## قراردادن Business Logic داخل Permission

اشتباه:

```text
محاسبات مالی

ارسال پیامک

ثبت لاگ
```

Permission فقط باید درباره مجاز بودن یا نبودن تصمیم بگیرد.

---

## استفاده از IsAdminUser به جای Permission اختصاصی

در پروژه‌های بزرگ معمولاً Permission اختصاصی مناسب‌تر است.

---

# Best Practices

1. Authentication و Permission را از هم جدا نگه دارید.
2. از Permissionهای آماده DRF استفاده کنید.
3. Permissionهای پیچیده را در فایل مستقل بنویسید.
4. Permissionها را داخل permissions.py قرار دهید.
5. از Object Level Permission برای مالکیت داده استفاده کنید.
6. منطق تجاری را داخل Permission قرار ندهید.
7. Permissionهای سراسری را در settings.py مدیریت کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Permission چیست.
* تفاوت آن با Authentication چیست.
* چگونه Permission روی APIها اعمال می‌شود.
* Permission سفارشی چگونه نوشته می‌شود.
* Object Level Permission چیست.
* چگونه دسترسی کاربران را کنترل کنیم.

---

```text
Authentication = شناسایی هویت

Authorization = تصمیم‌گیری درباره سطح دسترسی

Permissions = مکانیزم DRF برای پیاده‌سازی Authorization
```

چون بسیاری از توسعه‌دهندگان تازه‌کار اشتباه می‌نویسند:

```text
Permission = Authorization
```

در حالی که از نظر معماری:

```text
Authorization
    ├── Permissions
    ├── Roles
    ├── ACL
    ├── RBAC
    └── Policy Engines
```

و Permission فقط یکی از روش‌های پیاده‌سازی Authorization است.

---

فصل بعدی:

```text
06.1 - JWT Authentication (Advanced)
```

در این فصل Token Authentication کلاسیک را با JWT مقایسه می‌کنیم و یک سیستم احراز هویت مدرن مبتنی بر Access Token و Refresh Token پیاده‌سازی خواهیم کرد.

## منابع رسمی

* Permissions
* AllowAny
* IsAuthenticated
* IsAdminUser
* IsAuthenticatedOrReadOnly
* DjangoModelPermissions
* DjangoObjectPermissions

https://www.django-rest-framework.org/api-guide/permissions/

