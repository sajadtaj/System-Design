<div dir="rtl" style="text-align: right;">

این فصل به ما نشان می‌دهد که چگونه یک لایه کاربردی مؤثر را با استفاده از سیستم مدیریت وظایف به عنوان مثال پیاده‌سازی کنیم. ما یاد می‌گیریم که چگونه موارد استفاده‌ای ایجاد کنیم که اشیای دامنه را هماهنگ کرده و مرزهای معماری تمیز را حفظ کنند. همچنین نحوه تعریف مدل‌های درخواست و پاسخ را که به وضوح مرزهای مورد استفاده را مشخص می‌کنند، و نحوه مدیریت وابستگی‌ها به خدمات خارجی بدون به خطر انداختن یکپارچگی معماری را خواهیم آموخت.

در پایان این فصل، شما درک عمیقی از چگونگی پیاده‌سازی لایه کاربردی و چگونگی ارکستراسیون اشیای دامنه و هماهنگی با خدمات خارجی برای برآورده کردن نیازهای کاربر خواهید داشت.

---

مثال‌های کد ارائه شده در این فصل و سراسر کتاب، با پایتون 3.13 آزمایش شده‌اند. برای اختصار و به دلیل عدم وجود دستورات لاگ‌گذاری، برخی از مثال‌های کد در این فصل فقط به صورت جزئی پیاده‌سازی شده‌اند. نسخه‌های کامل تمام مثال‌ها را می‌توانید در مخزن گیت‌هاب همراه کتاب به آدرس: `https://github.com/PacktPublishing/Clean-Architecture-with-Python` بیابید.

---

در معماری تمیز (Clean Architecture)، هر لایه هدف خاصی در حفظ تفکیک نگرانی‌ها (separation of concerns) دارد. همانطور که در فصول قبلی دیدیم، لایه دامنه (Domain layer) قوانین اصلی کسب‌وکار ما را محصور می‌کند. **لایه کاربردی به عنوان رهبر ارکستر در ارکستر معماری تمیز عمل می‌کند.** این لایه اشیای دامنه و خدمات خارجی را برای انجام موارد استفاده خاص هماهنگ می‌کند، در حالی که مرز سخت‌گیرانه‌ای را بین قوانین کسب‌وکار و دنیای خارج حفظ می‌کند.

با پیاده‌سازی صحیح این لایه، برنامه‌هایی ایجاد می‌کنیم که نه تنها کارآمد هستند، بلکه قابل نگهداری و سازگار با تغییرات نیز هستند. لایه کاربردی اصل تفکیک نگرانی‌ها را در مرزهای معماری گسترش می‌دهد، جزئیات زیرساخت را از دامنه و پیچیدگی‌های دامنه را از واسط‌های خارجی پنهان می‌کند. این پنهان‌سازی عمدی اطلاعات، باعث می‌شود تلاش اضافی برای ایجاد پورت‌ها (ports)، آداپتورها (adapters) و مدل‌های درخواست/پاسخ (request/response models) ارزشمند باشد. با تنها نمایش دادن آنچه ضروری است از طریق واسط‌های با دقت طراحی شده، سیستمی ایجاد می‌کنیم که اجزای آن می‌توانند به صورت مستقل تکامل یابند و در عین حال به طور یکپارچه با یکدیگر کار کنند.

محل دیاگرام Figure 5.1: Application layer and task management

لایه کاربردی مسئولیت‌های مشخصی دارد:

* **ارکستراسیون موارد استفاده (Use case orchestration):**
  * هماهنگی اشیای دامنه برای انجام وظایف کاربر.
  * مدیریت توالی عملیات.
  * اطمینان از اعمال صحیح قوانین کسب‌وکار.
* **رسیدگی به خطا و اعتبار سنجی (Error handling and validation):**
  * اعتبار سنجی ورودی قبل از رسیدن به اشیای دامنه.
  * گرفتن و ترجمه خطاهای دامنه.
  * ارائه پاسخ‌های خطای یکنواخت.
* **مدیریت تراکنش (Transaction management):**
  * اطمینان از اتمیک بودن عملیات در صورت نیاز.
  * حفظ یکپارچگی داده‌ها.
  * مدیریت بازگشت به عقب در صورت شکست.
* **ترجمه مرزی (Boundary translation):**
  * تبدیل فرمت‌های داده خارجی به فرمت‌های دامنه.
  * تبدیل اشیای دامنه برای نمایش خارجی.
  * مدیریت ارتباطات بین‌مرزی.

این مسئولیت‌ها با هم کار می‌کنند تا یک لایه هماهنگی قدرتمند ایجاد کنند که مرزهای تمیز را حفظ کرده و در عین حال رفتار قابل اعتماد برنامه را تضمین می‌کند.

