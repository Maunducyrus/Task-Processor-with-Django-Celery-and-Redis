from django.http import JsonResponse
from .models import TaskLog

def task_logs_api(request):
    logs = TaskLog.objects.all().order_by('-created_at')
    data = [
        {
            "task_id": log.task_id,
            "name": log.name,
            "status": log.status,
            "result": log.result,
            "created_at": log.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for log in logs
    ]
    return JsonResponse(data, safe=False)
