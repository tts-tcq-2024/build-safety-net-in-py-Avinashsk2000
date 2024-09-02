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
    # Combined initialization and empty check
    name = name.upper()
    if not name:  # 1st decision point
        return ""

    soundex = name[0]  # Start with the first letter
    prev_code = get_soundex_code(soundex)
    length = 1

    for char in name[1:]:  # 2nd decision point (loop)
        code = get_soundex_code(char)
        if code != prev_code and code != '0':  # 3rd decision point (combined check)
            soundex += code
            prev_code = code
            length += 1
        if length == 4:  # Exit when length is reached
            break

    return soundex.ljust(4, '0')  # Pad with zeros to make length 4
