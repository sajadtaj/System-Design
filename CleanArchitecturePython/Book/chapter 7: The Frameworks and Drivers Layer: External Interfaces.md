<div dir="rtl" style="text-align: right;">
# ۷. لایه فریم‌ورک‌ها و درایورها: رابط‌های خارجی

</div>

<div dir="rtl" style="text-align: right;">
**نیازمندی‌های فنی**

</div>

<div dir="rtl" style="text-align: right;">
مثال‌های کد ارائه‌شده در این فصل و در سراسر کتاب با **پایتون ۳.۱۳** تست شده‌اند. برای اختصار، بیشتر مثال‌های کد در این فصل تنها به صورت جزئی پیاده‌سازی شده‌اند. نسخه‌های کامل تمام مثال‌ها را می‌توان در مخزن گیت‌هاب همراه کتاب به آدرس `https://github.com/PacktPublishing/Clean-Architecture-with-Python` یافت. اگر تصمیم دارید مثال درایور ایمیل در بخش «ادغام سرویس‌های خارجی» را اجرا کنید، باید برای یک حساب توسعه‌دهنده رایگان SendGrid در `https://app.sendgrid.com` ثبت‌نام کنید.

</div>

<div dir="rtl" style="text-align: right;">
### درک لایه فریم‌ورک‌ها و درایورها

</div>

<div dir="rtl" style="text-align: right;">
هر **برنامه کاربردی نرم‌افزاری** قابل توجهی باید در نهایت با دنیای واقعی تعامل داشته باشد. پایگاه‌های داده نیاز به پرس‌وجو دارند، فایل‌ها نیاز به خواندن دارند و کاربران به رابط کاربری نیاز دارند. در معماری پاک، این تعاملات ضروری اما ناپایدار از طریق **لایه فریم‌ورک‌ها و درایورها** مدیریت می‌شوند. موقعیت و مسئولیت‌های منحصر به فرد این لایه، آن را هم قدرتمند و هم بالقوه خطرناک برای اهداف معماری ما می‌سازد.

</div>

<div dir="rtl" style="text-align: right;">
#### موقعیت در معماری پاک

</div>

<div dir="rtl" style="text-align: right;">
موقعیت لایه فریم‌ورک‌ها و درایورها در لبه معماری تصادفی نیست؛ این لایه **جزئیات سیستم** ما را که معماری پاک نام می‌برد، نمایش می‌دهد. این جزئیات، اگرچه برای یک برنامه کاربردی فعال ضروری هستند، اما باید از منطق اصلی کسب‌وکار ما جدا بمانند. این جداسازی یک مرز محافظ ایجاد می‌کند که معمولاً تغییرات را فقط به لایه بیرونی محدود می‌کند. با این حال، هنگامی که الزامات جدید نیاز به اصلاح قوانین اصلی کسب‌وکار را ایجاب می‌کنند، معماری پاک مسیرهای روشنی را برای پیاده‌سازی این تغییرات به صورت سیستماتیک از طریق هر لایه فراهم می‌کند و تضمین می‌کند که سیستم ما بدون به خطر انداختن یکپارچگی معماری خود، به آرامی تکامل می‌یابد.

چندین اصل کلیدی در مورد موقعیت لایه فریم‌ورک‌ها و درایورها در معماری پاک وجود دارد:

*   **مرز خارجی**: به عنوان بیرونی‌ترین لایه، تمام تعاملات با دنیای خارج را مدیریت می‌کند:
    *   رابط‌های کاربری (رابط خط فرمان (CLI)، وب، نقاط پایانی API)
    *   سیستم‌های پایگاه داده (درایورهایی مانند SQLite، یا فریم‌ورک‌هایی مانند SQLAlchemy)
    *   سرویس‌ها و APIهای خارجی
    *   سیستم‌های فایل و تعاملات دستگاه

*   **جهت وابستگی**: طبق قانون اساسی معماری پاک، تمام وابستگی‌ها به سمت داخل اشاره دارند. فریم‌ورک‌ها و درایورهای ما به رابط‌های لایه درونی وابسته هستند اما هرگز برعکس:
    *   یک آداپتور پایگاه داده، رابط مخزنی را که توسط لایه کاربرد تعریف شده است، پیاده‌سازی می‌کند.
    *   یک کنترلر وب از رابط‌های لایه آداپتورهای رابط استفاده می‌کند.
    *   کلاینت‌های سرویس خارجی با انتزاعات داخلی ما از لایه کاربرد سازگار می‌شوند.

*   **جزئیات پیاده‌سازی**: این لایه شامل مواردی است که معماری پاک آن را **جزئیات** می‌داند، انتخاب‌های فنی خاصی که باید قابل تعویض باشند:
    *   انتخاب بین SQLite یا PostgreSQL
    *   استفاده از Click به جای Typer برای پیاده‌سازی CLI
    *   انتخاب SendGrid یا AWS SES برای اعلان‌های ایمیل

این موقعیت استراتژیک چندین مزیت کلیدی را فراهم می‌کند:

*   **استقلال فریم‌ورک**: منطق اصلی کسب‌وکار از انتخاب‌های فریم‌ورک خاص بی‌اطلاع می‌ماند.
*   **تست‌پذیری آسان**: وابستگی‌های خارجی را می‌توان با تست دابل‌ها (test doubles) جایگزین کرد.
*   **تکامل منعطف**: جزئیات پیاده‌سازی می‌توانند بدون تأثیر بر لایه‌های داخلی تغییر کنند.
*   **مرزهای واضح**: رابط‌های صریح تعریف می‌کنند که چگونه مسائل خارجی با سیستم ما تعامل می‌کنند.

برای سیستم مدیریت وظایف ما، این بدان معناست که چه ما یک رابط خط فرمان را پیاده‌سازی کنیم، چه وظایف را در فایل‌ها ذخیره کنیم، یا اعلان‌ها را از طریق سرویس‌های ایمیل ارسال کنیم، تمام این جزئیات پیاده‌سازی در این لایه بیرونی قرار دارند در حالی که به رابط‌های تعریف‌شده توسط لایه‌های داخلی احترام می‌گذارند.

</div>

محل دیاگرام ۱.۷: لایه فریم‌ورک‌ها و درایورها با اجزای اصلی

<div dir="rtl" style="text-align: right;">
در ادامه، تمایز بین فریم‌ورک‌ها و درایورها را بررسی خواهیم کرد تا به ما در درک نحوه پیاده‌سازی مؤثر هر نوع وابستگی خارجی کمک کند.

</div>

<div dir="rtl" style="text-align: right;">
#### فریم‌ورک‌ها در مقابل درایورها: درک تمایز

</div>

<div dir="rtl" style="text-align: right;">
در حالی که هم فریم‌ورک‌ها و هم درایورها در بیرونی‌ترین لایه معماری پاک قرار دارند، اما در پیچیدگی ادغام خود به طور قابل توجهی متفاوت هستند. این تمایز از نحوه تعامل آن‌ها با لایه‌هایی که در فصل‌های ۵ و ۶ بررسی کردیم، ناشی می‌شود.

**فریم‌ورک‌ها** پلتفرم‌های نرم‌افزاری جامعی هستند که معماری و جریان کنترل خود را تحمیل می‌کنند:

*   فریم‌ورک‌های وب مانند Flask یا FastAPI
*   فریم‌ورک‌های CLI مانند Click یا Typer
*   فریم‌ورک‌های ORM (مدل‌سازی رابطه‌ای شیء) مانند SQLAlchemy

فریم‌ورک‌هایی مانند Click (که برای CLI خود پیاده‌سازی خواهیم کرد) به مجموعه کاملی از اجزای لایه آداپتورهای رابط برای حفظ مرزهای معماری پاک نیاز دارند:

*   کنترلرها که درخواست‌های خاص فریم‌ورک را به ورودی‌های مورد انتظار Use Case ما تبدیل می‌کنند
*   پرزنترها که داده‌های دامنه را برای مصرف فریم‌ورک فرمت می‌کنند
*   مدل‌های View که داده‌ها را به طور مناسب برای نمایش فریم‌ورک ساختار می‌دهند

**درایورها**، در مقابل، اجزای ساده‌تری هستند که سرویس‌های سطح پایین را بدون تحمیل ساختار یا جریان خود ارائه می‌دهند. مثال‌ها شامل درایورهای پایگاه داده، اجزای دسترسی به سیستم فایل، و کلاینت‌های API خارجی هستند. برخلاف فریم‌ورک‌ها، درایورها نحوه کار برنامه شما را دیکته نمی‌کنند، بلکه به سادگی قابلیت‌هایی را ارائه می‌دهند که شما آن‌ها را با نیازهای خود تطبیق می‌دهید.

این درایورها از طریق پورت‌ها (ports) با برنامه ما تعامل می‌کنند— رابط‌های انتزاعی که ما برای اولین بار در فصل ۵ معرفی کردیم. ما دو مثال کلیدی از پورت‌ها را در آن فصل دیدیم:
*   `TaskRepository` (مخزن وظیفه)
*   `NotificationPort` (پورت اعلان)

یک پورت یک قرارداد انتزاعی است که لایه داخلی تعریف می‌کند تا بتواند با یک سرویس خارجی تعامل کند. سپس یک درایور پیاده‌سازی واقعی آن قرارداد را در لایه بیرونی فراهم می‌کند.

برای درک بهتر تمایز بین فریم‌ورک‌ها و درایورها، این مثال‌های شبه‌کد را در نظر بگیرید:

</div>

```python
# Framework example - requires full Interface Adapters stack
# todo_app/infrastructure/web/routes.py
@app.route("/tasks", methods=["POST"])
def create_task():
"""Framework requires full Interface Adapters stack"""
result = task_controller.handle_create(  # Controller from Ch.6
title=request.json["title"],
description=request.json["description"]
)
return task_presenter.present(result)    # Presenter from Ch.6
```

<div dir="rtl" style="text-align: right;">
توجه کنید که مثال فریم‌ورک هم به یک کنترلر برای تبدیل درخواست و هم به یک پرزنتر برای فرمت‌بندی پاسخ نیاز دارد.
در ادامه، به مثال یک درایور نگاه می‌کنیم:

</div>

```python
# Driver example - only needs interface and implementation
# todo_app/infrastructure/persistence/sqlite_task_repository.py
class SQLiteTaskRepository(TaskRepository):  # Interface from Ch.5
"""Driver needs only basic interface implementation"""
def save(self, task: Task) -> None:
self.connection.execute(
"INSERT INTO tasks (id, title) VALUES (?, ?)",
(str(task.id), task.title)
)
```

<div dir="rtl" style="text-align: right;">
در اینجا می‌بینیم که درایور SQLite به سادگی رابط مخزن را مستقیماً با یک عملیات ذخیره پایه پیاده‌سازی می‌کند.

