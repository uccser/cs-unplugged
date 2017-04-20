from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.utils.translation import activate


class BaseTestWithDB(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = None

    @classmethod
    def setUpTestData(self):
        '''Setup data for the whole class.
        '''
        pass

    @classmethod
    def setUpClass(self):
        '''Called before tests in class.
        '''
        super(BaseTestWithDB, self).setUpClass()
        self.client = Client()
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'

    @classmethod
    def tearDownClass(self):
        '''Called after tests in class.
        '''
        super(BaseTestWithDB, self).setUpClass()

    def setUp(self):
        '''Called before each test.
        Sets the language if specified, creates a new user and logs into the database
        '''
        if self.language is not None:
            activate(self.language)
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

    def tearDown(self):
        '''Called after each test.
        Deletes the user.
        '''
        self.test_user.delete()
