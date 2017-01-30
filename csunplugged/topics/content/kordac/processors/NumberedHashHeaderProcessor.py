from markdown.blockprocessors import BlockProcessor
from markdown.util import etree
import re

class NumberedHashHeaderProcessor(BlockProcessor):
    """ Process Hash Headers. """

    def __init__(self, ext, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_generator = NumberGenerator()
        self.ext = ext
        self.pattern = re.compile(ext.tag_patterns['heading']['pattern'])

    def test(self, parent, block):
        return self.pattern.search(block) is not None

    def run(self, parent, blocks):
        block = blocks.pop(0)
        match = self.pattern.search(block)
        if match:
            before = block[:match.start()]  # All lines before header
            after = block[match.end():]     # All lines after header
            if before:
                # As the header was not the first line of the block and the
                # lines before the header must be parsed first,
                # recursively parse this lines as a block.
                self.parser.parseBlocks(parent, [before])
            # Create header using named groups from RE
            level = len(match.group('level'))
            heading = match.group('header').strip()
            if not self.ext.page_heading:
                self.ext.page_heading = heading
                parent = etree.SubElement(parent, 'div', attrib={'class': 'z-depth-0 page-title-header'})
                parent = etree.SubElement(parent, 'div', attrib={'class': 'container'})

            number = self.number_generator.next(level)
            h = etree.SubElement(parent, 'h{}'.format(level), attrib={'class':'section-heading anchor-link'})
            span = etree.SubElement(h, 'span', attrib={'class':'section_number'})
            span.text = '{{{{ chapter.number }}}}.{}'.format(number)
            span.tail = ' ' + heading

            if after:
                # Insert remaining lines as first block for future parsing.
                blocks.insert(0, after)

class NumberGenerator:
    """Used to allocate numbers throughout guide"""
    def __init__(self):
        self.number_list = [None, 0]
        self.cur_level = 1

    def __str__(self):
        """Return formatted number eg. "1.5.6.2"
        """
        out = ''
        for num in self.number_list[2:]:
            out += str(num) + '.'
        return out

    def next(self, level):
        """Returns next number for a given level.
        Numbers must be generated in order.
        -   For higher levels, 1 values are appended until
            desired level reached
        -   For lower levels, values popped from list until
            desired level reached, then incrememnted by 1
        """
        if level > self.cur_level:
            while level > self.cur_level:
                self.number_list.append(1)
                self.cur_level += 1
        else:
            while self.cur_level > level:
                self.number_list.pop()
                self.cur_level -= 1
            self.number_list[-1] += 1
        return str(self)