### **رسیدگی به خطا با انواع نتایج (Error handling with result types)**

قبل از پرداختن به الگوهای پیاده‌سازی، ضروری است که مفهوم اساسی در لایه کاربردی ما را درک کنیم:  **استفاده از نوع نتیجه (result type)** . این الگو ستون فقرات استراتژی رسیدگی به خطای ما را تشکیل می‌دهد و به جای صرفاً تکیه بر استثناها (exceptions)، رسیدگی صریح به موفقیت و شکست را فراهم می‌کند. این رویکرد چندین مزیت دارد:

* مسیرهای موفقیت/شکست را در امضاهای توابع صریح می‌کند.
* رسیدگی به خطای یکنواخت را در سراسر برنامه فراهم می‌کند.
* با ترجمه خطاهای دامنه، مرزهای معماری تمیز را حفظ می‌کند.
* قابلیت تست و پیش‌بینی رسیدگی به خطا را بهبود می‌بخشد.

ابتدا، یک کلاس `Error` استاندارد برای نمایش تمام خطاهای سطح برنامه تعریف می‌کنیم:

</div>

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any, Self

class ErrorCode(Enum):
    NOT_FOUND = "NOT_FOUND"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    # Add other error codes as needed

@dataclass(frozen=True)
class Error:
    """Standardized error information"""
    code: ErrorCode
    message: str
    details: Optional[dict[str, Any]] = None

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
```

```python
@dataclass(frozen=True)
class Result:
    """Represents success or failure of a use case execution"""
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
```

```python
# Assuming find_project, create_task, ProjectNotFoundError, ValidationError, etc. are defined elsewhere
# (This is pseudo-code as it directly comes from the source as part of explanation and not a full runnable example)
try:
    project = find_project(project_id)
    task = create_task(task_details)
    project.add_task(task)
    notify_stakeholders(task)
    return Result.success(TaskResponse.from_entity(task))
except ProjectNotFoundError:
    return Result.failure(Error.not_found("Project", str(project_id)))
except ValidationError as e:
    return Result.failure(Error.validation_error(str(e)))
