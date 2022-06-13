"""URL configuration for the Django system.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
"""

from django.conf import settings
from django.http.response import HttpResponse
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from config import views
import environ
env = environ.Env()

urlpatterns = i18n_patterns(
    path('', include('general.urls', namespace='general')),
    path('topics/', include('topics.urls', namespace='topics')),
    path('resources/', include('resources.urls', namespace='resources')),
    path('at-home/', include('at_home.urls', namespace='at_home')),
    path('plugging-it-in/', include('plugging_it_in.urls', namespace='plugging_it_in')),
    path('moocs/', include('moocs.urls', namespace='moocs')),
)

urlpatterns += [
    path('', include('classic.urls')),
    path('en/search/', include('search.urls', namespace='search')),
    path('admin/', admin.site.urls),
    path('healthcheck/', HttpResponse),
    path('status/', view=views.get_release_and_commit, name="get-release-and-commit")
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    # These patterns allows these error pages to be debugged during development.
    from django.views import defaults
    urlpatterns += [
        path('400/', defaults.bad_request, kwargs={'exception': Exception('Bad request')}),
        path('403/', defaults.permission_denied, kwargs={'exception': Exception('Permission denied')}),
        path('404/', defaults.page_not_found, kwargs={'exception': Exception('Page not found')}),
        path('500/', defaults.server_error),
    ]
