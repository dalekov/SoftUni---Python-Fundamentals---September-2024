def get_longest_string(string1, string2):
    return string1 if len(string1) > len(string2) else string2

def get_shortest_string(string1, string2):
    return string1 if len(string1) < len(string2) else string2

string_1, string_2 = input().split()

total = 0
if len(string_1) == len(string_2):
    for i in range(len(string_1)):
        total += ord(string_1[i]) * ord(string_2[i])
else:
    longest_string = get_longest_string(string_1, string_2)
    shortest_string = get_shortest_string(string_1, string_2)

    for i in range(len(longest_string)):
        if i <= len(shortest_string) - 1:
            total += ord(longest_string[i]) * ord(shortest_string[i])
        else:
            total += ord(longest_string[i])

print(total)
