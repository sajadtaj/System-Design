# 15 - Content Negotiation

## اهداف فصل

در پایان این فصل:

* مفهوم Content Negotiation را درک می‌کنید.
* نقش Renderer و Parser را می‌شناسید.
* با Headerهای `Accept` و `Content-Type` آشنا می‌شوید.
* نحوه انتخاب فرمت Response در DRF را می‌فهمید.
* می‌دانید چرا اکثر APIهای مدرن فقط JSON ارائه می‌کنند.

---

# Content Negotiation چیست؟

Content Negotiation یعنی:

```text
توافق بین Client و Server
برای فرمت تبادل داده
```

---

به زبان ساده:

Client می‌گوید:

```text
من دوست دارم پاسخ را با این فرمت دریافت کنم.
```

---

و Server تصمیم می‌گیرد:

```text
آیا این فرمت را پشتیبانی می‌کنم یا خیر؟
```

---

# مثال

Client:

```http
GET /api/books/

Accept: application/json
```

---

Server:

```http
200 OK

Content-Type: application/json
```

---

پاسخ:

```json
{
    "id": 1,
    "title": "DRF"
}
```

---

# دو Header مهم

## Accept

مشخص می‌کند:

```text
Client چه فرمتی می‌خواهد.
```

---

مثال:

```http
Accept: application/json
```

---

یا:

```http
Accept: text/html
```

---

## Content-Type

مشخص می‌کند:

```text
بدنه Request یا Response
چه فرمتی دارد.
```

---

مثال:

```http
Content-Type: application/json
```

---

# تفاوت Accept و Content-Type

| Header       | کاربرد                |
| ------------ | --------------------- |
| Accept       | فرمت پاسخ مورد انتظار |
| Content-Type | فرمت داده ارسالی      |

---

مثال:

```http
POST /api/books/

Content-Type: application/json
Accept: application/json
```

---

یعنی:

```text
من JSON ارسال می‌کنم
و JSON هم دریافت می‌کنم.
```

---

# Renderer چیست؟

Renderer مسئول تولید Response است.

---

مثال:

```python
Book Object
```

↓

```python
BookSerializer
```

↓

```python
JSONRenderer
```

↓

```json
{
    "id": 1,
    "title": "DRF"
}
```

---

# Rendererهای پیش‌فرض DRF

معمولاً:

```python
JSONRenderer
BrowsableAPIRenderer
```

---

فعال هستند.

---

# JSONRenderer

رایج‌ترین Renderer.

---

خروجی:

```json
{
    "title": "DRF"
}
```

---

در اکثر پروژه‌های Production فقط همین Renderer استفاده می‌شود.

---

# BrowsableAPIRenderer

قابلیت مشهور DRF.

---

به جای JSON:

```json
{
    "title": "DRF"
}
```

---

یک رابط HTML تولید می‌کند.

---

مزیت:

* تست سریع API
* مشاهده Endpointها
* ارسال Request بدون Postman

---

# مشاهده Renderer فعال

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_RENDERER_CLASSES": [

        "rest_framework.renderers.JSONRenderer",

        "rest_framework.renderers.BrowsableAPIRenderer",
    ]
}
```

---

# محدود کردن Rendererها

در محیط Production گاهی فقط JSON فعال می‌شود.

---

فایل:

```text
MyProject/config/settings.py
```

```python
REST_FRAMEWORK = {

    "DEFAULT_RENDERER_CLASSES": [

        "rest_framework.renderers.JSONRenderer",
    ]
}
```

---

نتیجه:

```text
Browsable API غیرفعال می‌شود.
```

---

# Renderer در سطح View

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.renderers import (
    JSONRenderer
)
```

---

```python
class BookAPIView(
    APIView
):

    renderer_classes = [
        JSONRenderer
    ]
```

---

این View فقط JSON تولید می‌کند.

---

# Parser چیست؟

Parser برعکس Renderer عمل می‌کند.

---

وظیفه:

```text
تبدیل Request
به داده قابل استفاده در Python
```

---

مسیر:

```text
Request
    ↓
JSONParser
    ↓
Python Dictionary
```

---

# مثال

Client:

```json
{
    "title": "DRF"
}
```

---

Parser:

```python
{
    "title": "DRF"
}
```

---

سپس:

```python
request.data
```

در اختیار View قرار می‌گیرد.

---

# JSONParser

رایج‌ترین Parser.

---

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.parsers import (
    JSONParser
)
```

---

```python
class BookAPIView(
    APIView
):

    parser_classes = [
        JSONParser
    ]
```

---

# انتخاب Renderer توسط DRF

فرض کنید:

```http
Accept: application/json
```

---

DRF بررسی می‌کند:

```text
آیا JSONRenderer وجود دارد؟
```

---

اگر بله:

```text
JSON Response
```

برمی‌گرداند.

---

اگر خیر:

```http
406 Not Acceptable
```

برمی‌گرداند.

---

# 406 Not Acceptable

مثال:

Client:

```http
Accept: application/xml
```

---

اما API فقط:

```text
application/json
```

را پشتیبانی می‌کند.

---

پاسخ:

```http
406 Not Acceptable
```

---

# 415 Unsupported Media Type

مثال:

```http
Content-Type: application/xml
```

---

در حالی که فقط:

```text
application/json
```

پذیرفته می‌شود.

---

پاسخ:

```http
415 Unsupported Media Type
```

---

# چرا JSON استاندارد شده است؟

مزایا:

* سبک
* سریع
* خوانا
* پشتیبانی گسترده
* سازگاری عالی با JavaScript

---

به همین دلیل تقریباً تمام APIهای مدرن:

```text
JSON First
```

هستند.

---

# ارتباط با فصل بعد

گاهی Client علاوه بر Header از URL نیز فرمت را مشخص می‌کند.

مثال:

```http
/api/books.json
```

یا:

```http
/api/books.api
```

---

این قابلیت در DRF با:

```python
format_suffix_patterns()
```

پیاده‌سازی می‌شود.

---

موضوع فصل بعد:

```text
Format Suffixes
```

---

# Best Practices

1. JSON را فرمت اصلی API قرار دهید.
2. از Rendererهای غیرضروری استفاده نکنید.
3. در Production معمولاً فقط JSON کافی است.
4. تفاوت Accept و Content-Type را به خوبی درک کنید.
5. برای APIهای عمومی، پاسخ 406 و 415 را بشناسید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Content Negotiation چیست.
* Accept Header چیست.
* Content-Type چیست.
* Renderer چیست.
* Parser چیست.
* JSONRenderer چگونه کار می‌کند.
* Browsable API چه کاربردی دارد.
* 406 و 415 چه زمانی رخ می‌دهند.

---

فصل بعدی:

```text
16 - Format Suffixes
```

---

## منابع رسمی

* Content Negotiation

[DRF Content Negotiation Documentation](https://www.django-rest-framework.org/api-guide/content-negotiation/?utm_source=chatgpt.com)

