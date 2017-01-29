from markdown.blockprocessors import BlockProcessor
import re

class CommentBlockProcessor(BlockProcessor):
    # comments spread across multiple lines

    def __init__(self, ext, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.p_start = re.compile(ext.tag_patterns['comment_block']['pattern_start'])
        self.p_end = re.compile(ext.tag_patterns['comment_block']['pattern_end'])

    def test(self, parent, block):
        return self.p_start.match(block) is not None

    def run(self, parent, blocks):
        block = blocks.pop(0)
        # removes comment blocks from text
        while self.p_end.search(block) is None and len(blocks) > 0:
            block = blocks.pop(0)
