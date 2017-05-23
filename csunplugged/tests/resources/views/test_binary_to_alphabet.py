from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from utils.create_query_string import query_string


class BinaryToAlphabetResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_binary_to_alphabet_resource_form_view(self):
        resource = self.test_data.create_test_resource(
            "binary-to-alphabet",
            "Binary To Alphabet",
            "resources/binary-to-alphabet.html",
            "binary_to_alphabet.py"
        )
        kwargs = {
            "resource_slug": resource.slug
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_binary_to_alphabet_resource_generation_student_a4(self):
        resource = self.test_data.create_test_resource(
            "binary-to-alphabet",
            "Binary To Alphabet",
            "resources/binary-to-alphabet.html",
            "binary_to_alphabet.py"
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "worksheet_version": "student",
            "paper_size": "a4",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary To Alphabet (student - a4).pdf"'
        )

    def test_binary_to_alphabet_resource_generation_student_letter(self):
        resource = self.test_data.create_test_resource(
            "binary-to-alphabet",
            "Binary To Alphabet",
            "resources/binary-to-alphabet.html",
            "binary_to_alphabet.py"
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "worksheet_version": "student",
            "paper_size": "letter",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary To Alphabet (student - letter).pdf"'
        )

    def test_binary_to_alphabet_resource_generation_teacher_a4(self):
        resource = self.test_data.create_test_resource(
            "binary-to-alphabet",
            "Binary To Alphabet",
            "resources/binary-to-alphabet.html",
            "binary_to_alphabet.py"
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "worksheet_version": "teacher",
            "paper_size": "a4",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary To Alphabet (teacher - a4).pdf"'
        )

    def test_binary_to_alphabet_resource_generation_teacher_letter(self):
        resource = self.test_data.create_test_resource(
            "binary-to-alphabet",
            "Binary To Alphabet",
            "resources/binary-to-alphabet.html",
            "binary_to_alphabet.py"
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "worksheet_version": "teacher",
            "paper_size": "letter",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary To Alphabet (teacher - letter).pdf"'
        )

    def test_binary_to_alphabet_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-to-alphabet",
            "Binary To Alphabet",
            "resources/binary-to-alphabet.html",
            "binary_to_alphabet.py"
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "worksheet_version": "teacher",
            "paper_size": "letter",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary To Alphabet (teacher - letter).pdf"'
        )

    def test_binary_to_alphabet_resource_generation_missing_worksheet_version_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-to-alphabet",
            "Binary To Alphabet",
            "resources/binary-to-alphabet.html",
            "binary_to_alphabet.py"
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "paper_size": "letter",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_binary_to_alphabet_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-to-alphabet",
            "Binary To Alphabet",
            "resources/binary-to-alphabet.html",
            "binary_to_alphabet.py"
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "worksheet_version": "student",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
