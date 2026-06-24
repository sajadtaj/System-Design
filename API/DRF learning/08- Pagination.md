# 08 - Pagination

## اهداف فصل

در پایان این فصل:

* مفهوم Pagination را درک می‌کنید.
* دلیل استفاده از Pagination را می‌فهمید.
* Pagination پیش‌فرض DRF را پیاده‌سازی می‌کنید.
* انواع Pagination در DRF را می‌شناسید.
* Custom Pagination می‌نویسید.
* نکات Performance مربوط به Pagination را یاد می‌گیرید.

---

# مقدمه

فرض کنید جدول کتاب‌ها دارای:

```text
1,000,000 Records
```

باشد.

API زیر:

```http
GET /api/books/
```

اگر تمام داده‌ها را برگرداند:

```text
1,000,000 JSON Objects
```

تولید خواهد شد.

---

نتیجه:

* مصرف RAM زیاد
* افزایش زمان Response
* فشار روی Database
* مصرف بالای پهنای باند
* تجربه کاربری ضعیف

---

برای حل این مشکل از Pagination استفاده می‌کنیم.

---

# Pagination چیست؟

Pagination یعنی:

```text
تقسیم نتایج بزرگ
به صفحات کوچک‌تر
```

---

مثال:

به جای:

```text
1000000 Record
```

ارسال می‌کنیم:

```text
Page 1
20 Record
```

---

سپس:

```text
Page 2
20 Record
```

---

و به همین ترتیب.

---

# معماری Pagination

```text
Database
    ↓
QuerySet
    ↓
Pagination
    ↓
Serializer
    ↓
Response
```

---

# بدون Pagination

درخواست:

```http
GET /api/books/
```

---

پاسخ:

```json
[
  {...},
  {...},
  {...},
  ...
]
```

ممکن است هزاران رکورد باشد.

---

# با Pagination

درخواست:

```http
GET /api/books/
```

---

پاسخ:

```json
{
    "count": 1000,
    "next": "...",
    "previous": null,
    "results": [
        {...},
        {...}
    ]
}
```

---

اکنون فقط بخشی از داده‌ها بازگردانده می‌شود.

---

# فعال‌سازی Pagination سراسری

فایل:

```text
MyProject/config/settings.py
```

---

تنظیم:

```python
REST_FRAMEWORK = {

    "DEFAULT_PAGINATION_CLASS":

        "rest_framework.pagination.PageNumberPagination",

    "PAGE_SIZE": 20,
}
```

---

نتیجه:

تمام Viewهای List:

```python
ListAPIView

ModelViewSet
```

به صورت خودکار Pagination خواهند داشت.

---

# PageNumberPagination

رایج‌ترین نوع Pagination.

---

درخواست:

```http
GET /api/books/?page=1
```

---

صفحه دوم:

```http
GET /api/books/?page=2
```

---

صفحه سوم:

```http
GET /api/books/?page=3
```

---

# پاسخ

```json
{
    "count": 150,

    "next":
        "http://localhost:8000/api/books/?page=2",

    "previous": null,

    "results": [
        ...
    ]
}
```

---

# اجزای پاسخ

## count

تعداد کل رکوردها.

---

مثال:

```json
"count": 150
```

---

## next

لینک صفحه بعد.

---

مثال:

```json
"next":
"http://localhost:8000/api/books/?page=2"
```

---

## previous

لینک صفحه قبل.

---

مثال:

```json
"previous":
"http://localhost:8000/api/books/?page=1"
```

---

## results

داده‌های واقعی.

---

مثال:

```json
"results": [
    ...
]
```

---

# تنظیم تعداد رکورد هر صفحه

فایل:

```text
MyProject/config/settings.py
```

```python
PAGE_SIZE = 50
```

---

نتیجه:

```text
هر صفحه
50 رکورد
```

---

# Pagination سفارشی

گاهی باید کنترل بیشتری داشته باشیم.

---

فایل:

```text
MyProject/common/pagination.py
```

```python
from rest_framework.pagination import (
    PageNumberPagination
)
```

---

کلاس:

```python
class StandardPagination(
    PageNumberPagination
):

    page_size = 20
```

---

استفاده:

فایل:

```text
MyProject/books/views.py
```

```python
class BookViewSet(
    ModelViewSet
):

    queryset = Book.objects.all()

    serializer_class = (
        BookSerializer
    )

    pagination_class = (
        StandardPagination
    )
```

---

# page_size_query_param

اجازه تغییر سایز صفحه توسط کاربر.

فایل:

```text
MyProject/common/pagination.py
```

```python
class StandardPagination(
    PageNumberPagination
):

    page_size = 20

    page_size_query_param = (
        "page_size"
    )
```

---

درخواست:

```http
GET /api/books/?page_size=50
```

---

نتیجه:

```text
50 رکورد
```

---

# max_page_size

برای جلوگیری از سوءاستفاده.

---

فایل:

```text
MyProject/common/pagination.py
```