```

<div dir="rtl" style="text-align: right;">

### **الگوهای لایه کاربردی (Application layer patterns)**

محل دیاگرام Figure 5.2: Request/Response flow in Clean Architecture

این تعامل هماهنگ بر روی سه الگوی اساسی متکی است که با هم کار می‌کنند تا مرزهای معماری تمیز را حفظ کنند:

* **تعامل‌کننده‌های مورد استفاده (Use case interactors):** این‌ها به عنوان هماهنگ‌کننده‌های اصلی عمل می‌کنند و عملیات کسب‌وکار خاص را پیاده‌سازی می‌کنند، در حالی که تراکنش‌ها را مدیریت کرده و اشیای دامنه را هماهنگ می‌کنند. آن‌ها اطمینان می‌دهند که هر عملیات متمرکز و اجرای آن سازگار است.
* **مرزهای واسط (Interface boundaries):** قراردادهای واضحی را بین لایه کاربردی ما و خدماتی که به آن‌ها وابسته است، برقرار می‌کنند.
* **معکوس سازی وابستگی (Dependency inversion):** پیاده‌سازی انعطاف‌پذیر و تست ساده را از طریق این مرزها امکان‌پذیر می‌کند و اطمینان می‌دهد که منطق اصلی کسب‌وکار ما از نگرانی‌های خارجی جدا باقی می‌ماند.

در ابتدا، موارد استفاده ما با پارامترهای ساده کار خواهند کرد و ساختارهای داده پایه را بازمی‌گردانند. با رشد برنامه، الگوهای پیچیده‌تری را برای مدیریت داده‌هایی که از مرزهای معماری ما عبور می‌کنند، معرفی خواهیم کرد. این تکامل به ما کمک می‌کند تا تفکیک تمیزی بین لایه‌ها را حفظ کنیم و در عین حال کدهایمان را با تغییرات سازگار نگه داریم.

این الگوها به طور طبیعی با **اصول SOLID** که در فصل 2 بررسی کردیم، همسو هستند. موارد استفاده اصل مسئولیت واحد (Single Responsibility Principle) را با تمرکز هر عملیات بر یک هدف خاص تجسم می‌کنند. تعاریف واسط از تفکیک واسط (interface segregation) با تعریف قراردادهای متمرکز و خاص مشتری پشتیبانی می‌کنند.

### **برنامه‌ریزی برای تکامل (Planning for evolution)**

برنامه‌ها به ندرت ثابت می‌مانند—برنامه‌های موفق ناگزیر در دامنه و پیچیدگی رشد می‌کنند. آنچه به عنوان یک سیستم مدیریت وظایف ساده شروع می‌شود، ممکن است نیاز به تکامل برای پشتیبانی از چندین تیم، ادغام با خدمات خارجی مختلف، یا مدیریت اتوماسیون جریان کار پیچیده داشته باشد.

معماری تمیز، توسعه این تکامل را نه با حدس زدن نیازهای آینده، بلکه با ایجاد **مرزهای استراتژیک** که به ما امکان می‌دهد قابلیت‌ها را با حداقل اختلال اضافه و حذف کنیم، امکان‌پذیر می‌کند. این مرزها به عنوان نقاط جداسازی عمل می‌کنند و به ما امکان می‌دهند تغییرات را به قسمت‌های خاصی از سیستم محدود کنیم.

این مزایای عملی را فراهم می‌کند:

* **انعطاف‌پذیری:**
  * افزودن رابط‌های کاربری جدید (مانند رابط کاربری وب، رابط خط فرمان، یا API) و استفاده از همان منطق اصلی کسب‌وکار از طریق همان رابط.
  * تغییر موتورهای پایگاه داده از SQLite به PostgreSQL بدون تغییر کد مورد استفاده.
* **مرزهای ثابت:**
  * رسیدگی به تبدیل داده‌ها در اشیای درخواست (Request objects) در نسخه‌های جدید API (v1 در مقابل v2) در حالی که از همان کد مورد استفاده زیرین استفاده می‌شود.
  * پیاده‌سازی مبدل‌های پاسخ (Response transformers) متمایز برای مشتریان مختلف (موبایل، وب، CLI) در حالی که منطق اصلی کسب‌وکار یکسان به اشتراک گذاشته می‌شود.

این پایه معماری به ما امکان می‌دهد سیستم خود را با اطمینان تکامل دهیم. هنگامی که تیم بازاریابی درخواست یکپارچه‌سازی Salesforce را می‌کند، یا هنگامی که الزامات تطابق، لاگ‌گذاری ممیزی (audit logging) را لازم می‌کند، این قابلیت‌ها را می‌توان بدون اختلال در عملکرد موجود یا به خطر انداختن یکپارچگی معماری اضافه کرد.

در بخش بعدی، چگونگی پیاده‌سازی این مفاهیم در پایتون را بررسی خواهیم کرد و تعامل‌کننده‌های مورد استفاده قوی را ایجاد خواهیم کرد که اصول معماری تمیز را حفظ می‌کنند.

---

### **پیاده‌سازی تعامل‌کننده‌های مورد استفاده (Implementing use case interactors)**

پس از بررسی مبانی نظری لایه کاربردی، اکنون به پیاده‌سازی عملی می‌پردازیم. **تعامل‌کننده‌های مورد استفاده، کلاس‌های مشخصی هستند که قوانین کسب‌وکار خاص برنامه را پیاده‌سازی می‌کنند.** اصطلاح *تعامل‌کننده‌ها* بر نقش آن‌ها در تعامل و هماهنگی بخش‌های مختلف سیستم تأکید می‌کند. در حالی که لایه دامنه (Domain layer) قوانین کسب‌وکار را تعریف می‌کند، تعامل‌کننده‌ها نحوه و زمان اعمال این قوانین را در پاسخ به نیازهای خاص برنامه تعریف می‌کنند. در پایتون، می‌توانیم این تعامل‌کننده‌ها را به روشی تمیز و گویا پیاده‌سازی کنیم.

### **ساختاردهی یک مورد استفاده (Structuring a use case)**

</div>

```python
from dataclasses import dataclass
from uuid import UUID
from typing import Optional

# Assuming TaskRepository, Result, TaskViewModel are defined elsewhere
# (This is a skeleton/partial code as provided in the source to demonstrate structure)
@dataclass(frozen=True)
class CompleteTaskUseCase:
    """Use case for marking a task as complete and notifying stakeholders"""
    task_repository: Any # This should be TaskRepository
    # ... additional use cases as needed
    # presenter: TaskPresenter # This is not part of the Use Case but an example of what it might interact with
    # For now, let's keep it clean as the source implies.

    def execute(
        self,
        task_id: UUID,
        completion_notes: Optional[str] = None
    ) -> Any: # This should be Result
        # ... implementation
        pass
```


<div dir="rtl" style="text-align: right;">


سپس، متد `execute` را بررسی می‌کنیم:

</div>

```python
# Assuming Task, TaskNotFoundError, ValidationError, Error, TaskResponse are defined elsewhere
# (This is a partial code as provided in the source to demonstrate implementation details)
def execute(
    self,
    task_id: UUID,
    completion_notes: Optional[str] = None
) -> Any: # This should be Result
    try:
        # Input validation
        task = self.task_repository.get(task_id)
        task.complete(
            notes=completion_notes
        )
        self.task_repository.save(task)
        # Return simplified task data
        return Result.success({
            "id": str(task.id),
            "status": "completed",
            "completion_date": task.completed_at.isoformat()
        })
    except TaskNotFoundError:
        return Result.failure(Error.not_found("Task", str(task_id)))
    except ValidationError as e:
        return Result.failure(Error.validation_error(str(e)))
