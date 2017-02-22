from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML, CSS

def pdf(request, resource_slug, **kwargs):
    context = dict()
    context['paper_size'] = request.GET['size']
    template = 'resources/{}/resource.html'.format(resource_slug)
    html_string = render_to_string(template, context)

    html = HTML(string=html_string)
    base_css = CSS(string=open('static/css/print-resource-pdf.css', encoding='UTF-8').read())
    resource_css = CSS(string=open('static/css/print-resource-{}-pdf.css'.format(resource_slug), encoding='UTF-8').read())
    pdf_file = html.write_pdf(stylesheets=[base_css, resource_css]);

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="example.pdf"'
    return response
