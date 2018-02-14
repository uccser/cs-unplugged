from django.test import override_settings
from tests.BaseTestWithDB import BaseTestWithDB
from general.models import GeneralPage


class GeneralPageModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_general_page_str(self):
        page = GeneralPage(
            slug="page",
            name="Page",
            template="template.html",
            url_name="url",
        )
        self.assertEqual(page.__str__(), "Page")

    def test_general_page_model_type(self):
        page = GeneralPage(
            slug="page",
            name="Page",
            template="template.html",
            url_name="url",
        )
        self.assertEqual(page.model_type(), "General page")

    @override_settings(ROOT_URLCONF="tests.general.models.assets.urls")
    def test_general_page_model_get_absolute_url(self):
        page = GeneralPage(
            slug="page",
            name="Page",
            template="template.html",
            url_name="url",
        )
        self.assertEqual(
            page.get_absolute_url(),
            "/valid-url"
        )
