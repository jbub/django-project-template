# coding=utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

urlpatterns = patterns('')

if settings.MEDIA_ROOT:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns(
    '',
    url(r'', include('conf.common.urls.admin')),
    url(r'', include('conf.urls')),
)
