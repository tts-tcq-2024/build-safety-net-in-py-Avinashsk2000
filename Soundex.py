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
    if not name:
        return ""

    soundex = name[0].upper() + ''.join(
        get_soundex_code(char) for char in name[1:]
        if (code := get_soundex_code(char)) != '0' and code != soundex[-1]
    )

    return (soundex[:4] if len(soundex) >= 4 else soundex.ljust(4, '0'))

