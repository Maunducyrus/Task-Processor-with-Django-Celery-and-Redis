# tasks/tasks.py
from celery import shared_task
import time

@shared_task
def sample_task(name):
    print(f"Processing task for {name}")
    time.sleep(5)
    return f"Task completed for {name}"
