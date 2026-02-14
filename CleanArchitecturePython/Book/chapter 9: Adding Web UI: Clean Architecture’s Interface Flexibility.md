

<div dir="rtl" style="text-align: right;">

### سرفصل‌ها و تیترهای اصلی و فرعی فصل نهم 
</div>


*   **درک انعطاف‌پذیری رابط کاربری در معماری پاک**
    *   درک پیاده‌سازی وب ما
    *   پیاده‌سازی‌های رابط موازی
    *   نقض‌های رایج مرزهای رابط
*   **الگوهای نمایش وب در معماری پاک**
    *   پیاده‌سازی پرزنترهای خاص وب
    *   پرزنترها در مقابل قالب‌بندی مبتنی بر الگو
    *   مدیریت حالت خاص وب
    *   مدیریت فرم و اعتبارسنجی
*   **یکپارچه‌سازی Flask با معماری پاک**
    *   پیاده‌سازی مسیرها (routes) و الگوها (templates)
    *   اجرای برنامه وب معماری پاک شما

</div>

### <div dir="rtl" style="text-align: right;"> الزامات فنی </div>

<div dir="rtl" style="text-align: right;">

مثال‌های کد ارائه شده در این فصل و در ادامه کتاب با پایتون 3.13 آزمایش شده‌اند. برای اختصار، بیشتر مثال‌های کد در فصل فقط به‌طور جزئی پیاده‌سازی شده‌اند. نسخه‌های کامل همه مثال‌ها را می‌توانید در مخزن گیت‌هاب همراه کتاب به آدرس [https://github.com/PacktPublishing/Clean-Architecture-with-Python](https://github.com/PacktPublishing/Clean-Architecture-with-Python) بیابید.

</div>

### <div dir="rtl" style="text-align: right;"> درک انعطاف‌پذیری رابط کاربری در معماری پاک </div>

<div dir="rtl" style="text-align: right;">

رابط کاربری خط فرمان (CLI) سیستم مدیریت وظایف ما (که در فصل ۷ پیاده‌سازی شد) **جداسازی دقیق بین منطق اصلی کسب‌وکار و رابط‌های کاربری** را در معماری پاک نشان می‌دهد. این جداسازی نه تنها یک رویه خوب بود، بلکه آماده‌سازی استراتژیکی برای اضافه کردن یک رابط کاربری کاملاً جدید بدون خدشه وارد کردن به عملکرد موجود بود.

#### <div dir="rtl" style="text-align: right;"> درک پیاده‌سازی وب ما </div>

برای پیاده‌سازی رابط کاربری وب، از Flask استفاده می‌شود؛ یک چارچوب وب سبک و انعطاف‌پذیر پایتون. **مدیریت صریح درخواست‌ها و ساختار ساده برنامه Flask** آن را برای نشان دادن مرزهای معماری پاک ایده‌آل می‌کند. هسته حداقلی و اکوسیستم گسترده افزونه‌های اختیاری آن نیز با **ترجیح معماری پاک برای وابستگی‌های صریح** همخوانی دارد.

رابط کاربری وب قابلیت‌های مدیریت وظیفه موجود را با بازخورد بصری فوری و ناوبری شهودی بهبود می‌بخشد. کاربران می‌توانند وظایف جدید ایجاد کرده، وضعیت آن‌ها را به‌روز رسانی کنند و آن‌ها را در پروژه‌ها سازماندهی نمایند.

محل دیاگرام ۹.۱: صفحه لیست رابط کاربری وب که پروژه‌ها و وظایف مرتبط با آن‌ها را نشان می‌دهد

<div dir="rtl" style="text-align: right;">

برای پیاده‌سازی این رابط در حالی که مرزهای معماری ما حفظ می‌شود، پیاده‌سازی وب به مؤلفه‌های متمایز سازماندهی شده است:

</div>

محل دیاگرام ۹.۲: فایل‌های مرتبط برای پیاده‌سازی رابط کاربری وب

<div dir="rtl" style="text-align: right;">

این ساختار، **تفکیک مسئولیت‌ها را در معماری پاک** نشان می‌دهد. در لایه آداپتورها و رابط‌ها (interfaces)، پرزنترهای وب می‌دانند چگونه داده‌ها را برای نمایش وب قالب‌بندی کنند (ایجاد رشته‌های HTML-پسند و ساختاربندی داده‌ها برای الگوها)، اما **کاملاً از Flask یا هر چارچوب وب خاصی بی‌اطلاع هستند**. این پرزنترها می‌توانند به‌همان خوبی با Django، FastAPI یا هر چارچوب وب دیگری کار کنند.

این جداسازی در **تضاد شدید با برنامه‌هایی است که بدون مرزهای معماری پاک ساخته شده‌اند**. در یک برنامه با ساختار کمتر، درخواست برای افزودن یک رابط وب اغلب باعث زنجیره‌ای از تغییرات در سراسر پایگاه کد می‌شود. منطق کسب‌وکار که با نگرانی‌های نمایش ترکیب شده، نیاز به بازسازی گسترده دارد. پرس‌وجوهای پایگاه داده که در منطق نمایش تعبیه شده‌اند، نیاز به بازسازی دارند. توانایی افزودن ویژگی‌های اصلی بدون تغییر عملکرد موجود، **ارزش عملی معماری پاک را در تکامل سیستم‌ها** نشان می‌دهد.

کد خاص چارچوب در دایرکتوری `infrastructure/web` درون لایه چارچوب‌ها و درایورها قرار دارد. در اینجا، نگرانی‌های خاص Flask مانند **مدیریت مسیرها، پیکربندی الگوها و مدیریت جلسات HTTP** در لبه‌های سیستم ما ایزوله می‌مانند. این جداسازی به این معنی است که می‌توانیم چارچوب وب را بدون تغییر آداپتورهای رابط یا منطق اصلی کسب‌وکارمان تغییر دهیم.

#### <div dir="rtl" style="text-align: right;"> پیاده‌سازی‌های رابط موازی </div>

رابط‌های CLI و وب ما در سیستم معماری پاک ما با هم وجود دارند. در حالی که این رابط‌ها از طریق مکانیسم‌های بسیار متفاوتی (خط فرمان در مقابل HTTP) به کاربران خدمات می‌دهند، **مؤلفه‌های اصلی یکسانی را به اشتراک می‌گذارند و از الگوهای معماری یکسانی پیروی می‌کنند**.

محل دیاگرام ۹.۳: مقایسه جریان درخواست

<div dir="rtl" style="text-align: right;">

این نمودار نشان می‌دهد که چگونه معماری ما مرزهای واضحی را حفظ می‌کند در حالی که از چندین رابط پشتیبانی می‌کند:
*   **CLI** ورودی خط فرمان را از طریق Click Command Handler تبدیل می‌کند.
*   **رابط وب** درخواست‌های HTTP را از طریق Flask Route Handler پردازش می‌کند.
*   **هسته مشترک** شامل Task Controller، Use Cases و Entities ما است.

معماری پاک این همزیستی را از طریق **قوانین وابستگی سخت‌گیرانه** ممکن می‌سازد. هر دو کنترل‌کننده رابط به همان کنترل‌کننده وظایف متصل می‌شوند، اما مؤلفه‌های اصلی کاملاً از نحوه استفاده از آن‌ها بی‌خبر می‌مانند. این **جداسازی** به این معنی است که منطق اصلی کسب‌وکار ما می‌تواند بر قوانین ایجاد وظیفه تمرکز کند، در حالی که هر رابط نگرانی‌های خاص خود را مدیریت می‌کند.

برای پیاده‌سازی این جداسازی، از **رویکرد عملی تزریق وابستگی** از طریق کانتینر `Application` استفاده می‌شود:

</div>

```python
# todo_app/infrastructure/configuration/container.py
from dataclasses import dataclass

from todo_app.application.ports.notification import NotificationPort
from todo_app.application.ports.project_repository import ProjectRepository
from todo_app.application.ports.task_repository import TaskRepository
from todo_app.interfaces.presenters.project import ProjectPresenter
from todo_app.interfaces.presenters.task import TaskPresenter


@dataclass
class Application:
    """Container which wires together all components."""
    task_repository: TaskRepository
    project_repository: ProjectRepository
    notification_service: NotificationPort
    task_presenter: TaskPresenter
    project_presenter: ProjectPresenter

    # ... use case and controller wiring happens in __post_init__
    # (truncated for brevity, see original source)
```

<div dir="rtl" style="text-align: right;">

فکتوری برنامه ما الگوی ریشه ترکیب معماری پاک را پیاده‌سازی می‌کند که به عنوان **نقطه واحدی عمل می‌کند که در آن هسته مستقل از رابط ما با پیاده‌سازی‌های خاص رابط ترکیب می‌شود**. این فکتوری دو اصل کلیدی معماری را نشان می‌دهد:

</div>

```python
# todo_app/infrastructure/configuration/container.py
from typing import TYPE_CHECKING, Tuple

# Assuming these imports are from respective layers as per Clean Architecture
from todo_app.infrastructure.configuration.repositories import create_repositories
from todo_app.infrastructure.notifications.factory import create_notification_service

if TYPE_CHECKING:
    from todo_app.application.ports.notification import NotificationPort
    from todo_app.application.ports.project_repository import ProjectRepository
    from todo_app.application.ports.task_repository import TaskRepository
    from todo_app.interfaces.presenters.project import ProjectPresenter
    from todo_app.interfaces.presenters.task import TaskPresenter
    from todo_app.application.application import Application


def create_application(
    notification_service: "NotificationPort",
    task_presenter: "TaskPresenter",
    project_presenter: "ProjectPresenter",
) -> "Application":
    """Factory function for the Application container."""
    task_repository, project_repository = create_repositories()
    notification_service = create_notification_service() # This line seems incorrect based on signature,
                                                        # as notification_service is passed as an argument.
                                                        # Assuming it's meant to be used for the default or
                                                        # if not provided, or for a different purpose like creating a *real* one.
                                                        # Sticking to source code for now, but flagging.
    from todo_app.application.application import Application as AppContainer # Local import to avoid circular dependency

    return AppContainer(
        task_repository=task_repository,
        project_repository=project_repository,
        notification_service=notification_service,
        task_presenter=task_presenter,
        project_presenter=project_presenter,
    )
```

<div dir="rtl" style="text-align: right;">

اولاً، این فکتوری اصل وارونگی وابستگی معماری پاک را در عمل نشان می‌دهد: **مؤلفه‌های خاص رابط (پرزنترها) به عنوان پارامترها منتقل می‌شوند، در حالی که زیرساخت‌های اصلی در داخل ایجاد می‌شوند**. این رویکرد به `cli_main.py` و `web_main.py` اجازه می‌دهد تا پیاده‌سازی‌های خاص رابط خود را ارائه دهند و یک نقطه ورود واحد را برای کل برنامه فراهم کنند.

</div>

```python
# cli_main.py
import sys

from todo_app.infrastructure.cli.click_cli_app import ClickCli
from todo_app.infrastructure.configuration.container import create_application
from todo_app.infrastructure.notifications.recorder import NotificationRecorder
from todo_app.interfaces.presenters.cli import CliProjectPresenter, CliTaskPresenter


def main() -> int:
    """Main entry point for the CLI application."""
    try:
        app = create_application(
            notification_service=NotificationRecorder(),
            task_presenter=CliTaskPresenter(),
            project_presenter=CliProjectPresenter(),
        )
        cli = ClickCli(app)
        return cli.run()
    except KeyboardInterrupt:
        print("\nGoodbye!", file=sys.stderr)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

<div dir="rtl" style="text-align: right;">

همانطور که مشاهده می‌شود، `main()` یک نمونه برنامه خاص CLI را با ارائه پیاده‌سازی‌های خاص رابط ( `CliTaskPresenter`، `CliProjectPresenter`) به کانتینر برنامه عمومی ما پیکربندی می‌کند. سپس کلاس `ClickCli` این برنامه اصلی را پوشش می‌دهد و ترجمه بین تعاملات خط فرمان و عملیات مستقل از رابط برنامه ما را مدیریت می‌کند. این الگوی پوشش کد خاص رابط در اطراف برنامه اصلی ما، یک **رویه اساسی معماری پاک** است که در پیاده‌سازی وب ما نیز منعکس خواهد شد.

با این تنظیمات، ما یک الگوی واضح برای نحوه اتصال رابط‌های جدید به برنامه اصلی خود ایجاد کرده‌ایم. برای افزودن رابط وب خود، باید مؤلفه‌های مشابهی را پیاده‌سازی کنیم که همین نقش‌ها را ایفا کنند، اما برای نگرانی‌های خاص وب:
*   **لایه نمایش**: پیاده‌سازی `WebTaskPresenter` برای الگوهای HTML.
*   **مدیریت درخواست**: پردازش ارسال‌های فرم و پارامترهای URL.
*   **حالت جلسه**: مدیریت پایداری بین درخواست‌ها.
*   **بازخورد کاربر**: پیاده‌سازی نمایش خطای خاص وب.

نکته کلیدی این است که **تمام نگرانی‌های خاص رابط در لبه‌های سیستم ما باقی می‌مانند**. هر رابط الزامات منحصر به فرد خود را مدیریت می‌کند، مانند مدیریت جلسه وب یا تجزیه آرگومان‌های CLI، در حالی که منطق اصلی کسب‌وکار ما متمرکز و تمیز باقی می‌ماند.

#### <div dir="rtl" style="text-align: right;"> نقض‌های رایج مرزهای رابط </div>

اثربخشی معماری پاک به **حفظ مرزهای واضح بین لایه‌ها** بستگی دارد. یک نقض رایج زمانی اتفاق می‌افتد که توسعه‌دهندگان اجازه می‌دهند قالب‌بندی خاص رابط به کنترل‌کننده‌ها نفوذ کند و وابستگی‌های مشکل‌ساز را در جهت اشتباه ایجاد کند. مثالی از یک **ضد الگو** را در نظر بگیرید:

</div>

```python
# Anti-pattern: Interface-specific logic in controller
# (truncated for brevity, see original source)
import click # This import is a violation in the Interface Adapters layer

def handle_create(self, request_data: dict) -> dict:
    """DON'T: Mixing CLI formatting in controller."""
    try:
        result = self.create_use_case.execute(request_data)
        if result.is_success:
            # Wrong: CLI-specific formatting doesn't belong here
            return {
                "message": click.style(
                    f"Created task: {result.value.title}",
                    fg="green"
                )
            }
        # ... error handling ...
        return {"error": click.style(str(e), fg="red")}
    except ValueError as e:
        # Wrong: CLI-specific error formatting
        return {"error": click.style(str(e), fg="red")}
```

<div dir="rtl" style="text-align: right;">

این پیاده‌سازی **قانون وابستگی معماری پاک** را به شیوه‌ای ظریف اما مهم نقض می‌کند. کنترل‌کننده که در لایه آداپتورهای رابط قرار دارد، به‌طور مستقیم به Click (یک چارچوب که باید به بیرونی‌ترین لایه ما محدود شود) ارجاع می‌دهد. این یک **همبستگی مشکل‌ساز** ایجاد می‌کند، زیرا کنترل‌کننده اکنون هم به لایه کاربردی (به سمت داخل) و هم به لایه چارچوب‌ها (به سمت خارج) وابسته است، که **قانون اساسی معماری پاک را که وابستگی‌ها فقط باید به سمت داخل اشاره کنند، نقض می‌کند**.

به‌جای آن، سیستم مدیریت وظایف ما تمام **نگرانی‌های قالب‌بندی را به‌طور صحیح به پرزنترهای خاص رابط واگذار می‌کند**. توجه کنید که کنترل‌کننده ما فقط به رابط `Presenter` انتزاعی وابسته است. از اینکه با یک پرزنتر CLI، وب یا هر پیاده‌سازی پرزنتر بتنی دیگری کار می‌کند، بی‌خبر است:

</div>

```python
# Correct: Interface-agnostic controller
# (truncated for brevity, see original source)
from dataclasses import dataclass
from typing import Any, Dict, Optional, TYPE_CHECKING

from todo_app.application.request_models import CreateTaskRequest
from todo_app.interfaces.operation_result import OperationResult

if TYPE_CHECKING:
    from todo_app.application.use_cases.task_use_cases import CreateTaskUseCase
    from todo_app.interfaces.presenters.task import TaskPresenter


@dataclass
class TaskController:
    create_use_case: "CreateTaskUseCase"
    # ... additional use cases as needed
    presenter: "TaskPresenter"

    def handle_create(
        self,
        title: str,
        description: str,
        project_id: Optional[str] = None,
        priority: Optional[str] = None,
        due_date: Optional[str] = None,
    ) -> OperationResult[Any]: # Any used here for simplicity, typically a ViewModel
        """DO: Keep controllers interface-agnostic."""
        try:
            request = CreateTaskRequest(
                title=title,
                description=description,
                project_id=project_id,
                priority=priority,
                due_date=due_date,
            )
            result = self.create_use_case.execute(request)
            if result.is_success:
                view_model = self.presenter.present_task(result.value)
                return OperationResult.succeed(view_model)
            error_vm = self.presenter.present_error(
                result.error.message, str(result.error.code.name)
            )
            return OperationResult.fail(error_vm.message, error_vm.code)
        except ValueError as e:
            error_vm = self.presenter.present_error(str(e), "VALIDATION_ERROR")
            return OperationResult.fail(error_vm.message, error_vm.code)
```

<div dir="rtl" style="text-align: right;">

این پیاده‌سازی اصلاح شده چندین **اصل معماری پاک** را نشان می‌دهد:
*   **کنترل‌کننده انواع ساده (`str`) را می‌پذیرد** و نه ساختارهای خاص چارچوب.
*   **مدیریت خطا** نمونه‌های `OperationResult` مستقل از چارچوب را تولید می‌کند.
*   **تمام قالب‌بندی‌ها** به رابط پرزنتر انتزاعی واگذار می‌شوند.
*   **کنترل‌کننده بر هماهنگی بین موارد استفاده و نمایش** تمرکز می‌کند.

لایه آداپتورهای رابط به عنوان **مرز محافظتی** عمل می‌کند و داده‌ها را بین هسته دامنه ما و رابط‌های خارجی تبدیل می‌کند. این مرز معماری به ما امکان می‌دهد تا یک رابط وب را بدون ایجاد اختلال در مؤلفه‌های موجود اضافه کنیم.

</div>

### <div dir="rtl" style="text-align: right;"> الگوهای نمایش وب در معماری پاک </div>

<div dir="rtl" style="text-align: right;">

در حالی که CLI ما داده‌ها را مستقیماً برای خروجی کنسول قالب‌بندی می‌کرد، رابط‌های وب باید نیازهای نمایشی پیچیده‌تری را مدیریت کنند: **قالب‌بندی داده‌ها برای الگوهای HTML، مدیریت وضعیت در چندین درخواست و ارائه بازخورد کاربر از طریق اعتبارسنجی فرم و پیام‌های فلش (flash messages)**.

#### <div dir="rtl" style="text-align: right;"> پیاده‌سازی پرزنترهای خاص وب </div>

برای اتصال منطق دامنه ما به الزامات نمایش وب، به پرزنترهایی نیاز داریم که با **قوانین وب** آشنا باشند. پرزنتر CLI ما (از فصل ۷) تمام تصمیمات قالب‌بندی خاص CLI (مانند وضعیت در براکت، اولویت‌های رنگی) را کپسوله می‌کند و در عین حال یک رابط تمیز را از طریق `TaskViewModel` حفظ می‌کند. این الگوی **تبدیل اشیاء دامنه به مدل‌های نمایش مناسب رابط**، راهنمای پیاده‌سازی وب ما خواهد بود:

</div>

```python
# CLI Presenter from Chapter 7 (truncated for brevity)
# todo_app/interfaces/presenters/cli.py
from datetime import datetime, timezone, timedelta
from typing import Optional
from dataclasses import dataclass

from todo_app.application.response_models import TaskResponse
from todo_app.domain.entities.task import Priority, TaskStatus
from todo_app.interfaces.presenters.task import TaskPresenter
from todo_app.interfaces.view_models import ErrorViewModel, TaskViewModel


class CliTaskPresenter(TaskPresenter):
    def present_task(self, task_response: TaskResponse) -> TaskViewModel:
        """Format task for CLI display."""
        return TaskViewModel(
            id=str(task_response.id),
            title=task_response.title,
            description=task_response.description,
            # CLI-specific bracketed format:
            status_display=self._format_status(task_response.status),
            # CLI-specific coloring:
            priority_display=self._format_priority(task_response.priority),
            due_date_display=self._format_due_date(task_response.due_date),
            project_display=self._format_project(task_response.project_id),
            completion_info=self._format_completion_info(
                task_response.completion_date, task_response.completion_notes
            ),
        )

    def _format_status(self, status: TaskStatus) -> str:
        if status == TaskStatus.TODO:
            return "[TO DO]"
        elif status == TaskStatus.IN_PROGRESS:
            return "[IN PROGRESS]"
        elif status == TaskStatus.DONE:
            return "[DONE]"
        return f"[{status.value}]"

    def _format_priority(self, priority: Priority) -> str:
        if priority == Priority.HIGH:
            return "HIGH PRIORITY"
        elif priority == Priority.MEDIUM:
            return "MEDIUM PRIORITY"
        elif priority == Priority.LOW:
            return "LOW PRIORITY"
        return priority.name

    def _format_due_date(self, due_date: Optional[datetime]) -> str:
        if not due_date:
            return "No due date"
        is_overdue = due_date < datetime.now(timezone.utc)
        date_str = due_date.strftime("%Y-%m-%d")
        return f"OVERDUE - Due: {date_str}" if is_overdue else f"Due: {date_str}"

    def _format_project(self, project_id: str) -> str:
        return f"Project ID: {project_id}" if project_id else "No Project"

    def _format_completion_info(
        self, completion_date: Optional[datetime], notes: Optional[str]
    ) -> str:
        if completion_date:
            date_str = completion_date.strftime("%Y-%m-%d %H:%M")
            if notes:
                return f"Completed on: {date_str} ({notes})"
            return f"Completed on: {date_str}"
        return ""

    def present_error(self, error_msg: str, code: Optional[str] = None) -> ErrorViewModel:
        message = f"Error: {error_msg}"
        if code:
            message += f" (Code: {code})"
        return ErrorViewModel(message=message, code=code)

```

<div dir="rtl" style="text-align: right;">

پرزنتر وب ما نیز از همین الگو پیروی می‌کند، اما قالب‌بندی را برای نمایش HTML تطبیق می‌دهد:

</div>

```python
# Web Presenter
# todo_app/interfaces/presenters/web.py
from datetime import datetime, timezone, timedelta
from typing import Optional
from dataclasses import dataclass

from todo_app.application.response_models import TaskResponse, ProjectResponse
from todo_app.domain.entities.task import Priority, TaskStatus
from todo_app.interfaces.presenters.project import ProjectPresenter as ProjectPresenterInterface
from todo_app.interfaces.presenters.task import TaskPresenter as TaskPresenterInterface
from todo_app.interfaces.view_models import ErrorViewModel, TaskViewModel, ProjectViewModel


class WebTaskPresenter(TaskPresenterInterface):
    def present_task(self, task_response: TaskResponse) -> TaskViewModel:
        """Format task for web display."""
        return TaskViewModel(
            id=str(task_response.id),
            title=task_response.title,
            description=task_response.description,
            status_display=task_response.status.value,  # HTML-friendly status value
            priority_display=task_response.priority.name,  # HTML-friendly priority value
            due_date_display=self._format_due_date(task_response.due_date),
            project_display=self._format_project(task_response.project_id),
            completion_info=self._format_completion_info(
                task_response.completion_date, task_response.completion_notes
            ),
        )

    def _format_due_date(self, due_date: Optional[datetime]) -> str:
        """Format due date for web display."""
        if not due_date:
            return ""
        is_overdue = due_date < datetime.now(timezone.utc)
        date_str = due_date.strftime("%Y-%m-%d")
        return f"Overdue: {date_str}" if is_overdue else date_str

    def _format_project(self, project_id: str) -> str:
        return f"Project ID: {project_id}" if project_id else "No Project"

    def _format_completion_info(
        self, completion_date: Optional[datetime], notes: Optional[str]
    ) -> str:
        if completion_date:
            date_str = completion_date.strftime("%Y-%m-%d %H:%M")
            if notes:
                return f"Completed on: {date_str} ({notes})"
            return f"Completed on: {date_str}"
        return ""

    def present_error(self, error_msg: str, code: Optional[str] = None) -> ErrorViewModel:
        message = f"Error: {error_msg}"
        if code:
            message += f" (Code: {code})"
        return ErrorViewModel(message=message, code=code)


class WebProjectPresenter(ProjectPresenterInterface):
    def present_project(self, project_response: ProjectResponse) -> ProjectViewModel:
        """Format project for web display."""
        return ProjectViewModel(
            id=str(project_response.id),
            name=project_response.name,
            description=project_response.description,
            task_count=project_response.task_count,
            status_display=project_response.status,
            project_type_display=project_response.project_type,
            creation_date_display=project_response.creation_date.strftime("%Y-%m-%d"),
        )

    def present_error(self, error_msg: str, code: Optional[str] = None) -> ErrorViewModel:
        message = f"Error: {error_msg}"
        if code:
            message += f" (Code: {code})"
        return ErrorViewModel(message=message, code=code)

```

<div dir="rtl" style="text-align: right;">

توجه کنید که کلاس `WebTaskPresenter` فیلدها و قالب‌بندی‌های اضافی خاص نیازهای نمایش وب را فراهم می‌کند. این پیاده‌سازی نشان می‌دهد که چگونه **پرزنترهای معماری پاک به عنوان یک لایه ترجمه سیستماتیک بین مفاهیم دامنه و نیازهای نمایش عمل می‌کنند**.

متد `_format_due_date` تمام تصمیمات مربوط به قالب‌بندی تاریخ را کپسوله می‌کند: **مدیریت منطقه زمانی، رشته‌های قالب‌بندی تاریخ و بررسی وضعیت سررسید**. با قرار دادن این تصمیمات در پرزنتر، اطمینان حاصل می‌شود که اشیاء دامنه ما بر قوانین کسب‌وکار (زمان سررسید یک وظیفه) تمرکز می‌کنند، در حالی که **نگرانی‌های نمایش (نحوه نمایش تاریخ سررسید) در لایه معماری مناسب باقی می‌مانند**.

این لایه ترجمه به الگوهای ما اجازه می‌دهد تا ساده بمانند در حالی که اطلاعات غنی و متنی را ارائه می‌دهند:

</div>

```html
<!-- Example HTML template snippet -->
<span class="badge
{% if 'overdue' in task.due_date_display %}bg-danger
{%else %}bg-info
{% endif %}">
{{ task.due_date_display }}
</span>
```

<div dir="rtl" style="text-align: right;">

الگو، تفکیک مسئولیت‌ها را در معماری پاک نشان می‌دهد: **صرفاً بر ساختار HTML و تصمیمات استایل‌دهی بر اساس مقادیر از پیش قالب‌بندی شده تمرکز می‌کند**. تمام منطق کسب‌وکار (مقایسه‌های `datetime`) و قالب‌بندی داده‌ها در لایه‌های معماری مناسب باقی می‌مانند.

همانطور که در فصل ۸، می‌توانیم این منطق قالب‌بندی را از طریق تست‌های واحد متمرکز تأیید کنیم. این تست‌ها نشان می‌دهند که چگونه **جداسازی مسئولیت‌ها در معماری پاک، تأیید دقیق منطق قالب‌بندی وب ما را امکان‌پذیر می‌سازد**. می‌توانیم سناریوهای پیچیده، مانند تاریخ‌های سررسید گذشته، را بدون هیچ‌گونه تنظیمات چارچوب وب آزمایش کنیم.

</div>

```python
# Test: Web Presenter formats overdue date
# todo_app/tests/interfaces/test_presenters.py
from datetime import datetime, timezone, timedelta
from uuid import UUID

from todo_app.application.response_models import TaskResponse
from todo_app.domain.entities.task import Priority, TaskStatus
from todo_app.interfaces.presenters.web import WebTaskPresenter


def test_web_presenter_formats_overdue_date():
    """Test that presenter properly formats overdue dates."""
    # Arrange
    past_date = datetime.now(timezone.utc) - timedelta(days=1)
    task_response = TaskResponse(
        id=str(UUID('12345678-1234-5678-1234-567812345678')),
        title="Test Task",
        description="Test Description",
        status=TaskStatus.TODO,
        priority=Priority.MEDIUM,
        project_id=str(UUID('45678901-2345-6789-0123-456789012345')),
        due_date=past_date
    )
    presenter = WebTaskPresenter()

    # Act
    view_model = presenter.present_task(task_response)

    # Assert
    assert "Overdue" in view_model.due_date_display
    assert past_date.strftime("%Y-%m-%d") in view_model.due_date_display
```

<div dir="rtl" style="text-align: right;">

این تست مکمل تضمین می‌کند که پرزنتر ما تاریخ‌های آینده را به درستی مدیریت می‌کند و تأیید منطق قالب‌بندی تاریخ را کامل می‌کند. همراه با تست قبلی، حضور و عدم حضور نشانگر 'Overdue' را تأیید کرده‌ایم، همه این‌ها بدون دست زدن به هیچ کد چارچوب وب.

</div>

```python
# Test: Web Presenter formats future date
# todo_app/tests/interfaces/test_presenters.py
from datetime import datetime, timezone, timedelta
from uuid import UUID

from todo_app.application.response_models import TaskResponse
from todo_app.domain.entities.task import Priority, TaskStatus
from todo_app.interfaces.presenters.web import WebTaskPresenter


def test_web_presenter_formats_future_date():
    """Test that presenter properly formats future dates."""
    # Arrange
    future_date = datetime.now(timezone.utc) + timedelta(days=1)
    task_response = TaskResponse(
        id=str(UUID('12345678-1234-5678-1234-567812345678')),
        title="Test Task",
        description="Test Description",
        status=TaskStatus.TODO,
        priority=Priority.MEDIUM,
        project_id=str(UUID('45678901-2345-6789-0123-456789012345')),
        due_date=future_date
    )
    presenter = WebTaskPresenter()

    # Act
    view_model = presenter.present_task(task_response)

    # Assert
    assert "Overdue" not in view_model.due_date_display
    assert future_date.strftime("%Y-%m-%d") in view_model.due_date_display

```

<div dir="rtl" style="text-align: right;">

این تست‌ها مزایای کلیدی الگوی پرزنتر معماری پاک را برجسته می‌کنند. **منطق قالب‌بندی ما می‌تواند بدون تنظیمات پیچیده وب تأیید شود**. نیازی به کلاینت‌های تست Flask، پایگاه داده‌های Mock یا تجزیه HTML نیست.

#### <div dir="rtl" style="text-align: right;"> پرزنترها در مقابل قالب‌بندی مبتنی بر الگو </div>

بسیاری از برنامه‌ها **قالب‌بندی را مستقیماً در الگوها تعبیه می‌کنند**. در معماری پاک، ما قالب‌بندی را به عنوان یک **نگرانی ترجمه** می‌شناسیم که در لایه آداپتورهای رابط قرار دارد و نه در خود الگوها.

</div>

```html
<!-- Common pattern in many web frameworks (anti-pattern in Clean Architecture) -->
<span class="badge {% if task.due_date < now() %}bg-danger{% else %}bg-info{% endif %}">
{{ task.due_date.strftime("%Y-%m-%d") }}
{% if task.due_date < now() %}(Overdue){% endif %}
</span>
```

<div dir="rtl" style="text-align: right;">

اگرچه این الگو گسترده است، اما **مرز بین تصمیمات نمایش و ساختار نمایش را محو می‌کند**. اصل اساسی معماری یکسان است: **حفظ مرزهای واضح بین لایه‌ها**.

#### <div dir="rtl" style="text-align: right;"> مدیریت حالت خاص وب </div>

داده‌های جلسه و وضعیت فرم چالش‌های منحصر به فردی را برای حفظ مرزهای معماری پاک ارائه می‌دهند. یک **ضد الگو رایج** این است که یک موجودیت دامنه مستقیماً به داده‌های جلسه وب دسترسی پیدا کند:

</div>

```python
# Anti-pattern: Domain entity accessing web state
# (truncated for brevity, see original source)
from datetime import datetime
from uuid import UUID

class Task:
    def complete(self, web_app_contatiner):
        # Wrong: Task shouldn't know about web sessions
        self.completed_by = web_app_contatiner.user.id
        self.completed_at = datetime.now()

```

<div dir="rtl" style="text-align: right;">

این نشان می‌دهد که **ترکیب نگرانی‌های وب در موجودیت‌های دامنه چالش‌های نگهداری متعددی را ایجاد می‌کند**. هندلرهای مسیر Flask ما به عنوان **مرز معماری عمل می‌کنند که در آن نگرانی‌های خاص وب مدیریت می‌شوند**. آن‌ها مفاهیم HTTP را به عملیات مستقل از دامنه ترجمه می‌کنند در حالی که مدیریت وضعیت وب را در جای خود نگه می‌دارند:

</div>

```python
# todo_app/infrastructure/web/routes.py
# (truncated for brevity, see original source)
from flask import Blueprint, render_template, request, url_for, redirect, flash, current_app

from todo_app.interfaces.presenters.web import WebProjectPresenter, WebTaskPresenter


bp = Blueprint('todo', __name__, url_prefix='/')

# Presenters are not directly used in the route methods,
# but initialized here for potential future direct use,
# or for clarity of architectural boundaries.
task_presenter = WebTaskPresenter()
project_presenter = WebProjectPresenter()


@bp.route("/")
def index():
    """List all projects with their tasks."""
    app = current_app.config["APP_CONTAINER"]
    show_completed = (
        request.args.get("show_completed", "false")
        .lower() == "true"
    )
    result = app.project_controller.handle_list()

    if not result.is_success:
        error = project_presenter.present_error(result.error.message)
        flash(error.message, "error")
        return redirect(url_for("todo.index"))
    return render_template(
        "index.html",
        projects=result.success,
        show_completed=show_completed
    )

```

<div dir="rtl" style="text-align: right;">

این هندلر، مدیریت مرز در معماری پاک را در عمل نشان می‌دهد. در این لایه بیرونی سیستم ما، مسیر، **وضعیت خاص وب مانند اولویت `show_completed` را دریافت و پردازش می‌کند** و مفاهیم HTTP را به عملیات مستقل از دامنه ترجمه می‌کند.

#### <div dir="rtl" style="text-align: right;"> مدیریت فرم و اعتبارسنجی </div>

ارسال‌های فرم در برنامه‌های وب یک **چالش معماری** را ارائه می‌دهند. یک ضد الگو رایج این است که **منطق اعتبارسنجی را در الگوها، کنترل‌کننده‌ها و موجودیت‌های دامنه پخش کنید**، که نگهداری و تکامل قوانین اعتبارسنجی را دشوار می‌کند.

</div>

```python
# todo_app/infrastructure/web/routes.py
# (truncated for brevity, see original source)
from flask import Blueprint, render_template, request, url_for, redirect, flash, current_app
from uuid import UUID

from todo_app.interfaces.presenters.web import WebProjectPresenter, WebTaskPresenter


bp = Blueprint('todo', __name__, url_prefix='/')

task_presenter = WebTaskPresenter()
project_presenter = WebProjectPresenter()


@bp.route("/projects/new", methods=["GET", "POST"])
def new_project():
    """Create a new project."""
    if request.method == "POST":
        name = request.form["name"]
        app = current_app.config["APP_CONTAINER"]
        result = app.project_controller.handle_create(name)
        if not result.is_success:
            error = project_presenter.present_error(result.error.message)
            flash(error.message, "error")
            return redirect(url_for("todo.index"))
        project = result.success
        flash(f'Project "{project.name}" created successfully', "success")
        return redirect(url_for("todo.index"))
    return render_template("project_form.html")

```

<div dir="rtl" style="text-align: right;">

هندلر مسیر، **جریان اعتبارسنجی معماری پاک** را نشان می‌دهد:
1.  **مسیر ورودی‌های خاص وب را استخراج می‌کند**: پارامترهای URL (`project_id`)، فیلدهای فرم (`request.form["title"]`، و غیره) و فیلدهای اختیاری با مقادیر پیش‌فرض (`due_date`).
2.  **کنترل‌کننده وظایف پارامترهای استاندارد پایتون را دریافت می‌کند**: رشته‌ها برای فیلدهای متنی، `None` برای فیلدهای اختیاری خالی و `project_id` از URL.
3.  **اعتبارسنجی دامنه از طریق لایه‌های ایجاد شده اتفاق می‌افتد**: قوانین کسب‌وکار در موجودیت‌ها، هماهنگی مورد استفاده و نتایج از طریق نوع `Result` ما بازگردانده می‌شوند.
4.  **پاسخ‌های خاص وب**: تغییر مسیرهای موفقیت‌آمیز با پیام‌های فلش و مدیریت خطا از طریق پیام‌های فلش و تغییر مسیرها.

این جداسازی تضمین می‌کند که **قوانین اعتبارسنجی ما با منطق دامنه ما** باقی می‌مانند، در حالی که لایه وب بر جمع‌آوری ورودی و ارائه بازخورد تمرکز می‌کند.

</div>

### <div dir="rtl" style="text-align: right;"> یکپارچه‌سازی Flask با معماری پاک </div>

<div dir="rtl" style="text-align: right;">

برای یکپارچه‌سازی Flask با سیستم معماری پاک خود، بر جنبه‌های خاص Flask رابط وب خود تمرکز خواهیم کرد:
*   پیکربندی **الگوی فکتوری برنامه Flask**.
*   مدیریت **تنظیمات و وابستگی‌های خاص Flask**.
*   اتصال **مسیرهای Flask به منطق برنامه اصلی** ما.

در اینجا نحوه یکپارچه‌سازی فکتوری برنامه Flask ما با معماری موجودمان نشان داده شده است:

</div>

```python
# todo_app/infrastructure/web/app.py
from flask import Flask, Blueprint
from todo_app.application.application import Application
from todo_app.infrastructure.web.middleware import trace_requests # Assuming this is the correct path for trace_requests


def create_web_app(app_container: Application) -> Flask:
    """Create and configure Flask application."""
    flask_app = Flask(__name__)
    # Change this in production:
    flask_app.config["SECRET_KEY"] = "dev"
    # Store container in config:
    flask_app.config["APP_CONTAINER"] = app_container

    # Add trace ID middleware (from Chapter 10)
    trace_requests(flask_app)

    # Register blueprints
    from . import routes
    flask_app.register_blueprint(routes.bp)
    return flask_app

```

<div dir="rtl" style="text-align: right;">

همانطور که در شکل ۹.۴ نشان داده شده است، `web_main.py` به عنوان **نقطه ورود برنامه ما** عمل می‌کند و ایجاد و پیکربندی منطق کسب‌وکار (Application Container) و رابط وب (Web Container) ما را از طریق Flask هماهنگ می‌کند. کانتینر برنامه منطق اصلی کسب‌وکار ما را در خود نگه می‌دارد، در حالی که کانتینر وب نگرانی‌های خاص Flask مانند مسیرها و الگوها را مدیریت می‌کند.

</div>

محل دیاگرام ۹.۴: راه‌اندازی برنامه Flask که روابط کانتینرها را نشان می‌دهد

<div dir="rtl" style="text-align: right;">

این ساختار از اصول معماری پاک به چند روش کلیدی پیروی می‌کند:
*   **ایزوله نگه داشتن کد خاص Flask** در کانتینر وب.
*   **حفظ استقلال کانتینر برنامه اصلی** ما از نگرانی‌های وب.
*   فعال کردن **مسیرهای ارتباطی واضح بین کانتینرها** از طریق رابط‌های تعریف‌شده.

#### <div dir="rtl" style="text-align: right;"> پیاده‌سازی مسیرها (routes) و الگوها (templates) </div>

مسیرهای وب ما درخواست‌های HTTP را به عملیات‌هایی که هسته برنامه ما می‌تواند درک کند، ترجمه می‌کنند. در حالی که مکانیسم تحویل متفاوت است (درخواست‌های HTTP به جای آرگومان‌های خط فرمان)، **الگوی معماری یکسان باقی می‌ماند**: ورودی خارجی از طریق آداپتورهای رابط ما جریان می‌یابد قبل از اینکه به هسته برنامه ما برسد.

در اینجا چگونگی مدیریت ایجاد وظیفه در CLI آورده شده است:

</div>

```python
# todo_app/infrastructure/cli/click_cli_app.py
# (truncated for brevity, see original source)
import click
from todo_app.application.application import Application
from todo_app.interfaces.view_models import TaskViewModel, ErrorViewModel
from typing import Any


class ClickCli:
    def __init__(self, app: Application):
        self.app = app
        self.current_projects = []

    # ... other methods ...

    def _create_task(self) -> None:
        """CLI task creation."""
        title = click.prompt("Task title", type=str)
        description = click.prompt("Description", type=str)
        
        # This part assumes handle_create can take these arguments directly.
        # In a real setup, it might use a request model.
        # Sticking to the book's direct argument passing for the example.
        result = self.app.task_controller.handle_create(
            title=title,
            description=description
        )
        if not result.is_success:
            click.secho(result.error.message, fg="red", err=True)
            return

        task: TaskViewModel = result.success
        click.secho(f"Task '{task.title}' created successfully.", fg="green")
        
        # Refresh current projects to include the new task if applicable
        self._load_projects()

```

<div dir="rtl" style="text-align: right;">

مسیر وب ما همان الگوی معماری CLI را پیاده‌سازی می‌کند، اگرچه برای چرخه درخواست-پاسخ HTTP تطبیق داده شده است. این هندلر مسیر به عنوان یک مرز تمیز بین مفاهیم HTTP و منطق دامنه ما عمل می‌کند:

</div>

```python
# todo_app/infrastructure/web/routes.py
# (truncated for brevity, see original source)
from flask import Blueprint, render_template, request, url_for, redirect, flash, current_app
from uuid import UUID
from datetime import datetime, timezone

from todo_app.interfaces.presenters.web import WebProjectPresenter, WebTaskPresenter
from todo_app.domain.entities.task import Priority, TaskStatus # Assuming these are needed for form processing


bp = Blueprint('todo', __name__, url_prefix='/')

task_presenter = WebTaskPresenter()
project_presenter = WebProjectPresenter()


@bp.route("/projects/<project_id>/tasks/new", methods=["GET", "POST"])
def new_task(project_id: str):
    """Create a new task in a project."""
    if request.method == "POST":
        app = current_app.config["APP_CONTAINER"]
        try:
            # Note: project_id from URL, other data from form
            result = app.task_controller.handle_create(
                project_id=project_id,
                title=request.form["title"],
                description=request.form["description"],
                priority=request.form["priority"],
                due_date=(
                    request.form["due_date"]
                    if request.form["due_date"] else None
                ),
            )
            if not result.is_success:
                error = task_presenter.present_error(result.error.message)
                flash(error.message, "error")
                return redirect(url_for("todo.index"))
            task = result.success
            flash(f'Task "{task.title}" created successfully', "success")
            return redirect(url_for("todo.index"))
        except Exception as e: # Catch any other exceptions during processing
            flash(f"An unexpected error occurred: {e}", "error")
            return redirect(url_for("todo.index"))

    # For GET request or if POST fails and needs to re-render form
    return render_template("task_form.html", project_id=project_id)

```

<div dir="rtl" style="text-align: right;">

این الگوهای ثابت نشان می‌دهد که چگونه معماری پاک، رابط‌های متعدد را فعال می‌کند در حالی که هسته برنامه ما را بر **منطق کسب‌وکار** متمرکز نگه می‌دارد.

الگوها (templates) بیرونی‌ترین لایه سیستم معماری پاک ما را نشان می‌دهند و به عنوان **نقطه تبدیل نهایی بین مفاهیم دامنه و رابط کاربری** ما عمل می‌کنند. در حالی که پرزنترهای ما تبدیل منطقی داده‌های دامنه به مدل‌های نمایش را انجام می‌دهند، الگوها **صرفاً بر نمایش بصری آن داده‌ها تمرکز می‌کنند**:

</div>

```html
<!-- Example HTML template snippet -->
{% extends 'base.html' %}
{% block content %}
{% for project in projects %}
<div class="card mb-4">
<div class="card-header">
<h2 class="card-title h5 mb-0">{{ project.name }}</h2>
</div>
<!-- Template focuses purely on structure and display -->
    <div class="card-body">
        <p class="card-text">{{ project.description }}</p>
        <p class="card-text">Tasks: {{ project.task_count }}</p>
        <p class="card-text">Status: {{ project.status_display }}</p>
        <p class="card-text">Type: {{ project.project_type_display }}</p>
        <p class="card-text">Created: {{ project.creation_date_display }}</p>
        
        <ul class="list-group list-group-flush">
            {% for task in project.tasks %}
            <li class="list-group-item">
                <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">{{ task.title }}</h5>
                    <small>{{ task.due_date_display }}</small>
                </div>
                <p class="mb-1">{{ task.description }}</p>
                <small class="text-muted">Status: {{ task.status_display }} | Priority: {{ task.priority_display }}</small>
                {% if task.completion_info %}
                    <small class="text-success d-block">{{ task.completion_info }}</small>
                {% endif %}
            </li>
            {% endfor %}
        </ul>
        <div class="card-footer text-right">
            <a href="{{ url_for('todo.new_task', project_id=project.id) }}" class="btn btn-primary btn-sm">Add Task</a>
        </div>
    </div>
</div>
{% endfor %}
{% endblock %}
```

<div dir="rtl" style="text-align: right;">

این الگو تفکیک مسئولیت‌ها را در عمل نشان می‌دهد. این الگو منحصراً با `ProjectViewModel` که توسط پرزنترهای ما ارائه شده، کار می‌کند. توجه کنید که چگونه این الگو به سادگی به `project.name` ارجاع می‌دهد بدون اینکه اطلاعی از نحوه بازیابی یا پردازش آن داده داشته باشد.

#### <div dir="rtl" style="text-align: right;"> اجرای برنامه وب معماری پاک شما </div>

اسکریپت `web_main.py` به عنوان **ریشه ترکیب** ما عمل می‌کند؛ **نقطه واحدی که در آن رابط‌های انتزاعی با پیاده‌سازی‌های بتنی خود ملاقات می‌کنند**. این نقطه ورود، ایجاد و اتصال مؤلفه‌های ما را هماهنگ می‌کند در حالی که **قوانین وابستگی معماری پاک** را حفظ می‌کند:

</div>

```python
# web_main.py
import sys
from todo_app.infrastructure.configuration.container import create_application
from todo_app.infrastructure.notifications.factory import create_notification_service
from todo_app.infrastructure.web.app import create_web_app
from todo_app.interfaces.presenters.web import WebProjectPresenter, WebTaskPresenter


def main():
    """Create and run the Flask web application."""
    # Configure logging early (from Chapter 10)
    # todo_app.infrastructure.logging.config.configure_logging(app_context="WEB")

    app_container = create_application(
        notification_service=create_notification_service(),
        task_presenter=WebTaskPresenter(),
        project_presenter=WebProjectPresenter(),
    )
    web_app = create_web_app(app_container)
    web_app.run(debug=True)


if __name__ == "__main__":
    main()

```

<div dir="rtl" style="text-align: right;">

**اصل وارونگی وابستگی** پیکربندی زمان اجرا پیاده‌سازی‌های بتنی را از طریق متغیرهای محیطی امکان‌پذیر می‌سازد. همانطور که برنامه CLI ما می‌توانست مؤلفه‌ها را بدون تغییر کد تغییر دهد، رابط وب ما نیز این انعطاف‌پذیری را حفظ می‌کند:

```bash
# Repository Configuration
export TODO_REPOSITORY_TYPE="memory"  # or "file"
export TODO_DATA_DIR="repo_data"      # used with file repository

# Optional: Email Notification Configuration
export TODO_SENDGRID_API_KEY="your_api_key"
export TODO_NOTIFICATION_EMAIL="recipient@example.com"
```

<div dir="rtl" style="text-align: right;">

این انعطاف‌پذیری پیکربندی، **یک مزیت کلیدی معماری پاک** را نشان می‌دهد: **توانایی آسان تعویض مؤلفه‌ها**. به عنوان مثال، تغییر `TODO_REPOSITORY_TYPE` از "memory" به "file" کل پیاده‌سازی ذخیره‌سازی ما را بدون نیاز به تغییر کد تغییر می‌دهد. همین الگو که به ما امکان افزودن یک رابط وب را داد، موارد زیر را نیز امکان‌پذیر می‌سازد:
*   افزودن **بک‌اندهای ذخیره‌سازی جدید** (مانند PostgreSQL یا MongoDB).
*   پیاده‌سازی **خدمات اعلان اضافی**.
*   ایجاد **رابط‌های جدید** (مانند یک برنامه دسکتاپ یا موبایل).
*   پشتیبانی از **روش‌های احراز هویت جایگزین**.

هر یک از این بهبودها می‌تواند **به‌طور ایزوله پیاده‌سازی و آزمایش شود**، سپس از طریق مرزهای معماری پاک ما یکپارچه شوند.

برای راه‌اندازی برنامه وب، اسکریپت اصلی را اجرا کنید:

</div>

```bash
> python web_main.py
 * Serving Flask app 'todo_app.infrastructure.web.app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 954-447-204
127.0.0.1 - - [05/Feb/2025 13:58:57] "GET / HTTP/1.1" 200 -
```

<div dir="rtl" style="text-align: right;">

با مراجعه به آدرس `http://127.0.0.1:5000` در مرورگر خود، یک رابط وب نمایش داده می‌شود که در ظاهر کاملاً متفاوت از CLI ما است، اما بر روی **مؤلفه‌های اصلی یکسان** کار می‌کند.

محل دیاگرام ۹.۵: فرم ایجاد وظیفه که مدیریت ورودی خاص وب را نشان می‌دهد

<div dir="rtl" style="text-align: right;">

این دوگانگی، معماری پاک را در عمل نشان می‌دهد. برنامه خط فرمان ساده ما اکنون با یک رابط وب کامل، شامل فرم‌ها، به‌روزرسانی‌های پویا و بازخورد بصری، همزیستی دارد. هر دو رابط **مستقل از یکدیگر اجرا می‌شوند اما مؤلفه‌های اصلی یکسانی را به اشتراک می‌گذارند**. مورد استفاده ایجاد وظیفه یکسان که قبلاً دستورات CLI را پردازش می‌کرد، اکنون به‌طور یکپارچه ارسال‌های فرم وب را مدیریت می‌کند.

</div>

### <div dir="rtl" style="text-align: right;"> خلاصه </div>

<div dir="rtl" style="text-align: right;">

انتقال از CLI به رابط وب، **قدرت معماری پاک را در فعال کردن تکامل سیستم بدون به خطر انداختن یکپارچگی معماری** برجسته می‌کند. این فصل نشان داد که چگونه **ساختار لایه‌ای معماری پاک** به ما امکان می‌دهد یک رابط کاربری وب کامل Flask را اضافه کنیم در حالی که هسته منطق کسب‌وکار ما متمرکز و محافظت‌شده باقی می‌ماند.

این انعطاف‌پذیری به قیمت **قابلیت نگهداری** تمام نمی‌شود. با متمرکز نگه داشتن موجودیت‌های دامنه بر قوانین کسب‌وکار و موارد استفاده ما بر مفاهیم دامنه خالص، سیستمی ایجاد کرده‌ایم که در آن **هر لایه می‌تواند به‌طور مستقل تکامل یابد**.

</div>

### <div dir="rtl" style="text-align: right;"> مطالعه بیشتر </div>

<div dir="rtl" style="text-align: right;">

*   مستندات Flask ([https://flask.palletsprojects.com/en/stable/](https://flask.palletsprojects.com/en/stable/)).
*   WTForms ([https://wtforms.readthedocs.io/en/3.2.x/](https://wtforms.readthedocs.io/en/3.2.x/)).

</div>