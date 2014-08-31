"""Production settings and globals."""

from __future__ import absolute_import

from core.utils import get_env_setting

from .base import *


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECURE_PROXY_SSL_HEADER
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['example.com', 'localhost', '127.0.0.1']
########## END HOST CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
# EMAIL_HOST = get_env_setting('EMAIL_HOST')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
# EMAIL_HOST_PASSWORD = get_env_setting('EMAIL_HOST_PASSWORD')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
# EMAIL_HOST_USER = get_env_setting('EMAIL_HOST_USER')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
# EMAIL_PORT = get_env_setting('EMAIL_PORT')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {}
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION
