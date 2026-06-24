# 03 - Generic Views

## اهداف فصل

در پایان این فصل:

* تفاوت APIView و Generic Views را درک می‌کنید.
* با GenericAPIView آشنا می‌شوید.
* نقش Mixins را متوجه می‌شوید.
* APIهای CRUD را با کمترین کد پیاده‌سازی می‌کنید.
* با Query Optimization آشنا می‌شوید.
* می‌توانید برای اکثر APIهای پروژه از Generic Views استفاده کنید.

---

# مقدمه

در فصل قبل با Serializer آشنا شدیم.

اکنون می‌خواهیم داده‌های مدل را از طریق API در اختیار کاربران قرار دهیم.

اولین راه حل استفاده از APIView است.

اما زمانی که تعداد APIها افزایش پیدا کند، حجم زیادی از کدهای تکراری ایجاد می‌شود.

DRF برای حل این مشکل Generic Views را معرفی کرده است.

---

# مسئله‌ای که Generic Views حل می‌کند

فرض کنید می‌خواهیم لیست کتاب‌ها را نمایش دهیم.

با APIView:

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


class BookListAPIView(APIView):

    def get(self, request):

        books = Book.objects.all()

        serializer = BookSerializer(
            books,
            many=True
        )

        return Response(serializer.data)
```

این کد کاملاً صحیح است.

اما تقریباً همین الگو را باید برای:

* لیست
* جزئیات
* ایجاد
* ویرایش
* حذف

تکرار کنیم.

Generic Views این تکرار را حذف می‌کنند.

---

# جایگاه Generic Views در معماری DRF

معماری داخلی DRF به شکل زیر است:

```text
APIView
    ↓
GenericAPIView
    ↓
Mixins
    ↓
Concrete Generic Views
```

یعنی:

```python
ListAPIView
```

در واقع روی:

```python
GenericAPIView
```

و

```python
ListModelMixin
```

ساخته شده است.

---

# GenericAPIView چیست؟

GenericAPIView کلاس پایه اکثر Viewهای DRF است.

ویژگی‌های مهم آن:

* مدیریت Queryset
* مدیریت Serializer
* مدیریت Pagination
* مدیریت Filtering
* مدیریت Lookup

مثال:

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.generics import GenericAPIView

from .models import Book
from .serializers import BookSerializer


class BookGenericAPIView(GenericAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer
```

به تنهایی کاربرد زیادی ندارد اما پایه تمام Generic Viewها است.

---

# Mixins چیست؟

Mixinها عملیات CRUD را پیاده‌سازی می‌کنند.

مهم‌ترین Mixins:

| Mixin              | وظیفه          |
| ------------------ | -------------- |
| ListModelMixin     | نمایش لیست     |
| CreateModelMixin   | ایجاد          |
| RetrieveModelMixin | نمایش یک رکورد |
| UpdateModelMixin   | ویرایش         |
| DestroyModelMixin  | حذف            |

---

# مثال Mixin

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from .models import Book
from .serializers import BookSerializer


class BookListAPIView(
    ListModelMixin,
    GenericAPIView
):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    def get(self, request):

        return self.list(request)
```

اما DRF همین الگو را به صورت آماده ارائه کرده است.

---

# مدل پروژه

برای ادامه فصل از مدل زیر استفاده می‌کنیم.

فایل:

```text
MyProject/books/models.py
```

```python
from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
```

---

# Serializer پروژه

فایل:

```text
MyProject/books/serializers.py
```

```python
from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book

        fields = [
            "id",
            "title",
            "author",
            "price",
            "created_at"
        ]
```

---

# ListAPIView

برای نمایش لیست داده‌ها استفاده می‌شود.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.generics import ListAPIView

from .models import Book
from .serializers import BookSerializer


class BookListAPIView(ListAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer
```

---

# URL

فایل:

```text
MyProject/books/urls.py
```

```python
from django.urls import path

from .views import BookListAPIView


urlpatterns = [
    path(
        "",
        BookListAPIView.as_view(),
        name="book-list"
    ),
]
```

---

درخواست:

```http
GET /books/
```

---

# CreateAPIView

برای ایجاد داده جدید.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.generics import CreateAPIView

from .models import Book
from .serializers import BookSerializer


