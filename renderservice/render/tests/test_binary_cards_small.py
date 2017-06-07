import itertools
from render.daemon.ResourceGenerator import TaskError
from render.tests.BaseResourceTest import BaseResourceTest


class BinaryCardsSmallResourceTest(BaseResourceTest):

    def __init__(self, *args, **kwargs):
        super(BinaryCardsSmallResourceTest, self).__init__(*args, **kwargs)
        self.module = "binary_cards_small"
        self.BASE_URL = "resources/binary-cards-small.html"
        self.TASK_TEMPLATE = {
            "resource_slug": "binary-cards",
            "resource_name": "Binary Cards (small)",
            "resource_view": "binary_cards_small",
            "url": None
        }

    def test_binary_cards_small_resource_generation_valid_configurations(self):
        resource_module = self.load_module()
        valid_options = resource_module.valid_options()
        valid_options["header_text"] = ["", "Example header"]
        valid_options["copies"] = [1, 2]
        valid_option_keys = sorted(valid_options)

        combinations = [
            dict(zip(valid_option_keys, product))
            for product in itertools.product(
                *(valid_options[valid_option_key] for valid_option_key in valid_option_keys))
        ]

        print()
        print("Testing Binary Cards (small):")
        for combination in combinations:
            print("   - Testing combination: {} ... ".format(combination), end="")
            url = self.BASE_URL + self.query_string(combination)
            task = self.TASK_TEMPLATE.copy()
            task.update(combination)
            task["url"] = url

            filename, pdf = self.generator.generate_resource_pdf(task)
            print("ok")

    def test_binary_cards_small_resource_generation_missing_dot_count_parameter(self):
        combination = {
            "number_bits": "4",
            "black_back": "yes",
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

    def test_binary_cards_small_resource_generation_missing_black_back_parameter(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
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

    def test_binary_cards_small_resource_generation_missing_paper_size_parameter(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_binary_cards_small_resource_generation_missing_header_text_parameter(self):
        expected_filename = "Binary Cards (small) (4 bits - with dot counts - with black back - a4).pdf"
        combination = {
            "dot_counts": "yes",
            "number_bits": "4",
            "black_back": "yes",
            "paper_size": "a4",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        filename, pdf = self.generator.generate_resource_pdf(task)
        self.assertEqual(filename, expected_filename)