این تمایز معماری به ما کمک می‌کند تا استراتژی‌های ادغام مناسبی را برای هر نوع وابستگی خارجی پیاده‌سازی کنیم، در حالی که **قانون وابستگی** معماری پاک را حفظ می‌کنیم. این جداسازی‌ها مزایای عملی فوری را ارائه می‌دهند: هنگامی که یک آسیب‌پذیری امنیتی در درایور پایگاه داده شما ظاهر می‌شود، رفع مشکل تنها شامل به‌روزرسانی پیاده‌سازی لایه بیرونی است. هنگامی که الزامات کسب‌وکار نحوه اولویت‌بندی وظایف را تغییر می‌دهد، آن تغییرات در منطق دامنه شما ایزوله باقی می‌مانند. اینها مزایای نظری نیستند، بلکه مزایای روزمره‌ای هستند که با رشد سیستم‌ها افزایش می‌یابند.

</div>

<div dir="rtl" style="text-align: right;">
#### ترکیب برنامه کاربردی

</div>

<div dir="rtl" style="text-align: right;">
تصور کنید یک ماشین پیچیده را مونتاژ می‌کنید. هر بخش باید دقیقاً با هم مطابقت داشته باشد، اما فرآیند مونتاژ نباید نحوه کار اجزای جداگانه را تغییر دهد.

ترکیب یک برنامه کاربردی معماری پاک شامل سه جنبه کلیدی است که با هم کار می‌کنند:

**مدیریت پیکربندی**:
*   تنظیمات خاص محیط را مدیریت می‌کند.
*   انتخاب فریم‌ورک و درایور را کنترل می‌کند.
*   جداسازی بین تنظیمات و منطق کسب‌وکار را حفظ می‌کند.
*   پیکربندی‌های مختلفی را برای توسعه، آزمایش و تولید فعال می‌کند.

**فکتوری‌های اجزا (Component factories)**:
*   پیاده‌سازی‌های به درستی پیکربندی شده رابط‌ها را ایجاد می‌کنند.
*   چرخه عمر وابستگی‌ها را مدیریت می‌کنند.
*   توالی‌های مقداردهی اولیه را مدیریت می‌کنند.
*   قانون وابستگی معماری پاک را در طول ایجاد شیء حفظ می‌کنند.

**نقطه ورود اصلی برنامه**:
*   توالی راه‌اندازی را هماهنگ می‌کند.
*   شرایط خطای سطح بالا را مدیریت می‌کند.
*   جداسازی پاکی را بین راه‌اندازی و عملیات کسب‌وکار حفظ می‌کند.
*   به عنوان ریشه ترکیب (composition root) عمل می‌کند که در آن وابستگی‌ها مونتاژ می‌شوند.

بیایید ببینیم چگونه این جنبه‌ها در عمل با هم کار می‌کنند:

</div>

محل دیاگرام ۲.۷: جریان ترکیب معماری پاک نشان‌دهنده پیکربندی، ریشه ترکیب، و آداپتورهای فریم‌ورک

<div dir="rtl" style="text-align: right;">
همانطور که در شکل ۲.۷ نشان داده شده است، سیستم مدیریت وظایف ما این الگوهای ترکیب را به روش‌های خاصی پیاده‌سازی می‌کند که ارزش عملی آن‌ها را نشان می‌دهد:

*   **مکانیسم پیکربندی** (Configuration mechanism) تنظیمات آگاه به محیط را ارائه می‌دهد که انتخاب‌های پیاده‌سازی را هدایت می‌کند، مانند انتخاب بین ذخیره‌سازی در حافظه یا مبتنی بر فایل.
*   **ریشه ترکیب** (Composition root)، از طریق `main.py` و کلاس `Application`، مونتاژ اجزای ما را هماهنگ می‌کند، در حالی که مرزهای معماری پاک را حفظ می‌کند.
*   **آداپتورهای فریم‌ورک** (Framework Adapters) رابط‌های کاربری ما را از طریق موارد زیر به برنامه اصلی متصل می‌کنند:
    *   کنترلرها که درخواست‌های رابط کاربری را به ورودی‌های Use Case تبدیل می‌کنند.
    *   پرزنترها که داده‌های دامنه را برای نمایش فرمت می‌کنند.
    *   جداسازی پاکی که به چندین رابط اجازه می‌دهد تا اجزای اصلی را به اشتراک بگذارند.

این رویکرد معماری چندین مزیت کلیدی را به همراه دارد:

*   **انعطاف‌پذیری پیاده‌سازی** از طریق ایجاد اجزای مبتنی بر فکتوری.
*   **جداسازی پاک مسئولیت‌ها** از طریق مرزهای به خوبی تعریف شده.
*   **تست‌پذیری آسان** از طریق ایزوله کردن اجزا.
*   **افزودن آسان ویژگی‌های جدید** بدون ایجاد اختلال در کد موجود.

این مزایا در سراسر پیاده‌سازی ما آشکار می‌شوند. در بخش‌های بعدی، هر جزء زیرساختی از شکل ۷.۲ را با جزئیات بررسی خواهیم کرد. ما همه چیز را از مدیریت پیکربندی تا آداپتورهای فریم‌ورک پوشش خواهیم داد و نشان خواهیم داد که چگونه آن‌ها در عمل از طریق الگوهای بتنی و مثال‌های کد با هم کار می‌کنند.

</div>

<div dir="rtl" style="text-align: right;">
#### الگوهای معماری پاک در لایه بیرونی

</div>

<div dir="rtl" style="text-align: right;">
الگوهایی که بررسی کردیم، استراتژی‌های واضحی را برای ادغام مسائل خارجی، در حالی که از منطق اصلی کسب‌وکار ما محافظت می‌کنند، ایجاد می‌کنند. با حرکت به سمت پیاده‌سازی اجزای خاص سیستم مدیریت وظایف ما، این الگوها به روش‌های متمایز با هم کار خواهند کرد تا مرزهای معماری را حفظ کنند.

در نظر بگیرید که چگونه این الگوها در عمل ترکیب می‌شوند: یک درخواست وب در لبه سیستم ما می‌رسد و آبشاری از تعاملات معماری پاک را آغاز می‌کند. آداپتورهای فریم‌ورک درخواست را به فرمت داخلی ما تبدیل می‌کنند، در حالی که پورت‌ها عملیات پایگاه داده و اعلان را بدون افشای جزئیات پیاده‌سازی آن‌ها امکان‌پذیر می‌سازند. تمام این هماهنگی از طریق ریشه ترکیب ما اتفاق می‌افتد، که تضمین می‌کند هر جزء وابستگی‌های به درستی پیکربندی شده خود را دریافت می‌کند.

در ادامه این فصل، با جزئیات بیشتر به این مباحث خواهیم پرداخت و بخش‌هایی از سیستم مدیریت وظایف خود را پیاده‌سازی خواهیم کرد تا این الگوها را در عمل مشاهده کنیم—از آداپتورهای CLI که دستورات کاربر را ترجمه می‌کنند تا پیاده‌سازی‌های مخزن (repository implementations) که پایداری (persistence) را مدیریت می‌کنند. هر پیاده‌سازی نه تنها الگوهای فردی، بلکه نحوه همکاری آن‌ها را برای حفظ اصول اصلی معماری پاک در حالی که عملکرد عملی را ارائه می‌دهند، نشان خواهد داد.

</div>

<div dir="rtl" style="text-align: right;">
### ایجاد آداپتورهای فریم‌ورک رابط کاربری

</div>

<div dir="rtl" style="text-align: right;">
هنگام ادغام فریم‌ورک‌های رابط کاربری، **جداسازی مسئولیت‌ها** در معماری پاک اهمیت ویژه‌ای پیدا می‌کند. فریم‌ورک‌های رابط کاربری هم **ناپایدار** و هم **متعصبانه** هستند، که ایزوله کردن تأثیر آن‌ها از منطق اصلی کسب‌وکار ما را بسیار حیاتی می‌کند. در این بخش، نحوه پیاده‌سازی آداپتورهای فریم‌ورک را بررسی خواهیم کرد که مرزهای پاک را حفظ می‌کنند، در حالی که رابط‌های کاربری عملی را ارائه می‌دهند.

</div>

<div dir="rtl" style="text-align: right;">
#### آداپتورهای فریم‌ورک در عمل

</div>

<div dir="rtl" style="text-align: right;">
بیایید با بررسی آنچه در حال ساخت آن هستیم، شروع کنیم. سیستم مدیریت وظایف ما به یک رابط کاربری نیاز دارد که به کاربران امکان می‌دهد پروژه‌ها و وظایف را به طور موثری مدیریت کنند. شکل ۷.۳ یک صفحه تعامل معمولی از رابط خط فرمان ما را نشان می‌دهد:

</div>

محل تصویر ۳.۷: رابط ویرایش وظیفه در برنامه CLI

<div dir="rtl" style="text-align: right;">
این رابط چندین جنبه کلیدی از سیستم ما را نشان می‌دهد:

*   نمایش واضح جزئیات و وضعیت وظیفه.
*   منوی ساده و شماره‌گذاری شده برای عملیات رایج.
*   فرمت‌بندی یکپارچه مفاهیم دامنه (وضعیت، اولویت).
*   ناوبری بصری بین نماهای مختلف.

اگرچه این رابط برای کاربران ساده به نظر می‌رسد، اما پیاده‌سازی آن نیاز به هماهنگی دقیق در مرزهای معماری دارد. هر قطعه اطلاعات نمایش داده شده و هر عملیات موجود، نشان‌دهنده جریان داده از طریق لایه‌های معماری پاک ما است. شکل ۷.۴ نشان می‌دهد که چگونه یک عملیات واحد - ایجاد یک پروژه - از طریق این مرزها جریان می‌یابد:

</div>

محل دیاگرام ۴.۷: کل جریان درخواست/پاسخ برای ایجاد یک پروژه

<div dir="rtl" style="text-align: right;">
این نمودار توالی (sequence diagram) چندین الگو مهم را آشکار می‌کند:

*   آداپتور CLI ورودی کاربر را از طریق کنترلر Click Command Handler به درخواست‌های به درستی ساختاریافته تبدیل می‌کند.
*   این درخواست‌ها از طریق لایه‌های معماری ما از طریق مرزهای به خوبی تعریف شده جریان می‌یابند.
*   هر لایه مسئولیت‌های خاص خود را انجام می‌دهد (اعتبار سنجی، منطق کسب‌وکار و غیره).
*   پاسخ‌ها از طریق لایه‌ها برمی‌گردند و به طور مناسب برای نمایش تبدیل می‌شوند.

با این درک از نحوه جریان داده از طریق مرزهای معماری ما، بیایید نحوه سازماندهی اجزای پیاده‌سازی این جریان را بررسی کنیم.

</div>

<div dir="rtl" style="text-align: right;">
### سازماندهی و مرزهای اجزا

</div>

<div dir="rtl" style="text-align: right;">
همانطور که در شکل ۷.۲ مشاهده کردیم، ترکیب برنامه ما یک ساختار واضح را ایجاد می‌کند که در آن هر جزء مسئولیت‌های خاصی دارد. در لبه‌های این سیستم، آداپتورهای فریم‌ورک باید تبدیل داده‌ها بین فریم‌ورک‌های خارجی و معماری پاک ما را مدیریت کنند، در حالی که تعاملات کاربر را نیز هماهنگ می‌کنند.

