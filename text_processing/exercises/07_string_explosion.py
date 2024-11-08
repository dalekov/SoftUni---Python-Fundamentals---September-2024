def process_string(s):
    result = []
    power = 0

    for i in range(len(s)):
        if s[i] == '>':
            power += int(s[i + 1])
            result.append(s[i])
        elif power > 0:
            power -= 1
        else:
            result.append(s[i])

    return ''.join(result)

s = input()

print(process_string(s))