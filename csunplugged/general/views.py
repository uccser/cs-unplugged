from django.shortcuts import render
from django.views.generic import TemplateView


class GeneralIndexView(TemplateView):
    template_name = 'general/index.html'

    def get_context_data(self, **kwargs):
        # TODO: Investigate if importing model from another
        # app is sensible/best approach.
        from topics.models import Topic
        context = super(GeneralIndexView, self).get_context_data(**kwargs)
        context['total_topics'] = Topic.objects.count()
        return context


class GeneralAboutView(TemplateView):
    template_name = 'general/about.html'
