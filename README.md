========================
django-twoscoops-project
========================

A customized project template for Django 1.6 using postgres for development and production. Ready to deploy on Heroku.

To use this project follow these steps:

1. Create the new project using the django-two-scoops template
2. Create dev and prod virtual environments
3. Install dependences for both dev and prod

*note: these instructions show creation of a project called "icecream". You
should replace this name with the actual name of your project.*

Creating your project
=====================

To create a new Django project called '**icecream**' using django-twoscoops-project, run the following command:

    $ django-admin.py startproject --template=https://github.com/imkevinxu/django-twoscoops-project/archive/master.zip --extension=py,rst,html icecream

Virtual Environments
====================

In Linux and Mac OSX, you can install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/), which will take care of managing your virtual environments and adding the project path to the `site-directory` for you:

    $ cd icecream
    $ mkvirtualenv icecream-dev && add2virtualenv `pwd` && deactivate
    $ mkvirtualenv icecream-prod && add2virtualenv `pwd` && deactivate

Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development:

    $ pip install -r requirements/local.txt

For production:

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Follows Best Practices
======================

![Two Scoops of Django](http://twoscoops.smugmug.com/Two-Scoops-Press-Media-Kit/i-C8s5jkn/0/O/favicon-152.png "Two Scoops Logo")

This project follows best practices as espoused in [Two Scoops of Django: Best Practices for Django 1.6](http://twoscoopspress.org/products/two-scoops-of-django-1-6).

Acknowledgements
================

- Many thanks to Randall Degges for the inspiration to write the book and django-skel.
- All of the [contributors](https://github.com/twoscoops/django-twoscoops-project/blob/master/CONTRIBUTORS.txt) to this project.
