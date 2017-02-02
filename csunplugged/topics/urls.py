from django.conf.urls import url

from . import views

app_name = 'topics'
urlpatterns = [
    # eg: /topics/
    url(r'^$', views.index, name='index'),
    # eg: /topics/binary-numbers/
    url(r'^(?P<slug>[-\w]+)/$', views.topic, name='topic'),
]
