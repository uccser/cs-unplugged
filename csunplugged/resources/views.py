from django.views import generic
from .models import Resource


class IndexView(generic.ListView):
    template_name = 'resources/index.html'
    context_object_name = 'all_resources'

    def get_queryset(self):
        """Return all topics"""
        return Resource.objects.order_by('name')


class ResourceView(generic.DetailView):
    model = Resource
    template_name = 'resources/resource.html'
    slug_url_kwarg = 'resource_slug'
