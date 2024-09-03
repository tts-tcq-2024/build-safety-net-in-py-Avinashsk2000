import unittest
from Soundex import generate_soundex
from parameterized import parameterized

class TestSoundex(unittest.TestCase):
    """Test for the Soundex function using parameterized inputs."""

    @parameterized.expand([
        # Test handling of an empty input string
        ("Empty input", "", "0000"),

        # Test handling of a single letter input
        ("Single letter", "A", "A000"),

        # Test case insensitivity
        ("Case insensitivity", "Yashwanth", "Y253"),
        ("Case insensitivity - lowercase", "yashwanth", "Y253"),

        # Test common names
        ("Typical name - Raghavendra", "Raghavendra", "R216"),
        ("Typical name - Vishwanath", "Vishwanath", "V253"),

        # Test padding to ensure four-character output
        ("Padding output", "G", "G000"),

        # Test trimming to ensure four-character output
        ("Trim output", "Balachandran", "B422"),

        # Test handling non-alphabetic characters
        ("Non-alphabetic characters", "A!@#$", "A000"),
        ("Non-alphabetic mixed with letters", "Raj123", "R200"),

        # Test names with spaces
        ("Names with spaces", "Anil Kumar", "A524"),
        ("Names with multiple spaces", "Anil  Kumar", "A524"),

        # Test numeric and special characters are ignored
        ("Numbers in name", "R2D2", "R300"),
        ("Special characters in name", "Ch@ndr@k@nth", "C536")
    ])
    def test_generate_soundex(self, name, input_name, expected_output):
        """
        Parameterized test for the generate_soundex function.

        Arguments:
            name (str): A description of the test case.
            input_name (str): The input name to generate Soundex for.
            expected_output (str): The expected Soundex output.
        """
        # Check if the Soundex function returns the expected output
        self.assertEqual(generate_soundex(input_name), expected_output)

if __name__ == '__main__':
    unittest.main()
