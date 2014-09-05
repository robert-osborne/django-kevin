"""Production settings and globals."""

from __future__ import absolute_import

from .base import *

import os


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECURE_PROXY_SSL_HEADER
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = [PROJECT_DOMAIN, '.herokuapp.com', 'localhost', '127.0.0.1']
########## END HOST CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.gmail.com'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 587

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = '%s Team <contact@%s>' % (PROJECT_NAME, PROJECT_DOMAIN)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'Serverbot <dev@%s>' % PROJECT_DOMAIN
########## END EMAIL CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Dev Team', 'Dev Team <dev@%s>' % PROJECT_DOMAIN),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
if 'REDISCLOUD_URL' in os.environ:
    import urlparse
    redis_url = urlparse.urlparse(os.getenv('REDISCLOUD_URL'))
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.cache.RedisCache',
            'LOCATION': '%s:%s:%s' % (redis_url.hostname, redis_url.port, 0),
            'OPTIONS': {
                'PASSWORD': redis_url.password
            }
        }
    }
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.environ['SECRET_KEY']
########## END SECRET CONFIGURATION


########## AMAZON S3 CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
if 'AWS_ACCESS_KEY_ID' in os.environ:
    INSTALLED_APPS += (
        'storages',
    )

    AWS_S3_SECURE_URLS = True
    AWS_QUERYSTRING_AUTH = False

    # Separate buckets for static files and media files
    AWS_STATIC_STORAGE_BUCKET_NAME = os.getenv('AWS_STATIC_STORAGE_BUCKET_NAME')
    AWS_MEDIA_STORAGE_BUCKET_NAME = os.getenv('AWS_MEDIA_STORAGE_BUCKET_NAME')
    S3_STATIC_URL = '//%s.s3.amazonaws.com/' % AWS_STATIC_STORAGE_BUCKET_NAME
    S3_MEDIA_URL = '//%s.s3.amazonaws.com/' % AWS_MEDIA_STORAGE_BUCKET_NAME

    # Using django-pipeline along with S3 storage for staticfiles
    # See: https://django-pipeline.readthedocs.org/en/latest/storages.html#using-with-other-storages
    from django.contrib.staticfiles.storage import CachedFilesMixin
    from pipeline.storage import PipelineMixin
    from storages.backends.s3boto import S3BotoStorage

    class S3PipelineCachedStorage(PipelineMixin, CachedFilesMixin, S3BotoStorage):
        pass

    StaticRootS3BotoStorage = lambda: S3PipelineCachedStorage(bucket=AWS_STATIC_STORAGE_BUCKET_NAME)
    STATICFILES_STORAGE = 'config.settings.production.StaticRootS3BotoStorage'
    STATIC_URL = S3_STATIC_URL

    MediaRootS3BotoStorage = lambda: S3BotoStorage(bucket=AWS_MEDIA_STORAGE_BUCKET_NAME)
    DEFAULT_FILE_STORAGE = 'config.settings.production.MediaRootS3BotoStorage'
    MEDIA_URL = S3_MEDIA_URL
########## END AMAZON S3 CONFIGURATION