```


<div dir="rtl" style="text-align: right;">


این پیاده‌سازی چندین اصل معماری کلیدی را در بر می‌گیرد:

* **محصور سازی (Encapsulation):** کلاس مورد استفاده یک مرز واضح را در اطراف یک عملیات کسب‌وکار خاص فراهم می‌کند.
* **تعریف واسط (Interface definition):** متد `execute` یک واسط تمیز و متمرکز با استفاده از نوع نتیجه را فراهم می‌کند. الگوی نتیجه تضمین می‌کند که هر دو مسیر موفقیت و شکست در واسط ما صریح هستند، و رسیدگی به خطا را به عنوان یک نگرانی درجه یک مطرح می‌کند.
* **رسیدگی به خطا (Error handling):** خطاهای دامنه گرفته شده و به خطاهای سطح برنامه ترجمه می‌شوند.
* **تزریق وابستگی (Dependency injection):** وابستگی‌ها از طریق سازنده (constructor) منتقل می‌شوند و به اصل معکوس سازی وابستگی که در فصل 2 معرفی شد، پایبند هستند.

از بین این اصول، **تزریق وابستگی** شایسته توجه ویژه‌ای است، زیرا بخش زیادی از انعطاف‌پذیری معماری ما را امکان‌پذیر می‌سازد.

### **تزریق وابستگی (Dependency injection)**


</div>

```python
from abc import ABC, abstractmethod
from uuid import UUID

# Assuming Task is defined elsewhere
class TaskRepository(ABC):
    """Repository interface defined by the Application Layer"""
    @abstractmethod
    def get(self, task_id: UUID) -> Any: # Should be -> Task
        """Retrieve a task by its ID"""
        pass

    @abstractmethod
    def save(self, task: Any) -> None: # Should be (self, task: Task) -> None
        """Save a task to the repository"""
        pass

    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        """Delete a task from the repository"""
        pass

class NotificationService(ABC):
    """Service interface for sending notifications"""
    @abstractmethod
    def notify_task_assigned(self, task_id: UUID) -> None:
        """Notify when a task is assigned"""
        pass

    @abstractmethod
    def notify_task_completed(self, task: Any) -> None: # Should be (self, task: Task) -> None
        """Notify when a task is completed"""
        pass
```


<div dir="rtl" style="text-align: right;">


یک پیاده‌سازی مشخص که به این قرارداد پایبند باشد، ممکن است به این شکل باشد:

</div> 

```python
# Assuming MongoClient, Task, TaskNotFoundError are defined elsewhere
# (This is a partial code as provided in the source to demonstrate implementation details)
class MongoDbTaskRepository(TaskRepository):
    """MongoDB implementation of the TaskRepository interface"""
    def __init__(self, client: Any): # Should be MongoClient
        self.client = client
        self.db = client.task_management
        self.tasks = self.db.tasks

    def get(self, task_id: UUID) -> Any: # Should be Task
        """Retrieve a task by its ID"""
        document = self.tasks.find_one({"_id": str(task_id)})
        if not document:
            raise TaskNotFoundError(task_id)
        # ... remainder of method implementation
        # Other interface methods implemented ...
        pass
```


<div dir="rtl" style="text-align: right;">


### **رسیدگی به عملیات پیچیده (Handling complex operations)**

`CompleteProjectUseCase` از الگوی تثبیت شده ما پیروی می‌کند:


</div>

```python
from dataclasses import dataclass
from uuid import UUID
from typing import Optional

# Assuming ProjectRepository, TaskRepository, NotificationService, Result are defined elsewhere
@dataclass(frozen=True)
class CompleteProjectUseCase:
    project_repository: Any # Should be ProjectRepository
    task_repository: Any # Should be TaskRepository
    notification_service: Any # Should be NotificationService

    def execute(
        self,
        project_id: UUID,
        completion_notes: Optional[str] = None
    ) -> Any: # Should be Result
        # ... implementation
        pass
