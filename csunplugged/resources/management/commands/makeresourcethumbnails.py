"""Module for the custom Django makeresourcethumbnails command."""

import os
import os.path
from urllib.parse import urlencode
from tqdm import tqdm
from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.http.request import QueryDict
from resources.models import Resource
from resources.views.views import generate_resource_copy
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.resource_valid_test_configurations import resource_valid_test_configurations
from utils.bool_to_yes_no import bool_to_yes_no

BASE_PATH_TEMPLATE = "build/img/resources/{resource}/thumbnails/"


class Command(BaseCommand):
    """Required command class for the custom Django makeresourcethumbnails command."""

    help = "Creates thumbnail images of resource combinations."

    def handle(self, *args, **options):
        """Automatically called when makeresourcethumbnails command is given."""
        resources = Resource.objects.order_by("name")

        for resource in resources:
            base_path = BASE_PATH_TEMPLATE.format(resource=resource.slug)
            if not os.path.exists(base_path):
                os.makedirs(base_path)

            # TODO: Import repeated in next for loop, check alternatives
            empty_generator = get_resource_generator(resource.generator_module)
            combinations = resource_valid_test_configurations(
                empty_generator.valid_options,
                header_text=False
            )

            # Create thumbnail for all possible combinations
            print("Creating thumbnails for {}".format(resource.name))
            progress_bar = tqdm(combinations, ascii=True)

            for combination in progress_bar:
                requested_options = QueryDict(urlencode(combination, doseq=True))
                generator = get_resource_generator(resource.generator_module, requested_options)

                thumbnail = generate_resource_thumbnail(resource.name, generator)

                filename = resource.slug + "-"
                for (key, value) in sorted(combination.items()):
                    filename += "{}-{}-".format(key, bool_to_yes_no(value))
                filename = "{}.png".format(filename[:-1])
                thumbnail_file = open(os.path.join(base_path, filename), "wb")
                thumbnail_file.write(thumbnail)
                thumbnail_file.close()


def generate_resource_thumbnail(name, generator):
    """Return image of thumbnail for of PDF resource.

    Args:
        name: Name of resource to be created (str).
        generator: Instance of specific resource generator class.

    Returns:
        Thumbnail of generated resource.
    """
    from weasyprint import HTML, CSS

    context = dict()
    context["resource"] = name
    context["paper_size"] = generator.requested_options["paper_size"]
    context["all_data"] = [generate_resource_copy(generator, thumbnail=True)]
    pdf_html = render_to_string("resources/base-resource-pdf.html", context)
    html = HTML(string=pdf_html, base_url=settings.BUILD_ROOT)
    css_file = finders.find("css/print-resource-pdf.css")
    css_string = open(css_file, encoding="UTF-8").read()
    base_css = CSS(string=css_string)
    return html.write_png(stylesheets=[base_css], resolution=72)
