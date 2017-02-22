from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

def pdf(request, **kwargs):
    context = dict()
    context['paragraphs'] = ['first paragraph', 'second paragraph', 'third paragraph']
    html_string = render_to_string('resources/pdf-template.html', context)

    html = HTML(string=html_string)
    pdf_file = html.write_pdf();

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="example.pdf"'
    return response
