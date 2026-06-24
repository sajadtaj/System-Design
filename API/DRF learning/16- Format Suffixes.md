# 16 - Format Suffixes

## اهداف فصل

در پایان این فصل:

* مفهوم Format Suffix را درک می‌کنید.
* با `format_suffix_patterns()` آشنا می‌شوید.
* ارتباط آن با Content Negotiation را می‌فهمید.
* مزایا و محدودیت‌های آن را می‌شناسید.
* می‌دانید چه زمانی از آن استفاده کنید.

---

# Format Suffix چیست؟

در فصل قبل دیدیم که Client معمولاً با Header زیر فرمت پاسخ را مشخص می‌کند:

```http
Accept: application/json
```

اما روش دیگری نیز وجود دارد.

---

به جای Header:

```http
GET /api/books/
```

می‌توان نوشت:

```http
GET /api/books.json
```

یا:

```http
GET /api/books.api
```

---

بخشی که به انتهای URL اضافه می‌شود:

```text
.json
.api
.xml
```

را:

```text
Format Suffix
```

می‌نامیم.

---

# چرا Format Suffix وجود دارد؟

برخی Clientها یا مرورگرها امکان ارسال Header مناسب را ندارند.

در این شرایط:

```text
URL
```

فرمت خروجی را مشخص می‌کند.

---

مثال:

```http
/api/books.json
```

---

یعنی:

```text
پاسخ را به صورت JSON برگردان.
```

---

# فعال‌سازی Format Suffix

فایل:

```text
MyProject/books/urls.py
```

---

```python
from django.urls import path

from .views import (
    BookListAPIView
)
```

---

```python
urlpatterns = [

    path(
        "books/",
        BookListAPIView.as_view()
    )
]
```

---

حال:

```python
from rest_framework.urlpatterns import (
    format_suffix_patterns
)
```

---

```python
urlpatterns = (
    format_suffix_patterns(
        urlpatterns
    )
)
```

---

# نتیجه

اکنون هر دو URL معتبر هستند:

```http
/api/books/

/api/books.json
```

---

و در صورت پشتیبانی:

```http
/api/books.api
```

---

# پارامتر format

پس از فعال شدن Format Suffix، مقدار فرمت در View قابل دسترسی است.

فایل:

```text
MyProject/books/views.py
```

---

```python
class BookListAPIView(
    APIView
):

    def get(
        self,
        request,
        format=None
    ):
        ...
```

---

مقدار:

```python
format
```

می‌تواند برابر باشد با:

```text
json
api
```

و سایر فرمت‌های پشتیبانی‌شده.

---

# محدود کردن فرمت‌ها

بهتر است فقط فرمت‌های مورد نیاز فعال باشند.

فایل:

```text
MyProject/books/urls.py
```

---

```python
urlpatterns = (
    format_suffix_patterns(
        urlpatterns,
        allowed=["json"]
    )
)
```

---

نتیجه:

مجاز:

```http
/api/books.json
```

---

غیرمجاز:

```http
/api/books.xml
```

---

# ارتباط با Content Negotiation

در فصل قبل گفتیم:

```text
Accept Header
```

فرمت را مشخص می‌کند.

---

اکنون:

```text
Format Suffix
```

هم می‌تواند همین کار را انجام دهد.

---

در واقع:

```text
Content Negotiation
```

ممکن است بر اساس:

```text
Header
```

یا:

```text
URL
```

انجام شود.

---

# مثال عملی

Client:

```http
GET /api/books.json
```

---

DRF:

```text
format=json
```

را تشخیص می‌دهد.

---

سپس:

```python
JSONRenderer
```

را انتخاب می‌کند.

---

و خروجی:

```json
[
    {
        "id": 1,
        "title": "DRF"
    }
]
```

را برمی‌گرداند.

---

# آیا XML هم پشتیبانی می‌شود؟

به صورت پیش‌فرض:

```text
خیر
```

---

DRF فقط Rendererهایی را پشتیبانی می‌کند که شما نصب و فعال کرده باشید.

---

اگر:

```python
XMLRenderer
```

وجود نداشته باشد:

```http
/api/books.xml
```

کار نخواهد کرد.

---

# کاربرد امروزی Format Suffix

در سال‌های ابتدایی REST APIها بسیار رایج بود.

---

امروزه اکثر Clientها:

* Mobile App
* Web App
* Backend Service

به راحتی Header ارسال می‌کنند.

---

بنابراین در پروژه‌های مدرن معمولاً:

```text
Accept Header
```

ترجیح داده می‌شود.

---

# آیا در پروژه جدید استفاده کنیم؟

در اکثر پروژه‌های جدید:

```text
خیر
```

---

زیرا:

```http
Accept: application/json
```

استانداردتر است.

---

اما هنگام نگهداری پروژه‌های قدیمی یا APIهای عمومی ممکن است هنوز با آن مواجه شوید.

---

# خطاهای رایج

## فعال کردن فرمت‌های غیرضروری

اشتباه:

```python
allowed=[
    "json",
    "xml",
    "yaml",
    "html"
]
```

---

در حالی که فقط JSON استفاده می‌شود.

---

## تصور پشتیبانی خودکار XML

وجود:

```http
/api/books.xml
```

به معنی پشتیبانی XML نیست.

---

باید Renderer مناسب نیز وجود داشته باشد.

---

## استفاده همزمان از چندین روش بدون نیاز

گاهی تیم هم:

```text
Accept Header
```

و هم:

```text
Format Suffix
```

را بدون دلیل فعال می‌کند.

---

این کار پیچیدگی API را افزایش می‌دهد.

---

# Best Practices

1. در پروژه‌های جدید از Accept Header استفاده کنید.
2. فقط فرمت‌های مورد نیاز را فعال کنید.
3. از Format Suffix برای سازگاری با Clientهای قدیمی استفاده کنید.
4. JSON را فرمت اصلی API قرار دهید.
5. از فعال کردن Rendererهای غیرضروری خودداری کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Format Suffix چیست.
* چگونه با `format_suffix_patterns()` فعال می‌شود.
* چگونه فرمت‌های مجاز را محدود کنیم.
* ارتباط آن با Content Negotiation چیست.
* چرا امروزه کمتر استفاده می‌شود.
* چه زمانی استفاده از آن منطقی است.

---

فصل بعدی:

```text
17 - Metadata
```

---

## منابع رسمی

* Format Suffixes

[DRF Format Suffixes Documentation](https://www.django-rest-framework.org/api-guide/format-suffixes/?utm_source=chatgpt.com)

