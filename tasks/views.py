from django.shortcuts import render
from .models import TaskLog
from django.http import JsonResponse
from .tasks import sample_task

def trigger_task(request):
    name = request.GET.get("name", "User")
    task = sample_task.delay(name)
    return JsonResponse({"message": "Task has been triggered!", "task_id": task.id})


def task_logs_page(request):
    logs = TaskLog.objects.all().order_by('-created_at')
    return render(request, 'tasklogs.html', {'logs': logs})
