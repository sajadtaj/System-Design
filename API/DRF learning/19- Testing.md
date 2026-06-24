# 19 - Testing

## اهداف فصل

در پایان این فصل:

* اهمیت تست در پروژه‌های DRF را درک می‌کنید.
* با `APITestCase` آشنا می‌شوید.
* از `APIClient` استفاده می‌کنید.
* Serializerها را تست می‌کنید.
* Endpointها را تست می‌کنید.
* Authentication و Permission را تست می‌کنید.
* با `force_authenticate()` آشنا می‌شوید.
* می‌دانید چه چیزهایی ارزش تست کردن دارند.

---

# Testing چیست؟

Testing یعنی:

```text id="t1"
بررسی خودکار
درست کار کردن برنامه
```

---

هدف تست:

```text id="t2"
کشف خطا
قبل از رسیدن به Production
```

است.

---

# چرا تست مهم است؟

فرض کنید امروز API زیر را توسعه می‌دهید:

فایل:

```text id="t3"
MyProject/books/views.py
```

```python
class BookListAPIView(
    ListAPIView
):
    ...
```

---

همه چیز درست کار می‌کند.

---

دو ماه بعد:

تغییری در Serializer انجام می‌دهید.

---

اکنون:

```text id="t4"
Pagination
```

یا:

```text id="t5"
Filtering
```

خراب می‌شود.

---

تست‌ها این مشکل را قبل از انتشار پیدا می‌کنند.

---

# ساختار تست

پیشنهاد:

```text
MyProject/books/

├── tests/
│
├── test_serializers.py
├── test_views.py
├── test_permissions.py
├── test_authentication.py
```

---

در پروژه‌های بزرگ:

```text
tests/
```

را جدی بگیرید.

---

# APITestCase

کلاس اصلی تست در DRF.

---

فایل:

```text
MyProject/books/tests/test_views.py
```

```python
from rest_framework.test import (
    APITestCase
)
```

---

```python
class BookAPITestCase(
    APITestCase
):
    pass
```

---

# APIClient

کلاینت تست DRF.

---

این ابزار درخواست HTTP شبیه‌سازی می‌کند.

---

```python
response = self.client.get(
    "/api/books/"
)
```

---

# تست GET

فایل:

```text
MyProject/books/tests/test_views.py
```

```python
from rest_framework import status
```

---

```python
class BookListTest(
    APITestCase
):

    def test_book_list_returns_200(
        self
    ):

        response = self.client.get(
            "/api/books/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
```

---

# تست POST

```python
response = self.client.post(
    "/api/books/",
    {
        "title": "DRF"
    }
)
```

---

```python
self.assertEqual(
    response.status_code,
    status.HTTP_201_CREATED
)
```

---

# تست Serializer

فایل:

```text
MyProject/books/tests/test_serializers.py
```

---

```python
from books.serializers import (
    BookSerializer
)
```

---

```python
class BookSerializerTest(
    APITestCase
):

    def test_serializer_valid(
        self
    ):

        serializer = (
            BookSerializer(
                data={
                    "title": "DRF"
                }
            )
        )

        self.assertTrue(
            serializer.is_valid()
        )
```

---

# تست Validation

```python
serializer = BookSerializer(
    data={
        "title": ""
    }
)
```

---

```python
self.assertFalse(
    serializer.is_valid()
)
```

---

# ساخت داده تست

معمولاً در:

```python
def setUp(
    self
):
```

انجام می‌شود.

---

```python
def setUp(self):

    self.book = Book.objects.create(
        title="DRF"
    )
```

---

قبل از هر تست اجرا می‌شود.

---

# تست Authentication

فایل:

```text
MyProject/accounts/tests/test_authentication.py
```

---

مثال:

```python
response = self.client.get(
    "/api/profile/"
)
```

---

```python
self.assertEqual(
    response.status_code,
    401
)
```

---

# ساخت User

```python
from django.contrib.auth import (
    get_user_model
)
```

---

```python
User = get_user_model()
```

---

```python
self.user = User.objects.create_user(
    username="test",
    password="123456"
)
```

---

# Login در تست

```python
self.client.force_login(
    self.user
)
```

