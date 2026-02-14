<div dir="rtl" style="text-align: right;">

**فصل 10: پیاده‌سازی مشاهده‌پذیری: نظارت و راستی‌آزمایی**

<br/>
<br/>

**مقدمه:**

در فصل‌های پیشین، ما اصول اصلی معماری پاک (Clean Architecture) را از طریق سیستم مدیریت وظایفمان تثبیت کردیم. ما موجودیت‌های دامنه (domain entities) را ساختیم، موارد استفاده (use cases) را پیاده‌سازی کردیم، و هم رابط کاربری خط فرمان (CLI) و هم رابط کاربری وب را ایجاد کردیم که نشان می‌دهد چگونه مرزهای معماری پاک، جداسازی شفافی بین منطق اصلی کسب‌وکار و رابط‌های کاربری ایجاد می‌کنند. این مرزها، علاوه بر افزایش قابلیت نگهداری سیستم، هدف حیاتی دیگری را نیز دنبال می‌کنند: **قابلیت مشاهده‌پذیری سیستم و قابلیت راستی‌آزمایی یکپارچگی معماری آن**.

این فصل نشان می‌دهد که چگونه معماری پاک، مشاهده‌پذیری سیستم را از یک نگرانی متقاطع به یک قابلیت ساختاریافته تبدیل می‌کند. از آنجایی که سیستم ما با لایه‌های معماری شفاف و رابط‌های صریح ساخته شده است، نظارت به یک گسترش طبیعی از ساختار موجودمان تبدیل می‌شود. این سازماندهی که نظارت را ساده می‌کند، همچنین امکان راستی‌آزمایی مداوم را فراهم می‌آورد و به اطمینان از حفظ یکپارچگی معماری سیستم با تکامل آن کمک می‌کند.

تا پایان این فصل، شما درک خواهید کرد که چگونه مشاهده‌پذیری مؤثر را در سیستم‌های معماری پاک پیاده‌سازی کنید و چگونه یکپارچگی معماری را در طول زمان راستی‌آزمایی کنید. شما تکنیک‌های عملی برای شناسایی و جلوگیری از انحراف معماری را خواهید آموخت و اطمینان حاصل خواهید کرد که سیستم‌های شما حتی با تکامل الزامات و تیم‌ها، ساختار پاک خود را حفظ می‌کنند.

<br/>
<br/>

**سرفصل‌ها و تیترهای اصلی و فرعی فصل:**

*   **پیش‌نیازهای فنی**
*   **درک مرزهای مشاهده‌پذیری در معماری پاک**
    *   **نقاط مشاهده طبیعی در معماری پاک**
    *   **درک مشاهده‌پذیری در معماری پاک**
*   **پیاده‌سازی ابزارسازی بین-مرزی (Cross-Boundary Instrumentation)**
    *   **اجتناب از وابستگی فریم‌ورک در لاگ‌برداری**
    *   **پیاده‌سازی الگوهای لاگ‌برداری ساختاریافته**
    *   **ساخت مشاهده‌پذیری بین-مرزی**
*   **راستی‌آزمایی یکپارچگی معماری از طریق توابع فیتنس (Fitness Functions)**
    *   **راستی‌آزمایی ساختار لایه**
    *   **اعمال قوانین وابستگی**
*   **خلاصه**
*   **مطالعه بیشتر**

<br/>
<br/>

**توضیحات مهم هر بخش و مثال‌ها و کاربردها:**

**پیش‌نیازهای فنی**

<div dir="rtl" style="text-align: right;">
نمونه کدهای ارائه شده در این فصل و در بقیه کتاب با **پایتون 3.13** آزمایش شده‌اند. برای اختصار، بیشتر نمونه کدها در فصل تنها به‌صورت جزئی پیاده‌سازی شده‌اند. نسخه‌های کامل تمامی مثال‌ها در مخزن گیت‌هاب کتاب موجود است.
</div>

<br/>

**درک مرزهای مشاهده‌پذیری در معماری پاک**

<div dir="rtl" style="text-align: right;">
موقعیت‌یابی لایه‌های صریح و دقیق در معماری پاک، نقاط طبیعی برای مشاهده سیستم فراهم می‌کند، که یک مزیت قابل توجه است که بسیاری از تیم‌ها آن را نادیده می‌گیرند. در حالی که معماری‌های لایه‌ای می‌توانند پیچیدگی ایجاد کنند، همین تقسیم‌بندی‌ها که به مدیریت وابستگی‌ها کمک می‌کنند، نظارت و مشاهده‌پذیری سیستماتیک را نیز ممکن می‌سازند. این بخش نحوه ایجاد فرصت‌های بهتر برای ابزارسازی سیستم را از طریق اصول بنیادی معماری پاک بررسی می‌کند و پایه‌ای برای پیاده‌سازی‌های عملی بعدی فراهم می‌آورد.
</div>

**نقاط مشاهده طبیعی در معماری پاک**

<div dir="rtl" style="text-align: right;">
**ساختار لایه‌ای معماری پاک به‌طور طبیعی نقاط استراتژیک برای مشاهده سیستم ایجاد می‌کند**. مشاهده‌پذیری مدرن، لاگ‌برداری، معیارها (metrics)، و ردیابی درخواست را ترکیب می‌کند تا تصویری کامل از رفتار سیستم ارائه دهد. در سیستم‌های سنتی که این نگرانی‌ها در تمام مؤلفه‌ها نفوذ می‌کنند، پیاده‌سازی نظارت جامع اغلب به تلاشی برای دور زدن وابستگی‌های درهم تنیده تبدیل می‌شود.

**معماری پاک این پیچیدگی را به وضوح تبدیل می‌کند** با ارائه نقاط مشاهده ثابت در هر گذار لایه.
**مثال**: تصور کنید وقتی کاربری از طریق رابط کاربری وب، وظیفه‌ای ایجاد می‌کند، می‌توانیم درخواست را در حین حرکت از طریق لایه‌های معماری، از مدیریت اولیه HTTP، از طریق عملیات تجاری، تا ذخیره‌سازی نهایی، مشاهده کنیم.
هر مرز لایه بینش خاصی ارائه می‌دهد:
*   **رابط کاربری وب** ما درخواست‌های ورودی و تغییرات آن‌ها را ردیابی می‌کند.
*   **موارد استفاده (Use Cases)** عملیات تجاری و نتایج آن‌ها را نظارت می‌کنند.
*   **موجودیت‌های دامنه (Domain Entities)** تغییرات وضعیت و کاربردهای قواعد تجاری را ثبت می‌کنند.
*   **مؤلفه‌های زیرساختی (Infrastructure Components)** استفاده از منابع و تعاملات خارجی را اندازه‌گیری می‌کنند.

