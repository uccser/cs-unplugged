"""Base test class with methods implemented for Django testing."""

from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.utils.translation import activate


class BaseTest(TestCase):
    """Base test class with methods implemented for Django testing."""

    def __init__(self, *args, **kwargs):
        """Create the BaseTest object by calling the parent's constructor."""
        TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        """Automatically called before each test.

        Sets the language to English, creates a new user and logs into the database.
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
        """Automatically called after each test.

        Deletes test user.
        """
        self.test_user.delete()
