from django.urls import path
from .views import trigger_task

urlpatterns = [
    path('trigger-task/', trigger_task, name='trigger-task'),
]
