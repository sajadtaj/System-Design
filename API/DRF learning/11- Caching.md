# 11 - Caching

## اهداف فصل

در پایان این فصل:

* مفهوم Cache را درک می‌کنید.
* تفاوت Cache و Database را می‌فهمید.
* سیستم Cache در Django را پیکربندی می‌کنید.
* Cache را در DRF استفاده می‌کنید.
* Per-View Cache را پیاده‌سازی می‌کنید.
* از Redis به عنوان Cache Backend استفاده می‌کنید.
* Cache Invalidation را درک می‌کنید.
* خطاهای رایج Cache را می‌شناسید.
* برای Production تصمیم درستی می‌گیرید.

---

# مقدمه

فرض کنید API زیر دارید:

فایل:

```text id="s61hxx"
MyProject/books/views.py
```

```python id="u0u1zz"
class BookListAPIView(
    ListAPIView
):

    queryset = (
        Book.objects
        .select_related("author")
        .prefetch_related("categories")
    )

    serializer_class = (
        BookSerializer
    )
```

---

میانگین زمان پاسخ:

```text id="e0uhx9"
850 ms
```

---

کاربران:

```text id="lhrn4r"
10,000 Request / Day
```

ارسال می‌کنند.

---

در نتیجه:

* Database تحت فشار قرار می‌گیرد.
* CPU مصرف می‌شود.
* Response Time افزایش می‌یابد.

---

راه‌حل:

```text id="z0t6i5"
Caching
```

---

# Cache چیست؟

Cache یعنی:

```text id="zlxkvd"
ذخیره موقت
داده‌های پرتکرار
```

---

به جای:

```text id="rbrcxy"
Database Query
```

---

از:

```text id="5kncf8"
Memory
```

استفاده می‌شود.

---

# مثال ساده

بدون Cache:

```text id="a2yksm"
Request
    ↓
View
    ↓
Database
    ↓
Serializer
    ↓
Response
```

---

با Cache:

```text id="l6l6aq"
Request
    ↓
Cache
    ↓
Response
```

---

اگر داده در Cache موجود نباشد:

```text id="q1hf7e"
Cache Miss
```

رخ می‌دهد.

---

اگر داده موجود باشد:

```text id="jlwmiz"
Cache Hit
```

رخ می‌دهد.

---

# چرا Cache مهم است؟

مزایا:

* کاهش Query
* افزایش سرعت پاسخ
* کاهش مصرف CPU
* کاهش بار Database
* افزایش Scalability

---

# تفاوت Cache و Database

| ویژگی          | Cache      | Database |
| -------------- | ---------- | -------- |
| سرعت           | بسیار زیاد | کمتر     |
| ماندگاری       | موقت       | دائمی    |
| مصرف RAM       | زیاد       | کمتر     |
| منبع اصلی داده | خیر        | بله      |

---

قاعده:

```text id="vx0y7m"
Database
Source Of Truth
```

---

Cache فقط یک نسخه موقت است.

---

# Cache Backend چیست؟

Django چند Backend دارد:

```python id="jqnf5m"
LocMemCache

FileBasedCache

DatabaseCache

RedisCache

Memcached
```

---

در پروژه‌های Production:

```text id="ojqrxf"
Redis
```

رایج‌ترین انتخاب است.

---

# Cache پیش‌فرض Django

فایل:

```text id="q3pyl7"
MyProject/config/settings.py
```

```python id="zhx8wv"
CACHES = {

    "default": {

        "BACKEND":

            "django.core.cache.backends.locmem.LocMemCache",

        "LOCATION":
            "unique-cache"
    }
}
```

---

# محدودیت LocMemCache

در محیط چند سروری:

```text id="m0kt3y"
Server A
```

و

```text id="i3ktko"
Server B
```

Cache مشترک ندارند.

---

در نتیجه:

```text id="h9r3zr"
Production مناسب نیست.
```

---

# Redis Cache

پیشنهاد اصلی برای Production.

