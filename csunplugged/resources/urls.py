from django.conf.urls import url

from .views import views

app_name = 'resources'
urlpatterns = [
    # eg: /resource/
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    # eg: /resource/example-resource/
    url(
        r'^(?P<resource_slug>[-\w]+)/$',
        views.resource,
        name='resource'
    ),
    # eg: /resource/example-resource/generate/
    url(
        r'^(?P<resource_slug>[-\w]+)/generate$',
        views.generate_resource,
        name='generate'
    ),
]
