from celery import shared_task
import time

@shared_task(bind=True)
def sample_task(self):
    time.sleep(5)
    return f"Task {self.request.id} completed!"
