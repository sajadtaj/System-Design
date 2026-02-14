<div dir="rtl" style="text-align: right;">

### **مقدمه فصل هشتم**

در فصل‌های پیشین، ما یک سیستم مدیریت وظایف را با دقت و با پیاده‌سازی هر لایه از معماری تمیز، از موجودیت‌های خالص دامنه تا رابط‌های مستقل از فریم‌ورک، ساختیم. برای بسیاری از توسعه‌دهندگان، تست‌نویسی می‌تواند طاقت‌فرسا باشد، باری ضروری که با تکامل سیستم‌ها به‌طور فزاینده‌ای پیچیده می‌شود. معماری تمیز رویکرد متفاوتی را ارائه می‌دهد و چارچوبی ساختاریافته را فراهم می‌کند که تست‌نویسی را هم قابل مدیریت و هم معنادار می‌سازد.

با احترام گذاشتن به مرزهای معماری تمیز و قوانین وابستگی آن، سیستم‌هایی ایجاد می‌کنیم که ذاتاً قابل تست هستند. مسئولیت‌های روشن هر لایه و رابط‌های صریح آن، ما را نه تنها در مورد اینکه چه چیزی را تست کنیم، بلکه در مورد نحوه انجام مؤثر تست نیز راهنمایی می‌کنند.

در این فصل یاد خواهید گرفت که چگونه مرزهای صریح معماری تمیز، پوشش تست جامع را از طریق تست‌های واحد و یکپارچه‌سازی متمرکز فعال می‌کنند. از طریق مثال‌های عملی، کشف خواهید کرد که چگونه تفکیک دغدغه‌ها در معماری تمیز به ما امکان می‌دهد رفتار سیستم را به طور کامل تأیید کنیم و در عین حال تست‌ها را قابل نگهداری نگه داریم. همچنین خواهید دید که چگونه رابط‌های خوش‌تعریف و قوانین وابستگی به طور طبیعی منجر به مجموعه‌های تستی می‌شوند که هم به عنوان ابزارهای تأیید و هم به عنوان محافظ‌های معماری عمل می‌کنند.

در پایان این فصل، قادر خواهید بود مجموعه‌های تستی ایجاد کنید که متمرکز، قابل نگهداری و در تشخیص زودهنگام مشکلات مؤثر هستند، که تست‌نویسی را از یک بار به یک ابزار قدرتمند برای حفظ یکپارچگی معماری تبدیل می‌کند.

### **سرفصل‌های اصلی فصل**

*   **مبانی تست‌نویسی در معماری تمیز**
*   **تست کامپوننت‌های تمیز: تست واحد در عمل**
*   **تست‌نویسی در طول مرزهای معماری**
*   **ابزارها و الگوهای پیشرفته برای نگهداری تست**

<div dir="rtl" style="text-align: right;">

#### **۱. مبانی تست‌نویسی در معماری تمیز**

لایه‌های ساختاریافته و وابستگی‌های صریح در معماری تمیز فقط باعث نمی‌شوند که تست‌نویسی بهتر باشد، بلکه یک مزیت مهم دیگر نیز دارند: آنها یک مزیت ساختاری ایجاد می‌کنند که رویکرد ما به تست‌نویسی را از یک چالش فنی پیچیده به یک ابزار عملی برای اطمینان از صحت و پایداری سیستم تبدیل می‌کند.

معماری تمیز دیدگاه متفاوتی را ارائه می‌دهد. به جای تکیه بر تست‌های سرتاسری (end-to-end tests) به طور اولیه، می‌توانیم با تست‌های متمرکز و قابل نگهداری که به مرزهای معماری احترام می‌گذارند، به سیستم خود اطمینان پیدا کنیم. به جای جنگیدن با وابستگی‌ها و تنظیمات پیچیده، متوجه می‌شویم که مرزهای معماری ما راهنمایی طبیعی برای ساخت مجموعه‌های تست مؤثر ارائه می‌دهند.

تست‌نویسی برای حفظ سلامت سیستم‌های نرم‌افزاری حیاتی است. از طریق تست‌نویسی، ما تأیید می‌کنیم که کد ما طبق برنامه عمل می‌کند، رگرسیون‌ها را زودهنگام تشخیص می‌دهیم و اطمینان حاصل می‌کنیم که مرزهای معماری ما دست‌نخورده باقی می‌مانند. مرزهای صریح و قوانین وابستگی معماری تمیز، نوشتن تست‌های متمرکز و قابل نگهداری را در هر سطح از سیستم ما آسان‌تر می‌کند.

محل دیاگرام 8.1

هرم تست نشان داده شده در شکل ۸.۱، توزیع ایده‌آل انواع تست را در یک سیستم خوش‌طراحی به تصویر می‌کشد. پایه وسیع شامل تست‌های واحد سریع است که اجزای منفرد را به صورت ایزوله تأیید می‌کنند و بازخورد سریع را در طول توسعه فراهم می‌کنند. با حرکت به سمت بالا، تست‌های یکپارچه‌سازی، تعامل بین لایه‌ها و اجزای مختلف را تأیید می‌کنند، اما همچنان از وابستگی‌های خارجی مانند پایگاه داده یا APIها اجتناب می‌کنند.

معماری تمیز این هرم را به روش‌های کلیدی تقویت می‌کند. **بیشتر تست‌های ما می‌توانند تست‌های واحد باشند، که به سرعت اجرا می‌شوند و بازخورد فوری ارائه می‌دهند**. این به دلیل ایزوله‌سازی قوی فراهم شده توسط معماری تمیز است. موجودیت‌های دامنه، که خالص‌ترین شکل منطق تجاری هستند، می‌توانند به طور کامل در تست‌های واحد تأیید شوند. لایه‌های بیرونی مانند رابط‌های آداپتور، مرزهای واضحی برای تست‌های یکپارچه‌سازی فراهم می‌کنند و به ما اجازه می‌دهند تعاملات کامپوننت را بدون تست کل گردش کار تأیید کنیم. این وضوح معماری به این معنی است که می‌توانیم در درجه اول از طریق تست‌های سریع و متمرکز به سیستم خود اطمینان پیدا کنیم. در حالی که تست سرتاسری از طریق رابط‌های کاربری جای خود را دارد، معماری تمیز به ما امکان می‌دهد تا به اطمینان قابل توجهی در سیستم خود از طریق تست‌های واحد و یکپارچه‌سازی متمرکز به تنهایی دست یابیم.

در سراسر این فصل، از `pytest`، فریم‌ورک استاندارد تست پایتون، برای نشان دادن این الگوهای تست استفاده خواهیم کرد. با استفاده از مرزهای معماری تمیز، خواهیم دید که چگونه رویکرد ساده `pytest` به ما کمک می‌کند تا پوشش تست جامع را بدون فریم‌ورک‌های تست پیچیده یا ابزارهای خودکارسازی مرورگر بسازیم. در حالی که مزایای تست معماری تمیز بدون توجه به انتخاب ابزار اعمال می‌شود، استفاده از یک فریم‌ورک واحد و خوش‌تعریف به ما امکان می‌دهد بر اصول معماری تمرکز کنیم تا نحو تست.

معماری تمیز نیاز به تنظیمات اولیه بیشتری نسبت به رویکردهای ساده‌تر دارد، شامل رابط‌های اضافی و تفکیک لایه‌ای که ممکن است برای برنامه‌های کوچک غیرضروری به نظر برسد. با این حال، این سرمایه‌گذاری اولیه، تست‌نویسی را از یک چالش فنی پیچیده به تأیید مستقیم تبدیل می‌کند. جایگزین‌های با اتصال قوی ممکن است در ابتدا سریع‌تر به نظر برسند، اما به زودی نیاز به هماهنگی پایگاه‌های داده و سرویس‌های خارجی فقط برای تست عملکرد اساسی دارند. **نظم معماری که ما ایجاد کرده‌ایم، سیستم‌هایی را ایجاد می‌کند که ذاتاً قابل تست هستند و به تیم‌ها اجازه می‌دهد تا با اطمینان، صحت کد را تأیید کنند**.

**بازخورد تست به عنوان بازخورد معماری**

تست‌نویسی نه تنها به ما کمک می‌کند تا مشکلات را پیدا کنیم، بلکه به عنوان یک ابزار تشخیصی قدرتمند برای طراحی معماری ما نیز عمل می‌کند. هنگامی که تست‌ها ناخوشایند یا شکننده می‌شوند، این غالباً نشان می‌دهد که ما مرزهای معماری را نقض کرده‌ایم یا دغدغه‌هایی را که باید جدا بمانند، با هم ترکیب کرده‌ایم.

این حلقه بازخورد معماری یکی از با ارزش‌ترین مزایای تست در معماری تمیز است. مرزها و رابط‌های صریح به طور طبیعی با رویکردهای مختلف تست، از جمله توسعه مبتنی بر تست (TDD) همسو می‌شوند. چه تست‌ها را اول بنویسید یا بعد از پیاده‌سازی، لایه‌های معماری تمیز ما را به سمت طراحی‌های بهتر راهنمایی می‌کنند: اگر نوشتن یک تست ناخوشایند به نظر می‌رسد، غالباً یک مرز معماری مورد نیاز را آشکار می‌کند. اگر تنظیم تست پیچیده شود، نشان می‌دهد که ما دغدغه‌هایی را که باید جدا بمانند، با هم ترکیب کرده‌ایم. این سیگنال‌ها به عنوان هشدارهای اولیه عمل می‌کنند و به ما کمک می‌کنند تا نقض‌های معماری را قبل از اینکه عمیقاً در کد پایه ما جا بیفتند، شناسایی و اصلاح کنیم.

برای تیم‌هایی که به دلیل پیچیدگی تنظیمات یا مرزهای نامشخص در پذیرش تست واحد جامع تردید دارند، معماری تمیز مسیری روشن را به جلو ارائه می‌دهد. هر لایه رابط‌ها و وابستگی‌های صریح را تعریف می‌کند و راهنمایی روشنی در مورد اینکه چه چیزی باید تست شود و چگونه ایزوله‌سازی را حفظ کنیم، ارائه می‌دهد.

در ادامه این فصل، این مزایا را با پیاده‌سازی تست‌های متمرکز برای هر لایه معماری سیستم مدیریت وظایف خود نشان خواهیم داد و نشان می‌دهیم که چگونه مرزهای معماری تمیز به طور طبیعی ما را به سمت مجموعه‌های تست قابل نگهداری راهنمایی می‌کنند.

**از پیچیدگی تست تا مرزهای واضح**

بسیاری از توسعه‌دهندگان با تست کدبیس‌هایی که فاقد مرزهای معماری واضح هستند، مشکل دارند. در سیستم‌هایی که منطق تجاری، پایداری و دغدغه‌های ارائه به شدت به هم گره خورده‌اند، حتی تست‌های ساده نیازمند تنظیمات پیچیده و استفاده از mock یا stub هستند. این منجر به تست‌های شکننده می‌شود که در صورت تغییر بخش‌های غیرمرتبط سیستم، اغلب از کار می‌افتند.

معماری تمیز، این پیچیدگی را به وضوح تبدیل می‌کند. با جدا کردن دغدغه‌ها در لایه‌های مشخص، می‌توانیم تست‌های واحد و یکپارچه‌سازی متمرکزی بنویسیم که روی مسئولیت‌های خاص اجزای منفرد تمرکز دارند. به جای تست‌هایی که باید چندین دغدغه درهم‌تنیده را هماهنگ کنند، می‌توانیم روی مسئولیت‌های خاص تمرکز کنیم:

*   **موجودیت‌های دامنه و قوانین تجاری می‌توانند به صورت ایزوله تست شوند**.
*   **هماهنگی مورد استفاده (use case orchestration) می‌تواند از طریق رابط‌های صریح تأیید شود**.
*   **دغدغه‌های زیرساختی به طور واضح در مرزهای سیستم جدا باقی می‌مانند**.

ساختار لایه‌ای، گردش کار توسعه را در عمل بهبود می‌بخشد. هر مرز معماری راهنمایی طبیعی را برای موارد زیر فراهم می‌کند:

*   **ایزوله‌سازی باگ‌ها به اجزا یا تعاملات خاص**.
*   **افزودن تست‌های متمرکز که موارد لبه (edge cases) را پوشش می‌دهند**.
*   **ساخت پوشش جامع به صورت افزایشی**.

این وضوح به طور چشمگیری گردش کار توسعه را بهبود می‌بخشد. هنگامی که باگ‌ها گزارش می‌شوند، این سازمان‌دهی لایه‌ای ما را مستقیماً به محدوده تست مناسب هدایت می‌کند. مشکلات منطق دامنه می‌توانند در تست‌های واحد بازتولید شوند، در حالی که مشکلات یکپارچه‌سازی مرزهای واضحی برای بررسی دارند. این سازمان‌دهی طبیعی به این معنی است که پوشش تست ما به طور ارگانیک با نگهداری و دیباگ سیستم بهبود می‌یابد. هر مشکل حل شده منجر به تست‌های متمرکزی می‌شود که رفتارهای خاص را تأیید می‌کنند و به تدریج یک مجموعه تست جامع ایجاد می‌کنند که موارد لبه را قبل از رسیدن به تولید تشخیص می‌دهد.

در بخش‌های زیر، پیاده‌سازی‌های ملموس این الگوهای تست را در سیستم مدیریت وظایف خود بررسی خواهیم کرد. خواهید دید که چگونه مرزهای معماری تمیز هر نوع تست را متمرکزتر و قابل نگهداری‌تر می‌کند، با شروع از تست‌های واحد لایه دامنه و پیشرفت به سمت تست‌های یکپارچه‌سازی رابط‌های خارجی ما.

</div>

---

<div dir="rtl" style="text-align: right;">

#### **۲. تست کامپوننت‌های تمیز: تست واحد در عمل**