این رویکرد سیستماتیک تضمین می‌کند که دید کاملی نسبت به تمامی جنبه‌های حیاتی رفتار سیستم داشته باشیم و در عین حال جداسازی شفافی بین نگرانی‌های فنی و تجاری حفظ کنیم. این کار نه تنها نظارت، بلکه کل رویکرد ما به نگهداری سیستم را متحول می‌کند. هنگام بررسی مشکلات یا تجزیه و تحلیل عملکرد، دقیقاً می‌دانیم کجا به دنبال اطلاعات مرتبط بگردیم.
</div>

**درک مشاهده‌پذیری در معماری پاک**

<div dir="rtl" style="text-align: right;">
**سیستم‌های واقعی از همان ابتدا به مشاهده‌پذیری نیاز دارند**. ابزارسازی زودهنگام بسیار حیاتی است. بدون آن، اشکال‌زدایی چالش‌برانگیزتر می‌شود، مشکلات عملکردی کشف نمی‌شوند و درک رفتار سیستم در محیط‌های مختلف تقریباً غیرممکن می‌شود.
**مثال**: سیستم مدیریت وظایف ما را در نظر بگیرید. محل دیاگرام Figure 10.1: Task completion flow with observation points نشان می‌دهد که یک عملیات بظاهر ساده مانند تکمیل وظیفه، شامل چندین انتقال معماری است که هر یک نیازهای مشاهده‌پذیری متمایزی دارند. این شکل نشان می‌دهد که چگونه دغدغه‌های نظارتی به‌طور طبیعی با لایه‌های معماری ما هم‌راستا می‌شوند. در هر انتقال، ما جنبه‌های خاصی از رفتار سیستم را ثبت می‌کنیم، از معیارهای فنی در مرزهای بیرونی گرفته تا عملیات تجاری در لایه‌های اصلی. این رویکرد سیستماتیک تضمین می‌کند که **دید جامع** را حفظ کرده و در عین حال به جداسازی نگرانی‌های معماری پاک احترام می‌گذاریم.

یک رویکرد نظارتی لایه‌ای، مزایای روشنی را فراهم می‌کند. هنگام بررسی مشکلات، می‌توانیم عملیات را در سیستم خود با دقت ردیابی کنیم. اگر مشتری گزارش دهد که وظایف به‌صورت متناوب تکمیل نمی‌شوند، می‌توانیم عملیات را از درخواست وب تا منطق تجاری دنبال کنیم تا دقیقاً محل بروز مشکل را شناسایی کنیم. گلوگاه‌های عملکردی آسان‌تر پیدا می‌شوند، زیرا می‌دانیم کدام لایه هر جنبه از عملیات را مدیریت می‌کند.

هر لایه آنچه را که بهتر می‌داند ارائه می‌دهد. رابط‌های کاربری وب، مدیریت درخواست را ردیابی می‌کنند، موارد استفاده، عملیات تجاری را نظارت می‌کنند، و زیرساخت، معیارهای فنی را ثبت می‌کند. با احترام به این تقسیم‌بندی‌های طبیعی، جداسازی شفافی بین نگرانی‌های تجاری و فنی حفظ می‌کنیم و در عین حال دید جامع نسبت به رفتار سیستم خود را تضمین می‌کنیم. این اصول نظارتی مستقیماً به الگوهای پیاده‌سازی ترجمه می‌شوند. در سیستم مدیریت وظایف خود، از چارچوب استاندارد لاگ‌برداری پایتون برای پیاده‌سازی این مشاهده‌پذیری لایه‌ای استفاده خواهیم کرد.
</div>

<br/>

**پیاده‌سازی ابزارسازی بین-مرزی (Cross-Boundary Instrumentation)**

<div dir="rtl" style="text-align: right;">
این بخش، درک ما از مزایای مشاهده‌پذیری معماری پاک را به پیاده‌سازی عملی ترجمه می‌کند. چارچوب‌های وب مدرن مانند فِلَسک، زیرساخت لاگ‌برداری خاص خود را ارائه می‌دهند، که می‌تواند توسعه‌دهندگان را به **اتصال تنگاتنگ** عملیات تجاری با لاگ‌برداری فریم‌ورک-خاص وسوسه کند. ما خواهیم دید که چگونه می‌توان با این مکانیزم‌های فریم‌ورکی به‌طور مؤثر کار کرد در حالی که منطق اصلی کسب‌وکار از فریم‌ورک مستقل باقی بماند. با پیاده‌سازی دقیق لاگ‌برداری ساختاریافته و ردیابی درخواست، الگوهایی را نشان خواهیم داد که مرزهای معماری پاک را حفظ کرده و در عین حال مشاهده‌پذیری جامع سیستم را ارائه می‌دهند.
</div>

**اجتناب از وابستگی فریم‌ورک در لاگ‌برداری**

<div dir="rtl" style="text-align: right;">
چارچوب‌های وب اغلب زیرساخت لاگ‌برداری خاص خود را فراهم می‌کنند. به عنوان مثال، فِلَسک استفاده مستقیم از لاگر برنامه خود (`app.logger`) را تشویق می‌کند.
</div>

```python
@app.route('/tasks/new', methods=['POST'])
def create_task():
    task = create_task_from_request(request.form)
    # Framework-specific logging:
    app.logger.info('Created task %s', task.id)
    return redirect(url_for('index'))
```

<div dir="rtl" style="text-align: right;">
در حالی که این رویکرد راحت است، **اتصال مشکل‌سازی** بین عملیات تجاری ما و لاگ‌برداری فریم‌ورک-خاص ایجاد می‌کند. استفاده از `app.logger` فِلَسک مستلزم دسترسی به شیء برنامه فِلَسک در سراسر کدبیس است، که این **نقض جدی قاعده وابستگی (Dependency Rule) معماری پاک** است. لایه‌های داخلی برای انجام لاگ‌برداری باید به لایه فریم‌ورک دسترسی پیدا کنند، که دقیقاً همان نوع وابستگی خارجی است که معماری پاک قصد جلوگیری از آن را دارد.

به جای آن، معماری پاک ما را به سمت **لاگ‌برداری مستقل از فریم‌ورک** سوق می‌دهد که به مرزهای معماری احترام می‌گذارد.
**مثال**: نحوه لاگ‌برداری عملیات توسط مورد استفاده ایجاد وظیفه (task creation use case) را در نظر بگیرید:
</div>