با نگاهی به شکل ۷.۴، می‌توانیم ببینیم که آداپتور CLI ما در یک مرز معماری حیاتی قرار دارد. ما Click را، یک فریم‌ورک پایتون محبوب برای ساخت رابط‌های خط فرمان، برای پیاده‌سازی CLI خود انتخاب کرده‌ایم. آداپتور باید بین الگوهای خاص Click و رابط‌های پاک برنامه ما تبدیل کند و هم ورودی کاربر و هم نمایش نتایج را مدیریت کند.

بیایید ساختار اصلی آداپتور را بررسی کنیم:

</div>

```python
class ClickCli:
    def __init__(self, app: Application):
        self.app = app
        self.current_projects = []  # Cached list of projects for display

    def run(self) -> int:
        """Entry point for running the Click CLI application"""
        try:
            while True:
                self._display_projects()
                self._handle_selection()
        except KeyboardInterrupt:
            click.echo("\nGoodbye!", err=True)
            return 0
        # ... additional methods
```

<div dir="rtl" style="text-align: right;">
این ساختار سطح بالا چندین اصل کلیدی معماری پاک را نشان می‌دهد:

**تزریق وابستگی (Dependency injection)**:
*   آداپتور نمونه `Application` خود را از طریق تزریق از طریق سازنده دریافت می‌کند.
*   این اصل **قانون وابستگی** را حفظ می‌کند و باعث می‌شود آداپتور به لایه‌های داخلی وابسته باشد.
*   هیچ نمونه‌سازی مستقیمی از اجزای برنامه در آداپتور رخ نمی‌دهد.

**ایزوله کردن فریم‌ورک**:
*   کد خاص Click در داخل آداپتور محصور می‌ماند.
*   نمونه `Application` یک رابط پاک به منطق اصلی کسب‌وکار ما ارائه می‌دهد.
*   مسائل مربوط به فریم‌ورک مانند تعامل کاربر و کشینگ نمایش در لبه سیستم باقی می‌مانند.

بیایید یک متد handler از `ClickCli` را بررسی کنیم تا ببینیم چگونه این اجزا با هم کار می‌کنند تا رابط نشان‌داده‌شده در شکل ۷.۳ را ایجاد کنند:

</div>

```python
    def _display_task_menu(self, task_id: str) -> None:
        """Display and handle task menu."""
        result = self.app.task_controller.handle_get(task_id)
        if not result.is_success:
            click.secho(result.error.message, fg="red", err=True)
            return
        task = result.success
        click.clear()
        click.echo("\nTASK DETAILS")
        click.echo("=" * 40)
        click.echo(f"Title:       {task.title}")
        click.echo(f"Description: {task.description}")
        click.echo(f"Status:      {task.status_display}")
        click.echo(f"Priority:    {task.priority_display}")
```

<div dir="rtl" style="text-align: right;">
هندلر منوی وظیفه مرزهای معماری ما را در عمل نشان می‌دهد:

*   عملیات کسب‌وکار از طریق کنترلرها همانطور که در شکل ۷.۴ نشان داده شده است، جریان می‌یابند.
*   نمونه `Application` آداپتور ما را از جزئیات منطق اصلی کسب‌وکار پنهان می‌کند.
*   کد خاص فریم‌ورک (دستورات Click) در لبه‌ها باقی می‌ماند.
*   مدیریت خطا جداسازی پاک بین لایه‌ها را حفظ می‌کند.

از طریق این سبک پیاده‌سازی، ما مرزهای واضح را حفظ می‌کنیم در حالی که یک رابط کاربری عملی را ارائه می‌دهیم. این پایه و اساس به ما امکان می‌دهد تا عملکرد خاصی را پیاده‌سازی کنیم که هم تعامل کاربر و هم عملیات کسب‌وکار را به صورت پاک مدیریت می‌کند.

اکنون بیایید بررسی کنیم که چگونه آداپتور، دستورات و تعاملات خاص کاربر را پردازش می‌کند.

</div>

<div dir="rtl" style="text-align: right;">
### پیاده‌سازی تعاملات کاربر

</div>

<div dir="rtl" style="text-align: right;">
هنگام ساخت CLI، باید اقدامات کاربر را به عملیات کسب‌وکار تبدیل کنیم در حالی که مرزهای معماری پاک را حفظ می‌کنیم. این شامل مدیریت ورودی دستور، نمایش نتایج و مدیریت ناوبری کاربر در سیستم است.

بیایید بررسی کنیم که چگونه کلاس آداپتور `ClickCli` یک جریان تعاملی معمولی را مدیریت می‌کند:

</div>

```python
    def _handle_selection(self) -> None:
        """Handle project/task selection."""
        selection = click.prompt(
            "\nSelect a project or task (e.g., '1' or '1.a')",
            type=str,
            show_default=False
        ).strip().lower()
        if selection == "np":
            self._create_new_project()
            return
        try:
            if "." in selection:
                project_num, task_letter = selection.split(".")
                self._handle_task_selection(int(project_num),
                                            task_letter)
            else:  # Project selection
                self._handle_project_selection(int(selection))
        except (ValueError, IndexError):
            click.secho(
                "Invalid selection. Use '1' for project or '1.a' for task.",
                fg="red",
                err=True,
            )
```

<div dir="rtl" style="text-align: right;">
این هندلر انتخاب (selection handler) چندین الگوی کلیدی را برای مدیریت تعامل کاربر در حالی که به مرزهای معماری پاک احترام می‌گذارد، نشان می‌دهد:

*   **تجزیه ورودی**:
    *   ورودی کاربر را قبل از پردازش اعتبار سنجی و نرمال‌سازی می‌کند.
    *   بازخورد واضحی برای انتخاب‌های نامعتبر ارائه می‌دهد.
    *   مسائل مربوط به مدیریت ورودی را در مرز فریم‌ورک نگه می‌دارد.
*   **مسیریابی دستور**:
    *   انتخاب‌های کاربر را به متدهای هندلر مناسب نگاشت می‌کند.
    *   جداسازی پاکی بین مدیریت ورودی و منطق کسب‌وکار را حفظ می‌کند.
    *   از الگوهای سازگار برای انواع مختلف انتخاب استفاده می‌کند.

اگر از هندلر `_create_new_project` پیروی کنیم، تعامل با لایه کاربرد را می‌بینیم:

</div>

```python
    def _create_new_project(self) -> None:
        """Create a new project."""
        name = click.prompt("Project name", type=str)
        description = click.prompt("Description (optional)",
                                   type=str, default="")

        result = self.app.project_controller.handle_create(
            name, description)
        if not result.is_success:
            click.secho(result.error.message,
                        fg="red", err=True)
```

<div dir="rtl" style="text-align: right;">
این پیاده‌سازی تبدیل پاک بین لایه‌های فریم‌ورک و درایورها و لایه‌های کاربرد را نشان می‌دهد:

*   جمع‌آوری ورودی خاص فریم‌ورک با استفاده از `prompt` (اعلان) Click.
*   تفویض مستقیم به کنترلرهای برنامه برای عملیات کسب‌وکار.
*   مدیریت خطای پاک که به مرزهای معماری احترام می‌گذارد.

این توجه دقیق به مرزهای معماری به ما کمک می‌کند تا یک جداسازی پاک بین رابط کاربری و منطق کسب‌وکار خود را حفظ کنیم، در حالی که هنوز یک تجربه کاربری یکپارچه را ارائه می‌دهیم. چه در حال مدیریت ورودی باشیم و چه در حال نمایش خروجی، هر جزء مسئولیت‌های خاص خود را در لایه‌بندی متمرکز معماری پاک حفظ می‌کند.

</div>

<div dir="rtl" style="text-align: right;">
### بینش‌های دامنه از طریق پیاده‌سازی

</div>

<div dir="rtl" style="text-align: right;">
هنگامی که رابط CLI را پیاده‌سازی می‌کنیم، شروع به کشف بینش‌هایی در مورد مدل دامنه خود از طریق الگوهای تعامل واقعی کاربر می‌کنیم. در ابتدا، مدل دامنه ما تخصیص پروژه به وظایف را اختیاری تلقی می‌کرد و انعطاف‌پذیری را در نحوه سازماندهی کار کاربران فراهم می‌کرد. با این حال، همانطور که رابط کاربری را پیاده‌سازی کردیم، این انعطاف‌پذیری به عنوان منبعی از اصطکاک آشکار شد.

باید توجه داشت که مرزهای معماری پاک ما را از تغییرات جزئیات پیاده‌سازی که در سراسر سیستم ما منتشر می‌شوند، محافظت می‌کنند، مانند تغییر پایگاه داده‌ها یا فریم‌ورک‌های رابط کاربری. با این حال، این کشف چیز متفاوتی را نشان می‌دهد.

آنچه ما کشف کرده‌ایم، یک **بینش اساسی در مورد مدل دامنه** ما است که نیاز به تغییر سیستماتیک در لایه‌های ما دارد. این نشان می‌دهد که چگونه معماری پاک ما را در مدیریت صحیح هر دو نوع تغییر راهنمایی می‌کند—ایزوله کردن پیاده‌سازی‌های فنی در لبه‌ها، در حالی که مسیرهای روشنی را برای تکامل مدل اصلی دامنه ما در صورت نیاز فراهم می‌کند.

پیاده‌سازی رابط کاربری نشان داد که مجبور کردن کاربران به انتخاب بین کار با پروژه‌ها یا وظایف مستقل، پیچیدگی غیرضروری ایجاد می‌کند. کاربران باید برای هر وظیفه تصمیمات صریحی در مورد تخصیص پروژه بگیرند و رابط کاربری نیاز به مدیریت ویژه برای هر دو وظایف مرتبط با پروژه و وظایف مستقل داشت. این امر بار شناختی کاربران و پیچیدگی پیاده‌سازی برای توسعه‌دهندگان را افزایش داد.

این درک منجر به یک بینش مهم دامنه می‌شود: وظایف به طور ذاتی در مدل ذهنی کاربران ما به پروژه‌ها تعلق دارند. به جای برخورد با تخصیص پروژه به عنوان اختیاری، می‌توانیم هم مدل دامنه و هم رابط کاربری خود را با اطمینان از اینکه تمام وظایف به یک پروژه تعلق دارند، ساده کنیم، با یک پروژه صندوق ورودی (Inbox) به عنوان ظرف پیش‌فرض برای وظایفی که به صراحت سازماندهی نشده‌اند.

توسعه رابط‌های کاربری اغلب به عنوان یک زمینه آزمایش حیاتی برای مدل دامنه ما عمل می‌کند، و بینش‌هایی را که ممکن است در طول طراحی اولیه آشکار نباشند، نمایان می‌کند. بیایید از این فرصت استفاده کنیم تا نشان دهیم که چگونه مرزهای معماری پاک ما اطمینان می‌دهند که می‌توانیم این کشفیات را به صورت سیستماتیک پیاده‌سازی کنیم، در حالی که جداسازی بین مسائل فریم‌ورک و منطق اصلی کسب‌وکار را حفظ می‌کنیم.

</div>

