from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client

from .models import Topic




class IndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'        
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

    def tearDown(self):
        self.test_user.delete()

    def test_index_with_no_topics(self):
        pass
        # url = reverse('topics:index')
        # response = self.client.get(url)
        # self.assertEqual(response.status_code, 200)

    def test_index_with_one_topic(self):
        new_topic = Topic(
            slug = 'binary-numbers',
            name='Binary Numbers',
            content = 'content',
            other_resources = 'content',
            icon = 'icon'
        )
        new_topic.save()
        print(new_topic)
        print(new_topic.id)
        print(Topic.objects.all())
        url = reverse('topics:index')
        response = self.client.get(url)
        print(response)
        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual(
            response.context['all_topics'],
            ['<Topic: Binary Numbers>']
        )
