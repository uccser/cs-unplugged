"""URL routing for the dev application."""

from django.conf.urls import url

from . import views

app_name = "dev"
urlpatterns = [
    # eg: /dev/
    url(
        r"^$",
        views.IndexView.as_view(),
        name="index"
    ),
]
