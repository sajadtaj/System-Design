# 04 - ViewSets and Routers

## اهداف فصل

در پایان این فصل:

* تفاوت Generic Views و ViewSet را درک می‌کنید.
* با ViewSet و ModelViewSet آشنا می‌شوید.
* Routerها را پیکربندی می‌کنید.
* CRUD کامل را با حداقل کد پیاده‌سازی می‌کنید.
* Custom Actionها را ایجاد می‌کنید.
* ساختار استاندارد URL در DRF را یاد می‌گیرید.

---

# مقدمه

در فصل قبل با Generic Views آشنا شدیم.

برای ساخت CRUD کامل معمولاً دو View نیاز داشتیم:

```text
BookListCreateAPIView

BookRetrieveUpdateDestroyAPIView
```

هرچند این روش بسیار خوب است، اما هنوز مقداری کد تکراری وجود دارد.

DRF یک سطح بالاتر از انتزاع را معرفی می‌کند:

```python
ViewSet
```

و

```python
ModelViewSet
```

که تقریباً تمام عملیات CRUD را در یک کلاس واحد قرار می‌دهند.

---

# مسئله‌ای که ViewSet حل می‌کند

فرض کنید در فصل قبل داشتیم:

فایل:

```text
MyProject/books/views.py
```

```python
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRUDAPIView(
    RetrieveUpdateDestroyAPIView
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

دو View مختلف.

دو URL مختلف.

تنظیمات تکراری.

---

ViewSet همین قابلیت را در یک کلاس متمرکز می‌کند:

```python
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

---

# جایگاه ViewSet در معماری DRF

معماری کلی:

```text
APIView
    ↓
GenericAPIView
    ↓
Generic Views
    ↓
ViewSet
    ↓
ModelViewSet
```

---

# مدل پروژه

فایل:

```text
MyProject/books/models.py
```

```python
from django.db import models


class Book(models.Model):

    title = models.CharField(
        max_length=200
    )

    author = models.CharField(
        max_length=100
    )

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


class BookSerializer(
    serializers.ModelSerializer
):

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

# ViewSet چیست؟

ViewSet مشابه View معمولی است اما به جای متدهای:

```python
get()
post()
put()
delete()
```

از Actionها استفاده می‌کند.

مثال:

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer


class BookViewSet(
    viewsets.ViewSet
):

    def list(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
```

---

# ModelViewSet چیست؟

در عمل تقریباً همیشه از:

```python
ModelViewSet
```

استفاده می‌کنیم.

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

    queryset = Book.objects.all()

    serializer_class = BookSerializer
```

همین چند خط:

* List
* Retrieve
* Create
* Update
* Partial Update
* Delete

را فعال می‌کند.

---

# Router چیست؟

Router به صورت خودکار URLها را تولید می‌کند.

بدون Router باید دستی URLها را تعریف کنیم.

Router این کار را انجام می‌دهد.

---

# DefaultRouter

فایل:

```text
MyProject/books/urls.py
```

```python
from rest_framework.routers import (
    DefaultRouter
)

from .views import BookViewSet


router = DefaultRouter()

router.register(
    "books",
    BookViewSet,
    basename="books"
)

urlpatterns = router.urls
```

---

# اتصال به URL اصلی پروژه

فایل:

```text
MyProject/config/urls.py
```

```python
from django.urls import (
    include,
    path
)

urlpatterns = [
    path(
        "api/",
        include("books.urls")
    ),
]
```

---

# URLهای تولید شده

Router به صورت خودکار این URLها را می‌سازد:

```http
GET     /api/books/
POST    /api/books/

GET     /api/books/1/

PUT     /api/books/1/

PATCH   /api/books/1/

