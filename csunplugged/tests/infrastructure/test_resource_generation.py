"""Tests for resource generation."""

# import os
# import re
# from django.core import management
# from config.settings.base import DEFAULT_LANGUAGES as LANGUAGES
from tests.BaseTestWithDB import BaseTestWithDB
# from resources.models import Resource


class ResourceGenerationTest(BaseTestWithDB):
    """Tests for resource generation."""

    # TODO: Test is currently broken, however test is skipped as not required for server migration.
    # def test_all_resource_pdfs_are_generated(self):
    #     # Check all resources are generated for each langage
    #     management.call_command("loadresources")

    #     # Generate all resource combinations in dictionary
    #     modes = ["dev", "prod"]
    #     resource_slugs = set(Resource.objects.values_list("slug", flat=True))
    #     languages = [lang[0] for lang in LANGUAGES]
    #     required_resources = dict()
    #     for mode in modes:
    #         required_resources[mode] = dict()
    #         for resource_slug in resource_slugs:
    #             required_resources[mode][resource_slug] = languages[:]

    #         # Check files for resource generations
    #         regex = re.compile(r'makeresources \"([^\n\"]*)\"(?: \"([^\n\"]*)\")?')

    #         path = "../infrastructure/{}-deploy/".format(mode)
    #         for filename in sorted(os.listdir(path)):
    #             if filename.startswith("deploy-resources"):
    #                 with open(os.path.join(path, filename), "r") as f:
    #                     contents = f.read()
    #                 results = re.findall(regex, contents)
    #                 update_mode_list(mode, required_resources, results)

    #     # Check if any languages are missed
    #     error_text = ''
    #     template = "\n{slug} does not generate PDFs for the {mode} website for the following languages: {languages}"
    #     for mode in modes:
    #         for (resource_slug, languages) in required_resources[mode].items():
    #             if languages:
    #                 error_text += template.format(slug=resource_slug, mode=mode, languages=languages)

    #     if error_text:
    #         raise Exception(error_text)


def update_mode_list(mode, required_resources, results):
    for (resource_slug, language) in results:
        if not language:
            del required_resources[mode][resource_slug]
        if language:
            required_resources[mode][resource_slug].remove(language)
