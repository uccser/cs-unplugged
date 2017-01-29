from django.conf.urls import url

from . import views

app_name = 'activities'
urlpatterns = [
    # eg: /activities/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # eg: /activities/binary-numbers/
    url(r'^(?P<slug>[-\w]+)/$', views.ActivityView.as_view(), name='activity'),
]
