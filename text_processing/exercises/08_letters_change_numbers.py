strings = input().split()

total = 0
for string in strings:
    first_letter = string[0]
    last_letter = string[-1]

    number = int(string[1:len(string) - 1])

    if first_letter.isupper():
        number /= ord(first_letter.lower()) - 96
    else:
        number *= ord(first_letter) - 96

    if last_letter.isupper():
        number -= ord(last_letter.lower()) - 96
    else:
        number += ord(last_letter) - 96

    total += number

print(f"{total:.2f}")