---

نصب:

```bash id="u2x6iv"
pip install redis
```

---

فایل:

```text id="x1s1ux"
MyProject/config/settings.py
```

```python id="m6gpnk"
CACHES = {

    "default": {

        "BACKEND":
            "django.core.cache.backends.redis.RedisCache",

        "LOCATION":
            "redis://redis:6379/1"
    }
}
```

---

# تست Cache

فایل:

```text id="wkfqeq"
MyProject/books/views.py
```

```python id="nn6sfp"
from django.core.cache import (
    cache
)
```

---

```python id="vjb7qh"
cache.set(
    "site_name",
    "DRF Book",
    timeout=60
)
```

---

خواندن:

```python id="2rxm9v"
cache.get(
    "site_name"
)
```

---

خروجی:

```text id="1xib08"
DRF Book
```

---

# پارامتر timeout

```python id="gsgu6j"
cache.set(
    key="site_name",

    value="DRF Book",

    timeout=60
)
```

---

یعنی:

```text id="0kxy0n"
60 ثانیه
```

---

پس از آن:

```text id="ifm74w"
Cache Expire
```

خواهد شد.

---

# Per-View Cache

رایج‌ترین روش در DRF.

---

فایل:

```text id="90e9oa"
MyProject/books/views.py
```

```python id="wjsh55"
from django.views.decorators.cache import (
    cache_page
)

from django.utils.decorators import (
    method_decorator
)
```

---

```python id="9i2bgh"
@method_decorator(
    cache_page(60),
    name="dispatch"
)
class BookListAPIView(
    ListAPIView
):

    queryset = (
        Book.objects.all()
    )

    serializer_class = (
        BookSerializer
    )
```

---

نتیجه:

```text id="d2u20e"
60 ثانیه Cache
```

---

# فرآیند اجرای Per-View Cache

اولین درخواست:

```text id="ylghgf"
Request
    ↓
View
    ↓
Database
    ↓
Cache Save
    ↓
Response
```

---

درخواست‌های بعدی:

```text id="3nwd9h"
Request
    ↓
Cache
    ↓
Response
```

---

# Cache برای Function View

فایل:

```text id="w9xlbl"
MyProject/books/views.py
```

```python id="f7ikns"
@cache_page(60)
def book_list(
    request
):
    ...
```

---

# Low-Level Cache API

برای کنترل کامل.

---

فایل:

```text id="f98j66"
MyProject/books/services.py
```

```python id="c4dg1q"
from django.core.cache import (
    cache
)
```

---

```python id="nvktg0"
books = cache.get(
    "books"
)
```

---

```python id="p60b7f"
if books is None:

    books = list(
        Book.objects.all()
    )

    cache.set(
        "books",
        books,
        timeout=300
    )
```

---

# حذف Cache

```python id="r3h1lk"
cache.delete(
    "books"
)
```

---

# پاک‌سازی کامل Cache

```python id="s2q5q8"
cache.clear()
```

---

# Cache Key

هر داده با یک کلید ذخیره می‌شود.

---

مثال:

```python id="mtznz5"
cache.set(
    "books",
    data
)
```

---

کلید:

```text id="24mgl7"
books
```

---

# نام‌گذاری مناسب Key

اشتباه:

```python id="ydpkhd"
cache.set(
    "data",
    value
)
```

---

صحیح:

```python id="n7vsz6"
cache.set(
    "books:list",
    value
)
```

---

یا:

```python id="43wddm"
cache.set(
    f"book:{book_id}",
    value
)
```

---

# Cache Invalidation چیست؟

سخت‌ترین بخش Cache.

---

سناریو:

```text id="89j74g"
Book Updated
```

---

اما:

```text id="bhq5eo"
Cache
```

هنوز داده قدیمی دارد.

---

در نتیجه:

```text id="6b7pov"
Stale Data
```

---

# راه‌حل

بعد از تغییر داده:

