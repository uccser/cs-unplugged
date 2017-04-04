from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
import pdfkit
from PIL import Image
from io import BytesIO
import importlib
import base64

RESPONSE_CONTENT_DISPOSITION = 'attachment; filename="{filename}.pdf"'


def generate_resource_pdf(request, resource, module_path):
    """Returns a response containing a randomly generated PDF resource.

    Returns:
        HTTP Response containing generated resource PDF
    """
    context = dict()
    get_request = request.GET
    context['resource'] = resource

    resource_image_generator = importlib.import_module(module_path)
    filename = '{} ({})'.format(resource.name, resource_image_generator.subtitle(get_request, resource))
    context['filename'] = filename

    context['resource_images'] = []
    for copy in range(0, int(get_request['copies'])):
        context['resource_images'].append(
            generate_resource_image(get_request, resource, module_path)
        )

    pdf_html = render_to_string('resources/base-resource-pdf.html', context)

    footer_template = "{name} - csunplugged.org{url}"
    footer_text = footer_template.format(name=resource.name, url=reverse('resources:resource', args=[resource.slug]))
    options = {
        'page-size': get_request['paper_size'],
        'image-dpi': '300',
        'margin-top': '10mm',
        'margin-right': '10mm',
        'margin-bottom': '10mm',
        'margin-left': '10mm',
        'encoding': 'UTF-8',
        'footer-center': footer_text,
        'footer-font-name': 'Open Sans',
        'footer-font-size': 10,
        'user-style-sheet': 'build/css/print-resource-pdf.css',
        'no-outline': None
    }
    pdf_file = pdfkit.from_string(pdf_html, False, options=options)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = RESPONSE_CONTENT_DISPOSITION.format(filename=filename)
    return response


def generate_resource_image(get_request, resource, module_path):
    """Calls the resource's image generator and returns the generated
    image. This function also resizes the generated image for the paper
    size requested.

    Returns:
        Base 64 string of a generated resource image.
    """
    # Get image from resource image creator
    resource_image_generator = importlib.import_module(module_path)
    image = resource_image_generator.resource_image(get_request, resource)

    # Resize image to reduce file size
    MARGIN_SIZE = 0
    MM_TO_PIXEL_RATIO = 3.78
    if get_request['paper_size'] == "A4":
        max_pixel_height = (297 - MARGIN_SIZE) * MM_TO_PIXEL_RATIO
    elif get_request['paper_size'] == "A3":
        max_pixel_height = (420 - MARGIN_SIZE) * MM_TO_PIXEL_RATIO
    elif get_request['paper_size'] == "Letter":
        max_pixel_height = (279 - MARGIN_SIZE) * MM_TO_PIXEL_RATIO
    elif get_request['paper_size'] == "Legal":
        max_pixel_height = (356 - MARGIN_SIZE) * MM_TO_PIXEL_RATIO
    (width, height) = image.size
    if height > max_pixel_height:
        ratio = max_pixel_height / height
        width *= ratio
        height *= ratio
        image = image.resize((int(width), int(height)), Image.ANTIALIAS)

    # Save image to buffer
    image_buffer = BytesIO()
    image.save(image_buffer, format='PNG')

    # Return base64 of image
    return base64.b64encode(image_buffer.getvalue())
