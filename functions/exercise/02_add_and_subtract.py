num1 = int(input())
num2 = int(input())
num3 = int(input())

def sum_numbers(a, b, c):
    return a + b


def subtract(a, b, c):
    return sum_numbers(a, b, c) - c

print(subtract(num1, num2, num3))