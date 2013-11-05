# coding=utf-8

import dj_database_url

from conf.settings import *

# ------
# Common
# ------
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'conf.staging.urls'

# ---------
# Databases
# ---------
DATABASES = {}
DATABASES['default'] = dj_database_url.config(env='DATABASE_URL')
DATABASES['default']['ENGINE'] = 'django_postgrespool'
DATABASES['default']['OPTIONS'] = {'autocommit': True}

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
SECRET_KEY = env_var('SECRET_KEY')

# -----
# South
# -----
SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2'
}
