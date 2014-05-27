# coding=utf-8

from conf.settings import *

# ------
# Common
# ------
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'conf.local.urls'

# -----
# Email
# -----
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
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

# -----
# Cache
# -----
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': PROJECT_MODULE_NAME,
    }
}

# --------------------
# django-debug-toolbar
# --------------------
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': set(['debug_toolbar.panels.redirects.RedirectsPanel'])
}
