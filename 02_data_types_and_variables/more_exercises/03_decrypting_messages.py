key = int(input())
n = int(input())

output = ""
for i in range(1, n + 1):
    letter = input()
    output += chr(ord(letter) + key)

print(output)