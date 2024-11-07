string = input()

to_append = ''
output_string = ''

for i in range(len(string)):

    if string[i].isalpha():
        to_append += string[i]
    elif string[i].isdigit():
        repeat_times = int(string[i])
        output_string += (to_append.upper() * repeat_times)
        to_append = ''
    else:
        to_append += string[i]


unique = []
for i in range(len(output_string)):
    if output_string[i] not in unique:
        unique.append(output_string[i])

print(f"Unique symbols used: {len(unique)}")
print(output_string)