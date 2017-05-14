from django import template

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TestDataGenerator import TestDataGenerator

from topics.models import CurriculumIntegration


class RenderHTMLFieldTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TestDataGenerator()

    def render_template(self, string, context=None):
        context = context or {}
        context = template.Context(context)
        return template.Template(string).render(context)

    def test_render_html_field_without_static(self):
        topic = self.test_data.create_test_topic(1)
        curriculum_integration_without_static = CurriculumIntegration.objects.create(
            topic=topic,
            slug="slug-1",
            number=1,
            name="1",
            content="<p>Example text.</p>"
        )
        context = {"integration": curriculum_integration_without_static}
        rendered = self.render_template(
            "{% load render_html_field %}\n{% render_html_field integration.content %}",
            context
        )
        self.assertHTMLEqual(rendered, "<p>Example text.</p>")

    def test_render_html_field_with_static(self):
        topic = self.test_data.create_test_topic(1)
        curriculum_integration_with_static = CurriculumIntegration.objects.create(
            topic=topic,
            slug="slug-2",
            number=2,
            name="2",
            content="<img src='{% static 'img/logo-small.png' %}'>"
        )
        context = {"integration": curriculum_integration_with_static}
        rendered = self.render_template(
            "{% load render_html_field %}\n{% render_html_field integration.content %}",
            context
        )
        self.assertHTMLEqual(rendered, "<img src='/staticfiles/img/logo-small.png'>")

    def test_render_html_field_empty(self):
        topic = self.test_data.create_test_topic(1)
        curriculum_integration_empty = CurriculumIntegration.objects.create(
            topic=topic,
            slug="slug-3",
            number=3,
            name="3",
            content=""
        )
        context = {"integration": curriculum_integration_empty}
        rendered = self.render_template(
            "{% load render_html_field %}\n{% render_html_field integration.content %}",
            context
        )
        self.assertEqual(rendered.strip(), "")

    def test_render_html_field_zero_parameters(self):
        self.assertRaises(
            template.TemplateSyntaxError,
            self.render_template,
            "{% load render_html_field %}\n{% render_html_field %}"
        )

    def test_render_html_field_two_parameters(self):
        self.assertRaises(
            template.TemplateSyntaxError,
            self.render_template,
            "{% load render_html_field %}\n{% render_html_field param1 param2 %}"
        )

    def test_render_html_field_invalid_parameter(self):
        topic = self.test_data.create_test_topic(1)
        curriculum_integration_with_static = CurriculumIntegration.objects.create(
            topic=topic,
            slug="slug-2",
            number=2,
            name="2",
            content="<img src='{% static 'img/logo-small.png' %}'>"
        )
        context = {"integration": curriculum_integration_with_static}
        self.assertRaises(
            template.TemplateSyntaxError,
            self.render_template,
            "{% load render_html_field %}\n{% render_html_field integration.topic %}",
            context
        )

    def test_render_html_field_missing_parameter(self):
        topic = self.test_data.create_test_topic(1)
        curriculum_integration_with_static = CurriculumIntegration.objects.create(
            topic=topic,
            slug="slug-2",
            number=2,
            name="2",
            content="<img src='{% static 'img/logo-small.png' %}'>"
        )
        context = {"integration": curriculum_integration_with_static}
        self.assertRaises(
            template.TemplateSyntaxError,
            self.render_template,
            "{% load render_html_field %}\n{% render_html_field integration.invalid %}",
            context
        )
