"""Tests for resource generation."""

import os
import re
from django.core import management
from tests.BaseTestWithDB import BaseTestWithDB
from resources.models import Resource


class ResourceGenerationTest(BaseTestWithDB):
    """Tests for resource generation."""

    def test_all_resources_are_generated(self):
        # Check all resources are generated for each langage
        management.call_command("loadresources")
        modes = ["dev", "prod"]
        for mode in modes:
            generated_resource_names = set()
            path = "../infrastructure/{}-deploy/".format(mode)
            for filename in sorted(os.listdir(path)):
                if filename.startswith("deploy-resources"):
                    with open(os.path.join(path, filename), "r") as f:
                        contents = f.read()
                    results = re.findall(
                        'makeresources \"(?P<resource_name>[^\"]*)\"',
                        contents,
                        re.M
                    )
                    generated_resource_names.update(results)
            self.assertEqual(
                generated_resource_names,
                set(Resource.objects.values_list("name", flat=True))
            )
