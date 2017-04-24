"""URL routing for the general application."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about/$', views.GeneralAboutView.as_view(), name='about'),
    url(r'^$', views.GeneralIndexView.as_view(), name='home'),
]
