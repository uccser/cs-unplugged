"""Module for generating custom resource PDFs."""

from django.http import Http404
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders
from django.conf import settings
from PIL import Image
from io import BytesIO
import importlib
import base64

MM_TO_PIXEL_RATIO = 6


def generate_resource_pdf(request, resource, module_path):
    """Return a response containing a generated PDF resource.

    Args:
        request: HTTP request object (HttpRequest).
        resource: Object of resource data (Resource).
        module_path: Path to module for generating resource (str).

    Returns:
        Tuple of PDF file of generated resource and filename.
    """
    from weasyprint import HTML, CSS
    context = dict()
    get_request = request.GET
    context["resource"] = resource
    context["header_text"] = get_request.get("header_text", "")
    context["paper_size"] = get_request.get("paper_size", None)

    if context["paper_size"] is None:
        raise Http404("Paper size parameter not specified.")

    resource_generator = importlib.import_module(module_path)
    num_copies = range(0, int(get_request.get("copies", 1)))
    context["all_data"] = []
    for copy in num_copies:
        context["all_data"].append(
            generate_resource_copy(get_request, module_path)
        )

    filename = "{} ({})".format(resource.name, resource_generator.subtitle(get_request, resource))
    context["filename"] = filename

    pdf_html = render_to_string("resources/base-resource-pdf.html", context)
    html = HTML(string=pdf_html, base_url=settings.STATIC_ROOT)
    css_file = finders.find("css/print-resource-pdf.css")
    css_string = open(css_file, encoding="UTF-8").read()
    base_css = CSS(string=css_string)
    return (html.write_pdf(stylesheets=[base_css]), filename)


def generate_resource_copy(request, module_path):
    """Retrieve data for one copy of resource from resource generator.

    Images are resized to paper size.

    Args:
        request: HTTP request object (HttpRequest).
        resource: Object of resource data (Resource).
        module_path: Path to module for generating resource (str).

    Returns:
        List of lists containing data for one copy.
        Each inner list contains:
        - String of type ("image", "html")
        - Data of type:
            - String for HTML.
            - Base64 string of image.
    """
    resource_module = importlib.import_module(module_path)
    data = resource_generator.data(request.GET.items())
    if not isinstance(data, list):
        data = [data]

    if get_request["paper_size"] == "a4":
        max_pixel_height = 267 * MM_TO_PIXEL_RATIO
    elif get_request["paper_size"] == "letter":
        max_pixel_height = 249 * MM_TO_PIXEL_RATIO

    # Resize images to reduce file size
    for index in range(len(data)):
        if data[index]["type"] == "image":
            image = data[index]["data"]
            (width, height) = image.size
            if height > max_pixel_height:
                ratio = max_pixel_height / height
                width *= ratio
                height *= ratio
                image = image.resize((int(width), int(height)), Image.ANTIALIAS)
            # Convert from Image object to base64 string
            image_buffer = BytesIO()
            image.save(image_buffer, format="PNG")
            data[index]["data"] = base64.b64encode(image_buffer.getvalue())
    return data
