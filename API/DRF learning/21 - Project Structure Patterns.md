# 21 - Project Structure Patterns

## اهداف فصل

در پایان این فصل:

* تفاوت پروژه کوچک و بزرگ Django را درک می‌کنید.
* با ساختار استاندارد Appها آشنا می‌شوید.
* می‌دانید چه زمانی یک App جدید ایجاد کنید.
* با مفهوم Separation of Concerns آشنا می‌شوید.
* ساختار مناسب پروژه‌های DRF متوسط و بزرگ را می‌شناسید.
* با مزایا و معایب Service Layer آشنا می‌شوید.

---

# مقدمه

در آموزش‌های ابتدایی Django معمولاً پروژه‌ای شبیه زیر می‌بینیم:

```text
project/

├── books/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
└── config/
```

---

برای پروژه‌های آموزشی مناسب است.

اما وقتی پروژه رشد می‌کند:

```text
50 Model
100 API Endpoint
10 Developer
```

این ساختار به سرعت دشوار می‌شود.

---

# اصل مهم

یکی از اصول اصلی Django:

```text
Application Reusability
```

است.

---

طبق مستندات Django:

هر App باید:

```text
یک مسئولیت مشخص
و
مرز مشخص
```

داشته باشد.

---

# App چیست؟

اشتباه رایج:

```text
هر Model = یک App
```

---

اشتباه دیگر:

```text
کل سیستم = یک App
```

---

هر دو رویکرد معمولاً مشکل‌ساز هستند.

---

# نمونه مناسب

فرض کنید یک سامانه فروش کتاب داریم.

---

ساختار منطقی:

```text
accounts
books
orders
payments
notifications
```

---

هر App:

```text
یک دامنه کسب‌وکار
(Business Domain)
```

را پوشش می‌دهد.

---

# مثال نامناسب

```text
models_app

views_app

serializers_app
```

---

چرا اشتباه است؟

زیرا Appها باید:

```text
Business Based
```

باشند.

نه:

```text
Technical Based
```

---

# ساختار پیشنهادی پروژه

```text
MyProject/

├── config/
│
├── common/
│
├── accounts/
│
├── books/
│
├── orders/
│
├── notifications/
│
└── tests/
```

---

# نقش config

مسئول:

```text
Settings
URLs
WSGI
ASGI
```

---

نمونه:

```text
MyProject/config/

├── settings.py
├── urls.py
├── wsgi.py
└── asgi.py
```

---

# نقش common

محل کدهای مشترک.

---

نمونه:

```text
MyProject/common/
```

---

موارد مناسب:

```text
Permissions

Mixins

Exceptions

Utilities

Base Classes
```

---

# موارد نامناسب در common

```text
Business Logic
```

---

منطق کسب‌وکار باید داخل Domain خودش باشد.

---

# ساختار داخلی App

مثال:

```text
MyProject/books/
```

---

```text
books/

├── migrations/

├── models.py

├── serializers.py

├── views.py

├── urls.py

├── permissions.py

├── filters.py

├── tests/
```

---

این ساختار برای اکثر پروژه‌ها کافی است.

---

# چه زمانی فایل‌ها را تفکیک کنیم؟

اگر:

```text
views.py
```

به 1000 خط رسید:

---

می‌توانیم:

```text
books/views/

├── list.py
├── create.py
├── update.py
└── delete.py
```

بسازیم.

---

همین موضوع برای:

```text
serializers
permissions
services
```

نیز صادق است.

---

# ساختار URL

فایل:

```text
MyProject/books/urls.py
```

---

نمونه:

```python
urlpatterns = [
    ...
]
```

---

سپس:

فایل:

```text
MyProject/config/urls.py
```

---

```python
path(
    "api/books/",
    include(
        "books.urls"
    )
)
```

---

این الگو باعث می‌شود:

```text
هر App
مالک URLهای خودش باشد.
```

---

# Separation of Concerns

