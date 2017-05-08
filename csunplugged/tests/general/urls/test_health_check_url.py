from tests.BaseTestWithDB import BaseTestWithDB


class HealthCheckURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = 'en'

    def test_valid_health_check_request(self):
        response = self.client.get('/_ah/health')
        self.assertEqual(200, response.status_code)
