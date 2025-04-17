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
from tasks.models import TaskLog

@shared_task(bind=True)
def sample_task(self, name):
    # result = f"Task completed for {name}"
    result_message = f"Task completed for {name}"
    
    # Update the result/status in DB
    TaskLog.objects.filter(task_id=self.request.id).update(
        status='SUCCESS',
        result=result_message
    )
    
    return result_message
