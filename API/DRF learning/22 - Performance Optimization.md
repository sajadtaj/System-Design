# 22 - Performance Optimization

## اهداف فصل

در پایان این فصل:

* مهم‌ترین گلوگاه‌های عملکرد در DRF را می‌شناسید.
* مشکل N+1 Query را درک می‌کنید.
* با `select_related()` و `prefetch_related()` آشنا می‌شوید.
* هزینه Serializerها را درک می‌کنید.
* تأثیر Pagination را می‌شناسید.
* با اصول بهینه‌سازی Queryها آشنا می‌شوید.
* می‌دانید قبل از Cache چه چیزهایی باید اصلاح شوند.

---

# مقدمه

بسیاری از توسعه‌دهندگان وقتی API کند می‌شود مستقیماً سراغ:

```text id="p1"
Redis
Cache
More CPU
```

می‌روند.

---

اما در اکثر پروژه‌های Django مشکل اصلی:

```text id="p2"
Database Queries
```

است.

---

طبق مستندات Django:

```text id="p3"
اول Queryها را اصلاح کنید،
بعد سراغ Cache بروید.
```

---

# قانون طلایی

قبل از هر بهینه‌سازی:

```text id="p4"
اندازه‌گیری کنید.
```

---

بدون اندازه‌گیری:

```text id="p5"
Optimization
=
Guessing
```

---

# رایج‌ترین مشکل DRF

## N+1 Query Problem

فرض کنید:

فایل:

```text id="p6"
MyProject/books/models.py
```

```python id="p7"
class Author(models.Model):
    name = models.CharField(...)
```

---

```python id="p8"
class Book(models.Model):

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
```

---

Serializer:

فایل:

```text id="p9"
MyProject/books/serializers.py
```

```python id="p10"
class BookSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Book
        fields = "__all__"
```

---

View:

فایل:

```text id="p11"
MyProject/books/views.py
```

```python id="p12"
queryset = Book.objects.all()
```

---

فرض کنید:

```text id="p13"
100 Book
```

داریم.

---

DRF ابتدا:

```sql id="p14"
SELECT * FROM books
```

---

سپس برای هر کتاب:

```sql id="p15"
SELECT * FROM authors
```

اجرا می‌کند.

---

نتیجه:

```text id="p16"
1 + 100 Query
```

---

این همان:

```text id="p17"
N+1 Problem
```

است.

---

# حل مشکل با select_related

فایل:

```text id="p18"
MyProject/books/views.py
```

```python id="p19"
queryset = (
    Book.objects
    .select_related(
        "author"
    )
)
```

---

اکنون:

```text id="p20"
1 Query
```

به جای:

```text id="p21"
101 Query
```

اجرا می‌شود.

---

# چه زمانی select_related؟

برای:

```text id="p22"
ForeignKey

OneToOneField
```

---

استفاده می‌شود.

---

# prefetch_related

برای:

```text id="p23"
ManyToMany

Reverse ForeignKey
```

---

استفاده می‌شود.

---

مثال:

```python id="p24"
queryset = (
    Book.objects
    .prefetch_related(
        "tags"
    )
)
```

---

# تفاوت select_related و prefetch_related

| ابزار            | نوع رابطه        |
| ---------------- | ---------------- |
| select_related   | ForeignKey       |
| select_related   | OneToOne         |
| prefetch_related | ManyToMany       |
| prefetch_related | Reverse Relation |

---

# توصیه رسمی DRF

در مستندات Generic Views آمده است:

```text id="p25"
برای جلوگیری از N+1
از select_related و prefetch_related استفاده کنید.
```

---

# Serializer Cost

گاهی مشکل از Query نیست.

---

مشکل:

```text id="p26"
Serializer
```

است.

---

مثال:

```python id="p27"
class BookSerializer(
    ModelSerializer
):
```

---

برای چند رکورد مناسب است.

---

اما برای:

```text id="p28"
100000 Row
```

ممکن است هزینه‌بر باشد.

---

# SerializerMethodField

بسیار مفید است.

اما باید با احتیاط استفاده شود.

---

مثال:

```python id="p29"
book_count = (
    serializers
    .SerializerMethodField()
)
```

---

```python id="p30"
def get_book_count(
    self,
    obj
):
    ...
```

---

اگر داخل آن Query اجرا شود:

```text id="p31"
N+1 Query
```

دوباره ایجاد می‌شود.

---

# فقط داده مورد نیاز را برگردانید

اشتباه:

```python id="p32"
fields = "__all__"
```

---

در حالی که Client فقط:

```text id="p33"
id
title
```

نیاز دارد.

---

بهتر:

```python id="p34"
fields = [
    "id",
    "title"
]
```

---

# Pagination

یکی از مهم‌ترین ابزارهای Performance.

