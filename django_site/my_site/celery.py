import os
from celery import Celery
from django.post_request_task.task import PostRequestTask
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
# os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('my_site', task_cls=PostRequestTask)

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# lambda: settings.INSTALLED_APPS