```

```python
# Assuming ProjectNotFoundError, ValidationError, Error, Project, Task, TaskResponse are defined elsewhere
# (This is a partial code as provided in the source to demonstrate implementation details)
def execute(
    self,
    project_id: UUID,
    completion_notes: Optional[str] = None
) -> Any: # Should be Result
    try:
        # Validate project exists
        project = self.project_repository.get(project_id)
        # Complete all outstanding tasks
        for task in project.incomplete_tasks:
            task.complete()
            self.task_repository.save(task)
            self.notification_service.notify_task_completed(task)
        # Complete the project itself
        project.mark_completed(
            notes=completion_notes
        )
        self.project_repository.save(project)
        return Result.success({
            "id": str(project.id),
            "status": project.status,
            "completion_date": project.completed_at,
            "task_count": len(project.tasks),
            "completion_notes": project.completion_notes,
        })
    except ProjectNotFoundError:
        return Result.failure(Error.not_found(
            "Project", str(project_id)))
    except ValidationError as e:
        return Result.failure(Error.validation_error(str(e)))
```


<div dir="rtl" style="text-align: right;">


با اعمال این الگوها به طور مداوم در سراسر لایه کاربردی، ما یک سیستم قوی ایجاد می‌کنیم که عملیات پیچیده را به آرامی مدیریت می‌کند در حالی که مرزهای معماری تمیز و تفکیک نگرانی‌های واضح را حفظ می‌کند.

---

### **تعریف مدل‌های درخواست و پاسخ (Defining request and response models)**

در بخش قبلی، موارد استفاده ما مستقیماً با انواع ابتدایی و دیکشنری‌ها کار می‌کردند. در حالی که این رویکرد می‌تواند برای موارد ساده کار کند، با رشد برنامه، به روش‌های ساختارمندتری برای رسیدگی به داده‌هایی که از مرزهای معماری ما عبور می‌کنند، نیاز داریم. **مدل‌های درخواست و پاسخ** این هدف را برآورده می‌کنند و DTOهای (Data Transfer Objects) تخصصی را فراهم می‌کنند که تبدیل داده‌ها را بین لایه‌های بیرونی و موارد استفاده انجام می‌دهند.

### **مدل‌های درخواست (Request models)**


</div>

```python
from dataclasses import dataclass
from typing import Optional
from uuid import UUID

# Assuming ValidationError is defined elsewhere
@dataclass(frozen=True)
class CompleteProjectRequest:
    """Data structure for project completion requests"""
    project_id: str  # From API (will be converted to UUID)
    completion_notes: Optional[str] = None

    def __post_init__(self) -> None:
        """Validate request data"""
        if not self.project_id.strip():
            raise ValidationError("Project ID is required")
        if self.completion_notes and len(self.completion_notes) > 1000:
            raise ValidationError(
                "Completion notes cannot exceed 1000 characters")

    def to_execution_params(self) -> dict:
        """Convert validated request data to use case parameters"""
        return {
            'project_id': UUID(self.project_id),
            'completion_notes': self.completion_notes
        }
```


<div dir="rtl" style="text-align: right;">


تا زمانی که داده‌ها از طریق یک مدل درخواست به موارد استفاده ما برسند، هم اعتبار سنجی شده و هم به فرمت دقیقی که منطق دامنه ما انتظار دارد، تبدیل شده‌اند. این امر تفکیک نگرانی‌های معماری تمیز را حفظ می‌کند و اطمینان می‌دهد که جزئیات پیاده‌سازی لایه‌های بیرونی (مانند نحوه قالب‌بندی شناسه‌ها در درخواست‌های HTTP) هرگز به قوانین اصلی کسب‌وکار ما نشت نمی‌کنند.

### **مدل‌های پاسخ (Response models)**


</div>

```python
from dataclasses import dataclass
from typing import Optional

# Assuming Project, UserService are defined elsewhere
@dataclass(frozen=True)
class CompleteProjectResponse:
    """Data structure for project completion responses"""
    id: str
    status: str
    completion_date: str
    task_count: int
    completion_notes: Optional[str]

    @classmethod
    def from_entity(cls,
                    project: Any, # Should be Project
                    user_service: Any # Should be UserService
                    ) -> 'CompleteProjectResponse':
        """Create response from domain entities"""
        return cls(
            id=str(project.id),
            status=project.status,
            completion_date=project.completed_at,
            task_count=len(project.tasks),
            completion_notes=project.completion_notes,
        )
