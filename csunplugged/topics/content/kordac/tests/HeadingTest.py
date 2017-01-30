import unittest
import markdown

from Kordac import Kordac
from processors.NumberedHashHeaderProcessor import NumberedHashHeaderProcessor
from tests.BaseTestCase import BaseTestCase

class HeadingTest(BaseTestCase):

    def __init__(self, *args, **kwargs):
        """Set tag name in class for file names"""
        BaseTestCase.__init__(self, *args, **kwargs)
        self.tag_name = 'heading'
        self.ext.tag_patterns = BaseTestCase.loadTagPatterns(self)

