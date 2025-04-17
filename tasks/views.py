from django.http import JsonResponse
from .models import TaskLog
from django.shortcuts import render

def task_logs_api(request):
    logs = TaskLog.objects.order_by('-created_at')[:10]
    data = [
        {
            'task_id': log.task_id,
            'task_name': log.task_name,
            'status': log.status,
            'result': log.result,
            'created_at': log.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for log in logs
    ]
    return JsonResponse(data, safe=False)

def task_logs_page(request):
    return render(request, "tasklogs.html")
