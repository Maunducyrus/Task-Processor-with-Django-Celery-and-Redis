from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .tasks import sample_task

def trigger_task(request):
    sample_task.delay("Cyrus")
    return JsonResponse({"message": "Task has been triggered!"})

