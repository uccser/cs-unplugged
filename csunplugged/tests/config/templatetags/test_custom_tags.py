from django import template
from django.test import override_settings

from tests.BaseTest import BaseTest

AVAILABLE_LANGUAGES_EN = (
    ("en", "English"),
)


class CustomDictTagTest(BaseTest):

    def render_template(self, string, context):
        context = template.Context(context)
        return template.Template(string).render(context)

    @override_settings(LANGUAGES=AVAILABLE_LANGUAGES_EN)
    def test_get_dict_value(self):
        context = {
            "a_dictionary": {"test_key": "test_value"}
        }
        rendered = self.render_template("{% load custom_tags %}"
                                        "{% if a_dictionary|get_item:'test_key' == 'test_value' %}Hello{% endif %}",
                                        context)
        self.assertEqual(
            "Hello",
            rendered
        )

    @override_settings(LANGUAGES=AVAILABLE_LANGUAGES_EN)
    def test_get_nonexistant_dict_value(self):
        context = {
            "a_dictionary": {"test_key": "test_value"}
        }
        rendered = self.render_template("{% load custom_tags %}"
                                        "{% if a_dictionary|get_item:'bad_key' == 'test_value' %}Hello{% endif %}",
                                        context)
        self.assertEqual(
            "",
            rendered
        )