---

اکنون درخواست‌ها با این کاربر ارسال می‌شوند.

---

# force_authenticate

ابزار اختصاصی DRF.

---

```python
from rest_framework.test import (
    APIClient
)
```

---

```python
client = APIClient()

client.force_authenticate(
    user=self.user
)
```

---

اکنون:

```python
client.get(...)
```

با کاربر لاگین‌شده اجرا می‌شود.

---

# تست Permission

مثال:

```python
response = self.client.get(
    "/api/admin-panel/"
)
```

---

انتظار:

```python
self.assertEqual(
    response.status_code,
    403
)
```

---

اگر Permission درست کار کند:

```text
403 Forbidden
```

دریافت می‌شود.

---

# تست JWT

در فصل 06.1 دیدیم:

```http
/api/token/
```

---

در تست:

```python
response = self.client.post(
    "/api/token/",
    {
        "username": "test",
        "password": "123456"
    }
)
```

---

```python
access_token = (
    response.data["access"]
)
```

---

استفاده:

```python
self.client.credentials(
    HTTP_AUTHORIZATION=
        f"Bearer {access_token}"
)
```

---

اکنون درخواست‌ها با JWT ارسال می‌شوند.

---

# تست Pagination

مثال:

```python
response = self.client.get(
    "/api/books/"
)
```

---

بررسی:

```python
self.assertIn(
    "results",
    response.data
)
```

---

یا:

```python
self.assertIn(
    "count",
    response.data
)
```

---

# تست Filtering

مثال:

```python
response = self.client.get(
    "/api/books/?title=django"
)
```

---

بررسی:

```python
self.assertEqual(
    response.status_code,
    200
)
```

---

و:

```python
len(response.data)
```

---

# تست Exception

مثال:

```python
response = self.client.get(
    "/api/books/999999/"
)
```

---

انتظار:

```python
self.assertEqual(
    response.status_code,
    404
)
```

---

# اجرای تست‌ها

کل پروژه:

```bash
python manage.py test
```

---

یک App:

```bash
python manage.py test books
```

---

یک فایل:

```bash
python manage.py test \
books.tests.test_views
```

---

# چه چیزهایی را تست کنیم؟

حتماً تست شوند:

```text
Serializer Validation

Authentication

Permission

Business Rules

Critical API Endpoints

Custom Exceptions
```

---

# چه چیزهایی معمولاً ارزش تست ندارند؟

مگر منطق خاصی داشته باشند:

```text
Model __str__

Admin Configuration

Simple CRUD بدون منطق خاص
```

---

# خطاهای رایج

## تست نکردن Permission

یکی از رایج‌ترین مشکلات امنیتی.

---

## تست نکردن Validation

باعث ورود داده نامعتبر می‌شود.

---

## تست فقط مسیر موفق

همیشه سناریوهای خطا را نیز تست کنید.

---

مثال:

```text
200
400
401
403
404
```

---

# Best Practices

1. تست‌ها را کنار کد توسعه دهید.
2. Authentication را تست کنید.
3. Permission را تست کنید.
4. Validation را تست کنید.
5. سناریوهای خطا را تست کنید.
6. تست‌های کوچک و خوانا بنویسید.
7. روی Business Logic تمرکز کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Testing چیست.
* APITestCase چیست.
* APIClient چیست.
* چگونه Endpointها را تست کنیم.
* چگونه Serializerها را تست کنیم.
* چگونه JWT را تست کنیم.
* چگونه Permission را تست کنیم.
* چه بخش‌هایی ارزش تست کردن دارند.

---

# نکته مهم برای پروژه‌های واقعی

در اکثر پروژه‌های DRF، بیشترین بازگشت سرمایه تست روی این بخش‌هاست:

```text
Authentication

Permissions

Serializer Validation

Business Logic

Critical API Flows
```

اگر زمان محدودی دارید، ابتدا این بخش‌ها را پوشش دهید.

---

فصل بعدی و پایانی:

```text
20 - Production Architecture
```

---

## منابع رسمی

* Testing

[DRF Testing Documentation](https://www.django-rest-framework.org/api-guide/testing/?utm_source=chatgpt.com)

