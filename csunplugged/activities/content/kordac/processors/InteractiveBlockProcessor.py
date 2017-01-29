from markdown.blockprocessors import BlockProcessor
from markdown.postprocessors import Postprocessor
from markdown.treeprocessors import Treeprocessor
from processors.utils import parse_argument
from markdown.util import etree

import bs4
import re
import os

class InteractiveBlockProcessor(BlockProcessor):

    def __init__(self, ext, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scripts = ext.page_scripts
        self.required = ext.required_files["interactives"]
        self.pattern = re.compile(ext.tag_patterns['interactive']['pattern'])

    def test(self, parent, block):
        return self.pattern.match(block) is not None

    def run(self, parent, blocks):
        block = blocks.pop(0)
        match = self.pattern.match(block)

        arguments = match.group('args')
        name = parse_argument('name', arguments)
        interactive_type = parse_argument('type', arguments)

        if name:
            if interactive_type == 'in-page':
                self.generate_inpage_interactive(name, parent)
            elif interactive_type == 'iframe':
                self.generate_iframe_interactive(name, parent)
            elif interactive_type == 'whole-page':
                self.generate_wholepage_interactive(name, parent)
            self.required.add(name)

    def generate_inpage_interactive(self, iname, parent):
        sibling = self.lastChild(parent)
        dj_tag ='\n{{% include \'interactive/{}/index.html\' %}}\n'.format(iname)
        if sibling is not None:
            sibling.tail = sibling.tail or '' +  dj_tag
        else:
            parent.text = parent.text or '' + dj_tag
        self.scripts.append('\n{{% include \'interactive/{}/scripts.html\' %}}\n'.format(iname))

    def generate_iframe_interactive(self, iname, parent):
        div = etree.SubElement(parent, 'div', attrib={'class':'interactive-iframe'})
        iframe = etree.SubElement(div, 'iframe', attrib={
            'src': '{{% url \'interactive\' iname=\'{}\' %}}'.format(iname),
            'class': 'interactive-iframe-resize',
            'frameborder': '0',
            'scrolling': 'no',
        })

    def generate_wholepage_interactive(self, iname, parent, thumbnail=None, arg_text=None):
        thumbnail = thumbnail or 'thumbnail.png'
        text = 'Click to load {text}'.format(text=arg_text or iname)
        atag = etree.SubElement(parent, 'a', attrib={
            'href': '{{% url \'interactive\' iname=\'{}\' %}}'.format(iname),
            'class': 'btn btn-expand btn-interactive-whole-page-container',
        })
        img = etree.SubElement(atag, 'img', attrib={
            'class': 'btn-interactive-whole-page-image',
            'src': '{{% static \'interactive/{}/{}\' %}}'.format(iname, thumbnail)
        })
        div = etree.SubElement(atag, 'div', attrib={
            'class': 'btn-interactive-whole-page-text',
        })
        div.text = text
