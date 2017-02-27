from django.views import generic
from django.utils.translation import ugettext
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from resources.models import Resource
from resources.generate_resource_pdf import generate_resource_pdf
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
    context['lessons'] = resource.lesson_generated_resources.all()
    if resource.thumbnail_static_path:
        context['thumbnail'] = resource.thumbnail_static_path
    return render(request, template_string, context)

def generate_resource(request, resource_slug):
    """Try to import and call resource image generator, 404 if not found."""
    resource = get_object_or_404(Resource, slug=resource_slug)
    module_path = 'resources.content.{}.image_generator'.format(resource.folder)
    try:
        importlib.import_module(module_path)
    except ImportError:
        raise Http404("PDF generation does not exist for resource: {}".format(resource_slug))
    else:
        # TODO: Add creation of PDF as job to job queue
        return generate_resource_pdf(request, resource, module_path)
