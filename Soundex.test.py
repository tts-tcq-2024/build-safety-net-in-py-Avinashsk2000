import unittest
from Soundex import generate_soundex

class TestSoundexBasic(unittest.TestCase):
    """Tests for basic Soundex functionality."""

    def test_empty_input(self):
        self.assertEqual(generate_soundex(""), "0000")

    def test_single_letter(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_common_name(self):
        self.assertEqual(generate_soundex("Raghav"), "R020")

    def test_case_independence(self):
        self.assertEqual(generate_soundex("Avinash"), generate_soundex("avinash"))


class TestSoundexPaddingAndTrimming(unittest.TestCase):
    """Tests for padding and trimming of Soundex code."""

    def test_zero_padding(self):
        self.assertEqual(generate_soundex("G"), "G000")

    def test_cut_to_four_characters(self):
        self.assertEqual(generate_soundex("Avi"), "A100")


class TestSoundexSpecialCharacters(unittest.TestCase):
    """Tests handling of special characters and non-alphabetic input."""

    def test_ignoring_non_letters(self):
        self.assertEqual(generate_soundex("Ravi@#$"), "R130")

    def test_name_with_spaces(self):
        self.assertEqual(generate_soundex("Arvind Rao"), "A653")
        self.assertEqual(generate_soundex("Sandeep  Prasad"), "S531") 

    def test_special_chars_and_digits(self):
        self.assertEqual(generate_soundex("Manoj@123"), "M520")

class TestSoundexEdgeCases(unittest.TestCase):
    """Tests for edge cases and unexpected input."""

    def test_number_in_name(self):
        self.assertEqual(generate_soundex("avina2"), "A150")

    def test_all_same_consonant_name(self):
        self.assertEqual(generate_soundex("Shashank"), "S520")

    def test_name_with_hyphens(self):
        self.assertEqual(generate_soundex("Hari-Prasad"), "H612")


if __name__ == '__main__':
    unittest.main()
