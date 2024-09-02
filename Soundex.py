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
    # Handle empty name upfront
    if not name:
        return "0000"
    
    # Prepare the initial soundex list with the first character
    name = name.upper()
    soundex = [name[0]]

    # Create a list of soundex codes, directly filtering out consecutive duplicates
    codes = list(map(get_soundex_code, name[1:]))
    filtered_codes = [code for i, code in enumerate(codes) if code != 0 and (i == 0 or code != codes[i - 1])]

    # Combine the first letter and the filtered codes
    soundex.extend(filtered_codes)

    # Return the first four characters, padded if necessary
    return "".join(str(code) for code in soundex[:4]).ljust(4, "0")
