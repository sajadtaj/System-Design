# 20 - Production Architecture

## اهداف فصل

در پایان این فصل:

* تفاوت پروژه آموزشی و Production را درک می‌کنید.
* معماری مناسب برای پروژه‌های واقعی DRF را می‌شناسید.
* جایگاه Redis، Celery، PostgreSQL و JWT را در معماری درک می‌کنید.
* با ساختار پیشنهادی پروژه‌های بزرگ آشنا می‌شوید.
* مهم‌ترین چک‌لیست استقرار Production را خواهید داشت.

---

# مقدمه

تا اینجا تقریباً تمام اجزای اصلی DRF را یاد گرفتیم.

اما هنوز یک سؤال مهم باقی مانده است:

```text id="p1"
چگونه یک API واقعی و قابل نگهداری بسازیم؟
```

---

بسیاری از آموزش‌ها در این نقطه تمام می‌شوند.

اما در دنیای واقعی:

```text id="p2"
Authentication
Permission
Serializer
View
```

فقط بخشی از سیستم هستند.

---

# معماری کلی یک سیستم Production

```text id="p3"
Client

    ↓

Nginx

    ↓

Gunicorn

    ↓

Django + DRF

    ↓

PostgreSQL

    ↓

Redis

    ↓

Celery Workers
```

---

# نقش هر بخش

## Client

می‌تواند:

* Flutter
* React
* Angular
* Mobile App
* Service-to-Service

باشد.

---

## Nginx

وظایف:

```text id="p4"
Reverse Proxy

SSL Termination

Static Files

Load Balancing
```

---

## Gunicorn

وظیفه:

```text id="p5"
اجرای Django
```

در محیط Production.

---

## Django + DRF

مسئول:

```text id="p6"
Business Logic

Authentication

Permissions

API Layer
```

---

## PostgreSQL

پایگاه داده اصلی.

---

در اکثر پروژه‌های DRF:

```text id="p7"
PostgreSQL
```

انتخاب استاندارد است.

---

## Redis

کاربردها:

```text id="p8"
Caching

Celery Broker

Rate Limiting

Session Storage
```

---

## Celery

برای عملیات زمان‌بر:

```text id="p9"
Email

SMS

Report Generation

Data Processing
```

---

# ساختار پیشنهادی پروژه

نمونه:

```text id="p10"
MyProject/

├── config/
│
├── common/
│
├── accounts/
│
├── books/
│
├── notifications/
│
├── services/
│
├── tests/
│
└── requirements/
```

---

# نقش Appها

نمونه:

```text id="p11"
accounts
```

برای:

```text id="p12"
Authentication
User Management
```

---

```text id="p13"
books
```

برای:

```text id="p14"
Book Domain
```

---

هر App باید:

```text id="p15"
یک مسئولیت مشخص
```

داشته باشد.

---

# ساختار داخلی App

مثال:

```text id="p16"
books/

├── models.py
├── serializers.py
├── views.py
├── permissions.py
├── filters.py
├── urls.py
├── tests/
```

---

# چه زمانی Service Layer ایجاد کنیم؟

در پروژه‌های کوچک:

```text id="p17"
نیازی نیست.
```

---

در پروژه‌های متوسط و بزرگ:

```text id="p18"
Business Logic
```

نباید داخل View قرار گیرد.

---

مثال:

```text id="p19"
books/services/
```

---

```python id="p20"
create_book()

publish_book()

archive_book()
```

---

مزایا:

* تست‌پذیری بیشتر
* کد تمیزتر
* استفاده مجدد

---

# Authentication در Production

پیشنهاد:

```text id="p21"
JWT
+
Refresh Token
```

---

بر اساس فصل:

```text id="p22"
06.1
```

---

همراه با:

```text id="p23"
Token Rotation

Blacklist
```

در صورت نیاز.

---

# Permission Strategy

پیشنهاد:

```text id="p24"
IsAuthenticated
```

به عنوان پیش‌فرض.

---

سپس:

```text id="p25"
Custom Permissions
```

برای قوانین کسب‌وکار.

---

# Pagination

برای Endpointهای لیستی:

```text id="p26"
همیشه فعال باشد.
```

---

اشتباه:

```http id="p27"
GET /api/books/
```

و بازگرداندن:

```text id="p28"
100000 رکورد
```

---

# Filtering

Endpointهای لیستی باید:

```text id="p29"
Filter
Search
Ordering
```