DELETE  /api/books/1/
```

---

# عملیات List

درخواست:

```http
GET /api/books/
```

پاسخ:

```json
[
    {
        "id": 1,
        "title": "DRF",
        "author": "Sajad",
        "price": "100.00"
    }
]
```

---

# عملیات Retrieve

درخواست:

```http
GET /api/books/1/
```

پاسخ:

```json
{
    "id": 1,
    "title": "DRF",
    "author": "Sajad",
    "price": "100.00"
}
```

---

# عملیات Create

درخواست:

```http
POST /api/books/
```

Body:

```json
{
    "title": "Docker",
    "author": "Sajad",
    "price": "150.00"
}
```

---

# عملیات Update

درخواست:

```http
PUT /api/books/1/
```

Body:

```json
{
    "title": "Advanced Docker",
    "author": "Sajad",
    "price": "180.00"
}
```

---

# عملیات Partial Update

درخواست:

```http
PATCH /api/books/1/
```

Body:

```json
{
    "price": "200.00"
}
```

---

# عملیات Delete

درخواست:

```http
DELETE /api/books/1/
```

---

# Custom Action چیست؟

گاهی عملیاتی داریم که جزو CRUD نیست.

مثال:

* Publish Book
* Archive Book
* Approve Book

برای این موارد از:

```python
@action
```

استفاده می‌کنیم.

---

# مثال Custom Action

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.decorators import (
    action
)

from rest_framework.response import (
    Response
)


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    @action(
        detail=True,
        methods=["post"]
    )
    def publish(
        self,
        request,
        pk=None
    ):

        return Response({
            "message": "Book published"
        })
```

---

# URL تولید شده

```http
POST /api/books/1/publish/
```

---

# detail=True و detail=False

## detail=True

برای یک رکورد خاص.

```http
POST /books/1/publish/
```

---

## detail=False

برای کل مجموعه.

```http
POST /books/export/
```

مثال:

```python
@action(
    detail=False,
    methods=["post"]
)
def export(self, request):
    pass
```

---

# تنظیمات مهم

## queryset

```python
queryset = Book.objects.all()
```

---

## serializer_class

```python
serializer_class = BookSerializer
```

---

## lookup_field

پیش‌فرض:

```python
lookup_field = "pk"
```

مثال:

```python
lookup_field = "slug"
```

---

# Query Optimization

همانند Generic Views.

اشتباه:

```python
queryset = Book.objects.all()
```

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

## فراموش کردن basename

گاهی Router نمی‌تواند نام Route را تشخیص دهد.

در این حالت:

```python
router.register(
    "books",
    BookViewSet,
    basename="books"
)
```

را مشخص کنید.

---

## استفاده بی‌دلیل از ViewSet

همه APIها CRUD نیستند.

برای APIهای پیچیده گاهی:

```python
APIView
```

یا

```python
GenericAPIView
```

انتخاب بهتری است.

---

## منطق تجاری داخل ViewSet

اشتباه:

```python
پردازش مالی

ارسال پیامک

محاسبات سنگین
```

این موارد باید در Service Layer باشند.

---

# چه زمانی از Generic Views استفاده کنیم؟

اگر API ساده و محدود است:

```python
ListAPIView
CreateAPIView
```

مناسب‌اند.

---

اگر CRUD کامل داریم:

```python
ModelViewSet
```

معمولاً بهترین انتخاب است.

---

# Best Practices

1. برای CRUDهای استاندارد از ModelViewSet استفاده کنید.
2. همیشه Router استفاده کنید.
3. Actionهای سفارشی را محدود نگه دارید.
4. Business Logic را داخل Service Layer قرار دهید.
5. Queryها را بهینه کنید.
6. Permissionها را روی ViewSet اعمال کنید.
7. Serializerهای جداگانه برای Create و Read در پروژه‌های بزرگ در نظر بگیرید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* ViewSet چیست.
* ModelViewSet چیست.
* Router چگونه کار می‌کند.
* URLها چگونه خودکار ساخته می‌شوند.
* Custom Action چیست.
* چه زمانی از ViewSet استفاده کنیم.

در فصل بعد وارد Authentication می‌شویم و یاد می‌گیریم چگونه کاربران را احراز هویت کنیم و دسترسی به APIها را کنترل کنیم.

## منابع رسمی

* Routers
* ViewSets
* ModelViewSet
* DefaultRouter
* SimpleRouter
* Action Decorator

https://www.django-rest-framework.org/api-guide/routers/

