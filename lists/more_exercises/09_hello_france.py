items = input().split("|")
budget = float(input())

budget_before = budget
money_from_sales = 0
MAX_PRICE_CLOTHES = 50
MAX_PRICE_SHOES = 35
MAX_PRICE_ACC = 20.50

bought_items = []
output_list = [] # List to store the prices after markup

TRAIN_TICKET = 150

for item in items:
    item_type, price = item.split("->")
    price = float(price)

    if budget >= price:
        if (item_type == "Clothes" and price > MAX_PRICE_CLOTHES) or (item_type == "Shoes" and price > MAX_PRICE_SHOES) or (item_type == "Accessories" and price > MAX_PRICE_ACC):
            continue
        else:
            budget -= price
            bought_items.append(item)

for item in bought_items:
    item_type, price = item.split("->")
    price = float(price)
    price *= 1.4
    output_list.append(price)
    budget += price # We add the price we have sold the item for to the total budget


for el in output_list:
    print(f"{el:.2f}", end=" ")

print(f"\nProfit: {budget - budget_before:.2f}")

if budget >= TRAIN_TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")
