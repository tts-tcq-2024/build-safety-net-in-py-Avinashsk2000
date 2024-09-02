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
    
    # Create a list of soundex codes, removing duplicates and '0' values
    codes = [get_soundex_code(c) for c in name]
    unique_codes = [code for code in codes if code != '0']

    # Initialize soundex with the first letter
    soundex = [name[0].upper()]
    
    # Add unique codes, avoiding consecutive duplicates
    soundex.extend(code for code in unique_codes[1:] if code != soundex[-1])
    
    # Ensure the final soundex code is 4 characters long
    return ''.join(soundex)[:4].ljust(4, '0')
