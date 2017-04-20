from tests.BaseTestWithDB import BaseTestWithDB
from topics.models import CurriculumArea


class CurriculumAreaModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_curriculum_area(self):
        new_curriculum_area = CurriculumArea.objects.create(
            slug='slug',
            name='name',
        )
        print(CurriculumArea.objects.count())
        query_result = CurriculumArea.objects.get(slug='slug')
        self.assertEqual(query_result, new_curriculum_area)
