strings = input().split()

output = ""

for string in strings:
    n = len(string)
    output += n * string

print(output)
