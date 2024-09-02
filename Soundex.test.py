import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    
if __name__ == '__main__':
    unittest.main()
    