```python
import logging
logger = logging.getLogger(__name__)

@dataclass
class CreateTaskUseCase:
    task_repository: TaskRepository
    project_repository: ProjectRepository

    def execute(self, request: CreateTaskRequest) -> Result:
        try:
            logger.info(
                "Creating new task",
                extra={"context": {
                    "title": request.title,
                    "project_id": request.project_id
                }},
            )
            # ... implementation continues ...
```

<div dir="rtl" style="text-align: right;">
این رویکرد چندین مزیت معماری پاک را ارائه می‌دهد:
*   **موارد استفاده (Use Cases) از جزئیات پیاده‌سازی لاگ‌برداری بی‌خبر می‌مانند**.
*   عبارات لاگ‌برداری به‌طور طبیعی عملیات تجاری را مستند می‌کنند.
*   می‌توانیم زیرساخت لاگ‌برداری را بدون تغییر منطق تجاری تغییر دهیم.
*   لاگ‌برداری فریم‌ورک-خاص در لبه‌های سیستم (جایی که به آن تعلق دارد) باقی می‌ماند.

این رویکرد لاگ‌برداری شفاف را به‌طور سیستماتیک پیاده‌سازی خواهیم کرد، با شروع از جداسازی مناسب نگرانی‌های لاگ‌برداری فریم‌ورک و برنامه.
</div>

**پیاده‌سازی الگوهای لاگ‌برداری ساختاریافته**

<div dir="rtl" style="text-align: right;">
همانطور که دیدیم، معماری پاک ایجاب می‌کند که نگرانی‌های زیرساختی، از جمله جزئیات پیاده‌سازی لاگ‌برداری، در لایه‌های بیرونی ایزوله شوند. برای پیاده‌سازی، ما **لاگ‌برداری ساختاریافته JSON** را انتخاب کرده‌ایم. این یک روش رایج است که پردازش و تجزیه و تحلیل دقیق لاگ را امکان‌پذیر می‌سازد. هر ورودی لاگ به یک شیء JSON با فیلدهای ثابت تبدیل می‌شود، که جستجو، فیلتر و تجزیه و تحلیل داده‌های لاگ را به‌صورت برنامه‌نویسی آسان‌تر می‌کند.
محل دیاگرام Figure 10.2: Logging files in the Frameworks and Drivers layer

این سازماندهی، پیکربندی لاگ‌برداری را در جایی که به آن تعلق دارد، یعنی در لایه فریم‌ورک‌ها و درایورها (Frameworks and Drivers layer)، نگه می‌دارد. جداسازی بین لاگ‌های فریم‌ورک (`access.log`) و لاگ‌های برنامه (`app.log`) نشان می‌دهد که چگونه مرزهای تمیز را حتی در خروجی لاگ خود حفظ می‌کنیم. این جداسازی دو هدف کلیدی معماری پاک را دنبال می‌کند:
*   **جداسازی نگرانی‌ها (Separation of Concerns)**: هر لایه آنچه را که بهتر می‌داند لاگ می‌کند. فِلَسک لاگ‌برداری درخواست HTTP را در قالب استاندارد خود مدیریت می‌کند، در حالی که برنامه ما عملیات تجاری را در قالب JSON ساختاریافته ثبت می‌کند. این جداسازی شفاف به معنای آن است که هر نوع لاگ می‌تواند به‌طور مستقل تکامل یابد، با استفاده از قالب‌ها و فیلدهایی که برای هدف خود مناسب هستند.
*   **استقلال از فریم‌ورک (Framework Independence)**: لاگ‌برداری اصلی برنامه ما کاملاً از فِلَسک یا هر چارچوب وب دیگری بی‌خبر می‌ماند. ما می‌توانیم به یک چارچوب دیگر تغییر دهیم، یا حتی رابط‌های جدیدی مانند REST API اضافه کنیم، در حالی که لاگ‌برداری عملیات تجاری ما بدون تغییر ادامه می‌یابد.

ما به روشی برای قالب‌بندی لاگ‌های برنامه خود نیاز داریم که از داده‌های ساختاریافته پشتیبانی کند و در عین حال مستقل از هر گونه نظری از سوی چارچوب باشد. **`JsonFormatter`** ما این مسئولیت را بر عهده می‌گیرد.
</div>

```python
from datetime import datetime, timezone
import logging
from json import JSONEncoder
from pathlib import Path
from uuid import UUID

class JsonLogEncoder(JSONEncoder):
    """Custom JSON encoder for logging specific types."""
    def default(self, obj):
        if isinstance(obj, (datetime, UUID)):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, Exception):
            return str(obj)
        return super().default(obj)

class JsonFormatter(logging.Formatter):
    """Formats log records as JSON."""
    def __init__(self, app_context: str):
        super().__init__()
        self.app_context = app_context
        # Custom encoder handles datetime, UUID, sets, and exceptions
        self.encoder = JsonLogEncoder()

    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON."""
        log_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "app_context": self.app_context,
        }
        # `extra` in the log statement, places `context`
        # on the LogRecord so seek and extract
        context = {}
        for key, value in record.__dict__.items():
            if key == "context":
                context = value
                break
        if context:
            log_data["context"] = context
        
        # Add trace ID if available
        trace_id = trace_id_var.get()
        if trace_id:
            log_data["trace_id"] = trace_id
            
        return self.encoder.encode(log_data)
```

<div dir="rtl" style="text-align: right;">
این فرمتر تمام منطق قالب‌بندی JSON را در یک مؤلفه واحد کپسوله می‌کند و **اصل مسئولیت واحد (Single Responsibility Principle)** را نشان می‌دهد.

با فرمتر ما که ساختار پیام‌های لاگ جداگانه را مدیریت می‌کند، اکنون باید پیکربندی کنیم که چگونه این پیام‌ها در سیستم ما جریان می‌یابند. این پیکربندی تعیین می‌کند که کدام لاگ‌ها به کجا می‌روند، و جداسازی شفاف ما بین لاگ‌برداری چارچوب و برنامه را حفظ می‌کند. برای وضوح، از `dictConfig` پایتون برای **تنظیم این مسیرها** استفاده خواهیم کرد.
</div>