class BookCreateAPIView(CreateAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer
```

---

درخواست:

```http
POST /books/create/
```

Body:

```json
{
    "title": "DRF",
    "author": "Sajad",
    "price": "100.00"
}
```

---

# RetrieveAPIView

نمایش یک رکورد.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.generics import RetrieveAPIView


class BookDetailAPIView(RetrieveAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer
```

---

درخواست:

```http
GET /books/1/
```

---

# UpdateAPIView

ویرایش رکورد.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.generics import UpdateAPIView


class BookUpdateAPIView(UpdateAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer
```

---

درخواست:

```http
PUT /books/1/update/
```

---

# DestroyAPIView

حذف رکورد.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.generics import DestroyAPIView


class BookDeleteAPIView(DestroyAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer
```

---

درخواست:

```http
DELETE /books/1/delete/
```

---

# ListCreateAPIView

یکی از پرکاربردترین کلاس‌ها.

هم لیست می‌دهد و هم ایجاد می‌کند.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.generics import ListCreateAPIView


class BookListCreateAPIView(ListCreateAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer
```

---

پشتیبانی از:

```http
GET /books/
POST /books/
```

---

# RetrieveUpdateDestroyAPIView

محبوب‌ترین Generic View در پروژه‌های واقعی.

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView
)


class BookRUDAPIView(
    RetrieveUpdateDestroyAPIView
):

    queryset = Book.objects.all()

    serializer_class = BookSerializer
```

---

پشتیبانی از:

```http
GET /books/1/
PUT /books/1/
PATCH /books/1/
DELETE /books/1/
```

---

# تنظیمات مهم

## queryset

منبع داده View.

```python
queryset = Book.objects.all()
```

---

## serializer_class

Serializer مورد استفاده.

```python
serializer_class = BookSerializer
```

---

## lookup_field

پیش‌فرض:

```python
pk
```

تغییر:

```python
lookup_field = "id"
```

یا:

```python
lookup_field = "slug"
```

---

# Query Optimization

یکی از مهم‌ترین نکات مستندات رسمی DRF.

فرض کنید:

فایل:

```text
MyProject/books/models.py
```

```python
class Category(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
```

---

اشتباه:

```python
queryset = Book.objects.all()
```

در تعداد زیاد رکورد ممکن است باعث N+1 Query شود.

---

بهتر:

```python
queryset = Book.objects.select_related(
    "category"
)
```

---

برای ManyToMany:

```python
queryset = Book.objects.prefetch_related(
    "tags"
)
```

---

# خطاها و نکات رایج

## فراموش کردن serializer_class

خطا:

```text
'serializer_class' is not set
```

---

## فراموش کردن queryset

خطا:

```text
AssertionError
```

---

## استفاده بیش از حد از APIView

بسیاری از توسعه‌دهندگان تازه‌کار همه چیز را با APIView می‌نویسند.

در حالی که Generic Views برای اکثر CRUDها مناسب‌تر هستند.

---

## عدم بهینه‌سازی Query ها

در محیط Production می‌تواند باعث افت شدید Performance شود.

---

# Best Practices

1. برای CRUDهای ساده از Generic Views استفاده کنید.
2. از ListCreateAPIView برای Collectionها استفاده کنید.
3. از RetrieveUpdateDestroyAPIView برای Resourceها استفاده کنید.
4. Queryها را با select_related و prefetch_related بهینه کنید.
5. منطق پیچیده را در Service Layer قرار دهید.
6. Validation را در Serializer انجام دهید.
7. Authentication و Permission را روی View اعمال کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* GenericAPIView چیست.
* Mixins چه هستند.
* چگونه CRUD کامل بسازیم.
* تفاوت Generic Views مختلف چیست.
* چگونه Queryها را بهینه کنیم.

در فصل بعد وارد ViewSets و Routers می‌شویم و می‌بینیم چگونه همین CRUD را با کد بسیار کمتر پیاده‌سازی کنیم.

## منابع رسمی

* GenericAPIView
* Generic Views
* Mixins
* ListAPIView
* CreateAPIView
* RetrieveAPIView
* UpdateAPIView
* DestroyAPIView
* Queryset Optimization

https://www.django-rest-framework.org/api-guide/generic-views/

