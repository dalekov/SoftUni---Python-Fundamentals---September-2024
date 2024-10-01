numbers = input().split()

def absolute_values():
    numbers_to_float = []
    for number in numbers:
        number = abs(float(number))
        numbers_to_float.append(number)

    print(numbers_to_float)

absolute_values()