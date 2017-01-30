import unittest
import json
import markdown
from Kordac import Kordac
from markdown.extensions import Extension

class BaseTestCase(unittest.TestCase):
    """A base test class for individual test classes"""

    def __init__(self, *args, **kwargs):
        """Creates BaseTest Case class

        Create class inheiriting from TestCase, while also storing
        the path to test files and the maxiumum difference to display on
        test failures.
        """
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.test_file_path = 'tests/assets/{tag_name}/{filename}.txt'
        # self.maxDiff = 640  # Set to None for full output of all test failures
        self.maxDiff = None

    def read_test_file(self, filename):
        """Returns a string for a given file

        This function reads a file from a given filename in UTF-8 encoding.
        """
        file_path = self.test_file_path.format(tag_name=self.tag_name, filename=filename)
        file_object = open(file_path, encoding="utf-8")
        return file_object.read()

    def loadHTMLTemplate(self, template):
        return open('html-templates/' + template + '.html').read()

    def loadTagPatterns(self):
        pattern_data = open('regex-list.json').read()
        return json.loads(pattern_data)

    def setUp(self):
        self.md = markdown.Markdown(extensions=[Kordac()])

    def tearDown(self):
        self.md = None
