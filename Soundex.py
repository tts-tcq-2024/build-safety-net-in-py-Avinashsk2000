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
    if not name:
        return "0000"

    # Lambda function for filtering and mapping soundex codes
    filter_and_map = lambda name: (
        str(code) for code, _ in groupby(
            filter(lambda x: x != 0, map(get_soundex_code, filter(str.isalpha, name)))
        )
    )

    # Generate soundex code
    return (
        name[0].upper() + ''.join(filter_and_map(name[1:]))
    )[:4].ljust(4, '0')
