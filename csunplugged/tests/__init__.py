import unittest

def suite():
	return  unittest.TestLoader().discover('topics.tests', pattern='*.py')