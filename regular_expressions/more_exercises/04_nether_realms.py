import re

demons = input()

split_pattern = r'[,\s]+'
demons = sorted(re.split(split_pattern, demons))

for demon in demons:
    total_health = 0
    base_damage = 0

    char_pattern = r'[a-zA-Z]'
    char_matches = re.findall(char_pattern, demon)
    for ch in char_matches:
        total_health += ord(ch)

    digit_pattern = r'[-+]?\d+(?:\.\d+)?'
    digit_matches = re.findall(digit_pattern, demon)
    for digit in digit_matches:
        base_damage += float(digit)


    symbol_pattern = r'[/*]'
    symbol_matches = re.findall(symbol_pattern, demon)
    for symbol in symbol_matches:
        if symbol == '*':
            base_damage *= 2
        elif symbol == '/':
            base_damage /= 2

    print(f"{demon} - {total_health} health, {base_damage:.2f} damage")