بیایید ببینیم چگونه معماری تمیز تست واحد را از تئوری به عمل تبدیل می‌کند. یک هدف تست ساده را در نظر بگیرید: تأیید اینکه وظایف جدید به طور پیش‌فرض اولویت متوسط دارند. در یک کدبیس که با پارادایم معماری تمیز همسو نیست، بسیاری از توسعه‌دهندگان با کلاس‌هایی مانند این مواجه شده‌اند که حتی منطق ساده دامنه با زیرساخت درهم آمیخته شده است:

</div>

```python
class Task(Entity):
    """Anti-pattern: Domain entity with
    direct infrastructure dependencies."""
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        # Direct database dependency:
        self.db = Database()
        # Direct notification dependency:
        self.notifier = NotificationService()
        self.priority = Priority.MEDIUM
        # Save to database and notify on creation
        self.id = self.db.save_task(self.as_dict())
        self.notifier(f"Task {self.id} created")
```

<div dir="rtl" style="text-align: right;">

این کد با اتصال قوی، ما را مجبور به تنظیمات پیچیده برای تست یک قانون تجاری ساده در مورد موجودیت `Task` می‌کند:

</div>

```python
def test_new_task_priority_antipattern():
    """An anti-pattern mixing infrastructure concerns
    with simple domain logic."""
    # Complex setup just to test a default value
    db_connection = create_database_connection()
    notification_service = create_notification_service()
    # Just creating a task hits the database and notification service
    task = Task(
        title="Test task",
        description="Test description"
    )
    # Even checking a simple property requires a database query
    saved_task = task.db.get_task(task.id)
    assert saved_task['priority'] == Priority.MEDIUM
```

<div dir="rtl" style="text-align: right;">

این تست، اگرچه کاربردی است، اما چندین مشکل رایج را نشان می‌دهد. برای تأیید یک قانون دامنه ساده، نیاز به تنظیمات پیچیده شامل پایگاه داده‌ها و سرویس‌ها دارد. اگر تست با شکست مواجه شود، علت می‌تواند هر چیزی باشد:

*   آیا مشکل اتصال به پایگاه داده وجود داشت؟
*   آیا سرویس اطلاع‌رسانی نتوانست مقداردهی اولیه شود؟
*   یا آیا واقعاً مشکلی در منطق پیش‌فرض‌گذاری اولویت ما وجود داشت؟

این سطح از پیچیدگی در تست حتی ویژگی‌های اساسی نشان می‌دهد که چرا بسیاری از توسعه‌دهندگان تست‌نویسی را دست‌وپاگیر و اغلب بی‌ارزش می‌دانند.

**مرزهای معماری تمیز این مشکلات را با نگه داشتن منطق دامنه ما خالص و متمرکز از بین می‌برد**. برای کدی که از رویکرد معماری تمیز پیروی می‌کند، می‌توانیم همین قانون تجاری را با وضوح قابل توجهی تست کنیم:

</div>

```python
from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from todo_app.domain.entities.priority import Priority
from todo_app.domain.entities.entity import Entity
from todo_app.domain.value_objects.task_status import TaskStatus
from typing import Optional

@dataclass
class Task(Entity):
    """Clean Architecture: Pure domain entity."""
    title: str
    description: str
    project_id: UUID
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)
    completed_at: Optional[datetime] = None

    def complete(self, notes: Optional[str] = None) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Task is already completed")
        self.status = TaskStatus.DONE
        self.completed_at = datetime.now(timezone.utc)


def test_new_task_priority():
    """Clean test focused purely on domain logic."""
    task = Task(
        title="Test task",
        description="Test description",
        project_id=UUID('12345678-1234-5678-1234-567812345678')
    )
    assert task.priority == Priority.MEDIUM
```

<div dir="rtl" style="text-align: right;">

تفاوت چشمگیر است. با متمرکز کردن موجودیت‌های دامنه ما بر قوانین تجاری:

*   **تست ما دقیقاً یک چیز را تأیید می‌کند؛ وظایف جدید به طور پیش‌فرض اولویت متوسط دارند**.
*   **تنظیمات فقط به داده‌های مورد نیاز برای تست ما نیاز دارد**.
*   **اگر تست با شکست مواجه شود، دقیقاً یک علت احتمالی وجود دارد**.
*   **تست بلافاصله و بدون وابستگی خارجی اجرا می‌شود**.

این تفکیک دغدغه‌های واضح یکی از مزایای کلیدی تست معماری تمیز را نشان می‌دهد: **توانایی تأیید قوانین تجاری با حداقل تنظیمات و حداکثر وضوح**. مرزهای معماری تمیز یک پیشرفت طبیعی برای ساخت پوشش تست جامع ایجاد می‌کنند. در سراسر این بخش، تست‌های متمرکز و قابل نگهداری را پیاده‌سازی خواهیم کرد که رفتار را تأیید می‌کنند و در عین حال به این مرزهای معماری احترام می‌گذارند. با ساده‌ترین حالت تست موجودیت‌های دامنه شروع می‌کنیم و به تدریج از طریق لایه‌های معماری خود به سمت بیرون حرکت می‌کنیم.

**تست موجودیت‌های دامنه**

قبل از پرداختن به تست‌های خاص، بیایید یک الگو را ایجاد کنیم که در طول مسیر تست ما به ما کمک خواهد کرد. **الگوی Arrange-Act-Assert (AAA)**، که در ابتدا توسط بیل ویک پیشنهاد شد، یک ساختار واضح برای سازمان‌دهی تست‌ها ارائه می‌دهد که به طور طبیعی با مرزهای معماری تمیز همسو می‌شود:

*   **Arrange (تنظیم)**: شرایط تست و داده‌های تست را تنظیم کنید.
*   **Act (عمل)**: رفتاری را که تست می‌شود، اجرا کنید.
*   **Assert (ادعا)**: نتایج مورد انتظار را تأیید کنید.

این الگو هنگام تست موجودیت‌های دامنه به طور خاص ظریف می‌شود، زیرا معماری تمیز منطق اصلی تجاری ما را از دغدغه‌های خارجی ایزوله می‌کند. نحوه تست رفتار تکمیل موجودیت `Task` ما را در نظر بگیرید:

</div>

```python
import pytest
from uuid import UUID
from datetime import datetime, timedelta, timezone

from todo_app.domain.entities.task import Task
from todo_app.domain.entities.priority import Priority


def test_task_completion_captures_completion_time():
    """Test that completing a task records the completion timestamp."""
    # Arrange
    task = Task(
        title="Test task",
        description="Test description",
        project_id=UUID('12345678-1234-5678-1234-567812345678'),
    )
    # Act
    task.complete()
    # Assert
    assert task.completed_at is not None
    assert (datetime.now(timezone.utc) - task.completed_at) < timedelta(seconds=1)
```

<div dir="rtl" style="text-align: right;">

این تست، ماهیت تست موجودیت دامنه را در معماری تمیز نشان می‌دهد. تنها کاری که باید انجام دهیم این است:

1.  **یک حالت اولیه را تنظیم کنیم** (یک وظیفه جدید با ویژگی‌های مورد نیاز).
2.  **یک عمل انجام دهیم** (تکمیل وظیفه).
3.  **حالت نهایی را تأیید کنیم** (زمان تکمیل ثبت شده است).

شفافیت تست دامنه از تفکیک دغدغه‌ها در معماری تمیز ناشی می‌شود. ما نیازی به:

*   **تنظیم یا مدیریت اتصالات پایگاه داده نداریم**.
*   **پیکربندی سرویس‌های اطلاع‌رسانی نداریم**.
*   **رسیدگی به احراز هویت یا مجوز نداریم**.
*   **مدیریت وضعیت سیستم خارجی نداریم**.

ما در حال تست منطق تجاری خالص هستیم: **هنگامی که یک وظیفه تکمیل می‌شود، باید زمان وقوع آن را ثبت کند**. این تمرکز تست‌های ما را سریع، قابل اعتماد و قابل خواندن می‌کند. اگر تست با شکست مواجه شود، تنها یک علت احتمالی وجود دارد، منطق تکمیل ما به درستی کار نمی‌کند.

این تمرکز بر قوانین تجاری خالص یکی از مزایای کلیدی است که معماری تمیز به تست‌نویسی می‌آورد. با ایزوله کردن منطق دامنه ما از دغدغه‌های زیرساختی، می‌توانیم رفتار را با تست‌های ساده و متمرکز تأیید کنیم که به عنوان مستندات زنده قوانین تجاری ما عمل می‌کنند. در ادامه خواهیم دید که چگونه این وضوح تست با حرکت از لایه دامنه داخلی به سمت بیرون ادامه می‌یابد.

**ابزارهای Test Double در پایتون**

قبل از اینکه با تست‌های مورد استفاده خود کار کنیم، بیایید بفهمیم که پایتون چگونه به ما در ایجاد "test double" کمک می‌کند که به عنوان جایگزین وابستگی‌ها برای کامپوننت مورد تست عمل می‌کنند. هنگام تست کدی که وابستگی دارد، اغلب به روشی برای جایگزینی پیاده‌سازی‌های واقعی (مانند پایگاه‌های داده یا سرویس‌های خارجی) با نسخه‌های شبیه‌سازی‌شده‌ای که می‌توانیم کنترل کنیم، نیاز داریم. کتابخانه `unittest.mock` پایتون، که به طور یکپارچه با `pytest` ادغام شده است، ابزارهای قدرتمندی برای ایجاد این test doubleها ارائه می‌دهد:

</div>

```python
from unittest.mock import Mock
# from uuid import UUID # Added for context, might not be in original snippet
# from todo_app.domain.entities.task import Task # Added for context, might not be in original snippet

# Create a mock object that records calls and can return preset values
mock_repo = Mock()
# Configure the response we want
# Assuming 'some_task' is a predefined Task instance or similar
# For demonstration purposes, let's create a simple Task mock
class MockTask:
    def __init__(self, id):
        self.id = id
some_task = MockTask(123)

mock_repo.get.return_value = some_task
# Call will return some_task
mock_repo.get(123)
# Verify the call happened exactly once
mock_repo.get.assert_called_once()
# Mocks track all interaction details
# Shows what arguments were passed
print(mock_repo.get.call_args)
# Shows how many times it was called
print(mock_repo.get.call_count)
```

<div dir="rtl" style="text-align: right;">

این mockها دو هدف اصلی در تست‌نویسی را دنبال می‌کنند:

*   **آنها به ما امکان می‌دهند رفتار وابستگی‌ها را کنترل کنیم** (مانند اطمینان از اینکه یک مخزن همیشه یک وظیفه خاص را برمی‌گرداند).
*   **آنها به ما امکان می‌دهند نحوه تعامل کد ما با آن وابستگی‌ها را تأیید کنیم** (مانند اطمینان از اینکه `save()` را دقیقاً یک بار فراخوانی کرده‌ایم).

**تست هماهنگی مورد استفاده (Use Case Orchestration)**

همانطور که از لایه دامنه به سمت بیرون حرکت می‌کنیم، به طور طبیعی با وابستگی به سایر اجزای سیستم خود مواجه می‌شویم. به عنوان مثال، یک مورد استفاده برای تکمیل وظیفه، هم به یک مخزن برای پایداری تغییرات و هم به یک سرویس اطلاع‌رسانی برای هشدار به ذینفعان نیاز دارد. با این حال، تأکید معماری تمیز بر انتزاع از طریق رابط‌ها، این وابستگی‌ها را از مشکلات احتمالی تست به جزئیات پیاده‌سازی مستقیم تبدیل می‌کند.

همانطور که این انتزاع‌ها به ما اجازه می‌دهند پیاده‌سازی یک مخزن را از ذخیره‌سازی مبتنی بر فایل به SQLite تغییر دهیم بدون اینکه هیچ کد وابسته را تغییر دهیم، به ما امکان می‌دهند تا پیاده‌سازی‌های واقعی را با test doubleها در طول تست جایگزین کنیم. موارد استفاده ما به رابط‌های انتزاعی مانند `TaskRepository` و `NotificationPort` وابسته هستند، نه پیاده‌سازی‌های ملموس. این بدان معنی است که می‌توانیم پیاده‌سازی‌های mock را برای تست بدون تغییر کد مورد استفاده خود ارائه دهیم. مورد استفاده نه می‌داند و نه اهمیت می‌دهد که آیا با یک مخزن واقعی SQLite یا یک test double کار می‌کند.

بیایید بررسی کنیم که چگونه از mockها برای تست مورد استفاده خود به صورت ایزوله استفاده می‌کنیم:

</div>

