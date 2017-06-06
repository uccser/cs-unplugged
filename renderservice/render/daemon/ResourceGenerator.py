"""Render Daemon for collecting and consuming render jobs."""
import os
import logging
import importlib
from io import BytesIO
from PIL import Image
from base64 import standard_b64encode
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from render.daemon.FileManager import FileManager

# Daemon Setup and Task Management Constants
STATIC_DIRECTORY = os.getenv("STATIC_DIRECTORY", "/renderservice/static_mnt")
TEMPLATE_DIRECTORY = os.getenv("TEMPLATE_DIRECTORY", "/renderservice/templates")

logger = logging.getLogger(__name__)

# File Generation and Processing Constants
MM_TO_PIXEL_RATIO = 3.78
A4_MM_SCALE = 267
LETTER_MM_SCALE = 249


class ResourceGenerator(object):
    """Turns a task into a pdf or image."""

    def __init__(self, *args, **kwargs):
        """Create a Render Daemon.

        Assumes that any SIGALRM signals are sent by itself for
        timeout exceptions.
        """
        super(ResourceGenerator, self).__init__(*args, **kwargs)
        self.file_manager = FileManager("/renderservice/static", STATIC_DIRECTORY, save_directory=STATIC_DIRECTORY)
        self.template_environment = Environment(
            loader=FileSystemLoader(TEMPLATE_DIRECTORY),
            autoescape=False
        )

    def generate_resource_pdf(self, task):
        """Return a response containing a generated PDF resource.

        Args:
            task: A dicitionary of values specifying the task.
                Must have:
                  - resource_slug
                  - resource_name
                  - resource_view
                  - header_text
                  - paper_size
                  - copies
                  - url

        Returns:
            Tuple of filename and PDF file of generated resource.
        """
        if task["paper_size"] is None:
            raise Exception()  # TODO

        module_path = "render.resources.{}".format(task["resource_view"])
        resource_image_generator = importlib.import_module(module_path)

        for option, values in resource_image_generator.valid_options().items():
            if option not in task.keys():
                raise Exception()  # TODO
            if task[option] not in values:
                raise Exception()  # TODO

        context = dict()
        context["resource_name"] = task["resource_name"]
        context["header_text"] = task["header_text"]
        context["url"] = task["url"]

        context["resource_images"] = []
        for copy in range(0, task["copies"]):
            context["resource_images"].append(
                self.generate_resource_image(task, resource_image_generator)
            )

        filename = "{} ({}).pdf".format(task["resource_name"], resource_image_generator.subtitle(task))
        context["filename"] = filename

        template_filename = task.get("template", "base-resource-pdf.html")
        css_filename = task.get("css", "css/print-resource-pdf.css")

        template = self.template_environment.get_template(template_filename)
        pdf_html = template.render(context)  # TODO: Future consider async
        html = HTML(string=pdf_html, base_url=STATIC_DIRECTORY)
        css_data = self.file_manager.load(css_filename).read()
        css_string = css_data.decode("utf-8")
        base_css = CSS(string=css_string)
        return filename, html.write_pdf(stylesheets=[base_css])

    def generate_resource_image(self, task, resource_image_generator):
        """Retrieve image(s) for one copy of resource from resource generator.

        Images are resized to size.

        Args:
            task: The specification of file to generate as a dictionary.
            resource_image_generator: The file generation module.

        Returns:
            List of Base64 strings of a generated resource images for one copy.
        """
        # Get images from resource image creator
        raw_images = resource_image_generator.resource_image(task, self.file_manager)
        if not isinstance(raw_images, list):
            raw_images = [raw_images]

        # Resize images to reduce file size
        max_pixel_height = 0
        if task["paper_size"].lower() == "a4":
            max_pixel_height = A4_MM_SCALE * MM_TO_PIXEL_RATIO
        elif task["paper_size"].lower() == "letter":
            max_pixel_height = LETTER_MM_SCALE * MM_TO_PIXEL_RATIO
        else:
            raise Exception()  # TODO

        images = []
        for image in raw_images:
            width, height = image.size
            if height > max_pixel_height:
                ratio = max_pixel_height / height
                width *= ratio
                height *= ratio
                image = image.resize((int(width), int(height)), Image.ANTIALIAS)

            # Save image to buffer
            image_buffer = BytesIO()
            image.save(image_buffer, format="PNG")

            # Add base64 of image to list of images
            images.append(standard_b64encode(image_buffer.getvalue()).decode())

        return images