```


<div dir="rtl" style="text-align: right;">


متد `from_entity` چندین هدف کلیدی را برآورده می‌کند:

* از نمایش اشیای دامنه به لایه‌های خارجی محافظت می‌کند.
* دقیقاً کنترل می‌کند که کدام داده‌ها و در چه قالبی نمایش داده می‌شوند (مثلاً تبدیل UUIDها به رشته‌ها).
* یک نقطه سریال‌سازی ثابت برای تمام واسط‌های خارجی فراهم می‌کند.
* اجازه می‌دهد فیلدهای محاسباتی یا مشتق شده (مانند `task_count`) بدون تغییر اشیای دامنه اضافه شوند.
* داده‌های محاسباتی یا تجمعی را که در موجودیت پایه وجود ندارند، شامل می‌شود.
* با حذف مقادیر زیادی از داده‌های نامربوط، عملکرد را بهینه می‌کند.
* فراداده‌های (metadata) خاص عملیات را شامل می‌شود.

بیایید نسخه تکامل یافته‌ای از `CompleteProjectUseCase` را دوباره بررسی کنیم تا نشان دهیم چگونه مدل‌های درخواست، منطق دامنه، و مدل‌های پاسخ با هم کار می‌کنند:


</div>

```python
from dataclasses import dataclass
from typing import Any # Use Any for simplicity as full imports are not provided in source.
# Assuming ProjectRepository, TaskRepository, NotificationService, Result,
# CompleteProjectRequest, CompleteProjectResponse, ProjectNotFoundError, ValidationError, Error
# are defined elsewhere
@dataclass(frozen=True)
class CompleteProjectUseCase:
    project_repository: Any # Should be ProjectRepository
    task_repository: Any # Should be TaskRepository
    notification_service: Any # Should be NotificationService

    # Using CompleteProjectRequest vs discreet parameters
    def execute(self, request: Any) -> Any: # Should be request: CompleteProjectRequest -> Result
        try:
            params = request.to_execution_params()
            project = self.project_repository.get(params["project_id"])
            project.mark_completed(notes=params["completion_notes"])
            # Complete all outstanding tasks
            # ... Truncated for brevity
            self.project_repository.save(project)
            # using CompleteProjectResponse vs handbuilt dict
            response = CompleteProjectResponse.from_entity(project)

            return Result.success(response)
        except ProjectNotFoundError:
            return Result.failure(
                Error.not_found("Project", str(params["project_id"]))
            )
        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))
```


<div dir="rtl" style="text-align: right;">



در  **لایه آداپتورهای واسط (Interface Adapters layer)** ، این مدل‌های پاسخ می‌توانند توسط مؤلفه‌های مختلفی از جمله کنترل‌کننده‌های رسیدگی‌کننده به درخواست‌های HTTP، پردازشگرهای دستور رابط خط فرمان، یا کنترل‌کننده‌های صف پیام مصرف شوند. هر آداپتور می‌تواند داده‌های پاسخ را به طور مناسب برای مکانیزم انتقال خاص خود تبدیل کند، آن را به JSON از طریق HTTP، خروجی کنسول، یا بار پیام (message payloads) در صورت نیاز تبدیل کند.

---

### **حفظ تفکیک از نگرانی‌های خارجی (Maintaining separation from external concerns)**

در معماری تمیز (Clean Architecture)، حفظ **تفکیک نگرانی‌ها** (separation of concerns) برای انعطاف‌پذیری و نگهداری بلندمدت سیستم ما حیاتی است. در حالی که مدل‌های درخواست و پاسخ به مدیریت جریان داده در مرزهای لایه کاربردی کمک می‌کنند، روش‌های دیگری نیز برای محافظت از منطق اصلی کسب‌وکار ما در برابر جزئیات زیرساخت خارجی وجود دارد.

پورت‌ها (Ports) به لایه کاربردی اجازه می‌دهند تا دقیقاً قابلیت‌هایی را که از خدمات خارجی نیاز دارد مشخص کند، بدون اینکه به پیاده‌سازی‌های خاصی وابسته باشد. **خدمات خارجی** شامل:

* سرویس‌های ایمیل برای ارسال اعلان‌ها (مانند SendGrid یا AWS SES).
* سیستم‌های ذخیره‌سازی فایل برای پیوست‌ها (مانند AWS S3 یا Google Cloud Storage).
* سرویس‌های احراز هویت (مانند Auth0 یا Okta).
* خدمات یکپارچه‌سازی تقویم (مانند Google Calendar یا Microsoft Outlook).
* سیستم‌های پیام‌رسان خارجی (مانند Slack یا Microsoft Teams).

در حالی که مدل‌های درخواست/پاسخ و پورت‌ها هر دو برای حفظ مرزهای معماری تمیز عمل می‌کنند، آن‌ها جنبه‌های مختلفی از تعامل سیستم با دنیای خارج را پوشش می‌دهند. مدل‌های درخواست/پاسخ بر **تبدیل داده در مرزهای API** تمرکز دارند. پورت‌ها  **قراردادها را برای خدمات خارجی که لایه کاربردی ما به آن‌ها وابسته است** ، تعریف می‌کنند.

### **مرزهای واسط (Interface boundaries)**


</div>

```python
from abc import ABC, abstractmethod
from typing import Any # Use Any for simplicity as full imports are not provided in source.

