from celery import shared_task

# دقیقا تسک های ککه درون جنگو داریم را باید اینجا کپی پیست کنیم
#  به ازای هر اپ و هر تسک در پروژه جنگو باید مشابه انرا در ورکر سلری داشته باشیم


@shared_task
def send_discount_emails():
    pass

@shared_task
def process_data_for_lm():
    pass