```python id="p3f6yc"
cache.delete(
    f"book:{book.id}"
)
```

---

# Cache و Authentication

نکته بسیار مهم.

---

این API:

```http id="9u6wev"
GET /api/profile/
```

وابسته به User است.

---

اگر Cache اشتباه اعمال شود:

```text id="c0hbfv"
User A
```

ممکن است اطلاعات:

```text id="xv2iuj"
User B
```

را دریافت کند.

---

# بنابراین

روی APIهای:

```text id="p4ccae"
User Specific
```

باید با دقت Cache اعمال شود.

---

# مثال اشتباه

فایل:

```text id="o2zl2c"
MyProject/accounts/views.py
```

```python id="31jxqm"
@method_decorator(
    cache_page(300),
    name="dispatch"
)
class ProfileAPIView(
    APIView
):
    ...
```

---

ممکن است باعث نشت اطلاعات شود.

---

# Cache و Query Parameters

مثال:

```http id="3z91r0"
GET /api/books/?page=1
```

---

```http id="lphd5g"
GET /api/books/?page=2
```

---

این دو درخواست:

```text id="67y7xv"
Cache Key
```

متفاوت خواهند داشت.

---

# Cache و Throttling

هر دو معمولاً از:

```text id="m1uywy"
Redis
```

استفاده می‌کنند.

---

اما هدف متفاوت است.

---

Cache:

```text id="h5s6ua"
Speed
```

---

Throttle:

```text id="w4e5ee"
Rate Control
```

---

# Cache و Celery

سناریوی رایج:

```text id="9wq8n5"
Celery Task
    ↓
Generate Report
    ↓
Save To Cache
```

---

سپس:

```text id="xkk2an"
API
```

نتیجه را از Cache می‌خواند.

---

# نکته Data Engineering

برای داده‌های بسیار بزرگ:

```text id="uxe2js"
Cache Everything
```

استراتژی مناسبی نیست.

---

باید فقط:

```text id="m7d8kg"
Hot Data
```

را Cache کنید.

---

# خطاهای رایج

## Cache کردن همه چیز

باعث مصرف زیاد RAM می‌شود.

---

## Cache بدون Expiration

ممکن است داده قدیمی باقی بماند.

---

## عدم حذف Cache پس از Update

باعث Stale Data می‌شود.

---

## استفاده از LocMem در Production

اشتباه معماری.

---

## Cache کردن داده‌های حساس

ریسک امنیتی ایجاد می‌کند.

---

# Best Practices

1. از Redis استفاده کنید.
2. فقط داده‌های پرتکرار را Cache کنید.
3. برای Cache Key استاندارد تعریف کنید.
4. Cache Invalidation را از ابتدا طراحی کنید.
5. روی داده‌های کاربرمحور با احتیاط Cache اعمال کنید.
6. Cache را جایگزین Database ندانید.
7. نرخ Hit/Miss را مانیتور کنید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Cache چیست.
* تفاوت Cache و Database چیست.
* Redis چگونه به Django متصل می‌شود.
* Per-View Cache چیست.
* Low-Level Cache API چیست.
* Cache Key چیست.
* Cache Invalidation چیست.
* خطرات Cache روی داده‌های کاربرمحور چیست.
* بهترین روش‌های استفاده از Cache در Production چیست.

---

# نکات اضافی

در پروژه‌های DRF مدرن، صرفاً `cache_page()` معمولاً کافی نیست. بهتر است موارد زیر مطالعه شود:

```text
Cache Aside Pattern
Read Through Cache
Write Through Cache
Cache Invalidation Strategies
Redis Cluster
```

زیرا این مفاهیم در سامانه‌های بزرگ بسیار مهم‌تر از خود API Cache هستند.

---

فصل بعدی:

```text id="next-chapter"
12 - Exceptions
```

---

## منابع رسمی

* Caching

[DRF Caching Documentation](https://www.django-rest-framework.org/api-guide/caching/?utm_source=chatgpt.com)

