from django.http import JsonResponse
from celery.result import AsyncResult
from celery import states
from taskprocessor.celery import app

def check_task_status(request, task_id):
    result = AsyncResult(task_id, app=app)
    response_data = {
        'task_id': task_id,
        'status': result.status,
    }

    # Only include result if it's JSON serializable
    if result.ready():
        try:
            response_data['result'] = result.result  # This might raise error if result is an Exception
        except Exception as e:
            response_data['result'] = str(e)

    return JsonResponse(response_data)
