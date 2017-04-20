from django.test import SimpleTestCase
from django.test.client import Client
from django.utils.translation import activate


class BaseTest(SimpleTestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = None

    @classmethod
    def setUpClass(cls):
        '''Called before tests in class.
        '''
        super(BaseTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        '''Called after tests in class.
        '''
        super(BaseTest, cls).tearDownClass()

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
