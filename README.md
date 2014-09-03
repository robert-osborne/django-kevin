Custom Django 1.6 Template
==========================

A personalized project template for Django 1.6 using postgres for development and production. Ready to deploy on Heroku.

Forked from the original [django-two-scoops-project](https://github.com/twoscoops/django-twoscoops-project).

Creating Your Project
=====================

*Prerequisites: python, pip, django*

To create a new Django project, run the following command replacing `{{ project_name }}` with your actual project name:

    django-admin.py startproject --template=https://github.com/imkevinxu/django-twoscoops-project/archive/master.zip --extension=py,md,html,json,tmp --name=Procfile,Procfile.dev {{ project_name }}

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
    echo CACHE=dummy >> .env.dev

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

First step is to deploy to Heroku with the `post_compile` script in bin/ so that node functions can be installed for python to call them.

    git init
    git add .
    git commit -m "ready for heroku deploy"
    heroku create
    heroku config:push
    git push heroku master

After `post_compile` is done, uncomment line 108 in `/{{ project_name }}/config/settings/base.py` to enable django-pipeline.

    git commit -am "enabled django-pipeline"
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

Add-ons
=======

Redis Cloud
-----------
In order to enable redis for caching and queues, add [Redis Cloud](https://devcenter.heroku.com/articles/rediscloud) to Heroku.

    heroku addons:add rediscloud:25

Redis Queue
-----------
Turn on background job worker queue with this one-liner:

    heroku scale worker=1

Amazon S3
---------
To use Amazon S3 as a static and media file storage, create a custom Group and User via IAM and then a custom static bucket and media bucket with public read policies.

Add the following config variables to Heroku:

    heroku config:set AWS_ACCESS_KEY_ID=INSERT_ACCESS_KEY_ID
    heroku config:set AWS_SECRET_ACCESS_KEY=INSERT_SECRET_ACCESS_KEY
    heroku config:set AWS_STATIC_STORAGE_BUCKET_NAME={{ project_name }}-static
    heroku config:set AWS_MEDIA_STORAGE_BUCKET_NAME={{ project_name }}-media

Third-party plugins used
========================

Currently using [Django 1.6.6](https://docs.djangoproject.com/en/1.6/) and [Node 0.10.x](http://nodejs.org/api/)

base.txt
--------
- [South 1.0](http://south.readthedocs.org/en/latest/index.html) - database migrations
- [bpython 0.13.1](http://docs.bpython-interpreter.org/) - advanced python interpreter/REPL
- [dj-static 0.0.6](https://github.com/kennethreitz/dj-static) - serve production static files with Django
- [django-authtools 1.0.0](http://django-authtools.readthedocs.org/en/latest/) - custom User model classes such as `AbstractEmailUser` and `AbstractNamedUser`
- [django-braces 1.4.0](http://django-braces.readthedocs.org/en/v1.4.0/) - lots of custom mixins
- [django-extensions 1.3.9](http://django-extensions.readthedocs.org/en/latest/) - useful command line extensions (`shell_plus`, `create_command`, `export_emails`)
- [django-floppyforms 1.2.0](http://django-floppyforms.readthedocs.org/en/latest/) - control of output of form rendering
- [django-jsonview 0.4.3](https://github.com/jsocol/django-jsonview) - return python objects as JSON
- [django-model-utils 2.2](https://django-model-utils.readthedocs.org/en/latest/) - useful model mixins and utilities such as `TimeStampedModel` and `Choices`
- [django-pipeline 1.3.25](http://django-pipeline.readthedocs.org/en/latest/) - CSS and JS compressor and compiler. Also minifies HTML
- [django-redis 3.7.1](https://django-redis.readthedocs.org/en/latest/) - enables redis cacheing
- [psycopg2 2.5.3](http://pythonhosted.org//psycopg2/) - PostgreSQL adapter
- [pytz 2014.4](http://pytz.sourceforge.net/) - world timezone definitions
- [requests 2.4.0](http://docs.python-requests.org/en/latest/) - HTTP request API
- [rq 0.4.6](http://python-rq.org/) - background tasks using redis as queue
- [static 1.0.2](https://github.com/lukearno/static) - serves static and dynamic content

local.txt
---------
- [Werkzeug 0.9.6](http://werkzeug.pocoo.org/) - WSGI utility library with powerful debugger
- [django-debug-toolbar 1.2.1](http://django-debug-toolbar.readthedocs.org/en/1.2/) - debug information in a toolbar

production.txt
--------------
- [boto 2.32.1](https://boto.readthedocs.org/en/latest/) - Python interface to AWS
- [dj-database-url 0.3.0](https://github.com/kennethreitz/dj-database-url) - allows Django to use database URLs for Heroku
- [django-storages 1.1.8](http://django-storages.readthedocs.org/en/latest/index.html) - custom storage backends; using S3
- [gunicorn 19.1.0](https://github.com/benoitc/gunicorn) - production WSGI server with workers

test.txt
--------
- [coverage 3.7.1](http://nedbatchelder.com/code/coverage/) - measures code coverage

package.json
------------
- [yuglify 0.1.4](https://github.com/yui/yuglify) - uglifyJS and cssmin compressor

Acknowledgements
================

![Two Scoops of Django](http://twoscoops.smugmug.com/Two-Scoops-Press-Media-Kit/i-C8s5jkn/0/O/favicon-152.png "Two Scoops Logo")

This project follows best practices as espoused in [Two Scoops of Django: Best Practices for Django 1.6](http://twoscoopspress.org/products/two-scoops-of-django-1-6).

Many thanks to:
---------------

- Daniel Greenfield and Audrey Roy for writing the book
- Randall Degges for django-skel
- All of the [contributors](https://github.com/twoscoops/django-twoscoops-project/blob/master/CONTRIBUTORS.txt) to the original fork
