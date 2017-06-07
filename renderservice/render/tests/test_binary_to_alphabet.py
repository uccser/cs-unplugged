import itertools
from render.daemon.ResourceGenerator import TaskError
from render.tests.BaseResourceTest import BaseResourceTest


class BinaryToAlphabetResourceTest(BaseResourceTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module = "binary_to_alphabet"
        self.BASE_URL = "resources/binary-to-alphabet.html"
        self.TASK_TEMPLATE = {
            "resource_slug": "binary-to-alphabet",
            "resource_name": "Binary To Alphabet",
            "resource_view": "binary_to_alphabet",
            "url": None
        }

    def test_binary_to_alphabet_resource_generation_valid_configurations(self):
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
        print("Testing Binary To Alphabet:")
        for combination in combinations:
            print("   - Testing combination: {} ... ".format(combination), end="")
            url = self.BASE_URL + self.query_string(combination)
            task = self.TASK_TEMPLATE.copy()
            task.update(combination)
            task["url"] = url

            filename, pdf = self.generator.generate_resource_pdf(task)
            print("ok")

    def test_binary_to_alphabet_resource_generation_missing_worksheet_version_parameter(self):
        combination = {
            "paper_size": "letter",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_binary_to_alphabet_resource_generation_missing_paper_size_parameter(self):
        combination = {
            "worksheet_version": "student",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_binary_to_alphabet_resource_generation_missing_header_text_parameter(self):
        expected_filename="Binary To Alphabet (teacher - letter).pdf"
        combination = {
            "worksheet_version": "teacher",
            "paper_size": "letter",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        filename, pdf = self.generator.generate_resource_pdf(task)
        self.assertEqual(filename, expected_filename)
