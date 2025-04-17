from django.urls import path
from .views import task_logs_page, trigger_task

urlpatterns = [
    path('logs/', task_logs_page, name='task-logs-page'),
    path('trigger-task/', trigger_task, name='trigger-task'),
]
