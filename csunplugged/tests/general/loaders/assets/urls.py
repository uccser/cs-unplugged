"""URL configuration for testing general pages loader."""

from django.conf.urls import url

urlpatterns = [
    url(r"", lambda: True, name="page"),
]
