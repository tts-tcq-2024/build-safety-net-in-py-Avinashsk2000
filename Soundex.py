from itertools import groupby

def get_soundex_code(c):
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

def filter_non_alpha(char):
    """Filter out non-alphabetic characters."""
    return char.isalpha()

def map_to_soundex_code(char):
    """Map a character to its Soundex code."""
    return get_soundex_code(char)

def remove_consecutive_duplicates(codes):
    """Remove consecutive duplicate Soundex codes."""
    return [key for key, _ in groupby(codes)]

def generate_soundex(name):
    if not name:
        return "0000"

    # Apply the processing steps
    filtered_name = filter(filter_non_alpha, name[1:])
    mapped_codes = map(map_to_soundex_code, filtered_name)
    filtered_codes = filter(lambda x: x != 0, mapped_codes)
    unique_codes = remove_consecutive_duplicates(filtered_codes)

    # Build the final Soundex code
    return (
        name[0].upper() + ''.join(map(str, unique_codes))
    )[:4].ljust(4, '0')
