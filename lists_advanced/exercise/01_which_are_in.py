sequence_1 = input().split(", ")
sequence_2 = input().split(", ")

result = []

for string in sequence_1:
    for string2 in sequence_2:
        if string in string2:
            if string not in result:
                result.append(string)

print(result)