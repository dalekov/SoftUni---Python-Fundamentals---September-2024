key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}


а
obtained = False

while not obtained:
    farm = input().split()

    for entry in range(0, len(farm), 2):
        quantity = int(farm[entry])
        material = farm[entry + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                if material == "shards":
                    print("Shadowmourne obtained!")
                elif material == "fragments":
                    print("Valanyr obtained!")
                elif material == "motes":
                    print("Dragonwrath obtained!")
                key_materials[material] -= 250
                obtained = True
                break
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity

for material in ("shards", "fragments", "motes"):
    print(f"{material}: {key_materials[material]}")

for key, value in junk.items():
    print(f"{key}: {value}")