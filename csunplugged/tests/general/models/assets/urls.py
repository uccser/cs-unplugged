"""URL configuration for testing general pages model."""

from django.conf.urls import url

urlpatterns = [
    url(r"valid-url", lambda: True, name="url"),
]