# Assuming Task is defined elsewhere
class NotificationPort(ABC):
    """Port: Defines capability needed by Application Layer"""
    @abstractmethod
    def notify_task_completed(self, task: Any) -> None: # Should be task: Task
        """Notify when a task is completed"""
        pass

    # other capabilities as needed
    @abstractmethod
    def notify_task_high_priority(self, task: Any) -> None: # Should be task: Task
        """Notify when a task is set to high priority."""
        pass
```


<div dir="rtl" style="text-align: right;">


سپس، در هر مورد استفاده، ممکن است از پورت تعریف شده به این صورت استفاده کنیم:

محل دیاگرام Figure 7.6: Notification flow through architectural layers

این دنباله مدیریت دقیق وابستگی‌ها در معماری تمیز را نشان می‌دهد:

* مورد استفاده فقط در مورد `NotificationPort` انتزاعی اطلاعات دارد.
* پیاده‌سازی `SendGrid` مشخص در لبه سیستم ما قرار دارد.
* منطق کسب‌وکار کاملاً از جزئیات پیاده‌سازی ایمیل بی‌خبر است.
* یکپارچه‌سازی خدمات خاص (`SendGrid`) به طور تمیز در مرزهای معماری اتفاق می‌افتد.


</div>

```python
from dataclasses import dataclass
from uuid import UUID
from typing import Any # Use Any for simplicity as full imports are not provided in source.

# Assuming TaskRepository, NotificationPort, Result,
# SetTaskPriorityRequest, Error, ValidationError, TaskResponse, Priority
# are defined elsewhere
@dataclass
class SetTaskPriorityUseCase:
    task_repository: Any # Should be TaskRepository
    notification_service: Any # Should be NotificationPort # Depends on capability interface

    def execute(self, request: Any) -> Any: # Should be request: SetTaskPriorityRequest -> Result
        try:
            params = request.to_execution_params()
            task = self.task_repository.get(params['task_id'])
            task.priority = params['priority']
            self.task_repository.save(task)
            if task.priority == Priority.HIGH:
                self.notification_service.notify_task_high_priority(task)
            return Result.success(TaskResponse.from_entity(task))

        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))
```


<div dir="rtl" style="text-align: right;">


### **پشتیبانی از یکپارچه‌سازی اختیاری (Supporting optional integration)**

گاهی اوقات، یک مورد استفاده باید با خدمات خارجی ارتباط برقرار کند که در همه پیاده‌سازی‌های برنامه موجود نیستند. به عنوان مثال، یک برنامه مدیریت وظایف ممکن است **آنالیتیکس** (analytics) برای ردیابی تکمیل وظایف یا یک **سرویس ممیزی** (audit service) برای ثبت تغییرات مهم داشته باشد. این خدمات **اختیاری** هستند—هسته اصلی کسب‌وکار می‌تواند بدون آن‌ها کار کند. این خدمات در لایه خارجی Frameworks and Drivers قرار دارند، بنابراین باید از طریق یک واسط abstract به لایه Application (به سمت داخل) وابسته باشند.

**الگوی خدمات اختیاری (optional services pattern)** به مدیریت این موضوع کمک می‌کند:


</div>

```python
from dataclasses import dataclass, field
from uuid import UUID
from typing import Any, Optional

# Assuming TaskRepository, NotificationPort, Result, Task, TaskResponse, ValidationError, Error are defined elsewhere
@dataclass(frozen=True)
class TaskManagementUseCase:
    task_repository: Any # Should be TaskRepository
    notification_service: Any # Should be NotificationPort
    _optional_services: dict[str, Any] = field(default_factory=dict)

    def register_service(self, name: str, service: Any) -> None:
        """Register an optional service"""
        self._optional_services[name] = service

    def complete_task(self, task_id: UUID) -> Any: # Should be Result
        try:
            task = self.task_repository.get(task_id)
            task.complete()
            self.task_repository.save(task)
            # Required notification
            self.notification_service.notify_task_completed(task)
            # Optional integrations
            if analytics := self._optional_services.get('analytics'):
                analytics.track_task_completion(task.id)
            if audit := self._optional_services.get('audit'):
                audit.log_task_completion(task.id)
            return Result.success(TaskResponse.from_entity(task))

        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))
```


<div dir="rtl" style="text-align: right;">


استفاده از یک دیکشنری برای ذخیره خدمات اختیاری همراه با اجرای شرطی (مثلاً `if analytics := self._optional_services.get('analytics')`) یک الگوی تمیز برای مدیریت مناسب ویژگی‌هایی که ممکن است در هر استقرار وجود داشته باشند یا نباشند، فراهم می‌کند.

### **سازگاری با تغییرات سرویس (Adapting to service changes)**

هنگام یکپارچه‌سازی با خدمات شخص ثالث یا مدیریت ارتقاء سیستم، اغلب نیاز به جابجایی بین واسط‌های مختلف داریم. **الگوی آداپتور (adapter pattern)** به ما در مدیریت این موضوع کمک می‌کند:


</div>

```python
from typing import Any # Use Any for simplicity as full imports are not provided in source.
# Assuming NotificationPort, Task are defined elsewhere
class ModernNotificationService:
    """Third-party service with a different interface"""
    def send_notification(self, payload: dict) -> None:
        # Modern service implementation
        pass

