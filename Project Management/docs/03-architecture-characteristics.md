

## ⚙️ پرامپت استاندارد برای فایل **03-architecture-characteristics.md**

```text
نقش شما: تیم معماران سامانه (Software Architect + DevOps Engineer + Backend Lead + Data Engineer + System Designer)

هدف: تولید سند کامل **docs/03-architecture-characteristics.md** به زبان فارسی در قالب Markdown، بر اساس اطلاعات موجود در دو فایل قبلی:
- docs/01-overview.md
- docs/02-features-map.md

این سند باید ویژگی‌های معماری (Architecture Characteristics) را در سه دسته‌ی اصلی Operational, Structural, و Cross-Cutting بررسی کند و ارتباط آن‌ها را با ویژگی‌های محصول (Features) مشخص نماید.

==============================
🔹 اطلاعات ورودی (قابل ویرایش توسط کاربر)
نام پروژه: [نام پروژه را بنویس]
خلاصه هدف پروژه (از Overview): [توضیح کوتاه]
ویژگی‌های کلیدی محصول (از FeaturesMap): [چند مورد کلیدی]
الزامات اصلی عملکردی (Performance, Security, Reliability و ...): [اختیاری]
==============================

🔹 خروجی مورد انتظار (Markdown نهایی برای فایل docs/03-architecture-characteristics.md):

# 03 - Architecture Characteristics

## 1. مقدمه
در این سند، ویژگی‌های معماری سیستم بر اساس نیازمندی‌های محصول و ویژگی‌های تعریف‌شده در اسناد **Overview** و **Features Map** تحلیل می‌شوند.  
معماران سیستم این ویژگی‌ها را در سه دسته‌ی اصلی تقسیم‌بندی می‌کنند:
1. Operational Architecture Characteristics (ویژگی‌های معماری عملیاتی)
2. Structural Architecture Characteristics (ویژگی‌های معماری ساختاری)
3. Cross-Cutting Architecture Characteristics (ویژگی‌های معماری فراگیر)

این ویژگی‌ها بنیان تصمیم‌های طراحی، انتخاب فناوری‌ها و ساختار سرویس‌ها را تعیین می‌کنند.

---

## 2. ویژگی‌های معماری عملیاتی (Operational Characteristics)

ویژگی‌های عملیاتی مرتبط با عملکرد، تاب‌آوری و پایداری سیستم در زمان اجرا هستند.  
در جدول زیر برای هر ویژگی، تعریف، هدف، و سرویس‌ها یا ماژول‌هایی که بیشترین وابستگی را دارند مشخص می‌شود:

| ویژگی | تعریف | سرویس‌ها / ماژول‌های مرتبط | وضعیت اهمیت | توضیح و ملاحظات طراحی |
|--------|--------|-----------------------------|---------------|-------------------------|
| Availability (دسترس‌پذیری) | میزان زمانی که سیستم باید فعال باشد (مثلاً 24/7). | Auth, API Gateway | حیاتی | نیاز به Load Balancer و Health Probe |
| Performance (کارایی) | سرعت پاسخ‌دهی، پیک بار و ظرفیت سخت‌افزاری. | Core Service, Analytics Engine | حیاتی | هدف: P95 ≤ 200ms |
| Scalability (مقیاس‌پذیری) | توان افزایش ظرفیت سرویس‌ها در برابر افزایش بار. | All stateless services | بالا | طراحی افقی با Replica و Auto-scaling |
| Recoverability (قابلیت بازیابی) | مدت زمان بازگشت سیستم پس از خطا یا حادثه. | Database, File Storage | متوسط | نیاز به Backup و Snapshot زمان‌بندی‌شده |
| Reliability (قابلیت اعتماد) | احتمال عملکرد صحیح در مدت مشخص. | Payment Processor | بالا | اضافه‌کردن Retry با Circuit Breaker |
| Robustness (تاب‌آوری) | توان مقاومت در برابر خطاها و قطعی‌ها. | External API Integration | بالا | مدیریت خطای graceful و fallback |
| Continuity (تداوم) | پایداری در فاجعه (Disaster Recovery). | Data Layer | بالا | نیاز به Multi-region Deployment |

> نکته: سطح اهمیت باید یکی از موارد "حیاتی" / "بالا" / "متوسط" / "کم" باشد.

---

## 3. ویژگی‌های معماری ساختاری (Structural Characteristics)

ویژگی‌های ساختاری بر نحوه‌ی سازمان‌دهی کد، ماژول‌ها، و ساختار سیستم اثر می‌گذارند.

| ویژگی | تعریف | وابستگی به ویژگی‌های محصول | اهمیت | راهبرد طراحی پیشنهادی |
|--------|--------|-----------------------------|--------|------------------------|
| Configurability (قابلیت پیکربندی) | امکان تغییر تنظیمات بدون نیاز به تغییر کد. | Feature: Notification, Auth | بالا | استفاده از .env و Config Service مرکزی |
| Extensibility (قابلیت گسترش) | امکان افزودن قابلیت جدید بدون تغییر ساختار اصلی. | Feature: Analytics Engine | حیاتی | استفاده از Plugin System |
| Maintainability (نگهداری‌پذیری) | سهولت در رفع خطا و توسعه. | تمامی ماژول‌ها | حیاتی | پیروی از SOLID و Clean Architecture |
| Portability (قابلیت حمل) | امکان اجرا در پلتفرم‌های مختلف. | Backend Services | متوسط | استفاده از Docker و Multi-Platform CI |
| Reusability (استفاده‌پذیری مجدد) | اشتراک ماژول‌های تکرارشونده. | Auth, Logger | بالا | طراحی Shared Libraries |
| Upgradeability (قابلیت ارتقاء) | سهولت در بروزرسانی نسخه‌ها. | Core API | بالا | بهره‌گیری از Rolling Update و Versioned API |

---

## 4. ویژگی‌های معماری فراگیر (Cross-Cutting Characteristics)

این ویژگی‌ها در سراسر سیستم جریان دارند و جنبه‌های امنیت، حریم خصوصی و تجربه‌ی کاربر را در بر می‌گیرند.

| ویژگی | تعریف | مؤلفه‌های مرتبط | اهمیت | سیاست طراحی / ابزار پیشنهادی |
|--------|--------|------------------|--------|--------------------------------|
| Security (امنیت) | محافظت از داده و دسترسی کاربران. | Auth, API Gateway, DB | حیاتی | رمزنگاری AES256 + TLS |
| Privacy (حریم خصوصی) | اطمینان از محرمانگی داده‌ها. | Data Layer | بالا | محدودسازی سطح دسترسی DBAها |
| Authorization (سطوح دسترسی) | کنترل دسترسی به داده‌ها و عملیات. | Auth, Admin Panel | حیاتی | RBAC و Keycloak Policy |
| Accessibility (دسترس‌پذیری برای همه) | امکان استفاده برای تمام کاربران. | Frontend/UI | متوسط | رعایت WCAG و تست رنگ |
| Legal (الزامات قانونی) | انطباق با مقررات داده. | Storage & Logging | متوسط | GDPR-Compliance Logging |
| Observability (پشتیبانی‌پذیری) | مانیتورینگ، Logging، Trace | تمامی سرویس‌ها | بالا | استفاده از Prometheus + OpenTelemetry |

---

## 5. ارتباط ویژگی‌های محصول با ویژگی‌های معماری (Feature → Characteristic Mapping)

| ویژگی محصول (از Features Map) | ویژگی‌های معماری مرتبط | دلایل و توضیحات |
|--------------------------------|------------------------|-----------------|
| Authentication Service | Security, Availability, Maintainability | امنیت و پایداری حیاتی |
| Analytics Engine (AI) | Performance, Scalability, Extensibility | نیاز به پردازش داده‌ی حجیم و توسعه‌پذیر |
| Notification System | Configurability, Reliability | وابستگی به Queue و Retry |
| Dashboard | Usability, Accessibility, Observability | تعامل کاربر و مانیتورینگ بلادرنگ |

---

## 6. جمع‌بندی

این سند، مرجع تصمیم‌های معماری در طراحی سیستم است.  
برای هر ویژگی محصول، خصوصیات معماری مشخص می‌شوند تا در طراحی فاز بعدی (**04-architecture.md**) از آن‌ها به‌عنوان **الزامات کیفی (Quality Scenarios)** استفاده شود.  

همچنین پیشنهاد می‌شود برای هر ویژگی حیاتی، **معیار سنجش (Measure / KPI)** تعیین گردد:
- Performance → P95 ≤ 200ms  
- Availability → ≥ 99.9%  
- Recoverability → ≤ 5 min  
- Security → مطابق با OWASP Top-10  

==============================

🔹 دستور خروجی:
- تمام بخش‌ها و جداول را با قالب Markdown بالا تولید کن.
- متن را فقط به زبان فارسی بنویس.
- ویژگی‌ها را از دو سند قبلی (Overview و FeaturesMap) استخراج و در جداول مرتبط توزیع کن.
- از توضیحات فنی و دقیق استفاده کن (نه عمومی).
- در پایان سند، جمع‌بندی تحلیلی ارائه بده که مستقیماً ورودی سند بعدی (04-architecture.md) باشد.
```

