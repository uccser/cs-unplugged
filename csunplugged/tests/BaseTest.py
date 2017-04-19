from django.test import SimpleTestCase
from django.test.client import Client
from django.utils.translation import activate


class BaseTest(SimpleTestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def setUpClass(self):
        '''Called before tests in class.
        '''
        super(BaseTest, self).setUpClass()

    @classmethod
    def tearDownClass(self):
        '''Called after tests in class.
        '''
        super(BaseTest, self).setUpClass()

    def setUp(self):
        '''Called before each test.
        Sets the language to English, and creates a new client.
        '''
        activate('en')
        self.client = Client()

    def tearDown(self):
        '''Called after each test.
        Deletes the user.
        '''
        self.test_user.delete()
