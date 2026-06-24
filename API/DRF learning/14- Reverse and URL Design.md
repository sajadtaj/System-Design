# 14 - Reverse and URL Design

## اهداف فصل

در پایان این فصل:

* URL Design صحیح در API را درک می‌کنید.
* با `reverse()` آشنا می‌شوید.
* مزایای نام‌گذاری URLها را می‌فهمید.
* وابستگی به URLهای Hard-Coded را حذف می‌کنید.
* با URL Generation در Routerها آشنا می‌شوید.
* بهترین روش طراحی URL در DRF را یاد می‌گیرید.

---

# URL Design چیست؟

URL Design یعنی:

```text
طراحی استاندارد
آدرس‌های API
```

---

مثال خوب:

```http
/api/books/

/api/books/15/

/api/authors/

/api/authors/8/
```

---

مثال ضعیف:

```http
/get-all-books/

/book-details?id=15

/fetch-author
```

---

در REST API معمولاً:

```text
اسم Resource
```

در URL قرار می‌گیرد.

---

# اصول طراحی URL

## از اسم استفاده کنید

صحیح:

```http
/api/books/
```

---

اشتباه:

```http
/api/get-books/
```

---

زیرا:

```text
HTTP Method
```

عملیات را مشخص می‌کند.

---

مثال:

```http
GET /api/books/
POST /api/books/
DELETE /api/books/15/
```

---

# ساختار استاندارد Resource

لیست:

```http
GET /api/books/
```

---

جزئیات:

```http
GET /api/books/15/
```

---

ایجاد:

```http
POST /api/books/
```

---

ویرایش:

```http
PUT /api/books/15/
```

---

حذف:

```http
DELETE /api/books/15/
```

---

# مشکل Hard-Coded URL

فرض کنید:

فایل:

```text
MyProject/books/views.py
```

---

کد:

```python
return Response({
    "url":
        "/api/books/15/"
})
```

---

مشکل:

اگر URL تغییر کند:

```http
/api/v2/books/15/
```

باید تمام پروژه اصلاح شود.

---

راه حل:

```python
reverse()
```

---

# reverse چیست؟

تابعی برای تولید URL از روی نام URL.

---

مزیت:

```text
عدم وابستگی
به مسیر واقعی URL
```

---

# تعریف URL Name

فایل:

```text
MyProject/books/urls.py
```

```python
from django.urls import path
from .views import BookDetailAPIView
```

---

```python
urlpatterns = [

    path(
        "books/<int:pk>/",
        BookDetailAPIView.as_view(),
        name="book-detail"
    )
]
```

---

# استفاده از reverse

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.reverse import reverse
```

---

```python
url = reverse(
    "book-detail",
    kwargs={"pk": 15},
    request=request
)
```

---

خروجی:

```http
http://localhost:8000/books/15/
```

---

# چرا reverse بهتر است؟

به جای:

```python
"/books/15/"
```

---

از:

```python
reverse(...)
```

استفاده می‌کنیم.

---

اگر URL تغییر کند:

```python
path(
    "api/books/<int:pk>/",
    ...
)
```

---

کدهای دیگر تغییری نمی‌کنند.

---

# reverse در Serializer

گاهی لازم است لینک Resource را برگردانیم.

---

فایل:

```text
MyProject/books/serializers.py
```

```python
from rest_framework import serializers
from rest_framework.reverse import reverse
```

---

```python
class BookSerializer(
    serializers.ModelSerializer
):

    detail_url = (
        serializers.SerializerMethodField()
    )

    class Meta:

        model = Book

        fields = [
            "id",
            "title",
            "detail_url"
        ]

    def get_detail_url(
        self,
        obj
    ):

        request = (
            self.context["request"]
        )

        return reverse(
            "book-detail",
            kwargs={"pk": obj.pk},
            request=request
        )
```

---

پاسخ:

```json
{
    "id": 1,
    "title": "DRF",
    "detail_url":
        "http://localhost:8000/books/1/"
}
```

---

# HyperlinkedModelSerializer

DRF راهکار آماده نیز دارد.

---

فایل:

```text
MyProject/books/serializers.py
```

```python
from rest_framework import serializers
```

---

```python
class BookSerializer(
    serializers.HyperlinkedModelSerializer
):

    class Meta:

        model = Book

        fields = [
            "url",
            "id",
            "title"
        ]
```

---

خروجی:

```json
{
    "url":
        "http://localhost:8000/books/1/",
    "id": 1,
    "title": "DRF"
}
```

---

# Router و URL Generation

فایل:

```text
MyProject/books/views.py
```

```python
class BookViewSet(
    ModelViewSet
):
    ...
```

---

فایل:

```text
MyProject/books/urls.py
```

```python
from rest_framework.routers import (
    DefaultRouter
)
```

---

```python
router = DefaultRouter()

router.register(
    "books",
    BookViewSet,
    basename="book"
)
```

---

DRF خودکار URL می‌سازد.

---

نمونه:

```http
/api/books/

/api/books/1/
```

---

و نام‌ها:

```text
book-list

book-detail
```

---

# reverse با Router

```python
reverse(
    "book-detail",
    kwargs={"pk": 1},
    request=request
)
```

---

بدون نیاز به دانستن مسیر واقعی.

---

# URL Design در پروژه واقعی

پیشنهاد:

```http
/api/v1/books/

/api/v1/authors/

/api/v1/categories/
```

---

نه:

```http
/books/

/authors/
```

---

چون Versioning را ساده‌تر می‌کند.

---

# Nested URL

مثال:

```http
/api/authors/5/books/
```

---

مناسب زمانی که:

```text
Book
وابسته به
Author
```

باشد.

---

اما زیاده‌روی نکنید.

---

اشتباه:

```http
/api/authors/5/books/10/reviews/2/comments/
```

---

چنین URLهایی نگهداری سختی دارند.

---

# Best Practices

## نام‌گذاری یکنواخت

صحیح:

```http
/api/books/
/api/authors/
/api/categories/
```

---

اشتباه:

```http
/api/book/
/api/GetAuthors/
/api/category-list/
```

---

## استفاده از اسم جمع

ترجیحاً:

```http
/books/
```

---

به جای:

```http
/book/
```

---

## استفاده از reverse

هرگز URL را Hard-Coded نکنید.

---

## استفاده از Router

در اکثر CRUDها:

```python
ModelViewSet
```

و:

```python
Router
```

بهترین انتخاب هستند.

---

# خطاهای رایج

## Hard-Coded URL

اشتباه:

```python
"/api/books/1/"
```

---

## نداشتن name

اشتباه:

```python
path(...)
```

بدون:

```python
name=
```

---

## URLهای طولانی

اشتباه:

```http
/api/authors/1/books/2/reviews/3/comments/4/
```

---

## استفاده از فعل

اشتباه:

```http
/get-books/
/create-book/
```

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* URL Design چیست.
* چگونه URL استاندارد طراحی کنیم.
* reverse چیست.
* چرا نباید URLها را Hard-Coded کنیم.
* HyperlinkedModelSerializer چیست.
* Router چگونه URL تولید می‌کند.
* بهترین روش طراحی URL در DRF چیست.

---

فصل بعدی:

```text
15 - Content Negotiation
```

---

## منابع رسمی

* Reverse

[DRF Reverse Documentation](https://www.django-rest-framework.org/api-guide/reverse/?utm_source=chatgpt.com)

* Routers

[DRF Routers Documentation](https://www.django-rest-framework.org/api-guide/routers/?utm_source=chatgpt.com)

