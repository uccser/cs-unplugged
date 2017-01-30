from markdown.blockprocessors import BlockProcessor
import re
from processors.utils import parse_argument, centre_html
from markdown.util import etree


class ImageBlockProcessor(BlockProcessor):

    def __init__(self, ext, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.required = ext.required_files["images"]
        self.IMAGE_TEMPLATE = ext.html_templates['image']
        self.pattern = re.compile(ext.tag_patterns['image']['pattern'])

    def test(self, parent, block):
        return self.pattern.match(block) is not None

    def run(self, parent, blocks):
        match = self.pattern.match(blocks.pop(0))
        arguments = match.group('args')
        filename = parse_argument('filename', arguments)

        if filename:
            html_string = self.IMAGE_TEMPLATE.format(filename=filename)
            node = etree.fromstring(html_string)
            parent.append(centre_html(etree.fromstring(html_string), 8))

            self.required.add(filename)
