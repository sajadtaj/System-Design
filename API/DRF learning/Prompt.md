پیشنهاد می‌کنم یک «کامند پروژه» تعریف کنیم که هر زمان آن را در ابتدای گفتگو بنویسی، کل ساختار، ترتیب فصل‌ها، سطح توضیحات و منابع به من یادآوری شود.

مثلاً:

DRF-BOOK

هدف:
تولید یک مستند آموزشی فارسی برای Django REST Framework به صورت گام‌به‌گام، ساده، عملی و مبتنی بر مستندات رسمی.

قواعد کلی:

* آموزش به زبان فارسی روان و فنی
* مناسب برنامه‌نویس Django
* هر فصل مستقل و قابل مطالعه باشد
* ابتدا مفهوم سپس پیاده‌سازی
* استفاده از مثال‌های واقعی
* استفاده از Best Practice های رسمی DRF
* محتوای رسمی مستندات در متن ادغام شود نه صرفاً ترجمه
* از پیچیدگی غیرضروری اجتناب شود
* ابتدا توضیح مفهومی سپس کد
* کدها کامل و قابل اجرا باشند
* اگر کد بخشی از ادامه یک مسیر یا پروژه یا توضیخات است حتما با ادرس محل ان باشد مثلا:

My project/account_module/views.py
تا خواننده در مسیر کدها گم نشود.

ساختار ثابت همه فصل‌ها:

# عنوان فصل

## اهداف فصل

## مقدمه

## مسئله‌ای که حل می‌کند

## جایگاه در معماری DRF

## پیاده‌سازی پایه

## مثال عملی

## تنظیمات و گزینه‌های مهم

## انواع و حالت‌های مختلف

## خطاها و نکات رایج

## Best Practices

## جمع‌بندی

## منابع رسمی

فصل‌ها:

00- Whats DRF

01- Installation

02- Serializers

03- Generic Views

04- ViewSets and Routers

05- Authentication

06- Permissions

07- Filtering

08- Pagination

09- Versioning

10- Throttling

12- Exceptions

11- Caching

13- Status Codes

14 - Reverse and URL Design

15 - Content Negotiation

16 - Format Suffixes

17 - Metadata

18 - Schemas

19 - Testing

20 - Production Architecture

منابع رسمی:

[https://www.django-rest-framework.org/api-guide/generic-views/](https://www.django-rest-framework.org/api-guide/generic-views/)

[https://www.django-rest-framework.org/api-guide/routers/](https://www.django-rest-framework.org/api-guide/routers/)

[https://www.django-rest-framework.org/api-guide/serializers/](https://www.django-rest-framework.org/api-guide/serializers/)

[https://www.django-rest-framework.org/api-guide/fields/](https://www.django-rest-framework.org/api-guide/fields/)

[https://www.django-rest-framework.org/api-guide/relations/](https://www.django-rest-framework.org/api-guide/relations/)

[https://www.django-rest-framework.org/api-guide/authentication/](https://www.django-rest-framework.org/api-guide/authentication/)

[https://www.django-rest-framework.org/api-guide/permissions/](https://www.django-rest-framework.org/api-guide/permissions/)

[https://www.django-rest-framework.org/api-guide/caching/](https://www.django-rest-framework.org/api-guide/caching/)

[https://www.django-rest-framework.org/api-guide/throttling/](https://www.django-rest-framework.org/api-guide/throttling/)

[https://www.django-rest-framework.org/api-guide/filtering/](https://www.django-rest-framework.org/api-guide/filtering/)

[https://www.django-rest-framework.org/api-guide/pagination/](https://www.django-rest-framework.org/api-guide/pagination/)

[https://www.django-rest-framework.org/api-guide/versioning/](https://www.django-rest-framework.org/api-guide/versioning/)

[https://www.django-rest-framework.org/api-guide/content-negotiation/](https://www.django-rest-framework.org/api-guide/content-negotiation/)

[https://www.django-rest-framework.org/api-guide/metadata/](https://www.django-rest-framework.org/api-guide/metadata/)

[https://www.django-rest-framework.org/api-guide/schemas/](https://www.django-rest-framework.org/api-guide/schemas/)

[https://www.django-rest-framework.org/api-guide/reverse/](https://www.django-rest-framework.org/api-guide/reverse/)

[https://www.django-rest-framework.org/api-guide/format-suffixes/](https://www.django-rest-framework.org/api-guide/format-suffixes/)

[https://www.django-rest-framework.org/api-guide/exceptions/](https://www.django-rest-framework.org/api-guide/exceptions/)

[https://www.django-rest-framework.org/api-guide/status-codes/](https://www.django-rest-framework.org/api-guide/status-codes/)

[https://www.django-rest-framework.org/api-guide/testing/](https://www.django-rest-framework.org/api-guide/testing/)

نحوه ادامه کار:

اگر کاربر بنویسد:

DRF-BOOK -> 02

باید فصل 02 (Serializers) تولید شود.

اگر کاربر بنویسد:

DRF-BOOK -> 05

باید فصل Authentication تولید شود.

اگر کاربر بنویسد:

DRF-BOOK -> NEXT

باید فصل بعدی تولید شود.

اگر کاربر بنویسد:

DRF-BOOK -> REVIEW

باید فصل فعلی بازبینی و تکمیل شود.

بعد از این کافی است در گفتگوهای بعدی فقط بنویسی:

```text
DRF-BOOK -> 02
```

یا

```text
DRF-BOOK -> NEXT
```

و عملاً کل قرارداد پروژه برای تولید فصل‌ها مشخص خواهد بود.

