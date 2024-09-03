import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        """Test handling of empty input."""
        self.assertEqual(generate_soundex(""), "0000")

    def test_single_character(self):
        """Test handling of single character input."""
        self.assertEqual(generate_soundex("A"), "A000")

    def test_basic_name(self):
        """Test a basic South Indian male name with no repeated or adjacent codes."""
        self.assertEqual(generate_soundex("Raghav"), "R210")

    def test_case_insensitivity(self):
        """Test that the function is case-insensitive."""
        self.assertEqual(generate_soundex("Yashwanth"), generate_soundex("yashwanth"))

    def test_padding_to_four_digits(self):
        """Test that the output is always padded to four digits."""
        self.assertEqual(generate_soundex("G"), "G000")

    def test_trimming_to_four_digits(self):
        """Test that the output is trimmed to four digits."""
        self.assertEqual(generate_soundex("Shivakumar"), "S125")

    def test_non_alphabetic_characters(self):
        """Test that non-alphabetic characters are ignored."""
        self.assertEqual(generate_soundex("Ravi@#$"), "R100")

    def test_names_with_spaces(self):
        """Test South Indian male names with spaces."""
        self.assertEqual(generate_soundex("Arvind Rao"), "A615")
        self.assertEqual(generate_soundex("Sandeep  Prasad"), "S531")  # Multiple spaces

    def test_south_indian_name_with_special_characters(self):
        """Test South Indian male names with special characters and numbers."""
        self.assertEqual(generate_soundex("Manoj@123"), "M520")

if __name__ == '__main__':
    unittest.main()
