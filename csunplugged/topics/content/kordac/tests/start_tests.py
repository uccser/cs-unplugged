import unittest
from collections import defaultdict

from tests.GlossaryLinkTest import GlossaryLinkTest
from tests.PanelTest import PanelTest
from tests.CommentTest import CommentTest
from tests.HeadingTest import HeadingTest
from tests.ImageTest import ImageTest
from tests.VideoTest import VideoTest
from tests.InteractiveTest import InteractiveTest


def suite():
    # NTS what order should these go in?
    allSuites = unittest.TestSuite((
        unittest.makeSuite(GlossaryLinkTest), # order of tests by cmp()
        unittest.makeSuite(PanelTest),
        unittest.makeSuite(CommentTest),
        unittest.makeSuite(HeadingTest),
        unittest.makeSuite(ImageTest),
        unittest.makeSuite(VideoTest),
        unittest.makeSuite(InteractiveTest)
    ))

    return allSuites


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
