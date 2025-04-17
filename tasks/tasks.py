from celery import shared_task

@shared_task
def sample_task(name="Cyrus"):
    print(f"Processing task for {name}")
    return f"Hello, {name}! Task completed successfully."
