from django.views.generic import TemplateView


class GeneralIndexView(TemplateView):
    template_name = 'general/index.html'


class GeneralAboutView(TemplateView):
    template_name = 'general/about.html'
