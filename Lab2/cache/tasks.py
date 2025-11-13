from celery import shared_task
import time

@shared_task
def long_task_one():
    time.sleep(5)
    print("Task One Completed")
    return "Task One Done"

@shared_task
def long_task_two():
    time.sleep(10)
    print("Task Two Completed")
    return "Task Two Done"
