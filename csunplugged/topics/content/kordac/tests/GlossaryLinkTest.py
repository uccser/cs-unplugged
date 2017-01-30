import markdown
from unittest.mock import Mock

from Kordac import Kordac
from processors.GlossaryLinkBlockProcessor import GlossaryLinkBlockProcessor
from tests.BaseTestCase import BaseTestCase


class GlossaryLinkTest(BaseTestCase):

    def __init__(self, *args, **kwargs):
        """Set tag name in class for file names"""
        BaseTestCase.__init__(self, *args, **kwargs)
        self.tag_name = 'glossary'
        self.ext = Mock()
        self.ext.html_templates = {self.tag_name: BaseTestCase.loadHTMLTemplate(self, self.tag_name)}
        self.ext.tag_patterns = BaseTestCase.loadTagPatterns(self)

    def test_match_false(self):
        test_string = self.read_test_file('fail_string')
        self.assertFalse(GlossaryLinkBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))
        # TODO test longer strings

    def test_match_single_word_term_true(self):
        test_string = self.read_test_file('single_word_term')
        self.assertTrue(GlossaryLinkBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))

    def test_match_multiple_word_term_true(self):
        test_string = self.read_test_file('multiple_word_term')
        self.assertTrue(GlossaryLinkBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))
        # TODO test more files with multiple terms

    def test_match_inline_true(self):
        test_string = self.read_test_file('inline_leading_characters')
        self.assertTrue(GlossaryLinkBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))
        test_string = self.read_test_file('inline_trailing_characters')
        self.assertTrue(GlossaryLinkBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))
        test_string = self.read_test_file('inline_leading_and_trailing_characters')
        self.assertTrue(GlossaryLinkBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))

    def test_matches_more_than_one_glossary_link_true(self):
        test_string = self.read_test_file('multiple_terms')
        self.assertTrue(GlossaryLinkBlockProcessor(self.ext, self.md.parser).test(None, test_string), msg='"{}"'.format(test_string))

    # should parsing tests be in their own class?
    def test_correctly_parsed_inline(self):
        test_string = self.read_test_file('inline_leading_characters')
        converted_test_string = markdown.markdown(test_string, extensions=[Kordac()]) + '\n'
        expected_file_string = self.read_test_file('inline_leading_characters_expected')
        self.assertEqual(converted_test_string, expected_file_string)

        test_string = self.read_test_file('inline_trailing_characters')
        converted_test_string = markdown.markdown(test_string, extensions=[Kordac()]) + '\n'
        expected_file_string = self.read_test_file('inline_trailing_characters_expected')
        self.assertEqual(converted_test_string, expected_file_string)

        test_string = self.read_test_file('inline_leading_and_trailing_characters')
        converted_test_string = markdown.markdown(test_string, extensions=[Kordac()]) + '\n'
        expected_file_string = self.read_test_file('inline_leading_and_trailing_characters_expected')
        self.assertEqual(converted_test_string, expected_file_string)

    def test_glossary_link_in_panel(self):
        pass