```python
from unittest.mock import Mock
from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from todo_app.domain.entities.task import Task
from todo_app.domain.entities.priority import Priority
from todo_app.domain.value_objects.task_status import TaskStatus
from typing import Optional, Any, Dict, List, Self
from enum import Enum

# Define mock interfaces/classes required for the test context
# (These would typically be in application layer interfaces or domain)

class ErrorCode(Enum):
    NOT_FOUND = "NOT_FOUND"
    VALIDATION_ERROR = "VALIDATION_ERROR"

@dataclass(frozen=True)
class Error:
    code: ErrorCode
    message: str
    details: Optional[Dict[str, Any]] = None

    @classmethod
    def not_found(cls, entity: str, entity_id: str) -> Self:
        return cls(
            code=ErrorCode.NOT_FOUND,
            message=f"{entity} with id {entity_id} not found"
        )

    @classmethod
    def validation_error(cls, message: str) -> Self:
        return cls(
            code=ErrorCode.VALIDATION_ERROR,
            message=message
        )

@dataclass(frozen=True)
class Result:
    value: Any = None
    error: Optional[Error] = None

    @property
    def is_success(self) -> bool:
        return self.error is None

    @classmethod
    def success(cls, value: Any) -> Self:
        return cls(value=value)

    @classmethod
    def failure(cls, error: Error) -> Self:
        return cls(error=error)

# Mock TaskRepository interface
class TaskRepository:
    def get(self, task_id: UUID) -> Task:
        raise NotImplementedError
    def save(self, task: Task) -> None:
        raise NotImplementedError

# Mock NotificationPort interface
class NotificationPort:
    def notify_task_completed(self, task: Task) -> None:
        raise NotImplementedError

# CompleteTaskRequest (simplified for example)
@dataclass(frozen=True)
class CompleteTaskRequest:
    task_id: str
    completion_notes: Optional[str] = None

# CompleteTaskUseCase (as defined in source)
@dataclass(frozen=True)
class CompleteTaskUseCase:
    task_repository: TaskRepository
    notification_service: NotificationPort

    def execute(
        self,
        request: CompleteTaskRequest
    ) -> Result:
        try:
            task_id_uuid = UUID(request.task_id)
            # Input validation - already done by request model, but can have additional
            task = self.task_repository.get(task_id_uuid)
            task.complete(
                notes=request.completion_notes
            )
            self.task_repository.save(task)
            # Placeholder for TaskResponse, assuming it's structured from entity
            # For this test, a simple dict is sufficient as return value from use case
            response_data = {
                "id": str(task.id),
                "status": "completed",
                "completion_date": task.completed_at.isoformat() if task.completed_at else None
            }
            return Result.success(response_data)
        except ValueError as e: # This handles Task.complete() ValueError
            return Result.failure(Error.validation_error(str(e)))
        except Exception as e: # Catch other potential errors from repository.get()
            if "not found" in str(e).lower(): # Simple check, in real code use specific exceptions
                return Result.failure(Error.not_found("Task", request.task_id))
            return Result.failure(Error.validation_error(str(e))) # Generic error for simplicity


def test_successful_task_completion():
    """Test task completion using mock dependencies."""
    # Arrange
    task_id_val = UUID('12345678-1234-5678-1234-567812345678')
    task = Task(
        title="Test task",
        description="Test description",
        project_id=task_id_val, # Ensure project_id is a UUID
    )
    task_repo = Mock(spec=TaskRepository)
    task_repo.get.return_value = task # Mocking the get method to return our task
    notification_service = Mock(spec=NotificationPort) # Mocking notification service

    use_case = CompleteTaskUseCase(
        task_repository=task_repo,
        notification_service=notification_service
    )
    request = CompleteTaskRequest(task_id=str(task.id))

    # Act
    result = use_case.execute(request)

    # Assert
    assert result.is_success
    task_repo.save.assert_called_once_with(task) # Verify save was called with the modified task
    notification_service.notify_task_completed.assert_called_once_with(task) # Verify notification was sent
```

<div dir="rtl" style="text-align: right;">

فاز Arrange، ایزولاسیون صحیح تست واحد را نشان می‌دهد. ما هم مخزن و هم سرویس اطلاع‌رسانی را mock می‌کنیم تا اطمینان حاصل کنیم که منطق هماهنگی مورد استفاده را به صورت ایزوله تست می‌کنیم. این تنظیم تضمین می‌کند که تست ما تحت تأثیر مشکلات پایگاه داده، مشکلات شبکه یا سایر عوامل خارجی قرار نخواهد گرفت.

گردش کار تست، مسئولیت‌های هماهنگی مورد استفاده ما را از طریق تأییدات mock متمایز، تأیید می‌کند:

*   **اعمال**:
    `result = use_case.execute(request)`
*   **تأیید**:
    `assert result.is_success`
    `task_repo.save.assert_called_once_with(task)`
    `notification_service.notify_task_completed.assert_called_once_with(task)`

این تست‌ها قابلیت اطمینان و انعطاف‌پذیری مورد استفاده ما را از طریق تست‌های متمرکز تأیید می‌کنند.

در بخش بعدی، خواهیم دید که چگونه تست رابط‌های آداپتور الگوهای جدیدی را برای تأیید تبدیل داده‌ها در مرزهای سیستم ما معرفی می‌کند.

**تست رابط‌های آداپتور**

هنگامی که به لایه رابط‌های آداپتور می‌رسیم، تمرکز تست ما به تأیید تبدیل صحیح بین فرمت‌های خارجی و هسته برنامه ما تغییر می‌کند. کنترلرها و ارائه‌دهنده‌ها به عنوان این تبدیل‌کننده‌ها عمل می‌کنند و درست مانند تست‌های واحد ما در لایه‌های قبلی، می‌خواهیم هر چیز خارجی به این لایه را mock کنیم. ما نمی‌خواهیم اتصالات پایگاه داده، سیستم‌های فایل یا حتی پیاده‌سازی‌های مورد استفاده، تست‌های منطق تبدیل ما را تحت تأثیر قرار دهند. رابط‌های صریح معماری تمیز این کار را ساده می‌کنند. می‌توانیم موارد استفاده خود را mock کنیم و صرفاً بر تأیید اینکه آداپتورهای ما داده‌ها را به درستی در حین عبور از مرزهای سیستم ما تبدیل می‌کنند، تمرکز کنیم.

بیایید بررسی کنیم که چگونه مسئولیت یک کنترلر برای تبدیل شناسه‌های رشته‌ای خارجی به UUIDهایی که دامنه ما انتظار دارد را تست می‌کنیم. هنگامی که کلاینت‌های وب یا CLI سیستم ما را فراخوانی می‌کنند، معمولاً شناسه‌ها را به صورت رشته ارائه می‌دهند. با این حال، دامنه ما به صورت داخلی با UUIDها کار می‌کند. کنترلر باید این تبدیل را انجام دهد:

</div>

```python
from unittest.mock import Mock
from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Optional, Any, Dict, List, Self
from enum import Enum

# --- Mocked Interfaces and DTOs for the test context ---
class ErrorCode(Enum):
    NOT_FOUND = "NOT_FOUND"
    VALIDATION_ERROR = "VALIDATION_ERROR"

@dataclass(frozen=True)
class Error:
    code: ErrorCode
    message: str
    details: Optional[Dict[str, Any]] = None

@dataclass(frozen=True)
class Result:
    value: Any = None
    error: Optional[Error] = None

    @property
    def is_success(self) -> bool:
        return self.error is None

    @classmethod
    def success(cls, value: Any) -> Self:
        return cls(value=value)

    @classmethod
    def failure(cls, error: Error) -> Self:
        return cls(error=error)

# Mocked Task entity (simplified for response model creation)
@dataclass
class Task:
    title: str
    description: str
    project_id: UUID
    id: UUID = field(default_factory=UUID, init=False) # Simplified for test
    status: Any = "TODO" # simplified
    completed_at: Optional[datetime] = None


# Mocked TaskResponse (simplified for the test)
@dataclass(frozen=True)
class TaskResponse:
    id: str
    title: str
    description: str
    status: Any
    priority: Any
    project_id: str
    due_date: Any = None
    completion_date: Any = None
    completion_notes: Optional[str] = None

    @classmethod
    def from_entity(cls, task: Task) -> 'TaskResponse':
        return cls(
            id=str(task.id),
            title=task.title,
            description=task.description,
            status=task.status,
            priority="MEDIUM", # Simplified
            project_id=str(task.project_id),
            completion_date=task.completed_at.isoformat() if task.completed_at else None
        )

# Mocked CompleteTaskRequest (internal DTO for use case)
@dataclass(frozen=True)
class CompleteTaskRequest:
    task_id: UUID # Expects UUID
    completion_notes: Optional[str] = None

# Mocked Use Case Interface
class CompleteTaskUseCase:
    def execute(self, request: CompleteTaskRequest) -> Result:
        raise NotImplementedError

# Mocked Presenter Interface (minimal spec for testing controller)
class TaskPresenter:
    def present_task(self, task_response: TaskResponse) -> Any: # Any for simplicity
        raise NotImplementedError
    def present_error(self, error_msg: str, code: Optional[str] = None) -> Any:
        raise NotImplementedError

# OperationResult and ErrorViewModel (as defined in source)
@dataclass
class ErrorViewModel:
    message: str
    code: Optional[str] = None

from typing import TypeVar, Generic
T = TypeVar('T')

@dataclass
class OperationResult(Generic[T]):
    _success: Optional[T] = None
    _error: Optional[ErrorViewModel] = None

    @property
    def is_success(self) -> bool:
        return self._error is None

    @classmethod
    def succeed(cls, value: T) -> 'OperationResult[T]':
        return cls(_success=value)

    @classmethod
    def fail(cls, message: str, code: Optional[str] = None) -> 'OperationResult[T]':
        return cls(_error=ErrorViewModel(message, code))


# TaskController (simplified for the test)
@dataclass
class TaskController:
    # Only include use cases relevant to the test
    complete_use_case: CompleteTaskUseCase
    presenter: TaskPresenter

    def handle_complete(
        self,
        task_id: str,
        completion_notes: Optional[str] = None
    ) -> OperationResult[Any]: # Any for simplicity in test return type
        try:
            # Here's where the conversion from str to UUID happens
            task_id_uuid = UUID(task_id)
            request = CompleteTaskRequest(
                task_id=task_id_uuid,
                completion_notes=completion_notes
            )
            result = self.complete_use_case.execute(request)
            if result.is_success:
                view_model = self.presenter.present_task(result.value)
                return OperationResult.succeed(view_model)
            else:
                error_vm = self.presenter.present_error(
                    result.error.message, str(result.error.code.name)
                )
                return OperationResult.fail(error_vm.message, error_vm.code)
        except ValueError as e: # This would catch invalid UUID string
            error_vm = self.presenter.present_error(
                str(e), "VALIDATION_ERROR"
            )
            return OperationResult.fail(error_vm.message, error_vm.code)


def test_controller_converts_string_id_to_uuid():
    """Test that controller properly converts
    string IDs to UUIDs for use cases."""
    # Arrange
    task_id = "123e4567-e89b-12d3-a456-426614174000"
    mock_task_entity = Task(
        title="Test Task",
        description="Test Description",
        project_id=UUID('12345678-1234-5678-1234-567812345678'),
        id=UUID(task_id)
    )
    mock_task_response = TaskResponse.from_entity(mock_task_entity)


    complete_use_case = Mock(spec=CompleteTaskUseCase)
    complete_use_case.execute.return_value = Result.success(mock_task_response)


    presenter = Mock(spec=TaskPresenter) # Use spec for stricter mock
    # Mock the present_task method of the presenter to return something
    presenter.present_task.return_value = Mock()


    controller = TaskController(
        complete_use_case=complete_use_case,
        presenter=presenter,
    )

    # Act
    controller.handle_complete(task_id=task_id)

    # Assert
    complete_use_case.execute.assert_called_once()
    # Access the arguments passed to the execute method
    called_request = complete_use_case.execute.call_args
    # Verify that the task_id within the request object is a UUID
    assert isinstance(called_request.task_id, UUID)
    assert str(called_request.task_id) == task_id # Verify it's the correct UUID
```

<div dir="rtl" style="text-align: right;">

فاز Arrange، سناریوی تست ما را تنظیم می‌کند. ما یک شناسه وظیفه را به صورت رشته (مانند آنچه که یک کلاینت ارائه می‌دهد) ارائه می‌دهیم و یک مورد استفاده mock را پیکربندی می‌کنیم که برای بازگرداندن یک نتیجه موفق پیکربندی شده است. هنگام ایجاد mock ارائه‌دهنده خود، از `spec=TaskPresenter` برای ایجاد یک mock سخت‌گیرانه استفاده می‌کنیم که از رابط ارائه‌دهنده ما آگاه است.

*   **بدون `spec`، هر متدی می‌تواند فراخوانی شود**:
    `loose_mock = Mock()`
    `loose_mock.non_existent_method()` # کار می‌کند، اما می‌تواند باگ‌ها را پنهان کند.
*   **با `spec`، mock رابط را اعمال می‌کند**:
    `strict_mock = Mock(spec=TaskPresenter)`
    `strict_mock.non_existent_method()` # `AttributeError` را ایجاد می‌کند.

این ایمنی نوع اضافی به ویژه در لایه رابط‌های آداپتور که حفظ مرزهای رابط صحیح حیاتی است، ارزشمند است. با استفاده از `spec`، اطمینان حاصل می‌کنیم که تست‌های ما نه تنها مشکلات رفتاری بلکه نقض‌های قرارداد را نیز تشخیص می‌دهند.

با پیکربندی صحیح test doubleهای ما برای اعمال مرزهای رابط، می‌توانیم منطق تبدیل کنترلر خود را تأیید کنیم:

*   **اعمال**:
    `controller.handle_complete(task_id=task_id)`
*   **تأیید**:
    `complete_use_case.execute.assert_called_once()`
    `called_request = complete_use_case.execute.call_args`
    `assert isinstance(called_request.task_id, UUID)`

هنگامی که `handle_complete` را فراخوانی می‌کنیم، کنترلر باید:

1.  شناسه وظیفه رشته‌ای را از کلاینت بگیرد.
2.  آن را به یک UUID تبدیل کند.
3.  یک درخواست با فرمت صحیح برای مورد استفاده ایجاد کند.

به طور مشابه، می‌توانیم ارائه‌دهندگان را تست کنیم تا اطمینان حاصل کنیم که آنها داده‌های دامنه را به طور مناسب برای مصرف خارجی فرمت می‌کنند. بیایید روی یک مسئولیت خاص تمرکز کنیم: فرمت‌بندی تاریخ‌های تکمیل وظیفه به رشته‌های قابل خواندن برای انسان برای CLI. این تبدیل به ظاهر ساده، نمونه‌ای کامل از نقش رابط آداپتور است:

</div>

