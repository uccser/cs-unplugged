from tests.BaseTest import BaseTest
from topics.models import Topic


class ModelTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_topic_str(self):
        new_topic = Topic(
            slug='binary-numbers',
            name='Binary Numbers',
            content='content',
            other_resources='content',
            icon='icon'
        )
        self.assertEqual(new_topic.__str__(), 'Binary Numbers')
