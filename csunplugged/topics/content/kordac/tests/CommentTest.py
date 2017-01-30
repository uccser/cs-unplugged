import markdown
from unittest.mock import Mock

from Kordac import Kordac
from processors.CommentPreprocessor import CommentPreprocessor
from processors.CommentBlockProcessor import CommentBlockProcessor
from tests.BaseTestCase import BaseTestCase

class CommentTest(BaseTestCase):

    def __init__(self, *args, **kwargs):
        """Set tag name in class for file names"""
        BaseTestCase.__init__(self, *args, **kwargs)
        self.tag_name = 'comment'
        self.ext = Mock()
        self.ext.tag_patterns = BaseTestCase.loadTagPatterns(self)

    def test_match_false(self):
        test_string = self.read_test_file('fail_string')
        self.assertFalse(CommentBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))

    def test_match_single_word_term_true(self):
        test_string = self.read_test_file('basic')
        self.assertTrue(CommentBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))

    def test_parses_basic(self):
        test_string = self.read_test_file('basic')
        converted_test_string = markdown.markdown(test_string, extensions=[Kordac()])
        expected_file_string = self.read_test_file('basic_expected')
        self.assertEqual(converted_test_string, expected_file_string)

    # NTS should preprocessor tests be separate?
    def test_preprocessor_match(self):
        test_string = self.read_test_file('singleline')
        self.assertTrue(CommentPreprocessor(self.ext, self.md.parser).test(test_string), msg='"{}"'.format(test_string))

    def test_preprocessor_parsing(self):
        test_string = self.read_test_file('singleline')
        converted_test_string = markdown.markdown(test_string, extensions=[Kordac()])
        expected_file_string = self.read_test_file('singleline_expected')
        self.assertEqual(converted_test_string, expected_file_string)