<div dir="rtl" style="text-align: right;">
### پیاده‌سازی بینش‌های دامنه: رابطه وظیفه-پروژه

</div>

<div dir="rtl" style="text-align: right;">
بیایید تغییرات کد کلیدی مورد نیاز را برای منعکس کردن درک دقیق خود از اینکه وظایف به طور طبیعی در دامنه ما به پروژه‌ها تعلق دارند، بررسی کنیم. ما این بینش را از لایه دامنه شروع کرده و به سمت بیرون کار خواهیم کرد، با استفاده از یک پروژه Inbox (صندوق ورودی) به عنوان یک مکانیسم عملی برای پشتیبانی از این سازماندهی طبیعی:

</div>

```python
# 1. Domain Layer: Add ProjectType and update entities
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timedelta, timezone

# Assuming Entity base class from previous chapter
@dataclass
class Entity:
    id: UUID = field(default_factory=uuid4, init=False)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

class ProjectType(Enum):
    REGULAR = "REGULAR"
    INBOX = "INBOX"

@dataclass
class Project(Entity):
    name: str
    description: str = ""
    project_type: ProjectType = field(default=ProjectType.REGULAR)
    _tasks: dict[UUID, 'Task'] = field(default_factory=dict, init=False) # Forward reference to Task

    @classmethod
    def create_inbox(cls) -> "Project":
        return cls(
            name="INBOX",
            description="Default project for unassigned tasks",
            project_type=ProjectType.INBOX
        )
    
    def add_task(self, task: 'Task') -> None: # Forward reference
        self._tasks[task.id] = task

    def remove_task(self, task_id: UUID) -> None:
        self._tasks.pop(task_id, None)

    def get_task(self, task_id: UUID) -> Optional['Task']:
        return self._tasks.get(task_id)

    @property
    def tasks(self) -> list['Task']:
        return list(self._tasks.values())
    
    @property
    def incomplete_tasks(self) -> list['Task']:
        # Assuming TaskStatus is defined elsewhere in domain entities
        from todo_app.domain.entities.task import TaskStatus 
        return [task for task in self.tasks if task.status != TaskStatus.DONE]

# Assuming TaskStatus and Priority are defined elsewhere in domain entities
class TaskStatus(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass(frozen=True)
class Deadline:
    due_date: datetime

    def __post_init__(self):
        if self.due_date < datetime.now(timezone.utc):
            raise ValueError("Deadline cannot be in the past")

    def is_overdue(self) -> bool:
        return datetime.now(timezone.utc) > self.due_date

    def time_remaining(self) -> timedelta:
        return max(
            timedelta(0),
            self.due_date - datetime.now(timezone.utc)
        )

    def is_approaching(
        self, warning_threshold: timedelta = timedelta(days=1)
    ) -> bool:
        return timedelta(0) < self.time_remaining() <= warning_threshold


@dataclass
class Task(Entity):
    title: str
    description: str
    project_id: UUID  # No longer optional
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)
    completed_at: Optional[datetime] = None
    completed_by: Optional[UUID] = None

    def start(self) -> None:
        if self.status != TaskStatus.TODO:
            raise ValueError(
                "Only tasks with 'TODO' status can be started")
        self.status = TaskStatus.IN_PROGRESS

    def complete(self, notes: Optional[str] = None) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Task is already completed")
        self.status = TaskStatus.DONE
        self.completed_at = datetime.now(timezone.utc) # Capture completion time
        # self.completed_by = user_id # This was in a later example, adding here for completeness
        # self.completion_notes = notes # This was in a later example, adding here for completeness

    def is_overdue(self) -> bool:
        return self.due_date is not None and self.due_date.is_overdue()

```

<div dir="rtl" style="text-align: right;">
این تغییرات لایه دامنه (Domain layer) اساس الگوی Inbox (صندوق ورودی) ما را بنا نهاده‌اند. با معرفی `ProjectType` و به‌روزرسانی موجودیت‌های ما، ما قانون کسب‌وکار را اعمال می‌کنیم که تمام وظایف باید به یک پروژه تعلق داشته باشند، در حالی که متد فکتوری `create_inbox` ایجاد مداوم پروژه Inbox را تضمین می‌کند. توجه داشته باشید که اکنون موجودیت `Task` به یک `project_id` نیاز دارد، که منعکس‌کننده مدل دامنه اصلاح شده ما است.

سپس تغییرات به لایه کاربرد (Application layer) ما جریان می‌یابند:

</div>

```python
# 2. Application Layer: Update repository interface and use cases
from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional, Any, Dict
from dataclasses import dataclass, field
from todo_app.domain.entities.project import Project, ProjectType
from todo_app.domain.entities.task import Task, TaskStatus, Priority, Deadline
from todo_app.application.common.result import Result, Error, ErrorCode # Assuming these are defined as per Chapter 5

class ProjectRepository(ABC):
    @abstractmethod
    def save(self, project: Project) -> None:
        pass

    @abstractmethod
    def get(self, project_id: UUID) -> Project:
        pass
    
    @abstractmethod
    def get_inbox(self) -> Project:
        """Get the INBOX project."""
        pass

    @abstractmethod
    def get_all(self) -> List[Project]:
        pass

    @abstractmethod
    def delete(self, project_id: UUID) -> None:
        pass

    def set_task_repository(self, task_repo: Any) -> None: # Added for FileProjectRepository
        pass

class TaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task) -> None:
        pass

    @abstractmethod
    def get(self, task_id: UUID) -> Task:
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        pass


@dataclass(frozen=True)
class CreateTaskRequest:
    title: str
    description: str
    project_id: Optional[str] = None # Still optional for request as it might be missing
    priority: Optional[str] = None
    due_date: Optional[str] = None

    def to_execution_params(self) -> Dict[str, Any]:
        params = {
            "title": self.title.strip(),
            "description": self.description.strip(),
        }
        if self.project_id:
            params["project_id"] = UUID(self.project_id)
        if self.priority:
            params["priority"] = Priority[self.priority.upper()]
        if self.due_date:
            from datetime import datetime, timezone
            try:
                params["due_date"] = Deadline(datetime.fromisoformat(self.due_date).replace(tzinfo=timezone.utc))
            except ValueError:
                raise ValueError("Invalid due date format. Use ISO format (YYYY-MM-DDTHH:MM:SS).")
        return params


@dataclass(frozen=True)
class CreateTaskUseCase:
    task_repository: TaskRepository
    project_repository: ProjectRepository

    def execute(self, request: CreateTaskRequest) -> Result:
        try:
            params = request.to_execution_params()
            project_id = params.get("project_id")
            
            if not project_id:
                # If no project_id is provided, assign to the INBOX project
                inbox_project = self.project_repository.get_inbox()
                project_id = inbox_project.id
            else:
                # Validate that the provided project_id exists
                try:
                    self.project_repository.get(project_id)
                except Exception: # A more specific ProjectNotFoundError would be better
                    return Result.failure(Error.not_found("Project", str(project_id)))

            task = Task(
                title=params["title"],
                description=params["description"],
                project_id=project_id,
                due_date=params.get("due_date"),
                priority=params.get("priority", Priority.MEDIUM)
            )
            self.task_repository.save(task)

            # Assuming TaskResponse and from_entity are defined
            from todo_app.application.dtos import TaskResponse
            return Result.success(TaskResponse.from_entity(task))
        except ValueError as e:
            return Result.failure(Error.validation_error(str(e)))
        except Exception as e:
            return Result.failure(Error(ErrorCode.VALIDATION_ERROR, str(e))) # Generic error for now
```

<div dir="rtl" style="text-align: right;">
تغییرات لایه کاربرد نشان می‌دهد که چگونه معماری پاک الزامات بین لایه‌ای را مدیریت می‌کند. رابط `ProjectRepository` قابلیت‌های خاص Inbox را به دست می‌آورد، در حالی که `CreateTaskUseCase` قانون کسب‌وکار جدید ما را با تخصیص خودکار وظایف به پروژه صندوق ورودی (Inbox project) در صورت عدم تعیین پروژه صریح، اعمال می‌کند. این امر قوانین کسب‌وکار ما را متمرکز و یکپارچه نگه می‌دارد. علاوه بر این، مدل `ProjectResponse` فیلد `project_type` را خواهد داشت و مدل `TaskResponse` فیلد `project_id` را الزامی خواهد کرد.

در نتیجه این تغییرات، آداپتور فریم‌ورک ما ساده‌تر می‌شود:

</div>

```python
# Simplification of framework adapter (example from ClickCli)
    def _create_task(self) -> None:
        """Handle task creation command."""
        title = click.prompt("Task title", type=str)
        description = click.prompt("Description", type=str)
        # Project selection is optional - defaults to Inbox
        if click.confirm("Assign to a specific project?", default=False):
            project_id = self._select_project()
        else:
            project_id = None # Let the use case assign to inbox

        # Use request DTO for the use case
        request = CreateTaskRequest(
            title=title,
            description=description,
            project_id=project_id
        )

        result = self.app.task_controller.handle_create(request) # Inbox handling in use case
        if not result.is_success:
            click.secho(result.error.message, fg="red", err=True)
            return

        # Assuming a presenter to display the created task
        click.echo("Task created successfully:")
        task_view_model = self.app.task_presenter.present_task(result.value)
        click.echo(f"Title: {task_view_model.title}, Status: {task_view_model.status_display}")
```

<div dir="rtl" style="text-align: right;">
به جای مدیریت منطق شرطی پیچیده برای وظایف دارای پروژه و بدون پروژه، آداپتور صرفاً بر تعامل کاربر تمرکز می‌کند. قانون کسب‌وکار اطمینان از ارتباط وظیفه-پروژه توسط Use Case مدیریت می‌شود، که نشان می‌دهد چگونه جداسازی مسئولیت‌ها در معماری پاک می‌تواند منجر به اجزای ساده‌تر و متمرکزتر شود. مدل‌های View نیز به همین ترتیب ساده می‌شوند، و دیگر نیازی به مدیریت موارد وظایف بدون پروژه ندارند.

این پیاده‌سازی رویکرد سیستماتیک معماری پاک را برای تغییر نشان می‌دهد:

*   تغییرات دامنه قوانین کسب‌وکار ثابت جدیدی را ایجاد می‌کنند.
*   لایه کاربرد برای اعمال این قوانین سازگار می‌شود.
*   آداپتورهای فریم‌ورک برای منعکس کردن مدل پاک‌تر ساده می‌شوند.
*   هر لایه مسئولیت‌های خاص خود را حفظ می‌کند.

با پیروی از مرزهای معماری پاک، ما بینش دامنه خود را پیاده‌سازی می‌کنیم در حالی که جداسازی مسئولیت‌ها را حفظ می‌کنیم و هم تجربه کاربری و هم سازماندهی کد را بهبود می‌بخشیم. در یک پایگاه کد کمتر ساختاریافته، جایی که قوانین کسب‌وکار ممکن است در اجزای رابط کاربری و کد دسترسی به داده پراکنده شوند، چنین تغییر اساسی نیاز به جستجو در چندین جزء برای اطمینان از رفتار ثابت خواهد داشت. مرزهای واضح معماری پاک به ما کمک می‌کنند تا از این چالش‌های ریفکتورینگ جلوگیری کنیم. همانطور که در بخش بعدی خواهیم دید، همین اصول پیاده‌سازی آداپتورهای پایگاه داده، یکی دیگر از اجزای حیاتی لایه فریم‌ورک‌ها و درایورهای ما را هدایت می‌کنند.

