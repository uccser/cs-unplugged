from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class UnitPlanURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_unit_plan(self):
        kwargs = {
            "topic_slug": "binary-numbers",
            "unit_plan_slug": "unit-plan",
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        self.assertEqual(url, "/en/topics/binary-numbers/unit-plan/")
