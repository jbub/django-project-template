# coding=utf-8

from django.utils.translation import activate


def pytest_runtest_setup(item):
    # run all tests with en locale
    activate('en')
