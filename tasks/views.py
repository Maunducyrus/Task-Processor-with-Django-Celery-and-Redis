from django.http import JsonResponse
from .tasks import sample_task

def trigger_task(request):
    task = sample_task.delay()
    return JsonResponse({
        'message': 'Task has been triggered!',
        'task_id': task.id
    })
