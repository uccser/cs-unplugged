"""URL redirect routing for the at home section of the CS Unplugged website."""

from django.conf.urls import url
from at_home import views

app_name = "at_home"
urlpatterns = [
    # eg: /at-home/
    url(
        r"^$",
        views.IndexView.as_view(),
        name="index"
    ),

]
