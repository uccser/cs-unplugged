from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders
from django.conf import settings
from multiprocessing import Pool
from functools import partial
from weasyprint import HTML, CSS
from PIL import Image
from io import BytesIO
import importlib
import base64

RESPONSE_CONTENT_DISPOSITION = 'attachment; filename="{filename}.pdf"'
MM_TO_PIXEL_RATIO = 3.78


def generate_resource_pdf(request, resource, module_path):
    """Returns a response containing a randomly generated PDF resource.

    Returns:
        HTTP Response containing generated resource PDF
    """
    context = dict()
    get_request = request.GET
    context['paper_size'] = get_request['paper_size']
    context['resource'] = resource
    context['header_text'] = get_request['header_text']

    resource_image_generator = importlib.import_module(module_path)
    filename = '{} ({})'.format(resource.name, resource_image_generator.subtitle(get_request, resource))
    context['filename'] = filename

    num_copies = range(0, int(get_request['copies']))
    image_generator = partial(
        generate_resource_image,
        get_request,
        resource,
        module_path
    )
    context['resource_images'] = []
    for copy in num_copies:
        context['resource_images'].append(
            generate_resource_image(get_request, resource, module_path)
        )

    pdf_html = render_to_string('resources/base-resource-pdf.html', context)
    html = HTML(string=pdf_html, base_url=settings.STATIC_ROOT)
    css_file = finders.find('css/print-resource-pdf.css')
    css_string = open(css_file, encoding='UTF-8').read()
    base_css = CSS(string=css_string)
    pdf_file = html.write_pdf(stylesheets=[base_css])

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
    if get_request['paper_size'] == "a4":
        max_pixel_height = 267 * MM_TO_PIXEL_RATIO
    elif get_request['paper_size'] == "letter":
        max_pixel_height = 249 * MM_TO_PIXEL_RATIO
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
