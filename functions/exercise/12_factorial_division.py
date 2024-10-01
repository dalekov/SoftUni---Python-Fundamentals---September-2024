first_number = int(input())
second_number = int(input())

def factorial_div(a, b):
    factorial_a = 1
    factorial_b = 1
    for i in range(1, a + 1):
        factorial_a *= i

    for j in range(1, b + 1):
        factorial_b *= j

    return f"{factorial_a / factorial_b:.2f}"

print(factorial_div(first_number, second_number))