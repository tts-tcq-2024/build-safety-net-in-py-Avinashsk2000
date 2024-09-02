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

    # Initialize with the first character, always included
    soundex = [name[0].upper()]
    prev_code = get_soundex_code(soundex[0])

    for char in name[1:]:  # 2nd decision point (loop)
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:  # Combined check to avoid extra if statements
            soundex.append(code)
            prev_code = code
        if len(soundex) == 4:  # Exit condition managed within the loop
            break

    # Pad or truncate to ensure the soundex is exactly 4 characters
    return ''.join(soundex).ljust(4, '0')  # No additional decision point here