```python
class StandardPagination(
    PageNumberPagination
):

    page_size = 20

    page_size_query_param = (
        "page_size"
    )

    max_page_size = 100
```

---

اگر کاربر ارسال کند:

```http
GET /api/books/?page_size=10000
```

---

حداکثر:

```text
100
```

اعمال می‌شود.

---

# LimitOffsetPagination

مدل محبوب در سیستم‌های دیتابیسی.

---

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_PAGINATION_CLASS":

        "rest_framework.pagination.LimitOffsetPagination",

    "PAGE_SIZE": 20,
}
```

---

درخواست:

```http
GET /api/books/?limit=20&offset=0
```

---

صفحه بعد:

```http
GET /api/books/?limit=20&offset=20
```

---

صفحه سوم:

```http
GET /api/books/?limit=20&offset=40
```

---

# مفهوم Limit

```text
چند رکورد
```

---

مثال:

```http
limit=20
```

---

# مفهوم Offset

```text
از کدام رکورد شروع شود
```

---

مثال:

```http
offset=40
```

---

# CursorPagination

پیشرفته‌ترین Pagination در DRF.

---

مناسب:

```text
Large Dataset

Real-Time Data

Infinite Scroll
```

---

فعال‌سازی:

```python
REST_FRAMEWORK = {

    "DEFAULT_PAGINATION_CLASS":

        "rest_framework.pagination.CursorPagination"
}
```

---

یا به صورت سفارشی:

فایل:

```text
MyProject/common/pagination.py
```

```python
from rest_framework.pagination import (
    CursorPagination
)
```

---

```python
class BookCursorPagination(
    CursorPagination
):

    page_size = 20

    ordering = "-id"
```

---

# مزیت CursorPagination

در دیتاست‌های بزرگ:

```text
Offset Pagination
```

کند می‌شود.

---

اما:

```text
Cursor Pagination
```

عملکرد بهتری دارد.

---

# مقایسه انواع Pagination

| نوع         | سادگی  | Performance | کاربرد          |
| ----------- | ------ | ----------- | --------------- |
| PageNumber  | زیاد   | خوب         | اکثر پروژه‌ها   |
| LimitOffset | متوسط  | خوب         | APIهای عمومی    |
| Cursor      | پیچیده | عالی        | دیتاست‌های بزرگ |

---

# Pagination و Filtering

این دو معمولاً با هم استفاده می‌شوند.

---

مثال:

```http
GET /api/books/?author=ali&page=2
```

---

ترتیب اجرا:

```text
Filtering
    ↓
Ordering
    ↓
Pagination
    ↓
Response
```

---

# Pagination و Ordering

مثال:

```http
GET /api/books/?ordering=-year&page=3
```

---

ابتدا:

```text
Sorting
```

انجام می‌شود.

سپس:

```text
Pagination
```

---

# نکته بسیار مهم

برای Pagination پایدار:

```python
queryset.order_by("id")
```

یا:

```python
ordering = ["id"]
```

استفاده کنید.

---

در غیر این صورت:

```text
صفحات مختلف
ممکن است داده‌های تکراری
یا گمشده داشته باشند.
```

---

# Performance

در پروژه‌های بزرگ:

اشتباه:

```python
Book.objects.all()
```

بدون Pagination.

---

صحیح:

```python
Book.objects.all()
```

به همراه:

```python
pagination
```

---

# نکته Database Manager

برای فیلدهای Ordering:

```sql
INDEX
```

ایجاد کنید.

---

مثال:

فایل:

```text
MyProject/books/models.py
```

```python
class Book(models.Model):

    created_at = (
        models.DateTimeField(
            db_index=True
        )
    )
```

---

# خطاهای رایج

## page_size بسیار بزرگ

اشتباه:

```http
?page_size=10000
```

---

## عدم استفاده از max_page_size

باعث فشار روی سیستم می‌شود.

---

## CursorPagination بدون ordering

خطا:

```text
CursorPagination requires ordering
```

---

## Pagination در Serializer

اشتباه معماری.

Pagination باید در View Layer انجام شود.

---

# Best Practices

1. همیشه Pagination فعال باشد.
2. برای APIهای عمومی از Pagination استفاده کنید.
3. از max_page_size استفاده کنید.
4. روی فیلدهای Ordering ایندکس ایجاد کنید.
5. Filtering و Pagination را با هم ترکیب کنید.
6. برای دیتاست‌های بسیار بزرگ CursorPagination را بررسی کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Pagination چیست.
* چرا استفاده از آن ضروری است.
* PageNumberPagination چگونه کار می‌کند.
* LimitOffsetPagination چیست.
* CursorPagination چیست.
* Pagination سفارشی چگونه ساخته می‌شود.
* نکات Performance مربوط به Pagination چیست.

فصل بعدی:

```text
09 - Versioning
```

---

## منابع رسمی

* Pagination

[DRF Pagination Documentation](https://www.django-rest-framework.org/api-guide/pagination/?utm_source=chatgpt.com)

