# coding=utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'', include('conf.common.urls.admin')),
    url(r'', include('conf.urls')),
)
