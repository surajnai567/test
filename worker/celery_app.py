from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.task_routes = {
    "worker.celery_worker.test_celery": "test-queue"}
celery_app.conf.update(task_track_started=True)