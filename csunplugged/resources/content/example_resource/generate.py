from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML, CSS
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
from random import sample

def pdf(request, resource, **kwargs):
    context = dict()

    # Create resource image
    base_image = Image.open('resources/content/example_resource/sorting-network-colour.png')

    # Create numbers to add to image
    difficulty = request.GET['difficulty']
    if difficulty == 'easy':
        range_min = 1
        range_max = 10
        font_size = 150
    elif difficulty == 'medium':
        range_min = 10
        range_max = 100
        font_size = 120
    else:
        range_min = 100
        range_max = 1000
        font_size = 90

    numbers = sample(range(range_min, range_max), 6)

    # Load image for adding text
    draw = ImageDraw.Draw(base_image)
    font_path = 'resources/content/fonts/PatrickHand-Regular.ttf'
    font = ImageFont.truetype(font_path, font_size)

    # Add numbers to text
    base_coord_x = 70
    base_coord_y = 2560
    coord_x_increment = 204
    for number in numbers:
        text = str(number)
        text_width, text_height = draw.textsize(text, font=font)
        coord_x = base_coord_x - (text_width / 2)
        coord_y = base_coord_y - (text_height / 2)
        draw.text(
            (coord_x, coord_y),
            text,
            font=font,
            fill='#000'
        )
        base_coord_x += coord_x_increment

    # Save image to buffer
    image_buffer = BytesIO()
    base_image.save(image_buffer, format='PNG')
    context['image_data'] = base64.b64encode(image_buffer.getvalue())

    # Write to PDF
    context['paper_size'] = request.GET['size']
    context['resource'] = resource
    template = '{}/resource.html'.format(resource.folder)
    html_string = render_to_string(template, context)

    html = HTML(string=html_string)
    base_css = CSS(string=open('static/css/print-resource-pdf.css', encoding='UTF-8').read())
    pdf_file = html.write_pdf(stylesheets=[base_css]);

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="example.pdf"'
    return response
