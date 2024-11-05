number = float(input())


if number == 0:
    print("zero")
elif number > 0:
    if number < 1:
        print("small positive")
    elif 1 <= number <= 1_000_000:
        print("positive")
    elif number > 1_000_000:
        print("large positive")
elif number < 0:
    if abs(number) < 1:
        print("small negative")
    elif 1 <= abs(number) <= 1_000_000:
        print("negative")
    elif abs(number) > 1_000_000:
        print("large negative")
