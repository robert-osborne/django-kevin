from __future__ import absolute_import

from .base import *

########## IN-MEMORY TEST DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'test.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
########## END IN-MEMORY TEST DATABASE


########## TEST RUNNER CONFIGURATION
# https://github.com/django-nose/django-nose
INSTALLED_APPS += (
    'django_nose',
)

TEST = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--where=%s' % basename(PROJECT_ROOT),
    '--exclude-dir=%s' % join(CONFIG_ROOT, 'settings'),
]
########## END TEST RUNNER CONFIGURATION
