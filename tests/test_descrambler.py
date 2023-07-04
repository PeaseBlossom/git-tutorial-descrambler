import unittest
from descrambler import *


class TestDescrambler(unittest.TestCase):
    """
    Contains tests for the descrambler package.
    """

    def test_descrambler1(self):
        input_lines = ['\n']
        expected_lines = ['\n']
        output_lines = descrambler1.descramble(input_lines)
        self.assertEqual(expected_lines, output_lines)

    def test_descrambler12(self):
        input_lines = ['Mo dayr Meskiwyynzha']
        expected_lines = ['My dear Miskowaanzhe']
        output_lines = descrambler12.descramble(input_lines)
        self.assertEqual(expected_lines, output_lines)


if __name__ == '__main__':
    unittest.main()