</div>

<div dir="rtl" style="text-align: right;">
### پیاده‌سازی آداپتورهای پایگاه داده

</div>

<div dir="rtl" style="text-align: right;">
با انتزاع منطق اصلی کسب‌وکار ما در لایه دامنه، می‌توانیم پیاده‌سازی ذخیره‌سازی داده‌های خود را در لایه بیرونی محصور کنیم، که معماری پاک آن را لایه **فریم‌ورک‌ها و درایورها** می‌نامد. این جداسازی تضمین می‌کند که **جزئیات زیرساخت** (مانند انتخاب پایگاه داده خاص یا ORM) هرگز به منطق اصلی کسب‌وکار ما نشت نمی‌کنند. به جای آن، منطق دامنه ما از طریق **رابط‌های مخزن (repository interfaces)** که در لایه کاربرد تعریف شده‌اند، با ذخیره‌سازی تعامل می‌کند. این رابط‌ها قراردادهای واضحی را برای هر پیاده‌سازی بتنی فراهم می‌کنند. این رابط‌ها تضمین می‌کنند که منطق اصلی کسب‌وکار ما از جزئیات ذخیره‌سازی مستقل باقی می‌ماند:

</div>

```python
# Defined in Application layer (e.g., todo_app/domain/repositories/task_repository.py)
from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from todo_app.domain.entities.task import Task

class TaskRepository(ABC):
    """Repository interface for Task entity persistence."""
    @abstractmethod
    def get(self, task_id: UUID) -> Task:
        """Retrieve a task by its ID."""
        pass
    @abstractmethod
    def save(self, task: Task) -> None:
        """Save a task to the repository."""
        pass
    @abstractmethod
    def get_all(self) -> List[Task]:
        """Retrieve all tasks."""
        pass
    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        """Delete a task by its ID."""
        pass
    # ... remaining methods of interface
```

<div dir="rtl" style="text-align: right;">
بیایید این رابط را با یک مخزن در حافظه پیاده‌سازی کنیم. در حالی که ذخیره داده‌ها در حافظه ممکن است برای یک سیستم تولیدی غیرعملی به نظر برسد، این پیاده‌سازی چندین مزیت را ارائه می‌دهد. قابل توجه‌تر از همه، یک پیاده‌سازی سبک‌وزن و سریع را برای آزمایش فراهم می‌کند - مزیتی که در فصل ۸ به طور کامل‌تر بررسی خواهیم کرد، زمانی که الگوهای آزمایش معماری پاک را مورد بحث قرار می‌دهیم.

</div>

```python
# todo_app/infrastructure/persistence/in_memory_task_repository.py
from todo_app.domain.repositories.task_repository import TaskRepository
from todo_app.domain.entities.task import Task
from todo_app.application.common.exceptions import TaskNotFoundError # Assuming this exception is defined
from uuid import UUID
from typing import Dict, List

class InMemoryTaskRepository(TaskRepository):
    """In-memory implementation of TaskRepository."""
    def __init__(self) -> None:
        self._tasks: Dict[UUID, Task] = {}

    def get(self, task_id: UUID) -> Task:
        """Retrieve a task by ID."""
        if task := self._tasks.get(task_id):
            return task
        raise TaskNotFoundError(task_id)

    def save(self, task: Task) -> None:
        """Save a task."""
        self._tasks[task.id] = task

    def get_all(self) -> List[Task]:
        """Retrieve all tasks."""
        return list(self._tasks.values())

    def delete(self, task_id: UUID) -> None:
        """Delete a task by its ID."""
        if task_id in self._tasks:
            del self._tasks[task_id]
        else:
            raise TaskNotFoundError(task_id)

```

<div dir="rtl" style="text-align: right;">
این پیاده‌سازی چندین اصل کلیدی معماری پاک را نشان می‌دهد. توجه کنید که چگونه:

*   رابط تعریف شده توسط لایه کاربرد ما را پیاده‌سازی می‌کند.
*   جداسازی پاکی را بین ذخیره‌سازی و منطق کسب‌وکار حفظ می‌کند.
*   خطاهای خاص دامنه (مانند `TaskNotFoundError`) را مدیریت می‌کند.
*   جزئیات پیاده‌سازی (ذخیره‌سازی دیکشنری) را کاملاً از کلاینت‌ها پنهان نگه می‌دارد.

در حالی که این الگو ساده است، اما پایه و اساس تمام پیاده‌سازی‌های مخزن ما را فراهم می‌کند. چه داده‌ها در حافظه، فایل‌ها یا پایگاه داده ذخیره شوند، الگوهای تعامل اصلی به لطف مرزهای معماری پاک ما ثابت می‌مانند.

به عنوان مثال، در اینجا نحوه پیاده‌سازی ذخیره‌سازی مبتنی بر فایل آورده شده است:

</div>

```python
# todo_app/infrastructure/persistence/file_task_repository.py
import json
from pathlib import Path
from typing import Dict, List, Any
from uuid import UUID
from datetime import datetime, timezone

from todo_app.domain.repositories.task_repository import TaskRepository
from todo_app.domain.entities.task import Task, TaskStatus, Priority, Deadline
from todo_app.application.common.exceptions import TaskNotFoundError

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, (datetime)):
            return obj.isoformat()
        if isinstance(obj, (TaskStatus, Priority)):
            return obj.value if isinstance(obj.value, str) else obj.name
        if isinstance(obj, Deadline):
            return {"due_date": obj.due_date.isoformat()}
        return super().default(obj)

class FileTaskRepository(TaskRepository):
    """JSON file-based implementation of TaskRepository."""
    def __init__(self, data_dir: Path):
        self.tasks_file = data_dir / "tasks.json"
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not self.tasks_file.exists():
            self.tasks_file.write_text(json.dumps([])) # Initialize with empty list

    def _load_tasks(self) -> List[Dict[str, Any]]:
        if not self.tasks_file.exists():
            return []
        try:
            return json.loads(self.tasks_file.read_text())
        except json.JSONDecodeError:
            return [] # Handle corrupted file

    def _save_tasks(self, tasks_data: List[Dict[str, Any]]):
        self.tasks_file.write_text(json.dumps(tasks_data, indent=4, cls=JSONEncoder))

    def _dict_to_task(self, task_data: Dict[str, Any]) -> Task:
        # Convert raw dict data back to Task entity
        task_id = UUID(task_data['id'])
        priority = Priority[task_data['priority'].upper()] if 'priority' in task_data else Priority.MEDIUM
        status = TaskStatus[task_data['status'].upper()] if 'status' in task_data else TaskStatus.TODO

        due_date = None
        if 'due_date' in task_data and task_data['due_date']:
            if isinstance(task_data['due_date'], dict) and 'due_date' in task_data['due_date']:
                due_date = datetime.fromisoformat(task_data['due_date']['due_date']).replace(tzinfo=timezone.utc)
            else: # Fallback for old format or simple string
                due_date = datetime.fromisoformat(task_data['due_date']).replace(tzinfo=timezone.utc)
            due_date = Deadline(due_date)

        completed_at = None
        if 'completed_at' in task_data and task_data['completed_at']:
            completed_at = datetime.fromisoformat(task_data['completed_at']).replace(tzinfo=timezone.utc)

        task = Task(
            title=task_data['title'],
            description=task_data['description'],
            project_id=UUID(task_data['project_id']),
            due_date=due_date,
            priority=priority,
        )
        # Manually set fields that are not part of __init__
        task.id = task_id
        task.status = status
        task.completed_at = completed_at
        task.completed_by = UUID(task_data['completed_by']) if 'completed_by' in task_data and task_data['completed_by'] else None

        return task


    def get(self, task_id: UUID) -> Task:
        """Retrieve a task by ID."""
        tasks_data = self._load_tasks()
        for task_data in tasks_data:
            if UUID(task_data["id"]) == task_id:
                return self._dict_to_task(task_data)
        raise TaskNotFoundError(task_id)

    def save(self, task: Task) -> None:
        """Save a task."""
        tasks_data = self._load_tasks()
        found = False
        for i, existing_task_data in enumerate(tasks_data):
            if UUID(existing_task_data["id"]) == task.id:
                tasks_data[i] = task.__dict__ # Convert dataclass to dict
                found = True
                break
        if not found:
            tasks_data.append(task.__dict__) # Convert dataclass to dict
        self._save_tasks(tasks_data)

    def get_all(self) -> List[Task]:
        """Retrieve all tasks."""
        tasks_data = self._load_tasks()
        return [self._dict_to_task(td) for td in tasks_data]

    def delete(self, task_id: UUID) -> None:
        """Delete a task by its ID."""
        tasks_data = self._load_tasks()
        initial_count = len(tasks_data)
        tasks_data = [td for td in tasks_data if UUID(td['id']) != task_id]
        if len(tasks_data) == initial_count:
            raise TaskNotFoundError(task_id)
        self._save_tasks(tasks_data)
```

<div dir="rtl" style="text-align: right;">
این پیاده‌سازی قدرت رویکرد مبتنی بر رابط معماری پاک را نشان می‌دهد:

*   همان رابط، استراتژی‌های ذخیره‌سازی بسیار متفاوتی را پشتیبانی می‌کند.
*   منطق اصلی کسب‌وکار کاملاً از جزئیات ذخیره‌سازی بی‌اطلاع می‌ماند.
*   پیچیدگی پیاده‌سازی (مانند سریال‌سازی JSON) در لایه بیرونی ایزوله می‌ماند.
*   مدیریت خطا در تمام پیاده‌سازی‌ها یکپارچه باقی می‌ماند.

کد دامنه ما می‌تواند با هر دو پیاده‌سازی به صورت شفاف کار کند:

</div>

```python
# Works identically with either repository
task = repository.get(task_id)
task.complete()
repository.save(task)
```

<div dir="rtl" style="text-align: right;">
این انعطاف‌پذیری فراتر از این دو پیاده‌سازی است. چه بعداً SQLite، PostgreSQL یا ذخیره‌سازی ابری را اضافه کنیم، رابط‌های پاک ما تضمین می‌کنند که منطق اصلی کسب‌وکار هرگز تغییر نمی‌کند.

</div>

<div dir="rtl" style="text-align: right;">
### مدیریت نمونه‌سازی مخزن

</div>

<div dir="rtl" style="text-align: right;">
همانطور که در شکل ۷.۲ نشان داده شده است، **مدیریت پیکربندی** نقش کلیدی در ترکیب برنامه ما ایفا می‌کند. یکی از مسئولیت‌های اصلی آن، هدایت انتخاب و ایجاد پیاده‌سازی‌های مخزن (repository) مناسب است. کلاس `Config` ما راهی پاک برای مدیریت این تصمیمات را فراهم می‌کند:

