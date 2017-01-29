from django.conf.urls import url

from . import views

app_name = 'activities'
urlpatterns = [
    # eg: /activities/
    url(r'^$', views.index, name='index'),
    # eg: /activities/binary-numbers/
    url(r'^(?P<activity_slug>[-\w]+)/$', views.activity, name='activity'),
]
