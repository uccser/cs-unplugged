"""Views for the at home application."""

from django.views import generic


class IndexView(generic.TemplateView):
    """View for the at home application homepage."""

    template_name = "at-home/index.html"
