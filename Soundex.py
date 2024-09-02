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
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def generate_soundex(name):
    if not name:  # 1st decision point
        return ""
    
    # Start with the first letter
    soundex = [name[0].upper()]
    prev_code = get_soundex_code(soundex[0])

    # Generate soundex codes for the rest of the name
    soundex_codes = (
        get_soundex_code(char)
        for char in name[1:].upper()
    )

    # Use filter to collect unique and valid codes, limiting to length of 4
    soundex += [
        code for code in soundex_codes
        if code != prev_code and code != '0'
    ][:3]  # Only take up to 3 additional codes

    # Return soundex code padded with zeros to ensure length of 4
    return ''.join(soundex).ljust(4, '0')