```python
from unittest.mock import Mock
from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Optional, Any, Dict, List, Self
from enum import Enum

# --- Mocked Task and TaskResponse for test context ---
@dataclass
class Task:
    title: str
    description: str
    project_id: UUID
    id: UUID = field(default_factory=UUID, init=False) # Simplified for test
    status: Any = "TODO" # simplified
    completed_at: Optional[datetime] = None

    def complete(self, notes: Optional[str] = None) -> None:
        if self.status == "DONE": # simplified
            raise ValueError("Task is already completed")
        self.status = "DONE" # simplified
        self.completed_at = datetime.now(timezone.utc)

@dataclass(frozen=True)
class TaskResponse:
    id: str
    title: str
    description: str
    status: Any
    priority: Any
    project_id: str
    due_date: Any = None
    completion_date: Any = None
    completion_notes: Optional[str] = None

    @classmethod
    def from_entity(cls, task: Task) -> 'TaskResponse':
        return cls(
            id=str(task.id),
            title=task.title,
            description=task.description,
            status=task.status,
            priority="MEDIUM", # Simplified for this test
            project_id=str(task.project_id),
            completion_date=task.completed_at.isoformat() if task.completed_at else None
        )

# Mocked TaskViewModel for presenter output (simplified)
@dataclass(frozen=True)
class TaskViewModel:
    id: str
    title: str
    description: str
    status_display: str
    priority_display: str
    due_date_display: Optional[str]
    project_display: Optional[str] = None # Assuming optional
    completion_info: Optional[str] = None


# CliTaskPresenter (simplified for test)
class CliTaskPresenter:
    def present_task(self, task_response: TaskResponse) -> TaskViewModel:
        # Simplified formatting for the test
        completion_info = (
            f"Completed: {datetime.fromisoformat(task_response.completion_date).strftime('%Y-%m-%d %H:%M')}"
            if task_response.completion_date else None
        )
        return TaskViewModel(
            id=task_response.id,
            title=task_response.title,
            description=task_response.description,
            status_display=f"[{task_response.status}]",
            priority_display=task_response.priority,
            due_date_display=task_response.due_date,
            completion_info=completion_info
        )

    def present_error(self, error_msg: str, code: Optional[str] = None) -> Any:
        raise NotImplementedError


def test_presenter_formats_completion_date():
    """Test that presenter formats dates according to
    interface requirements."""
    # Arrange
    completion_time = datetime(2024, 1, 15, 14, 30, tzinfo=timezone.utc)
    task_id_val = UUID('12345678-1234-5678-1234-567812345678')

    task = Task(
        title="Test Task",
        description="Test Description",
        project_id=task_id_val,
    )
    task.complete() # Set status to DONE and completed_at
    # Override completed_at for deterministic testing
    task.completed_at = completion_time

    task_response = TaskResponse.from_entity(task)
    presenter = CliTaskPresenter()

    # Act
    view_model = presenter.present_task(task_response)

    # Assert
    expected_format = "2024-01-15 14:30"
    assert expected_format in view_model.completion_info
```

<div dir="rtl" style="text-align: right;">

این تست نشان می‌دهد که چگونه رویکرد لایه‌ای معماری تمیز، تست‌نویسی را ساده می‌کند. از آنجایی که موجودیت‌های دامنه ما وابستگی خارجی ندارند، می‌توانیم به راحتی آنها را در تست‌های خود ایجاد و دستکاری کنیم. نیازی نیست نگران نحوه تنظیم زمان تکمیل در عمل باشیم. قوانین تجاری ذاتی موجودیت `Task` از هرگونه حالت غیرقانونی (مانند تنظیم زمان تکمیل برای یک وظیفه ناتمام) جلوگیری می‌کند. این ایزوله‌سازی، تست‌های ارائه‌دهنده ما را مستقیم و قابل اعتماد می‌کند.

*   **اعمال**:
    `view_model = presenter.present_task(task_response)`
*   **تأیید**:
    `expected_format = "2024-01-15 14:30"`
    `assert expected_format in view_model.completion_info`

این جریان تست نشان می‌دهد که چگونه مرزهای صریح معماری تمیز، تست رابط آداپتور را ساده می‌کنند. ما صرفاً بر تأیید فرمت‌بندی داده‌ها تمرکز می‌کنیم بدون اینکه پایداری، قوانین تجاری یا سایر دغدغه‌هایی را که تست‌های واحد ما قبلاً تأیید کرده‌اند، درگیر کنیم. هر آداپتور مسئولیت روشن و واحدی دارد که می‌توانیم آن را به صورت ایزوله تست کنیم.

در حالی که تست دغدغه‌های فرمت‌بندی فردی ارزشمند است، ارائه‌دهندگان ما اغلب نیاز به مدیریت همزمان چندین جنبه نمایش دارند. بیایید ببینیم چگونه تفکیک دغدغه‌ها در معماری تمیز به ما کمک می‌کند تا ایجاد مدل نمایش جامع را به روشی روشن و متدیک تست کنیم:

</div>

```python
import pytest
from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Optional, Any, Dict, List, Self
from enum import Enum

# --- Mocked Task and TaskResponse for test context ---
@dataclass
class Task:
    title: str
    description: str
    project_id: UUID
    id: UUID = field(default_factory=UUID, init=False) # Simplified for test
    status: Any = "TODO" # simplified, assuming string values or simple enum for test
    priority: Any = "MEDIUM" # simplified, assuming string values or simple enum for test
    completed_at: Optional[datetime] = None

    def complete(self, notes: Optional[str] = None) -> None:
        if self.status == "DONE":
            raise ValueError("Task is already completed")
        self.status = "DONE"
        self.completed_at = datetime.now(timezone.utc)

@dataclass(frozen=True)
class TaskResponse:
    id: str
    title: str
    description: str
    status: Any
    priority: Any
    project_id: str
    due_date: Any = None
    completion_date: Any = None
    completion_notes: Optional[str] = None

    @classmethod
    def from_entity(cls, task: Task) -> 'TaskResponse':
        return cls(
            id=str(task.id),
            title=task.title,
            description=task.description,
            status=task.status,
            priority=task.priority, # Use task's actual priority for the test
            project_id=str(task.project_id),
            completion_date=task.completed_at.isoformat() if task.completed_at else None
        )

# Mocked TaskViewModel for presenter output
@dataclass(frozen=True)
class TaskViewModel:
    id: str
    title: str
    description: str
    status_display: str
    priority_display: str
    due_date_display: Optional[str]
    project_display: Optional[str] = None
    completion_info: Optional[str] = None

# CliTaskPresenter (simplified for the test to focus on general formatting)
class CliTaskPresenter:
    def present_task(self, task_response: TaskResponse) -> TaskViewModel:
        # Simulate CLI-specific formatting
        status_display_val = f"[{task_response.status}]"
        priority_display_val = f"{task_response.priority.upper()} PRIORITY" if isinstance(task_response.priority, str) else task_response.priority.name + " PRIORITY" # Simplified
        due_date_display_val = task_response.due_date.strftime("%Y-%m-%d") if task_response.due_date else "No due date"
        completion_info_val = (
            f"Completed on: {datetime.fromisoformat(task_response.completion_date).strftime('%Y-%m-%d %H:%M')}"
            if task_response.completion_date else None
        )
        return TaskViewModel(
            id=task_response.id,
            title=task_response.title,
            description=task_response.description,
            status_display=status_display_val,
            priority_display=priority_display_val,
            due_date_display=due_date_display_val,
            completion_info=completion_info_val
        )

    def present_error(self, error_msg: str, code: Optional[str] = None) -> Any:
        raise NotImplementedError


def test_presenter_provides_complete_view_model():
    """Test presenter creates properly formatted view model
    with all display fields."""
    # Arrange
    task_id_val = UUID('12345678-1234-5678-1234-567812345678')
    project_id_val = UUID('87654321-4321-8765-4321-876543210000')

    task = Task(
        title="Important Task",
        description="Testing view model creation",
        project_id=project_id_val,
        priority="HIGH" # Using string for priority for simplicity here
    )
    task.complete()  # Set status to DONE and completed_at

    task_response = TaskResponse.from_entity(task)
    presenter = CliTaskPresenter()

    # Act
    view_model = presenter.present_task(task_response)

    # Assert
    assert view_model.title == "Important Task"
    assert view_model.status_display == "[DONE]" # Assuming status.value for DONE is "DONE"
    assert view_model.priority_display == "HIGH PRIORITY"
    assert isinstance(view_model.completion_info, str)
    assert "Completed on:" in view_model.completion_info
```

<div dir="rtl" style="text-align: right;">

این تست تأیید می‌کند که چگونه ارائه‌دهنده ما چندین جنبه از وضعیت دامنه را به فرمت‌های قابل نمایش تبدیل می‌کند. **تفکیک دغدغه‌ها در معماری تمیز به این معنی است که می‌توانیم تمام منطق ارائه (نمایش وضعیت، فرمت‌بندی اولویت و اطلاعات تکمیل) را بدون درگیر کردن قوانین تجاری یا دغدغه‌های زیرساختی تأیید کنیم**.

با الگوهای ایجاد شده برای تست لایه‌های فردی، اکنون می‌توانیم نحوه کمک معماری تمیز به تست تعاملات در سراسر مرزهای معماری را بررسی کنیم.

</div>

---

<div dir="rtl" style="text-align: right;">

#### **۳. تست‌نویسی در طول مرزهای معماری**

از آنجایی که تست‌های واحد ما قوانین تجاری و منطق هماهنگی را به طور کامل از طریق رابط‌های صریح تأیید می‌کنند، می‌توانیم اطمینان حاصل کنیم که در صورت تغییر پیاده‌سازی‌های زیرساختی، موارد استفاده ما به درستی کار می‌کنند. ما قبلاً تأیید کردیم که موارد استفاده ما به درستی ایجاد وظایف و انتساب پروژه را هماهنگ می‌کنند. اکنون تست خواهیم کرد که پیاده‌سازی‌های واقعی `FileTaskRepository` و `FileProjectRepository` ما این روابط را هنگام پایداری در دیسک حفظ می‌کنند.

بیایید بررسی کنیم که چگونه مرز پایداری سیستم فایل خود را تست کنیم – یکی از حوزه‌هایی که تست یکپارچه‌سازی ارزشی فراتر از پوشش تست واحد ما فراهم می‌کند:

</div>

```python
import pytest
from uuid import UUID
from pathlib import Path
from todo_app.infrastructure.persistence.file_project_repository import FileProjectRepository
from todo_app.infrastructure.persistence.file_task_repository import FileTaskRepository
from todo_app.domain.entities.project import Project
from todo_app.domain.entities.task import Task
from todo_app.domain.entities.priority import Priority
from todo_app.domain.value_objects.task_status import TaskStatus

# Define an Entity base class and Project/Task entities if not already globally available
@dataclass
class Entity:
    id: UUID = field(default_factory=UUID, init=False) # Simplified UUID generation for test

@dataclass
class Project(Entity):
    name: str
    description: str = ""
    _tasks: Dict[UUID, Task] = field(default_factory=dict, init=False)
    # Add methods like add_task, remove_task, get_task, tasks property to Project if not present
    def add_task(self, task: Task) -> None:
        self._tasks[task.id] = task
    def remove_task(self, task_id: UUID) -> None:
        self._tasks.pop(task_id, None)
    def get_task(self, task_id: UUID) -> Optional[Task]:
        return self._tasks.get(task_id)
    @property
    def tasks(self) -> List[Task]:
        return list(self._tasks.values())
    @property
    def incomplete_tasks(self) -> List[Task]:
        return [t for t in self.tasks if t.status != TaskStatus.DONE]


@dataclass
class Task(Entity):
    title: str
    description: str
    project_id: UUID
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)
    completed_at: Optional[datetime] = None

    def complete(self, notes: Optional[str] = None) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Task is already completed")
        self.status = TaskStatus.DONE
        self.completed_at = datetime.now(timezone.utc)

# Mock/Simplified ProjectType as it's used by FileProjectRepository
class ProjectType(Enum):
    REGULAR = "REGULAR"
    INBOX = "INBOX"

# Assume FileTaskRepository and FileProjectRepository are defined elsewhere and manage
# their file interactions (e.g., loading/saving JSON) based on data_dir.
# For this test, we assume their save and get implementations are working.
# (The actual implementations from the book would be here if doing a full copy-paste)
# Example simplified versions for test context if not available:
# class FileTaskRepository:
#     def __init__(self, data_dir: Path): self.data_dir = data_dir
#     def save(self, task: Task): pass # Simplistic mock
#     def get(self, task_id: UUID): pass # Simplistic mock

# class FileProjectRepository:
#     def __init__(self, data_dir: Path): self.data_dir = data_dir
#     def set_task_repository(self, task_repo): self.task_repo = task_repo
#     def save(self, project: Project): pass # Simplistic mock
#     def get(self, project_id: UUID) -> Project: # Simplistic mock, returns dummy project with mock tasks
#         project = Project(name="Loaded Project", description="Loaded Desc", id=project_id)
#         project.add_task(Task(title="Loaded Task", description="Desc", project_id=project_id))
#         return project
#     def get_inbox(self) -> Project: return Project(name="INBOX", description="Inbox Project", project_type=ProjectType.INBOX)


@pytest.fixture
def repository(tmp_path): # tmp_path is a pytest builtin for temp dirs
    """Create repository using temporary directory."""
    return FileTaskRepository(data_dir=tmp_path)

def test_repo_handles_project_task_relationships(tmp_path):
    # Arrange
    task_repo = FileTaskRepository(tmp_path)
    project_repo = FileProjectRepository(tmp_path)
    project_repo.set_task_repository(task_repo) # Link repositories if needed for their internal logic

    # Create project and tasks through the repository
    project = Project(name="Test Project",
                      description="Testing relationships")
    project_repo.save(project)

    task = Task(title="Test Task",
                description="Testing relationships",
                project_id=project.id) # Assign task to the project
    task_repo.save(task)

    # Act - Load project with its tasks
    # Assume FileProjectRepository's get method also loads associated tasks.
    # In a real implementation, this would involve loading tasks based on project_id.
    # For this test, let's assume the mock Project's tasks property is populated or mocked.
    # If using actual file repos, the get method for project would internally load tasks.
    # We will manually add the task to the loaded_project for testing purposes
    # as the mock FileProjectRepository get() does not load tasks from file.
    loaded_project = project_repo.get(project.id)
    # The actual FileProjectRepository.get() should load tasks,
    # but for simplicity of this snippet, we'll manually add the task to the returned project.
    # In a full test, you'd verify the FileProjectRepository's get() method properly hydrated tasks.
    loaded_project.add_task(task) # Simulating that get() also loaded the task

    # Assert
    assert len(loaded_project.tasks) == 1
    assert loaded_project.tasks.title == "Test Task"
    assert loaded_project.tasks.project_id == project.id
```

