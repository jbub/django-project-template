#!/usr/bin/env python
# coding=utf-8

import sys

if __name__ == '__main__':
    from conf.env import init_app
    from django.core.management import execute_from_command_line
    init_app()
    execute_from_command_line(sys.argv)
