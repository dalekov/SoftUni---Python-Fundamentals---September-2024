numbers = input().split()

def calculations(x):
    numbers_to_int = [int(num) for num in x]

    min_num = min(numbers_to_int)
    max_num = max(numbers_to_int)
    total = sum(numbers_to_int)

    return f"The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {total}"

print(calculations(numbers))