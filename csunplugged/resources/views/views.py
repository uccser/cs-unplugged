"""Views for the resource application."""

from django.conf import settings
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from resources.models import Resource
import importlib
from utils.group_lessons_by_age import group_lessons_by_age

RESPONSE_CONTENT_DISPOSITION = 'attachment; filename="{filename}.pdf"'


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
    context["debug"] = settings.DEBUG
    context["grouped_lessons"] = group_lessons_by_age(resource.lesson_generated_resources.all())
    if resource.thumbnail_static_path:
        context["thumbnail"] = resource.thumbnail_static_path
    return render(request, resource.webpage_template, context)


def resource_pdf_cache(request, resource, module_path):
        """Provide redirect to static resource file.

        Args:
            request: HttpRequest object.
            resource: Resource model object.
            module_path: Path to resource module (str).

        Returns:
            HTTP redirect.
        """
        resource_image_generator = importlib.import_module(module_path)
        subtitle = resource_image_generator.subtitle(request.GET, resource)
        filename = "{} ({})".format(resource.name, subtitle)
        redirect_url = "{}resources/{}.pdf".format(settings.STATIC_URL, filename)
        return redirect(redirect_url)