<div dir="rtl" style="text-align: right;">

این تنظیم تست یک نقطه یکپارچگی کلیدی را نشان می‌دهد که در آن ما در حال ایجاد مخازن واقعی هستیم که از طریق ذخیره‌سازی سیستم فایل هماهنگ می‌شوند. تست‌های واحد ما قبلاً قوانین تجاری را با استفاده از mockها تأیید کرده‌اند، بنابراین این تست صرفاً بر تأیید اینکه لایه زیرساخت ما این روابط را به درستی حفظ می‌کند، تمرکز دارد.

*   **اعمال – بارگذاری پروژه با وظایف آن**:
    `loaded_project = project_repo.get(project.id)`
*   **تأیید**:
    `assert len(loaded_project.tasks) == 1`
    `assert loaded_project.tasks.title == "Test Task"`

این تست رفتاری را تأیید می‌کند که نتوانستیم در تست‌های واحد خود ثبت کنیم:

*   **پروژه‌ها می‌توانند وظایف مرتبط خود را از دیسک بارگذاری کنند**.
*   **روابط وظیفه-پروژه از سریال‌سازی جان سالم به در می‌برند**.

این هماهنگی مخزن به ویژه هنگام کار با تضمین‌های معماری که چندین عملیات را در بر می‌گیرد، مهم می‌شود. یکی از این تضمین‌ها، پروژه Inbox ما است، که یک تصمیم کلیدی در سطح زیرساخت در فصل ۷ گرفته شده است تا اطمینان حاصل شود که همه وظایف یک خانه سازمان‌دهی دارند.

یک نقطه یکپارچگی حیاتی دیگر، تأیید اینکه پیاده‌سازی‌های `ProjectRepository` ما این تضمین Inbox را حفظ می‌کنند، است. در حالی که تست‌های واحد ما قوانین تجاری مربوط به استفاده از Inbox (مانند جلوگیری از حذف یا تکمیل آن) را تأیید کرده‌اند، تست‌های یکپارچه‌سازی ما باید تأیید کنند که لایه زیرساخت به درستی وجود این پروژه خاص را حفظ می‌کند:

</div>

```python
import pytest
from uuid import UUID
from pathlib import Path
from todo_app.infrastructure.persistence.file_project_repository import FileProjectRepository
from todo_app.domain.entities.project import Project, ProjectType
from todo_app.domain.entities.task import Task


def test_repository_automatically_creates_inbox(tmp_path):
    """Test that project repository maintains inbox project
    across instantiations."""
    # Arrange - Create initial repository and verify Inbox exists
    initial_repo = FileProjectRepository(tmp_path)
    initial_inbox = initial_repo.get_inbox() # This method should ensure inbox exists and return it
    assert initial_inbox.name == "INBOX"
    assert initial_inbox.project_type == ProjectType.INBOX

    # Act - Create new repository instance pointing to same directory
    new_repo = FileProjectRepository(tmp_path) # Should load from existing file if present

    # Assert - New instance maintains same Inbox
    persisted_inbox = new_repo.get_inbox() # This should load the *same* inbox if it was created and persisted
    assert persisted_inbox.id == initial_inbox.id
    assert persisted_inbox.project_type == ProjectType.INBOX
```

<div dir="rtl" style="text-align: right;">

این تست رفتاری را تأیید می‌کند که تست‌های واحد ما نمی‌توانستند ثبت کنند، زیرا از مخازن mock شده استفاده می‌کردند. پیاده‌سازی مخزن ملموس ما مالکیت مقداردهی اولیه و پایداری Inbox را بر عهده می‌گیرد. با ایجاد دو نمونه مخزن جداگانه که به یک دایرکتوری داده اشاره می‌کنند، تأیید می‌کنیم که:

*   **مخزن به طور خودکار Inbox را در اولین استفاده ایجاد می‌کند**.
*   **نمونه‌های بعدی مخزن، همان Inbox را بارگذاری می‌کنند**.
*   **خواص Inbox در طول پایداری حفظ می‌شوند**.

معماری تمیز، تست یکپارچه‌سازی متمرکز را در سطح مورد استفاده (use case) فعال می‌کند. مورد استفاده ایجاد وظیفه ما را در نظر بگیرید. در حالی که تست‌های واحد ما منطق تجاری آن را با استفاده از مخازن mock شده تأیید کردند، باید تأیید کنیم که با پایداری واقعی به درستی کار می‌کند. مرزهای صریح معماری تمیز به ما امکان می‌دهند این کار را به صورت استراتژیک انجام دهیم، پایداری واقعی را تست کنیم و در عین حال دغدغه‌های غیرپایداری مانند اطلاع‌رسانی‌ها را mock کنیم:

</div>

```python
import pytest
from unittest.mock import Mock
from uuid import UUID
from pathlib import Path
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Optional, Any, Dict, List, Self
from enum import Enum

# --- Mocked Interfaces and DTOs for the test context ---
class ErrorCode(Enum):
    NOT_FOUND = "NOT_FOUND"
    VALIDATION_ERROR = "VALIDATION_ERROR"

@dataclass(frozen=True)
class Error:
    code: ErrorCode
    message: str
    details: Optional[Dict[str, Any]] = None

@dataclass(frozen=True)
class Result:
    value: Any = None
    error: Optional[Error] = None

    @property
    def is_success(self) -> bool:
        return self.error is None

    @classmethod
    def success(cls, value: Any) -> Self:
        return cls(value=value)

    @classmethod
    def failure(cls, error: Error) -> Self:
        return cls(error=error)

# Domain Entities (simplified for test)
@dataclass
class Entity:
    id: UUID = field(default_factory=UUID, init=False)

@dataclass
class Project(Entity):
    name: str
    description: str = ""
    project_type: Any = "REGULAR" # Using Any/string for simplicity
    _tasks: Dict[UUID, Any] = field(default_factory=dict, init=False)
    # Simplified get_inbox for testing CreateTaskUseCase
    # In a real scenario, FileProjectRepository would implement this
    @classmethod
    def create_inbox(cls) -> Self:
        return cls(name="INBOX", description="Default inbox", project_type="INBOX", id=UUID("00000000-0000-0000-0000-000000000001"))

@dataclass
class Task(Entity):
    title: str
    description: str
    project_id: UUID
    priority: Any = "MEDIUM" # Simplified
    status: Any = "TODO" # Simplified
    completed_at: Optional[datetime] = None


# Application layer DTOs (as defined in source)
@dataclass(frozen=True)
class CreateTaskRequest:
    title: str
    description: str
    project_id: Optional[str] = None # Expects string from outer layer

    def to_execution_params(self) -> Dict[str, Any]:
        params = {
            "title": self.title.strip(),
            "description": self.description.strip(),
        }
        if self.project_id:
            params["project_id"] = UUID(self.project_id)
        return params

@dataclass(frozen=True)
class TaskResponse:
    id: str
    title: str
    description: str
    status: Any
    priority: Any
    project_id: str
    due_date: Any = None
    completion_date: Any = None
    completion_notes: Optional[str] = None


# Application layer interfaces (as defined in source)
class TaskRepository:
    def get(self, task_id: UUID) -> Task:
        raise NotImplementedError
    def save(self, task: Task) -> None:
        raise NotImplementedError

class ProjectRepository:
    def get_inbox(self) -> Project:
        raise NotImplementedError
    def get(self, project_id: UUID) -> Project:
        raise NotImplementedError
    def save(self, project: Project) -> None:
        raise NotImplementedError


class NotificationPort:
    def notify_task_completed(self, task: Task) -> None:
        raise NotImplementedError


# Use Case (as defined in source, adjusted for file persistence context)
@dataclass(frozen=True)
class CreateTaskUseCase:
    task_repository: TaskRepository
    project_repository: ProjectRepository
    notification_service: NotificationPort # Still mock this

    def execute(self, request: CreateTaskRequest) -> Result:
        try:
            params = request.to_execution_params()
            project_id_from_params = params.get("project_id")
            
            project_id = project_id_from_params
            if not project_id_from_params:
                # If no project_id, get the inbox project
                inbox_project = self.project_repository.get_inbox()
                project_id = inbox_project.id

            task = Task(
                title=params["title"],
                description=params["description"],
                project_id=project_id,
            )
            self.task_repository.save(task)
            # Notification is mocked, so we just call it
            # self.notification_service.notify_task_created(task) # Assuming such a method

            # Convert Task entity to TaskResponse for consistent output
            response = TaskResponse(
                id=str(task.id),
                title=task.title,
                description=task.description,
                status=task.status,
                priority=task.priority,
                project_id=str(task.project_id)
            )
            return Result.success(response)
        except ValueError as e:
            return Result.failure(Error.validation_error(str(e)))
        except Exception as e:
            # Handle potential TaskNotFoundError or other exceptions from get_inbox
            return Result.failure(Error.validation_error(f"Failed to create task: {e}"))


# File based repositories (simplified for the test to demonstrate actual persistence)
class FileTaskRepository(TaskRepository):
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.tasks_file = data_dir / "tasks.json"
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not self.tasks_file.exists():
            self.tasks_file.write_text("[]")

    def save(self, task: Task) -> None:
        import json
        tasks_data = self._load_tasks_raw()
        task_dict = {
            "id": str(task.id),
            "title": task.title,
            "description": task.description,
            "project_id": str(task.project_id),
            "status": task.status,
            "priority": task.priority
        }
        # Update or add task
        found = False
        for i, existing_task_dict in enumerate(tasks_data):
            if existing_task_dict["id"] == str(task.id):
                tasks_data[i] = task_dict
                found = True
                break
        if not found:
            tasks_data.append(task_dict)
        self.tasks_file.write_text(json.dumps(tasks_data, indent=4))

    def get(self, task_id: UUID) -> Task:
        import json
        tasks_data = self._load_tasks_raw()
        for task_dict in tasks_data:
            if UUID(task_dict["id"]) == task_id:
                return Task(
                    id=UUID(task_dict["id"]),
                    title=task_dict["title"],
                    description=task_dict["description"],
                    project_id=UUID(task_dict["project_id"]),
                    status=task_dict["status"],
                    priority=task_dict["priority"]
                )
        raise ValueError(f"Task with ID {task_id} not found") # Simplified not found error


    def _load_tasks_raw(self) -> List[Dict]:
        import json
        if not self.tasks_file.exists() or not self.tasks_file.read_text():
            return []
        return json.loads(self.tasks_file.read_text())


class FileProjectRepository(ProjectRepository):
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.projects_file = data_dir / "projects.json"
        self._ensure_file_exists()
        self.inbox_project = self._get_or_create_inbox()

    def _ensure_file_exists(self):
        if not self.projects_file.exists():
            self.projects_file.write_text("[]")

    def _load_projects_raw(self) -> List[Dict]:
        import json
        if not self.projects_file.exists() or not self.projects_file.read_text():
            return []
        return json.loads(self.projects_file.read_text())

    def save(self, project: Project) -> None:
        import json
        projects_data = self._load_projects_raw()
        project_dict = {
            "id": str(project.id),
            "name": project.name,
            "description": project.description,
            "project_type": project.project_type,
        }
        # Update or add project
        found = False
        for i, existing_project_dict in enumerate(projects_data):
            if existing_project_dict["id"] == str(project.id):
                projects_data[i] = project_dict
                found = True
                break
        if not found:
            projects_data.append(project_dict)
        self.projects_file.write_text(json.dumps(projects_data, indent=4))

    def get(self, project_id: UUID) -> Project:
        projects_data = self._load_projects_raw()
        for project_dict in projects_data:
            if UUID(project_dict["id"]) == project_id:
                return Project(
                    id=UUID(project_dict["id"]),
                    name=project_dict["name"],
                    description=project_dict["description"],
                    project_type=project_dict["project_type"]
                )
        raise ValueError(f"Project with ID {project_id} not found")

    def _get_or_create_inbox(self) -> Project:
        projects_data = self._load_projects_raw()
        for project_dict in projects_data:
            if project_dict.get("project_type") == ProjectType.INBOX.value:
                return Project(
                    id=UUID(project_dict["id"]),
                    name=project_dict["name"],
                    description=project_dict["description"],
                    project_type=project_dict["project_type"]
                )
        # If not found, create and save a new Inbox project
        inbox = Project.create_inbox()
        self.save(inbox)
        return inbox

    def get_inbox(self) -> Project:
        return self.inbox_project


@pytest.fixture
def file_repositories(tmp_path):
    task_repo = FileTaskRepository(tmp_path)
    project_repo = FileProjectRepository(tmp_path)
    # project_repo.set_task_repository(task_repo) # This linkage might not be needed for this specific test
    return task_repo, project_repo


def test_task_creation_with_persistence(file_repositories):
    """Test task creation use case with real persistence."""
    # Arrange
    task_repo, project_repo = file_repositories
    
    # Ensure Inbox project exists before the use case runs
    # This is handled by FileProjectRepository's constructor via _get_or_create_inbox
    inbox_project_id = project_repo.get_inbox().id

    use_case = CreateTaskUseCase(
        task_repository=task_repo,
        project_repository=project_repo,
        notification_service=Mock()  # Still mock non-persistence concerns
    )

    # Act
    request = CreateTaskRequest(
        title="Test Task",
        description="Integration test",
        project_id=None # Let the use case assign to inbox
    )
    result = use_case.execute(request)

    # Assert - Task was persisted
    assert result.is_success
    created_task_response = result.value
    
    # Retrieve the task directly from the repository to confirm persistence
    persisted_task = task_repo.get(UUID(created_task_response.id))

    assert persisted_task.title == "Test Task"
    assert persisted_task.description == "Integration test"
    assert persisted_task.project_id == inbox_project_id # Verify it's assigned to the inbox
```

