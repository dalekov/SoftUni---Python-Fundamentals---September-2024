number = int(input())

def perfect_number(x):
    is_perfect = False

    if x >= 0:
        positive_divisors = []

        for i in range(1, x):
            if x % i == 0:
                positive_divisors.append(i)

        if sum(positive_divisors) == x:
            is_perfect = True


    if is_perfect:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

print(perfect_number(number))


