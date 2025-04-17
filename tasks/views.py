from django.shortcuts import render
from .models import TaskLog

def task_logs_page(request):
    logs = TaskLog.objects.all().order_by('-created_at')
    return render(request, 'tasklogs.html', {'logs': logs})
