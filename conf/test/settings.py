# coding=utf-8

from conf.settings import *

# ------
# Common
# ------
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'conf.test.urls'

# ---------
# Databases
# ---------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

# -----
# Cache
# -----
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': PROJECT_MODULE_NAME,
    }
}
