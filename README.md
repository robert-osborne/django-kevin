Custom Django 1.6 Template
==========================

A personalized project template for Django 1.6 using postgres for development and production. Ready to deploy on Heroku.

Forked from the original [django-two-scoops-project](https://github.com/twoscoops/django-twoscoops-project).

Creating Your Project
=====================

*Prerequisites: python, pip, django*

To create a new Django project, run the following command replacing `{{ project_name }}` with your actual project name:

    django-admin.py startproject --template=https://github.com/imkevinxu/django-twoscoops-project/archive/master.zip --extension=py,md,html --name=Procfile {{ project_name }}

Make virtual environments
-------------------------

*Prerequisites: virtualenv, virtualenvwrapper*

    cd {{ project_name }}
    mkvirtualenv {{ project_name }}-dev && add2virtualenv `pwd`
    mkvirtualenv {{ project_name }}-prod && add2virtualenv `pwd`

Install python packages
-----------------------

For development:

    workon {{ project_name }}-dev
    pip install -r requirements/local.txt

For production:

    workon {{ project_name }}-prod
    pip install -r requirements.txt

Development Mode
================

Set .env.dev variable for dev
--------------------------

The environment variables for development sets the appropriate DJANGO_SETTINGS_MODULE and PYTHONPATH in order to use django-admin.py seemlessly. Necessary for Foreman and other worker processes

*.env.dev is not version controlled so the first person to create this project needs to create a .env.dev file for Foreman to read into the environment. Future collaboraters need to email the creator for it.*

    echo DJANGO_SETTINGS_MODULE=config.settings.local >> .env.dev
    echo PYTHONPATH={{ project_name }} >> .env.dev
    echo PYTHONUNBUFFERED=True >> .env.dev
    echo DUMMY_CACHE=True >> .env.dev

Create local postgres database for dev
--------------------------------------

*Prerequisites: Postgres and Heroku Toolbelt*

Install Postgres for your OS [here](http://www.postgresql.org/download/). For Max OSX the easiest option is to download and run [Postgres.app](http://postgresapp.com/).

    # Make sure Postgres.app is running
    workon {{ project_name }}-dev
    createdb {{ project_name }}
    foreman run django-admin.py syncdb --noinput

Run project locally in dev environment
--------------------------------------

Recommended to use foreman to start processes:

*By default, .foreman uses the development versions of .env and Procfile*

    foreman start

To run one-off commands use:

    foreman run django-admin.py COMMAND

Production Mode
===============

Set .env variable for prod
--------------------------

The environment variables for production must contain a separate SECRET_KEY for security and the appropriate DJANGO_SETTINGS_MODULE and PYTHONPATH in order to use django-admin.py seemlessly. Hacky use of `date | md5` to generate a pseudo-random string.

*.env is not version controlled so the first person to create this project needs to create a .env file for Foreman and Heroku to read into the environment. Future collaboraters need to email the creator for it.*

    echo "SECRET_KEY=`date | md5`" >> .env
    echo "DJANGO_SETTINGS_MODULE=config.settings.production" >> .env
    echo "PYTHONPATH={{ project_name }}" >> .env
    echo "WEB_CONCURRENCY=3" >> .env
    echo "PYTHONUNBUFFERED=True" >> .env

Deploy to Heroku
----------------

*Prerequisites: Heroku Toolbelt and heroku-config*

    git init
    git add .
    git commit -m "ready for heroku deploy"
    heroku create
    heroku config:push
    git push heroku master
    heroku run django-admin.py syncdb --noinput
    heroku run django-admin.py migrate
    heroku open

Run project locally in prod environment
---------------------------------------

This is meant to mimic production as close as possible using both the production database and environment settings so proceed with caution.

*Make sure to edit the .foreman file to use production versions of .env and Procfile*

    workon {{ project_name }}-prod
    heroku config:pull
    foreman run django-admin.py collectstatic --noinput
    foreman start

Suggestions
===========

Third-party plugins
-------------------

- [Celery](http://www.celeryproject.org/) for asynchronous tasks and cron jobs
- [Redis](http://redis.io/) as a backend for Celery and for caching, auto-completion, sessions, etc.
- [Memcached](http://memcached.org/) for caching
- [Varnish](https://www.varnish-cache.org/) for HTTP caching
- [Fabric](http://www.fabfile.org/) for deployment scripts
- [New Relic](http://newrelic.com/) for application monitoring
- [Sentry](https://getsentry.com/welcome/) for exception handling
- [PG Backups](https://addons.heroku.com/pgbackups) for PostgreSQL backups
- [django-storages](http://django-storages.readthedocs.org/en/latest/) for CDN static storage

Django core functions
---------------------

- Use named URLs, reverse, and the url template tag
- Use django management commands for scripting

Acknowledgements
================

![Two Scoops of Django](http://twoscoops.smugmug.com/Two-Scoops-Press-Media-Kit/i-C8s5jkn/0/O/favicon-152.png "Two Scoops Logo")

This project follows best practices as espoused in [Two Scoops of Django: Best Practices for Django 1.6](http://twoscoopspress.org/products/two-scoops-of-django-1-6).

Many thanks to:
---------------

- Daniel Greenfield and Audrey Roy for writing the book
- Randall Degges for django-skel
- All of the [contributors](https://github.com/twoscoops/django-twoscoops-project/blob/master/CONTRIBUTORS.txt) to the original fork
