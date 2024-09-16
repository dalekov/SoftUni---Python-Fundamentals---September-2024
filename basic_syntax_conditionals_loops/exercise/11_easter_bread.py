budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = (price_flour * 1.25) * 0.25 # Milk used in one loaf.

price_bread = price_flour + price_eggs + price_milk

bread_count = 0
eggs_received = 0

while budget - price_bread > 0:
    budget -= price_bread

    bread_count += 1
    eggs_received += 3
    # Every third bread, we lose (bread_count - 2) eggs
    if bread_count % 3 == 0:
        eggs_received -= (bread_count - 2)

print(f"You made {bread_count} loaves of Easter bread! Now you have {eggs_received} eggs and {budget:.2f}BGN left.")

