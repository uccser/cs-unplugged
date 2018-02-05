from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class CurriculumAreaModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_curriculum_area_str(self):
        area = self.test_data.create_curriculum_area(1)
        self.assertEqual(
            area.__str__(),
            "Area 1"
        )

    def test_curriculum_area_str_as_child(self):
        area_1 = self.test_data.create_curriculum_area(1)
        area_2 = self.test_data.create_curriculum_area(2, parent=area_1)
        self.assertEqual(
            area_2.__str__(),
            "Area 1: Area 2"
        )

    def test_curriculum_area_model_type(self):
        area = self.test_data.create_curriculum_area(1)
        self.assertEqual(
            area.model_type(),
            "Curriculum Area"
        )
