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
    name = name.upper()

    if not name:
        return "0000"

    # Create the soundex code from the name
    soundex = [name[0]]

    soundex.extend(
        get_soundex_code(c)
        for c in name[1:]
    )

    # Remove consecutive duplicates
    soundex = [soundex[i] for i in range(len(soundex)) if i == 0 or soundex[i] != soundex[i-1]]

    # Return soundex code padded to 4 characters
    return "".join(str(code) for code in soundex[:4]).ljust(4, "0")
