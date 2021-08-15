"""URL configuration for testing general pages model."""

from django.urls import path

urlpatterns = [
    path('valid-url', lambda: True, name='url'),
]
