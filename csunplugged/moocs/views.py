"""Views for the MOOCs application."""

from django.views.generic import TemplateView


class MoocsIndexView(TemplateView):
    """View for the MOOCs homepage that renders from a template."""

    template_name = "moocs/index.html"
