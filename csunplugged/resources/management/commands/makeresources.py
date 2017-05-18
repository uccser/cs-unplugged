"""Module for the custom Django makestaticresources command."""

import os
import os.path
import importlib
import itertools
from django.core.management.base import BaseCommand
from django.http.request import HttpRequest
from resources.models import Resource
from resources.views.generate_resource_pdf import generate_resource_pdf


class Command(BaseCommand):
    """Required command class for the custom Django makestaticresources command."""

    help = "Creates static PDF files of resource combinations."

    def handle(self, *args, **options):
        """Automatically called when the makestaticresources command is given."""
        BASE_PATH = "staticfiles/resources/"
        if not os.path.exists(BASE_PATH):
            os.makedirs(BASE_PATH)

        for resource in Resource.objects.all():
            # Get path to resource module
            resource_view = resource.generation_view
            if resource_view.endswith(".py"):
                resource_view = resource_view[:-3]
            module_path = "resources.views.{}".format(resource_view)
            # Save resource module
            resource_module = importlib.import_module(module_path)
            valid_options = resource_module.valid_options()
            valid_option_keys = sorted(valid_options)
            combinations = [dict(zip(valid_option_keys, product)) for product in itertools.product(*(valid_options[valid_option_key] for valid_option_key in valid_option_keys))]  # noqa: E501
            # Create PDF for all possible combinations
            for combination in combinations:
                request = HttpRequest()
                if resource.copies:
                    combination["copies"] = 30
                request.GET = combination
                (pdf_file, filename) = generate_resource_pdf(request, resource, module_path)
                filename = "{}.pdf".format(filename)
                pdf_file_output = open(os.path.join(BASE_PATH, filename), "wb")
                pdf_file_output.write(pdf_file)
                pdf_file_output.close()
                print("Created {}".format(filename))
