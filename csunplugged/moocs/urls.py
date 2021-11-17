"""URL routing for the moocs application."""

from django.urls import path

from . import views

app_name = 'moocs'
urlpatterns = [
    path(
        '',
        views.MoocsIndexView.as_view(),
        name="index"
    ),
]
