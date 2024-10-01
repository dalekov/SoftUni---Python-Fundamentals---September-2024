num = int(input())


def sum_even_odd(num):
    num = str(num)

    sum_even = 0
    sum_odd = 0

    for digit in num:
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        elif int(digit) % 2 == 1:
            sum_odd += int(digit)

    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"

print(sum_even_odd(num))