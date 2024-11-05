quantity = int(input())
days_left = int(input())

days_shopping = 0
spirit_points = 0
total_cost = 0

while days_left > 0:
    days_shopping += 1

    if days_shopping % 11 == 0:
        quantity += 2

    if days_shopping % 2 == 0:
        spirit_points += 5
        total_cost += quantity * 2

    if days_shopping % 3 == 0:
        spirit_points += 13
        total_cost += quantity * 5 + quantity * 3

    if days_shopping % 5 == 0:
        spirit_points += 17
        total_cost += quantity * 15

        if days_shopping % 3 == 0:
            spirit_points  += 30
    # The cat ruining:
    if days_shopping % 10 == 0:
        spirit_points -= 20
        total_cost += 23

    if days_shopping % 10 == 0 and days_left == 1:
        spirit_points -= 30

    days_left -= 1

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_points}")
