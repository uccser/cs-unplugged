import re
from markdown.util import etree

CENTERED_HTML = """
<div class='row'>
  <div content='' class='content col s12 m{width} offset-m{offset_width} center-align'>
  </div>
</div>
"""

def parse_argument(argument_key, arguments):
    """Search for the given argument in a string of all arguments
    Returns: Value of an argument as a string if found, otherwise None"""
    result = re.search('{}="([^"]*)"'.format(argument_key), arguments)
    if result:
        argument_value = result.group(1)
    else:
        argument_value = None
    return argument_value

def from_kebab_case(text):
    """Returns given kebab case text to plain text.
    Text is camel case, with dashs replaced with spaces
    """
    return text.replace('-', ' ').title()

def to_kebab_case(text):
    """Returns the given text as kebab case.
    The text is lower case, has spaces replaced as dashes.
    All punctuation is also removed.
    """
    text = ''.join(letter for letter in text if letter in set(string.ascii_letters + string.digits + ' -'))
    text = text.replace(' ', '-').lower()
    return text


def centre_html(node, width):
    """Wraps the given node with HTML to centre using the given number of columns"""
    offset_width = (12 - width) // 2
    root = etree.fromstring(CENTERED_HTML.format(width=width, offset_width=offset_width))
    root.find(".//div[@content]").append(node)
    return root
