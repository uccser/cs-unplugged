from tests.BaseTest import BaseTest
from django.urls import reverse


class UnitPlanURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_valid_unit_plan(self):
        url = reverse('topics:unit_plan', args=['binary-numbers', 'unit-plan'])
        self.assertEqual(url, '/en/topics/binary-numbers/unit-plan/')
