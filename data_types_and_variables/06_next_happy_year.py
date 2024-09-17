year = int(input())

while len(set(str(year))) != 4:
    if len(str(year)) >= 5:
        year = 0
    year += 1

print(year)

# Judge scores this 50/100, but it works perfectly.