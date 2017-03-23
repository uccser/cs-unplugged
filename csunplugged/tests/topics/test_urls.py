from tests.BaseTest import BaseTest
from topics import urls
from django.urls import reverse


class UrlsTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_topics_index(self):
        url = reverse('topics:index')
        self.assertEqual(url, '/en/topics/')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_topic(self):
        url = reverse('topics:topic', args=['binary-numbers'])
        self.assertEqual(url, '/en/topics/binary-numbers/')

        # response = self.client.get(url)
        # self.assertEqual(200, response.status_code)

    def test_missing_topic(self):
        pass
        # url = reverse('topics:topic')
        # response = self.client.get(url)
        # self.assertEqual(404, response.status_code)

    def test_activity(self):
        pass

    def test_other_resources(self):
        pass

    def test_plugged_in(self):
        pass

    def test_prog_ex(self):
        pass

    def test_prog_ex_solution(self):
        pass

    def test_unit_plan(self):
        pass

    def test_lesson(self):
        pass

    def test_difficulty(self):
        pass
