"""URL configuration for the Django system.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
"""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from general import views

urlpatterns = i18n_patterns(
    path("", include("general.urls", namespace="general")),
    path("topics/", include("topics.urls", namespace="topics")),
    path("resources/", include("resources.urls", namespace="resources")),
)

urlpatterns += [
    path("", include("classic.urls")),
    path("en/search/", include("search.urls", namespace="search")),
    path("_ah/health", views.health_check),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += i18n_patterns(
        path("__dev__/", include("dev.urls", namespace="dev")),
    )
    # These patterns allows these error pages to be debugged during development.
    from django.views import defaults
    urlpatterns += [
        path('400/', defaults.bad_request, kwargs={'exception': Exception("Bad request")}),
        path('403/', defaults.permission_denied, kwargs={'exception': Exception("Permissin denied")}),
        path('404/', defaults.page_not_found, kwargs={'exception': Exception("Page not found")}),
        path('500/', defaults.server_error),
    ]
