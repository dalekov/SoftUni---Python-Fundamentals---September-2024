n = int(input())
ascii_value = 0
for i in range(1, n + 1):
    letter = input()
    ascii_value += ord(letter)

print(f"The sum equals: {ascii_value}")