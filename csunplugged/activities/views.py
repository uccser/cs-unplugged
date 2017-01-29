from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Activity

class IndexView(generic.ListView):
    template_name = 'activities/index.html'
    context_object_name = 'all_activities'

    def get_queryset(self):
        """Return all activities"""
        return Activity.objects.order_by('name')


class ActivityView(generic.DetailView):
    model = Activity
    template_name = 'activities/activity.html'
    slug_url_kwarg = 'slug'
