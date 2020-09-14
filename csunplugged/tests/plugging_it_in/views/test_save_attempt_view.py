import json

from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class SaveAttemptViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_save_new_attempt_response(self):
        new_attempt = {
            "challenge": "test_challenge",
            "attempt": "print('Hello World')",
            "status": "passed"
        }

        url = reverse("plugging_it_in:save_attempt")
        response = self.client.post(url, json.dumps(new_attempt), content_type='application/json')

        self.assertEqual(
            response.content.decode(),
            "Saved the attempt."
        )

    def test_save_new_attempt_session(self):
        new_attempt = {
            "challenge": "test_challenge",
            "attempt": "print('Hello World')",
            "status": "passed"
        }

        url = reverse("plugging_it_in:save_attempt")
        self.client.post(url, json.dumps(new_attempt), content_type='application/json')

        self.assertEqual(
            self.client.session['saved_attempts']['test_challenge'],
            {
                "status": "passed",
                "code": "print('Hello World')"
            }
        )

    def test_save_empty_attempt_response(self):
        new_attempt = {
            "challenge": "",
            "attempt": "",
            "status": ""
        }

        url = reverse("plugging_it_in:save_attempt")
        response = self.client.post(url, json.dumps(new_attempt), content_type='application/json')

        self.assertEqual(
            response.content.decode(),
            "Response does not need to be saved."
        )

    def test_save_empty_attempt_session(self):
        new_attempt = {
            "challenge": "",
            "attempt": "",
            "status": ""
        }

        url = reverse("plugging_it_in:save_attempt")
        self.client.post(url, json.dumps(new_attempt), content_type='application/json')

        self.assertEqual(
            self.client.session['saved_attempts'],
            {}
        )

    def test_save_started_attempt_response(self):
        new_attempt = {
            "challenge": "test_challenge",
            "attempt": "print('Hello World')",
            "status": "started"
        }

        url = reverse("plugging_it_in:save_attempt")
        response = self.client.post(url, json.dumps(new_attempt), content_type='application/json')

        self.assertEqual(
            response.content.decode(),
            "Saved the attempt."
        )

    def test_save_started_attempt_session(self):
        new_attempt = {
            "challenge": "test_challenge",
            "attempt": "print('Hello World')",
            "status": "started"
        }

        url = reverse("plugging_it_in:save_attempt")
        self.client.post(url, json.dumps(new_attempt), content_type='application/json')

        self.assertEqual(
            self.client.session['saved_attempts']['test_challenge'],
            {
                "status": "started",
                "code": "print('Hello World')"
            }
        )

    def test_save_started_attempt_following_passed_attempt_response(self):
        first_attempt = {
            "challenge": "test_challenge",
            "attempt": "print('Hello World')",
            "status": "passed"
        }

        second_attempt = {
            "challenge": "test_challenge",
            "attempt": "print('Hello World')",
            "status": "started"
        }

        url = reverse("plugging_it_in:save_attempt")

        # First save is a passed attempt
        self.client.post(url, json.dumps(first_attempt), content_type='application/json')

        # Second save is a started attempt
        response = self.client.post(url, json.dumps(second_attempt), content_type='application/json')

        # The second attempt should not be saved as started since this overrides a passed attempt
        self.assertEqual(
            response.content.decode(),
            "Response does not need to be saved."
        )

    def test_save_started_attempt_following_passed_attempt_session(self):
        first_attempt = {
            "challenge": "test_challenge",
            "attempt": "print('Hello World')",
            "status": "passed"
        }

        second_attempt = {
            "challenge": "test_challenge",
            "attempt": "print('Hello World')",
            "status": "started"
        }

        url = reverse("plugging_it_in:save_attempt")

        # First save is a passed attempt
        self.client.post(url, json.dumps(first_attempt), content_type='application/json')

        # Second save is a started attempt
        self.client.post(url, json.dumps(second_attempt), content_type='application/json')

        # The first attempt should be retained since it has been checked
        self.assertEqual(
            self.client.session['saved_attempts']['test_challenge'],
            {
                "status": "passed",
                "code": "print('Hello World')"
            }
        )
