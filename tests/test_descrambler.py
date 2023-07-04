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

    def test_descrambler6(self):
        input_lines = ['Daarest Blue-ba-de-dae,\n']
        expected_lines = ['Dearest Blue-da-ba-dee,\n']
        output_lines = descrambler1.descramble(input_lines)
        self.assertEqual(expected_lines, output_lines)


if __name__ == '__main__':
    unittest.main()
