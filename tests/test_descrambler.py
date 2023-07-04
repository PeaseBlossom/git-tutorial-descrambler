import unittest
from descrambler import *


class TestDescrambler(unittest.TestCase):
    """
    Contains tests for the descrambler package.
    """


    def test_descrambler1(self):
        input_lines = ['My Dearizzle Moodizzle Indigo,\n']
        expected_lines = ['My Dear Mood Indigo,\n']

        output_lines = descrambler1.descramble(input_lines)
        self.assertEqual(expected_lines, output_lines)


if __name__ == '__main__':
    unittest.main()
