import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_regular_name(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Tymczak"), "T522")

    def test_ignore_vowels_and_special_characters(self):
        self.assertEqual(generate_soundex("O'Brien"), "O165")
        self.assertEqual(generate_soundex("Hannah"), "H500")

    def test_case_insensitivity(self):
        self.assertEqual(generate_soundex("Robert"), generate_soundex("robert"))
        self.assertEqual(generate_soundex("Smith"), generate_soundex("sMiTh"))

    def test_repeated_characters(self):
        self.assertEqual(generate_soundex("Smee"), "S500")  # Adjacent 'M' and 'E' ignored
        self.assertEqual(generate_soundex("Pfister"), "P236")  # Adjacent 'F' treated as one

    def test_longer_name_truncation(self):
        self.assertEqual(generate_soundex("Washington"), "W252")  # Should truncate to 4 characters
        self.assertEqual(generate_soundex("Jackson"), "J250")  # Should pad with zeroes

    def test_mixed_case_input(self):
        self.assertEqual(generate_soundex("MacDonald"), "M235")
        self.assertEqual(generate_soundex("macdonald"), "M235")

    def test_special_characters(self):
        self.assertEqual(generate_soundex("123"), "1000")  # Should return first letter followed by zeros
        self.assertEqual(generate_soundex("@#*"), "0000")  # Non-alphabetic characters only

if __name__ == '__main__':
    unittest.main()
