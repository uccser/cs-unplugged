import json
from unittest import mock

from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    # Create mock JOBE server response when the api key is set to 'mockapikey'
    if args[0] == 'http://mockjobeserver/jobe/index.php/restapi/runs/' \
       and 'X-API-KEY' in kwargs['headers'] \
       and kwargs['headers']['X-API-KEY'] == 'mockapikey':
        return MockResponse('Hello World (with API key)', 200)

    # Create a mock JOBE server response when no api key is set
    elif args[0] == 'http://mockjobeserver/jobe/index.php/restapi/runs/':
        return MockResponse('Hello World', 200)


class JobeProxyViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def get_test_program_data(self, source_code):
        return {
            "run_spec": {
                "language_id": "python3",
                "sourcefilename": "test_program",
                "sourcecode": source_code,
                "input": "input"
            }
        }

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_valid_jobe_proxy_call(self, mock_post):
        test_program_data = self.get_test_program_data("print('Hello World')")

        url = reverse("plugging_it_in:jobe_proxy")

        # Set the settings variable to call the mock JOBE server
        with self.settings(JOBE_SERVER_URL='http://mockjobeserver'):
            response = self.client.post(url, json.dumps(test_program_data), content_type='application/json')

        # Assert that the function returns the correct response from the mock JOBE server.
        self.assertEqual(response.content.decode(), 'Hello World')

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_valid_jobe_proxy_call_with_api_key(self, mock_post):
        test_program_data = self.get_test_program_data("print('Hello World') (with API key)")

        url = reverse("plugging_it_in:jobe_proxy")

        # Set the settings variable to call the mock JOBE server
        with self.settings(JOBE_SERVER_URL='http://mockjobeserver'), self.settings(JOBE_API_KEY='mockapikey'):
            response = self.client.post(url, json.dumps(test_program_data), content_type='application/json')

        # Assert that the function returns the correct response from the mock JOBE server.
        self.assertEqual(response.content.decode(), 'Hello World (with API key)')
