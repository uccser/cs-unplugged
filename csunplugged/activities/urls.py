from django.conf.urls import url

from . import views

urlpatterns = [
    # eg: /activities/
    url(r'^$', views.index, name='index'),
    # eg: /activities/binary-numbers/
    url(r'^(?P<activity_name>[-\w]*)/$', views.description, name='description'),
]
