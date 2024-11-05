n = int(input())
CAPACITY = 255
total_liters = 0

for i in range(1, n + 1):
    liters_poured = int(input())
    total_liters += liters_poured

    if (total_liters > CAPACITY):
        print("Insufficient capacity!")
        total_liters -= liters_poured
        continue
else:
    print(total_liters)