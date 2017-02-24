from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML, CSS
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
from random import sample
from multiprocessing import Pool
from django.utils.translation import ugettext as _

MM_TO_PIXEL_RATIO = 3.78

def generate_image(base_image_settings):
    # Load image
    base_image = Image.open(base_image_settings['base_image_path'])
    draw = ImageDraw.Draw(base_image)

    # Add numbers to text if needed
    if base_image_settings['prefilled_values'] != 'blank':
        font = ImageFont.truetype(base_image_settings['font_path'], base_image_settings['font_size'])
        numbers = sample(range(base_image_settings['range_min'], base_image_settings['range_max']), 6)
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

    # Resize image to reduce file size
    if base_image_settings['paper_size'] == "a4":
        max_pixel_height = 267 * MM_TO_PIXEL_RATIO
    elif base_image_settings['paper_size'] == "letter":
        max_pixel_height = 249 * MM_TO_PIXEL_RATIO
    (width, height) = base_image.size
    if height > max_pixel_height:
        ratio = max_pixel_height / height
        width *= ratio
        height *= ratio
        base_image = base_image.resize((int(width), int(height)), Image.ANTIALIAS)

    # Save image to buffer
    image_buffer = BytesIO()
    base_image.save(image_buffer, format='PNG')
    return base64.b64encode(image_buffer.getvalue())

class PageCreator(object):
    def __init__(self, base_image_settings):
        self.base_image_settings = base_image_settings

    def __call__(self, call_num):
        return generate_image(self.base_image_settings)

def pdf(request, resource, **kwargs):
    context = dict()

    prefilled_values = request.GET['prefilled_values']
    paper_size = request.GET['size']

    base_image_settings = dict()
    base_image_settings['prefilled_values'] = prefilled_values
    base_image_settings['paper_size'] = paper_size
    if prefilled_values == 'easy':
        base_image_settings['range_min'] = 1
        base_image_settings['range_max'] = 10
        base_image_settings['font_size'] = 150
    elif prefilled_values == 'medium':
        base_image_settings['range_min'] = 10
        base_image_settings['range_max'] = 100
        base_image_settings['font_size'] = 120
    elif prefilled_values == 'hard':
        base_image_settings['range_min'] = 100
        base_image_settings['range_max'] = 1000
        base_image_settings['font_size'] = 90

    # Create resource image
    base_image_settings['base_image_path'] = 'resources/content/{}/sorting-network-colour.png'.format(resource.folder)
    base_image_settings['font_path'] = 'resources/content/fonts/PatrickHand-Regular.ttf'
    with Pool() as pool:
        context['resource_images'] = pool.map(PageCreator(base_image_settings), range(0, int(request.GET['copies'])))

    # Write to PDF
    context['paper_size'] = paper_size
    context['resource'] = resource
    html_string = render_to_string('resources/base-resource-pdf.html', context)

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    base_css = CSS(string=open('static/css/print-resource-pdf.css', encoding='UTF-8').read())
    pdf_file = html.write_pdf(stylesheets=[base_css]);

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="example.pdf"'
    return response
