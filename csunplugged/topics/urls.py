from django.conf.urls import url

from . import views

app_name = 'topics'
urlpatterns = [
    # eg: /topics/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # eg: /topics/binary-numbers/
    url(r'^(?P<slug>[-\w]+)/$', views.TopicView.as_view(), name='topic'),
]
