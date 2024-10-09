electrons = int(input())

result = [0] * 10

while electrons > 0:
    for i in range(1, len(result) + 1):
        max_electrons = 2 * (i ** 2)

        if electrons >= max_electrons:
            result[i - 1] += max_electrons
            electrons -= max_electrons
        else:
            result[i - 1] += electrons
            electrons -= electrons

        if electrons <= 0:
            break


result = list(filter(lambda x: x != 0, result))
print(result)

