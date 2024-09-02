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

def generate_soundex(name):
    # Return "0000" for empty input
    return "0000" if not name else ''.join(
        [name[0].upper()] +  # Start with the first letter in uppercase
        list(filter(lambda x: x != '0', map(str, [
            key for key, _ in groupby(map(get_soundex_code, name[1:].upper()))
        ])))   # Apply Soundex coding, remove duplicates, and filter out '0'
    )[:4].ljust(4, '0')