---

اشتباه:

```http id="p35"
GET /api/books/
```

---

بازگشت:

```text id="p36"
50000 Record
```

---

درست:

```http id="p37"
GET /api/books/?page=1
```

---

مثلاً:

```text id="p38"
20 Record
```

---

# Filtering

بدون Filter:

```text id="p39"
کل جدول
```

خوانده می‌شود.

---

با Filter:

```http id="p40"
GET /books/?title=django
```

---

بار سیستم کاهش می‌یابد.

---

# Index

یکی از مهم‌ترین موضوعات پایگاه داده.

---

مثال:

```python id="p41"
email = models.EmailField(
    unique=True
)
```

---

یا:

```python id="p42"
db_index=True
```

---

Index مناسب:

```text id="p43"
سرعت Query
```

را به شدت افزایش می‌دهد.

---

# QuerySet Evaluation

QuerySetها:

```text id="p44"
Lazy
```

هستند.

---

مثال:

```python id="p45"
books = Book.objects.all()
```

---

هنوز Query اجرا نشده است.

---

وقتی:

```python id="p46"
list(books)
```

یا:

```python id="p47"
for book in books
```

انجام شود:

Query اجرا می‌شود.

---

# count()

اشتباه:

```python id="p48"
len(queryset)
```

---

بهتر:

```python id="p49"
queryset.count()
```

---

زیرا:

```sql id="p50"
COUNT(*)
```

در پایگاه داده اجرا می‌شود.

---

# exists()

اشتباه:

```python id="p51"
if queryset:
```

---

بهتر:

```python id="p52"
queryset.exists()
```

---

زیرا:

```sql id="p53"
SELECT EXISTS(...)
```

سریع‌تر است.

---

# Cache آخرین مرحله است

اشتباه رایج:

```text id="p54"
مشکل Query
↓
Redis
```

---

ابتدا:

```text id="p55"
Query Optimization
```

---

سپس:

```text id="p56"
Caching
```

---

# ابزارهای بررسی عملکرد

برای توسعه:

```text id="p57"
Django Debug Toolbar
```

---

نمایش می‌دهد:

* تعداد Queryها
* زمان Queryها
* Queryهای تکراری

---

# چه چیزی را اندازه‌گیری کنیم؟

حداقل:

```text id="p58"
Response Time

Query Count

Memory Usage
```

---

# اشتباهات رایج

## fields="**all**"

بدون نیاز واقعی.

---

## SerializerMethodField با Query

منبع بسیاری از مشکلات عملکرد.

---

## نداشتن Pagination

در Endpointهای لیستی.

---

## Cache قبل از اصلاح Query

یکی از رایج‌ترین اشتباهات.

---

## عدم استفاده از Index

در ستون‌های پرتکرار.

---

# Best Practices

1. ابتدا Queryها را بررسی کنید.
2. N+1 Query را حذف کنید.
3. از select_related استفاده کنید.
4. از prefetch_related استفاده کنید.
5. Pagination را فعال کنید.
6. فقط داده مورد نیاز را برگردانید.
7. قبل از Cache، Queryها را اصلاح کنید.
8. Query Count را اندازه‌گیری کنید.
9. روی ستون‌های مناسب Index ایجاد کنید.

---

# چک‌لیست Performance Review

برای هر Endpoint:

```text id="p59"
✓ Pagination دارد؟

✓ Filtering دارد؟

✓ N+1 Query ندارد؟

✓ select_related استفاده شده؟

✓ prefetch_related استفاده شده؟

✓ Serializer سبک است؟

✓ Index مناسب وجود دارد؟

✓ Query Count اندازه‌گیری شده؟
```

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* N+1 Query چیست.
* select_related چیست.
* prefetch_related چیست.
* Serializer چگونه روی عملکرد اثر می‌گذارد.
* Pagination چرا مهم است.
* نقش Index چیست.
* چرا Cache آخرین مرحله بهینه‌سازی است.

---

# مهم‌ترین نکته فصل

در اکثر پروژه‌های DRF:

```text id="p60"
بزرگ‌ترین مشکل عملکرد

Redis نیست،
سرور نیست،
CPU نیست،

بلکه Queryهای نامناسب پایگاه داده است.
```

---

فصل بعدی:

```text id="p61"
23 - Security Checklist
```

---

## منابع رسمی

* [Django Database Optimization Documentation](https://docs.djangoproject.com/en/stable/topics/db/optimization/?utm_source=chatgpt.com)
* [Django QuerySet API Reference](https://docs.djangoproject.com/en/stable/ref/models/querysets/?utm_source=chatgpt.com)
* [DRF Generic Views Documentation (Avoiding N+1 Queries)](https://www.django-rest-framework.org/api-guide/generic-views/?utm_source=chatgpt.com)

