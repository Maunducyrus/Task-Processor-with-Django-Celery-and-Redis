from django.contrib import admin
from .models import TaskLog

@admin.register(TaskLog)
class TaskLogAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'task_name', 'status', 'created_at')
    search_fields = ('task_id', 'task_name')