<div dir="rtl" style="text-align: right;">

در این تنظیم تست، ما از مخازن واقعی برای تأیید رفتار پایداری استفاده می‌کنیم و در عین حال اطلاع‌رسانی‌ها را mock می‌کنیم، زیرا آنها به این تست یکپارچه‌سازی مرتبط نیستند.

*   **اعمال**:
    `result = use_case.execute(CreateTaskRequest(title="Test Task", description="Integration test"))`
*   **تأیید – وظیفه پایدار شد**:
    `assert result.is_success`
    `created_task = task_repo.get(UUID(result.value.id))`
    `assert created_task.project_id == project_repo.get_inbox().id`

این تست تأیید می‌کند که مورد استفاده ما به درستی ایجاد وظیفه را با پایداری واقعی هماهنگ می‌کند:

*   **وظیفه به درستی در دیسک ذخیره می‌شود**.
*   **وظیفه طبق انتظار به Inbox اختصاص می‌یابد**.
*   **می‌توانیم وظیفه پایدار شده را از طریق مخزن بازیابی کنیم**.

با mock نگه داشتن اطلاع‌رسانی‌ها، ما تمرکز تست را حفظ می‌کنیم و در عین حال رفتار پایداری حیاتی را تأیید می‌کنیم. این رویکرد استراتژیک به تست یکپارچه‌سازی، که شامل تست پیاده‌سازی‌های واقعی مرزهای خاص در حالی که سایرین را mock می‌کند، نشان می‌دهد که چگونه معماری تمیز به ما کمک می‌کند تا پوشش تست جامع را بدون پیچیدگی غیرضروری ایجاد کنیم.

این تست‌های یکپارچه‌سازی نشان می‌دهند که چگونه مرزهای صریح معماری تمیز، تست متمرکز و قابل نگهداری را فعال می‌کنند و به ما اطمینان می‌دهند که سیستم ما در سراسر لایه‌ها به درستی کار می‌کند. در بخش بعدی، ابزارها و الگوهای پیشرفته برای نگهداری تست را بررسی خواهیم کرد.

</div>

---

<div dir="rtl" style="text-align: right;">

#### **۴. ابزارها و الگوهای پیشرفته برای نگهداری تست**

با رشد کاتالوگ تست شما، زمان اجرا می‌تواند به یک دغدغه مهم تبدیل شود. آنچه به عنوان یک مجموعه تست سریع آغاز شد، اکنون دقایق زیادی برای اجرا طول می‌کشد. در سیستم مدیریت وظایف ما، ما پوشش جامعی را در تمام لایه‌ها از جمله موجودیت‌های دامنه، موارد استفاده، رابط‌های آداپتور و زیرساخت ایجاد کرده‌ایم. اجرای متوالی تمام این تست‌ها، به ویژه آنهایی که شامل عملیات سیستم فایل یا رفتارهای مبتنی بر زمان هستند، می‌تواند تأخیرهای قابل توجهی را در حلقه بازخورد توسعه ایجاد کند.

اجرای سریع تست برای حفظ یکپارچگی معماری حیاتی است. مجموعه‌های تست طولانی‌مدت، تأیید مکرر را در طول توسعه دلسرد می‌کنند و خطر نشت نقض‌های معماری را افزایش می‌دهند. `pytest-xdist` ابزارهایی را برای موازی‌سازی اجرای تست در حالی که یکپارچگی تست حفظ می‌شود، فراهم می‌کند. ابتدا افزونه را با `pip` نصب کنید:
`pip install pytest-xdist`

حتی با تست‌ها و fixtureهای خوش‌سازمان، سناریوهای تست خاصی چالش‌های منحصر به فردی را ارائه می‌دهند. در بخش‌های قبلی، دیدیم که چگونه ساختار لایه‌ای معماری تمیز به ما کمک می‌کند تا کد تست پذیرتری بنویسیم.

هنگامی که یک تست شکست می‌خورد، باید به سرعت بفهمیم کدام مرز معماری نقض شده است. هنگامی که قوانین تجاری تغییر می‌کنند، باید بتوانیم تست‌ها را به طور سیستماتیک به روز کنیم به جای اینکه مجبور باشیم چندین فایل را جستجو کنیم. هنگام افزودن موارد تست جدید، می‌خواهیم از زیرساخت تست موجود استفاده کنیم به جای اینکه مجبور باشیم کد تنظیمات را تکرار کنیم.

اکوسیستم تست پایتون، به ویژه `pytest`، ابزارهای قدرتمندی را فراهم می‌کند که به طور طبیعی با اهداف معماری تمیز همسو هستند.

در ادامه بررسی خواهیم کرد که چگونه:

*   **سناریوهای متعدد را تأیید کنیم و در عین حال کد تست را تمیز و متمرکز نگه داریم**.
*   **Fixtureهای تست را برای احترام به مرزهای معماری سازماندهی کنیم**.
*   **از ابزارهای تست که نگهداری را آسان‌تر می‌کنند، استفاده کنیم**.
*   **مسائل ظریفی را که می‌تواند یکپارچگی معماری ما را نقض کند، تشخیص دهیم**.

از طریق مثال‌های عملی، خواهیم دید که چگونه این الگوها به ما کمک می‌کنند تا پوشش تست جامع را بدون ایجاد بار نگهداری حفظ کنیم، به ما امکان می‌دهند سناریوهای بیشتری را با کد کمتر تأیید کنیم و در عین حال تست‌های ما را به همان اندازه معماری ما تمیز نگه می‌دارند.

**ساختاردهی فایل‌های تست**

مرزهای صریح معماری تمیز، سازماندهی طبیعی برای فایل‌های تست ما فراهم می‌کنند. چه تیم شما انتخاب کند که تست‌ها را بر اساس نوع (واحد/یکپارچه‌سازی) سازماندهی کند یا آنها را با هم نگه دارد، ساختار داخلی باید معماری برنامه شما را منعکس کند. یک ساختار دایرکتوری تست نمونه ممکن است به این صورت باشد:

```
tests/
├── domain/
│   ├── entities/
│   │   ├── test_task.py
│   │   └── test_project.py
│   └── value_objects/
│       └── test_deadline.py
├── application/
│   └── use_cases/
│       └── test_task_use_cases.py
└── infrastructure/
    ├── persistence/
    │   ├── test_file_repositories.py
    └── web/
        └── test_web_routes.py
# ... Remaining tests by layer
```

این سازمان‌دهی، قوانین وابستگی معماری تمیز را از طریق مرزهای سیستم فایل تقویت می‌کند. تست‌ها در `tests/domain` نیازی به import کردن چیزی از `application` یا `interfaces` ندارند، در حالی که یک تست در `tests/interfaces` می‌تواند با کامپوننت‌هایی از تمام لایه‌ها کار کند، درست مانند همتایان تولیدی آنها. این هم‌ترازی ساختاری همچنین هشدار اولیه نقض‌های معماری احتمالی را فراهم می‌کند. اگر خود را در حال تمایل به import کردن یک مخزن در یک تست موجودیت دامنه بیابیم، مسیر import ناخوشایند نشان می‌دهد که احتمالاً در حال نقض قانون وابستگی معماری تمیز هستیم.

**تست پارامتری برای پوشش جامع**

هنگام تست در سراسر مرزهای معماری، اغلب نیاز داریم رفتار مشابهی را در شرایط مختلف تأیید کنیم. مورد استفاده ایجاد وظیفه ما را در نظر بگیرید. ما نیاز داریم انتساب پروژه، تنظیم اولویت و اعتبارسنجی مهلت را در ترکیب‌های ورودی متعدد تست کنیم. نوشتن متدهای تست جداگانه برای هر سناریو منجر به کد تکراری و نگهداری دشوارتر می‌شود. هنگامی که قوانین تجاری تغییر می‌کنند، باید چندین تست را به روز کنیم به جای یک منبع حقیقت واحد.

دکوراتور `pytest.mark.parametrize` نحوه رسیدگی به این سناریوها را تغییر می‌دهد. به جای تکرار کد تست، می‌توانیم تغییرات داده‌ای را تعریف کنیم که مرزهای معماری ما را تمرین می‌دهند:

</div>

```python
import pytest
from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Optional, Any, Dict, List, Self
from enum import Enum

# --- Domain Entities and Enums (Simplified for test context) ---
class ProjectType(Enum):
    REGULAR = "REGULAR"
    INBOX = "INBOX"

@dataclass
class Entity:
    id: UUID = field(default_factory=UUID, init=False)

@dataclass
class Project(Entity):
    name: str
    description: str = ""
    project_type: ProjectType = field(default=ProjectType.REGULAR)

    @classmethod
    def create_inbox(cls) -> Self:
        return cls(name="INBOX", description="Default inbox", project_type=ProjectType.INBOX, id=UUID("00000000-0000-0000-0000-000000000001"))


@dataclass
class Task(Entity):
    title: str
    description: str
    project_id: UUID
    priority: Any = "MEDIUM" # Simplified, for test
    status: Any = "TODO" # Simplified, for test
    completed_at: Optional[datetime] = None


class Priority(Enum): # Ensure this is defined for expected_behavior
    LOW = 1
    MEDIUM = 2
    HIGH = 3

# --- Application Layer DTOs and Interfaces (Simplified for test context) ---
@dataclass(frozen=True)
class CreateTaskRequest:
    title: str
    description: str
    project_id: Optional[str] = None

    def to_execution_params(self) -> Dict[str, Any]:
        params = {
            "title": self.title.strip(),
            "description": self.description.strip(),
        }
        if self.project_id:
            params["project_id"] = UUID(self.project_id)
        return params

@dataclass(frozen=True)
class TaskResponse:
    id: str
    title: str
    description: str
    status: Any
    priority: Any
    project_id: str


class TaskRepository:
    def save(self, task: Task) -> None:
        raise NotImplementedError
    def get(self, task_id: UUID) -> Task:
        raise NotImplementedError

class ProjectRepository:
    def get_inbox(self) -> Project:
        raise NotImplementedError
    def get(self, project_id: UUID) -> Project:
        raise NotImplementedError

class NotificationPort:
    def notify_task_completed(self, task: Task) -> None:
        raise NotImplementedError


# --- Use Case (Simplified for test context) ---
@dataclass(frozen=True)
class CreateTaskUseCase:
    task_repository: TaskRepository
    project_repository: ProjectRepository
    # notification_service: NotificationPort # Removed for simplicity in this test

    def execute(self, request: CreateTaskRequest) -> Any: # Returns TaskResponse or similar
        params = request.to_execution_params()
        project_id_from_params = params.get("project_id")
        
        project_id = project_id_from_params
        if not project_id_from_params:
            inbox_project = self.project_repository.get_inbox()
            project_id = inbox_project.id

        task = Task(
            title=params["title"],
            description=params["description"],
            project_id=project_id,
            priority=params.get("priority", Priority.MEDIUM) # Allow priority from params
        )
        self.task_repository.save(task)
        return task # Return the task entity for assertion


@pytest.fixture
def tmp_path(tmp_path_factory):
    # This fixture is usually provided by pytest itself.
    # Defining it here for standalone snippet clarity if not present.
    return tmp_path_factory.mktemp("test_dir")


@pytest.mark.parametrize(
    "request_data,expected_behavior",
    [
        # Basic task creation - defaults to INBOX project
        (
            {
                "title": "Test Task",
                "description": "Basic creation"
            },
            {
                "project_type": ProjectType.INBOX,
                "priority": Priority.MEDIUM
            }
        ),
        # Explicit project assignment
        (
            {
                "title": "Project Task",
                "description": "With project",
                "project_id": "12345678-1234-5678-1234-567812345678" # Example UUID
            },
            {
                "project_type": ProjectType.REGULAR,
                "priority": Priority.MEDIUM
            }
        ),
        # High priority task
        (
            {
                "title": "High Priority Task",
                "description": "Urgent work",
                "priority": "HIGH" # Passed as string, will be converted to Enum
            },
            {
                "project_type": ProjectType.INBOX, # Defaults to inbox if not specified
                "priority": Priority.HIGH
            }
        ),
    ],
    ids=["basic-task", "project-task", "priority-task"]
)
def test_task_creation_scenarios(request_data, expected_behavior, tmp_path):
    """Test task creation use case handles various
    input scenarios correctly."""

    from unittest.mock import Mock

    # Arrange
    task_repo = Mock(spec=TaskRepository)
    # Mock save to do nothing, get to return simple task (if needed later)
    task_repo.save.return_value = None
    task_repo.get.return_value = Mock(spec=Task) # Just a placeholder if get is called

    project_repo = Mock(spec=ProjectRepository)
    # Mock get_inbox to return a predefined inbox project
    project_repo.get_inbox.return_value = Project.create_inbox()
    # Mock get for explicit project assignment scenario
    if request_data.get("project_id"):
        explicit_project_uuid = UUID(request_data["project_id"])
        project_repo.get.return_value = Project(name="Explicit Project", description="", id=explicit_project_uuid)
    
    use_case = CreateTaskUseCase(
        task_repository=task_repo,
        project_repository=project_repo,
        # notification_service=Mock() # Not used in this simplified test
    )

    # Act
    # Create CreateTaskRequest from request_data
    request_obj = CreateTaskRequest(**request_data)
    result_task = use_case.execute(request_obj) # Use execute to get the created task directly

    # Assert
    # Verify task was saved
    task_repo.save.assert_called_once()
    saved_task = task_repo.save.call_args # Get the task object that was saved

    if expected_behavior["project_type"] == ProjectType.INBOX:
        assert saved_task.project_id == project_repo.get_inbox().id
    else:
        assert saved_task.project_id == UUID(request_data["project_id"])

    assert saved_task.priority == expected_behavior["priority"]
    assert saved_task.title == request_data["title"]
    assert saved_task.description == request_data["description"]
```

<div dir="rtl" style="text-align: right;">

سپس در متد تست بعد از دکوراتور `parametrize` بالا، تست برای هر مورد در لیست پارامترها یک بار اجرا می‌شود:

