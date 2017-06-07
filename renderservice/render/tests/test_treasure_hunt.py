import itertools
from render.daemon.ResourceGenerator import TaskError
from render.tests.BaseResourceTest import BaseResourceTest


class TreasureHuntResourceTest(BaseResourceTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module = "treasure_hunt"
        self.BASE_URL = "resources/treasure-hunt.html"
        self.TASK_TEMPLATE = {
            "resource_slug": "treasure-hunt",
            "resource_name": "Treasure Hunt",
            "resource_view": "treasure_hunt",
            "url": None
        }

    def test_treasure_hunt_resource_generation_valid_configurations(self):
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
        print("Testing Treasure Hunt:")
        for combination in combinations:
            print("   - Testing combination: {} ... ".format(combination), end="")
            url = self.BASE_URL + self.query_string(combination)
            task = self.TASK_TEMPLATE.copy()
            task.update(combination)
            task["url"] = url

            filename, pdf = self.generator.generate_resource_pdf(task)
            print("ok")

    def test_treasure_hunt_resource_generation_missing_prefilled_values_parameter(self):
        combination = {
            "number_order": "sorted",
            "paper_size": "a4",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_treasure_hunt_resource_generation_missing_number_order_parameter(self):
        combination = {
            "prefilled_values": "blank",
            "paper_size": "a4",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_treasure_hunt_resource_generation_missing_paper_size_parameter(self):
        combination = {
            "prefilled_values": "blank",
            "number_order": "sorted",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_treasure_hunt_generation_missing_header_text_parameter(self):
        expected_filename = "Treasure Hunt (blank - a4).pdf"
        combination = {
            "prefilled_values": "blank",
            "number_order": "sorted",
            "paper_size": "a4",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        filename, pdf = self.generator.generate_resource_pdf(task)
        self.assertEqual(filename, expected_filename)
