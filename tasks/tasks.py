from celery import shared_task
from .models import TaskLog

@shared_task(bind=True)
def sample_task(self, name):
    task_log, created = TaskLog.objects.get_or_create(
        task_id=self.request.id,
        defaults={"task_name": self.name, "status": "STARTED"}
    )

    try:
        result = f"Task completed for {name}"
        task_log.status = "SUCCESS"
        task_log.result = result
        task_log.save()
        return result

    except Exception as e:
        task_log.status = "FAILURE"
        task_log.result = str(e)
        task_log.save()
        raise
