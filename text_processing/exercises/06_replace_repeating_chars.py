string = input()

result = ""

for i in range(len(string)):
    if i == 0 or string[i] != string[i - 1]:
        result += string[i]

print(result)