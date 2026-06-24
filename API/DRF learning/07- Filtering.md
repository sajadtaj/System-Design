# 07 - Filtering

## اهداف فصل

در پایان این فصل:

* مفهوم Filtering را در DRF درک می‌کنید.
* Query Parameterها را برای فیلتر داده‌ها استفاده می‌کنید.
* `get_queryset()` را برای فیلترسازی سفارشی پیاده‌سازی می‌کنید.
* با `DjangoFilterBackend` آشنا می‌شوید.
* Search و Ordering را پیاده‌سازی می‌کنید.
* خطاهای رایج Filtering را می‌شناسید.

---

# مقدمه

فرض کنید 100,000 کتاب در سیستم وجود دارد.

API زیر:

```http
GET /api/books/
```

تمام رکوردها را برمی‌گرداند.

اما کاربر معمولاً همه داده‌ها را نمی‌خواهد.

مثلاً فقط:

```text
کتاب‌های منتشر شده در سال 2025
```

یا:

```text
کتاب‌های نویسنده خاص
```

یا:

```text
کتاب‌هایی که نام آن‌ها شامل Django است
```

Filtering برای حل این مسئله استفاده می‌شود.

---

# Filtering چیست؟

Filtering یعنی:

```text
محدود کردن نتایج Query
بر اساس شرایط مشخص
```

مثال:

```http
GET /api/books/?author=ali
```

---

# محل انجام Filtering

معماری:

```text
Request
   ↓
Query Parameters
   ↓
Filtering
   ↓
QuerySet
   ↓
Serializer
   ↓
Response
```

---

# روش اول: Override کردن get_queryset

ساده‌ترین روش.

مدل:

فایل:

```text
MyProject/books/models.py
```

```python
from django.db import models


class Book(models.Model):

    title = models.CharField(
        max_length=255
    )

    author = models.CharField(
        max_length=255
    )

    year = models.IntegerField()
```

---

ViewSet:

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.viewsets import (
    ModelViewSet
)

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):

    serializer_class = BookSerializer

    def get_queryset(self):

        queryset = Book.objects.all()

        author = self.request.query_params.get(
            "author"
        )

        if author:
            queryset = queryset.filter(
                author=author
            )

        return queryset
```

---

درخواست:

```http
GET /api/books/?author=ali
```

---

# فیلتر بر اساس چند فیلد

فایل:

```text
MyProject/books/views.py
```

```python
def get_queryset(self):

    queryset = Book.objects.all()

    author = self.request.query_params.get(
        "author"
    )

    year = self.request.query_params.get(
        "year"
    )

    if author:
        queryset = queryset.filter(
            author=author
        )

    if year:
        queryset = queryset.filter(
            year=year
        )

    return queryset
```

---

مثال:

```http
GET /api/books/?author=ali&year=2025
```

---

# چرا get_queryset مهم است؟

مزایا:

* انعطاف بالا
* مناسب Business Logic
* کنترل کامل Query

---

معایب:

* با زیاد شدن فیلترها پیچیده می‌شود.
* نگهداری سخت‌تر می‌شود.

---

# DjangoFilterBackend

برای پروژه‌های واقعی معمولاً از:

```python
django_filters
```

استفاده می‌شود.

---

# نصب

```bash
pip install django-filter
```

---

# ثبت در settings.py

فایل:

```text
MyProject/config/settings.py
```

```python
INSTALLED_APPS = [

    ...

    "django_filters",
]
```

---

# تنظیم DRF

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_FILTER_BACKENDS": [

        "django_filters.rest_framework.DjangoFilterBackend"
    ]
}
```

---

# استفاده از filterset_fields

فایل:

```text
MyProject/books/views.py
```

```python
from django_filters.rest_framework import (
    DjangoFilterBackend
)

from rest_framework.viewsets import (
    ModelViewSet
)


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    filter_backends = [
        DjangoFilterBackend
    ]

    filterset_fields = [
        "author",
        "year",
    ]
```

---

اکنون:

```http
GET /api/books/?author=ali
```

و

```http
GET /api/books/?year=2025
```

و

```http
GET /api/books/?author=ali&year=2025
```

پشتیبانی می‌شوند.

---

# SearchFilter

گاهی نیاز داریم جستجوی متنی انجام دهیم.

مثال:

```http
GET /api/books/?search=django
```

---

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.filters import (
    SearchFilter
)


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    filter_backends = [
        SearchFilter
    ]

    search_fields = [
        "title",
        "author",
    ]
```

---

درخواست:

```http
GET /api/books/?search=django
```

---

نتیجه:

```text
تمام رکوردهایی که
django
در title یا author دارند.
```

---

# OrderingFilter

مرتب‌سازی داده‌ها.

مثال:

```http
GET /api/books/?ordering=year
```

---

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.filters import (
    OrderingFilter
)


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    filter_backends = [
        OrderingFilter
    ]

    ordering_fields = [
        "year",
        "title",
    ]
```

---

مرتب‌سازی صعودی:

```http
GET /api/books/?ordering=year
```

---

مرتب‌سازی نزولی:

```http
GET /api/books/?ordering=-year
```

---

# ترکیب Filtering و Search

فایل:

```text
MyProject/books/views.py
```

```python
from django_filters.rest_framework import (
    DjangoFilterBackend
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    filter_backends = [

        DjangoFilterBackend,

        SearchFilter,

        OrderingFilter,
    ]

    filterset_fields = [
        "author",
        "year",
    ]

    search_fields = [
        "title",
    ]

    ordering_fields = [
        "year",
    ]
```

---

نمونه:

```http
GET /api/books/?author=ali&search=django&ordering=-year
```

---

# Filtering روی Current User

سناریوی بسیار رایج.

فایل:

```text
MyProject/books/views.py
```

```python
def get_queryset(self):

    return Book.objects.filter(
        owner=self.request.user
    )
```

---

نتیجه:

```text
هر کاربر
فقط داده‌های خودش را می‌بیند.
```

---

# نکته Performance

Filtering باید روی Database انجام شود.

صحیح:

```python
Book.objects.filter(
    year=2025
)
```

---

اشتباه:

```python
books = Book.objects.all()

for book in books:
    ...
```

---

همیشه:

```text
Database Filtering
```

بهتر از:

```text
Python Filtering
```

است.

---

# خطاهای رایج

## استفاده از فیلتر روی فیلد نامعتبر

خطا:

```text
FieldError
```

---

## فراموش کردن django-filter

خطا:

```text
ImproperlyConfigured
```

---

## Filtering در Serializer

اشتباه معماری.

Filtering باید در:

```python
QuerySet
```

انجام شود.

---

## بازگرداندن همه داده‌ها

در پروژه‌های بزرگ:

```python
Book.objects.all()
```

بدون فیلتر و Pagination خطرناک است.

---

# Best Practices

1. Filtering را در QuerySet انجام دهید.
2. از django-filter استفاده کنید.
3. Search را فقط روی فیلدهای لازم فعال کنید.
4. Ordering را محدود کنید.
5. Filtering را با Pagination ترکیب کنید.
6. Queryهای سنگین را با Index مناسب بهینه کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Filtering چیست.
* چگونه با `get_queryset()` فیلتر ایجاد کنیم.
* چگونه از `DjangoFilterBackend` استفاده کنیم.
* SearchFilter چیست.
* OrderingFilter چیست.
* چگونه چند فیلتر را ترکیب کنیم.
* نکات Performance در Filtering چیست.

فصل بعدی:

```text
08 - Pagination
```

## منابع رسمی

* Filtering

https://www.django-rest-framework.org/api-guide/filtering/

