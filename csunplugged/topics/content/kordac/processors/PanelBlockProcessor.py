from markdown.blockprocessors import BlockProcessor
from markdown.util import etree
import processors.utils as utils
import re


class PanelBlockProcessor(BlockProcessor):
    # p_start = re.compile('^\{panel ?(?P<args>[^\}]*)\}')
    # p_end = re.compile('\{panel end\}')

    def __init__(self, ext, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.PANEL_TEMPLATE = ext.html_templates['panel']
        self.p_start = re.compile(ext.tag_patterns['panel']['pattern_start'])
        self.p_end = re.compile(ext.tag_patterns['panel']['pattern_end'])

    def test(self, parent, block):
        # return re.search('\{panel ?(?P<args>[^\}]*)\}', block) is not None
        return self.p_start.search(block) is not None

    def run(self, parent, blocks):
        # block contains the match as a substring
        block = blocks.pop(0)

        # find start of match and place back in blocks list up to end of match
        m_start = self.p_start.match(block)
        blocks.insert(0, block[m_start.end():])

        # iterate over blocks until find {panel end} block
        panel_content = ''
        while len(blocks) > 0:
            block = blocks.pop(0)
            m_end = self.p_end.search(block)
            if m_end is not None:
                text = block[:m_end.start()]
                if len(text)  > 0:
                    panel_content += '<p>' + text + '</p>'
                break
            else:
                # have not found end of panel, so add entire block
                if len(block) > 0:
                    panel_content += '<p>' + block + '</p>'

        panel_attributes = self.get_attributes(m_start.group('args'))

        if panel_attributes['expanded']:
            panel_attributes['expanded'] = ' active'
        else:
            panel_attributes['expanded'] = ''

        heading = utils.from_kebab_case(panel_attributes['panel_type'])
        if panel_attributes['summary']:
            heading += ': {}'.format(panel_attributes['summary'])

        self.PANEL_TEMPLATE = self.PANEL_TEMPLATE.format(
                type_class='panel-'+panel_attributes['panel_type'],
                expanded=panel_attributes['expanded'],
                panel_heading=heading,
                content=panel_content
                )

        # create panel node and add it to parent element
        node = etree.fromstring(self.PANEL_TEMPLATE)
        parent.append(node)

    def get_attributes(self, args):
        panel_type = utils.parse_argument('type', args)
        summary = utils.parse_argument('summary', args)
        expanded = utils.parse_argument('expanded', args)
        return {
            'panel_type': panel_type,
            'expanded': expanded,
            'summary': summary
        }

