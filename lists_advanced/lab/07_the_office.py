def multiply(n):
    return n * 3

happiness = list(map(int, input().split()))
factor = int(input())

multiplied = list(map(multiply, happiness))

average_happiness = sum(multiplied) / len(multiplied)

happy_employees_filtered = [el for el in multiplied if el >= average_happiness]

if len(happy_employees_filtered) / len(multiplied) >= 0.5:
    print(f"Score: {len(happy_employees_filtered)}/{len(multiplied)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees_filtered)}/{len(multiplied)}. Employees are not happy!")
