from itertools import groupby

def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Use '0' for characters not in the mapping

def generate_soundex(name):
    # Edge case for empty name
    if not name:
        return "0000"

    # Start with the first letter capitalized
    first_letter = name[0].upper()

    # Generate codes for the rest of the name, filter out zeros, and remove consecutive duplicates
    soundex_codes = ''.join(str(get_soundex_code(c)) for c in name[1:].upper() if c.isalpha())
    filtered_codes = ''.join(k for k, _ in groupby(soundex_codes) if k != '0')

    # Form the Soundex code by combining the first letter and processed codes
    soundex = (first_letter + filtered_codes)[:4].ljust(4, '0')

    return soundex
