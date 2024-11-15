import re
n = int(input())

attacked_planets = []
destroyed_planets = []

for i in range(n):
    letters = ['s', 't', 'a', 'r']
    encrypted_message = input()

    key = 0
    for ch in encrypted_message:
        if ch.lower() in letters:
            key += 1

    decrypted_message = ""
    for ch in encrypted_message:
        if ch.isdigit():
            ch_new = str(int(ch) - key)
            if int(ch_new) < 0:
                ch_new = '-'
        else:
            ch_new = chr(ord(ch) - key)
        decrypted_message += ch_new

    planet_regex = r'@([a-zA-Z]+)'
    planet_match = re.findall(planet_regex, decrypted_message)

    population_regex = r':(\d+)'
    population_match = re.findall(population_regex, decrypted_message)

    attack_type_regex = r'!(A|D)!'
    attack_type_match = re.findall(attack_type_regex, decrypted_message)

    soldier_count_regex = r'->(\d+)'
    soldier_count_match = re.findall(soldier_count_regex, decrypted_message)

    if planet_match and population_match and attack_type_match and soldier_count_match:
        if attack_type_match[0] == 'A':
            attacked_planets.append(planet_match[0])
        elif attack_type_match[0] == 'D':
            destroyed_planets.append(planet_match[0])

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
