from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from tests.resources.views.ResourceViewBaseTest import ResourceViewBaseTest
from tests.create_query_string import query_string


@tag("resource")
class TrainStationsResourceViewTest(ResourceViewBaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_train_stations_resource_form_view(self):
        resource = self.test_data.create_resource(
            "train-stations",
            "Train Stations",
            "resources/train-stations.html",
            "TrainStationsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_train_stations_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "train-stations",
            "Train Stations",
            "resources/train-stations.html",
            "TrainStationsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        base_url = reverse("resources:generate", kwargs=kwargs)
        self.run_valid_configuration_tests(resource, base_url)

    def test_train_stations_resource_generation_missing_tracks_parameter(self):
        resource = self.test_data.create_resource(
            "train-stations",
            "Train Stations",
            "resources/train-stations.html",
            "TrainStationsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "paper_size": "a4",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_train_stations_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "train-stations",
            "Train Stations",
            "resources/train-stations.html",
            "TrainStationsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "tracks": "circular",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_train_stations_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "train-stations",
            "Train Stations",
            "resources/train-stations.html",
            "TrainStationsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "tracks": "circular",
            "paper_size": "a4",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        filename = "Resource Train Stations (circular tracks - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def subtitle(self, combination):
        """Return text of subtitle for given combination.

        Args:
            combination (dict): Dictionary of a valid combination

        Returns:
            String of subtitle.
        """
        text = "{} tracks - {}".format(
            combination["tracks"],
            combination["paper_size"],
        )
        return text
