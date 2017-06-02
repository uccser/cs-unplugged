"""Starts tests for the Render Service, daemon and webservice."""
import sys
import unittest


def generate_suite():
    """Build tests for generation of pdfs."""
    return unittest.TestSuite((
        unittest.makeSuite(),
    ))


if __name__ == "__main__":
    runner = unittest.TextTestRunner()

    print("Running Generation Tests")
    generate_result = runner.run(generate_suite())
    print()

    if not generate_result.wasSuccessful():
        sys.exit(1)
