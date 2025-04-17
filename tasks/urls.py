from django.urls import path
from .views import trigger_task, check_task_status

urlpatterns = [
    path('trigger-task/', trigger_task, name='trigger-task'),
    path('task-status/<str:task_id>/', check_task_status, name='task-status'),
]
