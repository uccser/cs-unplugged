from tests.BaseTest import BaseTest
from resources.utils.get_options_html import get_options_html
from resources.utils.resource_parameters import EnumResourceParameter
from lxml import etree
from django.test import override_settings


class GetOptionsHTMLTest(BaseTest):
    def test_get_options_html_no_local(self):
        options = {
            "option1": EnumResourceParameter(
                name="option1",
                description="Option 1",
                values={"value1": "Value 1"},
            ),
            "option2": EnumResourceParameter(
                name="option2",
                description="Option 2",
                values={"value2": "Value 2"},
            )
        }
        html = "<form>{}</form>".format(get_options_html(options, None))
        form = etree.fromstring(html)
        option1_elems = form.xpath("fieldset/div/input[@name='option1']")
        self.assertEqual(1, len(option1_elems))
        option2_elems = option1_elems[0].xpath("../../following-sibling::fieldset/div/input[@name='option2']")
        self.assertEqual(1, len(option2_elems))

        # Check local generation heading is not included
        self.assertNotIn("Local Generation Only", html)

    def test_get_options_html_with_local_no_debug(self):
        options = {
            "option1": EnumResourceParameter(
                name="option1",
                description="Option 1",
                values={"value1": "Value 1"},
            ),
            "option2": EnumResourceParameter(
                name="option2",
                description="Option 2",
                values={"value2": "Value 2"},
            )
        }
        local_options = {
            "local1": EnumResourceParameter(
                name="local1",
                description="Option 1",
                values={"value1": "Value 1"},
            ),
            "local2": EnumResourceParameter(
                name="local2",
                description="Option 2",
                values={"value2": "Value 2"},
            )
        }
        html = "<form>{}</form>".format(get_options_html(options, local_options))
        form = etree.fromstring(html)
        option1_elems = form.xpath("fieldset/div/input[@name='option1']")
        self.assertEqual(1, len(option1_elems))
        # Option 2 after Option 1
        option2_elems = option1_elems[0].xpath("../../following-sibling::fieldset/div/input[@name='option2']")
        self.assertEqual(1, len(option2_elems))

        # Debug is not True, so local settings should not be included
        self.assertNotIn("local1", html)
        self.assertNotIn("local2", html)
        self.assertNotIn("Local Generation Only", html)

    @override_settings(DEBUG=True)
    def test_get_options_html_with_local_and_debug(self):
        options = {
            "option1": EnumResourceParameter(
                name="option1",
                description="Option 1",
                values={"value1": "Value 1"},
            ),
            "option2": EnumResourceParameter(
                name="option2",
                description="Option 2",
                values={"value2": "Value 2"},
            )
        }
        local_options = {
            "local1": EnumResourceParameter(
                name="local1",
                description="Option 1",
                values={"value1": "Value 1"},
            ),
            "local2": EnumResourceParameter(
                name="local2",
                description="Option 2",
                values={"value2": "Value 2"},
            )
        }
        html = "<form>{}</form>".format(get_options_html(options, local_options))
        form = etree.fromstring(html)
        option1_elems = form.xpath("fieldset/div/input[@name='option1']")
        self.assertEqual(1, len(option1_elems))
        option2_elems = option1_elems[0].xpath("../../following-sibling::fieldset/div/input[@name='option2']")
        self.assertEqual(1, len(option2_elems))

        # Debug is True, so local settings should be included
        self.assertIn("local1", html)
        self.assertIn("local2", html)
        self.assertIn("Local Generation Only", html)

        # Local options heading should follow other options
        local_options_headings = option2_elems[0].xpath("../../following-sibling::h3[text()='Local Generation Only']")
        self.assertEqual(1, len(local_options_headings))

        # Local options should follow heading
        local1_elems = local_options_headings[0].xpath("following-sibling::fieldset/div/input[@name='local1']")
        self.assertEqual(1, len(local1_elems))
        local2_elems = local1_elems[0].xpath("../../following-sibling::fieldset/div/input[@name='local2']")
        self.assertEqual(1, len(local2_elems))

    def test_get_options_html_no_options(self):
        result = get_options_html({}, {})
        self.assertEqual("", result)
