# taskprocessor/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskprocessor.settings')

app = Celery('taskprocessor')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
