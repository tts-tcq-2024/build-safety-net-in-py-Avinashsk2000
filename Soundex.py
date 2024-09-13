from itertools import groupby

def get_soundex_code(c):
    """Map characters to Soundex codes."""
    c = c.upper()
    mapping = {
        'B': 1, 'F': 1, 'P': 1, 'V': 1,
        'C': 2, 'G': 2, 'J': 2, 'K': 2, 'Q': 2, 'S': 2, 'X': 2, 'Z': 2,
        'D': 3, 'T': 3,
        'L': 4,
        'M': 5, 'N': 5,
        'R': 6
    }
    return mapping.get(c, 0)

def filter_non_alphabet(char):
    """Filter out non-alphabetic characters."""
    return char.isalpha()

def map_to_soundex_code(char):
    """Map a character to its Soundex code."""
    return get_soundex_code(char)

def remove_consecutive_duplicates(codes):
    """Remove consecutive duplicate Soundex codes."""
    return [key for key, _ in groupby(codes)]

def process_name(input):
    """Process the input by filtering, mapping, and removing duplicates."""
    filtered_name = filter(filter_non_alphabet, input[1:])
    mapped_codes = map(map_to_soundex_code, filtered_name)
    filtered_codes = filter(lambda x: x != 0, mapped_codes)
    return remove_consecutive_duplicates(filtered_codes)

def build_soundex_code(input, unique_codes):
    """Build the final Soundex code with the first letter and mapped Soundex codes."""
    return (input[0].upper() + ''.join(map(str, unique_codes)))[:4].ljust(4, '0')

def generate_soundex(input):
    """Generate the Soundex code for a given name."""
    if not input:
        return "0000"
    unique_codes = process_name(input)
    return build_soundex_code(input, unique_codes)
