from django.conf.urls import include, url

from . import views

urlpatterns = [
    url('^$', views.index, name='home-page'),
    url('^example$', views.example, name='exampple'),
]
