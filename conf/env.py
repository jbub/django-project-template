# coding=utf-8

import os
import sys
import dotenv

from django.core.exceptions import ImproperlyConfigured


def init_app(env_file='.env'):
    """
    Initializes the application environment and paths.
    """
    init_path()
    init_env(env_file)


def init_path():
    """
    Initializes application paths.
    """
    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    apps_path = os.path.join(root_path, 'apps')

    if apps_path not in sys.path:
        sys.path.append(apps_path)


def init_env(env_file):
    """
    Loads environment variables from env_file to environ.
    """
    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    env_file = os.path.join(root_path, '.env')
    dotenv.read_dotenv(dotenv=env_file)


def env_var(key):
    """
    Returns value of the environment variable.
    """
    if key not in os.environ:
        raise ImproperlyConfigured('Environment variable {0} not provided!'.format(key))
    return os.environ[key]