</div>

```python
# todo_app/infrastructure/configuration/config.py
import os
from pathlib import Path
from enum import Enum
import logging

class RepositoryType(Enum):
    FILE = "file"
    MEMORY = "memory"

class Config:
    """Application configuration."""
    DEFAULT_REPOSITORY_TYPE = RepositoryType.FILE
    DEFAULT_DATA_DIR_NAME = "data"

    @classmethod
    def get_repository_type(cls) -> RepositoryType:
        repo_type_str = os.getenv(
            "TODO_REPOSITORY_TYPE",
            cls.DEFAULT_REPOSITORY_TYPE.value
        )
        try:
            return RepositoryType(repo_type_str.lower())
        except ValueError:
            raise ValueError(f"Invalid repository type: {repo_type_str}")

    @classmethod
    def get_data_directory(cls) -> Path:
        data_dir_str = os.getenv("TODO_DATA_DIR")
        if data_dir_str:
            data_dir = Path(data_dir_str)
        else:
            # Default to a 'data' directory in the user's home directory
            data_dir = Path.home() / cls.DEFAULT_DATA_DIR_NAME
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir

    @classmethod
    def get_sendgrid_api_key(cls) -> str:
        """Get the SendGrid API key."""
        return os.getenv("TODO_SENDGRID_API_KEY", "")

    @classmethod
    def get_notification_email(cls) -> str:
        """Get the notification recipient email."""
        return os.getenv("TODO_NOTIFICATION_EMAIL", "")
```

<div dir="rtl" style="text-align: right;">
ما اکنون از این قابلیت پیکربندی در پیاده‌سازی یک فکتوری (factory) استفاده می‌کنیم که نمونه‌سازی واقعی مخازن ما را مدیریت می‌کند. این الگوی فکتوری، که در بحث ترکیب برنامه کاربردی (application composition) به آن اشاره شد، راهی پاک برای ایجاد نمونه‌های مخزن به درستی پیکربندی شده را فراهم می‌کند:

</div>

```python
# todo_app/infrastructure/configuration/factories.py
from typing import Tuple
from todo_app.domain.repositories.task_repository import TaskRepository
from todo_app.domain.repositories.project_repository import ProjectRepository
from todo_app.infrastructure.configuration.config import Config, RepositoryType
from todo_app.infrastructure.persistence.file_task_repository import FileTaskRepository
from todo_app.infrastructure.persistence.file_project_repository import FileProjectRepository
from todo_app.infrastructure.persistence.in_memory_task_repository import InMemoryTaskRepository
from todo_app.infrastructure.persistence.in_memory_project_repository import InMemoryProjectRepository

def create_repositories() -> Tuple[TaskRepository, ProjectRepository]:
    repo_type = Config.get_repository_type()
    if repo_type == RepositoryType.FILE:
        data_dir = Config.get_data_directory()
        task_repo = FileTaskRepository(data_dir)
        project_repo = FileProjectRepository(data_dir)
        project_repo.set_task_repository(task_repo) # Ensure FileProjectRepository can access tasks
        return task_repo, project_repo
    elif repo_type == RepositoryType.MEMORY:
        task_repo = InMemoryTaskRepository()
        project_repo = InMemoryProjectRepository()
        project_repo.set_task_repository(task_repo) # Ensure InMemoryProjectRepository can access tasks
        return task_repo, project_repo
    else:
        # This case should ideally not be reached due to Config.get_repository_type() validation
        raise ValueError(f"Invalid repository type: {repo_type}")

```

<div dir="rtl" style="text-align: right;">
این فکتوری چندین الگوی کلیدی معماری پاک را در عمل نشان می‌دهد. پیکربندی:

*   انتخاب پیاده‌سازی‌های مخزن را (فایل یا حافظه) هدایت می‌کند.
*   اجزا را به درستی آماده می‌کند (به عنوان مثال، مسیر فایل داده).
*   انعطاف‌پذیری را برای تغییر استراتژی‌های ذخیره‌سازی بدون اصلاح کد اصلی کسب‌وکار فراهم می‌کند.

با الگوهای ایجاد مخزن (repository creation) ما، بیایید بررسی کنیم که چگونه این اجزا در سراسر مرزهای معماری ما برای تشکیل یک سیستم کامل هماهنگ می‌شوند.

</div>

<div dir="rtl" style="text-align: right;">
#### مرور کلی هماهنگی اجزا (Component orchestration)

</div>

<div dir="rtl" style="text-align: right;">
ما کلاس‌های پیکربندی، الگوهای فکتوری و اصول ترکیب را پوشش داده‌ایم—همه با هم برای مدیریت ایجاد مخزن کار می‌کنند.

بیایید یک قدم به عقب برگردیم و تصویر کامل را بررسی کنیم. شکل ۷.۵ بر نمای کلی معماری ما از شکل ۷.۲ تمرکز دارد و نحوه تعامل اجزای پیکربندی و ریشه ترکیب را در سراسر مرزهای معماری ما با جزئیات نشان می‌دهد:

</div>

محل دیاگرام ۵.۷: تعاملات اجزا بین لایه فریم‌ورک‌ها و درایورها و لایه آداپتورهای رابط

<div dir="rtl" style="text-align: right;">
همانطور که در شکل ۷.۵ نشان داده شده است، جریان ترکیب ما با `main.py` شروع می‌شود که فرآیند ایجاد برنامه را آغاز می‌کند. تابع `create_application` به عنوان فکتوری اصلی ما عمل می‌کند و با مدیریت پیکربندی و فکتوری‌های اجزا هماهنگ می‌شود تا یک نمونه کلاس `Application` کاملاً پیکربندی شده را مونتاژ کند. هر جزء مرزهای پاک را حفظ می‌کند در حالی که با هم کار می‌کنند تا یک سیستم انعطاف‌پذیر و قابل نگهداری را از طریق ترکیب فراهم کنند. در حالی که هر جزء مسئولیت‌های واضح و متمرکزی دارد، آن‌ها با هم کار می‌کنند تا یک سیستم انعطاف‌پذیر و قابل نگهداری را ایجاد کنند که به مرزهای معماری احترام می‌گذارد. در بخش بعدی، ادغام سرویس‌های خارجی را بررسی خواهیم کرد و نگاه دقیق‌تری به نحوه کنار هم آوردن این اجزا توسط کلاس `Application` و `main.py` در زمان اجرا خواهیم داشت.

</div>

<div dir="rtl" style="text-align: right;">
### ادغام سرویس‌های خارجی

</div>

<div dir="rtl" style="text-align: right;">
در حالی که پایگاه‌های داده وضعیت برنامه ما را ذخیره می‌کنند، سرویس‌های خارجی به برنامه ما امکان می‌دهند با دنیای گسترده‌تر از طریق ارسال اعلان‌ها، پردازش پرداخت‌ها یا ادغام با سرویس‌های شخص ثالث دیگر تعامل داشته باشد.

برای سیستم مدیریت وظایف ما، اعلان‌ها یک قابلیت کلیدی هستند. ممکن است بخواهیم کاربران را در مورد وظایف جدید، مهلت‌های نزدیک، یا وظایف تکمیل شده مطلع کنیم. معماری پاک به ما امکان می‌دهد این قابلیت‌های خارجی را بدون به خطر انداختن پاکی منطق اصلی کسب‌وکار خود اضافه کنیم.

همانطور که در فصل ۵ (لایه کاربرد) بحث شد، ما این نیازها را با تعریف **پورت‌ها (ports)** — رابط‌های انتزاعی که برنامه ما به آن‌ها نیاز دارد، بدون دانستن جزئیات پیاده‌سازی — مدیریت می‌کنیم. برای اعلان‌ها، این شامل تعریف یک رابط `NotificationPort` می‌شود:

</div>

```python
# todo_app/domain/services/notification_service.py
from abc import ABC, abstractmethod
from todo_app.domain.entities.task import Task
from todo_app.domain.entities.project import Project
from uuid import UUID

class NotificationPort(ABC):
    """Repository interface for Task entity persistence."""
    @abstractmethod
    def notify_task_completed(self, task: Task) -> None:
        """Notify when a task is completed."""
        pass
    @abstractmethod
    def notify_task_high_priority(self, task: Task) -> None:
        """Notify when a task is set to high priority."""
        pass
    @abstractmethod
    def notify_project_created(self, project: Project) -> None:
        """Notify when a project is created."""
        pass
    @abstractmethod
    def notify_task_deadline_approaching(self, task: Task) -> None:
        """Notify when a task deadline is approaching."""
        pass
```

<div dir="rtl" style="text-align: right;">
این رابط، که در لایه کاربرد ما تعریف شده است، چندین اصل کلیدی معماری پاک را نشان می‌دهد:

*   برنامه اصلی دقیقاً مشخص می‌کند که به چه قابلیت‌های اعلانی نیاز دارد.
*   هیچ جزئیات پیاده‌سازی به رابط نشت نمی‌کند.
*   رابط صرفاً بر عملیات کسب‌وکار تمرکز دارد.
*   مدیریت خطا در این سطح انتزاعی باقی می‌ماند.

بیایید بررسی کنیم که چگونه یک اعلان تکمیل وظیفه از طریق مرزهای معماری ما جریان می‌یابد:

</div>

محل دیاگرام ۶.۷: جریان اعلان از طریق لایه‌های معماری

<div dir="rtl" style="text-align: right;">
این توالی مدیریت دقیق وابستگی‌ها در معماری پاک را نشان می‌دهد:

*   Use Case (مورد استفاده) فقط از `NotificationPort` انتزاعی مطلع است.
*   پیاده‌سازی بتنی SendGrid در لبه سیستم ما قرار دارد.
*   منطق کسب‌وکار کاملاً از جزئیات پیاده‌سازی ایمیل بی‌اطلاع می‌ماند.
*   ادغام سرویس خاص (SendGrid) به صورت پاک در مرزهای معماری اتفاق می‌افتد.

</div>

<div dir="rtl" style="text-align: right;">
#### ادغام SendGrid

</div>

<div dir="rtl" style="text-align: right;">
با تعریف رابط پورت اعلان (notification port) ما، بیایید اعلان‌های ایمیل را با استفاده از SendGrid پیاده‌سازی کنیم— یک سرویس ایمیل مبتنی بر ابر که APIهایی برای ارسال ایمیل‌های تراکنشی فراهم می‌کند. با پیاده‌سازی پورت اعلان خود با SendGrid، نشان خواهیم داد که چگونه معماری پاک به ما کمک می‌کند تا با سرویس‌های شخص ثالث ادغام شویم در حالی که مرزهای معماری پاک را حفظ می‌کنیم:

</div>