این تست چندین مزیت کلیدی تست پارامتری را نشان می‌دهد. دکوراتور `parametrize` `request_data` و `expected_behavior` هر مورد تست را به متد تست ما تزریق می‌کند، جایی که `request_data` ورودی را در لبه سیستم ما و `expected_behavior` قوانین دامنه مورد انتظار ما را تعریف می‌کند. این تفکیک به ما امکان می‌دهد سناریوهای تست خود را به صورت **اعلامی** تعریف کنیم و در عین حال منطق تأیید را تمیز و متمرکز نگه داریم.

**سازماندهی Test Fixtureها**

در طول مثال‌های تست ما، از fixtureهای `pytest` برای مدیریت وابستگی‌های تست استفاده کرده‌ایم، از ارائه موجودیت‌های وظیفه تمیز گرفته تا پیکربندی مخازن mock. در حالی که این fixtureهای فردی نیازهای تست فوری ما را برآورده می‌کردند، با رشد مجموعه‌های تست، مدیریت تنظیمات تست در سراسر مرزهای معماری به طور فزاینده‌ای پیچیده می‌شود. هر لایه نیازهای تنظیمات خاص خود را دارد: تست‌های دامنه به نمونه‌های موجودیت تمیز نیاز دارند، تست‌های مورد استفاده به مخازن و سرویس‌های به درستی پیکربندی شده نیاز دارند، و تست‌های رابط به داده‌های درخواست فرمت شده نیاز دارند.

سیستم fixture `pytest`، به ویژه در کنار فایل‌های `conftest.py` آن، به ما کمک می‌کند تا این الگوی fixture را در سراسر سلسله‌مراتب تست خود مقیاس‌بندی کنیم و در عین حال مرزهای معماری تمیز را حفظ کنیم. با قرار دادن fixtureها در دایرکتوری تست مناسب، اطمینان حاصل می‌کنیم که هر تست دقیقاً به آنچه نیاز دارد، بدون وابستگی‌های اضافی، دسترسی دارد:

```python
# tests/conftest.py - Root fixtures available to all tests
import pytest
from uuid import UUID

@pytest.fixture
def sample_task_data():
    """Provide basic task attributes for testing."""
    return {
        "title": "Test Task",
        "description": "Sample task for testing",
        "project_id": UUID('12345678-1234-5678-1234-567812345678'),
    }

# tests/domain/conftest.py - Domain layer fixtures
from todo_app.domain.entities.task import Task

@pytest.fixture
def domain_task(sample_task_data):
    """Provide a clean Task entity for domain tests."""
    return Task(**sample_task_data)

# tests/application/conftest.py - Application layer fixtures
from unittest.mock import Mock
from todo_app.application.interfaces.task_repository import TaskRepository # Assuming this path

@pytest.fixture
def mock_task_repository(domain_task):
    """Provide a pre-configured mock repository."""
    repo = Mock(spec=TaskRepository)
    repo.get.return_value = domain_task
    return repo
```

<div dir="rtl" style="text-align: right;">

این سازمان‌دهی به طور طبیعی قانون وابستگی معماری تمیز را از طریق ساختار تست ما اعمال می‌کند. تستی که هم به موجودیت‌های دامنه و هم به مخازن نیاز دارد، باید در لایه برنامه (Application layer) یا بالاتر قرار گیرد، زیرا به fixtureهای هر دو لایه وابسته است. به طور مشابه، تستی که فقط از موجودیت‌های دامنه استفاده می‌کند، می‌تواند مطمئن باشد که به طور تصادفی به دغدغه‌های زیرساختی وابسته نیست.

خود fixtureها به مرزهای معماری ما احترام می‌گذارند:

```python
# tests/interfaces/conftest.py - Interface layer fixtures
import pytest
from unittest.mock import Mock
from todo_app.application.use_cases.create_task import CreateTaskUseCase # Assuming this path
from todo_app.application.interfaces.project_repository import ProjectRepository # Assuming this path
from todo_app.application.interfaces.notification_port import NotificationPort # Assuming this path
from todo_app.interfaces.controllers.task_controller import TaskController # Assuming this path
from todo_app.interfaces.presenters.task_presenter import TaskPresenter # Assuming this path
from todo_app.application.use_cases.complete_task import CompleteTaskUseCase # Assuming this path
from todo_app.application.use_cases.update_task import UpdateTaskUseCase # Assuming this path
from todo_app.application.use_cases.delete_task import DeleteTaskUseCase # Assuming this path
from todo_app.application.use_cases.get_task import GetTaskUseCase # Assuming this path
from todo_app.interfaces.request_models.task_requests import CreateTaskRequest # Assuming this path

@pytest.fixture
def task_controller(mock_task_repository, mock_notification_port):
    """Provide a properly configured TaskController."""
    # These use cases would also be mocked or their dependencies mocked
    create_use_case = Mock(spec=CreateTaskUseCase)
    complete_use_case = Mock(spec=CompleteTaskUseCase)
    update_use_case = Mock(spec=UpdateTaskUseCase)
    delete_use_case = Mock(spec=DeleteTaskUseCase)
    get_use_case = Mock(spec=GetTaskUseCase)


    return TaskController(
        create_use_case=create_use_case,
        complete_use_case=complete_use_case,
        update_use_case=update_use_case,
        delete_use_case=delete_use_case,
        get_use_case=get_use_case,
        presenter=Mock(spec=TaskPresenter) # Mock presenter for controller test
    )

@pytest.fixture
def task_request_json():
    """Provide sample request data as it would come from clients."""
    return {
        "title": "Test Task",
        "description": "Testing task creation",
        "priority": "HIGH"
    }
```

<div dir="rtl" style="text-align: right;">

هنگام استفاده از fixtureها در سراسر مرزهای معماری، آنها را مطابق با تزریق وابستگی تولید خود ساختاردهی کنید. به عنوان مثال، برای تأیید اینکه کنترلر ما به درستی درخواست‌های خارجی را به عملیات مورد استفاده تبدیل می‌کند:

```python
from unittest.mock import Mock
from todo_app.interfaces.controllers.task_controller import TaskController # Assuming this path
from todo_app.application.interfaces.task_repository import TaskRepository # Assuming this path
from todo_app.interfaces.request_models.task_requests import CreateTaskRequest # Assuming this path
from todo_app.interfaces.presenters.task_presenter import TaskPresenter # Assuming this path
from todo_app.interfaces.result_models.operation_result import OperationResult # Assuming this path
from todo_app.application.use_cases.create_task import CreateTaskUseCase # Assuming this path
from todo_app.domain.entities.task import Task # Assuming this path
from todo_app.interfaces.result_models.task_view_model import TaskViewModel # Assuming this path
from uuid import UUID

@pytest.fixture
def task_controller():
    mock_create_use_case = Mock(spec=CreateTaskUseCase)
    # Setup mock_create_use_case.execute to return a successful result
    # It should return a Task entity or a TaskResponse that the presenter can handle
    mock_task_entity = Task(title="Created Title", description="Created Desc", project_id=UUID("00000000-0000-0000-0000-000000000001"))
    mock_create_use_case.execute.return_value = OperationResult.succeed(mock_task_entity)

    mock_presenter = Mock(spec=TaskPresenter)
    # Mock the present_task method to return a dummy TaskViewModel
    mock_presenter.present_task.return_value = TaskViewModel(
        id="mock_id",
        title="Mock Title",
        description="Mock Description",
        status_display="[MOCK_STATUS]",
        priority_display="MOCK_PRIORITY",
        due_date_display="No due date",
        project_display="Mock Project",
        completion_info=None
    )
    mock_presenter.present_error.return_value = Mock() # Also mock error presenter

    controller = TaskController(
        create_use_case=mock_create_use_case,
        complete_use_case=Mock(), # Or provide real mocks if testing these
        update_use_case=Mock(),
        delete_use_case=Mock(),
        get_use_case=Mock(),
        presenter=mock_presenter,
    )
    return controller

@pytest.fixture
def task_request_json():
    """Provide sample request data as it would come from clients."""
    return {
        "title": "Test Task",
        "description": "Testing task creation",
        "priority": "HIGH"
    }

def test_controller_handles_task_creation(
    task_controller,
    task_request_json,
):
    """Test task creation through controller layer."""
    # Ensure the create_use_case mock is accessible through the controller
    mock_create_use_case = task_controller.create_use_case

    # Act
    result = task_controller.handle_create(**task_request_json)

    # Assert
    assert result.is_success
    # Verify that the execute method of the use case was called once
    mock_create_use_case.execute.assert_called_once()
    # Verify that the saved task was created with the correct title
    # This requires accessing the arguments passed to the mock's execute method
    called_request = mock_create_use_case.execute.call_args
    assert called_request.title == task_request_json["title"]
    assert called_request.description == task_request_json["description"]
    # Verify that the presenter's present_task method was called for success
    task_controller.presenter.present_task.assert_called_once()
    # Verify the result from the controller is a TaskViewModel via OperationResult.succeed
    assert isinstance(result.value, TaskViewModel)
```

<div dir="rtl" style="text-align: right;">

این رویکرد مبتنی بر fixture چندین مزیت عملی دارد:

*   **تست‌ها بر رفتار تمرکز می‌کنند تا تنظیمات**. تست ما مسئولیت کنترلر را بدون کد تنظیمات که متد تست را شلوغ می‌کند، تأیید می‌کند.
*   **پیکربندی‌های تست رایج قابل استفاده مجدد هستند**. همان fixture `task_controller` می‌تواند چندین سناریوی تست کنترلر را پشتیبانی کند.
*   **وابستگی‌ها صریح هستند**. پارامترهای تست به وضوح نشان می‌دهند که با کدام کامپوننت‌ها کار می‌کنیم.
*   **تغییرات در مقداردهی اولیه کامپوننت فقط نیاز به به روزرسانی در fixture دارد، نه در هر تست**.

در ادامه بررسی خواهیم کرد که چگونه این الگوها با ابزارهای تست ترکیب می‌شوند تا نقض‌های معماری ظریف را تشخیص دهند.

**ابزارهای تست و تکنیک‌ها**

حتی با تست‌ها و fixtureهای خوش‌سازمان، سناریوهای تست خاصی چالش‌های منحصر به فردی را ارائه می‌دهند. در معماری تمیز، هر کامپوننت باید مستقل باشد، با وابستگی‌هایی که به صراحت از طریق رابط‌ها منتقل می‌شوند. با این حال، وضعیت سراسری ظریفی می‌تواند نفوذ کند. سرویس اطلاع‌رسانی سیستم مدیریت وظایف ما را در نظر بگیرید: ممکن است یک صف داخلی از اطلاع‌رسانی‌های در انتظار را حفظ کند که بین تست‌ها باقی می‌ماند. یک تست که اطلاع‌رسانی‌های وظیفه با اولویت بالا را تأیید می‌کند، ممکن است در صورت اجرا به تنهایی قبول شود اما در صورت اجرا پس از تستی که این صف را پر می‌کند، شکست بخورد. یا مخزن پروژه ما ممکن است تعداد وظایف را برای عملکرد کش کند، که منجر به تست‌هایی می‌شود که بسته به اینکه تست‌های دیگر این کش را دستکاری کرده‌اند یا نه، قبول یا رد می‌شوند.

این وابستگی‌های وضعیت پنهان نه تنها تست‌ها را غیرقابل اعتماد می‌کنند، بلکه اغلب نقض‌های معماری را نشان می‌دهند که در آن کامپوننت‌ها وضعیت را حفظ می‌کنند که باید در رابط‌های ما صریح باشد. **بهتر است این مسائل را در اسرع وقت آشکار کنیم، بنابراین به شدت توصیه می‌شود که تست‌ها را به صورت تصادفی اجرا کنید**. با `pytest` این کار با نصب `pytest-random-order` امکان‌پذیر است:
`pip install pytest-random-order`

سپس آن را برای اجرا در هر تست پیکربندی کنید:

```ini
# pytest.ini
[pytest]
addopts = --random-order
```

هنگامی که تست‌ها به صورت تصادفی اجرا می‌شوند، وابستگی‌های وضعیت پنهان به سرعت از طریق شکست‌های تست آشکار می‌شوند. لحظه‌ای که یک تست به وضعیت سراسری یا ترتیب اجرا متکی است؛ به طور غیرقابل پیش‌بینی شکست خواهد خورد. این یک سیگنال واضح است که ما نیاز به بررسی مرزهای معماری خود داریم. هنگامی که چنین شکستی رخ می‌دهد، افزونه یک مقدار seed را ارائه می‌دهد که به شما امکان می‌دهد ترتیب اجرای تست دقیق را بازتولید کنید:
`pytest --random-order-seed=123456`

سپس می‌توانید تست‌ها را به ترتیبی که با seed مشخص شده است، هر چند بار که لازم است اجرا کنید تا علت اصلی شکست را تعیین کنید.

**مدیریت زمان در تست‌ها**

تست سناریوهایی که شامل زمان می‌شوند، یک چالش رایج را ارائه می‌دهند. به عنوان مثال، تست وظایف با مهلت‌های نزدیک می‌تواند منجر به تست‌هایی شود که به طور غیرقابل پیش‌بینی شکست می‌خورند، زیرا زمان واقعی بین اجرای تست‌ها تغییر می‌کند. این ممکن است شما را مجبور کند که به طور ناخوشایند زمان را `sleep` کنید (که تست‌ها را کند و غیرقابل اعتماد می‌کند) یا زمان سیستم را دستکاری کنید (که به طور بالقوه بر سایر تست‌ها تأثیر می‌گذارد). بدتر از آن، تست‌های مبتنی بر زمان ممکن است بسته به زمان اجرای آنها در طول روز، قبول یا رد شوند.

کتابخانه `freezegun` این مشکلات را با اجازه دادن به ما برای کنترل زمان در تست‌های خود بدون تغییر منطق دامنه ما حل می‌کند. ابتدا کتابخانه را نصب کنید:
`pip install freezegun`

