from celery import Celery

app = Celery("task")

app.config_from_object("celery_config")



app.conf.imports = ('notifications.tasks',)
app.autodiscover_tasks()