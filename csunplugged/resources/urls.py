"""URL routing for the resources application."""

from django.urls import path

from . import views

app_name = "resources"
urlpatterns = [
    # eg: /resource/
    path(
        '',
        views.IndexView.as_view(),
        name="index"
    ),
    # eg: /resource/example-resource/
    path(
        '<slug:resource_slug>/',
        views.resource,
        name="resource"
    ),
    # eg: /resource/example-resource/generate/
    path(
        '<slug:resource_slug>/generate',
        views.generate_resource,
        name="generate"
    ),
]
