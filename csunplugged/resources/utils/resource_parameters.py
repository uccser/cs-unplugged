"""Module for resource parameter classes."""

from lxml import etree
from django.utils.translation import ugettext as _
from utils.errors.QueryParameterMissingError import QueryParameterMissingError
from utils.errors.QueryParameterInvalidError import QueryParameterInvalidError
from utils.errors.QueryParameterMultipleValuesError import QueryParameterMultipleValuesError


BOOTSTRAP_CLASSES = {
    "radio-container": "form-check",
    "radio-input": "form-check-input",
    "radio-label": "form-label",
}


class ResourceParameter(object):
    """Base resource parameter class."""

    def __init__(self, name="", description=""):
        """Initialise ResourceParameter.

        Args:
            name: (str) parameter name i.e. barcode_length
            description: (str) description of parameter for end user
        """
        self.name = name
        self.description = description

    def html_element(self):
        """Return an html fieldset element representing the parameter.

        Returns:
            etree.Element
        """
        legend = etree.Element('legend')
        legend.text = self.description
        fieldset = etree.Element('fieldset')
        fieldset.append(legend)
        return fieldset

    def process_requested_values(self, requested_values):
        """Validate and load value(s) from QueryDict.

        Must be implemented on any subclass.

        Args:
            requested_values: QueryDict of requested values
        """
        raise NotImplementedError("process_requested_values must be implemented on all ResourceParameter subclasses")

    def process_value(self, value):
        """Validate and process a single requested value."""
        return value


class SingleValuedParameter(ResourceParameter):
    """Resource parameter class where requesting multiple values is invalid."""

    def __init__(self, default=None, required=True, **kwargs):
        """Initialise SingleValuedParameter.

        Args:
            default: default value
            required: if true, end user must provide a value
        """
        super().__init__(**kwargs)
        self.value = None
        self.single_valued = True
        self.default = default
        self.required = required

    def process_requested_values(self, requested_values):
        """Validate and load value from QueryDict.

        Args:
            requested_values: QueryDict of requested values

        Raises:
            QueryParameterMultipleValuesError: more than one value was given
            QueryParameterMissingError: no value found, and parameter is required
        """
        if len(requested_values) > 1:
            raise QueryParameterMultipleValuesError(self.name, requested_values)
        if len(requested_values) == 0:
            if self.required:
                raise QueryParameterMissingError(self.name)
            else:
                self.value = self.default
        else:
            self.value = self.process_value(requested_values[0])

    def html_default(self, request_parameters):
        """Return the default parameter HTML value.

        If the HTTP request for the resource form has a requested parameter
        default, return the requested value. Otherwise return the parameter
        default.

        Args:
            request_parameters (QueryDict): Request QueryDict for resource form.

        Return:
            String of default value.
        """
        default = self.default
        if request_parameters:
            requested_default = request_parameters.get(self.name)
            if requested_default and requested_default in self.valid_values.keys():
                default = requested_default
        return default


class MultiValuedParameter(ResourceParameter):
    """Resource parameter class where requesting multiple values is valid."""

    def __init__(self, **kwargs):
        """Initialise MultiValuedParameter."""
        self.values = []
        self.single_valued = False

    def process_requested_values(self, requested_values):
        """Validate and load values from QueryDict.

        Args:
            requested_values: QueryDict of requested values
        """
        for value in requested_values:
            self.values.append(self.process_value(value))


class EnumResourceParameter(SingleValuedParameter):
    """Resource parameter class where value must be one of given set of valid values."""

    def __init__(self, values=dict(), default=None, **kwargs):
        """Initialise EnumResourceParameter.

        Args:
            values: (dict) valid values for the parameter. Should be of form
                {<value>: <description of value for end user>, ...}
            required: if true, end user must provide a value
        """
        super().__init__(**kwargs)
        self.valid_values = values
        self.indices = {value: i for i, value in enumerate(values.keys())}
        self.default = default
        if self.default not in self.valid_values:
            self.default = list(self.valid_values.keys())[0]  # Select first value
        self.value = None

    def html_element(self, request_parameters=None):
        """Return HTML element for the EnumResourceParameter.

        Args:
            request_parameters (QueryDict): QueryDict of request_parameters.

        Returns:
            Element tree of HTML.
        """
        default_value = super().html_default(request_parameters)
        base_elem = super().html_element()
        for value, value_desc in self.valid_values.items():
            container = etree.Element("div")
            container.set("class", BOOTSTRAP_CLASSES["radio-container"])
            input_elem = etree.Element(
                "input",
                type="radio",
                name=self.name,
                id='{}_{}'.format(self.name, value),
                value=str(value),
            )
            input_elem.set("class", BOOTSTRAP_CLASSES["radio-input"])
            if value == default_value:
                input_elem.set("checked", "checked")
            container.append(input_elem)
            label_elem = etree.Element(
                "label",
            )
            label_elem.set("for", "{}_{}".format(self.name, value))
            label_elem.set("class", BOOTSTRAP_CLASSES["radio-label"])
            label_elem.text = value_desc
            container.append(label_elem)
            base_elem.append(container)
        return base_elem

    def index(self, value):
        """Return unique index of a value in the list of valid values."""
        return self.indices[value]

    def process_value(self, value):
        """Validate and process requested value.

        Args:
            value: (str) requested value.
        Returns:
            value, unchanged (if valid)
        Raises:
            QueryParameterInvalidError: value is not in the valid_values set
        """
        if value not in self.valid_values:
            raise QueryParameterInvalidError(self.name, value)
        return value