اصل مهم مهندسی نرم‌افزار:

```text
هر بخش
یک مسئولیت
```

---

نمونه:

Model:

```text
Data
```

---

Serializer:

```text
Validation
Transformation
```

---

View:

```text
HTTP Layer
```

---

Permission:

```text
Authorization
```

---

# اشتباه رایج

قرار دادن همه منطق در View

---

مثال:

```python
def post():
    validate()
    calculate()
    create_order()
    send_sms()
    update_wallet()
```

---

View تبدیل به:

```text
God Object
```

می‌شود.

---

# Service Layer چیست؟

در پروژه‌های بزرگ:

گاهی منطق کسب‌وکار از View جدا می‌شود.

---

نمونه:

```text
MyProject/orders/services/
```

---

```text
orders/services/

create_order.py

cancel_order.py

refund_order.py
```

---

# مزایای Service Layer

```text
Testability

Reusability

Maintainability
```

---

# نکته مهم

Service Layer:

```text
الزام Django نیست.
```

---

در مستندات رسمی Django وجود ندارد.

---

بلکه:

```text
Architectural Pattern
```

است.

---

# چه زمانی Service Layer استفاده کنیم؟

پروژه کوچک:

```text
خیر
```

---

پروژه متوسط:

```text
گاهی
```

---

پروژه بزرگ:

```text
معمولاً بله
```

---

# ساختار تست‌ها

پیشنهاد:

```text
books/

└── tests/

    ├── test_views.py
    ├── test_serializers.py
    ├── test_permissions.py
    └── test_services.py
```

---

# تنظیمات چند محیطی

وقتی پروژه رشد می‌کند:

---

بهتر است:

```text
settings/
```

داشته باشیم.

---

نمونه:

```text
MyProject/config/settings/

├── base.py
├── development.py
├── production.py
└── testing.py
```

---

مزایا:

```text
Isolation

Security

Maintainability
```

---

# Appهای مشترک

گاهی چند پروژه داریم.

---

در این شرایط:

```text
accounts
audit
notifications
```

---

می‌توانند:

```text
Reusable App
```

باشند.

---

این دقیقاً یکی از اهداف اصلی Django است.

---

# نشانه‌های ساختار ضعیف

اگر مشاهده کردید:

```text
views.py = 5000 lines

models.py = 3000 lines

circular import

duplicate code
```

---

احتمالاً زمان بازنگری ساختار رسیده است.

---

# Best Practices

1. Appها را بر اساس Business Domain طراحی کنید.
2. هر App مسئولیت مشخص داشته باشد.
3. از common برای کدهای مشترک استفاده کنید.
4. URLها را داخل App نگه دارید.
5. از God View و God Serializer اجتناب کنید.
6. فقط در صورت نیاز Service Layer اضافه کنید.
7. ساختار پروژه را متناسب با اندازه پروژه توسعه دهید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* App چیست.
* چگونه Appها را طراحی کنیم.
* ساختار مناسب پروژه‌های DRF چیست.
* Separation of Concerns چیست.
* Service Layer چیست.
* چه زمانی فایل‌ها را تفکیک کنیم.
* چه زمانی ساختار پروژه نیاز به بازنگری دارد.

---

# نکته مهم

طبق مستندات رسمی Django:

```text
Appها باید
قابل استفاده مجدد،
مستقل
و دارای مسئولیت مشخص باشند.
```

اما درباره:

```text
Service Layer
Repository Pattern
```

باید بدانید که این‌ها الگوهای معماری هستند و بخشی از استاندارد رسمی Django محسوب نمی‌شوند.

---

فصل بعدی:

```text
22 - Performance Optimization
```

---

## منابع رسمی

* [Django Applications Documentation](https://docs.djangoproject.com/en/stable/ref/applications/?utm_source=chatgpt.com)
* [Django Reusable Apps Documentation](https://docs.djangoproject.com/en/stable/intro/reusable-apps/?utm_source=chatgpt.com)

