from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class UnitPlanDescriptionURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_unit_plan_description(self):
        url = reverse("topics:unit_plan_description", args=["binary-numbers", "unit-plan"])
        self.assertEqual(url, "/en/topics/binary-numbers/unit-plan/description/")
