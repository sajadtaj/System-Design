# 01 - Installation

## اهداف فصل

در پایان این فصل:

* با نقش DRF در پروژه Django آشنا می‌شوید.
* Django REST Framework را نصب می‌کنید.
* اولین API خود را ایجاد می‌کنید.
* تفاوت View معمولی Django و API View را درک می‌کنید.
* ساختار اولیه یک پروژه DRF را خواهید شناخت.

---

# مقدمه

تا اینجا می‌دانیم Django برای ساخت وب‌سایت و Backend استفاده می‌شود.

اما امروزه بسیاری از Frontend ها مانند:

* Flutter
* React
* Vue
* Angular
* Mobile Apps
* Microservices

به HTML نیاز ندارند.

آن‌ها داده را به صورت JSON دریافت می‌کنند.

اینجاست که Django REST Framework یا DRF وارد می‌شود.

DRF مجموعه‌ای از ابزارها و کلاس‌های آماده است که ساخت API در Django را بسیار ساده‌تر می‌کند.

---

# مسئله‌ای که حل می‌کند

فرض کنید یک مدل کتاب داریم:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```

اگر بخواهیم بدون DRF داده را به JSON تبدیل کنیم:

```python
from django.http import JsonResponse

def books(request):
    data = list(Book.objects.values())
    return JsonResponse(data, safe=False)
```

این روش:

* Validation ندارد.
* Authentication ندارد.
* Permission ندارد.
* Pagination ندارد.
* Filtering ندارد.
* قابلیت توسعه ضعیفی دارد.

DRF تمام این امکانات را به صورت استاندارد فراهم می‌کند.

---

# جایگاه در معماری DRF

معماری ساده DRF:

```text
Client
   │
   ▼
Request
   │
   ▼
APIView
   │
   ▼
Serializer
   │
   ▼
Response(JSON)
```

جریان کلی:

1. کلاینت درخواست ارسال می‌کند.
2. View درخواست را دریافت می‌کند.
3. Serializer داده را تبدیل می‌کند.
4. Response به صورت JSON برگردانده می‌شود.

---

# نصب DRF

## نصب پکیج

```bash
pip install djangorestframework
```

بررسی نصب:

```bash
pip show djangorestframework
```

---

## افزودن به settings.py

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
]
```

---

## بررسی سلامت نصب

اجرای پروژه:

```bash
python manage.py runserver
```

در این مرحله پروژه بدون خطا باید بالا بیاید.

---

# ایجاد اولین App

ساخت App:

```bash
python manage.py startapp api
```

افزودن به settings.py:

```python
INSTALLED_APPS = [
    ...
    "api",
]
```

---

# اولین API

## فایل views.py

```python
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloAPIView(APIView):

    def get(self, request):
        return Response({
            "message": "Hello DRF"
        })
```

---

## فایل urls.py اپلیکیشن

```python
from django.urls import path

from .views import HelloAPIView

urlpatterns = [
    path("hello/", HelloAPIView.as_view()),
]
```

---

## فایل urls.py پروژه

```python
from django.urls import include, path

urlpatterns = [
    path("api/", include("api.urls")),
]
```

---

# تست API

اجرای سرور:

```bash
python manage.py runserver
```

سپس:

```http
GET /api/hello/
```

خروجی:

```json
{
    "message": "Hello DRF"
}
```

---

# Response چیست؟

در Django معمولی:

```python
HttpResponse
```

در DRF:

```python
Response
```

نمونه:

```python
return Response({
    "status": "ok"
})
```

مزیت Response:

* تبدیل خودکار به JSON
* هماهنگی با Serializer
* پشتیبانی از Renderer ها
* پشتیبانی از Content Negotiation

---

# Request چیست؟

در Django:

```python
request
```

در DRF:

```python
Request
```

نمونه:

```python
request.data
```

به جای:

```python
request.POST
```

مزیت:

* پشتیبانی از JSON
* پشتیبانی از Form
* پشتیبانی از Multipart
* یکپارچگی بیشتر

---

# مثال عملی

فرض کنید Backend مربوط به اپلیکیشن Flutter شما است.

Flutter درخواست می‌فرستد:

```http
GET /api/hello/
```

Backend پاسخ می‌دهد:

```json
{
    "message": "Hello DRF"
}
```

همین ساختار پایه تمام APIهای بزرگ را تشکیل می‌دهد.

فقط بعداً:

* Serializer
* Authentication
* Permissions
* Filtering
* Pagination

به آن اضافه می‌شوند.

---

# تنظیمات و گزینه‌های مهم

در settings.py می‌توان تنظیمات کلی DRF را تعریف کرد:

```python
REST_FRAMEWORK = {}
```

فعلاً آن را خالی می‌گذاریم.

در فصل‌های بعدی آن را تکمیل خواهیم کرد.

---

# انواع و حالت‌های مختلف

در DRF چند روش برای ساخت API وجود دارد:

### APIView

```python
class HelloAPIView(APIView):
    ...
```

---

### Generic Views

```python
ListAPIView
CreateAPIView
```

---

### ViewSets

```python
ModelViewSet
```

در فصل‌های آینده با جزئیات بررسی خواهند شد.

---

# خطاها و نکات رایج

## فراموش کردن rest_framework

خطا:

```text
ModuleNotFoundError
```

راه حل:

```python
INSTALLED_APPS += ["rest_framework"]
```

---

## استفاده از JsonResponse به جای Response

اشتباه:

```python
return JsonResponse(...)
```

در DRF بهتر است:

```python
return Response(...)
```

---

## فراموش کردن as_view()

اشتباه:

```python
path("hello/", HelloAPIView)
```

صحیح:

```python
path("hello/", HelloAPIView.as_view())
```

---

# Best Practices

1. از ابتدا همه APIها را داخل اپ جداگانه API قرار دهید.
2. از Response به جای JsonResponse استفاده کنید.
3. همه Endpoint ها را زیر `/api/` قرار دهید.
4. از همان ابتدا ساختار URL استاندارد طراحی کنید.
5. برای APIهای واقعی از Serializer استفاده کنید و داده خام برنگردانید.

---

# جمع‌بندی

در این فصل:

* DRF را نصب کردیم.
* اولین API را ساختیم.
* با Request و Response آشنا شدیم.
* ساختار کلی DRF را شناختیم.

در فصل بعد وارد مهم‌ترین بخش DRF یعنی **Serializers** می‌شویم؛ بخشی که قلب تبدیل داده بین Model و JSON محسوب می‌شود.

---

## منابع رسمی

* DRF Installation
* DRF Requests
* DRF Responses
* DRF APIView
* DRF Status Codes
* DRF Official Documentation:
  [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

