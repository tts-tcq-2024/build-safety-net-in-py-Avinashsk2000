import unittest
from Soundex import generate_soundex

class TestSoundexBasic(unittest.TestCase):
    """Tests for basic Soundex functionality."""

    def test_empty_string_returns_0000(self):
        """
        Test: Empty input should return '0000'.
        Explanation: No letters in the input, so it's padded with zeros.
        """
        self.assertEqual(generate_soundex(""), "0000")

    def test_single_letter_returns_letter_and_zeros(self):
        """
        Test: Single letter 'A' should return 'A000'.
        Explanation: The first letter is kept, followed by three zeros since no consonants remain.
        """
        self.assertEqual(generate_soundex("A"), "A000")

    def test_common_name_raghav_returns_r210(self):
        """
        Test: Name 'Raghav' becomes 'R210'.
        Explanation: 
        - 'R' is kept as the first letter.
        - 'g', 'h', 'v' map to Soundex digits '2', '1', and '0', respectively.
        - Vowels 'a' are ignored.
        """
        self.assertEqual(generate_soundex("Raghav"), "R210")

    def test_case_independence_returns_same_code(self):
        """
        Test: Case-insensitive comparison for 'Avinash' and 'avinash'.
        Explanation: The Soundex code should be identical regardless of case.
        """
        self.assertEqual(generate_soundex("Avinash"), generate_soundex("avinash"))


class TestSoundexPaddingAndTrimming(unittest.TestCase):
    """Tests for padding and trimming of Soundex code."""


    def test_short_name_padded_to_four_characters(self):
        """
        Test: Name 'Avi' becomes 'A100'.
        Explanation: 
        - 'A' is kept.
        - 'v' maps to '1', and there's no more consonant, so zeros are added to make it four characters.
        """
        self.assertEqual(generate_soundex("Avi"), "A100")


class TestSoundexSpecialCharacters(unittest.TestCase):
    """Tests handling of special characters and non-alphabetic input."""

    def test_special_characters_ignored_in_name(self):
        """
        Test: Name 'Ravi@#$' becomes 'R100'.
        Explanation: 
        - Special characters are ignored.
        - 'R' is kept, 'v' maps to '1', and no more consonants follow, so zeros pad the result.
        """
        self.assertEqual(generate_soundex("Ravi@#$"), "R100")

    def test_spaces_ignored_in_multi_word_name(self):
        """
        Test: Name 'Arvind Rao' becomes 'A615', 'Sandeep Prasad' becomes 'S531'.
        Explanation: 
        - Spaces are ignored.
        - 'Arvind' maps to 'A615' with vowels ignored.
        - 'Sandeep' maps to 'S531', combining consonant codes across both first and last names.
        """
        self.assertEqual(generate_soundex("Arvind Rao"), "A615")
        self.assertEqual(generate_soundex("Sandeep  Prasad"), "S531")

    def test_special_characters_and_digits_ignored(self):
        """
        Test: Name 'Manoj@123' becomes 'M520'.
        Explanation: 
        - Special characters and digits are ignored.
        - 'M' is kept, 'n', 'j' map to '5' and '2', 'o' is ignored, 'h' maps to '0'.
        """
        self.assertEqual(generate_soundex("Manoj@123"), "M520")


class TestSoundexEdgeCases(unittest.TestCase):
    """Tests for edge cases and unexpected input."""

    def test_numbers_in_name_are_ignored(self):
        """
        Test: Name 'avina2' becomes 'A150'.
        Explanation: 
        - The number '2' is ignored.
        - 'A' is kept, and the rest of the consonants map to '150'.
        """
        self.assertEqual(generate_soundex("avina2"), "A150")

    def test_name_with_repeated_consonants(self):
        """
        Test: Name 'Shashank' becomes 'S252'.
        Explanation: 
        - Repeated consonants like 'h' are ignored.
        - 'S' is kept, 'h' and 'k' map to '2', and 'sh' produces '5'.
        """
        self.assertEqual(generate_soundex("Shashank"), "S252")

    def test_name_with_hyphens_ignored(self):
        """
        Test: Name 'Hari-Prasad' becomes 'H616'.
        Explanation: 
        - Hyphens are ignored.
        - 'H' is kept, and consonants 'r', 'p', and 's' map to '6', '1', and '6' respectively.
        """
        self.assertEqual(generate_soundex("Hari-Prasad"), "H616")


if __name__ == '__main__':
    unittest.main()
