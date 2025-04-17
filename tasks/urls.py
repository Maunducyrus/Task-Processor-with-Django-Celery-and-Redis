from django.urls import path
from .views import task_logs_page
from . import views

urlpatterns = [
    path('logs/', task_logs_page, name='task-logs-page'),
    # path('trigger-task/', trigger_task, name='trigger-task'),
    path("api/logs/", views.task_logs_api, name="task-logs-api"),
]
