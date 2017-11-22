from tests.BaseTest import BaseTest
from lxml import etree
from utils.errors.QueryParameterMissingError import QueryParameterMissingError
from utils.errors.QueryParameterInvalidError import QueryParameterInvalidError
from utils.errors.QueryParameterMultipleValuesError import QueryParameterMultipleValuesError

from resources.utils.resource_parameters import (
    ResourceParameter,
    SingleValuedParameter,
    MultiValuedParameter,
    EnumResourceParameter,
    BoolResourceParameter,
    TextResourceParameter,
    IntegerResourceParameter
)

class ResourceParametersTest(BaseTest):

    def test_resource_parameter_base_process_requested_values(self):
        param = ResourceParameter()
        with self.assertRaises(NotImplementedError):
            param.process_requested_values(None)

    def test_resource_parameter_base_process_value(self):
        param = ResourceParameter()
        processed = param.process_value("value")
        # Parameter should be unchanged
        self.assertEqual("value", processed)

    def test_resource_parameter_base_html_element(self):
        param = ResourceParameter("param1", "param1 description")
        html = param.html_element()
        self.assertIsInstance(html, etree._Element)
        self.assertEqual("fieldset", html.tag)
        self.assertEqual(1, len(html)) # Should only have 1 child, the
        self.assertEqual("legend", html[0].tag)
        self.assertEqual("param1 description", html[0].text)

    def test_single_valued_parameter_process_requested_values_required_present(self):
        param = SingleValuedParameter()
        param.process_requested_values([1])
        self.assertEqual(1, param.value)

    def test_single_valued_parameter_process_requested_values_required_missing(self):
        param = SingleValuedParameter()
        with self.assertRaises(QueryParameterMissingError):
            param.process_requested_values([])

    def test_single_valued_parameter_process_requested_values_not_required_missing(self):
        param = SingleValuedParameter(default="default value", required=False)
        param.process_requested_values([])
        self.assertEqual("default value", param.value)


    def test_single_valued_parameter_process_requested_values_multiple_values(self):
        param = SingleValuedParameter()
        with self.assertRaises(QueryParameterMultipleValuesError):
            param.process_requested_values(["value1", "value2"])

    def test_multi_valued_parameter_process_requested_values_single_value(self):
        param = MultiValuedParameter()
        param.process_requested_values(["value1"])
        self.assertEqual(["value1"], param.values)

    def test_multi_valued_parameter_process_requested_values_multiple_values(self):
        param = MultiValuedParameter()
        param.process_requested_values(["value1", "value2"])
        self.assertEqual(["value1", "value2"], param.values)

    def test_enum_resource_parameter_html_element(self):
        values = {"value1": "Value 1", "value2": "Value 2"}
        param = EnumResourceParameter(
            name="option1",
            values=values,
            default="value2",
            description="option1 description"
        )
        html = param.html_element()
        self.assertIsInstance(html, etree._Element)
        self.assertEqual("fieldset", html.tag)
        self.assertEqual(7, len(html)) # legend, (input, label, br) X 2

        self.assertEqual("legend", html[0].tag)
        self.assertEqual("option1 description", html[0].text)

        self.assertEqual("input", html[1].tag)
        self.assertEqual("option1", html[1].get("name"))
        self.assertEqual("value1", html[1].get("value"))
        self.assertEqual("radio", html[1].get("type"))
        self.assertEqual(None, html[1].get("checked"))  # Not the default

        self.assertEqual("label", html[2].tag)
        self.assertEqual("Value 1", html[2].text)

        self.assertEqual("br", html[3].tag)

        self.assertEqual("input", html[4].tag)
        self.assertEqual("option1", html[1].get("name"))
        self.assertEqual("value2", html[4].get("value"))
        self.assertEqual("radio", html[4].get("type"))
        self.assertEqual("checked", html[4].get("checked"))  # default

        self.assertEqual("label", html[5].tag)
        self.assertEqual("Value 2", html[5].text)

        self.assertEqual("br", html[6].tag)

    def test_enum_resource_parameter_process_value_valid_value(self):
        param = EnumResourceParameter(values={"value1": "Value 1"})
        processed = param.process_value("value1")
        self.assertEqual("value1", processed) # Returned unchanged

    def test_enum_resource_parameter_process_value_invalid_value(self):
        param = EnumResourceParameter(values={"value1": "Value 1"})
        with self.assertRaises(QueryParameterInvalidError):
            param.process_value("invalid")

    def test_enum_resource_parameter_index(self):
        param = EnumResourceParameter(values={"1":"One", "2":"Two", "3":"Three"})
        self.assertEqual(1, param.index("2")) # Index of value 2 in the dict

    def test_bool_resource_parameter_default_text(self):
        param = BoolResourceParameter()
        self.assertEqual({"yes": "Yes", "no": "No"}, param.valid_values)

    def test_bool_resource_parameter_custom_text(self):
        param = BoolResourceParameter(true_text="Custom1", false_text="Custom2")
        self.assertEqual({"yes": "Custom1", "no": "Custom2"}, param.valid_values)

    def test_bool_resource_parameter_process_value_valid(self):
        param = BoolResourceParameter()
        self.assertEqual(True, param.process_value("yes"))
        self.assertEqual(False, param.process_value("no"))

    def test_bool_resource_parameter_process_value_invalid(self):
        param = BoolResourceParameter()
        with self.assertRaises(QueryParameterInvalidError):
            param.process_value("invalid")

    def test_text_resource_parameter_html_element(self):
        param = TextResourceParameter(name="option1")
        html = param.html_element()
        self.assertIsInstance(html, etree._Element)

        self.assertEqual("fieldset", html.tag)
        self.assertEqual(2, len(html)) # legend and input
        self.assertEqual("legend", html[0].tag)

        self.assertEqual("input", html[1].tag)
        self.assertEqual("option1", html[1].get("name"))
        self.assertEqual("", html[1].get("placeholder"))
        self.assertEqual("text", html[1].get("type"))

    def test_text_resource_parameter_html_element_with_placeholder(self):
        param = TextResourceParameter(name="option1", placeholder="placeholder text")
        html = param.html_element()
        self.assertIsInstance(html, etree._Element)

        self.assertEqual("fieldset", html.tag)
        self.assertEqual(2, len(html)) # legend and input
        self.assertEqual("legend", html[0].tag)

        self.assertEqual("input", html[1].tag)
        self.assertEqual("option1", html[1].get("name"))
        self.assertEqual("placeholder text", html[1].get("placeholder"))
        self.assertEqual("text", html[1].get("type"))

    def test_integer_resource_parameter_html_element(self):
        param = IntegerResourceParameter(name="option1")
        html = param.html_element()
        self.assertIsInstance(html, etree._Element)

        self.assertEqual("fieldset", html.tag)
        self.assertEqual(2, len(html)) # legend and input
        self.assertEqual("legend", html[0].tag)

        self.assertEqual("input", html[1].tag)
        self.assertEqual("option1", html[1].get("name"))
        self.assertEqual("number", html[1].get("type"))
        self.assertEqual(None, html[1].get("min"))
        self.assertEqual(None, html[1].get("max"))
        self.assertEqual(None, html[1].get("value"))

    def test_integer_resource_parameter_html_element_with_min_max_default(self):
        param = IntegerResourceParameter(
            name="option1",
            default=20,
            min_val=10,
            max_val=30
        )
        html = param.html_element()
        self.assertIsInstance(html, etree._Element)

        self.assertEqual("fieldset", html.tag)
        self.assertEqual(2, len(html)) # legend and input
        self.assertEqual("legend", html[0].tag)

        self.assertEqual("input", html[1].tag)
        self.assertEqual("option1", html[1].get("name"))
        self.assertEqual("number", html[1].get("type"))
        self.assertEqual("10", html[1].get("min"))
        self.assertEqual("30", html[1].get("max"))
        self.assertEqual("20", html[1].get("value"))

    def test_integer_resource_parameter_process_value_no_range(self):
        param = IntegerResourceParameter(name="option1")
        self.assertEqual(10, param.process_value("10"))
        self.assertEqual(0, param.process_value("0"))
        self.assertEqual(-10, param.process_value("-10"))

    def test_integer_resource_parameter_process_value_in_range(self):
        param = IntegerResourceParameter(name="option1", min_val=-20, max_val=20)
        self.assertEqual(10, param.process_value("10"))
        self.assertEqual(0, param.process_value("0"))
        self.assertEqual(-10, param.process_value("-10"))

    def test_integer_resource_parameter_process_value_out_of_range(self):
        param = IntegerResourceParameter(name="option1", min_val=-20, max_val=20)
        with self.assertRaises(QueryParameterInvalidError):
            param.process_value("-30")
        with self.assertRaises(QueryParameterInvalidError):
            param.process_value("30")

    def test_integer_resource_parameter_process_value_invalid_value_type(self):
        param = IntegerResourceParameter(name="option1")
        with self.assertRaises(QueryParameterInvalidError):
            param.process_value("notaninteger")
