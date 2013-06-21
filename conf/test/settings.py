# coding=utf-8

import multiprocessing

from conf.settings import *

# ------
# Common
# ------
ROOT_URLCONF = 'conf.test.urls'

# ---------
# Databases
# ---------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
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

# ----
# Apps
# ----
INSTALLED_APPS += (
    'django_nose',
)

# -----
# Tests
# -----
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--processes={0}'.format(multiprocessing.cpu_count()),
             '--stop', '--nologcapture']

# -----
# South
# -----
SOUTH_TESTS_MIGRATE = False

# ----------------------
# django-dynamic-fixture
# ----------------------
DDF_VALIDATE_MODELS = True
