import markdown
from unittest.mock import Mock

from Kordac import Kordac
from processors.VideoBlockProcessor import VideoBlockProcessor
from tests.BaseTestCase import BaseTestCase

# NTS videos have different links
# need to test:
#   - vimeo
#   - youtu.be
#   - /embed/
#   - /watch/
# etc

class VideoTest(BaseTestCase):

    def __init__(self, *args, **kwargs):
        """Set tag name in class for file names"""
        BaseTestCase.__init__(self, *args, **kwargs)
        self.tag_name = 'video'
        self.ext = Mock()
        self.ext.html_templates = {self.tag_name: BaseTestCase.loadHTMLTemplate(self, self.tag_name)}
        self.ext.tag_patterns = BaseTestCase.loadTagPatterns(self)

    def test_match_false(self):
        test_string = self.read_test_file('fail_string')
        self.assertFalse(VideoBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))

    def test_match_true(self):
        test_string = self.read_test_file('basic')
        self.assertTrue(VideoBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))

    def test_parses(self):
        test_string = self.read_test_file('basic')
        converted_test_string = markdown.markdown(test_string, extensions=[Kordac()]) + '\n'
        expected_file_string = self.read_test_file('basic_expected')
        self.assertEqual(converted_test_string, expected_file_string)
