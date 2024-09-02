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
        """Test a basic name with no repeated or adjacent codes."""
        self.assertEqual(generate_soundex("Smith"), "S530")

    def test_case_insensitivity(self):
        """Test that the function is case-insensitive."""
        self.assertEqual(generate_soundex("Robert"), generate_soundex("robert"))

    def test_padding_to_four_digits(self):
        """Test that the output is always padded to four digits."""
        self.assertEqual(generate_soundex("R"), "R000")

    def test_trimming_to_four_digits(self):
        """Test that the output is trimmed to four digits."""
        self.assertEqual(generate_soundex("Rubinstein"), "R152")

    def test_non_alphabetic_characters(self):
        """Test that non-alphabetic characters are ignored."""
        self.assertEqual(generate_soundex("A!@#$"), "A000")

    def test_names_with_spaces(self):
        """Test names with spaces."""
        self.assertEqual(generate_soundex("John Smith"), "J525")
        self.assertEqual(generate_soundex("John  Smith"), "J525")  # Multiple spaces

if __name__ == '__main__':
    unittest.main()
