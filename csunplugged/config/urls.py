"""URL configuration for the Django system.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from general import views

urlpatterns = i18n_patterns(
    url(r'', include('general.urls', namespace='general')),
    url(r'^topics/', include('topics.urls', namespace='topics')),
    url(r'^resources/', include('resources.urls', namespace='resources')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += [
    url(r'^_ah/health', views.health_check),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += i18n_patterns(
        url(r'^__dev__/', include('dev.urls', namespace='dev')),
    )