```python
# todo_app/infrastructure/notifications/sendgrid_notifier.py
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from todo_app.domain.services.notification_service import NotificationPort
from todo_app.domain.entities.task import Task
from todo_app.domain.entities.project import Project
from todo_app.application.common.exceptions import NotificationError # Assuming this exception is defined
from todo_app.infrastructure.configuration.config import Config # To get API key and email

class SendGridNotifier(NotificationPort):
    def __init__(self) -> None:
        self.api_key = Config.get_sendgrid_api_key()
        self.notification_email = Config.get_notification_email()
        self._init_sg_client()

    def _init_sg_client(self):
        if self.api_key:
            self.client = SendGridAPIClient(self.api_key)
        else:
            self.client = None
            # Log a warning if API key is not configured, but don't raise an error
            print("WARNING: SendGrid API key not configured. Email notifications will be disabled.")


    def notify_task_completed(self, task: Task) -> None:
        """Send email notification for completed task if configured."""
        if not (self.client and self.notification_email):
            return # Notifications are disabled

        try:
            message = Mail(
                from_email=self.notification_email,
                to_emails=self.notification_email, # Can be dynamic based on task assignee
                subject=f"Task Completed: {task.title}",
                plain_text_content=f"Task '{task.title}' (ID: {task.id}) has been completed. Notes: {task.completed_at}"
            )
            self.client.send(message)
            print(f"DEBUG: Sent task completion email for '{task.title}'")
        except Exception as e:
            # Log error but don't disrupt business operations
            print(f"ERROR: Failed to send task completion email for '{task.title}': {e}")
            raise NotificationError(f"SendGrid failed: {e}") from e


    def notify_task_high_priority(self, task: Task) -> None:
        """Notify when a task is set to high priority."""
        if not (self.client and self.notification_email):
            return

        try:
            message = Mail(
                from_email=self.notification_email,
                to_emails=self.notification_email,
                subject=f"HIGH PRIORITY Task: {task.title}",
                plain_text_content=f"Task '{task.title}' (ID: {task.id}) has been marked as HIGH PRIORITY. Due: {task.due_date.due_date.isoformat() if task.due_date else 'N/A'}"
            )
            self.client.send(message)
            print(f"DEBUG: Sent high priority task email for '{task.title}'")
        except Exception as e:
            print(f"ERROR: Failed to send high priority task email for '{task.title}': {e}")
            raise NotificationError(f"SendGrid failed: {e}") from e

    def notify_project_created(self, project: Project) -> None:
        """Notify when a project is created."""
        if not (self.client and self.notification_email):
            return
        
        try:
            message = Mail(
                from_email=self.notification_email,
                to_emails=self.notification_email,
                subject=f"Project Created: {project.name}",
                plain_text_content=f"Project '{project.name}' (ID: {project.id}) has been created."
            )
            self.client.send(message)
            print(f"DEBUG: Sent project creation email for '{project.name}'")
        except Exception as e:
            print(f"ERROR: Failed to send project creation email for '{project.name}': {e}")
            raise NotificationError(f"SendGrid failed: {e}") from e

    def notify_task_deadline_approaching(self, task: Task) -> None:
        """Notify when a task deadline is approaching."""
        if not (self.client and self.notification_email):
            return
        
        try:
            message = Mail(
                from_email=self.notification_email,
                to_emails=self.notification_email,
                subject=f"Deadline Approaching: {task.title}",
                plain_text_content=f"The deadline for task '{task.title}' (ID: {task.id}) is approaching. Due: {task.due_date.due_date.isoformat() if task.due_date else 'N/A'}"
            )
            self.client.send(message)
            print(f"DEBUG: Sent deadline approaching email for '{task.title}'")
        except Exception as e:
            print(f"ERROR: Failed to send deadline approaching email for '{task.title}': {e}")
            raise NotificationError(f"SendGrid failed: {e}") from e

```

<div dir="rtl" style="text-align: right;">
پیاده‌سازی SendGrid ما، مانند پیاده‌سازی‌های مخزن (repository) قبلی ما، برای مدیریت تنظیمات خاص سرویس به مدیریت پیکربندی (configuration management) متکی است. با تکیه بر الگوهای ایجاد شده در پیکربندی مخزن ما، کلاس `Config` ما برای پشتیبانی از تنظیمات اعلان رشد می‌کند:

</div>

```python
# todo_app/infrastructure/configuration/config.py
import os
from pathlib import Path
from enum import Enum
import logging

class RepositoryType(Enum):
    FILE = "file"
    MEMORY = "memory"

class Config:
    """Application configuration."""
    DEFAULT_REPOSITORY_TYPE = RepositoryType.FILE
    DEFAULT_DATA_DIR_NAME = "data"

    @classmethod
    def get_repository_type(cls) -> RepositoryType:
        repo_type_str = os.getenv(
            "TODO_REPOSITORY_TYPE",
            cls.DEFAULT_REPOSITORY_TYPE.value
        )
        try:
            return RepositoryType(repo_type_str.lower())
        except ValueError:
            raise ValueError(f"Invalid repository type: {repo_type_str}")

    @classmethod
    def get_data_directory(cls) -> Path:
        data_dir_str = os.getenv("TODO_DATA_DIR")
        if data_dir_str:
            data_dir = Path(data_dir_str)
        else:
            # Default to a 'data' directory in the user's home directory
            data_dir = Path.home() / cls.DEFAULT_DATA_DIR_NAME
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir

    @classmethod
    def get_sendgrid_api_key(cls) -> str:
        """Get the SendGrid API key."""
        return os.getenv("TODO_SENDGRID_API_KEY", "")

    @classmethod
    def get_notification_email(cls) -> str:
        """Get the notification recipient email."""
        return os.getenv("TODO_NOTIFICATION_EMAIL", "")

```

<div dir="rtl" style="text-align: right;">
بیایید ببینیم که این چگونه در جریان کار تکمیل وظیفه ما قرار می‌گیرد. `CompleteTaskUseCase` (مورد استفاده تکمیل وظیفه) ما از فصل ۵ را به یاد بیاورید که تکمیل وظیفه را با اعلان‌ها هماهنگ می‌کند:

</div>

```python
# todo_app/application/use_cases/complete_task.py
from dataclasses import dataclass
from uuid import UUID
from todo_app.domain.repositories.task_repository import TaskRepository
from todo_app.domain.services.notification_service import NotificationPort
from todo_app.application.common.result import Result, Error
from todo_app.application.common.exceptions import TaskNotFoundError, ValidationError
from todo_app.application.dtos import TaskResponse, CompleteTaskRequest # Assuming TaskResponse and CompleteTaskRequest DTOs

@dataclass(frozen=True)
class CompleteTaskUseCase:
    """Use case for marking a task as complete and notifying stakeholders"""
    task_repository: TaskRepository
    notification_service: NotificationPort

    def execute(self, request: CompleteTaskRequest) -> Result:
        try:
            # Input validation already done by request DTO if coming from controller
            task_id_uuid = UUID(request.task_id) # Convert string ID to UUID for domain layer

            task = self.task_repository.get(task_id_uuid)
            task.complete(notes=request.completion_notes) # Updated task.complete to accept notes
            self.task_repository.save(task)
            
            self.notification_service.notify_task_completed(task)

            return Result.success(TaskResponse.from_entity(task))
        except TaskNotFoundError:
            return Result.failure(Error.not_found("Task", request.task_id))
        except ValueError as e:
            return Result.failure(Error.validation_error(str(e)))
        except ValidationError as e: # Catch DTO validation errors as well
            return Result.failure(Error.validation_error(str(e)))

```

<div dir="rtl" style="text-align: right;">
با پیاده‌سازی `NotificationPort` با SendGrid، ما یک مزیت کلیدی مرزهای معماری پاک را نشان می‌دهیم: افزودن اعلان‌های ایمیل فقط نیاز به تغییر در لبه سیستم دارد. از آنجایی که لایه کاربرد ما رابط `NotificationPort` را تعریف کرد و Use Caseهای ما فقط به این انتزاع وابسته هستند، پیاده‌سازی اعلان‌های SendGrid نیازی به تغییر در منطق اصلی کسب‌وکار ما ندارد. فقط پیاده‌سازی `SendGridNotifier` و سیم‌کشی ریشه ترکیب مرتبط با آن باید اضافه شود. این نشان می‌دهد که چگونه معماری پاک به ما امکان می‌دهد سرویس‌های خارجی قدرتمند را ادغام کنیم در حالی که برنامه اصلی ما کاملاً بدون تغییر باقی می‌ماند.

</div>

<div dir="rtl" style="text-align: right;">
### بوت‌استرپینگ برنامه کاربردی

</div>

<div dir="rtl" style="text-align: right;">
همانطور که در بحث ما در مورد هماهنگی اجزا دیدیم، **ریشه ترکیب (composition root)** تمام اجزای لایه فریم‌ورک‌ها و درایورهای ما را گرد هم می‌آورد در حالی که مرزهای معماری پاک را حفظ می‌کند. بیایید پیاده‌سازی این ترکیب را با شروع از کلاس کانتینر `Application` (برنامه کاربردی) ما بیشتر بررسی کنیم.

کلاس کانتینر `Application` تمام اجزای مورد نیاز برنامه را به عنوان فیلد نگه می‌دارد:

</div>

```python
# todo_app/infrastructure/configuration/container.py
from dataclasses import dataclass, field
from todo_app.domain.repositories.task_repository import TaskRepository
from todo_app.domain.repositories.project_repository import ProjectRepository
from todo_app.domain.services.notification_service import NotificationPort
from todo_app.interfaces.presenters import TaskPresenter, ProjectPresenter # Assuming these are abstract interfaces
from todo_app.application.use_cases.create_task import CreateTaskUseCase # Specific use case imports for wiring
from todo_app.application.use_cases.complete_task import CompleteTaskUseCase
from todo_app.application.use_cases.get_task import GetTaskUseCase
from todo_app.application.use_cases.delete_task import DeleteTaskUseCase
from todo_app.application.use_cases.update_task import UpdateTaskUseCase
from todo_app.application.use_cases.create_project import CreateProjectUseCase
from todo_app.application.use_cases.get_project import GetProjectUseCase
from todo_app.application.use_cases.list_projects import ListProjectsUseCase
from todo_app.interfaces.controllers.task_controller import TaskController
from todo_app.interfaces.controllers.project_controller import ProjectController


@dataclass
class Application:
    """Container which wires together all components."""
    task_repository: TaskRepository
    project_repository: ProjectRepository
    notification_service: NotificationPort
    task_presenter: TaskPresenter
    project_presenter: ProjectPresenter
    
    # Use cases
    create_task_use_case: CreateTaskUseCase = field(init=False)
    complete_task_use_case: CompleteTaskUseCase = field(init=False)
    get_task_use_case: GetTaskUseCase = field(init=False)
    delete_task_use_case: DeleteTaskUseCase = field(init=False)
    update_task_use_case: UpdateTaskUseCase = field(init=False)

    create_project_use_case: CreateProjectUseCase = field(init=False)
    get_project_use_case: GetProjectUseCase = field(init=False)
    list_projects_use_case: ListProjectsUseCase = field(init=False)
    
    # Controllers
    task_controller: TaskController = field(init=False)
    project_controller: ProjectController = field(init=False)


    def __post_init__(self):
        """Wire up use cases and controllers."""
        # Configure task use cases
        self.create_task_use_case = CreateTaskUseCase(
            self.task_repository, self.project_repository)
        self.complete_task_use_case = CompleteTaskUseCase(
            self.task_repository, self.notification_service
        )
        self.get_task_use_case = GetTaskUseCase(self.task_repository)
        self.delete_task_use_case = DeleteTaskUseCase(self.task_repository)
        self.update_task_use_case = UpdateTaskUseCase(
            self.task_repository, self.notification_service
        )

        # Wire up task controller
        self.task_controller = TaskController(
            create_use_case=self.create_task_use_case,
            complete_use_case=self.complete_task_use_case,
            update_use_case=self.update_task_use_case,
            delete_use_case=self.delete_task_use_case,
            get_use_case=self.get_task_use_case,
            presenter=self.task_presenter,
        )

        # Configure project use cases
        self.create_project_use_case = CreateProjectUseCase(self.project_repository)
        self.get_project_use_case = GetProjectUseCase(self.project_repository)
        self.list_projects_use_case = ListProjectsUseCase(self.project_repository)

        # Wire up project controller
        self.project_controller = ProjectController(
            create_use_case=self.create_project_use_case,
            get_use_case=self.get_project_use_case,
            list_use_case=self.list_projects_use_case,
            presenter=self.project_presenter,
        )
```