class ModernNotificationAdapter(NotificationPort):
    """Adapts modern notification service to work with our interface"""
    def __init__(self, modern_service: ModernNotificationService):
        self._service = modern_service

    def notify_task_completed(self, task: Any) -> None: # Should be Task
        self._service.send_notification({
            "type": "TASK_COMPLETED",
            "taskId": str(task.id)
        })
```


<div dir="rtl" style="text-align: right;">


با استفاده از این الگوها با هم، می‌توانیم سیستم‌هایی ایجاد کنیم که به آرامی هم ویژگی‌های اختیاری و هم پیاده‌سازی‌های خدمات در حال تغییر را مدیریت می‌کنند در حالی که مرزهای معماری تمیز را حفظ می‌کنند.

---

در این فصل، **لایه کاربردی** معماری تمیز را بررسی کردیم و بر نحوه هماهنگی اشیای دامنه و همکاری با خدمات خارجی برای برآورده کردن نیازهای کاربر تمرکز کردیم. آموختیم که چگونه موارد استفاده را پیاده‌سازی کنیم که مرزهای معماری تمیز را حفظ کرده و در عین حال عملکرد معنی‌داری ارائه دهند.

با استفاده از سیستم مدیریت وظایف به عنوان مثال، نحوه ایجاد تعامل‌کننده‌های مورد استفاده را کشف کردیم که اشیای دامنه را هماهنگ می‌کنند در حالی که به **قانون وابستگی** معرفی شده در فصل 1 احترام می‌گذارند. ما بر مبنای **اصول SOLID** از فصل 2 و **الگوهای آگاهی از نوع** از فصل 3 ساختیم تا پیاده‌سازی‌های قوی و قابل نگهداری ایجاد کنیم. موارد استفاده ما به طور مؤثری اشیای دامنه و خدماتی را که در فصل 4 توسعه دادیم، هماهنگ می‌کنند و نشان می‌دهند که چگونه لایه‌های معماری تمیز به طور هماهنگ با هم کار می‌کنند.

چندین الگوی کلیدی و مفهوم را پیاده‌سازی کردیم:

* تعامل‌کننده‌های مورد استفاده که عملیات دامنه را هماهنگ می‌کنند.
* مدل‌های درخواست و پاسخ که مرزهای واضحی ایجاد می‌کنند.
* الگوهای رسیدگی به خطا که تفکیک معماری را حفظ می‌کنند.
* تعاریف واسط که نگرانی‌های خارجی را جدا نگه می‌دارند.

این پیاده‌سازی‌ها نشان دادند که چگونه یکپارچگی معماری خود را حفظ کنیم در حالی که سیستمی را می‌سازیم که به طور یکپارچه نیازهای کسب‌وکار را برآورده می‌کند.

در فصل بعدی، **لایه آداپتورهای واسط (The Interface Adapters Layer)** را بررسی خواهیم کرد. در آنجا، یاد خواهیم گرفت که چگونه کنترل‌کننده‌ها و ارائه‌دهنده‌ها (presenters) را ایجاد کنیم که داده‌ها را بین لایه‌های داخلی و خارجی سیستم ما ترجمه می‌کنند.

### **مطالعه بیشتر (Further reading)**

برای کسب اطلاعات بیشتر در مورد موضوعاتی که در این فصل پوشش داده شده‌اند، به منابع زیر مراجعه کنید:

* **Building Microservices: Designing Fine-Grained Systems** اثر Sam Newman. اگرچه این کتاب بر میکروسرویس‌ها تمرکز دارد، اما فصل‌های آن در مورد مرزهای سرویس، ارتباطات بین سرویس‌ها و رسیدگی به داده‌ها، بینش‌های ارزشمندی را برای ایجاد مرزهای با دقت تعریف شده در لایه‌های کاربردی فراهم می‌کند و می‌تواند در برنامه‌های monolithic نیز اعمال شود.
* **Hexagonal Architecture** اثر Alistair Cockburn. این مقاله الگوی پورت‌ها و آداپتورها (یا معماری شش‌ضلعی) را توضیح می‌دهد، که بسیار مکمل اصول معماری تمیز است. این مقاله درک روشنی از مدیریت وابستگی‌ها و ترجمه مرزها را فراهم می‌کند، که برای پیاده‌سازی لایه کاربردی بسیار مهم هستند.
