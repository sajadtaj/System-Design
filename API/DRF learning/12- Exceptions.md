# 12 - Exceptions

## اهداف فصل

در پایان این فصل:

* مفهوم Exception را در DRF درک می‌کنید.
* تفاوت Exception و Error را می‌فهمید.
* Exception Handler پیش‌فرض DRF را می‌شناسید.
* Exceptionهای رایج DRF را یاد می‌گیرید.
* Custom Exception می‌نویسید.
* Custom Exception Handler پیاده‌سازی می‌کنید.
* ساختار استاندارد خطا در API را طراحی می‌کنید.
* Best Practiceهای مدیریت خطا را یاد می‌گیرید.

---

# مقدمه

فرض کنید API زیر را داریم:

فایل:

```text
MyProject/books/views.py
```

```python
class BookAPIView(APIView):

    def get(
        self,
        request,
        book_id
    ):
        ...
```

---

درخواست:

```http
GET /api/books/999999/
```

---

اما:

```text
Book ID = 999999
```

وجود ندارد.

---

چه اتفاقی باید بیفتد؟

---

آیا باید:

```json
{
    "success": false
}
```

برگردانیم؟

---

یا:

```http
404 Not Found
```

؟

---

پاسخ:

```text
Exception Handling
```

---

# Exception چیست؟

Exception یعنی:

```text
شرایط غیرعادی
در زمان اجرای برنامه
```

---

مثال:

```text
Object Not Found
```

---

```text
Permission Denied
```

---

```text
Validation Error
```

---

```text
Authentication Failed
```

---

# Error و Exception

معمولاً این دو واژه اشتباه استفاده می‌شوند.

---

## Error

مشکل برنامه‌نویسی.

مثال:

```python
x = 10 / 0
```

---

```text
ZeroDivisionError
```

---

یا:

```python
print(a)
```

---

```text
NameError
```

---

## Exception

شرایط قابل مدیریت.

مثال:

```text
کاربر وجود ندارد
```

---

یا:

```text
رمز عبور اشتباه است
```

---

# مسیر Exception در DRF

```text
Request
    ↓
View
    ↓
Exception
    ↓
Exception Handler
    ↓
Response
```

---

# Exception Handler چیست؟

DRF به صورت خودکار Exceptionها را گرفته و تبدیل به:

```http
Response
```

می‌کند.

---

مثال:

```python
raise NotFound()
```

---

خروجی:

```http
404 Not Found
```

---

```json
{
    "detail": "Not found."
}
```

---

# APIException

تمام Exceptionهای DRF از:

```python
rest_framework.exceptions.APIException
```

مشتق می‌شوند.

---

ساختار:

```python
from rest_framework.exceptions import (
    APIException
)
```

---

```python
class MyException(
    APIException
):
    pass
```

---

# ValidationError

یکی از پرکاربردترین Exceptionها.

---

مثال:

فایل:

```text
MyProject/books/serializers.py
```

```python
from rest_framework import (
    serializers
)
```

---

```python
class BookSerializer(
    serializers.Serializer
):

    title = (
        serializers.CharField()
    )

    def validate_title(
        self,
        value
    ):

        if len(value) < 3:

            raise serializers.ValidationError(
                "Title is too short."
            )

        return value
```

---

پاسخ:

```http
400 Bad Request
```

---

```json
{
    "title": [
        "Title is too short."
    ]
}
```

---

# NotFound

برای رکوردهای پیدا نشده.

---

فایل:

```text
MyProject/books/views.py
```

```python
from rest_framework.exceptions import (
    NotFound
)
```

---

```python
raise NotFound()
```

---

پاسخ:

```http
404 Not Found
```

---

```json
{
    "detail": "Not found."
}
```

---

# PermissionDenied

زمانی که کاربر مجاز نیست.

---

```python
from rest_framework.exceptions import (
    PermissionDenied
)
```

---

```python
raise PermissionDenied()
```

---

پاسخ:

```http
403 Forbidden
```

---

```json
{
    "detail":
        "You do not have permission."
}
```

---

# AuthenticationFailed

خطای احراز هویت.

---

```python
from rest_framework.exceptions import (
    AuthenticationFailed
)
```

---

```python
raise AuthenticationFailed()
```

---

پاسخ:

```http
401 Unauthorized
```

---

```json
{
    "detail":
        "Incorrect authentication credentials."
}
```

---

# ParseError

خطای JSON یا Body.

---

مثال:

```json
{
    "title":
```

---

JSON ناقص است.

---

پاسخ:

```http
400 Bad Request
```

---

```json
{
    "detail":
        "JSON parse error."
}
```

---

# MethodNotAllowed

مثال:

```http
POST /api/books/
```

---

اما View فقط:

```http
GET
```

را پشتیبانی می‌کند.

---

پاسخ:

```http
405 Method Not Allowed
```

---

# Throttled

از فصل قبل.

---

مثال:

```http
429 Too Many Requests
```

---

```python
raise Throttled()
```

---

# ساخت Custom Exception

فایل:

```text
MyProject/common/exceptions.py
```

