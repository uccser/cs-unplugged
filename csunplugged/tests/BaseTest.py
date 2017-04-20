from django.test import SimpleTestCase
from django.test.client import Client
from django.utils.translation import activate


class BaseTest(SimpleTestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = None

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
        Sets the language if specified and creates a new client.
        '''
        if self.language is not None:
            activate(self.language)
        self.client = Client()

    def tearDown(self):
        '''Called after each test.
        '''
        pass
