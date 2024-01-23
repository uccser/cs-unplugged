from http import HTTPStatus
from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from topics.models import GlossaryTerm


class GlossaryViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_glossary_with_no_definitions(self):
        url = reverse("topics:glossary")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(len(response.context["glossary_terms"]), 0)

    def test_glossary_with_one_definition(self):
        term = GlossaryTerm(
            slug="algorithm",
            term="Algorithms",
            definition="<p>Algorithms definition.</p>",
            languages=["en"]
        )
        term.save()

        url = reverse("topics:glossary")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(len(response.context["glossary_terms"]), 1)
        self.assertQuerysetEqual(
            response.context["glossary_terms"],
            ["<GlossaryTerm: Algorithms>"],
            transform=repr,
        )

    def test_glossary_with_two_definitions(self):
        term1 = GlossaryTerm(
            slug="algorithm",
            term="Algorithms",
            definition="<p>Algorithms definition.</p>",
            languages=["en"]
        )
        term1.save()
        term2 = GlossaryTerm(
            slug="pixel",
            term="Pixel",
            definition="<p>Pixel definition.</p>",
            languages=["en"]
        )
        term2.save()

        url = reverse("topics:glossary")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(len(response.context["glossary_terms"]), 2)
        self.assertQuerysetEqual(
            response.context["glossary_terms"],
            [
                "<GlossaryTerm: Algorithms>", 
                "<GlossaryTerm: Pixel>"
            ],
            transform=repr,
        )

    def test_glossary_order(self):
        term_c = GlossaryTerm(
            slug="c",
            term="C",
            definition="C",
            languages=["en"]
        )
        term_c.save()
        term_b = GlossaryTerm(
            slug="b",
            term="B",
            definition="B",
            languages=["en"]
        )
        term_b.save()
        term_a = GlossaryTerm(
            slug="a",
            term="A",
            definition="A",
            languages=["en"]
        )
        term_a.save()

        url = reverse("topics:glossary")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(len(response.context["glossary_terms"]), 3)
        self.assertQuerysetEqual(
            response.context["glossary_terms"],
            [
                "<GlossaryTerm: A>",
                "<GlossaryTerm: B>",
                "<GlossaryTerm: C>"
            ],
            transform=repr,
        )

    def test_glossary_json_with_one_definition(self):
        term = GlossaryTerm(
            slug="algorithm",
            term="Algorithms",
            definition="<p>Algorithms definition.</p>",
            languages=["en"]
        )
        term.save()

        url = reverse("topics:glossary_json")
        response = self.client.get(url, {"term": "algorithm"})
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            {
                "definition": "<p>Algorithms definition.</p>",
                "slug": "algorithm",
                "term": "Algorithms",
                "translated": True
            }
        )

    def test_glossary_json_with_two_definitions(self):
        term1 = GlossaryTerm(
            slug="algorithm",
            term="Algorithms",
            definition="<p>Algorithms definition.</p>",
            languages=["en"]
        )
        term1.save()
        term2 = GlossaryTerm(
            slug="pixel",
            term="Pixel",
            definition="<p>Pixel definition.</p>",
            languages=["en"]
        )
        term2.save()

        url = reverse("topics:glossary_json")
        response = self.client.get(url, {"term": "pixel"})
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            {
                "definition": "<p>Pixel definition.</p>",
                "slug": "pixel",
                "term": "Pixel",
                "translated": True
            }
        )

    def test_glossary_json_with_invalid_term(self):
        term = GlossaryTerm(
            slug="algorithm",
            term="Algorithms",
            definition="<p>Algorithms definition.</p>"
        )
        term.save()

        url = reverse("topics:glossary_json")
        response = self.client.get(url, {"term": "pixel"})
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_glossary_json_with_invalid_key(self):
        term = GlossaryTerm(
            slug="algorithm",
            term="Algorithms",
            definition="<p>Algorithms definition.</p>"
        )
        term.save()

        url = reverse("topics:glossary_json")
        response = self.client.get(url, {"word": "pixel"})
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)
