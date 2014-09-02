web: gunicorn {{ project_name }}.config.wsgi --workers $WEB_CONCURRENCY
worker: python -u {{ project_name }}/worker.py
