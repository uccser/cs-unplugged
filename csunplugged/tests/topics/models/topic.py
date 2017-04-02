from tests.BaseTest import BaseTest
from topics.models import Topic


class TopicModelTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_topic(self):
        new_topic = Topic.objects.create(
            slug='binary-numbers',
            name='Binary Numbers',
            content='content',
            other_resources='content',
            icon='icon'
        )
        query_result = Topic.objects.get(name='Binary Numbers')
        self.assertEqual(query_result, new_topic)
