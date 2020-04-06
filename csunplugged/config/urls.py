"""URL configuration for the Django system.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    url(r"", include("general.urls", namespace="general")),
    url(r"^topics/", include("topics.urls", namespace="topics")),
    url(r"^plugging-it-in/", include("plugging_it_in.urls", namespace="plugging_it_in")),
    url(r"^resources/", include("resources.urls", namespace="resources")),
    url(r"^at-home/", include("at_home.urls", namespace="at_home")),
)

urlpatterns += [
    url(r"", include("classic.urls")),
    url(r"^en/search/", include("search.urls", namespace="search")),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    urlpatterns += [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += i18n_patterns(
        url(r"^__dev__/", include("dev.urls", namespace="dev")),
    )
    # These patterns allows these error pages to be debugged during development.
    from django.views import defaults
    urlpatterns += [
        url(r'^400/$', defaults.bad_request, kwargs={'exception': Exception("Bad request")}),
        url(r'^403/$', defaults.permission_denied, kwargs={'exception': Exception("Permissin denied")}),
        url(r'^404/$', defaults.page_not_found, kwargs={'exception': Exception("Page not found")}),
        url(r'^500/$', defaults.server_error),
    ]