```python
# todo_app/infrastructure/logging/config.py
# ... (JsonLogEncoder and JsonFormatter classes are omitted for brevity,
# as they were shown previously. Assume they are defined here.)

def configure_logging(app_context: Literal["CLI", "WEB"]) -> None:
    """Configure application logging with sensible defaults."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {"()": JsonFormatter, "app_context": app_context},
            "standard": {
                "format": "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
            },
            "web_access": {
                "format": "%(asctime)s %(levelname)s: %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
            },
            "app_file": {
                "class": "logging.FileHandler",
                "filename": log_dir / "app.log",
                "formatter": "json",
            },
            "web_access_file": {
                "class": "logging.FileHandler",
                "filename": log_dir / "access.log",
                "formatter": "web_access",
            },
        },
        "loggers": {
            "todo_app": {
                "handlers": ["app_file"],
                "level": "INFO",
                "propagate": False,
            },
            "werkzeug": {  # Flask's built-in web server logger
                "handlers": ["web_access_file"],
                "level": "INFO",
                "propagate": False,
            },
            "": {  # Root logger, catches everything else
                "handlers": ["console"],
                "level": "WARNING",
                "propagate": False,
            },
        },
    }
    logging.config.dictConfig(config)
```

<div dir="rtl" style="text: right;">
هر هندلر (handler) یک مقصد لاگ را با فرمتر مناسب خود متصل می‌کند و جداسازی شفاف ما بین نگرانی‌های چارچوب و برنامه را حفظ می‌کند. این پیکربندی در اوایل راه‌اندازی برنامه ما فعال می‌شود.
</div>

```python
# web_main.py
import sys
from todo_app.infrastructure.configuration.container import create_application
from todo_app.infrastructure.logging.config import configure_logging
from todo_app.infrastructure.web.app import create_web_app
from todo_app.infrastructure.web.presenters import WebProjectPresenter, WebTaskPresenter
from todo_app.infrastructure.notifications.recorder import NotificationRecorder

def main():
    """Create and run the Flask web application."""
    configure_logging(app_context="WEB") # Configure logging early
    
    app_container = create_application(
        notification_service=NotificationRecorder(),
        task_presenter=WebTaskPresenter(),
        project_presenter=WebProjectPresenter(),
    )
    
    web_app = create_web_app(app_container)
    web_app.run(debug=True)

if __name__ == "__main__":
    main()
```

<div dir="rtl" style="text-align: right;">
مهم‌تر از همه، این پیکربندی به این معنی است که هر کدی در برنامه ما می‌تواند به‌سادگی از ماژول استاندارد لاگ‌برداری پایتون استفاده کند بدون اینکه از قالب‌بندی JSON، هندلرهای فایل، یا هر جزئیات پیاده‌سازی دیگری بداند. این نگرانی‌ها به‌درستی در لایه زیرساخت ما قرار می‌گیرند.

**مثال**: مورد استفاده ایجاد وظیفه (Task Creation Use Case) را نشان می‌دهد که چگونه عملیات تجاری را می‌توان به‌وضوح لاگ‌برداری کرد بدون آگاهی از جزئیات خاص چارچوب.
</div>

```python
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List, Optional
from uuid import UUID

from todo_app.application.dtos import CompleteTaskRequest, CreateTaskRequest, TaskResponse
from todo_app.application.ports import NotificationPort
from todo_app.application.repositories import ProjectRepository, TaskRepository
from todo_app.domain.entities.project import Project, ProjectType
from todo_app.domain.entities.task import Task, TaskStatus, Priority, Deadline
from todo_app.domain.errors import ProjectNotFoundError, TaskNotFoundError, ValidationError
from todo_app.application.results import Result, Error

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CreateTaskUseCase:
    task_repository: TaskRepository
    project_repository: ProjectRepository

    def execute(self, request: CreateTaskRequest) -> Result:
        try:
            params = request.to_execution_params()
            project_id = params.get("project_id")

            if not project_id:
                project_id = self.project_repository.get_inbox().id
            else:
                try:
                    project = self.project_repository.get(project_id)
                    if project.project_type == ProjectType.INBOX:
                        return Result.failure(Error.validation_error("Cannot assign task directly to Inbox project."))
                except ProjectNotFoundError:
                    return Result.failure(Error.not_found("Project", str(project_id)))

            # Log before task creation
            logger.info(
                "Creating new task",
                extra={"context": {
                    "title": request.title,
                    "project_id": str(project_id) if project_id else "No project assigned"
                }},
            )

            task = Task(
                title=params["title"],
                description=params["description"],
                project_id=project_id,
                due_date=params.get("due_date"),
                priority=params.get("priority", Priority.MEDIUM),
            )
            self.task_repository.save(task)

            # Log after successful task creation
            logger.info(
                "Task created successfully",
                extra={"context":{
                    "task_id": str(task.id),
                    "project_id": str(project_id),
                    "priority": task.priority.name}}
            )

            return Result.success(TaskResponse.from_entity(task))
        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))
        except Exception as e:
            logger.exception("An unexpected error occurred during task creation")
            return Result.failure(Error.validation_error("An unexpected error occurred."))


@dataclass(frozen=True)
class CompleteTaskUseCase:
    task_repository: TaskRepository
    notification_service: NotificationPort

    def execute(
        self,
        request: CompleteTaskRequest,
    ) -> Result:
        try:
            params = request.to_execution_params()
            task_id = params["task_id"]

            logger.info("Attempting to complete task", extra={"context": {"task_id": str(task_id)}})
            task = self.task_repository.get(task_id)
            task.complete(notes=params["completion_notes"])
            self.task_repository.save(task)
            self.notification_service.notify_task_completed(task)
            logger.info("Task completed successfully", extra={"context": {"task_id": str(task_id)}})
            return Result.success(TaskResponse.from_entity(task))
        except TaskNotFoundError:
            logger.warning("Task not found for completion", extra={"context": {"task_id": str(task_id)}})
            return Result.failure(Error.not_found("Task", str(task_id)))
        except ValidationError as e:
            logger.warning("Validation error during task completion", extra={"context": {"task_id": str(task_id), "error": str(e)}})
            return Result.failure(Error.validation_error(str(e)))
        except Exception as e:
            logger.exception("An unexpected error occurred during task completion")
            return Result.failure(Error.validation_error("An unexpected error occurred."))


@dataclass(frozen=True)
class GetTaskUseCase:
    task_repository: TaskRepository

    def execute(self, task_id: UUID) -> Result:
        try:
            logger.info("Attempting to retrieve task", extra={"context": {"task_id": str(task_id)}})
            task = self.task_repository.get(task_id)
            logger.info("Task retrieved successfully", extra={"context": {"task_id": str(task_id)}})
            return Result.success(TaskResponse.from_entity(task))
        except TaskNotFoundError:
            logger.warning("Task not found for retrieval", extra={"context": {"task_id": str(task_id)}})
            return Result.failure(Error.not_found("Task", str(task_id)))
        except Exception as e:
            logger.exception("An unexpected error occurred during task retrieval")
            return Result.failure(Error.validation_error("An unexpected error occurred."))


@dataclass(frozen=True)
class DeleteTaskUseCase:
    task_repository: TaskRepository

    def execute(self, task_id: UUID) -> Result:
        try:
            logger.info("Attempting to delete task", extra={"context": {"task_id": str(task_id)}})
            self.task_repository.delete(task_id)
            logger.info("Task deleted successfully", extra={"context": {"task_id": str(task_id)}})
            return Result.success(None)  # No specific value needed for success
        except TaskNotFoundError:
            logger.warning("Task not found for deletion", extra={"context": {"task_id": str(task_id)}})
            return Result.failure(Error.not_found("Task", str(task_id)))
        except Exception as e:
            logger.exception("An unexpected error occurred during task deletion")
            return Result.failure(Error.validation_error("An unexpected error occurred."))


@dataclass(frozen=True)
class UpdateTaskUseCase:
    task_repository: TaskRepository
    notification_service: NotificationPort

    def execute(self, task_id: UUID, title: Optional[str] = None, description: Optional[str] = None, 
                due_date: Optional[Deadline] = None, priority: Optional[Priority] = None) -> Result:
        try:
            logger.info("Attempting to update task", extra={"context": {"task_id": str(task_id), "updates": {"title": title, "description": description, "due_date": due_date, "priority": priority}}})
            task = self.task_repository.get(task_id)

            if title:
                task.title = title
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if priority:
                task.priority = priority

            self.task_repository.save(task)
            logger.info("Task updated successfully", extra={"context": {"task_id": str(task_id)}})
            
            # Example of conditional notification based on priority change
            if priority == Priority.HIGH:
                self.notification_service.notify_task_high_priority(task)

            return Result.success(TaskResponse.from_entity(task))
        except TaskNotFoundError:
            logger.warning("Task not found for update", extra={"context": {"task_id": str(task_id)}})
            return Result.failure(Error.not_found("Task", str(task_id)))
        except ValidationError as e:
            logger.warning("Validation error during task update", extra={"context": {"task_id": str(task_id), "error": str(e)}})
            return Result.failure(Error.validation_error("An unexpected error occurred."))
```

