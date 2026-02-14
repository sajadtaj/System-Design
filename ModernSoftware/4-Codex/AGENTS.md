# AGENTS.md

# Purpose: Root Agent Constitution (Policy Router + Precedence Lock)

# Language: Persian (UTF-8)

## 0) هدف

این فایل، قانون اساسی اجرای کار توسط Agent در این ریپو است.
Agent MUST قبل از هر اقدام (تحلیل/کدنویسی/تغییر فایل/اجرای دستور) این فایل را بخواند و مطابق آن عمل کند.

این فایل:

- منابع حقیقت (SoT) را تثبیت می‌کند
- تقدم قوانین را قفل می‌کند
- مسیر فایل‌های مرجع را قابل تغییر نگه می‌دارد
- رفتار توقف (Stop) و حل تعارض (Conflict) را استاندارد می‌کند
- جلوی حدس‌زدن و مسیرسازی دستی را می‌گیرد

---

## 1) فایل‌های مرجع (قابل تغییر) — Single Source of Truth Paths

### 1.1) Agent MUST از این سه فایل مرجع پیروی کند

> مسیرها ممکن است در آینده تغییر کنند؛ تنها نقطه رسمی تغییر مسیرها همین بخش است.
> Agent MUST همیشه از مسیرهای همین بخش استفاده کند.

- **ARCHITECTURE_CONTRACT**: `./AGENTS.LayeredArchitecture.Django.md`

  - (ممکن است بعداً به یکی از این‌ها تغییر کند)
    - `./AGENTS.MicrokernelArchitecture.Engine.md`
    - `./AGENTS.MicroservicesArchitecture.airflow.md`
- **TOOLING_CONTRACT**: `./AGENTS.tools.md`
- **GUIDELINE_GATEWAY**: `./assistant/guideline/root-guideline-and-invocation.json`

### 1.2) قانون تغییر مسیرها

- Agent MUST هرگز به‌صورت خودسرانه مسیرهای بالا را تغییر ندهد.
- تغییر هر مسیر = تغییر ساختاری (Structural Change) و نیازمند تایید صریح کاربر است.

---

## 2) تقدم قوانین (Precedence Order) — حل تعارض الزامی

در صورت هرگونه تعارض یا تناقض:

1) **AGENTS.md** (این فایل) مقدم است.
2) **ARCHITECTURE_CONTRACT** (معماری سرویس فعال) مقدم است.
3) **TOOLING_CONTRACT** (ابزارها و اجرای استاندارد) مقدم است.
4) **GUIDELINE_GATEWAY** و تمام guidelineهای زیرمجموعه‌اش مقدم بعدی هستند.

قانون:

- اگر guidelineها چیزی را توصیه کنند که معماری/ابزار ممنوع کرده، Agent MUST متوقف شود و Conflict Report ارائه کند (بخش 7).

---

## 3) اصول غیرقابل مذاکره (Hard Rules)

### 3.1) No Guessing

Agent MUST فقط بر اساس منابع حقیقت تعریف‌شده در GUIDELINE_GATEWAY (truth_sources) و فایل‌های مرجع این سند تصمیم بگیرد.
حدس، فرض، و تولید مسیر/ساختار بدون پشتوانه ممنوع است.

### 3.2) No Improvisation in Scaffolding

Agent MUST در مواردی که ابزار رسمی/Template استاندارد وجود دارد، از آن استفاده کند و Boilerplate دستی تولید نکند.
جزئیات در TOOLING_CONTRACT تعریف شده است.

### 3.3) UTF-8 End-to-End

Agent MUST در تمام فایل‌های متنی و داده‌های فارسی (DB/UI/Docs) UTF-8 را رعایت کند.

### 3.4) Structural Changes Need Approval

موارد زیر بدون تایید صریح کاربر ممنوع است:

- اضافه/حذف dependency
- تغییر نسخه ابزارها یا پین‌ها
- تغییر ساختار سرویس‌ها یا topology
- تغییر روش Auth/AuthZ یا API versioning scheme
- تغییر schema DB و migration policy
- تغییر مسیر فایل‌های مرجع (بخش 1)

---

## 4) پروتکل اجرای فرمان‌ها (Command Protocol)

Agent MUST رفتار خود را مطابق GUIDELINE_GATEWAY تنظیم کند.
اگر کاربر یک فرمان استاندارد را گفت (یا معنایش را گفت)، Agent MUST همان flow را دنبال کند:

