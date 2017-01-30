from markdown.preprocessors import Preprocessor
import re


class CommentPreprocessor(Preprocessor):
    # comments contained in one line

    def __init__(self, ext, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pattern = re.compile(ext.tag_patterns['comment_pre']['pattern'])

    def test(self, lines):
        return self.pattern.match(lines) is not None

    def run(self, lines):
        # if the comment is contained in the one block, removes the comment from the string
        for i, line in enumerate(lines):
            lines[i] = re.sub(self.pattern, '', line)
        return lines

