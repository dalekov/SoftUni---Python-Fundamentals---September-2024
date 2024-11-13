import re
bought_furniture = []
total = 0
while True:
    command = input()
    if command == "Purchase":
        print("Bought furniture:")
        for furniture in bought_furniture:
            print(furniture)
        print(f"Total money spend: {total:.2f}")
        break


    regex = r'>>([a-zA-Z]+)<<(\d+(\.\d+)?)!(\d+)'
    match = re.findall(regex, command)

    if match:
        furniture = match[0][0]
        bought_furniture.append(furniture)
        price = match[0][1]
        if '.' in price:
            price = float(price)
        else:
            price = int(price)

        quantity = int(match[0][3])

        total += price * quantity


