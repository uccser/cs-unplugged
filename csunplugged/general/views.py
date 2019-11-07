"""Views for the general application."""

from django.views.generic import TemplateView


class GeneralIndexView(TemplateView):
    """View for the homepage that renders from a template."""

    template_name = "general/index.html"

    def get_context_data(self, **kwargs):
        """Provide the context data for the homepage.

        Returns:
            Dictionary of context data.
        """
        context = super(GeneralIndexView, self).get_context_data(**kwargs)
        context["homepage"] = True
        return context


class GeneralAboutView(TemplateView):
    """View for the about page that renders from a template."""

    template_name = "general/about.html"


class GeneralContactView(TemplateView):
    """View for the contact page that renders from a template."""

    template_name = "general/contact.html"


class GeneralPeopleView(TemplateView):
    """View for the people page that renders from a template."""

    template_name = "general/people.html"


class GeneralPrinciplesView(TemplateView):
    """View for the princples page that renders from a template."""

    template_name = "general/principles.html"


class WhatIsCSView(TemplateView):
    """View for the 'What is Computer Science?' page that renders from a template."""

    template_name = "general/what-is-computer-science.html"


class ComputationalThinkingView(TemplateView):
    """View for the Computational Thinking page that renders from a template."""

    template_name = "general/computational-thinking.html"


class HowDoITeachCSUnpluggedView(TemplateView):
    """View for the 'How do I teach CS Unplugged?' page that renders from a template."""

    template_name = "general/how-do-i-teach-cs-unplugged.html"
