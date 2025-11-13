
# Project Documentation Framework

این مخزن مستندات، شالودهٔ مدیریت و طراحی پروژه‌های فنی است. هدف آن جلوگیری از توسعهٔ بی‌برنامه، حفظ یکپارچگی بین نقش‌ها (Backend/DevOps/DB/Data/Mobile)، و ردیابی شفاف تصمیم‌ها و ریسک‌ها در طول عمر پروژه است. خروجی این ساختار باید مستقیماً به معماری پایدار، توسعهٔ تدریجی، و کنترل کیفیت منجر شود.

## اهداف
- تعریف دقیق «چه» و «چرا» پیش از «چگونه».
- هم‌راستاسازی تصمیم‌های معماری با ویژگی‌های محصول و الزامات کیفی.
- ردیابی مداوم تصمیم‌ها (ADR) و ریسک‌ها/فرضیات/وابستگی‌ها (RAID).
- تضمین سازگاری Backend و موبایل؛ استانداردسازی API و تست قرارداد.
- پایبندی به UTF-8 برای تمام داده‌های فارسی در DB و UI.

---

## ساختار اسناد (۱۰ قلم)
> روی هر مورد کلیک کنید:

1. [01-overview.md](./docs/01-overview.md) — تعریف محصول، مسئله، راه‌حل، ارزش، پرسونا، مقایسه
2. [02-features-map.md](./docs/02-features-map.md) — ویژگی‌های عمومی/متمایز و نگاشت به سرویس/ماژول
3. [03-architecture-characteristics.md](./docs/03-architecture-characteristics.md) — ویژگی‌های معماری: Operational/Structural/Cross-Cutting
4. [04-architecture.md](./docs/04-architecture.md) — سبک معماری، C4 (Context/Container)، نگاشت سرویس‌ها
5. [05-roadmap.md](./docs/05-roadmap.md) — نقشهٔ راه: اهداف کوتاه/میان/بلندمدت، نگاشت Feature→Goal
6. [06-phasing.md](./docs/06-phasing.md) — فازبندی زنجیره‌ای منطبق با Clean Architecture و سبک منتخب
7. [07-milestones/](./docs/7-milestones.md) — شناسنامهٔ اجرایی هر فاز (قبل از شروع هر فاز تکمیل می‌شود)
8. [08-docs-phase/](./docs/8-docs-phase.md) — گزارش نهایی هر فاز پس از اجرا و تست
9. [09-adrs.md](./docs/09-adrs.md) — نمایهٔ تصمیم‌های معماری + ارجاع به فایل‌های ADR تاریخ‌دار در `docs/09-adrs/`
10. [10-raids.md](./docs/10-raids.md) — ثبت ریسک‌ها، فرضیات، مشکلات و وابستگی‌ها (RAID Log)

> توجه دربارهٔ ADR: علاوه بر فایل نمایهٔ `09-adrs.md`، هر تصمیم معماری مهم به‌صورت لاگ تاریخ‌دار در مسیر `docs/09-adrs/` نگهداری می‌شود، مانند:
>
> `docs/09-adrs/adrs2025-11-12_adrs.md`

---

## نقشهٔ ارتباط اسناد (Documentation Dependency Map)

```mermaid

graph TD

  %% --- Nodes ---
  O[01 - Overview];
  F[02 - Features Map];
  AC[03 - Architecture Characteristics];

  A[04 - Architecture];
  R[05 - Roadmap];
  P[06 - Phasing];

  M[07 - Milestones/];
  D[08 - Docs-Phase/];

  ADRI[09 - ADRs Index];
  ADRS[(docs/09-adrs/*.md)];

  RAID[10 - RAIDs];

  %% --- Edges ---
  O --> F;
  O --> AC;
  F --> AC;

  AC --> A;

  A --> R;
  R --> P;

  P --> M;
  P --> D;

  A --> ADRI;
  ADRI -.-> ADRS;
  ADRI --> R;
  ADRI --> P;

  R --> RAID;
  M --> RAID;
  D --> RAID;
  RAID --> R;

  %% --- Classes ---
  classDef vision fill:#e8f0fe,stroke:#90caf9,color:#0d47a1;
  classDef design fill:#e8f5e9,stroke:#81c784,color:#1b5e20;
  classDef plan   fill:#fff8e1,stroke:#ffcc80,color:#e65100;
  classDef exec   fill:#f3e5f5,stroke:#ce93d8,color:#4a148c;
  classDef gov    fill:#ffebee,stroke:#ef9a9a,color:#b71c1c;

  class O,F,AC vision;
  class A design;
  class R,P plan;
  class M,D exec;
  class ADRI,ADRS,RAID gov;
  

```

---

## گانت اجرای مستندات (Gantt)

> تاریخ‌ها نمونه هستند؛ با توجه به پروژه به‌روزرسانی شوند.

```mermaid

gantt

  dateFormat  YYYY-MM-DD
  title برنامهٔ زمان‌بندی تولید و نگهداری مستندات

  section Vision
  Overview                 :active, o1, 2025-11-12, 3d
  Features Map             :o2, after o1, 3d

  section Design
  Arch Characteristics     :d1, after o2, 4d
  Architecture             :d2, after d1, 4d

  section Plan
  Roadmap                  :p1, after d2, 3d
  Phasing                  :p2, after p1, 3d

  section Execute
  Milestones (per-phase)   :m1, after p2, 7d
  Docs-Phase (per-phase)   :m2, after m1, 3d

  section Governance (continuous)
  ADRs (continuous)        :adr, 2025-11-12, 90d
  RAIDs (continuous)       :raid, 2025-11-12, 90d
```

---

## قواعد کلیدی

* تنها دو پوشهٔ ثابت: `docs/07-milestones/` و `docs/08-docs-phase/`.
* برای ADR‌ها:

  * فایل نمایه: `docs/09-adrs.md`
  * لاگ‌های تاریخ‌دار: `docs/09-adrs/adrsYYYY-MM-DD_adrs.md`
* استاندارد UTF-8 برای تمامی متون و داده‌های فارسی در DB و UI.
* قراردادهای API، نسخه‌بندی، الگوی خطا، و تست قرارداد باید در اولین فاز عملیاتی تثبیت شوند.
* هر تغییر معماری باید ADR داشته باشد؛ هر تغییر ریسک/فرضیات باید در RAID ثبت شود.

## مالکیت و بازبینی

* مالک فنی: Tech Lead
* بازبین‌ها: معمار سیستم، Backend Lead، DevOps، Data
* چرخهٔ بازبینی: هر ۴ هفته یا با هر ADR مهم




