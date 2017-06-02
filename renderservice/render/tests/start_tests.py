"""Starts tests for the Render Service, daemon and webservice."""
import unittest

from render.tests.test_binary_cards_small import BinaryCardsSmallResourceTest
from render.tests.test_binary_cards import BinaryCardsResourceTest
from render.tests.test_binary_to_alphabet import BinaryToAlphabetResourceTest
from render.tests.test_binary_windows import BinaryWindowsResourceTest
from render.tests.test_modulo_clock import ModuloClockResourceTest

# def generate_suite():
#     """Build tests for generation of pdfs."""
#     return unittest.TestSuite((
#         unittest.makeSuite(BinaryCardsSmallResourceTest),
#         unittest.makeSuite(BinaryCardsResourceTest),
#         unittest.makeSuite(BinaryToAlphabetResourceTest),
#         unittest.makeSuite(BinaryToAlphabetResourceTest),
#     ))


if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    #
    # print("Running Generation Tests")
    # generate_result = runner.run(generate_suite())
    # print()
    #
    # if not generate_result.wasSuccessful():
    #     sys.exit(1)
    unittest.main()
