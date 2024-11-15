import re

total = 0

while True:
    line = input()

    if line == 'end of shift':
        print(f"Total income: {total:.2f}")
        break

    name_regex = r"%([A-Z][a-z]+)%"
    name_match = re.findall(name_regex, line)

    product_regex = r"<([\w]+)>"
    product_match = re.findall(product_regex, line)

    quantity_regex = r"\|(\d+)\|"
    quantity_match = re.findall(quantity_regex, line)

    price_regex = r"(\d+(\.\d{1,2})?)\$"
    price_match = re.findall(price_regex, line)

    if name_match and product_match and quantity_match and price_match:
        name = name_match[0]
        product = product_match[0]
        quantity = int(quantity_match[0])
        price = price_match[0][0]

        total_customer = quantity * float(price)
        total += total_customer

        print(f"{name}: {product} - {total_customer:.2f}")
