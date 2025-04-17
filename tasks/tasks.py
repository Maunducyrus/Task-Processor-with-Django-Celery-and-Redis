from celery import shared_task
import time

@shared_task
def sample_task(name="default"):
    print(f"Processing task for {name}")
    return f"Hello, {name}! Task completed successfully."
