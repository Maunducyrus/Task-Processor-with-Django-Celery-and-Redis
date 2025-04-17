from django.http import JsonResponse
from celery.result import AsyncResult
from .tasks import sample_task
from taskprocessor.celery import app  # Update if your project name is different


# View 1: Trigger the asynchronous task
def trigger_task(request):
    task = sample_task.delay()
    return JsonResponse({
        'message': 'Task has been triggered!',
        'task_id': task.id
    })


# View 2: Check the status of a given task ID
def check_task_status(request, task_id):
    task_result = AsyncResult(task_id, app=app)
    return JsonResponse({
        'task_id': task_id,
        'status': task_result.status,
        'result': task_result.result
    })