- `make_plan`  → مطابق `invocation_flows.make_plan`
- `make_task`  → مطابق `invocation_flows.make_task`
- `execute_task` → مطابق `invocation_flows.execute_task`
- `milestone_completion` → مطابق `invocation_flows.milestone_completion`
- `manual_consistency_check` → مطابق `invocation_flows.manual_consistency_check`

قانون:

- Agent MUST فقط guidelineهای مرتبط را invoke کند (invoke_only_relevant_guidelines).
- Agent MUST ترتیب اولویت P0>P1>P2 را رعایت کند.
- Agent MUST stop_conditions را قبل از اجرا بررسی کند.

---

## 5) طبقه‌بندی تغییرات (Classification Rules)

برای جلوگیری از انتخاب سلیقه‌ای guidelineها، Agent MUST تغییرات را این‌گونه طبقه‌بندی کند:

### 5.1) API Change

اگر هرکدام از این موارد تغییر کرد:

- routes/urls
- views/viewsets
- serializers
- auth/permissions/throttling
- response schema / pagination / error format
  آنگاه Agent MUST از gateway، guidelineهای مرتبط با API را وارد کند (حداقل api-contract-and-versioning) و نسخه‌بندی/سازگاری را رعایت کند.

### 5.2) DB Change

اگر model/migration/index/constraint تغییر کرد:

- Agent MUST ریسک‌های schema/perf را گزارش کند
- migration policy را رعایت کند
- و تست‌های مرتبط را اضافه/به‌روزرسانی کند

### 5.3) Runtime/DevOps Change

اگر Docker/Compose/env/logging/observability تغییر کرد:

- Agent MUST guidelineهای runtime/observability را invoke کند
- و اثر روی deploy/health/logging را گزارش کند

### 5.4) Pure Code / Refactor

اگر تغییر فقط در منطق/ساختار کد است:

- Agent MUST اصول ARCHITECTURE_CONTRACT را رعایت کند
- و SOLID/structure/style guidelineهای مرتبط را از gateway اعمال کند

---

## 6) فرمت خروجی الزامی (Output Contract)

Agent MUST خروجی را به‌گونه‌ای تولید کند که قابل audit باشد.

### 6.1) برای هر تغییر کد/فایل (execute_task و هر اصلاح)

Agent MUST در ابتدای پاسخ این موارد را بیاورد:

- File Path:
- File Name:
- Class/Function Name (اگر دارد):
- What changed:
- Why changed:
- Affected parts (DB/DevOps/API/Data):
- Replacement: full / partial

### 6.2) Applied Guidelines

Agent MUST طبق gateway، لیست guidelineهای اعمال‌شده را اعلام کند (حداقل در یک خط).

### 6.3) Stop Mode

اگر stop_condition فعال شد:

- Agent MUST فقط Gap Report بدهد:
  - چه چیزی کم است
  - کدام فایل/دستور لازم است
  - قدم بعدی کاربر چیست
    و هیچ خروجی اجرایی/کد تولید نکند.

---

## 7) گزارش تعارض (Conflict Report)

اگر تعارض رخ داد (بین اسناد یا کمبود ورودی):
Agent MUST روند conflict_resolution در gateway را اجرا کند و خروجی را دقیقاً با این قالب بدهد:

- Conflict Type: Hard/Soft/Coverage
- Guidelines Involved: [ ... ]
- What conflicts: (1 جمله)
- Priority Decision: (کدام سند/گایدلاین برنده است + چرا)
- Blocked On: (missing_input/decision)
- Next Step: (کاربر چه باید بکند)

---

## 8) نکات سرویس‌محور (برای آینده)

این ریپو ممکن است چند سرویس/سبک معماری داشته باشد.
قانون:

- هر سرویس می‌تواند ARCHITECTURE_CONTRACT متفاوت داشته باشد.
- در آن حالت، Agent MUST از نزدیک‌ترین `AGENTS.*.md` در مسیر سرویس پیروی کند.
- اما تقدم کلی (بخش 2) همچنان برقرار است.

---

## 9) چک‌لیست حداقل قبل از هر Merge (Agent MUST)

- stop_conditions بررسی شده
- ابزارها مطابق TOOLING_CONTRACT استفاده شده (نه مسیرسازی دستی)
- معماری مطابق ARCHITECTURE_CONTRACT رعایت شده
- API/DB/Runtime impact گزارش شده (اگر مرتبط)
- تست‌های حداقلی اضافه/آپدیت شده (اگر تغییر رفتاری وجود دارد)
- Applied Guidelines اعلام شده
- هیچ حدسی خارج از SoT انجام نشده

---
