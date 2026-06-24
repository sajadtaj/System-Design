
"""
ماژول سفارشی‌سازی مجوزها برای API وبلاگ.

این ماژول کلاس‌های مجوز سفارشی را ارائه می‌دهد که قابلیت‌های داخلی
Django REST Framework را برای پیاده‌سازی کنترل دسترسی دقیق در سطح پست‌های وبلاگ توسعه می‌دهند.

کلاس‌ها:
    IsAuthorOrReadOnly: یک کلاس مجوز سفارشی که دسترسی فقط خواندنی را به همه کاربران
        می‌دهد و عملیات نوشتن، بروزرسانی و حذف را به نویسنده اصلی پست محدود می‌کند.

ویژگی‌ها:
    - کاربران احراز هویت‌نشده: فقط می‌توانند پست‌ها را بخوانند (GET, HEAD, OPTIONS)
    - کاربران احراز هویت‌شده: می‌توانند همه پست‌ها را بخوانند اما فقط پست‌های خود را ویرایش کنند
    - نویسندگان: دسترسی کامل CRUD به پست‌های خود دارند

مثال:
    from rest_framework import viewsets
    from .permissions import IsAuthorOrReadOnly

    class PostViewSet(viewsets.ModelViewSet):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = [IsAuthorOrReadOnly]

    تنظیمات فوق تضمین می‌کند که:
    - GET /posts/ - همه کاربران می‌توانند لیست را ببینند
    - GET /posts/1/ - همه کاربران می‌توانند پست خاصی را ببینند
    - POST /posts/ - فقط کاربران احراز هویت‌شده
    - PUT/PATCH /posts/1/ - فقط نویسنده می‌تواند بروزرسانی کند
    - DELETE /posts/1/ - فقط نویسنده می‌تواند حذف کند

ملاحظات امنیتی:
    - همیشه با سیستم احراز هویت جنگو استفاده شود
    - مطمئن شوید که user.is_authenticated به درستی از طریق
      SessionAuthentication یا TokenAuthentication تنظیم شده است
    - ماژول فرض می‌کند obj.author یک ForeignKey به مدل User جنگو است
    - در صورت احراز هویت‌نشده بودن کاربر برای متدهای غیرایمن، خطای 403 Forbidden برمی‌گرداند
    - اگر کاربر احراز هویت‌شده نویسنده نباشد، خطای 403 Forbidden برمی‌گرداند

پیش‌نیازها:
    - Django REST Framework (rest_framework)
    - Middleware احراز هویت جنگو

تاریخچه نسخه‌ها:
    - 1.0.0: پیاده‌سازی اولیه (2024)
    - 1.1.0: رفع اشتباه تایپی در has_object_permission (request.use -> request.user)

مجوز: MIT
نویسنده: نام شما
"""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    مجوز سفارشی برای اجازه دسترسی فقط خواندنی به همه کاربران و
    دسترسی کامل CRUD فقط به نویسنده پست.

    قوانین مجوز:
        - has_permission (سطح ویو):
            - اجازه دسترسی به همه کاربران احراز هویت‌شده
            - عدم اجازه دسترسی به کاربران احراز هویت‌نشده

        - has_object_permission (سطح شیء):
            - اجازه SAFE_METHODS (GET, HEAD, OPTIONS) به همه
            - اجازه عملیات نوشتن (POST, PUT, PATCH, DELETE) فقط به نویسنده

    کاربرد:
        از این کلاس مجوز در ModelViewSet یا APIView استفاده کنید تا اطمینان حاصل شود
        کاربران فقط می‌توانند محتوای خود را ویرایش کنند.

    نکته:
        مجوز سطح شیء (has_object_permission) فقط توسط ویوهای عمومی DRF
        هنگام دریافت یک شیء خاص فراخوانی می‌شود. برای ویوهای لیست،
        فقط has_permission فراخوانی می‌شود.
    """

    def has_permission(self, request, view, *args, **kwargs):
        """
        بررسی می‌کند که آیا کاربر مجوز دسترسی به ویو را دارد یا خیر.

        این متد برای هر درخواست فراخوانی می‌شود تا مشخص کند کاربر
        اصلاً اجازه دسترسی به endpoint را دارد یا نه.

        آرگومان‌ها:
            request: شیء درخواست HTTP
            view: کلاس ویویی که در حال دسترسی به آن هستیم
            *args: آرگومان‌های موقعیتی اضافی
            **kwargs: آرگومان‌های کلیدی اضافی

        خروجی:
            bool: اگر کاربر احراز هویت شده باشد True، در غیر این صورت False

        مثال:
            - یک کاربر احراز هویت‌شده می‌تواند به هر ویوی پست دسترسی داشته باشد
            - یک کاربر احراز هویت‌نشده خطای 403 Forbidden دریافت می‌کند
        """
        # فقط کاربران احراز هویت‌شده می‌توانند ویو لیست را ببینند
        if request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        بررسی می‌کند که آیا کاربر مجوز انجام عملیات روی یک شیء خاص را دارد یا نه.

        این متد برای درخواست‌های GET, PUT, PATCH, DELETE روی
        اشیاء خاص فراخوانی می‌شود (نه برای ویوهای لیست).

        منطق مجوز:
            1. متدهای ایمن (GET, HEAD, OPTIONS): اجازه دسترسی به همه
            2. متدهای غیرایمن (POST, PUT, PATCH, DELETE): فقط به نویسنده اجازه دهد

        آرگومان‌ها:
            request: شیء درخواست HTTP
            view: کلاس ویویی که در حال دسترسی به آن هستیم
            obj: نمونه شیء در حال دسترسی (مثلاً یک شیء Post)

        خروجی:
            bool:
                - اگر متد ایمن باشد (فقط خواندنی) True برمی‌گرداند
                - اگر کاربر جاری نویسنده شیء باشد True برمی‌گرداند
                - در غیر این صورت False برمی‌گرداند

        مثال:
            - GET /posts/1/ -> همیشه مجاز است (فقط خواندنی)
            - PUT /posts/1/ -> فقط اگر request.user == obj.author مجاز است
            - DELETE /posts/1/ -> فقط اگر request.user == obj.author مجاز است

        نکته امنیتی:
            فیلد 'author' باید روی مدل شیء وجود داشته باشد و باید
            یک ForeignKey به مدل User جنگو باشد.
        """
        # مجوزهای خواندنی به همه درخواست‌ها داده می‌شود پس همیشه
        # متدهای GET, HEAD, یا OPTIONS را مجاز می‌دانیم
        if request.method in permissions.SAFE_METHODS:
            return True
        # مجوزهای نوشتنی فقط به نویسنده پست داده می‌شود
        return obj.author == request.user  # اصلاح شده: 'request.use' -> 'request.user'