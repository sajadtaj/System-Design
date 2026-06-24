# 02 - Serializers

## اهداف فصل

در پایان این فصل:

* مفهوم Serializer را درک می‌کنید.
* تفاوت Serializer و ModelSerializer را می‌شناسید.
* داده Model را به JSON تبدیل می‌کنید.
* اعتبارسنجی (Validation) را پیاده‌سازی می‌کنید.
* با Field ها و Relation ها آشنا می‌شوید.
* بهترین روش استفاده از Serializer در پروژه‌های واقعی را یاد می‌گیرید.

---

# مقدمه

Serializer قلب DRF است.

وظیفه اصلی آن تبدیل داده بین دو دنیا است:

```text
Python Objects
      ↕
 Serializer
      ↕
JSON
```

هنگامی که API داده‌ای را برای کاربر ارسال می‌کند، Serializer آبجکت‌های Django را به JSON تبدیل می‌کند.

هنگامی که کاربر داده‌ای ارسال می‌کند، Serializer JSON را به داده قابل استفاده در Django تبدیل و اعتبارسنجی می‌کند.

---

# مسئله‌ای که حل می‌کند

فرض کنید مدل زیر را داریم.

فایل:

```text
MyProject/books/models.py
```

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

اگر Serializer وجود نداشت باید به صورت دستی بنویسیم:

```python
{
    "id": book.id,
    "title": book.title,
    "author": book.author,
    "price": str(book.price)
}
```

این کار:

* تکراری است.
* اعتبارسنجی ندارد.
* نگهداری سختی دارد.

Serializer این مشکل را حل می‌کند.

---

# جایگاه در معماری DRF

```text
Client
   │
   ▼
APIView
   │
   ▼
Serializer
   │
   ▼
Model
```

در هنگام خواندن:

```text
Model
   ▼
Serializer
   ▼
JSON
```

در هنگام نوشتن:

```text
JSON
   ▼
Serializer
   ▼
Model
```

---

# پیاده‌سازی پایه

## ساخت Serializer ساده

فایل:

```text
MyProject/books/serializers.py
```

```python
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )
```

---

# اولین استفاده از Serializer

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BookSerializer

class ExampleAPIView(APIView):

    def get(self, request):

        data = {
            "id": 1,
            "title": "Django",
            "author": "Sajad",
            "price": "100.00"
        }

        serializer = BookSerializer(data)

        return Response(serializer.data)
```

---

# ModelSerializer

در پروژه‌های واقعی تقریباً همیشه از ModelSerializer استفاده می‌شود.

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
            "price"
        ]
```

---

# مثال عملی

مدل:

```text
MyProject/books/models.py
```

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

Serializer:

```text
MyProject/books/serializers.py
```

```python
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
```

View:

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

خروجی:

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

# تنظیمات و گزینه‌های مهم

## fields

```python
class Meta:
    model = Book
    fields = [
        "id",
        "title"
    ]
```

---

## exclude

```python
class Meta:
    model = Book
    exclude = [
        "created_at"
    ]
```

---

## read_only_fields

```python
class Meta:
    model = Book

    read_only_fields = [
        "id"
    ]
```

---

## extra_kwargs

```python
class Meta:
    model = Book

    extra_kwargs = {
        "title": {
            "required": True
        }
    }
```

---

# Validation

## اعتبارسنجی یک فیلد

فایل:

```text
MyProject/books/serializers.py
```

```python
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    def validate_price(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero."
            )

        return value
```

---

## اعتبارسنجی چند فیلد

```python
def validate(self, attrs):

    if attrs["title"] == attrs["author"]:
        raise serializers.ValidationError(
            "Title and author cannot be equal."
        )

    return attrs
```

---

# انواع و حالت‌های مختلف

## Serializer

کاملاً دستی

```python
serializers.Serializer
```

---

## ModelSerializer

مبتنی بر Model

```python
serializers.ModelSerializer
```

---

## HyperlinkedModelSerializer

برای API های مبتنی بر URL

```python
serializers.HyperlinkedModelSerializer
```

---

# روابط (Relations)

فرض کنید:

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

Serializer:

```python
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
```

خروجی:

```json
{
    "id": 1,
    "title": "DRF",
    "category": 2
}
```

---

# خطاها و نکات رایج

## فراموش کردن many=True

اشتباه:

```python
serializer = BookSerializer(books)
```

صحیح:

```python
serializer = BookSerializer(
    books,
    many=True
)
```

---

## استفاده از fields="**all**"

برای پروژه‌های کوچک مناسب است.

اما در پروژه‌های Production بهتر است فیلدها را صریح مشخص کنیم.

---

## قرار دادن Business Logic داخل Serializer

اشتباه:

```python
پردازش مالی
ارسال پیامک
ثبت لاگ
```

Serializer فقط باید:

* Validation
* Transformation

انجام دهد.

---

# Best Practices

1. هر Model یک Serializer مستقل داشته باشد.
2. Validation را داخل Serializer انجام دهید.
3. Business Logic را داخل Service Layer نگه دارید.
4. در Production از fields مشخص استفاده کنید.
5. Serializer ها را کوچک و تک‌منظوره نگه دارید.
6. برای Query های سنگین از select_related و prefetch_related استفاده کنید.

---

# جمع‌بندی

Serializer مهم‌ترین جزء DRF است.

در این فصل یاد گرفتیم:

* Serializer چیست.
* ModelSerializer چیست.
* Validation چگونه کار می‌کند.
* Relation ها چگونه مدیریت می‌شوند.
* Best Practice های استفاده از Serializer چیست.

در فصل بعد وارد Generic Views می‌شویم و یاد می‌گیریم چگونه بدون نوشتن View های تکراری، API های استاندارد CRUD بسازیم.

## منابع رسمی

* serializers
* fields
* relations
* ModelSerializer
* Validation
* Nested Relationships

