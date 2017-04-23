"""Views for the general application."""

from django.views.generic import TemplateView


class GeneralIndexView(TemplateView):
    """View for the homepage that renders from a template."""

    template_name = 'general/index.html'

    def get_context_data(self, **kwargs):
        """Provide the context data for the homepage view."""
        # TODO: Investigate if importing model from another
        # app is sensible/best approach.
        from topics.models import Topic
        context = super(GeneralIndexView, self).get_context_data(**kwargs)
        context['total_topics'] = Topic.objects.count()
        return context


class GeneralAboutView(TemplateView):
    """View for the about page that renders from a template."""

    template_name = 'general/about.html'
