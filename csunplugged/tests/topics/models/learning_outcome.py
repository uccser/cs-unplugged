from tests.BaseTest import BaseTest

class LearningOutcomeModelTest(BaseTest):

    def __init__(self):
        pass

    def arbitrary_test(self):
        print('here')
        new_topic = Topic(
            slug='binary-numbers',
            name='Binary Numbers',
            content='content',
            other_resources='content',
            icon='icon'
        )
        self.assertEqual(new_topic.__str__(), 'Binary Numbers')