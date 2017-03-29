from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.utils.translation import activate


class BaseTest(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        """
        Called before each test.
        Sets the language to English, creates a new user and logs into the database
        """
        activate('en')

        self.client = Client()
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

    def tearDown(self):
        self.test_user.delete()
