#!/usr/bin/env python

"""
test_stringmetric
-----------------

Tests for the `stringmetric` module.
"""


import unittest

from stringmetric.distance import hamming


class TestStringmetric(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_hamming(self):
        self.assertIsNone(hamming.compare("", "a"))

    def test_001_hamming(self):
        self.assertIsNone(hamming.compare("a", "ab"))

    def test_002_hamming(self):
        self.assertEqual(hamming.compare("a", "a"), 0)

    def test_003_hamming(self):
        self.assertEqual(hamming.compare("a", "b"), 1)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
