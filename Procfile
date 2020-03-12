web: gunicorn -w 3 -k uvicorn.workers.UvicornWorker src.main:app
worker: celery worker -A worker.celery_app.celery_app -l INFO


