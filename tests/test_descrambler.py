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

    def test_descrambler10(self):
        input_lines = ['inside. live to place a me give Yours events. not structures, are Letters']
        expected_lines = ['Letters are structures, not events. Yours give me a place to live inside.']
        output_lines = descrambler10.descramble(input_lines)
        self.assertEqual(expected_lines, output_lines)


if __name__ == '__main__':
    unittest.main()
