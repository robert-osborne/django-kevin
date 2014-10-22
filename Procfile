web: gunicorn config.wsgi --workers $WEB_CONCURRENCY --pythonpath $PYTHONPATH
worker: django-admin.py rqworker high default low
scheduler: rqscheduler --url $REDISCLOUD_URL
