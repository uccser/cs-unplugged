"""Module for getting HTML form elements for list of ResourceParameters."""

from django.conf import settings
from lxml import etree


def get_options_html(options, local_options, request_parameters=None):
    """Return HTML string of form elements for given options.

    Args:
        options (list): List of ResourceParameters options.
        local_options (list): List of ResourceParameters local options.
        request_parameters (QueryDict): Request QueryDict for resource form.

    Returns:
        HTML string
    """
    html_string = ""
    for parameter in options.values():
        html_string += element_to_string(parameter.html_element(request_parameters))
    html_string = '<div id="resource-options">{}</div>'.format(html_string)

    if settings.DEBUG:
        html_string_local_options = element_to_string(etree.Element("hr"))
        h3 = etree.Element("h3")
        h3.text = "Local Generation Only"
        html_string_local_options += element_to_string(h3)
        for parameter in local_options.values():
            html_string_local_options += element_to_string(parameter.html_element(request_parameters))

        html_string += '<div id="local-generation-resource-options">{}</div>'.format(html_string_local_options)
    return html_string

def element_to_string(element):
    return etree.tostring(element, pretty_print=True, encoding='utf-8').decode('utf-8')
