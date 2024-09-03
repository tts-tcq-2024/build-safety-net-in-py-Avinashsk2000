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
    # Use a one-liner to handle empty input and generate Soundex
    return (
        "0000" if not name else (
            (name[0].upper() +  # Start with the first letter
             ''.join(
                 str(code) for code, _ in groupby(
                     filter(lambda x: x != 0, map(get_soundex_code, filter(str.isalpha, name[1:])))
                 )
             )
            )[:4].ljust(4, '0')
        )
    )
