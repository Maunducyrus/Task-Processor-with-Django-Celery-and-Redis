# Create your models here.

from django.db import models

class TaskLog(models.Model):
    task_id = models.CharField(max_length=255, unique=True)
    task_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    result = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task_name} - {self.status}"

