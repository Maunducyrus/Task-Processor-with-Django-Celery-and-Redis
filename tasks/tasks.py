# from celery import shared_task
# from .models import TaskLog

# @shared_task(bind=True)
# def sample_task(self, name):
#     try:
#         result = f"Task completed for {name}"

#         TaskLog.objects.create(
#             task_id=self.request.id,
#             task_name=self.name,
#             status="SUCCESS",
#             result=result
#         )

#         return result

#     except Exception as e:
#         TaskLog.objects.create(
#             task_id=self.request.id,
#             task_name=self.name,
#             status="FAILURE",
#             result=str(e)
#         )
#         raise e

from celery import shared_task
from .models import TaskLog

@shared_task(bind=True)
def sample_task(self, name):
    result = f"Task completed for {name}"

    # Log to DB
    TaskLog.objects.create(
        task_id=self.request.id,
        task_name='sample_task',
        status='SUCCESS',
        result=result,
    )

    return result
