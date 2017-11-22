"""Module for getting HTML form elements for list of ResourceParameters."""

from django.conf import settings
from lxml import etree
from django.utils.translation import ugettext as _


def get_options_html(options, local_options):
    """Return HTML string of form elements for given options.

    Args:
        options: (list of ResourceParameters) options list
        local_options: (list of ResourceParameters) local options list

    Returns:
        HTML string
    """
    html_elements = []
    for parameter in options.values():
        html_elements.append(parameter.html_element())
    if settings.DEBUG:
        html_elements.append(etree.Element("hr"))
        h3 = etree.Element("h3")
        h3.text = _("Local Generation Only")
        html_elements.append(h3)
        for parameter in local_options.values():
            html_elements.append(parameter.html_element())

    html_string = ""
    for html_elem in html_elements:
        html_string += etree.tostring(html_elem, pretty_print=True, encoding='utf-8').decode('utf-8')
    return html_string