داشته باشند.

---

# Caching

از فصل Caching:

---

برای:

```text id="p30"
Read Heavy APIs
```

بسیار مهم است.

---

نمونه:

```text id="p31"
Redis Cache
```

---

# Throttling

از فصل Throttling:

---

برای جلوگیری از:

```text id="p32"
Abuse

Spam

Brute Force
```

---

# Logging

هر پروژه Production باید Logging داشته باشد.

---

حداقل:

```text id="p33"
INFO

WARNING

ERROR
```

---

ثبت شوند.

---

نمونه:

```text id="p34"
logs/

app.log

error.log
```

---

# Monitoring

اگر Monitoring نداشته باشید:

```text id="p35"
از خرابی سیستم
بعد از کاربران
مطلع می‌شوید.
```

---

ابزارهای رایج:

* Prometheus
* Grafana
* Sentry

---

# Exception Handling

همان فصل Exceptions.

---

هدف:

```text id="p36"
پاسخ‌های یکنواخت
```

---

مثال:

```json id="p37"
{
    "error": {
        "code": "validation_error",
        "message": "..."
    }
}
```

---

# Documentation

همان فصل Schema.

---

پیشنهاد:

```text id="p38"
drf-spectacular
```

---

و:

```text id="p39"
Swagger
```

---

# Testing

حداقل:

```text id="p40"
Authentication

Permissions

Critical APIs
```

باید تست شوند.

---

# Docker

در پروژه‌های جدید:

```text id="p41"
Docker
```

تقریباً استاندارد است.

---

نمونه سرویس‌ها:

```text id="p42"
django

postgres

redis

celery

nginx
```

---

# تنظیمات Environment

فایل:

```text id="p43"
.env
```

---

نمونه:

```env id="p44"
DEBUG=False

SECRET_KEY=...

DB_NAME=...

DB_USER=...

DB_PASSWORD=...
```

---

هرگز:

```text id="p45"
Secret
Password
Token
```

را داخل Git قرار ندهید.

---

# چک‌لیست Production

قبل از انتشار:

---

## امنیت

```text id="p46"
DEBUG=False

HTTPS Enabled

Strong Secret Key

Secure Cookies
```

---

## پایگاه داده

```text id="p47"
Backup Strategy

Indexes

Connection Pooling
```

---

## API

```text id="p48"
Authentication

Permissions

Pagination

Filtering

Throttling
```

---

## کیفیت

```text id="p49"
Tests

Logging

Monitoring

Documentation
```

---

## استقرار

```text id="p50"
Docker

Nginx

Gunicorn
```

---

# اشتباهات رایج

## Business Logic داخل View

اشتباه رایج پروژه‌های در حال رشد.

---

## نداشتن تست

در ابتدا مشکلی دیده نمی‌شود.

اما با رشد پروژه هزینه زیادی ایجاد می‌کند.

---

## فعال بودن DEBUG

یکی از خطرناک‌ترین اشتباهات Production.

---

## نداشتن Logging

رفع خطا را بسیار دشوار می‌کند.

---

## نداشتن Backup

ممکن است کل داده‌های سیستم از بین بروند.

---

# معماری پیشنهادی برای اکثر پروژه‌های DRF

```text id="p51"
Django + DRF

PostgreSQL

Redis

Celery

JWT

Docker

Nginx

Swagger
```

---

این ترکیب برای بخش بزرگی از:

* استارتاپ‌ها
* سامانه‌های سازمانی
* پنل‌های مدیریتی
* سرویس‌های B2B

کافی و قابل اتکا است.

---

# جمع‌بندی نهایی کتاب

در این کتاب با مهم‌ترین مفاهیم DRF آشنا شدیم:

```text id="p52"
Serializers

Views

Generic Views

ViewSets

Routers

Authentication

Permissions

JWT

Filtering

Pagination

Caching

Throttling

Versioning

Exceptions

Status Codes

Content Negotiation

Metadata

Schemas

Testing
```

---

و در نهایت یاد گرفتیم:

```text id="p53"
هدف DRF فقط ساخت Endpoint نیست.

هدف ساخت APIهای
قابل توسعه،
قابل نگهداری،
امن
و Production-Ready است.
```

---

## منابع تکمیلی

* [Django REST Framework Official Documentation](https://www.django-rest-framework.org/?utm_source=chatgpt.com)
* [Simple JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/?utm_source=chatgpt.com)

