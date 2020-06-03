"""URL routing for the dev application."""

from django.urls import path

from . import views

app_name = 'dev'
urlpatterns = [
    # eg: /dev/
    path(
        '',
        views.IndexView.as_view(),
        name="index"
    ),
]
