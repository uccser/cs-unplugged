from django.conf.urls import include, url

from . import views

urlpatterns = [
    url('^$', views.index, name='home-page'),
    url('^example$', views.example, name='example'),
    url(r'^lesson-one-how-binary-digits-work', views.lesson_one_how_binary_digits_work, name='lesson_one'),
]
