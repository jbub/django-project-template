# coding=utf-8

from conf.settings import *

# ------
# Common
# ------
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'conf.production.urls'

# ---------
# Databases
# ---------
DATABASES = {
    'default': {
        'ENGINE': 'django_postgrespool',
        'HOST': '',
        'PORT': '',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '',
        'OPTIONS': {
            'autocommit': True,
        }
    },
}

# ------
# Static
# ------
STATIC_URL = '/static/'

# -----
# Media
# -----
MEDIA_URL = '/media/'

# ----------------
# Template loaders
# ----------------
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# -----
# Cache
# -----
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': PROJECT_MODULE_NAME,
    }
}

# -------
# Session
# -------
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = 'default'

# --------
# Security
# --------
ALLOWED_HOSTS = ['.{{ project_name }}.sk']

# -----
# South
# -----
SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2'
}
