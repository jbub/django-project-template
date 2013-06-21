# coding=utf-8

from conf.settings import *

# ------
# Common
# ------
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'conf.local.urls'

# ---------
# Databases
# ---------
DATABASES = {
    'default': {
        'ENGINE': 'django_postgrespool',
        'HOST': 'localhost',
        'NAME': '{{ project_name }}',
        'USER': '',
        'PASSWORD': '',
        'OPTIONS': {
            'autocommit': True,
        }
    },
}

# -----
# Email
# -----
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'djangoemailsender@gmail.com'
EMAIL_HOST_PASSWORD = 'do9fkWHJwS1QBmu'
EMAIL_USE_TLS = True

# ----
# Apps
# ----
INSTALLED_APPS += (
    'debug_toolbar',
)

# ----------
# Middleware
# ----------
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# --------------------
# django-debug-toolbar
# --------------------
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

# -----
# South
# -----
SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2'
}
