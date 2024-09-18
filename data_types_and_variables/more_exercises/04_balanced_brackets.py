n = int(input())

count_opening = 0
count_closing = 0

output = ""

for i in range(1, n + 1):
    symbol = input()

    if symbol == '(':
        count_opening += 1
    elif symbol == ')':
        count_closing += 1

    if count_opening == count_closing:
        output = "BALANCED"
    else:
        output = "UNBALANCED"

print(output)