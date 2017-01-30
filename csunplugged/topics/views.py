from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Topic

class IndexView(generic.ListView):
    template_name = 'topics/index.html'
    context_object_name = 'all_topics'

    def get_queryset(self):
        """Return all topics"""
        return Topic.objects.order_by('name')


class TopicView(generic.DetailView):
    model = Topic
    template_name = 'topics/topic.html'
    slug_url_kwarg = 'slug'
