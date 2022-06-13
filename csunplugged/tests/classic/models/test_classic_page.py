from tests.BaseTestWithDB import BaseTestWithDB
from classic.models import ClassicPage


class ClassicPageModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_classic_page_str(self):
        page = ClassicPage(
            slug="page",
            name="Page",
            redirect="http://www.example.com",
        )
        self.assertEqual(page.__str__(), "Page")

    def test_classic_page_model_name(self):
        page = ClassicPage(
            slug="page",
            name="Page",
            redirect="http://www.example.com",
        )
        self.assertEqual(page.MODEL_NAME, "Classic CS Unplugged Page")

    def test_classic_page_model_get_absolute_url(self):
        page = ClassicPage(
            slug="page",
            name="Page",
            redirect="http://www.example.com",
        )
        self.assertEqual(
            page.get_absolute_url(),
            "http://www.example.com"
        )
