import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')




# تسکهای را که در تمام برزنامه داریم اینجا مسیردهی میکنیم
# تا توسط صف رمبوطه پردازش شوند
# مقادیر صف را داکرکمپوز برای ایمیج ها مشخص کردیم
# command: uv run celery --app=config worker -l INFO -Q queue1
# command: uv run celery --app=celery_base worker -l INFO -Q queue2

# app.conf.task_routes ={
#     'notifications.tasks.send_discount_emails':{'queue':'queue1'},
#     'notifications.tasks.process_data_for_lm': {'queue':'queue2'}
# }

app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}


app.autodiscover_tasks()