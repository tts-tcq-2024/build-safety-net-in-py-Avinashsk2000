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
    name = name.upper()
    if not name:
        return "0000"
    
    # Start with the first letter
    soundex = [name[0]]

    # Generate soundex codes for the rest of the name
    prev_code = get_soundex_code(name[0])
    
    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex.append(code)
            prev_code = code

    # Return soundex code padded with zeros to ensure length of 4
    return (soundex[0] + ''.join(soundex[1:])[:3]).ljust(4, '0')
