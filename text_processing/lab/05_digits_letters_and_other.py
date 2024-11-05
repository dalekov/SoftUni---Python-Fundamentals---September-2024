string = input()

digits = []
letters = []
other = []

for ch in string:
    if ch.isdigit():
        digits.append(ch)
    elif ch.isalpha():
        letters.append(ch)
    else:
        other.append(ch)

print(''.join(digits))
print(''.join(letters))
print(''.join(other))