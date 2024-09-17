n = int(input())

for num in range(1, n + 1):
    num = str(num)
    digit_sum = 0
    for digit in num:
        digit_sum += int(digit)

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")

