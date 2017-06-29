"""Test the resource generator for expected failures."""
from render.tests.BaseResourceTest import BaseResourceTest
from render.daemon.ResourceGenerator import ResourceGenerator, TaskError


class ResourceGeneratorTest(BaseResourceTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generator = ResourceGenerator()
        self.BASE_URL = "resources/binary-cards.html"
        self.TASK_TEMPLATE = {
            "resource_slug": "binary-cards",
            "resource_name": "Binary Cards",
            "resource_view": "binary_cards",
            "url": None
        }

    def test_task_missing_resource_slug(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "paper_size": "a4",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        task.pop("resource_slug")
        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_task_missing_resource_name(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "paper_size": "a4",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        task.pop("resource_name")
        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_task_missing_resource_view(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "paper_size": "a4",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        task.pop("resource_view")
        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_task_missing_paper_size(self):
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

    def test_task_missing_copies(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "paper_size": "a4",
            "header_text": ""
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_task_missing_url(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "paper_size": "a4",
            "header_text": "",
            "copies": 1
        }

        task = self.TASK_TEMPLATE.copy()
        task.update(combination)

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_invalid_resource_view(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "paper_size": "a4",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        task["resource_view"] = "invalid_resource.py"
        with self.assertRaises(ImportError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_invalid_paper_size(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "paper_size": "a0",
            "header_text": "",
            "copies": 1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)

    def test_invalid_copies(self):
        combination = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "paper_size": "a4",
            "header_text": "",
            "copies": -1
        }

        url = self.BASE_URL + self.query_string(combination)
        task = self.TASK_TEMPLATE.copy()
        task.update(combination)
        task["url"] = url

        with self.assertRaises(TaskError):
            filename, pdf = self.generator.generate_resource_pdf(task)