<div dir="rtl" style="text-align: right;">
سپس در پیاده‌سازی خود از متد `__post_init__` برای ساخت این اجزا استفاده می‌کنیم.

این کلاس `Application` ساختار روابط اجزای ما را فراهم می‌کند، اما ما هنوز به روشی برای ایجاد نمونه‌های به درستی پیکربندی شده برای تزریق به کلاس کانتینر `Application` نیاز داریم. این توسط متد فکتوری `create_application` ما مدیریت می‌شود:

</div>

```python
# todo_app/infrastructure/configuration/container.py
from todo_app.infrastructure.configuration.factories import create_repositories, create_notification_service
from todo_app.interfaces.presenters import TaskPresenter, ProjectPresenter
from todo_app.domain.services.notification_service import NotificationPort

def create_application(
    notification_service: NotificationPort,
    task_presenter: TaskPresenter,
    project_presenter: ProjectPresenter,
) -> "Application":
    """ Factory function for the Application container. """
    # Call the factory methods
    task_repository, project_repository = create_repositories()
    notification_service_instance = create_notification_service(notification_service) # Pass the provided abstract instance to factory

    return Application(
        task_repository=task_repository,
        project_repository=project_repository,
        notification_service=notification_service_instance,
        task_presenter=task_presenter,
        project_presenter=project_presenter,
    )
```

<div dir="rtl" style="text-align: right;">
این تابع فکتوری، مدیریت وابستگی معماری پاک را در عمل نشان می‌دهد:

*   پارامترهای متد (`notification_service`، `task_presenter`، `project_presenter`) رابط‌های انتزاعی را می‌پذیرند نه پیاده‌سازی‌های بتنی.
*   اجزای پورت از طریق فکتوری‌ها ایجاد می‌شوند: متدهای `create_repositories` و `create_notification_service`.
*   همه این اجزا در نهایت در نمونه‌سازی نهایی کلاس `Application`، جایی که هر وابستگی به درستی پیکربندی و تزریق می‌شود، گرد هم می‌آیند.

جداسازی بین متد فکتوری `create_application` و کلاس `Application`، توجه معماری پاک به جداسازی مسئولیت‌ها را نشان می‌دهد. کانتینر بر روابط اجزا تمرکز دارد در حالی که فکتوری جزئیات ایجاد را مدیریت می‌کند.

در نهایت، اسکریپت `main.py` ما به عنوان رأس ریشه ترکیب ما عمل می‌کند که تنها مکانی است که تمام اجزا در هنگام راه‌اندازی برنامه نمونه‌سازی و به هم متصل می‌شوند:

</div>

```python
# todo_app/main.py (For CLI application)
import sys
from todo_app.infrastructure.configuration.container import create_application
from todo_app.infrastructure.notifications.recorder import NotificationRecorder # For CLI-specific notification service
from todo_app.infrastructure.cli.presenters import CliTaskPresenter, CliProjectPresenter # For CLI-specific presenters
from todo_app.infrastructure.cli.click_cli_app import ClickCli # CLI framework adapter

def main() -> int:
    """Main entry point for the CLI application."""
    try:
        # Create application with dependencies
        app = create_application(
            notification_service=NotificationRecorder(), # CLI specific
            task_presenter=CliTaskPresenter(), # CLI specific
            project_presenter=CliProjectPresenter(), # CLI specific
        )
        # Create and run CLI implementation
        cli = ClickCli(app)
        return cli.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())

```

<div dir="rtl" style="text-align: right;">
این فرآیند بوت‌استرپینگ نشان می‌دهد که چگونه معماری پاک تمام اجزایی را که در این فصل بررسی کرده‌ایم، گرد هم می‌آورد. توجه کنید که چگونه فراخوانی `create_application` اجزای اصلی ما را مونتاژ می‌کند، در حالی که `ClickCli(app)` آداپتور فریم‌ورک ما را مقداردهی اولیه می‌کند. این جداسازی مهم است: ما می‌توانیم این `main` خاص CLI را با یک نقطه ورود برنامه وب جایگزین کنیم که از همان فکتوری `create_application` استفاده می‌کند اما یک آداپتور فریم‌ورک متفاوت مانند FastAPI یا Flask را به جای CLI Click مقداردهی اولیه می‌کند.

استراتژی مدیریت خطا نیز قابل توجه است. بلوک‌های `try/except` سطح بالا، هم خاموش شدن آرام (KeyboardInterrupt) و هم خطاهای غیرمنتظره را در مرز سیستم مدیریت می‌کنند و یک استراتژی خروج پاک از طریق کدهای بازگشتی فراهم می‌کنند. در سراسر این ترکیب، مرزهای معماری پاک دست نخورده باقی می‌مانند: منطق کسب‌وکار مونتاژ شده توسط `create_application` هیچ چیز در مورد پیاده‌سازی CLI ما نمی‌داند، و آداپتور `ClickCli` فقط با انتزاعاتی که توسط کانتینر `Application` ما ارائه می‌شود، تعامل می‌کند.

الگوهای ترکیبی که با مخازن (repositories) ایجاد کردیم، به طور طبیعی به تمام اجزای لایه فریم‌ورک‌ها و درایورهای ما گسترش می‌یابند و یک سیستم منسجم ایجاد می‌کنند که به مرزهای معماری پاک احترام می‌گذارد در حالی که عملکرد عملی را ارائه می‌دهد.

بیایید این بخش را با اذعان به نتیجه نهایی به پایان برسانیم: یک CLI کاربردی که تمام اجزایی را که در این فصل بررسی کرده‌ایم، گرد هم می‌آورد.

</div>

محل دیاگرام ۷.۷: CLI شروع‌کننده برای برنامه مدیریت وظیفه

<div dir="rtl" style="text-align: right;">
همانطور که در شکل ۷.۷ نشان داده شده است، پیاده‌سازی معماری پاک ما کاربران را قادر می‌سازد تا پروژه‌ها و وظایف را از طریق یک رابط بصری مدیریت کنند، با پروژه صندوق ورودی (inbox project) که نشان می‌دهد چگونه انتخاب‌های معماری ما از الگوهای جریان کار طبیعی پشتیبانی می‌کنند.

قابلیت رابط کاربری برای نمایش پروژه‌ها، وظایف، وضعیت‌ها و اولویت‌های آن‌ها در حالی که تعاملات کاربر را به صورت یکپارچه مدیریت می‌کند، نشان می‌دهد که چگونه معماری پاک به ما امکان می‌دهد برنامه‌های کاربردی عملی و کاربرپسند را بدون به خطر انداختن یکپارچگی معماری ایجاد کنیم. هر قطعه اطلاعات نمایش داده شده، از نام پروژه تا اولویت‌های وظیفه، از طریق مرزهای معماری به دقت تعریف شده ما جریان می‌یابد، و ثابت می‌کند که اصول معماری پاک به عملکرد واقعی تبدیل می‌شوند.

</div>

<div dir="rtl" style="text-align: right;">
## خلاصه

</div>

<div dir="rtl" style="text-align: right;">
در این فصل، ما لایه **فریم‌ورک‌ها و درایورها** از معماری پاک را بررسی کردیم، و نشان دادیم که چگونه نگرانی‌های خارجی را ادغام کنیم در حالی که مرزهای معماری پاک را حفظ می‌کنیم. از طریق پیاده‌سازی سیستم مدیریت وظایف ما، دیدیم که چگونه فریم‌ورک‌ها، پایگاه‌های داده و سرویس‌های خارجی را به طور مؤثر مدیریت کنیم در حالی که منطق اصلی کسب‌وکار ما بکر و محافظت شده باقی می‌ماند.

ما چندین الگوی کلیدی را پیاده‌سازی کردیم که مزایای عملی معماری پاک را نشان می‌دهند:

*   **آداپتورهای فریم‌ورک** که به طور پاک، مسائل رابط کاربری را از منطق کسب‌وکار جدا می‌کنند.
*   **پیاده‌سازی‌های پایگاه داده** که انعطاف‌پذیری رابط را نشان می‌دهند.
*   **ادغام سرویس خارجی** که استقلال اصلی را حفظ می‌کند.
*   **مدیریت پیکربندی** که با نیازهای سیستم ما تکامل می‌یابد.

این پیاده‌سازی‌ها نقاط قوت دوگانه معماری پاک را نشان دادند: ایزوله کردن جزئیات پیاده‌سازی در لبه‌ها، در حالی که مسیرهای روشنی را برای تکامل مدل دامنه فراهم می‌کنند. ما این را دو بار در عمل دیدیم. اول، هنگام پیاده‌سازی سرویس‌های خارجی مانند SendGrid بدون دست زدن به منطق اصلی کسب‌وکار ما. دوم، هنگام تکامل رابطه وظیفه-پروژه مدل دامنه ما، که نیاز به تغییر سیستماتیک در لایه‌ها داشت. از مخازن تا آداپتورهای فریم‌ورک، توجه دقیق به مرزهای معماری به ما کمک کرد تا یک سیستم قابل نگهداری ایجاد کنیم که می‌تواند با هر دو نوع تغییر سازگار شود.

در فصل ۸، بررسی خواهیم کرد که چگونه این مرزهای پاک، استراتژی‌های آزمایش جامع را در تمام لایه‌های سیستم ما امکان‌پذیر می‌سازند.

</div>

<div dir="rtl" style="text-align: right;">
## مطالعه بیشتر

</div>

<div dir="rtl" style="text-align: right;">
برای کسب اطلاعات بیشتر در مورد مباحث پوشش داده شده در این فصل، به منابع زیر مراجعه کنید:

*   **Dependency Injector—Dependency Injection Framework for Python** (`https://python-dependency-injector.ets-labs.org/`): برای پروژه‌های پیچیده‌تر، می‌توانید یک فریم‌ورک تزریق وابستگی را برای مدیریت آنچه در اینجا با کلاس `Application` انجام داده‌ایم، در نظر بگیرید.

</div>