resources = {}

while True:
    resource = input()

    if resource == 'stop':
        for resources, quantity in resources.items():
            print(f"{resources} -> {quantity}")
        break

    quantity = int(input())

    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

