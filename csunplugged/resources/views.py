from django.views import generic
from django.utils.translation import ugettext
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from resources.models import Resource
import importlib

class IndexView(generic.ListView):
    template_name = 'resources/index.html'
    context_object_name = 'all_resources'

    def get_queryset(self):
        """Return all topics"""
        return Resource.objects.order_by('name')

def resource(request, resource_slug):
    resource = get_object_or_404(Resource, slug=resource_slug)
    template_string = '{}/index.html'.format(resource.folder)
    context = dict()
    context['resource'] = resource
    return render(request, template_string, context)

def generate_resource(request, resource_slug, **kwargs):
    module_name = resource_slug.replace('-', '_')
    resource = get_object_or_404(Resource, slug=resource_slug)
    module_path = 'resources.content.{}.generate'.format(resource.folder)
    try:
        pdf_view = importlib.import_module(module_path)
    except ImportError:
        raise Http404("PDF generation does not exist for resource: {}".format(resource_slug))
    return pdf_view.pdf(request, resource, **kwargs)
