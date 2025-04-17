from django.http import JsonResponse
from django.shortcuts import render
from .models import TaskLog
from tasks.tasks import sample_task  # <-- celery task

def task_logs_page(request):
    return render(request, "tasklogs.html")

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

def trigger_task(request):
    name = request.GET.get('name', 'Anonymous')
    task = sample_task.delay(name)

    TaskLog.objects.create(
        task_id=task.id,
        # task_name='sample_task',
        task_name=f"sample_task({name})",
        status='PENDING'
    )

    return JsonResponse({
        'message': 'Task has been triggered!',
        'task_id': task.id
    })
