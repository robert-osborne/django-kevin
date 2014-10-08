web: gunicorn config.wsgi --workers $WEB_CONCURRENCY --pythonpath $PYTHONPATH
worker: python -u {{ project_name }}/config/worker.py
