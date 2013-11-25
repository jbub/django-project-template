# coding=utf-8

import os

from django.conf.global_settings import *
from django.core.exceptions import ImproperlyConfigured


def env_var(key):
    if key not in os.environ:
        raise ImproperlyConfigured('Environment variable {0} not provided!'.format(key))
    return os.environ[key]

# ------
# Common
# ------
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SITE_ID = 1
ADMINS = (
    #('Example Name', 'test@example.com'),
)
MANAGERS = ADMINS

# -----------
# Directories
# -----------
PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))))
PROJECT_ROOT = os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME)

# --------------
# Language, time
# --------------
TIME_ZONE = 'Europe/Bratislava'
LANGUAGE_CODE = 'sk'
LANGUAGES = (
    ('sk', gettext_noop('Slovak')),
)
USE_I18N = True
USE_L10N = True
USE_TZ = False
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

# ----
# Urls
# ----
ROOT_URLCONF = 'conf.urls'

# -----
# Media
# -----
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# ------
# Static
# ------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = ()
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

# ---------
# Templates
# ---------
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# ----
# Apps
# ----
INSTALLED_APPS = (
    # django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    # 3rd party
    'south',
    'pipeline',
    'braces',
    'djorm_pool',
    # own
    'base',
)

# ------------------
# Context processors
# ------------------
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

# ----------
# Middleware
# ----------
MIDDLEWARE_CLASSES += (
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# --------
# Security
# --------
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECRET_KEY = '{{ secret_key }}'
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# ----
# Wsgi
# ----
WSGI_APPLICATION = 'conf.wsgi.application'

# -------
# Logging
# -------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# ---------------
# django-pipeline
# ---------------
PIPELINE_CSS = {
    'main': {
        'source_filenames': ('base/css/base.css',),
        'output_filename': 'base/css/cache-main.css',
    },
}
PIPELINE_JS = {
    'footer': {
        'source_filenames': ('base/js/script.js',),
        'output_filename': 'base/js/cache-footer.js',
    },
}
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE_CSS_COMPRESSOR = 'base.compressors.CSSMinCompressor'
PIPELINE_DISABLE_WRAPPER = True
