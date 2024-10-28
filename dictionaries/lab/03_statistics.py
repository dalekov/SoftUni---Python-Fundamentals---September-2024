bakery = {}

while True:
    command = input().split(": ")

    if command[0] == "statistics":
        print("Products in stock:")
        for key, value in bakery.items():
            print(f"- {key}: {value}")
        print(f"Total Products: {len(bakery)}")
        print(f"Total Quantity: {sum(bakery.values())}")
        break

    else:
        key = command[0]
        quantity = int(command[1])

        if key not in bakery:
            bakery[key] = quantity
        else:
            bakery[key] += quantity


