from django.http import QueryDict
from django.test import tag
from resources.generators.JobBadgesResourceGenerator import JobBadgesResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class JobBadgesResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_data(self):
        generator = JobBadgesResourceGenerator()
        data = generator.data()
        self.assert_data_valid(data)

    def test_subtitle_a4(self):
        query = QueryDict("paper_size=a4")
        generator = JobBadgesResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "a4"
        )

    def test_subtitle_letter(self):
        query = QueryDict("paper_size=letter")
        generator = JobBadgesResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "letter"
        )
