# coding=utf-8

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
DATABASES = {
    'default': {
        'ENGINE': 'django_postgrespool',
        'HOST': '',
        'PORT': '',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '',
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
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# --------
# Security
# --------
ALLOWED_HOSTS = ['.{{ project_name }}.sk']

# ---------------
# django-pipeline
# ---------------
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE_CSS_COMPRESSOR = 'base.compressors.CSSMinCompressor'

# -----
# South
# -----
SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2'
}
