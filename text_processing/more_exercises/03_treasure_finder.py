import re

keys = list(map(int, input().split()))

while True:
    string = input()
    decrypted_string = ''

    if string == 'find':
        break

    # Wrap around the keys list
    for i in range(len(string)):
        key_i = i % len(keys)
        key = keys[key_i]

        # Adding new char to decrypted string
        decrypted_string += chr(ord(string[i]) - key)

    # Patterns to look for treasure and cords
    pattern_treasure = r'&\w+\&' #enclosed in &
    pattern_coords = r'<\w+\>' #enclosed in <>

    match_treasure = re.findall(pattern_treasure, decrypted_string)
    match_coords = re.findall(pattern_coords, decrypted_string)

    treasure = match_treasure[0].strip('&')
    coords = match_coords[0].strip('<').strip('>')

    print(f'Found {treasure} at {coords}')
