loot = input().split("|")

while True:
    command = input().split()

    if command[0] == "Yohoho!":
        if loot:
            total_sum = 0
            for item in loot:
                total_sum += len(item)

            print(f"Average treasure gain: {total_sum / len(loot):.2f} pirate credits.")
        else:
            print("Failed treasure hunt.")
        break

    if command[0] == "Loot":
        for item in command[1:]:
            if item not in loot:
                loot.insert(0, item)

    if command[0] == "Drop":
        index = int(command[1])

        if index <= len(loot) - 1:
            loot.append(loot.pop(index))

    if command[0] == "Steal":
        count = int(command[1])
        stolen_items = []

        for _ in range(min(count, len(loot))):
            stolen_items.append(loot.pop(-1))

        print(f"{', '.join(reversed(stolen_items))}")



