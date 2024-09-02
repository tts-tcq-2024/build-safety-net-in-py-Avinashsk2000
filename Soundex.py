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
    # Return "0000" for empty input (single decision point)
    if not name:
        return "0000"

    # Convert the name to uppercase and map to soundex codes
    name = name.upper()
    first_letter = name[0]

    # Generate soundex codes for the rest of the name
    codes = map(get_soundex_code, name[1:])

    # Remove consecutive duplicates using groupby, and filter out '0's
    filtered_codes = [key for key, _ in groupby(codes) if key != 0]

    # Combine the first letter with the filtered codes
    soundex = [first_letter] + filtered_codes

    # Return the first four characters, padded if necessary
    return ''.join(str(code) for code in soundex[:4]).ljust(4, '0')


