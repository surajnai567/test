from celery import Celery
import os

# BROKER_URL = os.environ.get("BROKER_URL")
BROKER_URL = "redis://localhost:6379/1"

celery_app = Celery(
    "worker",
    broker=BROKER_URL,
    include=['worker.celery_worker']
)
