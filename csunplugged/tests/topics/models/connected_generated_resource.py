from model_mommy import mommy
from tests.BaseTest import BaseTest
from topics.models import ConnectedGeneratedResource
from topics.models import Lesson
from resources.models import Resource


class ConnectedGeneratedResourceModelTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_connected_generated_resource(self):
        resource = mommy.make(Resource)
        lesson = mommy.make(Lesson)
        new_resource = ConnectedGeneratedResource.objects.create(
            resource=resource,
            lesson=lesson,
            description='this is a description'
        )
        query_result = ConnectedGeneratedResource.objects.get(pk=1)
        self.assertEqual(query_result, new_resource)
