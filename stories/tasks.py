import time
from celery import shared_task
from celery import schedules

@shared_task
def export(a):
    print("Start Exporting data...")
    time.sleep(a)
    print("Exporting data completed!")







