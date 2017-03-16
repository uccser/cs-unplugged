from django.test import TestCase
from django.urls import reverse

from .models import Topic


class IndexViewTest(TestCase):

    def test_index_with_no_topics(self):
        pass
        # response = self.client.get(reverse('topics:index'))
        # self.assertEqual(response.status_code, 200)

    def test_index_with_one_topic(self):
        Topic.objects.create(name='Binary Numbers')
        response = self.client.get(reverse('topics:index'))
        print(response)
        self.assertQuerysetEqual(
            response.context['all_topics'],
            ['<Topic: Binary Numbers>']
        )
