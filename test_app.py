import unittest
from script import print_phrase_words, get_length_phrase
from io import StringIO
import sys

class TestPrintPhraseWords(unittest.TestCase):
    def test_print_phrase_words(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_phrase_words("Today I'm very happy because I'm moving towards 2000 mo per month")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Today\nI'm\nvery\nhappy\nbecause\nI'm\nmoving\ntowards\n2000\nmo\nper\nmonth\n")

class TestGetLengthPhrase(unittest.TestCase):
    def test_get_length_phrase(self):
        # Test case 1: Check length of a simple phrase
        self.assertEqual(get_length_phrase("Hello world"), 2)

        # Test case 2: Check length of a phrase with multiple words
        self.assertEqual(get_length_phrase("This is a test"), 4)

        # Test case 3: Check length of an empty phrase
        self.assertEqual(get_length_phrase(""), 0)

        # Test case 4: Check length of a phrase with special characters
        self.assertEqual(get_length_phrase("Hello! How are you?"), 4)

if __name__ == '__main__':
    unittest.main()