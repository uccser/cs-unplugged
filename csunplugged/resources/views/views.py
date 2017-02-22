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
    template_string = 'resources/{}/index.html'.format(resource_slug)
    context = dict()
    context['resource'] = get_object_or_404(Resource, slug=resource_slug)
    return render(request, template_string, context)

def pdf_handler(request, resource_slug, **kwargs):
    module_name = resource_slug.replace('-', '_')
    module_path = 'resources.views.resource.{}'.format(module_name)
    try:
        pdf_view = importlib.import_module(module_path)
    except ImportError:
        raise Http404("PDF generation does not exist for resource: {}".format(resource_slug))
    return pdf_view.pdf(request, **kwargs)
