string = input()
list_capitals = []
for i in range(len(string)):
    if string[i].isupper():
        list_capitals.append(i)

print(list_capitals)