<div dir="rtl" style="text-align: right;">
وقتی برنامه را اجرا می‌کنیم، خروجی لاگ به فرمت JSON ساختاریافته را در فایل `app.log` مشاهده می‌کنیم.
</div>

**ساخت مشاهده‌پذیری بین-مرزی**

<div dir="rtl" style="text-align: right;">
مرزهای صریح معماری پاک، مزایای حیاتی را فراهم می‌کنند، اما **ردیابی عملیات در سراسر لایه‌ها** می‌تواند چالش‌برانگیز باشد. در حالی که لاگ‌برداری ساختاریافته بینشی در مورد عملیات فردی ارائه می‌دهد، ردیابی درخواست‌ها در سراسر این مرزهای معماری نیازمند زیرساخت اضافی است.
**مثال**: یک عملیات مانند ایجاد وظیفه توسط کاربر از طریق رابط کاربری وب، چندین مرز معماری را در بر می‌گیرد:
1.  درخواست وب به هندلر مسیر فِلَسک ما می‌رسد.
2.  درخواست از طریق کنترلر وظیفه ما جریان می‌یابد.
3.  کنترلر مورد استفاده ما را فراخوانی می‌کند.
4.  مورد استفاده با مخازن (repositories) هماهنگ می‌شود.
5.  در نهایت، نتیجه از طریق این لایه‌ها باز می‌گردد.

**بدون ارتباط بین این رویدادها، اشکال‌زدایی و نظارت چالش‌برانگیز می‌شود**. راه‌حل ما ساده اما قدرتمند است: ما یک **شناسه منحصربه‌فرد (trace ID)** برای هر درخواست تولید کرده و این ID را در هر عبارت لاگ مربوط به آن درخواست وارد می‌کنیم. این کار به ما امکان می‌دهد تا **مسیر یک درخواست را در تمامی لایه‌های سیستم**، از درخواست اولیه وب تا عملیات پایگاه داده و بازگشت، دنبال کنیم.
برای پیاده‌سازی این ردیابی، باید:
1.  فایل `infrastructure/logging/trace.py` را برای مدیریت تولید و ذخیره‌سازی شناسه ردیابی ایجاد کنیم.
2.  پیکربندی لاگ‌برداری خود را در `infrastructure/logging/config.py` گسترش دهیم تا شناسه‌های ردیابی را در قالب‌های لاگ بگنجانیم.
3.  میان‌افزار فِلَسک را در `infrastructure/web/middleware.py` اضافه کنیم تا شناسه‌های ردیابی را برای درخواست‌های ورودی تنظیم کند.

از آنجایی که ما زیرساخت لاگ‌برداری خود را بر اساس اصول معماری پاک ساخته‌ایم، **هیچ تغییری در کد برنامه لازم نیست**. شناسه‌های ردیابی به‌طور خودکار از طریق فراخوانی‌های لاگ‌برداری موجود ما جریان خواهند یافت. بیایید با پایه شروع کنیم: مدیریت شناسه ردیابی. این زیرساخت، در حالی که کاملاً در لایه بیرونی ما قرار دارد، دید در سراسر تمام مرزهای معماری را امکان‌پذیر می‌سازد.
</div>

```python
# todo_app/infrastructure/logging/trace.py
from contextvars import ContextVar
from typing import Optional
from uuid import uuid4

# Thread-safe context variable to hold trace ID
trace_id_var: ContextVar[Optional[str]] = ContextVar("trace_id",
                                                     default=None)

def get_trace_id() -> str:
    """Get current trace ID or generate new one if not set."""
    current = trace_id_var.get()
    if current is None:
        current = str(uuid4())
        trace_id_var.set(current)
    return current

def set_trace_id(trace_id: Optional[str] = None) -> str:
    """Set trace ID for current context."""
    new_id = trace_id or str(uuid4())
    trace_id_var.set(new_id)
    return new_id
```

<div dir="rtl" style="text-align: right;">
تابع `set_trace_id` یک شناسه منحصربه‌فرد برای هر درخواست در سیستم ما ایجاد می‌کند.

با وجود مدیریت شناسه ردیابی، باید اطمینان حاصل کنیم که پیکربندی لاگ‌برداری ما، شناسه ردیابی را در قالب‌های لاگ شامل شود.
</div>

