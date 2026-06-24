# 23 - Security Checklist

## اهداف فصل

در پایان این فصل:

* مهم‌ترین تهدیدهای امنیتی API را می‌شناسید.
* با چک‌لیست امنیتی Django و DRF آشنا می‌شوید.
* نقش Authentication و Authorization را در امنیت درک می‌کنید.
* با توصیه‌های OWASP آشنا می‌شوید.
* می‌توانید قبل از انتشار API یک بازبینی امنیتی اولیه انجام دهید.

---

# مقدمه

بسیاری از مشکلات امنیتی به دلیل:

```text id="s1"
پیچیدگی فنی
```

رخ نمی‌دهند.

---

بلکه به دلیل:

```text id="s2"
فراموش کردن تنظیمات پایه
```

اتفاق می‌افتند.

---

نمونه‌های رایج:

```text id="s3"
DEBUG=True

Permission اشتباه

Secret Key افشا شده

Endpoint بدون Authentication
```

---

# اصل مهم

امنیت:

```text id="s4"
یک قابلیت نیست
```

---

بلکه:

```text id="s5"
یک فرآیند دائمی
```

است.

---

# Authentication

اولین سؤال:

```text id="s6"
کاربر چه کسی است؟
```

---

بررسی:

```text id="s7"
Authentication فعال است؟
```

---

فایل:

```text id="s8"
MyProject/config/settings.py
```

---

```python id="s9"
REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES": [
        ...
    ]
}
```

---

# Authorization

دومین سؤال:

```text id="s10"
کاربر چه کاری مجاز است انجام دهد؟
```

---

Authentication:

```text id="s11"
Identity
```

---

Authorization:

```text id="s12"
Access Control
```

---

# اصل Least Privilege

کاربر باید فقط به چیزی دسترسی داشته باشد که نیاز دارد.

---

نه بیشتر.

---

مثال:

```text id="s13"
Customer
```

نباید بتواند:

```text id="s14"
Admin APIs
```

را فراخوانی کند.

---

# Permissions

بررسی:

```python id="s15"
permission_classes
```

---

در Viewها تعریف شده‌اند؟

---

مثال:

```python id="s16"
permission_classes = [
    IsAuthenticated
]
```

---

# JWT Security

اگر JWT استفاده می‌کنید:

فصل:

```text id="s17"
06.1
```

---

بررسی کنید:

```text id="s18"
Access Token Lifetime

Refresh Token Lifetime
```

---

منطقی باشند.

---

# Secret Key

هرگز:

```text id="s19"
SECRET_KEY
```

را داخل Git قرار ندهید.

---

اشتباه:

```python id="s20"
SECRET_KEY = "123456"
```

---

درست:

```env id="s21"
SECRET_KEY=...
```

---

# DEBUG

در Production:

```python id="s22"
DEBUG = False
```

---

باید فعال باشد.

---

اشتباه:

```python id="s23"
DEBUG = True
```

---

می‌تواند اطلاعات داخلی سیستم را افشا کند.

---

# HTTPS

در محیط Production:

```text id="s24"
همیشه HTTPS
```

---

استفاده شود.

---

چرا؟

```text id="s25"
رمزنگاری ارتباط
```

---

و جلوگیری از:

```text id="s26"
Man In The Middle
```

---

# Password Storage

هرگز:

```text id="s27"
Password Plain Text
```

ذخیره نکنید.

---

Django به صورت پیش‌فرض:

```text id="s28"
Password Hashing
```

انجام می‌دهد.

---

# Input Validation

همیشه داده ورودی را اعتبارسنجی کنید.

---

وظیفه:

```text id="s29"
Serializer
```

---

مثال:

```python id="s30"
serializer.is_valid(
    raise_exception=True
)
```

---

# SQL Injection

خبر خوب:

---

ORM جنگو به صورت پیش‌فرض در برابر بسیاری از حملات SQL Injection محافظت می‌کند.

---

اما:

```python id="s31"
raw()
```

---

یا:

```python id="s32"
Raw SQL
```

---

نیازمند دقت بیشتری هستند.

---

# XSS

اگر خروجی API مستقیماً در Frontend نمایش داده شود:

---

باید اعتبارسنجی و Escaping مناسب انجام شود.

---

بررسی:

```text id="s33"
Cross Site Scripting
```

---

مطابق توصیه‌های OWASP.

---

# CORS

اگر Frontend جداگانه دارید:

---

مثلاً:

```text id="s34"
React

Flutter Web
```

---

باید:

```text id="s35"
CORS
```

را به درستی تنظیم کنید.

---

اشتباه:

```python id="s36"
CORS_ALLOW_ALL_ORIGINS = True
```

---

در Production.

---

# CSRF

برای Session Authentication اهمیت دارد.

---

برای JWT APIها معمولاً:

