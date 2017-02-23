from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML, CSS
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
from random import shuffle

def pdf(request, resource, **kwargs):
    context = dict()

    # Create resource image
    base_image = Image.open('resources/content/example_resource/sorting-network-colour.png')

    # Create numbers to add to image
    numbers = list(range(1, 7))
    shuffle(numbers)

    # Load image for adding text
    draw = ImageDraw.Draw(base_image)
    font_path = 'resources/content/fonts/PatrickHand-Regular.ttf'
    font = ImageFont.truetype(font_path, 150)

    # Add numbers to text
    coord_x = 45
    coord_y = 2475
    for number in numbers:
        draw.text(
            (coord_x, coord_y),
            str(number),
            font=font,
            fill='#000',
            align='center'
        )
        coord_x += 204

    # Save image to buffer
    image_buffer = BytesIO()
    base_image.save(image_buffer, format='PNG')
    context['image_data'] = base64.b64encode(image_buffer.getvalue())

    # Write to PDF
    context['paper_size'] = request.GET['size']
    template = '{}/resource.html'.format(resource.folder)
    html_string = render_to_string(template, context)

    html = HTML(string=html_string)
    base_css = CSS(string=open('static/css/print-resource-pdf.css', encoding='UTF-8').read())
    pdf_file = html.write_pdf(stylesheets=[base_css]);

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="example.pdf"'
    return response
