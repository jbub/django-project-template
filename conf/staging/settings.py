# coding=utf-8

from conf.settings import *

# ------
# Common
# ------
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'conf.staging.urls'

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
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': env_var('REDIS_CACHE_URL'),
        'KEY_PREFIX': PROJECT_MODULE_NAME,
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}

# --------
# Security
# --------
ALLOWED_HOSTS = ['.{{ project_name }}.sk']
