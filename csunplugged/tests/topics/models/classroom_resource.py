from tests.BaseTestWithDB import BaseTestWithDB
from topics.models import ClassroomResource


class ClassroomResourceModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_classroom_resource(self):
        new_resource = ClassroomResource.objects.create(
            text='this is a resource'
        )
        query_result = ClassroomResource.objects.get(pk=1)
        self.assertEqual(query_result, new_resource)