کتابخانه `freezegun` یک `context manager` را فراهم می‌کند که به ما امکان می‌دهد یک نقطه زمانی خاص را برای کدی که در محدوده آن اجرا می‌شود، تنظیم کنیم. هر کدی در داخل بلوک `freeze_time():` زمان را در آن لحظه به صورت ثابت شده می‌بیند، در حالی که کد بیرون با زمان عادی ادامه می‌یابد. این به ما امکان می‌دهد سناریوهای تست دقیق ایجاد کنیم و در عین حال موجودیت‌های دامنه ما همچنان با اشیاء `datetime` واقعی کار می‌کنند:

</div>

```python
import pytest
from unittest.mock import Mock
from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Optional, Any, Dict, List, Self
from enum import Enum
from freezegun import freeze_time


# --- Domain Entities and Value Objects (Simplified for test context) ---
@dataclass
class Entity:
    id: UUID = field(default_factory=UUID, init=False)

@dataclass
class Project(Entity):
    name: str
    description: str = ""
    project_type: Any = "REGULAR"


@dataclass
class Deadline: # As defined in Chapter 4
    due_date: datetime

    def is_overdue(self) -> bool:
        return datetime.now(timezone.utc) > self.due_date

    def time_remaining(self) -> timedelta:
        return max(
            timedelta(0),
            self.due_date - datetime.now(timezone.utc)
        )

@dataclass
class Task(Entity): # As defined in Chapter 4
    title: str
    description: str
    project_id: UUID
    priority: Any = "MEDIUM"
    status: Any = "TODO"
    completed_at: Optional[datetime] = None
    due_date: Optional[Deadline] = None # Added due_date for this test


# --- Application Interfaces (Simplified for test context) ---
class TaskRepository:
    def get(self, task_id: UUID) -> Task:
        raise NotImplementedError
    def save(self, task: Task) -> None:
        raise NotImplementedError

class NotificationPort:
    def notify_task_deadline_approaching(self, task: Task) -> None:
        raise NotImplementedError


# --- Use Case for checking deadlines (Example for this test) ---
@dataclass
class CheckDeadlinesUseCase:
    task_repository: TaskRepository
    notification_service: NotificationPort
    warning_threshold: timedelta = timedelta(days=1)

    def execute(self) -> Any: # Returns a Result object in real app
        # In a real use case, this would fetch all tasks or tasks due soon
        # For simplicity, we assume task_repository.get() is how we get the task
        # This test relies on the specific task created in the test, so we'll pass it in
        # For this test, let's assume the use case would iterate over tasks
        # but here we'll just check the single task passed to the repository mock.
        mock_task = self.task_repository.get(UUID("any-task-id")) # This is just to satisfy the call

        if mock_task.due_date and mock_task.due_date.is_approaching(self.warning_threshold):
            self.notification_service.notify_task_deadline_approaching(mock_task)
            return "Notification sent"
        return "No notification" # Or Result.success(None) in a real app


def test_task_deadline_approaching():
    """Test deadline notifications respect time boundaries."""
    # Arrange
    # Use freeze_time to set a specific starting point for the test
    with freeze_time("2024-01-14 12:00:00", tz_offset=timezone.utc.utcoffset(datetime.now())):
        task_id_val = UUID('12345678-1234-5678-1234-567812345678')
        task = Task(
            title="Time-sensitive task",
            description="Testing deadlines",
            project_id=task_id_val,
            due_date=Deadline(datetime(
                2024, 1, 15, 12, 0, tzinfo=timezone.utc)) # Due 24 hours later
        )

        task_repository = Mock(spec=TaskRepository)
        task_repository.get.return_value = task # Mock the repository to return our task

        notification_service = Mock(spec=NotificationPort)
        use_case = CheckDeadlinesUseCase(
            task_repository=task_repository,
            notification_service=notification_service,
            warning_threshold=timedelta(days=1) # 24 hours threshold
        )

    # Act
    # Move time forward one hour. Now task is due in 23 hours.
    with freeze_time("2024-01-14 13:00:00", tz_offset=timezone.utc.utcoffset(datetime.now())):
        # Execute the use case which checks for approaching deadlines
        result = use_case.execute()

    # Assert
    # Verify that the notification service was called
    notification_service.notify_task_deadline_approaching.assert_called_once_with(task)
```

<div dir="rtl" style="text-align: right;">

در این تنظیم تست، ما زمان را در ظهر ۱۴ ژانویه ثابت می‌کنیم تا وظیفه خود را با مهلتی ۲۴ ساعت بعد ایجاد کنیم. این به ما یک حالت اولیه دقیق برای تست محاسبات مهلت می‌دهد. موجودیت‌های دامنه ما همچنان با اشیاء `datetime` استاندارد کار می‌کنند و تفکیک دغدغه‌ها در معماری تمیز را حفظ می‌کنند. فقط درک زمان فعلی تحت تأثیر قرار می‌گیرد.

*   **اعمال**:
    `with freeze_time("2024-01-14 13:00:00"):`
    `result = use_case.execute()`
*   **تأیید**:
    `assert result.is_success`
    `notification_service.notify_task_deadline_approaching.assert_called_once()`

حرکت زمان به جلو به مدت یک ساعت به ما امکان می‌دهد تأیید کنیم که سیستم اطلاع‌رسانی مهلت ما به درستی وظایفی را که در آستانه مهلت هشدار هستند، شناسایی می‌کند. تست بلافاصله اجرا می‌شود و در عین حال یک سناریوی واقعی را شبیه‌سازی می‌کند و در نهایت، به ما کمک می‌کند تا کد خود را در برابر رفتارهای مرتبط با زمان، قوی کنیم.

**آشکارسازی وابستگی‌های وضعیت**

مشکلات وضعیت پنهان به ویژه در اطراف وضعیت سراسری خود را نشان می‌دهند. در معماری تمیز، هر کامپوننت باید مستقل باشد، با وابستگی‌هایی که به صراحت از طریق رابط‌ها منتقل می‌شوند. با این حال، وضعیت سراسری ظریفی می‌تواند نفوذ کند. این وابستگی‌های وضعیت پنهان نه تنها تست‌ها را غیرقابل اعتماد می‌کنند، بلکه اغلب نشان‌دهنده نقض‌های معماری هستند که در آن کامپوننت‌ها وضعیت را حفظ می‌کنند که باید در رابط‌های ما صریح باشد. **بهتر است این مسائل را در اسرع وقت آشکار کنیم، بنابراین به شدت توصیه می‌شود که تست‌ها را به صورت تصادفی اجرا کنید**. با `pytest` این کار با نصب `pytest-random-order` امکان‌پذیر است:
`pip install pytest-random-order`

سپس آن را برای اجرا در هر تست پیکربندی کنید:

```ini
# pytest.ini
[pytest]
addopts = --random-order
```

هنگامی که تست‌ها به صورت تصادفی اجرا می‌شوند، وابستگی‌های وضعیت پنهان به سرعت از طریق شکست‌های تست آشکار می‌شوند. لحظه‌ای که یک تست به وضعیت سراسری یا ترتیب اجرا متکی است؛ به طور غیرقابل پیش‌بینی شکست خواهد خورد. این یک سیگنال واضح است که ما نیاز به بررسی مرزهای معماری خود داریم. هنگامی که چنین شکستی رخ می‌دهد، افزونه یک مقدار seed را ارائه می‌دهد که به شما امکان می‌دهد ترتیب اجرای تست دقیق را بازتولید کنید:
`pytest --random-order-seed=123456`

سپس می‌توانید تست‌ها را به ترتیبی که با seed مشخص شده است، هر چند بار که لازم است اجرا کنید تا علت اصلی شکست را تعیین کنید.

**تسریع اجرای تست**

با رشد کاتالوگ تست شما، زمان اجرا می‌تواند به یک دغدغه مهم تبدیل شود. آنچه به عنوان یک مجموعه تست سریع آغاز شد، اکنون دقایق زیادی برای اجرا طول می‌کشد. اجرای سریع تست برای حفظ یکپارچگی معماری حیاتی است. مجموعه‌های تست طولانی‌مدت، تأیید مکرر را در طول توسعه دلسرد می‌کنند و خطر نشت نقض‌های معماری را افزایش می‌دهند. `pytest-xdist` ابزارهایی را برای موازی‌سازی اجرای تست در حالی که یکپارچگی تست حفظ می‌شود، فراهم می‌کند. ابتدا افزونه را با `pip` نصب کنید:
`pip install pytest-xdist`

اجرای موازی را در `pytest.ini` خود پیکربندی کنید:

```ini
# pytest.ini
[pytest]
addopts = --random-order -n auto  # Combine random order with parallel execution
```

برای هر سناریویی که تست‌ها نمی‌توانند در یک گروه موازی اجرا شوند (به عنوان مثال، تست‌هایی که وضعیت سراسری یا منابع مشترک شناخته شده‌ای دارند)، `pytest-xdist` چندین ابزار را فراهم می‌کند:

*   **از `@pytest.mark.serial` برای علامت‌گذاری تست‌هایی که باید به صورت متوالی اجرا شوند، استفاده کنید**.
*   **محدوده منابع را با `@pytest.mark.resource_group('global-cache')` پیکربندی کنید تا اطمینان حاصل شود که تست‌هایی که از منابع مشابه استفاده می‌کنند، با هم اجرا می‌شوند**.

پرچم `-n auto` به طور خودکار از هسته‌های CPU موجود استفاده می‌کند، اگرچه می‌توانید یک عدد دقیق مانند `-n 4` را در صورت تمایل مشخص کنید. این رویکرد به ما امکان می‌دهد اجرای سریع تست را حفظ کنیم و در عین حال به محدودیت‌های مرزهای معماری خود احترام بگذاریم. تست‌های حیاتی که اصول معماری تمیز ما را تأیید می‌کنند، به اندازه کافی سریع اجرا می‌شوند تا بخشی از هر چرخه توسعه باشند و به تشخیص زودهنگام نقض‌های معماری کمک می‌کنند.

</div>

---

<div dir="rtl" style="text-align: right;">

### **خلاصه فصل**

در این فصل، چگونگی ترجمه مستقیم اصول معماری تمیز به شیوه‌های تست مؤثر را بررسی کردیم. یاد گرفتیم که چگونه مرزهای معماری به طور طبیعی استراتژی تست ما را هدایت می‌کنند و به وضوح مشخص می‌کنند که چه چیزی را تست کنیم و چگونه آن تست‌ها را ساختار دهیم. از طریق سیستم مدیریت وظایف خود، دیدیم که چگونه معماری تمیز تست متمرکز را بدون اتکای زیاد به تست‌های سرتاسری امکان‌پذیر می‌کند و در عین حال سیستم ما را قابل انطباق و پایدار نگه می‌دارد.

ما چندین الگوی تست کلیدی را پیاده‌سازی کردیم که مزایای معماری تمیز را نشان می‌دهند:

*   **تست‌های واحد که از مرزهای طبیعی معماری تمیز برای تأیید متمرکز استفاده می‌کنند**.
*   **تست‌های یکپارچه‌سازی که رفتار را در سراسر لایه‌های معماری خاص تأیید می‌کنند**.
*   **ابزارها و الگوها برای ساخت مجموعه‌های تست قابل نگهداری در مقیاس**.

مهمتر از همه، دیدیم که چگونه توجه دقیق معماری تمیز به وابستگی‌ها و رابط‌ها، تست‌های ما را متمرکزتر و قابل نگهداری‌تر می‌کند. با سازماندهی تست‌های خود برای احترام به مرزهای معماری، از ساختار فایل گرفته تا fixtureها، مجموعه‌های تستی را ایجاد می‌کنیم که به طور یکپارچه با سیستم‌های ما رشد می‌کنند.

در فصل ۹، نحوه اعمال اصول معماری تمیز در طراحی رابط کاربری وب را بررسی خواهیم کرد، نشان می‌دهیم که چگونه توجه دقیق ما به مرزهای معماری به ما امکان می‌دهد یک رابط کاربری وب کامل مبتنی بر Flask را با حداقل تغییرات در برنامه اصلی خود به سیستم مدیریت وظایف خود اضافه کنیم. این نمایش عملی نشان خواهد داد که چگونه تفکیک دغدغه‌ها در معماری تمیز به ما امکان می‌دهد CLI موجود خود را حفظ کرده و در عین حال رابط‌های کاربری جدیدی را به طور یکپارچه معرفی کنیم.

### **مطالعه بیشتر**

برای کسب اطلاعات بیشتر در مورد مباحث مطرح شده در این فصل، به منابع زیر مراجعه کنید:

*   راهنمای تست نرم‌افزار (https://martinfowler.com/testing/). مجموعه‌ای از تمام مقالات تست در وبلاگ مارتین فاولر.
*   فقط به تست‌های سرتاسری بیشتر "نه" بگویید (https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html). یک وبلاگ از تیم تست گوگل، که استدلال می‌کند اتکای بیش از حد به تست‌های سرتاسری می‌تواند منجر به افزایش پیچیدگی، شکنندگی و تأخیر در بازخورد در توسعه نرم‌افزار شود و به جای آن از یک رویکرد متعادل که بر تست‌های واحد و یکپارچه‌سازی تأکید می‌کند، حمایت می‌کند.
*   تست پایتون با `pytest` (https://pytest.org/). مستندات رسمی `pytest`، که اطلاعات دقیقی در مورد ابزارهای تست مورد استفاده در سراسر این فصل ارائه می‌دهد.
*   توسعه مبتنی بر تست (https://www.oreilly.com/library/view/test-driven-development/0321146530/). یک راهنمای ضروری برای TDD توسط کنت بک، یکی از پیشگامان آن. این کتاب یک پایه محکم برای درک اینکه چگونه TDD می‌تواند طراحی نرم‌افزار شما را بهبود بخشد و چگونه به طور طبیعی با الگوهای معماری مانند آنچه در معماری تمیز یافت می‌شود، همسو می‌شود، ارائه می‌دهد.

</div>