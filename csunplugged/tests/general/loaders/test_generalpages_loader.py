from os.path import join, dirname
from django.conf import settings
from django.test import override_settings
from tests.BaseTestWithDB import BaseTestWithDB
from general.models import GeneralPage
from general.management.commands._GeneralPagesLoader import GeneralPagesLoader

BASE_PATH = "tests/general/loaders/assets/"
test_template_settings = settings.TEMPLATES
default_path = test_template_settings[0]["DIRS"][0]
new_path = join(dirname(default_path), BASE_PATH, "templates/")
test_template_settings[0]["DIRS"].append(new_path)
url_conf = join(BASE_PATH, "urls").replace("/", ".")


@override_settings(TEMPLATES=test_template_settings)
@override_settings(ROOT_URLCONF=url_conf)
class GeneralPageLoaderTest(BaseTestWithDB):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loader_name = "generalpage"
        self.BASE_PATH = join(BASE_PATH, "generalpages/")

    def test_basic_generalpage_loader_config(self):
        config_file = "basic-config.yaml"
        generalpage_loader = GeneralPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        generalpage_loader.load()
        pages = GeneralPage.objects.all()
        self.assertEqual(1, len(pages))
        page = pages[0]
        self.assertEqual("General page", page.name)
        self.assertEqual("general-page", page.slug)
        self.assertEqual("template.html", page.template)
        self.assertEqual("page", page.url_name)
