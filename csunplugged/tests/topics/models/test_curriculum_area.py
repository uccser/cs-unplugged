from tests.BaseTestWithDB import BaseTestWithDB
from topics.models import CurriculumArea


class CurriculumAreaModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_curriculum_area(self):
        new_curriculum_area = CurriculumArea.objects.create(
            slug="slug",
            name="name",
            colour="red",
        )
        query_result = CurriculumArea.objects.get(slug="slug")
        self.assertEqual(query_result, new_curriculum_area)

    def test_curriculum_area_str(self):
        new_curriculum_area = CurriculumArea.objects.create(
            slug="slug",
            name="name",
            colour="red",
        )
        self.assertEqual(new_curriculum_area.__str__(), "name")

    def test_curriculum_area_str_as_child(self):
        parent_curriculum_area = CurriculumArea.objects.create(
            slug="parent-slug",
            name="parent name",
            colour="red",
        )
        child_curriculum_area = CurriculumArea.objects.create(
            slug="child-slug",
            name="child name",
            colour="red",
            parent=parent_curriculum_area,
        )
        self.assertEqual(child_curriculum_area.__str__(), "parent name: child name")
