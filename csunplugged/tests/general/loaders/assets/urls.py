"""URL configuration for testing general pages loader."""

from django.urls import path

urlpatterns = [
    path('', lambda: True, name='page'),
]
