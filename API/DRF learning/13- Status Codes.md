# 13 - Status Codes

## اهداف فصل

در پایان این فصل:

* مفهوم HTTP Status Code را درک می‌کنید.
* مهم‌ترین Status Codeهای مورد استفاده در DRF را می‌شناسید.
* تفاوت 401 و 403 را متوجه می‌شوید.
* از ماژول `status` در DRF استفاده می‌کنید.
* از Status Code صحیح در API استفاده می‌کنید.

---

# Status Code چیست؟

هر Response در HTTP دارای یک کد وضعیت است.

مثال:

```http id="x1"
HTTP/1.1 200 OK
```

---

این کد مشخص می‌کند:

```text id="x2"
درخواست چه نتیجه‌ای داشته است.
```

---

# دسته‌بندی کلی

| گروه | مفهوم      |
| ---- | ---------- |
| 2xx  | موفق       |
| 3xx  | انتقال     |
| 4xx  | خطای کاربر |
| 5xx  | خطای سرور  |

---

در APIهای DRF عمدتاً با:

```text id="x3"
2xx

4xx

5xx
```

کار داریم.

---

# 200 OK

درخواست با موفقیت انجام شده است.

مثال:

```http id="x4"
GET /api/books/
```

---

پاسخ:

```http id="x5"
200 OK
```

---

# 201 Created

یک Resource جدید ایجاد شده است.

مثال:

```http id="x6"
POST /api/books/
```

---

پاسخ:

```http id="x7"
201 Created
```

---

# 204 No Content

عملیات موفق بوده اما داده‌ای برای بازگشت وجود ندارد.

مثال:

```http id="x8"
DELETE /api/books/1/
```

---

پاسخ:

```http id="x9"
204 No Content
```

---

# 400 Bad Request

داده ارسالی معتبر نیست.

مثال:

```json id="x10"
{
    "title": ""
}
```

---

پاسخ:

```http id="x11"
400 Bad Request
```

---

معمولاً از:

```python id="x12"
ValidationError
```

ایجاد می‌شود.

---

# 401 Unauthorized

کاربر احراز هویت نشده است.

مثال:

```http id="x13"
GET /api/profile/
```

---

بدون JWT Token.

---

پاسخ:

```http id="x14"
401 Unauthorized
```

---

# 403 Forbidden

کاربر لاگین کرده اما مجوز لازم را ندارد.

مثال:

```text id="x15"
User Logged In
```

اما:

```text id="x16"
Admin نیست
```

---

پاسخ:

```http id="x17"
403 Forbidden
```

---

# تفاوت 401 و 403

## 401

```text id="x18"
تو را نمی‌شناسم
```

---

## 403

```text id="x19"
تو را می‌شناسم
اما اجازه نداری
```

---

این یکی از مهم‌ترین مفاهیم DRF است.

---

# 404 Not Found

Resource پیدا نشده است.

مثال:

```http id="x20"
GET /api/books/999999/
```

---

پاسخ:

```http id="x21"
404 Not Found
```

---

# 405 Method Not Allowed

متد HTTP پشتیبانی نمی‌شود.

مثال:

```http id="x22"
PATCH /api/books/
```

---

در حالی که View فقط:

```http id="x23"
GET
```

را پشتیبانی می‌کند.

---

# 409 Conflict

تعارض داده.

مثال:

```text id="x24"
Duplicate Email
```

یا:

```text id="x25"
Duplicate Username
```

---

# 415 Unsupported Media Type

فرمت داده پشتیبانی نمی‌شود.

مثال:

```http id="x26"
Content-Type: text/xml
```

در حالی که API فقط:

```text id="x27"
application/json
```

را قبول می‌کند.

---

# 429 Too Many Requests

از فصل Throttling.

---

کاربر بیش از حد درخواست ارسال کرده است.

---

پاسخ:

```http id="x28"
429 Too Many Requests
```

---

# 500 Internal Server Error

خطای داخلی سرور.

مثال:

```python id="x29"
ZeroDivisionError
```

---

یا:

```python id="x30"
AttributeError
```

---

این خطا معمولاً نشانه باگ در برنامه است.

---

# استفاده از ماژول Status

فایل:

```text id="x31"
MyProject/books/views.py
```

---

```python id="x32"
from rest_framework import status
```

---

به جای:

```python id="x33"
return Response(
    data,
    status=200
)
```

---

بنویسید:

```python id="x34"
return Response(
    data,
    status=status.HTTP_200_OK
)
```

---

مثال ایجاد رکورد:

```python id="x35"
return Response(
    serializer.data,
    status=status.HTTP_201_CREATED
)
```

---

مثال حذف رکورد:

```python id="x36"
return Response(
    status=status.HTTP_204_NO_CONTENT
)
```

---

# ارتباط با Exceptionها

| Exception            | Status Code |
| -------------------- | ----------- |
| ValidationError      | 400         |
| AuthenticationFailed | 401         |
| PermissionDenied     | 403         |
| NotFound             | 404         |
| MethodNotAllowed     | 405         |
| Throttled            | 429         |

---

# اشتباه رایج

اشتباه:

```json id="x37"
{
    "success": false
}
```

با:

```http id="x38"
200 OK
```

---

در این حالت Client نمی‌تواند تشخیص دهد درخواست موفق بوده یا خیر.

---

صحیح:

```http id="x39"
400 Bad Request
```

یا:

```http id="x40"
404 Not Found
```

یا:

```http id="x41"
403 Forbidden
```

---

# Best Practices

1. همیشه Status Code صحیح برگردانید.
2. از ماژول `status` استفاده کنید.
3. بین 401 و 403 تفاوت قائل شوید.
4. برای Validation از 400 استفاده کنید.
5. هرگز خطا را با 200 برنگردانید.
6. خطاهای 500 را Log و بررسی کنید.

---

# جمع‌بندی

مهم‌ترین Status Codeهای DRF:

```text id="x42"
200 OK
201 Created
204 No Content

400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed
409 Conflict
415 Unsupported Media Type
429 Too Many Requests

500 Internal Server Error
```

این کدها بیش از 95٪ نیازهای روزمره پروژه‌های DRF را پوشش می‌دهند.

---

فصل بعدی:

```text id="x43"
14 - Testing
```

---

## منابع رسمی

* Status Codes

[DRF Status Codes Documentation](https://www.django-rest-framework.org/api-guide/status-codes/?utm_source=chatgpt.com)