class BoolResourceParameter(EnumResourceParameter):
    """Resource parameter class for boolean values."""

    TRUE_VALUE = "yes"
    FALSE_VALUE = "no"

    def __init__(self, default=False, true_text=_("Yes"), false_text=_("No"), **kwargs):
        """Initialise BoolResourceParameter.

        Args:
            default: (bool) True/False default value
            true_text: (str) Description of true value to end user (eg. "Yes")
            false_text: (str) Description of false value to end user (eg. "No")
        """
        values = {
            self.TRUE_VALUE: true_text,
            self.FALSE_VALUE: false_text
        }
        default = self.TRUE_VALUE if default is True else self.FALSE_VALUE
        super().__init__(values=values, default=default, **kwargs)

    def process_value(self, value):
        """Validate and process requested bool value.

        Args:
            value: (str) requested value.
        Returns:
            bool version of value
        Raises:
            QueryParameterInvalidError: value is not TRUE_VALUE or FALSE_VALUE
        """
        if value == self.TRUE_VALUE:
            return True
        elif value == self.FALSE_VALUE:
            return False
        else:
            raise QueryParameterInvalidError(self.name, value)


class TextResourceParameter(SingleValuedParameter):
    """Resource parameter class for freeform text values."""

    def __init__(self, placeholder="", **kwargs):
        """Initialise TextResourceParameter.

        Args:
            placeholder: (str) Placeholder text for input field
        """
        super().__init__(**kwargs)
        self.placeholder = placeholder

    def html_element(self, request_parameters=None):
        """Return HTML element for the TextResourceParameter.

        Args:
            request_parameters (QueryDict): QueryDict of request_parameters.

        Returns:
            Element tree of HTML.
        """
        base_elem = super().html_element()
        input_elem = etree.Element(
            "input",
            type="text",
            name=self.name,
            placeholder=self.placeholder,
        )
        input_elem.set("class", "long-text-field")
        base_elem.append(input_elem)
        return base_elem


class IntegerResourceParameter(SingleValuedParameter):
    """Resource parameter class for integer values."""

    def __init__(self, default=None, min_val=None, max_val=None, **kwargs):
        """Initialise IntegerResourceParameter.

        Args:
            default: (int) default value
            min_val: (int) minimum valid value
            max_val: (int) maximum valid value
        """
        super().__init__(**kwargs)
        self.min_val = min_val
        self.max_val = max_val
        self.default = default

    def html_element(self, request_parameters=None):
        """Return HTML element for the IntegerResourceParameter.

        Args:
            request_parameters (QueryDict): QueryDict of request_parameters.

        Returns:
            Element tree of HTML.
        """
        default_value = super().html_default(request_parameters)
        base_elem = super().html_element()
        input_elem = etree.Element(
            "input",
            type="number",
            name=self.name,
        )
        if self.min_val:
            input_elem.set("min", str(self.min_val))
        if self.max_val:
            input_elem.set("max", str(self.max_val))
        if default_value:
            input_elem.set("value", str(default_value))
        base_elem.append(input_elem)
        return base_elem

    def process_value(self, value):
        """Validate and process requested integer value.

        Args:
            value: (str) string version of integer value eg "37"
        Returns:
            Integer value
        Raises:
            QueryParameterInvalidError: If value is outside valid range, or
                cannot be turned into an integer
        """
        try:
            int_val = int(value)
        except (TypeError, ValueError):
            raise QueryParameterInvalidError(self.name, value)
        if (self.min_val and int_val < self.min_val) or (self.max_val and int_val > self.max_val):
            raise QueryParameterInvalidError(self.name, value)
        return int_val