```text id="s37"
کمتر مطرح است.
```

---

اما باید مفهوم آن را بشناسید.

---

# Rate Limiting

از فصل Throttling.

---

هدف:

```text id="s38"
جلوگیری از Abuse
```

---

نمونه:

```python id="s39"
UserRateThrottle
```

---

# Brute Force Protection

Endpointهای حساس:

```text id="s40"
Login

OTP

Password Reset
```

---

باید محدود شوند.

---

# اطلاعات حساس در Log

هرگز لاگ نکنید:

```text id="s41"
Password

Access Token

Refresh Token

Secret Key
```

---

# Error Messages

اشتباه:

```json id="s42"
{
    "error":
    "Database Connection Failed ..."
}
```

---

افشای اطلاعات داخلی.

---

بهتر:

```json id="s43"
{
    "error":
    "Internal Server Error"
}
```

---

# File Upload

اگر فایل دریافت می‌کنید:

بررسی کنید:

```text id="s44"
Size

Extension

Content Type
```

---

کنترل شده باشند.

---

# Dependency Updates

کتابخانه‌های قدیمی:

```text id="s45"
Security Risk
```

هستند.

---

به‌روزرسانی منظم انجام دهید.

---

# Security Headers

در Production بررسی کنید:

```text id="s46"
HSTS

X-Frame-Options

Content-Type Protection
```

---

تنظیم شده باشند.

---

# Backup

امنیت فقط جلوگیری از نفوذ نیست.

---

باید بتوانید:

```text id="s47"
بازیابی اطلاعات
```

را نیز انجام دهید.

---

# Logging

ثبت:

```text id="s48"
Authentication Failure

Permission Denied

Critical Errors
```

---

بسیار مهم است.

---

# Monitoring

باید بدانید:

```text id="s49"
چه زمانی حمله رخ داده است.
```

---

یا:

```text id="s50"
سیستم دچار خطا شده است.
```

---

# چک‌لیست انتشار

قبل از Production:

---

## تنظیمات

```text id="s51"
✓ DEBUG=False

✓ SECRET_KEY امن

✓ HTTPS فعال
```

---

## API

```text id="s52"
✓ Authentication

✓ Permissions

✓ Throttling
```

---

## داده‌ها

```text id="s53"
✓ Validation

✓ Backup

✓ Logging
```

---

## زیرساخت

```text id="s54"
✓ Monitoring

✓ Dependency Updates

✓ Security Headers
```

---

# مهم‌ترین توصیه OWASP

هرگز به داده ورودی اعتماد نکنید.

---

```text id="s55"
Validate Everything
```

---

# اشتباهات رایج

## Endpoint بدون Permission

بسیار رایج.

---

## DEBUG=True

یکی از خطرناک‌ترین اشتباهات.

---

## Token Lifetime طولانی

در JWT.

---

## لاگ کردن اطلاعات حساس

مشکل امنیتی جدی.

---

## عدم محدودسازی Login

مستعد Brute Force.

---

# Best Practices

1. Authentication را اجباری کنید.
2. از Least Privilege استفاده کنید.
3. همیشه Validation انجام دهید.
4. HTTPS را اجباری کنید.
5. Throttling را فعال کنید.
6. Secretها را خارج از کد نگهداری کنید.
7. لاگ‌های امنیتی ثبت کنید.
8. Dependencyها را به‌روز نگه دارید.

---

# جمع‌بندی

در این فصل یاد گرفتیم:

* مهم‌ترین تهدیدهای API چیست.
* Authentication و Authorization چه نقشی دارند.
* چگونه از JWT به شکل امن استفاده کنیم.
* چرا HTTPS مهم است.
* چگونه Input Validation انجام دهیم.
* نقش CORS و CSRF چیست.
* چگونه قبل از انتشار API بازبینی امنیتی انجام دهیم.

---

# مهم‌ترین نکته فصل

بیشتر رخنه‌های امنیتی ناشی از:

```text id="s56"
اشتباهات پیکربندی
```

هستند.

نه ضعف‌های پیچیده فنی.

بنابراین داشتن یک چک‌لیست امنیتی منظم از بسیاری از حملات جلوگیری می‌کند.

---

فصل بعدی:

```text id="s57"
24 - Celery and Background Tasks
```

---

## منابع رسمی

* [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/?utm_source=chatgpt.com)
* [OWASP Top 10](https://owasp.org/www-project-top-ten/?utm_source=chatgpt.com)
* [DRF Authentication Documentation](https://www.django-rest-framework.org/api-guide/authentication/?utm_source=chatgpt.com)
* [DRF Permissions Documentation](https://www.django-rest-framework.org/api-guide/permissions/?utm_source=chatgpt.com)
* [DRF Throttling Documentation](https://www.django-rest-framework.org/api-guide/throttling/?utm_source=chatgpt.com)

