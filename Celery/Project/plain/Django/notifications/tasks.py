from celery import shared_task
import time

# تسکهای را که در تمام برزنامه داریم اینجا مسیردهی میکنیم
# تا توسط صف رمبوطه پردازش شوند
# مقادیر صف را داکرکمپوز برای ایمیج ها مشخص کردیم
# command: uv run celery --app=config worker -l INFO -Q celery,celery:1,celery:2,celery:3



@shared_task()
def task_1(queue='celery'):
    time.sleep(3)
    return


@shared_task(task_rate_limit='1/m')
def task_2(queue='celery:1'):
    time.sleep(3)
    return


@shared_task()
def task_3(queue='celery:2'):
    time.sleep(3)
    return


@shared_task()
def task_4(queue='celery:3'):
    time.sleep(3)
    return


