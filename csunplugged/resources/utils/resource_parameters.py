from lxml import etree
from django.utils.translation import ugettext as _
from utils.errors.QueryParameterMissingError import QueryParameterMissingError
from utils.errors.QueryParameterInvalidError import QueryParameterInvalidError
from utils.errors.QueryParameterMultipleValuesError import QueryParameterMultipleValuesError



class ResourceParameter(object):
    def __init__(self, name="", description="", required=True):
        self.name = name
        self.description = description

    def html_element(self):
        legend = etree.Element('legend')
        legend.text = self.description
        fieldset = etree.Element('fieldset')
        fieldset.append(legend)
        return fieldset

    def process_requested_values(self, requested_values):
        raise NotImplementedError("process_requested_values must be implemented on all ResourceParameter subclasses")

    def process_value(self, value):
        return value


class SingleValuedParameter(ResourceParameter):
    def __init__(self, default=None, required=True, **kwargs):
        super().__init__(**kwargs)
        self.value = None
        self.single_valued = True
        self.default = default
        self.required = required

    def process_requested_values(self, requested_values):

        if len(requested_values) > 1:
            raise QueryParameterMultipleValuesError(self.name, requested_values)
        if len(requested_values) == 0:
            if self.required:
                raise QueryParameterMissingError(self.name)
            else:
                self.value = self.default
        else:
            self.value = self.process_value(requested_values[0])


class MultiValuedParameter(ResourceParameter):
    def __init__(self, **kwargs):
        self.values = []
        self.single_valued = False

    def process_requested_values(self, requested_values):
        for value in requested_values:
            self.values.append(self.process_value(value))


class EnumResourceParameter(SingleValuedParameter):
    def __init__(self, values=dict(), default=None, **kwargs):
        super().__init__(**kwargs)
        self.valid_values = values
        self.indices = {value: i for i, value in enumerate(values.keys())}
        self.default = default
        if self.default not in self.valid_values:
            self.default = list(self.valid_values.keys())[0] # Select first value
        self.value = None

    def html_element(self):
        base_elem = super().html_element()
        for value, value_desc in self.valid_values.items():
            input_elem = etree.Element(
                'input',
                type="radio",
                name=self.name,
                id='{}_{}'.format(self.name, value),
                value=str(value)
            )
            if value == self.default:
                input_elem.set("checked", "checked")
            base_elem.append(input_elem)
            label_elem = etree.Element(
                "label",
            )
            label_elem.set("for", "{}_{}".format(self.name, value))
            label_elem.text = value_desc
            base_elem.append(label_elem)
            base_elem.append(etree.Element('br'))
        return base_elem

    def index(self, value):
        return self.indices[value]

    def process_value(self, value):
        if value not in self.valid_values:
            raise QueryParameterInvalidError(self.name, value)
        return value

class BoolResourceParameter(EnumResourceParameter):
    TRUE_VALUE="yes"
    FALSE_VALUE="no"

    def __init__(self, default=True, true_text=_("Yes"), false_text=_("No"), **kwargs):
        values = {
            self.TRUE_VALUE: true_text,
            self.FALSE_VALUE: false_text
        }
        super().__init__(values=values, default=default, **kwargs)

    def process_value(self, value):
        if value == self.TRUE_VALUE:
            return True
        elif value == self.FALSE_VALUE:
            return False
        else:
            raise QueryParameterInvalidError(self.name, value)


class TextResourceParameter(SingleValuedParameter):
    def __init__(self, placeholder="", **kwargs):
        super().__init__(**kwargs)
        self.placeholder = placeholder

    def html_element(self):
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
    def __init__(self, default=None, min_val=None, max_val=None, **kwargs):
        super().__init__(**kwargs)
        self.min_val = min_val
        self.max_val = max_val
        self.default = default

    def html_element(self):
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
        if self.default:
            input_elem.set("value", str(self.default))
        base_elem.append(input_elem)
        return base_elem

    def process_value(self, value):
        try:
            int_val = int(value)
        except:
            raise QueryParameterInvalidError(self.name, value)
        if (self.min_val and int_val < self.min_val) or (self.max_val and int_val > self.max_val):
            raise QueryParameterInvalidError(self.name, value)
        return int_val
