import unittest
from script import print_phrase_words
from io import StringIO
import sys

class TestPrintPhraseWords(unittest.TestCase):
    def test_print_phrase_words(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_phrase_words("Today I'm very happy because I'm moving towards 2000 mo per month")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Today\nI'm\nvery\nhappy\nbecause\nI'm\nmoving\ntowards\n2000\nmo\nper\nmonth\n")

if __name__ == '__main__':
    unittest.main()