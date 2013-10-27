#!/usr/bin/env python
# coding=utf-8

import os
import sys

PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.realpath(__file__))
)

sys.path.append(os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME))
sys.path.append(os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'apps'))

if __name__ == '__main__':
    settings = 'conf.{0}.settings'.format('test' if 'test' in sys.argv else 'local')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
