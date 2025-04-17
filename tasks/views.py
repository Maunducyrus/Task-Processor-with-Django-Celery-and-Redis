# tasks/views.py
from django.http import JsonResponse
from tasks.tasks import sample_task
from celery.result import AsyncResult
from taskprocessor.celery import app  # make sure this matches your actual celery app path

# This view triggers the task
def trigger_task(request):
    task = sample_task.delay()
    return JsonResponse({"message": "Task has been triggered!", "task_id": task.id})

# This view checks the task status
def check_task_status(request, task_id):
    result = AsyncResult(task_id, app=app)
    return JsonResponse({
        "task_id": task_id,
        "state": result.state,
        "result": str(result.result) if result.result else None
    })