---

```python
from rest_framework.exceptions import (
    APIException
)
```

---

```python
class BookLimitExceeded(
    APIException
):

    status_code = 400

    default_detail = (
        "Book limit exceeded."
    )

    default_code = (
        "book_limit_exceeded"
    )
```

---

استفاده:

```python
raise BookLimitExceeded()
```

---

پاسخ:

```json
{
    "detail":
        "Book limit exceeded."
}
```

---

# Custom Message

```python
raise BookLimitExceeded(
    "Maximum books reached."
)
```

---

# Exception Handler سفارشی

گاهی خروجی پیش‌فرض کافی نیست.

---

مثال:

می‌خواهیم تمام خطاها:

```json
{
    "success": false,
    "error": "...",
    "status": 400
}
```

برگردانند.

---

# ساخت Handler

فایل:

```text
MyProject/common/exception_handlers.py
```

---

```python
from rest_framework.views import (
    exception_handler
)
```

---

```python
def custom_exception_handler(
    exc,
    context
):

    response = (
        exception_handler(
            exc,
            context
        )
    )

    if response is None:
        return response

    response.data = {

        "success": False,

        "status":
            response.status_code,

        "error":
            response.data
    }

    return response
```

---

# فعال‌سازی Handler

فایل:

```text
MyProject/config/settings.py
```

---

```python
REST_FRAMEWORK = {

    "EXCEPTION_HANDLER":

        "common.exception_handlers.custom_exception_handler"
}
```

---

# نتیجه

قبل:

```json
{
    "detail":
        "Not found."
}
```

---

بعد:

```json
{
    "success": false,

    "status": 404,

    "error": {
        "detail":
            "Not found."
    }
}
```

---

# context چیست؟

پارامتر:

```python
context
```

اطلاعات View جاری را دارد.

---

مثال:

```python
context["view"]
```

---

یا:

```python
context["request"]
```

---

# Exception و Logging

نکته بسیار مهم Production.

---

اشتباه:

```python
except Exception:
    pass
```

---

این کار:

```text
خطا را مخفی می‌کند.
```

---

در محیط Production:

* Log
* Monitoring
* Alerting

باید فعال باشند.

---

# Exception و Validation

بسیاری از Validationها نباید در View باشند.

---

اشتباه:

```python
if len(title) < 3:
    raise ValidationError(...)
```

---

داخل View.

---

بهتر:

```python
Serializer Validation
```

---

انجام شود.

---

# Exception و Business Logic

سناریو:

```text
هر کاربر
حداکثر 5 کتاب
```

---

اگر تعداد بیشتر شد:

```python
raise BookLimitExceeded()
```

---

استفاده از Custom Exception منطقی است.

---

# معماری پیشنهادی

```text
common/

├── exceptions.py
├── exception_handlers.py
```

---

در پروژه‌های بزرگ:

```text
accounts/

books/

orders/
```

همگی از Exceptionهای مشترک استفاده می‌کنند.

---

# خطاهای رایج

## Exception عمومی

اشتباه:

```python
raise Exception(
    "Something wrong"
)
```

---

بهتر:

```python
raise ValidationError(...)
```

---

یا:

```python
raise PermissionDenied(...)
```

---

## مخفی کردن Exception

اشتباه:

```python
try:
    ...
except:
    pass
```

---

## ارسال 200 برای خطا

اشتباه:

```json
{
    "success": false
}
```

---

با:

```http
200 OK
```

---

همیشه از Status Code صحیح استفاده کنید.

---

# Best Practices

1. از Exceptionهای استاندارد DRF استفاده کنید.
2. Validation را در Serializer انجام دهید.
3. Business Errorها را با Custom Exception مدیریت کنید.
4. Exceptionها را Log کنید.
5. از Exception Handler سراسری استفاده کنید.
6. فرمت خطا را در کل API یکسان نگه دارید.
7. از `raise Exception()` به ندرت استفاده کنید.

---

# نکته مهم معماری

در بسیاری از پروژه‌های Enterprise، استاندارد پاسخ خطا از روز اول تعریف می‌شود.

مثال:

```json
{
    "success": false,
    "code": "BOOK_NOT_FOUND",
    "message": "Book not found.",
    "status": 404
}
```

---

این ساختار برای:

* Mobile App
* Frontend
* Logging
* Monitoring

بسیار مناسب‌تر از پیام‌های متنی ساده است.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* Exception چیست.
* تفاوت Error و Exception چیست.
* Exceptionهای آماده DRF کدام‌اند.
* ValidationError چیست.
* NotFound چیست.
* PermissionDenied چیست.
* AuthenticationFailed چیست.
* چگونه Custom Exception بسازیم.
* چگونه Custom Exception Handler پیاده‌سازی کنیم.
* بهترین روش‌های مدیریت خطا در DRF چیست.

---

فصل بعدی:

```text
13 - Status Codes
```

---

## منابع رسمی

* Exceptions

[DRF Exceptions Documentation](https://www.django-rest-framework.org/api-guide/exceptions/?utm_source=chatgpt.com)

