gifts = input().split(" ")

index = None

while True:
    command = input()

    if command == "No Money":
        break

    parts = command.split()
    action = parts[0]
    item = parts[1]

    if action == "OutOfStock":
        gifts = [None if item == gift else gift for gift in gifts]  # Replace any element in the gift list that matches
        # with None.

    elif action == "Required":
        index = int(parts[2])

        if 0 <= index < len(gifts):  # Checks if index is valid
            gifts[index] = item

    elif action == "JustInCase":
        gifts[-1] = item  # Replace last gift with the current item

for gift in gifts:  # Print all elements, which are not None.
    if gift is not None:
        print(gift, end=" ")
