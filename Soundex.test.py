import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        """Test that an empty string returns an empty result."""
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        """Test that a single character returns the character followed by three zeros."""
        self.assertEqual(generate_soundex("A"), "A000")

    def test_repeated_characters(self):
        """Test that repeated characters with the same soundex code are handled correctly."""
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Pfister"), "P236")
    
    def test_varying_case(self):
        """Test that varying cases return the same result."""
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("ROBERT"), "R163")
        self.assertEqual(generate_soundex("robert"), "R163")

    def test_name_with_vowels(self):
        """Test names with vowels between consonants."""
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Ashcroft"), "A261")

    def test_edge_cases(self):
        """Test edge cases like special characters and non-mapped characters."""
        self.assertEqual(generate_soundex("H123"), "H000")
        self.assertEqual(generate_soundex("O'Neill"), "O540")
        self.assertEqual(generate_soundex("Washington"), "W252")

    def test_exactly_four_characters(self):
        """Test that names producing exactly four characters are handled properly."""
        self.assertEqual(generate_soundex("Euler"), "E460")
        self.assertEqual(generate_soundex("Smith"), "S530")

    def test_long_names(self):
        """Test that long names are trimmed correctly."""
        self.assertEqual(generate_soundex("Jackson"), "J250")
        self.assertEqual(generate_soundex("Johnson"), "J525")
    
    def test_padding_with_zeros(self):
        """Test that names that are too short are padded with zeros."""
        self.assertEqual(generate_soundex("Lee"), "L000")
        self.assertEqual(generate_soundex("G"), "G000")

if __name__ == '__main__':
    unittest.main()
