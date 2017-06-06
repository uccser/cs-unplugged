import itertools
from render.tests.BaseResourceTest import BaseResourceTest


class SortingNetworkResourceTest(BaseResourceTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module = "sorting_network"

    def test_sorting_network_resource_generation_valid_configurations(self):
        BASE_URL = "resources/modulo-clock.html"
        TASK_TEMPLATE = {
            "resource_slug": "sorting-network",
            "resource_name": "Sorting Network",
            "resource_view": "sorting_network",
            "url": None
        }

        resource_module = self.load_module()
        valid_options = resource_module.valid_options()
        valid_options["header_text"] = ["", "Example header"]
        valid_options["copies"] = [1, 2, 5]
        valid_option_keys = sorted(valid_options)

        combinations = [
            dict(zip(valid_option_keys, product))
            for product in itertools.product(
                *(valid_options[valid_option_key] for valid_option_key in valid_option_keys))
        ]

        print()
        print("Testing Sorting Network:")
        for combination in combinations:
            print("   - Testing combination: {} ... ".format(combination), end="")
            url = BASE_URL + self.query_string(combination)
            task = TASK_TEMPLATE.copy()
            task.update(combination)
            task["url"] = url

            filename, pdf = self.generator.generate_resource_pdf(task)
            print("ok")