```python
# todo_app/infrastructure/logging/config.py
# ... (JsonLogEncoder and JsonFormatter classes are omitted for brevity,
# as they were shown previously. Assume they are defined here.)

def configure_logging(app_context: Literal["CLI", "WEB"]) -> None:
    """Configure application logging with sensible defaults."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {"()": JsonFormatter, "app_context": app_context},
            "standard": {
                "format": "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
            },
            "web_access": {
                "format": "%(asctime)s %(levelname)s: %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
            },
            "app_file": {
                "class": "logging.FileHandler",
                "filename": log_dir / "app.log",
                "formatter": "json",
            },
            "web_access_file": {
                "class": "logging.FileHandler",
                "filename": log_dir / "access.log",
                "formatter": "web_access",
            },
        },
        "loggers": {
            "todo_app": {
                "handlers": ["app_file"],
                "level": "INFO",
                "propagate": False,
            },
            "werkzeug": {  # Flask's built-in web server logger
                "handlers": ["web_access_file"],
                "level": "INFO",
                "propagate": False,
            },
            "": {  # Root logger, catches everything else
                "handlers": ["console"],
                "level": "WARNING",
                "propagate": False,
            },
        },
    }
    logging.config.dictConfig(config)
```

<div dir="rtl" style="text-align: right;">
پیکربندی لاگ‌برداری ما شامل شناسه‌های ردیابی در هر پیام لاگ، صرف نظر از قالب لاگ، می‌شود. برای لاگ‌های چارچوب، شناسه‌های ردیابی را با استفاده از نحو الگوی لاگ‌برداری داخلی پایتون (`%(trace_id)s`) به قالب استاندارد اضافه می‌کنیم. فرمتر JSON ما به‌طور خودکار شناسه‌های ردیابی را در خروجی ساختاریافته شامل می‌شود. این ثبات به این معنی است که می‌توانیم عملیات را در تمام منابع لاگ دنبال کنیم، در حالی که هر جریان لاگ قالب مناسب خود را حفظ می‌کند.

در نهایت، میان‌افزار وب ما تضمین می‌کند که هر درخواست یک شناسه ردیابی دریافت کند.
</div>

```python
# todo_app/infrastructure/web/middleware.py
from flask import request, g
from todo_app.infrastructure.logging.trace import set_trace_id

def trace_requests(flask_app):
    """Add trace ID to all requests."""
    @flask_app.before_request
    def before_request():
        trace_id = request.headers.get("X-Trace-ID") or None
        # pull trace id from globals
        g.trace_id = set_trace_id(trace_id)

    @flask_app.after_request
    def after_request(response):
        response.headers["X-Trace-ID"] = g.trace_id
        return response
```

<div dir="rtl" style="text-align: right;">
این میان‌افزار تضمین می‌کند که هر درخواست وب یک شناسه ردیابی منحصر به فرد دریافت کند. این شناسه سپس در سراسر پردازش درخواست در دسترس است و برای اهداف اشکال‌زدایی در هدرهای پاسخ گنجانده می‌شود. شناسه ردیابی تمام ورودی‌های لاگ مربوط به پردازش آن درخواست خاص را به هم متصل می‌کند، از دریافت اولیه HTTP تا عملیات تجاری و پاسخ نهایی.

محل دیاگرام Figure 7.6: Notification flow through architectural layers (This diagram illustrates a similar concept of flow through layers with observation points in Chapter 7, though not explicitly numbered in Chapter 10, it visually represents the "cross-boundary observability" concept).

پیاده‌سازی لاگ‌برداری و ردیابی ما نشان می‌دهد که چگونه مرزهای معماری پاک، مشاهده‌پذیری جامع سیستم را بدون به خطر انداختن اصول معماری امکان‌پذیر می‌سازند.
</div>

<br/>

**راستی‌آزمایی یکپارچگی معماری از طریق توابع فیتنس (Fitness Functions)**

<div dir="rtl" style="text-align: right;">
با تکامل سیستم‌ها، حفظ یکپارچگی معماری به‌طور فزاینده‌ای چالش‌برانگیز می‌شود. **توابع فیتنس معماری (Architectural Fitness Functions)**، همانطور که توسط ربه‌کا پارسونز، نیل فورد و پاتریک کوآ در کتابشان "Building Evolutionary Architectures" مطرح شده است، رویکردی سیستماتیک برای حفظ یکپارچگی معماری ارائه می‌دهند. همانطور که تست‌های واحد (unit tests) رفتار کد را راستی‌آزمایی می‌کنند، توابع فیتنس نیز ویژگی‌های معماری را راستی‌آزمایی می‌کنند. با کشف زودهنگام نقض‌ها در فرآیند توسعه (رویکردی که به آن "شیفت به چپ" (shift left) گفته می‌شود)، این تست‌ها به تیم‌ها کمک می‌کنند تا اصول معماری پاک را به‌صورت خودکار حفظ کنند.

در حالی که چارچوب‌های اعتبارسنجی معماری جامع وجود دارند، پایتون ما را قادر می‌سازد تا اعتبارسنجی مؤثر را به روشی ساده‌تر و عملگرایانه‌تر با استفاده از قابلیت‌های داخلی زبان پیاده‌سازی کنیم. در رویکرد راستی‌آزمایی معماری خود، بر دو جنبه کلیدی تمرکز خواهیم کرد: **اطمینان از حفظ سازماندهی لایه‌ای ساختار منبع (source structure)** و **کشف هر گونه نقض قاعده وابستگی بنیادی** که ایجاب می‌کند وابستگی‌ها فقط به سمت داخل (لایه‌های مرکزی‌تر) جریان یابند. این بررسی‌های مکمل به تیم‌ها کمک می‌کنند تا یکپارچگی معماری را با تکامل سیستم‌ها حفظ کنند.
</div>

**راستی‌آزمایی ساختار لایه**

<div dir="rtl" style="text-align: right;">
ابتدا، ساختار معماری مورد انتظار خود را تعریف می‌کنیم. در حالی که پیاده‌سازی خاص معماری پاک هر تیم ممکن است کمی متفاوت باشد، **اصل اصلی سازماندهی لایه صریح ثابت باقی می‌ماند**. ما می‌توانیم تفسیر خاص خود را در یک پیکربندی ساده ثبت کنیم:
</div>

```python
class ArchitectureConfig:
    """Defines Clean Architecture structure and rules."""
    # Ordered from innermost to outermost layer
    LAYER_HIERARCHY = [
        "domain",
        "application",
        "interfaces",
        "infrastructure"
    ]
```

<div dir="rtl" style="text-align: right;">
این پیکربندی به‌عنوان **قرارداد معماری** ما عمل می‌کند، و نحوه سازماندهی پوشه‌های کدبیس ما را تعریف می‌کند.

