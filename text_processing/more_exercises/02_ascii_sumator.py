first_char_ascii = ord(input())
second_char_ascii = ord(input())

string = input()
total = 0

for ch in string:
    if first_char_ascii < ord(ch) < second_char_ascii:
        total += ord(ch)

print(total)