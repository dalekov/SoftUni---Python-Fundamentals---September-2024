string = input()
power = 0
result = []

for i in range(len(string)):
    if string[i] == '>' and i + 1 < len(string):
        power = int(string[i + 1])
        result.append(string[i])
    elif power > 0:
        power -= 1
    else:
        result.append(string[i])

print(''.join(result))