با تعریف ساختارمان، می‌توانیم تست‌های راستی‌آزمایی را پیاده‌سازی کنیم که اطمینان حاصل کنند کدبیس ما این سازماندهی را حفظ می‌کند.
</div>

```python
from pathlib import Path
import unittest

class ArchitectureConfig:
    """Defines Clean Architecture structure and rules."""
    # Ordered from innermost to outermost layer
    LAYER_HIERARCHY = [
        "domain",
        "application",
        "interfaces",
        "infrastructure"
    ]

class TestArchitectureStructure(unittest.TestCase):
    def test_source_folders(self):
        """Verify todo_app contains only Clean Architecture layer folders."""
        src_path = Path("todo_app")
        folders = {f.name for f in src_path.iterdir() if f.is_dir()}

        # All layer folders must exist
        for layer in ArchitectureConfig.LAYER_HIERARCHY:
            self.assertIn(
                layer,
                folders,
                f"Missing {layer} layer folder"
            )
        
        # No unexpected folders
        unexpected = folders - set(ArchitectureConfig.LAYER_HIERARCHY)
        self.assertEqual(
            unexpected,
            set(),
            f"Source should only contain Clean Architecture layers.\n"
            f"Unexpected folders found: {unexpected}"
        )
```

<div dir="rtl" style="text-align: right;">
این بررسی ساده یک اصل بنیادی معماری پاک را اعمال می‌کند: **کد منبع ما باید به‌طور صریح در لایه‌هایی با تعریف مشخص سازماندهی شود**.

**مثال**: یک سناریوی رایج را در نظر بگیرید: یک توسعه‌دهنده جدید، پوشه‌ای جدید به نام `notifications` در سطح ریشه (`root level`) ایجاد می‌کند. این انتخاب سازماندهی بظاهر بی‌ضرر، شروع "انحراف معماری" (architectural drift) را نشان می‌دهد. کد نوتیفیکیشن‌ها باید در لایه زیرساخت (Infrastructure) قرار گیرد زیرا یک نگرانی خارجی است. با ایجاد یک پوشه سطح بالا جدید، ما:
*   در مورد محل قرارگیری کد مربوط به نوتیفیکیشن‌ها سردرگمی ایجاد کرده‌ایم.
*   شروع به دور زدن لایه‌بندی صریح معماری پاک کرده‌ایم.
*   سابقه ای برای ایجاد پوشه‌های سطح بالا جدید زمانی که توسعه‌دهندگان در مورد مکان صحیح نامطمئن هستند، ایجاد کرده‌ایم.

بررسی ساختاری ساده ما این مورد را **به‌سرعت (به‌معنای واقعی کلمه در عرض چند ثانیه)** اگر تست‌ها روی دستگاه توسعه‌دهنده اجرا شوند، تشخیص می‌دهد.
</div>

```bash
❯ pytest tests/architecture
========== test session starts ==================
tests/architecture/test_source_structure.py F
E    AssertionError: Items in the first set but not the second:
E    'notifications' : Source should only contain Clean Architecture layers.
E    Unexpected folders found: {'notifications'}
```

<div dir="rtl" style="text-align: right;">
این خطا توسعه‌دهنده جدید را به **ادغام صحیح کد نوتیفیکیشن در لایه زیرساخت** سوق می‌دهد. این بررسی‌های ساختاری ساده، انحراف معماری را قبل از اینکه بتواند قابلیت نگهداری سیستم را به خطر بیندازد، تشخیص می‌دهند. با این حال، ساختار مناسب تنها بخشی از الزامات معماری پاک است.
</div>

**اعمال قوانین وابستگی**

<div dir="rtl" style="text-align: right;">
با راستی‌آزمایی ساختار لایه ما، باید اطمینان حاصل کنیم که این لایه‌ها به‌درستی طبق اصول معماری پاک با یکدیگر تعامل دارند. اساسی‌ترین این اصول، **قاعده وابستگی (Dependency Rule)** است، که بیان می‌کند **وابستگی‌ها فقط باید به سمت داخل به سمت لایه‌های مرکزی‌تر اشاره کنند**. حتی یک نقض کوچک از این قاعده می‌تواند یکپارچگی معماری را که با دقت ساخته‌ایم، به خطر بیندازد.

در ادامه راستی‌آزمایی ساختاری، نحوه کشف نقض‌های قاعده وابستگی را بررسی می‌کنیم. این قاعده برای حفظ جداسازی شفاف نگرانی‌ها بسیار مهم است، اما می‌تواند به‌طور ظریفی در طول توسعه نقض شود.

راستی‌آزمایی قاعده وابستگی ما رویکردی مستقیم دارد، با بررسی عبارت‌های `import` پایتون تا اطمینان حاصل شود که آنها فقط به سمت داخل از طریق لایه‌های معماری ما جریان می‌یابند.
</div>

```python
from pathlib import Path
import unittest
import ast

class TestDependencyRule(unittest.TestCase):
    def test_domain_layer_dependencies(self):
        """Verify domain layer has no outward dependencies."""
        domain_path = Path("todo_app/domain")
        violations = []
        for py_file in domain_path.rglob("*.py"):
            with open(py_file) as f:
                tree = ast.parse(f.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import) or isinstance(
                        node, ast.ImportFrom
                    ):
                        module = node.names.name
                        if module.startswith("todo_app."):
                            layer = module.split(".")
                            if layer in [
                                "infrastructure",
                                "interfaces",
                                "application"
                            ]:
                                violations.append(
                                    f"{py_file.relative_to(domain_path)}: "
                                    f"Domain layer cannot import from "
                                    f"{layer} layer"
                                )
        self.assertEqual(
            violations,
            [],
            "\nDependency Rule Violations:\n" + "\n".join(violations)
        )
```

<div dir="rtl" style="text-align: right;">
این پیاده‌سازی تست از ماژول داخلی `ast` پایتون برای تجزیه و تحلیل عبارت‌های `import` در کد لایه دامنه ما استفاده می‌کند.
**مثال**: یک توسعه‌دهنده در حال پیاده‌سازی نوتیفیکیشن‌های تکمیل وظیفه است. او متوجه می‌شود که `NotificationService` در لایه زیرساخت (Infrastructure) از قبل منطق مورد نیاز او را دارد. به‌جای پیروی از الگوهای معماری پاک، او از یک **میان‌بر** استفاده می‌کند که قاعده وابستگی بنیادی ما را نقض می‌کند:
</div>

