"""Views for the resource application."""

from urllib.parse import quote
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from resources.models import Resource
from resources.utils.resource_pdf_cache import resource_pdf_cache
from resources.utils.get_options_html import get_options_html
from resources.utils.get_thumbnail import (
    get_thumbnail_base,
    get_thumbnail_static_path_for_resource,
)
from utils.group_lessons_by_age import group_lessons_by_age
from utils.translated_first import translated_first
from resources.utils.get_resource_generator import get_resource_generator
from utils.errors.QueryParameterMissingError import QueryParameterMissingError
from utils.errors.QueryParameterInvalidError import QueryParameterInvalidError
from utils.errors.QueryParameterMultipleValuesError import QueryParameterMultipleValuesError

RESPONSE_CONTENT_DISPOSITION = "attachment; filename*=UTF-8''{filename}.pdf; filename=\"{filename}.pdf\""


class IndexView(generic.ListView):
    """View for the resource application homepage."""

    template_name = "resources/index.html"
    context_object_name = "all_resources"

    def get_queryset(self):
        """Get queryset of all resources.

        Returns:
            Queryset of all resources ordered by name.
        """
        return translated_first(Resource.objects.all())

    def get_context_data(self, **kwargs):
        """Provide the context data for the index view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        for resource in self.object_list:
            resource.thumbnail = get_thumbnail_static_path_for_resource(resource)
        return context


def resource(request, resource_slug):
    """View for a specific resource in the resources application.

    Args:
        request: HttpRequest object.
        resource_slug: The slug of the requested resource.

    Returns:
        HTML response of webpage, 404 if not found.
    """
    resource = get_object_or_404(Resource, slug=resource_slug)
    context = dict()
    generator = get_resource_generator(resource.generator_module)
    context["options_html"] = get_options_html(generator.get_options(), generator.get_local_options(), request.GET)
    context["resource"] = resource
    context["debug"] = settings.DEBUG
    context["grouped_lessons"] = group_lessons_by_age(resource.lessons.all())
    context["copies_amount"] = settings.RESOURCE_COPY_AMOUNT
    context["resource_thumbnail_base"] = get_thumbnail_base(resource.slug)
    return render(request, "resources/resource.html", context)


def generate_resource(request, resource_slug):
    """View for generated PDF of a specific resource.

    Args:
        request: HttpRequest object.
        resource_slug: The slug of the requested resource.

    Returns:
        HTML response containing PDF of resource, 404 if not found.
    """
    resource = get_object_or_404(Resource, slug=resource_slug)
    if not request.GET:
        raise Http404("No parameters given for resource generation.")
    try:
        generator = get_resource_generator(resource.generator_module, request.GET)
    except (QueryParameterMissingError,
            QueryParameterInvalidError,
            QueryParameterMultipleValuesError) as e:
        raise Http404(e) from e

    # TODO: Weasyprint handling in production
    # TODO: Add creation of PDF as job to job queue
    if settings.DEPLOYED:
        # Return cached static PDF file of resource.
        # Currently developing system for dynamically rendering
        # custom PDFs on request (https://github.com/uccser/render).
        return resource_pdf_cache(resource, generator)
    else:
        (pdf_file, filename) = generator.pdf(resource.name)
        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = RESPONSE_CONTENT_DISPOSITION.format(filename=quote(filename))
        return response
