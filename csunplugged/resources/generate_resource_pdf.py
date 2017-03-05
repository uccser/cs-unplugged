from django.http import HttpResponse
from django.template.loader import render_to_string
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

    num_copies = range(0, int(get_request['copies']))
    image_generator = partial(
        generate_resource_image,
        get_request,
        resource,
        module_path
    )
    with Pool() as pool:
        context['resource_images'] = pool.map(image_generator, num_copies)
    pool.close()

    pdf_html = render_to_string('resources/base-resource-pdf.html', context)
    html = HTML(string=pdf_html, base_url=request.build_absolute_uri())
    base_css = CSS(string=open('static/css/print-resource-pdf.css', encoding='UTF-8').read())
    pdf_file = html.write_pdf(stylesheets=[base_css])

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = RESPONSE_CONTENT_DISPOSITION.format(filename=resource.name)
    return response


def generate_resource_image(get_request, resource, module_path, copy_num):
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
