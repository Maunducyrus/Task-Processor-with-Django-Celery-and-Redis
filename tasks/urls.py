from django.urls import path
from .views import task_logs_page

urlpatterns = [
    path('logs/', task_logs_page, name='task-logs-page'),
]
