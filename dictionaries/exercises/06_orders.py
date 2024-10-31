products = {}

while True:
    command = input().split()

    if command[0] == "buy":
        break

    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in products:
        products.update({product: {"price": price, "quantity": quantity}})
    else:
        products[product]["price"] = price
        products[product]["quantity"] += quantity


for product in products:
    print(f"{product} -> {products[product]['price'] * products[product]['quantity']:.2f}")