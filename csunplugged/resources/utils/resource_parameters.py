from lxml import etree
from django.utils.translation import ugettext as _

class ResourceParameter(object):
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description

    def html_element(self):
        legend = etree.Element('legend')
        legend.text = self.description
        fieldset = etree.Element('fieldset')
        fieldset.append(legend)
        return fieldset


class EnumResourceParameter(ResourceParameter):
    def __init__(self, values=[], default=None, **kwargs):
        super().__init__(**kwargs)
        self.values = values
        self.default = default
        if self.default not in self.values:
            raise Exception(self.values)

    def html_element(self):
        base_elem = super().html_element()
        for value, value_desc in self.values.items():
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

class BoolResourceParameter(EnumResourceParameter):
    def __init__(self, default=True, true_text=_("Yes"), false_text=_("No"), **kwargs):
        values = {
            True: true_text,
            False: false_text
        }
        super().__init__(values=values, default=default, **kwargs)