```python
# todo_app/domain/entities/task.py
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

# For demonstration of the anti-pattern, this import would be present:
# from todo_app.infrastructure.notifications.recorder import NotificationRecorder

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
        # We need to enforce UTC for comparisons consistently
        if self.due_date.tzinfo is None:
            raise ValueError("Deadline datetime must be timezone-aware (UTC recommended)")
        if self.due_date < datetime.now(timezone.utc):
            raise ValueError("Deadline cannot be in the past")

    def is_overdue(self) -> bool:
        return datetime.now(timezone.utc) > self.due_date

    def time_remaining(self) -> timedelta:
        return max(
            timedelta(0),
            self.due_date - datetime.now(timezone.utc)
        )

    def is_approaching(self, warning_threshold: timedelta = timedelta(days=1)) -> bool:
        remaining = self.time_remaining()
        return timedelta(0) < remaining <= warning_threshold


@dataclass
class Task:
    title: str
    description: str
    project_id: UUID
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)
    id: UUID = field(default_factory=uuid4, init=False)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc), init=False)
    completed_at: Optional[datetime] = field(default=None, init=False)
    completed_by: Optional[UUID] = field(default=None, init=False)
    notes: Optional[str] = field(default=None, init=False)

    def start(self) -> None:
        if self.status != TaskStatus.TODO:
            raise ValueError(
                f"Only tasks with '{TaskStatus.TODO.value}' status can be started"
            )
        self.status = TaskStatus.IN_PROGRESS

    def complete(self, notes: Optional[str] = None, user_id: Optional[UUID] = None) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Task is already completed")
        self.status = TaskStatus.DONE
        self.completed_at = datetime.now(timezone.utc)
        self.notes = notes
        self.completed_by = user_id
        
        # Anti-pattern: Direct dependency on infrastructure – violates Clean Architecture
        # This line would be present in the anti-pattern example:
        # notification = NotificationRecorder()
        # notification.notify_task_completed(self)
```

<div dir="rtl" style="text-align: right;">
این تغییر ممکن است بی‌ضرر به نظر برسد زیرا کار را انجام می‌دهد. با این حال، دقیقاً همان نوع وابستگی خارجی را ایجاد می‌کند که معماری پاک آن را ممنوع کرده است. موجودیت دامنه ما اکنون مستقیماً به یک مؤلفه زیرساختی وابسته است، به این معنی که:
*   موجودیت `Task` دیگر نمی‌تواند بدون `NotificationService` آزمایش شود.
*   نمی‌توانیم پیاده‌سازی‌های نوتیفیکیشن را بدون تغییر کد دامنه تغییر دهیم.
*   یک سابقه برای ترکیب نگرانی‌های زیرساخت با منطق دامنه ایجاد کرده‌ایم.

بررسی وابستگی ما این نقض را **بلافاصله** در طول آزمایش تشخیص می‌دهد:
</div>

```bash
❯ pytest tests/architecture
====================== test session starts ==========
...
E    'entities/task.py: Domain layer cannot import from infrastructure layer'
E    Dependency Rule Violations:
E    entities/task.py: Domain layer cannot import from infrastructure layer
====================== 2 passed in 0.01s ============
```

<div dir="rtl" style="text-align: right;">
پیام خطا به‌وضوح شناسایی می‌کند:
*   فایل حاوی نقض.
*   اینکه کدام قانون معماری نقض شده است.
*   نحوه رفع آن (لایه دامنه نمی‌تواند از لایه زیرساخت وارد کند).

این راستی‌آزمایی‌های ساده اما قدرتمند به تیم‌ها کمک می‌کنند تا با اصول معماری پاک هم‌تراز باقی بمانند تا سیستم‌ها تکامل یابند.
</div>

<br/>
<br/>

**خلاصه:**

<div dir="rtl" style="text-align: right;">
در این فصل، چگونگی فعال‌سازی **نظارت سیستماتیک و راستی‌آزمایی** سیستم‌هایمان را از طریق مرزهای صریح معماری پاک بررسی کردیم. از طریق سیستم مدیریت وظایفمان، نشان دادیم که چگونه مشاهده‌پذیری مؤثر را پیاده‌سازی کنیم در حالی که یکپارچگی معماری حفظ شود. دیدیم که چگونه معماری پاک، نظارت را از یک نگرانی متقاطع به بخشی طبیعی از ساختار سیستممان تبدیل می‌کند.

چندین الگوی مشاهده‌پذیری کلیدی را پیاده‌سازی کردیم که مزایای معماری پاک را نشان می‌دهند:
*   **لاگ‌برداری مستقل از فریم‌ورک** که به مرزهای معماری احترام می‌گذارد و در عین حال دید جامع سیستم را فراهم می‌کند.
*   **ردیابی درخواست بین-مرزی** که جداسازی شفاف بین نگرانی‌های فنی و تجاری را حفظ می‌کند.
*   **راستی‌آزمایی خودکار معماری** که به تیم‌ها کمک می‌کند تا اصول معماری پاک را با تکامل سیستم‌ها حفظ کنند.

مهم‌تر از همه، دیدیم که چگونه توجه دقیق معماری پاک به مرزها، سیستم‌های ما را نه تنها **قابل نگهداری** بلکه **قابل مشاهده و قابل راستی‌آزمایی** می‌کند. با سازماندهی زیرساخت لاگ‌برداری و نظارتمان بر اساس اصول معماری پاک، سیستم‌هایی را ایجاد می‌کنیم که در طول زمان آسان‌تر درک، اشکال‌زدایی و نگهداری می‌شوند.

در **فصل 11**، نحوه اعمال اصول معماری پاک را در سیستم‌های موجود بررسی خواهیم کرد و نشان خواهیم داد که چگونه همین مرزها و الگوها می‌توانند به **تحول کدبیس‌های قدیمی به معماری‌های پاک و قابل نگهداری** کمک کنند.
</div>

<br/>

**مطالعه بیشتر:**

<div dir="rtl" style="text-align: right;">
برای کسب اطلاعات بیشتر در مورد مباحث مطرح شده در این فصل، به منابع زیر مراجعه کنید:
*   **راهنمای لاگ‌برداری پایتون (Python Logging Cookbook)**: مجموعه‌ای از دستورالعمل‌های کد مرتبط با لاگ‌برداری.
*   **Building Evolutionary Architectures**: کتابی عالی در مورد معماری نرم‌افزار که اصطلاح "تابع فیتنس" (Fitness Function) برای اولین بار در آن ابداع شد.
*   **PyTestArch**: یک چارچوب متن‌باز است که به شما امکان می‌دهد قوانین معماری را در کد تعریف کرده و به عنوان تست اجرا کنید.
</div>
</div>