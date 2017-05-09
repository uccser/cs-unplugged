"""Views for the resource application."""

from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from resources.models import Resource
from .generate_resource_pdf import generate_resource_pdf
import importlib


class IndexView(generic.ListView):
    """View for the resource application homepage."""

    template_name = "resources/index.html"
    context_object_name = "all_resources"

    def get_queryset(self):
        """Get queryset of all resources.

        Returns:
            Queryset of all resources ordered by name.
        """
        return Resource.objects.order_by("name")


def resource(request, resource_slug):
    """View for a specific resource in the resources application.

    Returns:
        HTML response of webpage, 404 if not found.
    """
    resource = get_object_or_404(Resource, slug=resource_slug)
    context = dict()
    context["resource"] = resource
    context["lessons"] = resource.lesson_generated_resources.all()
    if resource.thumbnail_static_path:
        context["thumbnail"] = resource.thumbnail_static_path
    return render(request, resource.webpage_template, context)


def generate_resource(request, resource_slug):
    """View for generated PDF of a specific resource.

    Returns:
        HTML response containing PDF of resource, 404 if not found.
    """
    resource = get_object_or_404(Resource, slug=resource_slug)
    resource_view = resource.generation_view
    # Remove .py extension if given
    if resource_view.endswith(".py"):
        resource_view = resource_view[:-3]
    module_path = "resources.views.{}".format(resource_view)
    spec = importlib.util.find_spec(module_path)
    if spec is None:
        raise Http404("PDF generation does not exist for resource: {}".format(resource_slug))
    else:
        # TODO: Add creation of PDF as job to job queue
        return generate_resource_pdf(request, resource, module_path)
