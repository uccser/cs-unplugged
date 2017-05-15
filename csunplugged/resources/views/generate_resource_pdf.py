"""Module for generating custom resource PDFs."""

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders
from django.conf import settings
from PIL import Image
from io import BytesIO
import importlib
import base64

RESPONSE_CONTENT_DISPOSITION = 'attachment; filename="{filename}.pdf"'
MM_TO_PIXEL_RATIO = 3.78


def generate_resource_pdf(request, resource, module_path):
    """Return a response containing a generated PDF resource.

    Args:
        request: HTTP request object
        resource: Object of resource data.
        module_path: Path to module for generating resource.

    Returns:
        HTTP response containing generated resource PDF.
    """
    # TODO: Weasyprint handling in production
    import environ
    env = environ.Env(
        DJANGO_PRODUCTION=(bool),
    )
    if env("DJANGO_PRODUCTION"):
        return HttpResponse("<html><body>PDF generation is currently not supported in production.</body></html>")
    else:
        from weasyprint import HTML, CSS
        context = dict()
        get_request = request.GET
        context["paper_size"] = get_request["paper_size"]
        context["resource"] = resource
        context["header_text"] = get_request["header_text"]

        resource_image_generator = importlib.import_module(module_path)
        filename = "{} ({})".format(resource.name, resource_image_generator.subtitle(get_request, resource))
        context["filename"] = filename

        num_copies = range(0, int(get_request.get("copies", 1)))
        context["resource_images"] = []
        for copy in num_copies:
            context["resource_images"].append(
                generate_resource_image(get_request, resource, module_path)
            )

        pdf_html = render_to_string("resources/base-resource-pdf.html", context)
        html = HTML(string=pdf_html, base_url=settings.STATIC_ROOT)
        css_file = finders.find("css/print-resource-pdf.css")
        css_string = open(css_file, encoding="UTF-8").read()
        base_css = CSS(string=css_string)
        pdf_file = html.write_pdf(stylesheets=[base_css])

        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = RESPONSE_CONTENT_DISPOSITION.format(filename=filename)
        return response


def generate_resource_image(get_request, resource, module_path):
    """Retrieve image(s) for one copy of resource from resource generator.

    Images are resized to size.

    Args:
        get_request: HTTP request object
        resource: Object of resource data.
        module_path: Path to module for generating resource.

    Returns:
        List of Base64 strings of a generated resource images for one copy.
    """
    # Get images from resource image creator
    resource_image_generator = importlib.import_module(module_path)
    raw_images = resource_image_generator.resource_image(get_request, resource)
    if not isinstance(raw_images, list):
        raw_images = [raw_images]

    # Resize images to reduce file size
    if get_request["paper_size"] == "a4":
        max_pixel_height = 267 * MM_TO_PIXEL_RATIO
    elif get_request["paper_size"] == "letter":
        max_pixel_height = 249 * MM_TO_PIXEL_RATIO

    images = []
    for image in raw_images:
        (width, height) = image.size
        if height > max_pixel_height:
            ratio = max_pixel_height / height
            width *= ratio
            height *= ratio
            image = image.resize((int(width), int(height)), Image.ANTIALIAS)

        # Save image to buffer
        image_buffer = BytesIO()
        image.save(image_buffer, format="PNG")
        # Add base64 of image to list of images
        images.append(base64.b64encode(image_buffer.getvalue()))

    return images
