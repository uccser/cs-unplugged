from django.conf.urls import url

from . import views

app_name = 'resources'
urlpatterns = [
    # eg: /resource/
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    # eg: /resource/example-resource/
    # url(
    #     r'^(?P<resource_slug>[-\w]+)/$',
    #     views.ResourceView.as_view(),
    #     name='resource'
    # )
]
